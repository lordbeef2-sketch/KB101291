# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxwlan_driver_api_tests.cpp sha256=bbc2a3df5f949497415678d5279d170ba9e7f55084d54e1b4d32627b946c6ae6 bytes=78053 -->
## FILE: source/tests/system/nirfmxwlan_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxwlan_driver_api_tests.cpp`
- sha256: `bbc2a3df5f949497415678d5279d170ba9e7f55084d54e1b4d32627b946c6ae6`
- bytes: 78053

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxwlan/nirfmxwlan_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"
#include "waveform_helpers.h"

using namespace ::testing;
using namespace nirfmxwlan_grpc;
namespace client = nirfmxwlan_grpc::experimental::client;
namespace instr_client = nirfmxinstr_grpc::experimental::client;
namespace nirfsa_client = nirfsa_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

typedef ::google::protobuf::int32 int32;
typedef ::google::protobuf::int64 int64;
typedef double float64;

constexpr auto PXI_5663E = "5663E";
constexpr auto RISING_EDGE_DETECTION_FAILED_WARNING = 379206;
constexpr auto RISING_EDGE_DETECTION_FAILED_WARNING_STR = "Rising edge detection failed for the acquired waveform";
constexpr auto EVM_CHIPS_MUST_BE_300_WARNING = 685353;
constexpr auto EVM_CHIPS_MUST_BE_300_WARNING_STR = "Number of available payload chips for EVM measurements";
constexpr auto INCORRECT_TYPE_ERROR = -380251;
constexpr auto INCORRECT_TYPE_ERROR_STR = "Incorrect data type specified";

class NiRFmxWLANDriverApiTests : public Test {
 protected:
  NiRFmxWLANDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxWLAN::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxWLANDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxWLAN::Stub>& stub() const
  {
    return stub_;
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxWLAN::Stub> stub_;
};

std::string get_comma_seperated_string(const std::vector<std::string>& array_of_names)
{
  int name_index = 0;
  int comma_index = 0;
  std::stringstream output;
  while (name_index < array_of_names.size()) {
    output << array_of_names[name_index];
    if (++name_index != array_of_names.size()) {
      output << ',';
    }
  }
  return output.str();
}

InitializeResponse init(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, resource_name, options);
}

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  return init(stub, model, "FakeDevice");
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto response = init(stub, model, resource_name);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
}

nidevice_grpc::Session init_instr_session(const instr_client::StubPtr& stub, const char* resource_name)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + PXI_5663E;
  auto response = instr_client::initialize(stub, std::string(resource_name), options);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

nirfsa_grpc::InitWithOptionsResponse init_rfsa(const nirfsa_client::StubPtr& stub, const std::string& resource_name)
{
  return nirfsa_client::init_with_options(stub, resource_name, false, false, "Simulate=1, DriverSetup=Model:5663E");
}

nidevice_grpc::Session init_analysis_session(const client::StubPtr& stub)
{
  auto options = std::string("Analysisonly = 1; MaxNumWfms:8");
  auto response = client::initialize(stub, "", options);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

std::vector<nidevice_grpc::NIComplexNumberF32> complex_f32_array(
    std::vector<float> reals,
    std::vector<float> imaginaries)
{
  return complex_array<float, nidevice_grpc::NIComplexNumberF32>(reals, imaginaries);
}

std::vector<nidevice_grpc::NIComplexNumber> complex_number_array(
    std::vector<double> reals,
    std::vector<double> imaginaries)
{
  return complex_array<double, nidevice_grpc::NIComplexNumber>(reals, imaginaries);
}

TEST_F(NiRFmxWLANDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxWLANDriverApiTests, InitializeFromNIRFSA_Close_Succeeds)
{
  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  auto init_rfsa_response = init_rfsa(rfsa_stub, "Sim");
  EXPECT_RESPONSE_SUCCESS(init_rfsa_response);
  auto init_response = client::initialize_from_nirfsa_session(stub(), init_rfsa_response.vi());
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxWLANDriverApiTests, OFDMModAccTXPCompositeFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_TXP | MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_averaging(stub(), session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::txp_cfg_averaging(stub(), session, "", TXP_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::txp_cfg_maximum_measurement_interval(stub(), session, "", 1e-3));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto ofdm_mod_acc_fetch_composite_rmsevm_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0));
  const auto txp_fetch_measurement_response = client::txp_fetch_measurement(stub(), session, "", 10.0);
  EXPECT_WARNING(RISING_EDGE_DETECTION_FAILED_WARNING, RISING_EDGE_DETECTION_FAILED_WARNING_STR, session, txp_fetch_measurement_response);

  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_data_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean());
  EXPECT_LT(0.0, txp_fetch_measurement_response.average_power_mean());
  EXPECT_LT(0.0, txp_fetch_measurement_response.peak_power_maximum());
}

TEST_F(NiRFmxWLANDriverApiTests, SemFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_mask_type(stub(), session, "", SEM_MASK_TYPE_STANDARD));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_span(stub(), session, "", SEM_SPAN_AUTO_TRUE, 66.0e6));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response.absolute_power());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response.relative_power());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(2454, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(2454, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(2454, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(2454, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxWLANDriverApiTests, SEMCustomMaskFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_OFFSETS = 3;
  std::vector<float64> offset_start_frequency{9e06, 11e06, 20e06};
  std::vector<float64> offset_stop_frequency{11e06, 20e06, 40e06};
  std::vector<int> offset_sideband{SEM_OFFSET_SIDEBAND_BOTH, SEM_OFFSET_SIDEBAND_BOTH, SEM_OFFSET_SIDEBAND_BOTH};
  std::vector<float64> relative_limit_start{0.0, -20.0, -28.0};
  std::vector<float64> relative_limit_stop{-20.0, -28.0, -40.0};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_mask_type(stub(), session, "", SEM_MASK_TYPE_CUSTOM));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_number_of_offsets(stub(), session, "", NUMBER_OF_OFFSETS));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_frequency_array(stub(), session, "", offset_start_frequency, offset_stop_frequency, offset_sideband));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_relative_limit_array(stub(), session, "", relative_limit_start, relative_limit_stop));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  int32 array_size = sem_fetch_upper_offset_margin_array_response.measurement_status_size();
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response.absolute_power());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response.relative_power());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(3, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(3, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(2974, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(2974, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(2974, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(2974, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxWLANDriverApiTests, TXPFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 10e-3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_TXP, true));
  EXPECT_SUCCESS(session, client::txp_cfg_maximum_measurement_interval(stub(), session, "", 1e-3));
  EXPECT_SUCCESS(session, client::txp_cfg_averaging(stub(), session, "", TXP_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto txp_fetch_power_trace_response = client::txp_fetch_power_trace(stub(), session, "", 10.0);
  EXPECT_WARNING(RISING_EDGE_DETECTION_FAILED_WARNING, RISING_EDGE_DETECTION_FAILED_WARNING_STR, session, txp_fetch_power_trace_response);
  const auto txp_fetch_measurement_response = client::txp_fetch_measurement(stub(), session, "", 10.0);
  EXPECT_WARNING(RISING_EDGE_DETECTION_FAILED_WARNING, RISING_EDGE_DETECTION_FAILED_WARNING_STR, session, txp_fetch_measurement_response);

  EXPECT_GT(0.0, txp_fetch_power_trace_response.x0());
  EXPECT_LT(0.0, txp_fetch_power_trace_response.dx());
  EXPECT_EQ(25250, txp_fetch_power_trace_response.power_size());
  EXPECT_EQ(25250, txp_fetch_power_trace_response.power().size());
  EXPECT_LT(0.0, txp_fetch_power_trace_response.power(0));
  EXPECT_LT(0.0, txp_fetch_measurement_response.average_power_mean());
  EXPECT_LT(0.0, txp_fetch_measurement_response.peak_power_maximum());
}

TEST_F(NiRFmxWLANDriverApiTests, DSSSModAccFromExample_FetchData_DataLooksReasonable)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_instr_session(instr_stub, resource_name);
  EXPECT_SUCCESS(session, instr_client::cfg_frequency_reference(instr_stub, session, "", nirfmxinstr_grpc::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_B));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_DSSSMODACC, true));
  EXPECT_SUCCESS(session, client::dsss_mod_acc_cfg_measurement_length(stub(), session, "", 0, 1000));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE, NIRFMXWLAN_INT32_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE_RECTANGULAR));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_DSSSMODACC_PULSE_SHAPING_FILTER_PARAMETER, 0.50));
  EXPECT_SUCCESS(session, client::dsss_mod_acc_cfg_evm_unit(stub(), session, "", DSSSMODACC_EVM_UNIT_PERCENTAGE));
  EXPECT_SUCCESS(session, client::dsss_mod_acc_cfg_averaging(stub(), session, "", DSSSMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto dsss_mod_acc_fetch_evm_response = client::dsss_mod_acc_fetch_evm(stub(), session, "", 10.0);
  EXPECT_WARNING(EVM_CHIPS_MUST_BE_300_WARNING, EVM_CHIPS_MUST_BE_300_WARNING_STR, session, dsss_mod_acc_fetch_evm_response);
  const auto dsss_mod_acc_fetch_ppdu_information_response = client::dsss_mod_acc_fetch_ppdu_information(stub(), session, "", 10.0);
  EXPECT_WARNING(EVM_CHIPS_MUST_BE_300_WARNING, EVM_CHIPS_MUST_BE_300_WARNING_STR, session, dsss_mod_acc_fetch_ppdu_information_response);
  const auto dsss_mod_acc_fetch_iq_impairments_response = client::dsss_mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  EXPECT_WARNING(EVM_CHIPS_MUST_BE_300_WARNING, EVM_CHIPS_MUST_BE_300_WARNING_STR, session, dsss_mod_acc_fetch_iq_impairments_response);
  const auto dsss_mod_acc_fetch_evm_per_chip_mean_trace_response = client::dsss_mod_acc_fetch_evm_per_chip_mean_trace(stub(), session, "", 10.0);
  EXPECT_WARNING(EVM_CHIPS_MUST_BE_300_WARNING, EVM_CHIPS_MUST_BE_300_WARNING_STR, session, dsss_mod_acc_fetch_evm_per_chip_mean_trace_response);
  const auto dsss_mod_acc_fetch_constellation_trace_response = client::dsss_mod_acc_fetch_constellation_trace(stub(), session, "", 10.0);
  EXPECT_WARNING(EVM_CHIPS_MUST_BE_300_WARNING, EVM_CHIPS_MUST_BE_300_WARNING_STR, session, dsss_mod_acc_fetch_constellation_trace_response);

  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_response.rms_evm_mean());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_response.peak_evm_80211_2016_maximum());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_response.peak_evm_80211_2007_maximum());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_response.peak_evm_80211_1999_maximum());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_response.frequency_error_mean());
  EXPECT_NE(0.0, dsss_mod_acc_fetch_evm_response.chip_clock_error_mean());
  EXPECT_EQ(0, dsss_mod_acc_fetch_evm_response.number_of_chips_used());
  EXPECT_EQ(3, dsss_mod_acc_fetch_ppdu_information_response.data_modulation_format());
  EXPECT_EQ(0, dsss_mod_acc_fetch_ppdu_information_response.payload_length());
  EXPECT_EQ(1, dsss_mod_acc_fetch_ppdu_information_response.preamble_type());
  EXPECT_EQ(0, dsss_mod_acc_fetch_ppdu_information_response.locked_clocks_bit());
  EXPECT_EQ(0, dsss_mod_acc_fetch_ppdu_information_response.header_crc_status());
  EXPECT_EQ(0, dsss_mod_acc_fetch_ppdu_information_response.psdu_crc_status());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_iq_impairments_response.iq_origin_offset_mean());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_iq_impairments_response.iq_gain_imbalance_mean());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_iq_impairments_response.iq_quadrature_error_mean());
  EXPECT_EQ(0.0, dsss_mod_acc_fetch_evm_per_chip_mean_trace_response.x0());
  EXPECT_EQ(1, dsss_mod_acc_fetch_evm_per_chip_mean_trace_response.dx());
  EXPECT_EQ(0, dsss_mod_acc_fetch_evm_per_chip_mean_trace_response.evm_per_chip_mean_size());
  EXPECT_EQ(0, dsss_mod_acc_fetch_evm_per_chip_mean_trace_response.evm_per_chip_mean().size());
  EXPECT_EQ(0, dsss_mod_acc_fetch_constellation_trace_response.actual_array_size());
}

TEST_F(NiRFmxWLANDriverApiTests, OFDMModAccFromExample_FetchData_DataLooksReasonable)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_instr_session(instr_stub, resource_name);
  EXPECT_SUCCESS(session, instr_client::cfg_frequency_reference(instr_stub, session, "", nirfmxinstr_grpc::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e06));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_frequency_error_estimation_method(stub(), session, "", OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_amplitude_tracking_enabled(stub(), session, "", OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_phase_tracking_enabled(stub(), session, "", OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_symbol_clock_error_correction_enabled(stub(), session, "", OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_channel_estimation_type(stub(), session, "", OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_averaging(stub(), session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto ofdm_mod_acc_fetch_composite_rmsevm_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_numberof_symbols_used_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_numberof_symbols_used(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_frequency_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_frequency_error_mean(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_symbol_clock_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_symbol_clock_error_mean(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_iq_impairments_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_iq_impairments(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_ppdu_type_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_ppdu_type(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_mcs_index_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_mcs_index(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_guard_interval_type_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_guard_interval_type(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_lsig_parity_check_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_lsig_parity_check_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_sigcrc_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_sigcrc_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_sigbcrc_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_sigbcrc_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_pilot_constellation_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_pilot_constellation_trace(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_data_constellation_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_data_constellation_trace(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace(stub(), session, "", 10.0));

  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_data_rms_evm_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean());
  EXPECT_EQ(16, ofdm_mod_acc_fetch_numberof_symbols_used_response.number_of_symbols_used());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_frequency_error_mean_response.frequency_error_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_symbol_clock_error_mean_response.symbol_clock_error_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_iq_impairments_response.relative_iq_origin_offset_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_iq_impairments_response.iq_gain_imbalance_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_iq_impairments_response.iq_quadrature_error_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_iq_impairments_response.absolute_iq_origin_offset_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_iq_impairments_response.iq_timing_skew_mean());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_ppdu_type_response.ppdu_type());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_guard_interval_type_response.guard_interval_type());
  EXPECT_EQ(-1, ofdm_mod_acc_fetch_sigcrc_status_response.sig_crc_status());
  EXPECT_EQ(-1, ofdm_mod_acc_fetch_sigbcrc_status_response.sig_b_crc_status());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response.pilot_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response.pilot_constellation(0).imaginary());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response.data_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response.data_constellation(0).imaginary());
  EXPECT_EQ(-26, ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response.x0());
  EXPECT_EQ(1, ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response.dx());
  EXPECT_EQ(53, ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean_size());
  EXPECT_EQ(53, ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean().size());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_chain_rmsevm_per_subcarrier_mean_trace_response.chain_rms_evm_per_subcarrier_mean(0));
}

TEST_F(NiRFmxWLANDriverApiTests, OFDMModAccMIMOFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_DEVICES = 2;
  const auto NUMBER_OF_FREQUENCY_SEGMENTS = 1;
  const auto NUMBER_OF_RECEIVE_CHAINS = 2;
  std::vector<std::string> resource_names = {"RFSA1", "RFSA2"};
  std::string comma_separated_resource_name = get_comma_seperated_string(resource_names);
  std::vector<float64> center_frequency_array{5.180000e9, 5.260000e9};
  std::vector<std::string> selected_ports_strings = {"", ""};
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_session(stub(), PXI_5663E, comma_separated_resource_name);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_PXI_CLK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_number_of_frequency_segments_and_receive_chains(stub(), session, "", NUMBER_OF_FREQUENCY_SEGMENTS, NUMBER_OF_RECEIVE_CHAINS));
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; ++i) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, segment_string_response.selector_string_out(), center_frequency_array[i]));
  }
  for (int i = 0; i < NUMBER_OF_DEVICES; ++i) {
    auto port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    selected_ports_strings[i] = port_string_response.selector_string_out();
    port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, port_string_response.selector_string_out(), 0.0));
    EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, port_string_response.selector_string_out(), 0.0));
  }
  std::string selected_ports_string_comma_separated = get_comma_seperated_string(selected_ports_strings);
  EXPECT_SUCCESS(session, client::cfg_selected_ports_multiple(stub(), session, "", selected_ports_string_comma_separated));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_N));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e06));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_frequency_error_estimation_method(stub(), session, "", OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_amplitude_tracking_enabled(stub(), session, "", OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_phase_tracking_enabled(stub(), session, "", OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_symbol_clock_error_correction_enabled(stub(), session, "", OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_channel_estimation_type(stub(), session, "", OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_averaging(stub(), session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED, NIRFMXWLAN_INT32_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto ofdm_mod_acc_fetch_composite_rmsevm_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_numberof_symbols_used_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_numberof_symbols_used(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_ppdu_type_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_ppdu_type(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_guard_interval_type_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_guard_interval_type(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_lsig_parity_check_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_lsig_parity_check_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_sigcrc_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_sigcrc_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_sigbcrc_status_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_sigbcrc_status(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_number_of_users_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_number_of_users(stub(), session, "", 10.0));
  const auto number_of_users = ofdm_mod_acc_fetch_number_of_users_response.number_of_users();
  std::vector<int32> mcs_index_vec(number_of_users);
  std::vector<int32> number_of_space_time_streams_vec(number_of_users);
  std::vector<int32> space_time_stream_offset_vec(number_of_users);
  auto number_of_stream_results = INT_MIN;
  for (int i = 0; i < number_of_users; i++) {
    const auto user_string_response = EXPECT_SUCCESS(session, client::build_user_string(stub(), "", i));
    const auto ofdm_mod_acc_fetch_mcs_index_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_mcs_index(stub(), session, user_string_response.selector_string_out(), 10.0));
    mcs_index_vec[i] = ofdm_mod_acc_fetch_mcs_index_response.mcs_index();
    const auto ofdm_mod_acc_fetch_number_of_space_time_streams_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_number_of_space_time_streams(stub(), session, user_string_response.selector_string_out(), 10.0));
    number_of_space_time_streams_vec[i] = ofdm_mod_acc_fetch_number_of_space_time_streams_response.number_of_space_time_streams();
    space_time_stream_offset_vec[i] = GET_ATTR_I32(session, user_string_response.selector_string_out(), NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_RESULTS_SPACE_TIME_STREAM_OFFSET);
    if ((space_time_stream_offset_vec[i] + number_of_space_time_streams_vec[i]) > number_of_stream_results) {
      number_of_stream_results = space_time_stream_offset_vec[i] + number_of_space_time_streams_vec[i];
    }
  }
  std::vector<OFDMModAccFetchFrequencyErrorMeanResponse> ofdm_mod_acc_fetch_frequency_error_mean_response_vec;
  std::vector<OFDMModAccFetchSymbolClockErrorMeanResponse> ofdm_mod_acc_fetch_symbol_clock_error_mean_response_vec;
  std::vector<std::vector<OFDMModAccFetchStreamRMSEVMResponse>> ofdm_mod_acc_fetch_stream_rmsevm_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTraceResponse>> ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<OFDMModAccFetchPilotConstellationTraceResponse>> ofdm_mod_acc_fetch_pilot_constellation_trace_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<OFDMModAccFetchDataConstellationTraceResponse>> ofdm_mod_acc_fetch_data_constellation_trace_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<OFDMModAccFetchCrossPowerResponse>> ofdm_mod_acc_fetch_cross_power_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<OFDMModAccFetchIQImpairmentsResponse>> ofdm_mod_acc_fetch_iq_impairments_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; i++) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    ofdm_mod_acc_fetch_frequency_error_mean_response_vec.push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_frequency_error_mean(stub(), session, segment_string_response.selector_string_out(), 10.0)));
    ofdm_mod_acc_fetch_symbol_clock_error_mean_response_vec.push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_symbol_clock_error_mean(stub(), session, segment_string_response.selector_string_out(), 10.0)));
    for (int j = 0; j < number_of_stream_results; j++) {
      const auto stream_string_response = EXPECT_SUCCESS(session, client::build_stream_string(stub(), segment_string_response.selector_string_out(), j));
      ofdm_mod_acc_fetch_stream_rmsevm_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_stream_rmsevm(stub(), session, stream_string_response.selector_string_out(), 10.0)));
      ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace(stub(), session, stream_string_response.selector_string_out(), 10.0)));
      ofdm_mod_acc_fetch_pilot_constellation_trace_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_pilot_constellation_trace(stub(), session, stream_string_response.selector_string_out(), 10.0)));
      ofdm_mod_acc_fetch_data_constellation_trace_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_data_constellation_trace(stub(), session, stream_string_response.selector_string_out(), 10.0)));
    }
    for (int j = 0; j < NUMBER_OF_RECEIVE_CHAINS; j++) {
      const auto chain_string_response = EXPECT_SUCCESS(session, client::build_chain_string(stub(), segment_string_response.selector_string_out(), j));
      ofdm_mod_acc_fetch_cross_power_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_cross_power(stub(), session, chain_string_response.selector_string_out(), 10.0)));
      ofdm_mod_acc_fetch_iq_impairments_response_vec[i].push_back(EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_iq_impairments(stub(), session, chain_string_response.selector_string_out(), 10.0)));
    }
  }

  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_data_rms_evm_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean());
  EXPECT_NE(0, ofdm_mod_acc_fetch_numberof_symbols_used_response.number_of_symbols_used());
  EXPECT_EQ(2, ofdm_mod_acc_fetch_ppdu_type_response.ppdu_type());
  EXPECT_EQ(-1, ofdm_mod_acc_fetch_lsig_parity_check_status_response.l_sig_parity_check_status());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_sigcrc_status_response.sig_crc_status());
  EXPECT_EQ(-1, ofdm_mod_acc_fetch_sigbcrc_status_response.sig_b_crc_status());
  EXPECT_EQ(1, number_of_users);
  for (int i = 0; i < number_of_users; i++) {
    EXPECT_LT(0, mcs_index_vec[i]);
    EXPECT_EQ(0, space_time_stream_offset_vec[i]);
  }
  EXPECT_LE(number_of_users, number_of_stream_results);
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_frequency_error_mean_response_vec[0].frequency_error_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_symbol_clock_error_mean_response_vec[0].symbol_clock_error_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_stream_rmsevm_response_vec[0][0].stream_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_stream_rmsevm_response_vec[0][0].stream_data_rms_evm_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_stream_rmsevm_response_vec[0][0].stream_pilot_rms_evm_mean());
  EXPECT_EQ(-28.0, ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[0][0].x0());
  EXPECT_EQ(1.0, ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[0][0].dx());
  EXPECT_NE(0, ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[0][0].stream_rms_evm_per_subcarrier_mean_size());
  EXPECT_NE(0, ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[0][0].stream_rms_evm_per_subcarrier_mean().size());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_stream_rmsevm_per_subcarrier_mean_trace_response_vec[0][0].stream_rms_evm_per_subcarrier_mean(0));
  EXPECT_NE(0, ofdm_mod_acc_fetch_pilot_constellation_trace_response_vec[0][0].pilot_constellation().size());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response_vec[0][0].pilot_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response_vec[0][0].pilot_constellation(0).imaginary());
  EXPECT_NE(0, ofdm_mod_acc_fetch_data_constellation_trace_response_vec[0][0].data_constellation().size());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response_vec[0][0].data_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response_vec[0][0].data_constellation(0).imaginary());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_cross_power_response_vec[0][0].cross_power_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_iq_impairments_response_vec[0][0].relative_iq_origin_offset_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_iq_impairments_response_vec[0][0].iq_gain_imbalance_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_iq_impairments_response_vec[0][0].iq_quadrature_error_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_iq_impairments_response_vec[0][0].absolute_iq_origin_offset_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_iq_impairments_response_vec[0][0].iq_timing_skew_mean());
}

TEST_F(NiRFmxWLANDriverApiTests, OFDMModAccSpeedOptimizedFromExample_FetchData_DataLooksReasonable)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_instr_session(instr_stub, resource_name);
  EXPECT_SUCCESS(session, instr_client::cfg_frequency_reference(instr_stub, session, "", nirfmxinstr_grpc::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AG));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e06));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED, NIRFMXWLAN_INT32_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_PPDU_TYPE, NIRFMXWLAN_INT32_OFDM_PPDU_TYPE_NON_HT));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_HEADER_DECODING_ENABLED, NIRFMXWLAN_INT32_OFDM_HEADER_DECODING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_MCS_INDEX, 0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_GUARD_INTERVAL_TYPE, NIRFMXWLAN_INT32_OFDM_GUARD_INTERVAL_TYPE_1_4));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_LTF_SIZE, NIRFMXWLAN_INT32_OFDM_LTF_SIZE_4X));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_frequency_error_estimation_method(stub(), session, "", OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_amplitude_tracking_enabled(stub(), session, "", OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_phase_tracking_enabled(stub(), session, "", OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_symbol_clock_error_correction_enabled(stub(), session, "", OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_averaging(stub(), session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_BURST_START_DETECTION_ENABLED, NIRFMXWLAN_INT32_OFDMMODACC_BURST_START_DETECTION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED, NIRFMXWLAN_INT32_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto ofdm_mod_acc_fetch_composite_rmsevm_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_numberof_symbols_used_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_numberof_symbols_used(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_frequency_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_frequency_error_mean(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_symbol_clock_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_symbol_clock_error_mean(stub(), session, "", 10.0));

  EXPECT_LT(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_rms_evm_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_data_rms_evm_mean());
  EXPECT_LT(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean());
  EXPECT_EQ(16, ofdm_mod_acc_fetch_numberof_symbols_used_response.number_of_symbols_used());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_frequency_error_mean_response.frequency_error_mean());
  EXPECT_GT(0.0, ofdm_mod_acc_fetch_symbol_clock_error_mean_response.symbol_clock_error_mean());
}

TEST_F(NiRFmxWLANDriverApiTests, OFDMModAccTriggerBasedPPDUFromExample_FetchData_DataLooksReasonable)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_instr_session(instr_stub, resource_name);
  EXPECT_SUCCESS(session, instr_client::cfg_frequency_reference(instr_stub, session, "", nirfmxinstr_grpc::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.412e9));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_AX));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e06));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_MCS_INDEX, 0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_RU_SIZE, 26));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_RU_OFFSET_MRU_INDEX, 0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_GUARD_INTERVAL_TYPE, NIRFMXWLAN_INT32_OFDM_GUARD_INTERVAL_TYPE_1_4));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_LTF_SIZE, NIRFMXWLAN_INT32_OFDM_LTF_SIZE_4X));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_PE_DISAMBIGUITY, 0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDM_PPDU_TYPE, NIRFMXWLAN_INT32_OFDM_PPDU_TYPE_SU));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE, NIRFMXWLAN_INT32_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE_LIMIT1));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_averaging(stub(), session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto ofdm_mod_acc_fetch_composite_rmsevm_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_unused_tone_error_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_unused_tone_error(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_unused_tone_error_margin_per_ru_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_unused_tone_error_margin_per_ru(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_frequency_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_frequency_error_mean(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_frequency_error_ccdf10_percent_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_frequency_error_ccdf10_percent(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_symbol_clock_error_mean_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_symbol_clock_error_mean(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_ppdu_type_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_ppdu_type(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_pilot_constellation_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_pilot_constellation_trace(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_data_constellation_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_data_constellation_trace(stub(), session, "", 10.0));
  const auto ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response = EXPECT_SUCCESS(session, client::ofdm_mod_acc_fetch_unused_tone_error_mean_trace(stub(), session, "", 10.0));

  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_data_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_composite_rmsevm_response.composite_pilot_rms_evm_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_unused_tone_error_response.unused_tone_error_margin());
  EXPECT_EQ(-1, ofdm_mod_acc_fetch_unused_tone_error_response.unused_tone_error_margin_ru_index());
  EXPECT_EQ(1, ofdm_mod_acc_fetch_unused_tone_error_margin_per_ru_response.unused_tone_error_margin_per_ru_size());
  EXPECT_EQ(1, ofdm_mod_acc_fetch_unused_tone_error_margin_per_ru_response.unused_tone_error_margin_per_ru().size());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_unused_tone_error_margin_per_ru_response.unused_tone_error_margin_per_ru(0));
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_frequency_error_mean_response.frequency_error_mean());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_symbol_clock_error_mean_response.symbol_clock_error_mean());
  EXPECT_EQ(3, ofdm_mod_acc_fetch_ppdu_type_response.ppdu_type());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response.pilot_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_pilot_constellation_trace_response.pilot_constellation(0).imaginary());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response.data_constellation(0).real());
  EXPECT_NE(0.0, ofdm_mod_acc_fetch_data_constellation_trace_response.data_constellation(0).imaginary());
  EXPECT_EQ(0.0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.x0());
  EXPECT_EQ(0.0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.dx());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.unused_tone_error_size());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.unused_tone_error().size());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.unused_tone_error_mask_size());
  EXPECT_EQ(0, ofdm_mod_acc_fetch_unused_tone_error_mean_trace_response.unused_tone_error_mask().size());
}

TEST_F(NiRFmxWLANDriverApiTests, SemMIMOFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_DEVICES = 2;
  const auto NUMBER_OF_FREQUENCY_SEGMENTS = 1;
  const auto NUMBER_OF_RECEIVE_CHAINS = 2;
  std::vector<std::string> resource_names = {"RFSA1", "RFSA2"};
  std::string comma_separated_resource_name = get_comma_seperated_string(resource_names);
  std::vector<float64> center_frequency_array{5.180000e9, 5.260000e9};
  std::vector<std::string> selected_ports_string{"", ""};
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_session(stub(), PXI_5663E, comma_separated_resource_name);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_PXI_CLK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_number_of_frequency_segments_and_receive_chains(stub(), session, "", NUMBER_OF_FREQUENCY_SEGMENTS, NUMBER_OF_RECEIVE_CHAINS));
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; ++i) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, segment_string_response.selector_string_out(), center_frequency_array[i]));
  }
  for (int i = 0; i < NUMBER_OF_DEVICES; ++i) {
    auto port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    selected_ports_string[i] = port_string_response.selector_string_out();
    port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, port_string_response.selector_string_out(), 0.0));
    EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, port_string_response.selector_string_out(), 0.0));
  }
  std::string selected_ports_string_comma_separated = get_comma_seperated_string(selected_ports_string);
  EXPECT_SUCCESS(session, client::cfg_selected_ports_multiple(stub(), session, "", selected_ports_string_comma_separated));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_N));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_mask_type(stub(), session, "", SEM_MASK_TYPE_STANDARD));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_span(stub(), session, "", SEM_SPAN_AUTO_TRUE, 66.0e6));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  std::vector<std::vector<SEMFetchCarrierMeasurementResponse>> sem_fetch_carrier_measurement_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<SEMFetchLowerOffsetMarginArrayResponse>> sem_fetch_lower_offset_margin_array_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<SEMFetchUpperOffsetMarginArrayResponse>> sem_fetch_upper_offset_margin_array_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<SEMFetchSpectrumResponse>> sem_fetch_spectrum_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; ++i) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    for (int j = 0; j < NUMBER_OF_RECEIVE_CHAINS; ++j) {
      const auto chain_string_response = EXPECT_SUCCESS(session, client::build_chain_string(stub(), segment_string_response.selector_string_out(), j));
      sem_fetch_carrier_measurement_response_vec[i].push_back(
          EXPECT_SUCCESS(session, client::sem_fetch_carrier_measurement(stub(), session, chain_string_response.selector_string_out(), 10.0)));
      sem_fetch_lower_offset_margin_array_response_vec[i].push_back(
          EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, chain_string_response.selector_string_out(), 10.0)));
      sem_fetch_upper_offset_margin_array_response_vec[i].push_back(
          EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, chain_string_response.selector_string_out(), 10.0)));
      sem_fetch_spectrum_response_vec[i].push_back(
          EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, chain_string_response.selector_string_out(), 10.0)));
    }
  }

  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response_vec[0][0].absolute_power());
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response_vec[0][0].relative_power());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].measurement_status_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].measurement_status().size());
  EXPECT_EQ(1, sem_fetch_lower_offset_margin_array_response_vec[0][0].measurement_status(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_frequency_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_frequency(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_absolute_power_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_absolute_power(0));
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_relative_power_size());
  EXPECT_EQ(4, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response_vec[0][0].margin_relative_power(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].measurement_status_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].measurement_status().size());
  EXPECT_EQ(1, sem_fetch_upper_offset_margin_array_response_vec[0][0].measurement_status(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_frequency_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_frequency(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_absolute_power_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_absolute_power(0));
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_relative_power_size());
  EXPECT_EQ(4, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response_vec[0][0].margin_relative_power(0));
  EXPECT_LT(0.0, sem_fetch_spectrum_response_vec[0][0].x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response_vec[0][0].dx());
  EXPECT_EQ(2454, sem_fetch_spectrum_response_vec[0][0].spectrum_size());
  EXPECT_EQ(2454, sem_fetch_spectrum_response_vec[0][0].spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response_vec[0][0].spectrum(0));
  EXPECT_EQ(2454, sem_fetch_spectrum_response_vec[0][0].composite_mask_size());
  EXPECT_EQ(2454, sem_fetch_spectrum_response_vec[0][0].composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response_vec[0][0].composite_mask(0));
}

TEST_F(NiRFmxWLANDriverApiTests, TXPMIMOFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_DEVICES = 2;
  const auto NUMBER_OF_FREQUENCY_SEGMENTS = 1;
  const auto NUMBER_OF_RECEIVE_CHAINS = 2;
  std::vector<std::string> resource_names = {"RFSA1", "RFSA2"};
  std::string comma_separated_resource_name = get_comma_seperated_string(resource_names);
  std::vector<float64> center_frequency_array{5.180000e9, 5.260000e9};
  std::vector<std::string> port_string = {"", ""};
  std::vector<std::string> selected_ports_string = {"", ""};
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  auto session = init_session(stub(), PXI_5663E, comma_separated_resource_name);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_PXI_CLK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_number_of_frequency_segments_and_receive_chains(stub(), session, "", NUMBER_OF_FREQUENCY_SEGMENTS, NUMBER_OF_RECEIVE_CHAINS));
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; ++i) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, segment_string_response.selector_string_out(), center_frequency_array[i]));
  }
  for (int i = 0; i < NUMBER_OF_DEVICES; ++i) {
    auto port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    selected_ports_string[i] = port_string_response.selector_string_out();
    port_string_response = EXPECT_SUCCESS(session, instr_client::build_port_string(instr_stub, "", "", resource_names[i], 0));
    port_string[i] = port_string_response.selector_string_out();
  }
  std::string selected_ports_string_comma_separated = get_comma_seperated_string(selected_ports_string);
  EXPECT_SUCCESS(session, client::cfg_selected_ports_multiple(stub(), session, "", selected_ports_string_comma_separated));
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_N));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 10e-3));
  for (int i = 0; i < NUMBER_OF_DEVICES; ++i) {
    EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, port_string[i], 0.0));
  }
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_TXP, true));
  EXPECT_SUCCESS(session, client::txp_cfg_maximum_measurement_interval(stub(), session, "", 1e-3));
  EXPECT_SUCCESS(session, client::txp_cfg_averaging(stub(), session, "", TXP_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  std::vector<std::vector<TXPFetchMeasurementResponse>> txp_fetch_measurement_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  std::vector<std::vector<TXPFetchPowerTraceResponse>> txp_fetch_power_trace_response_vec(NUMBER_OF_FREQUENCY_SEGMENTS);
  for (int i = 0; i < NUMBER_OF_FREQUENCY_SEGMENTS; ++i) {
    const auto segment_string_response = EXPECT_SUCCESS(session, client::build_segment_string(stub(), "", i));
    for (int j = 0; j < NUMBER_OF_RECEIVE_CHAINS; ++j) {
      // Note: using EXPECT_RESPONSE_SUCCESS here instead of EXPECT_SUCCESS because get_error() is
      // returning the text for RISING_EDGE_DETECTION_FAILED_WARNING
      const auto chain_string_response = client::build_chain_string(stub(), segment_string_response.selector_string_out(), j);
      EXPECT_RESPONSE_SUCCESS(chain_string_response);
      txp_fetch_measurement_response_vec[i].push_back(
          EXPECT_WARNING(
              RISING_EDGE_DETECTION_FAILED_WARNING, RISING_EDGE_DETECTION_FAILED_WARNING_STR, session,
              client::txp_fetch_measurement(stub(), session, chain_string_response.selector_string_out(), 10.0)));
      txp_fetch_power_trace_response_vec[i].push_back(
          EXPECT_WARNING(
              RISING_EDGE_DETECTION_FAILED_WARNING, RISING_EDGE_DETECTION_FAILED_WARNING_STR, session,
              client::txp_fetch_power_trace(stub(), session, chain_string_response.selector_string_out(), 10.0)));
    }
  }

  EXPECT_LT(0.0, txp_fetch_measurement_response_vec[0][0].average_power_mean());
  EXPECT_LT(0.0, txp_fetch_measurement_response_vec[0][0].peak_power_maximum());
  EXPECT_GT(0.0, txp_fetch_power_trace_response_vec[0][0].x0());
  EXPECT_LT(0.0, txp_fetch_power_trace_response_vec[0][0].dx());
  EXPECT_EQ(25250, txp_fetch_power_trace_response_vec[0][0].power_size());
  EXPECT_EQ(25250, txp_fetch_power_trace_response_vec[0][0].power().size());
  EXPECT_LT(0.0, txp_fetch_power_trace_response_vec[0][0].power(0));
}

TEST_F(NiRFmxWLANDriverApiTests, AnalyzeNWaveformsIQ_FetchData_DataLooksReasonable)
{
  const auto num_frequency_segments = 1;
  const auto num_receive_chains = 2;
  double centerFrequency[num_receive_chains] = {5.18e9, 5.26e9};
  auto session = init_analysis_session(stub());
  EXPECT_SUCCESS(session, client::cfg_number_of_frequency_segments_and_receive_chains(stub(), session, "", num_frequency_segments, num_receive_chains));
  for (int i = 0; i < num_frequency_segments; i++) {
    const auto build_segment_string_response = client::build_segment_string(stub(), "", i);
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, build_segment_string_response.selector_string_out(), centerFrequency[i]));
  }
  EXPECT_SUCCESS(session, client::cfg_standard(stub(), session, "", STANDARD_802_11_N));
  EXPECT_SUCCESS(session, client::cfg_channel_bandwidth(stub(), session, "", 20e6));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_measurement_length(stub(), session, "", 0, 16));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_frequency_error_estimation_method(stub(), session, "", OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_amplitude_tracking_enabled(stub(), session, "", OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_phase_tracking_enabled(stub(), session, "", OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_symbol_clock_error_correction_enabled(stub(), session, "", OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::ofdm_mod_acc_cfg_channel_estimation_type(stub(), session, "", OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE));
  // READ TDMS File
  auto waveforms = load_test_multiple_waveforms_data<float, nidevice_grpc::NIComplexNumberF32>("WLAN_80211n_20MHz_1Seg_2Chain_MIMO.json", 2);
  // Concatenate waveform data, two dimension array passed as one dimension array with size array determining where one starts and one stops.
  std::vector<float64> iq_x0{0, 0};
  std::vector<float64> iq_dx{0, 0};
  std::vector<int> iq_sizes{0, 0};
  std::vector<nidevice_grpc::NIComplexNumberF32> iq;
  for (int i = 0; i < num_receive_chains; i++) {
    auto waveform = waveforms[i];
    auto data = waveform.data;
    iq_x0[i] = waveform.t0;
    iq_dx[i] = waveform.dt;
    iq_sizes[i] = static_cast<int>(data.size());
    iq.insert(iq.end(), data.begin(), data.end());
  }

  // Analyze Waveforms
  EXPECT_SUCCESS(session, client::analyze_n_waveforms_iq(stub(), session, "", "", iq_x0, iq_dx, iq, iq_sizes, true));

  // Fetch Results and check they are reasonable
  const auto fetch_composite_response = client::ofdm_mod_acc_fetch_composite_rmsevm(stub(), session, "", 10.0);
  EXPECT_GT(0.0, fetch_composite_response.composite_rms_evm_mean());
  EXPECT_GT(0.0, fetch_composite_response.composite_data_rms_evm_mean());
  EXPECT_GT(0.0, fetch_composite_response.composite_pilot_rms_evm_mean());
}

// Note: there aren't any complex attributes
TEST_F(NiRFmxWLANDriverApiTests, SetAttributeComplex_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_ni_complex_double_array(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_REFERENCE_LEVEL, complex_number_array({1.2, 2.2}, {1e6, 1.01e6})));
}

// Note: there aren't any i8 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxWLANDriverApiTests, SetAttributeInt8_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_i8(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, 1));
  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_u8(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, 1));
  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_i8_array(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, {1, 0, -1, 0}));
  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_u8_array(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, {1, 0, 1, 0}));
}

// Note: there aren't any i16 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxWLANDriverApiTests, SetAttributeInt16_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_i16(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, -400));
  EXPECT_ERROR(
      INCORRECT_TYPE_ERROR, INCORRECT_TYPE_ERROR_STR, session,
      client::set_attribute_u16(stub(), session, "", NiRFmxWLANAttribute::NIRFMXWLAN_ATTRIBUTE_OFDM_DCM_ENABLED, 400));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxwlan_restricted_driver_api_tests.cpp sha256=d72af0b669de3742483c6ad3347d0c5e7e6d3a61edcc7e534ebc1cdd3cab4774 bytes=7498 -->
## FILE: source/tests/system/nirfmxwlan_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxwlan_restricted_driver_api_tests.cpp`
- sha256: `d72af0b669de3742483c6ad3347d0c5e7e6d3a61edcc7e534ebc1cdd3cab4774`
- bytes: 7498

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <thread>
#include <tuple>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxwlan/nirfmxwlan_client.h"
#include "nirfmxwlan_restricted/nirfmxwlan_restricted_client.h"
#include "rfmx_macros.h"
#include "waveform_helpers.h"

using namespace nirfmxwlan_grpc;
using namespace nirfmxwlan_restricted_grpc;
namespace client = nirfmxwlan_grpc::experimental::client;
namespace instr_client = nirfmxinstr_grpc::experimental::client;
namespace restricted_client = nirfmxwlan_restricted_grpc::experimental::client;
using namespace ::testing;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5841 = "5841";

class NiRFmxWLANRestrictedDriverApiTests : public ::testing::Test {
 protected:
  NiRFmxWLANRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxwlan_stub_(NiRFmxWLAN::NewStub(device_server_->InProcessChannel())),
        nirfmxwlan_restricted_stub_(NiRFmxWLANRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiRFmxWLANRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiRFmxWLAN::Stub>& stub()
  {
    return nirfmxwlan_stub_;
  }

  std::unique_ptr<NiRFmxWLANRestricted::Stub>& restricted_stub()
  {
    return nirfmxwlan_restricted_stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxWLAN::Stub> nirfmxwlan_stub_;
  std::unique_ptr<NiRFmxWLANRestricted::Stub> nirfmxwlan_restricted_stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, resource_name, options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto response = init(stub, model, resource_name);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

void configure_OFDMModAccFromExample(const instr_client::StubPtr& instr_stub, const nidevice_grpc::Session& session, const client::StubPtr& wlan_stub)
{
  EXPECT_RESPONSE_SUCCESS(instr_client::cfg_frequency_reference(instr_stub, session, "", nirfmxinstr_grpc::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_RESPONSE_SUCCESS(client::cfg_frequency(wlan_stub, session, "", 2.412e9));
  EXPECT_RESPONSE_SUCCESS(client::cfg_reference_level(wlan_stub, session, "", 0.0));
  EXPECT_RESPONSE_SUCCESS(client::cfg_external_attenuation(wlan_stub, session, "", 0.0));
  EXPECT_RESPONSE_SUCCESS(client::cfg_iq_power_edge_trigger(wlan_stub, session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 5e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_RESPONSE_SUCCESS(client::cfg_standard(wlan_stub, session, "", STANDARD_802_11_AG));
  EXPECT_RESPONSE_SUCCESS(client::cfg_channel_bandwidth(wlan_stub, session, "", 20e06));
  EXPECT_RESPONSE_SUCCESS(client::select_measurements(wlan_stub, session, "", MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_measurement_length(wlan_stub, session, "", 0, 16));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_frequency_error_estimation_method(wlan_stub, session, "", OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_amplitude_tracking_enabled(wlan_stub, session, "", OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_phase_tracking_enabled(wlan_stub, session, "", OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_symbol_clock_error_correction_enabled(wlan_stub, session, "", OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_channel_estimation_type(wlan_stub, session, "", OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE));
  EXPECT_RESPONSE_SUCCESS(client::ofdm_mod_acc_cfg_averaging(wlan_stub, session, "", OFDMMODACC_AVERAGING_ENABLED_FALSE, 10));
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
}

TEST_F(NiRFmxWLANRestrictedDriverApiTests, GetChannelListBehavior_ReturnsNonEmptyResult)
{
  const auto session = init_session(stub(), PXI_5841);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_OFDMMODACC, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto response = restricted_client::get_channel_list(restricted_stub(), session, "", 0);
  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(response.center_frequencies(), Not(IsEmpty()));
  EXPECT_THAT(response.channel_bandwidths(), Not(IsEmpty()));
  EXPECT_GT(response.actual_array_size(), 0);
}

TEST_F(NiRFmxWLANRestrictedDriverApiTests, OFDMModAccFromExample_FetchCommonPilotErrorTradeIndB_ResponseLooksReasonable)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  const auto session = init_session(stub(), PXI_5841);
  configure_OFDMModAccFromExample(instr_stub, session, stub());
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto response = restricted_client::ofdm_mod_acc_fetch_common_pilot_error_trace_ind_b(restricted_stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(0.0, response.x0());
  EXPECT_NE(0.0, response.dx());
  EXPECT_THAT(response.common_pilot_error_magnitude(), Not(IsEmpty()));
  EXPECT_THAT(response.common_pilot_error_phase(), Not(IsEmpty()));
}

TEST_F(NiRFmxWLANRestrictedDriverApiTests, OFDMModAccFromExample_NoiseCalibrate_Succeeds)
{
  char* resource_name = "RFSA";
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  const auto session = init_session(stub(), PXI_5841);
  configure_OFDMModAccFromExample(instr_stub, session, stub());
  std::vector<float64> center_frequency{2.412e9};
  std::vector<float64> channel_bandwidth{2.0e7};
  // Note that ofdm_mod_acc_noise_calibrate is non-public and requires setup with non-public attributes.
  const auto NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_CENTER_FREQUENCIES = 10502272;
  const auto NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_CHANNEL_BANDWIDTHS = 10502273;
  EXPECT_SUCCESS(session, client::set_attribute_f64_array(stub(), session, "", (nirfmxwlan_grpc::NiRFmxWLANAttribute)NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_CENTER_FREQUENCIES, center_frequency));
  EXPECT_SUCCESS(session, client::set_attribute_f64_array(stub(), session, "", (nirfmxwlan_grpc::NiRFmxWLANAttribute)NIRFMXWLAN_ATTRIBUTE_OFDMMODACC_CHANNEL_BANDWIDTHS, channel_bandwidth));
  
  EXPECT_SUCCESS(session, restricted_client::ofdm_mod_acc_noise_calibrate(restricted_stub(), session, "", 0));

  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxwlan_session_tests.cpp sha256=641b0a389b2bfec1f663fc7ef9b5b6d800d95dd600b29d652be942f0e3fd89b6 bytes=6976 -->
## FILE: source/tests/system/nirfmxwlan_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxwlan_session_tests.cpp`
- sha256: `641b0a389b2bfec1f663fc7ef9b5b6d800d95dd600b29d652be942f0e3fd89b6`
- bytes: 6976

````cpp
#include "device_server.h"
#include "nirfmxwlan/nirfmxwlan_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxwlan = nirfmxwlan_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxWLANSession = -380598;
const char* kRFmxWLANTestRsrc = "FakeDevice";
const char* kRFmxWLANOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxWLANTestSession = "SessionName";
const char* kRFmxWLANTestSessionTwo = "SessionTwoName";
const char* kRFmxWLANTestInvalidRsrc = "";

class NiRFmxWLANSessionTest : public ::testing::Test {
 protected:
  NiRFmxWLANSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxwlan_stub_(rfmxwlan::NiRFmxWLAN::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxWLANSessionTest() {}

  std::unique_ptr<rfmxwlan::NiRFmxWLAN::Stub>& GetStub()
  {
    return nirfmxwlan_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxwlan::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxwlan::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxwlan::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxwlan::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxwlan::NiRFmxWLAN::Stub> nirfmxwlan_stub_;
};

TEST_F(NiRFmxWLANSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxwlan::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSession, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxWLANSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxwlan::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxWLANSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxwlan::InitializeResponse response;
    call_initialize(kRFmxWLANTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxWLANSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxwlan::InitializeResponse init_response;
  call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSession, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxwlan::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxwlan::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxWLANSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxwlan::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSession, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxwlan::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxWLANSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxwlan::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxWLANSession);
}

TEST_F(NiRFmxWLANSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxwlan::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSession, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxWLANTestRsrc, kRFmxWLANOptionsString, kRFmxWLANTestSession, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxwlan::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxWLANSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfsa_driver_api_tests.cpp sha256=67e0a2d3605e535137727a6dce75b21ee14b2ba2c4df88a0f39588cc4052f074 bytes=24128 -->
## FILE: source/tests/system/nirfsa_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfsa_driver_api_tests.cpp`
- sha256: `67e0a2d3605e535137727a6dce75b21ee14b2ba2c4df88a0f39588cc4052f074`
- bytes: 24128

````cpp
#include <gmock/gmock.h>

#include <algorithm>
#include <nlohmann/json.hpp>

#include "device_server.h"
#include "niRFSAErrors.h"
#include "nirfsa/nirfsa_client.h"
#include "niscope/niscope_client.h"
#include "nitclk/nitclk_client.h"
#include "tests/utilities/test_helpers.h"

using namespace ::testing;
using namespace nirfsa_grpc;
namespace client = nirfsa_grpc::experimental::client;
namespace nitclk_client = nitclk_grpc::experimental::client;
namespace niscope_client = niscope_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";
const auto PXI_5603 = "5603";
const auto IVI_ATTRIBUTE_NOT_SUPPORTED_ERROR = 0xBFFA0012;
const auto REF_OUT_STR = "RefOut";

template <typename TResponse>
void EXPECT_SUCCESS(const TResponse& response)
{
  EXPECT_EQ(0, response.status());
}

class NiRFSADriverApiTests : public Test {
 protected:
  NiRFSADriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFSA::NewStub(device_server_->InProcessChannel()))
  {
  }

  virtual ~NiRFSADriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFSA::Stub>& stub() const
  {
    return stub_;
  }

  std::unique_ptr<nitclk_grpc::NiTClk::Stub> create_tclk_stub() const
  {
    return nitclk_grpc::NiTClk::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<niscope_grpc::NiScope::Stub> create_scope_stub() const
  {
    return niscope_grpc::NiScope::NewStub(device_server_->InProcessChannel());
  }

  void check_error(const nidevice_grpc::Session& session)
  {
    auto response = client::get_error(stub(), session);
    EXPECT_EQ("", std::string(response.error_description().c_str()));
  }

  void clear_error(const nidevice_grpc::Session& session)
  {
    auto response = client::clear_error(stub(), session);
    ni::tests::system::EXPECT_SUCCESS(response);
  }

  template <typename TResponse>
  void EXPECT_SUCCESS(const nidevice_grpc::Session& session, const TResponse& response)
  {
    ni::tests::system::EXPECT_SUCCESS(response);
    check_error(session);
  }

  void EXPECT_RFSA_ERROR(int32_t expected_error, const std::string& message_substring, const nidevice_grpc::experimental::client::grpc_driver_error& ex, const nidevice_grpc::Session& session)
  {
    EXPECT_DRIVER_ERROR_WITH_SUBSTR(ex, expected_error, message_substring);
    clear_error(session);
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFSA::Stub> stub_;
};

InitWithOptionsResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::init_with_options(stub, "FakeDevice", false, false, options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.vi();
  EXPECT_SUCCESS(response);
  return session;
}

TEST_F(NiRFSADriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.vi();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session);

  EXPECT_SUCCESS(session, close_response);
}

TEST_F(NiRFSADriverApiTests, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    client::init_with_options(stub(), "", false, false, "");
  }, -200220, "Device identifier is invalid.");
}

MATCHER(IsNonDefaultComplexArray, "")
{
  return std::all_of(
      arg.cbegin(),
      arg.cend(),
      [](const auto& val) { return (val.real() != 0 && val.imaginary() != 0); });
}

TEST_F(NiRFSADriverApiTests, ConfigureGettingStartedIQ_FetchIQSingleRecordComplexF64_ReturnsData)
{
  const auto NUMBER_OF_SAMPLES = 1000;
  auto session = init_session(stub(), PXI_5663E);
  auto configure_clock = client::configure_ref_clock(stub(), session, RefClockSource::REF_CLOCK_SOURCE_ONBOARD_CLOCK, 10e6);
  auto configure_reference_level = client::configure_reference_level(stub(), session, "", 0);
  auto configure_acquisition_type = client::configure_acquisition_type(stub(), session, AcquisitionType::ACQUISITION_TYPE_IQ);
  auto configure_number_of_samples = client::configure_number_of_samples(stub(), session, "", true, 1000);
  auto configure_iq_rate = client::configure_iq_rate(stub(), session, "", 1e6);
  EXPECT_SUCCESS(session, configure_clock);
  EXPECT_SUCCESS(session, configure_reference_level);
  EXPECT_SUCCESS(session, configure_acquisition_type);
  EXPECT_SUCCESS(session, configure_number_of_samples);
  EXPECT_SUCCESS(session, configure_iq_rate);

  auto fetch_record = client::read_iq_single_record_complex_f64(stub(), session, "", 10.0, NUMBER_OF_SAMPLES);

  EXPECT_SUCCESS(session, fetch_record);
  EXPECT_EQ(NUMBER_OF_SAMPLES, fetch_record.data().size());
  EXPECT_THAT(fetch_record.data(), IsNonDefaultComplexArray());
  EXPECT_EQ(0, fetch_record.wfm_info().absolute_initial_x());
  EXPECT_EQ(NUMBER_OF_SAMPLES, fetch_record.wfm_info().actual_samples());
  EXPECT_EQ(1, fetch_record.wfm_info().gain());
  EXPECT_NEAR(1e-06, fetch_record.wfm_info().x_increment(), 1e-08);
}

TEST_F(NiRFSADriverApiTests, ConfigureGettingStartedIQ_FetchIQMultiRecordComplexF32_ReturnsData)
{
  const auto NUMBER_OF_SAMPLES = 10;
  const auto NUMBER_OF_RECORDS = 2;
  auto session = init_session(stub(), PXI_5663E);
  auto configure_acquisition_type = client::configure_acquisition_type(stub(), session, AcquisitionType::ACQUISITION_TYPE_IQ);
  auto configure_number_of_samples = client::configure_number_of_samples(stub(), session, "", true, NUMBER_OF_SAMPLES);
  auto configure_number_of_records = client::configure_number_of_records(stub(), session, "", true, NUMBER_OF_RECORDS);
  EXPECT_SUCCESS(session, configure_acquisition_type);
  EXPECT_SUCCESS(session, configure_number_of_samples);
  EXPECT_SUCCESS(session, configure_number_of_records);

  auto initiate = client::initiate(stub(), session);
  auto fetch_record = client::fetch_iq_multi_record_complex_f32(stub(), session, "", 0, NUMBER_OF_RECORDS, NUMBER_OF_SAMPLES, 10.0);

  EXPECT_SUCCESS(session, fetch_record);
  EXPECT_EQ(NUMBER_OF_SAMPLES * NUMBER_OF_RECORDS, fetch_record.data().size());
  EXPECT_THAT(fetch_record.data(), IsNonDefaultComplexArray());
  EXPECT_EQ(NUMBER_OF_RECORDS, fetch_record.wfm_info().size());
}

TEST_F(NiRFSADriverApiTests, ConfigureGettingStartedIQ_FetchIQSingleRecordComplexI16_ReturnsData)
{
  const auto NUMBER_OF_SAMPLES = 10;
  auto session = init_session(stub(), PXI_5663E);
  auto configure_acquisition_type = client::configure_acquisition_type(stub(), session, AcquisitionType::ACQUISITION_TYPE_IQ);
  auto configure_number_of_samples = client::configure_number_of_samples(stub(), session, "", true, NUMBER_OF_SAMPLES);
  EXPECT_SUCCESS(session, configure_acquisition_type);
  EXPECT_SUCCESS(session, configure_number_of_samples);

  auto initiate = client::initiate(stub(), session);
  auto fetch_record = client::fetch_iq_single_record_complex_i16(stub(), session, "", 0, NUMBER_OF_SAMPLES, 10.0);

  EXPECT_SUCCESS(session, fetch_record);
  EXPECT_EQ(NUMBER_OF_SAMPLES, fetch_record.data().size());
  EXPECT_THAT(fetch_record.data(), IsNonDefaultComplexArray());
}

TEST_F(NiRFSADriverApiTests, ConfigureGettingStartedSpectrum_ReadPowerSpectrumF64_ReturnsSpectrumData)
{
  auto session = init_session(stub(), PXI_5663E);
  auto configure_clock = client::configure_ref_clock(stub(), session, std::string("OnboardClock"), 10e6);
  auto configure_reference_level = client::configure_reference_level(stub(), session, "", 0);
  auto configure_acquisition_type = client::configure_acquisition_type(stub(), session, AcquisitionType::ACQUISITION_TYPE_SPECTRUM);
  auto configure_frequency_start_stop = client::configure_spectrum_frequency_start_stop(stub(), session, "", 990e6, 1010e6);
  auto configure_resolution_bandwidth = client::configure_resolution_bandwidth(stub(), session, "", 10e3);
  auto number_of_spectral_lines = client::get_number_of_spectral_lines(stub(), session, "");
  EXPECT_SUCCESS(session, configure_clock);
  EXPECT_SUCCESS(session, configure_reference_level);
  EXPECT_SUCCESS(session, configure_acquisition_type);
  EXPECT_SUCCESS(session, configure_frequency_start_stop);
  EXPECT_SUCCESS(session, configure_resolution_bandwidth);
  EXPECT_SUCCESS(session, number_of_spectral_lines);
  EXPECT_EQ(4974, number_of_spectral_lines.number_of_spectral_lines());

  auto power_spectrum = client::read_power_spectrum_f64(
      stub(),
      session,
      "",
      10.0,
      number_of_spectral_lines.number_of_spectral_lines());
  EXPECT_SUCCESS(session, power_spectrum);
  auto max_power_iter = std::max_element(
      power_spectrum.power_spectrum_data().cbegin(),
      power_spectrum.power_spectrum_data().cend());
  EXPECT_NE(0.0, *max_power_iter);
  EXPECT_THAT(power_spectrum.power_spectrum_data(), Each(Ne(0.0)));
  EXPECT_EQ(
      power_spectrum.spectrum_info().number_of_spectral_lines(),
      number_of_spectral_lines.number_of_spectral_lines());
  EXPECT_NE(0.0, power_spectrum.spectrum_info().initial_frequency());
  EXPECT_NE(0.0, power_spectrum.spectrum_info().frequency_increment());
}

TEST_F(NiRFSADriverApiTests, GetDeviceResponse_ReturnsResponseData)
{
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::get_device_response(stub(), session, "", DeviceResponse::DEVICE_RESPONSE_DOWNCONVERTER_IF_RESPONSE);

  const auto EXPECTED_SIZE = 81;
  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(response.frequencies(), Each(Not(Eq(0))));
  EXPECT_THAT(response.phase_response(), Each(Eq(0)));
  EXPECT_THAT(response.magnitude_response(), Each(Eq(0)));
  EXPECT_EQ(EXPECTED_SIZE, response.frequencies().size());
  EXPECT_EQ(EXPECTED_SIZE, response.phase_response().size());
  EXPECT_EQ(EXPECTED_SIZE, response.magnitude_response().size());
}

// TODO: AB#1639825. This currently fails because of an off-by-one error.
TEST_F(NiRFSADriverApiTests, GetRelayName_ReturnsRelayName)
{
  auto session = init_session(stub(), PXI_5603);
  auto response = client::get_relay_name(stub(), session, "", 1);

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ("Cal Tone Path Switch", response.name());
}

TEST_F(NiRFSADriverApiTests, GetRelayOperationsCount_ReturnsOperationCounts)
{
  const auto EXPECTED = std::vector<::google::protobuf::int32>{0, 0, 0, 0};
  auto session = init_session(stub(), PXI_5603);
  auto response = client::get_relay_operations_count(stub(), session, "");

  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(
      response.operations_count(),
      ElementsAreArray(EXPECTED.cbegin(), EXPECTED.cend()));
}

TEST_F(NiRFSADriverApiTests, ConfigureDigitalEdgeRefTrigger_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::configure_digital_edge_ref_trigger(
      stub(),
      session,
      DigitalEdgeTriggerSource::DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0,
      DigitalEdge::DIGITAL_EDGE_RISING_EDGE,
      10);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSADriverApiTests, ReconfigureExportedRefClockOutTerminal_UpdatesRefClockSuccessfully)
{
  auto session = init_session(stub(), PXI_5663E);
  auto initial_response = client::get_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL);
  auto set_response = client::set_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL,
      NiRFSAStringAttributeValuesMapped::NIRFSA_STRING_REF_CLOCK_OUT_TERMINAL_REF_OUT);
  auto get_response = client::get_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(REF_OUT_STR, get_response.value());
}

TEST_F(NiRFSADriverApiTests, ReconfigureFFTWindowType_UpdatesFFTWindowSuccessfully)
{
  auto session = init_session(stub(), PXI_5663E);
  auto initial_response = client::get_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FFT_WINDOW_TYPE);
  auto set_response = client::set_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FFT_WINDOW_TYPE,
      NiRFSAInt32AttributeValues::NIRFSA_INT32_FFT_WINDOW_TYPE_GAUSSIAN);
  auto get_response = client::get_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FFT_WINDOW_TYPE);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(
      NiRFSAInt32AttributeValues::NIRFSA_INT32_FFT_WINDOW_TYPE_GAUSSIAN,
      get_response.value());
}

TEST_F(NiRFSADriverApiTests, ExportSignal_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::export_signal(
      stub(),
      session,
      Signal::SIGNAL_START_TRIGGER,
      "",
      ExportTerminal::EXPORT_TERMINAL_REF_OUT);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSADriverApiTests, DisableFractionalResampling_FractionalResamplingIsDisabled)
{
  auto session = init_session(stub(), PXI_5663E);
  auto initial_response = client::get_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_ENABLE_FRACTIONAL_RESAMPLING);
  auto set_response = client::set_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_ENABLE_FRACTIONAL_RESAMPLING,
      false);
  auto get_response = client::get_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_ENABLE_FRACTIONAL_RESAMPLING);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_FALSE(get_response.value());
}

TEST_F(NiRFSADriverApiTests, ReconfigureIQRate_UpdatesIQRateSuccessfully)
{
  auto NEW_RATE = 1.2e6;
  auto session = init_session(stub(), PXI_5663E);
  auto initial_response = client::get_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_IQ_RATE);
  auto set_response = client::set_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_IQ_RATE,
      NEW_RATE);
  auto get_response = client::get_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_IQ_RATE);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_NEAR(NEW_RATE, get_response.value(), .0001);
}

TEST_F(NiRFSADriverApiTests, ReconfigureFetchOffset_UpdatesFetchOffsetSuccessfully)
{
  const auto NEW_OFFSET = 100ULL;
  auto session = init_session(stub(), PXI_5663E);
  auto initial_response = client::get_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FETCH_OFFSET);
  auto set_response = client::set_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FETCH_OFFSET,
      NEW_OFFSET);
  auto get_response = client::get_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_FETCH_OFFSET);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(NEW_OFFSET, get_response.value());
}

// NOTE: disabled because this test requires a 58XX device. Simulating a 58XX hangs on shutdown.
// FIXED in RFSA 21.5 (in development as of this comment).
TEST_F(NiRFSADriverApiTests, DISABLED_ReconfigureDowncoverterMode_UpdatesDownconverterModeSuccessfully)
{
  constexpr auto USER_DEFINED = NiRFSAInt32AttributeValues::NIRFSA_INT32_DOWNCONVERTER_FREQUENCY_OFFSET_MODE_USER_DEFINED;
  constexpr auto ENABLED = NiRFSAInt32AttributeValues::NIRFSA_INT32_DOWNCONVERTER_FREQUENCY_OFFSET_MODE_ENABLED;
  const auto session = init_session(stub(), "5841");
  // Per nirfsa.sub: "NOTE: You must set this attribute to enable the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE attribute."
  const auto bandwidth_response = client::set_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_SIGNAL_BANDWIDTH,
      1e4);
  const auto initial_response = client::get_attribute_vi_int32(stub(), session, "", NiRFSAAttribute::NIRFSA_ATTRIBUTE_DOWNCONVERTER_FREQUENCY_OFFSET_MODE);
  // Toggle the mode since it persists between sessions.
  const auto new_mode = (initial_response.value() == USER_DEFINED) ? ENABLED : USER_DEFINED;
  const auto set_response = client::set_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_DOWNCONVERTER_FREQUENCY_OFFSET_MODE,
      new_mode);
  const auto get_response = client::get_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_DOWNCONVERTER_FREQUENCY_OFFSET_MODE);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(new_mode, get_response.value());
}

TEST_F(NiRFSADriverApiTests, CreateConfigurationList_Succeeds)
{
  const auto LIST_NAME = "MyList";
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::create_configuration_list(
      stub(),
      session,
      LIST_NAME,
      {NiRFSAAttribute::NIRFSA_ATTRIBUTE_EXTERNAL_GAIN, NiRFSAAttribute::NIRFSA_ATTRIBUTE_DEVICE_INSTANTANEOUS_BANDWIDTH},
      true);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSADriverApiTests, CreateConfigurationListWithInvalidAttribute_ReportsError)
{
  const auto LIST_NAME = "MyList";
  auto session = init_session(stub(), PXI_5663E);

  EXPECT_THROW({
    try {
      client::create_configuration_list(
          stub(),
          session,
          LIST_NAME,
          {NiRFSAAttribute::NIRFSA_ATTRIBUTE_EXTERNAL_GAIN, NiRFSAAttribute::NIRFSA_ATTRIBUTE_NOTCH_FILTER_ENABLED},
          true);
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_RFSA_ERROR(IVI_ATTRIBUTE_NOT_SUPPORTED_ERROR, "Attribute or property not supported.", ex, session);
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);
}

TEST_F(NiRFSADriverApiTests, GetScalingCoefficients_ReturnsCoefficients)
{
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::get_scaling_coefficients(
      stub(),
      session,
      "");

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(1, response.coefficient_info().size());
  EXPECT_NE(0.0, response.coefficient_info()[0].gain());
  EXPECT_EQ(0.0, response.coefficient_info()[0].offset());
}

TEST_F(NiRFSADriverApiTests, GetNormalizationCoefficients_ReturnsCoefficients)
{
  auto session = init_session(stub(), PXI_5663E);
  auto response = client::get_normalization_coefficients(
      stub(),
      session,
      "");

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(1, response.coefficient_info().size());
  EXPECT_NE(0.0, response.coefficient_info()[0].gain());
  EXPECT_EQ(0.0, response.coefficient_info()[0].offset());
}

TEST_F(NiRFSADriverApiTests, ConfiguredSpectrumAcquisition_GetSpectralInfoForSmt_ReturnsSpectralInforForSmt)
{
  auto session = init_session(stub(), PXI_5663E);
  auto spectral_lines = client::get_number_of_spectral_lines(stub(), session, "");
  auto configure_acquisition_type = client::configure_acquisition_type(
      stub(),
      session,
      AcquisitionType::ACQUISITION_TYPE_SPECTRUM);
  auto power_spectrum = client::read_power_spectrum_f64(stub(), session, "", 10.0, spectral_lines.number_of_spectral_lines());
  auto response = client::get_spectral_info_for_smt(stub(), session);

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(312, response.spectrum_info().fft_size());
  EXPECT_EQ(1, response.spectrum_info().linear_db());
  EXPECT_EQ(2, response.spectrum_info().spectrum_type());
  EXPECT_EQ(312, response.spectrum_info().window_size());
  EXPECT_EQ(8, response.spectrum_info().window());
}

TEST_F(NiRFSADriverApiTests, TwoSessions_SetupTclkSyncPulseSenderSynchronization_Succeeds)
{
  auto first_session = init_session(stub(), PXI_5663E);
  auto second_session = init_session(stub(), PXI_5663E);

  auto tclk_stub = create_tclk_stub();
  auto result = nitclk_client::setup_for_sync_pulse_sender_synchronize(tclk_stub, {first_session, second_session}, 0);

  EXPECT_SUCCESS(first_session, result);
}

TEST_F(NiRFSADriverApiTests, SelfCalibrateWithStepsToOmit_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  const auto response = client::self_calibrate(stub(), session, SelfCalibrateSteps::SELF_CALIBRATE_STEPS_ALIGNMENT);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSADriverApiTests, IsSelfCalValid)
{
  auto session = init_session(stub(), PXI_5663E);
  const auto response = client::is_self_cal_valid(stub(), session);

  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(response.valid_steps_array(), ElementsAre(SELF_CALIBRATE_STEPS_DIGITIZER_SELF_CAL));
  EXPECT_EQ(SELF_CALIBRATE_STEPS_DIGITIZER_SELF_CAL, response.valid_steps_raw());
}

TEST_F(NiRFSADriverApiTests, SelfTest_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  const auto response = client::self_test(stub(), session);

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ("PASS", response.test_message());
}

TEST_F(NiRFSADriverApiTests, ErrorMessage_ReturnsErrorMessage)
{
  auto session = init_session(stub(), PXI_5663E);
  const auto response = client::error_message(stub(), session, IVI_ATTRIBUTE_NOT_SUPPORTED_ERROR);

  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(
      response.error_message(),
      HasSubstr("Attribute or property not supported."));
}

TEST_F(NiRFSADriverApiTests, GetCalUserDefinedInfo_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  const auto response = client::get_cal_user_defined_info(stub(), session);

  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(
      "Simulated Device",
      response.info());
}

// NOTE: disabled because this test requires a 58XX device. Simulating a 58XX hangs on shutdown.
// FIXED in RFSA 21.5 (in development as of this comment).
TEST_F(NiRFSADriverApiTests, DISABLED_GetDeembeddingCompensationGain_Succeeds)
{
  auto session = init_session(stub(), "5830");

  const auto deembedding_type = client::set_attribute_vi_int32(
      stub(),
      session,
      "if1",
      NiRFSAAttribute::NIRFSA_ATTRIBUTE_DEEMBEDDING_TYPE,
      NiRFSAInt32AttributeValues::NIRFSA_INT32_DEEMBEDDING_TYPE_SCALAR);
  const auto compensation_gain = client::get_attribute_vi_real64(stub(), session, "", NiRFSAAttribute::NIRFSA_ATTRIBUTE_DEEMBEDDING_COMPENSATION_GAIN);

  EXPECT_NEAR(0.0, compensation_gain.value(), 1e-6);
  EXPECT_SUCCESS(session, compensation_gain);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfsg_driver_api_tests.cpp sha256=ec27fdcca8fdf18eaf62c67b3206d819c95f82a5e55678ae7e388bee0909f04a bytes=19611 -->
## FILE: source/tests/system/nirfsg_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfsg_driver_api_tests.cpp`
- sha256: `ec27fdcca8fdf18eaf62c67b3206d819c95f82a5e55678ae7e388bee0909f04a`
- bytes: 19611

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <thread>

#include "device_server.h"
#include "nirfsg/nirfsg_client.h"
#include "nitclk/nitclk_client.h"

using namespace nirfsg_grpc;
namespace client = nirfsg_grpc::experimental::client;
namespace nitclk_client = nitclk_grpc::experimental::client;
using namespace ::testing;

namespace nidevice_grpc {
// Needs to be in the nidevice_grpc namespace for googletest to find this
// because of argument-dependent lookup - see
// https://stackoverflow.com/questions/33371088/how-to-get-a-custom-operator-to-work-with-google-test
bool operator==(const NIComplexNumber& first, const NIComplexNumber& second)
{
  return first.real() == second.real() && first.imaginary() == second.imaginary();
}
}  // namespace nidevice_grpc

namespace ni {
namespace tests {
namespace system {

const auto PXI_5652 = "5652";
const auto PXI_5820 = "5820";
const auto PXI_5841 = "5841";
const auto IVI_ATTRIBUTE_NOT_SUPPORTED_ERROR = 0xBFFA0012;

const int krfsgDriverApiSuccess = 0;

template <typename TResponse>
void EXPECT_SUCCESS(const TResponse& response)
{
  EXPECT_EQ(krfsgDriverApiSuccess, response.status());
}

class NiRFSGDriverApiTests : public ::testing::Test {
 protected:
  NiRFSGDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfsg_stub_(NiRFSG::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiRFSGDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  std::unique_ptr<NiRFSG::Stub>& stub()
  {
    return nirfsg_stub_;
  }

  std::unique_ptr<nitclk_grpc::NiTClk::Stub> create_tclk_stub() const
  {
    return nitclk_grpc::NiTClk::NewStub(device_server_->InProcessChannel());
  }

  void check_error(const nidevice_grpc::Session& session)
  {
    auto response = client::get_error(stub(), session);
    EXPECT_EQ("", std::string(response.error_description().c_str()));
  }

  template <typename TResponse>
  void EXPECT_SUCCESS(const nidevice_grpc::Session& session, const TResponse& response)
  {
    ni::tests::system::EXPECT_SUCCESS(response);
    if (response.status() != krfsgDriverApiSuccess) {
      auto error_message_response = client::error_message(stub(), session, response.status());
      EXPECT_EQ("", std::string(error_message_response.error_message().c_str()));
    }
    check_error(session);
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFSG::Stub> nirfsg_stub_;
};

InitWithOptionsResponse init(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::init_with_options(stub, resource_name, false, false, options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model, const std::string& resource_name)
{
  auto response = init(stub, model, resource_name);
  auto session = response.vi();
  EXPECT_SUCCESS(response);
  return session;
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
}

TEST_F(NiRFSGDriverApiTests, PerformSelfTest_Succeeds)
{
  auto session = init_session(stub(), PXI_5652);
  auto response = client::self_test(stub(), session);
  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_EQ("Passed", response.self_test_message());
}

TEST_F(NiRFSGDriverApiTests, PerformReset_Succeeds)
{
  auto session = init_session(stub(), PXI_5652);
  auto response = client::reset(stub(), session);
  EXPECT_SUCCESS(session, response);
  EXPECT_EQ(0, response.status());
}

void WaitForAndAssertGenerationStarted(const client::StubPtr& stub, const nidevice_grpc::Session& session)
{
  int retries = 0;
  while (retries < 100) {
    auto check_status = client::check_generation_status(stub, session);
    EXPECT_SUCCESS(check_status);
    if (!check_status.is_done()) {
      return;
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
    retries++;
  }
  EXPECT_TRUE(false);
}

TEST_F(NiRFSGDriverApiTests, GettingStartedSingleToneGenerationFromExample_Succeeds)
{
  auto session = init_session(stub(), PXI_5652);
  auto configure_rf = client::configure_rf(stub(), session, 1e9, -5);
  auto initiate = client::initiate(stub(), session);

  WaitForAndAssertGenerationStarted(stub(), session);

  // change frequency
  auto abort = client::abort(stub(), session);
  auto configure_rf2 = client::configure_rf(stub(), session, 1.5e9, -5);
  auto initiate2 = client::initiate(stub(), session);

  WaitForAndAssertGenerationStarted(stub(), session);

  auto disable_output = client::configure_output_enabled(stub(), session, false);
  auto close = client::close(stub(), session);

  EXPECT_SUCCESS(session, configure_rf);
  EXPECT_SUCCESS(session, initiate);
  EXPECT_SUCCESS(session, abort);
  EXPECT_SUCCESS(session, configure_rf2);
  EXPECT_SUCCESS(session, initiate2);
  EXPECT_SUCCESS(session, disable_output);
  EXPECT_SUCCESS(session, close);
}

TEST_F(NiRFSGDriverApiTests, GenerateAndRouteReferenceClockFromExample_Succeeds)
{
  auto session = init_session(stub(), PXI_5652);
  auto configure_rf = client::configure_rf(stub(), session, 1e9, -5);
  auto configure_generation_mode = client::configure_generation_mode(stub(), session, GenerationMode::GENERATION_MODE_CW);
  auto configure_clock = client::configure_ref_clock(stub(), session, RefClockSource::REF_CLOCK_SOURCE_ONBOARD_CLOCK, 10e6);
  auto initiate = client::initiate(stub(), session);

  WaitForAndAssertGenerationStarted(stub(), session);

  auto disable_output = client::configure_output_enabled(stub(), session, false);
  auto close = client::close(stub(), session);

  EXPECT_SUCCESS(session, configure_rf);
  EXPECT_SUCCESS(session, configure_generation_mode);
  EXPECT_SUCCESS(session, configure_clock);
  EXPECT_SUCCESS(session, initiate);
  EXPECT_SUCCESS(session, disable_output);
  EXPECT_SUCCESS(session, close);
}

TEST_F(NiRFSGDriverApiTests, ConfigureDigitalEdgeStartTrigger_Succeeds)
{
  auto session = init_session(stub(), PXI_5841);
  auto response = client::configure_digital_edge_start_trigger(
      stub(),
      session,
      TriggerSource::TRIGGER_SOURCE_PXI_TRIG0,
      DigitalEdgeEdge::DIGITAL_EDGE_EDGE_RISING_EDGE);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSGDriverApiTests, ReconfigureExportedRefClockOutTerminal_UpdatesRefClockSuccessfully)
{
  auto session = init_session(stub(), PXI_5652);
  auto initial_response = client::get_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL);
  auto set_response = client::set_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL,
      NiRFSGStringAttributeValuesMapped::NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT);
  auto get_response = client::get_attribute_vi_string(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ("RefOut", get_response.value());
}

TEST_F(NiRFSGDriverApiTests, SetAutomaticThermalCorrection_UpdatesSuccessfully)
{
  auto session = init_session(stub(), PXI_5652);
  auto initial_response = client::get_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION);
  auto set_response = client::set_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION,
      NiRFSGInt32AttributeValues::NIRFSG_INT32_ENABLE_VALUES_DISABLE);
  auto get_response = client::get_attribute_vi_int32(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(
      NiRFSGInt32AttributeValues::NIRFSG_INT32_ENABLE_VALUES_DISABLE,
      get_response.value());
}

TEST_F(NiRFSGDriverApiTests, ExportSignal_Succeeds)
{
  auto session = init_session(stub(), PXI_5841);
  auto response = client::export_signal(
      stub(),
      session,
      RoutedSignal::ROUTED_SIGNAL_START_TRIGGER,
      std::string(""),
      OutputSignal::OUTPUT_SIGNAL_PFI0);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFSGDriverApiTests, DisableIQImpairment_IQImpairmentIsDisabled)
{
  auto session = init_session(stub(), PXI_5841);
  auto initial_response = client::get_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED);
  auto set_response = client::set_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED,
      false);
  auto get_response = client::get_attribute_vi_boolean(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_FALSE(get_response.value());
}

TEST_F(NiRFSGDriverApiTests, ReconfigureIQRate_UpdatesIQRateSuccessfully)
{
  auto NEW_RATE = 1.2e6;
  auto session = init_session(stub(), PXI_5841);
  auto initial_response = client::get_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_RATE);
  auto set_response = client::set_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_RATE,
      NEW_RATE);
  auto get_response = client::get_attribute_vi_real64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_RATE);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_NEAR(NEW_RATE, get_response.value(), .0001);
}

TEST_F(NiRFSGDriverApiTests, SetHostDMABufferSize_UpdatesHostDMABufferSizeSuccessfully)
{
  auto NEW_VALUE = 10 * 1024 * 1024;
  auto session = init_session(stub(), PXI_5841);
  auto initial_response = client::get_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE);
  auto set_response = client::set_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE,
      NEW_VALUE);
  auto get_response = client::get_attribute_vi_int64(
      stub(),
      session,
      "",
      NiRFSGAttribute::NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE);

  EXPECT_SUCCESS(session, initial_response);
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_NE(initial_response.value(), get_response.value());
  EXPECT_EQ(NEW_VALUE, get_response.value());
}

TEST_F(NiRFSGDriverApiTests, GetDeembeddingSParameters_Empty)
{
  auto session = init_session(stub(), PXI_5841);
  auto parameters = client::get_deembedding_sparameters(stub(), session);

  EXPECT_SUCCESS(session, parameters);
  EXPECT_EQ(0, parameters.number_of_sparameters());
  EXPECT_EQ(0, parameters.sparameters_size());
  EXPECT_EQ(0, parameters.sparameters().size());
}

TEST_F(NiRFSGDriverApiTests, SetDeembeddingSParameters_GetDeembeddingSParameters_Match)
{
  auto session = init_session(stub(), PXI_5841);
  std::vector<double> frequencies = {1 * 1000 * 1000 * 1000};
  auto parameter1 = nidevice_grpc::NIComplexNumber();
  parameter1.set_real(1.0);
  parameter1.set_imaginary(-1.0);
  auto parameter2 = nidevice_grpc::NIComplexNumber();
  parameter2.set_real(-0.5);
  parameter2.set_imaginary(0.5);
  auto parameter3 = nidevice_grpc::NIComplexNumber();
  parameter3.set_real(0.0);
  parameter3.set_imaginary(1.0);
  auto parameter4 = nidevice_grpc::NIComplexNumber();
  parameter4.set_real(-1.0);
  parameter4.set_imaginary(0.0);
  std::vector<nidevice_grpc::NIComplexNumber> parameters = {parameter1, parameter2, parameter3, parameter4};
  auto set_parameters = client::create_deembedding_sparameter_table_array(
      stub(),
      session,
      "",
      "table",
      frequencies,
      parameters,
      2,
      SParameterOrientation::S_PARAMETER_ORIENTATION_PORT2_TOWARDS_DUT);
  auto get_parameters = client::get_deembedding_sparameters(stub(), session);

  EXPECT_SUCCESS(session, set_parameters);
  EXPECT_SUCCESS(session, get_parameters);
  EXPECT_EQ(2, get_parameters.number_of_ports());
  EXPECT_EQ(4, get_parameters.sparameters_size());
  EXPECT_EQ(4, get_parameters.sparameters().size());
  EXPECT_EQ(parameter1, get_parameters.sparameters(0));
  EXPECT_EQ(parameter1, get_parameters.sparameters()[0]);
  EXPECT_EQ(parameter2, get_parameters.sparameters(1));
  EXPECT_EQ(parameter2, get_parameters.sparameters()[1]);
  EXPECT_EQ(parameter3, get_parameters.sparameters(2));
  EXPECT_EQ(parameter3, get_parameters.sparameters()[2]);
  EXPECT_EQ(parameter4, get_parameters.sparameters(3));
  EXPECT_EQ(parameter4, get_parameters.sparameters()[3]);
}

TEST_F(NiRFSGDriverApiTests, WriteArbWaveformI16_Succeeds)
{
  auto session = init_session(stub(), PXI_5841);
  auto configure_rf = client::configure_rf(stub(), session, 1e9, -5);
  auto configure_generation_mode = client::configure_generation_mode(stub(), session, GenerationMode::GENERATION_MODE_ARB_WAVEFORM);
  auto configure_power_level_type = client::configure_power_level_type(stub(), session, PowerLevelType::POWER_LEVEL_TYPE_PEAK_POWER);
  auto point1 = nidevice_grpc::NIComplexI16();
  point1.set_real(INT16_MAX);
  point1.set_imaginary(INT16_MIN);
  auto point2 = nidevice_grpc::NIComplexI16();
  point2.set_real(0);
  point2.set_imaginary(0);
  auto point3 = nidevice_grpc::NIComplexI16();
  point3.set_real(INT16_MIN);
  point3.set_imaginary(INT16_MAX);
  auto point4 = nidevice_grpc::NIComplexI16();
  point4.set_real(0);
  point4.set_imaginary(0);
  std::vector<nidevice_grpc::NIComplexI16> waveform = {point1, point2, point3, point4};
  auto write_waveform = client::write_arb_waveform_complex_i16(stub(), session, "waveform", waveform);
  auto initiate = client::initiate(stub(), session);
  std::this_thread::sleep_for(std::chrono::milliseconds(100));

  auto check_status = client::check_generation_status(stub(), session);
  auto disable_output = client::configure_output_enabled(stub(), session, false);
  auto close = client::close(stub(), session);

  EXPECT_SUCCESS(session, configure_rf);
  EXPECT_SUCCESS(session, configure_generation_mode);
  EXPECT_SUCCESS(session, configure_power_level_type);
  EXPECT_SUCCESS(session, write_waveform);
  EXPECT_SUCCESS(session, initiate);
  EXPECT_SUCCESS(session, check_status);
  EXPECT_SUCCESS(session, disable_output);
  EXPECT_SUCCESS(session, close);
}

TEST_F(NiRFSGDriverApiTests, WriteArbWaveformF32_Succeeds)
{
  auto session = init_session(stub(), PXI_5820);
  auto configure_generation_mode = client::configure_generation_mode(stub(), session, GenerationMode::GENERATION_MODE_ARB_WAVEFORM);
  auto configure_power_level_type = client::configure_power_level_type(stub(), session, PowerLevelType::POWER_LEVEL_TYPE_PEAK_POWER);
  auto configure_iq_port_level = client::set_attribute_vi_real64(stub(), session, "", NiRFSGAttribute::NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LEVEL, 0.2);
  auto configure_gain = client::set_attribute_vi_real64(stub(), session, "", NiRFSGAttribute::NIRFSG_ATTRIBUTE_ARB_PRE_FILTER_GAIN, -20);
  auto point1 = nidevice_grpc::NIComplexNumberF32();
  point1.set_real(0.7f);
  point1.set_imaginary(-0.7f);
  auto point2 = nidevice_grpc::NIComplexNumberF32();
  point2.set_real(0);
  point2.set_imaginary(1.0);
  auto point3 = nidevice_grpc::NIComplexNumberF32();
  point3.set_real(-0.7f);
  point3.set_imaginary(0.7f);
  auto point4 = nidevice_grpc::NIComplexNumberF32();
  point4.set_real(-1.0);
  point4.set_imaginary(0);
  auto point5 = nidevice_grpc::NIComplexNumberF32();
  point5.set_real(1.0);
  point5.set_imaginary(0);
  auto point6 = nidevice_grpc::NIComplexNumberF32();
  point6.set_real(0);
  point6.set_imaginary(-1.0f);
  auto point7 = nidevice_grpc::NIComplexNumberF32();
  point7.set_real(0.7f);
  point7.set_imaginary(0.7f);
  auto point8 = nidevice_grpc::NIComplexNumberF32();
  point8.set_real(-0.7f);
  point8.set_imaginary(-0.7f);
  std::vector<nidevice_grpc::NIComplexNumberF32> waveform = {point1, point2, point3, point4, point5, point6, point7, point8};
  auto write_waveform = client::write_arb_waveform_complex_f32(stub(), session, "waveform", waveform, false);
  auto initiate = client::initiate(stub(), session);
  std::this_thread::sleep_for(std::chrono::milliseconds(100));

  auto check_status = client::check_generation_status(stub(), session);
  auto disable_output = client::configure_output_enabled(stub(), session, false);
  auto close = client::close(stub(), session);

  EXPECT_SUCCESS(session, configure_generation_mode);
  EXPECT_SUCCESS(session, configure_power_level_type);
  EXPECT_SUCCESS(session, configure_iq_port_level);
  EXPECT_SUCCESS(session, configure_gain);
  EXPECT_SUCCESS(session, write_waveform);
  EXPECT_SUCCESS(session, initiate);
  EXPECT_SUCCESS(session, check_status);
  EXPECT_SUCCESS(session, disable_output);
  EXPECT_SUCCESS(session, close);
}

TEST_F(NiRFSGDriverApiTests, SetUserData_GetUserData_DataMatches)
{
  auto session = init_session(stub(), PXI_5652);
  std::string data = "abc";
  data.push_back('\0');
  data.append("def");
  auto set_response = client::set_user_data(stub(), session, "identifier", data);
  auto get_response = client::get_user_data(stub(), session, "identifier");
  EXPECT_SUCCESS(session, set_response);
  EXPECT_SUCCESS(session, get_response);
  EXPECT_EQ(7, get_response.data().length());
  EXPECT_EQ(data, get_response.data());
}

TEST_F(NiRFSGDriverApiTests, TwoSessions_SetupTclkSyncPulseSenderSynchronization_Succeeds)
{
  auto first_session = init_session(stub(), PXI_5841, "FakeDevice");
  auto second_session = init_session(stub(), PXI_5841, "AnotherFakeDevice");

  auto tclk_stub = create_tclk_stub();
  auto result = nitclk_client::setup_for_sync_pulse_sender_synchronize(tclk_stub, {first_session, second_session}, 0);

  EXPECT_SUCCESS(first_session, result);
}

TEST_F(NiRFSGDriverApiTests, ErrorMessage_ReturnsErrorMessage)
{
  auto session = init_session(stub(), PXI_5652);
  const auto response = client::error_message(stub(), session, IVI_ATTRIBUTE_NOT_SUPPORTED_ERROR);

  EXPECT_SUCCESS(session, response);
  EXPECT_THAT(
      response.error_message(),
      HasSubstr("Attribute or property not supported."));
}
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfsg_restricted_driver_api_tests.cpp sha256=88aec66bf204ff9929ea18d3beaf5c8f9140c71333db3e10c667bb9912ac84b2 bytes=4322 -->
## FILE: source/tests/system/nirfsg_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfsg_restricted_driver_api_tests.cpp`
- sha256: `88aec66bf204ff9929ea18d3beaf5c8f9140c71333db3e10c667bb9912ac84b2`
- bytes: 4322

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <thread>

#include "device_server.h"
#include "nirfsg/nirfsg_client.h"
#include "nirfsg_restricted/nirfsg_restricted_client.h"

using namespace nirfsg_grpc;
using namespace nirfsg_restricted_grpc;
namespace client = nirfsg_grpc::experimental::client;
namespace restricted_client = nirfsg_restricted_grpc::experimental::client;
using namespace ::testing;

namespace ni {
namespace tests {
namespace system {

const auto PXI_5841 = "5841";
const int krfsgDriverApiSuccess = 0;

template <typename TResponse>
void EXPECT_SUCCESS(const TResponse& response)
{
  EXPECT_EQ(krfsgDriverApiSuccess, response.status());
}

class NiRFSGRestrictedDriverApiTests : public ::testing::Test {
 protected:
  NiRFSGRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfsg_stub_(NiRFSG::NewStub(device_server_->InProcessChannel())),
        nirfsg_restricted_stub_(NiRFSGRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiRFSGRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  std::unique_ptr<NiRFSG::Stub>& stub()
  {
    return nirfsg_stub_;
  }

  std::unique_ptr<NiRFSGRestricted::Stub>& restricted_stub()
  {
    return nirfsg_restricted_stub_;
  }
  
  void check_error(const nidevice_grpc::Session& session)
  {
    auto response = client::get_error(stub(), session);
    EXPECT_EQ("", std::string(response.error_description().c_str()));
  }
  
  template <typename TResponse>
  void EXPECT_SUCCESS(const TResponse& response)
  {
    EXPECT_EQ(krfsgDriverApiSuccess, response.status());
  }
  
  template <typename TResponse>
  void EXPECT_SUCCESS(const nidevice_grpc::Session& session, const TResponse& response)
  {
    ni::tests::system::EXPECT_SUCCESS(response);
    if (response.status() != krfsgDriverApiSuccess) {
      auto error_message_response = client::error_message(stub(), session, response.status());
      EXPECT_EQ("", std::string(error_message_response.error_message().c_str()));
    }
    check_error(session);
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFSG::Stub> nirfsg_stub_;
  std::unique_ptr<NiRFSGRestricted::Stub> nirfsg_restricted_stub_;
};

nidevice_grpc::Session init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  auto response = client::init_with_options(stub, "FakeDevice", false, false, options);
  auto session = response.vi();
  EXPECT_SUCCESS(response);
  return session;
}

TEST_F(NiRFSGRestrictedDriverApiTests, RestrictedSetDeembeddingSparameterTable_Succeeds)
{
  auto session = init(stub(), PXI_5841);
  std::vector<double> frequencies = {1 * 1000 * 1000 * 1000};
  auto parameter1 = nidevice_grpc::NIComplexNumber();
  parameter1.set_real(1.0);
  parameter1.set_imaginary(-1.0);
  auto parameter2 = nidevice_grpc::NIComplexNumber();
  parameter2.set_real(-0.5);
  parameter2.set_imaginary(0.5);
  auto parameter3 = nidevice_grpc::NIComplexNumber();
  parameter3.set_real(0.0);
  parameter3.set_imaginary(1.0);
  auto parameter4 = nidevice_grpc::NIComplexNumber();
  parameter4.set_real(-1.0);
  parameter4.set_imaginary(0.0);
  std::vector<nidevice_grpc::NIComplexNumber> parameters = {parameter1, parameter2, parameter3, parameter4};
  auto configure_table = restricted_client::create_deembedding_sparameter_table(restricted_stub(), session, "", "table", 1, 2);
  auto configure_frequencies = restricted_client::configure_sparameter_table_frequencies(restricted_stub(), session, "", "table", frequencies);
  auto configure_sparameter = restricted_client::configure_sparameter_table_sparameters(restricted_stub(), session, "", "table", parameters, nirfsg_restricted_grpc::SParameterOrientation::S_PARAMETER_ORIENTATION_PORT2_TOWARDS_DUT);
  auto close = client::close(stub(), session);

  EXPECT_SUCCESS(session, configure_table);
  EXPECT_SUCCESS(session, configure_frequencies);
  EXPECT_SUCCESS(session, configure_sparameter);
  EXPECT_SUCCESS(session, close);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfsg_session_tests.cpp sha256=01015b836a43778d428f75f39580ffab20c568c4aaedb452b1289de81c2441e7 bytes=4567 -->
## FILE: source/tests/system/nirfsg_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfsg_session_tests.cpp`
- sha256: `01015b836a43778d428f75f39580ffab20c568c4aaedb452b1289de81c2441e7`
- bytes: 4567

````cpp
#include "device_server.h"
#include "nirfsg/nirfsg_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace rfsg = nirfsg_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFSGSession = -1074130544;
const char* kRFSGErrorResourceNotFoundMessage = "Device identifier is invalid.";
const char* kRFSGTestRsrc = "FakeDevice";
const char* kRFSGOptionsString = "Simulate=1, DriverSetup=Model:5652; BoardType:PXI";
const char* kRFSGTestSession = "SessionName";
const char* kRFSGTestInvalidRsrc = "";

class NiRFSGSessionTest : public ::testing::Test {
 protected:
  NiRFSGSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfsg_stub_(rfsg::NiRFSG::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFSGSessionTest() {}

  std::unique_ptr<rfsg::NiRFSG::Stub>& GetStub()
  {
    return nirfsg_stub_;
  }

  ::grpc::Status call_init_with_options(const char* resource_name, const char* option_string, const char* session_name, rfsg::InitWithOptionsResponse* response)
  {
    ::grpc::ClientContext context;
    rfsg::InitWithOptionsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset_device(false);
    request.set_id_query(false);

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  void expect_error_string(nidevice_grpc::Session& session, google::protobuf::int32 error_code, const char* expected_error_string)
  {
    ::grpc::ClientContext context;
    rfsg::GetErrorRequest error_request;
    error_request.mutable_vi()->set_name(session.name());
    rfsg::GetErrorResponse error_response;
    ::grpc::Status status = GetStub()->GetError(&context, error_request, &error_response);
    EXPECT_TRUE(status.ok());
    EXPECT_STREQ(expected_error_string, error_response.error_description().c_str());
    EXPECT_EQ(error_code, error_response.error_code());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfsg::NiRFSG::Stub> nirfsg_stub_;
};

TEST_F(NiRFSGSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfsg::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kRFSGTestRsrc, kRFSGOptionsString, kRFSGTestSession, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiRFSGSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfsg::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kRFSGTestRsrc, kRFSGOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiRFSGSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfsg::InitWithOptionsResponse init_response;
  call_init_with_options(kRFSGTestRsrc, kRFSGOptionsString, kRFSGTestSession, &init_response);

  nidevice_grpc::Session session = init_response.vi();
  ::grpc::ClientContext context;
  rfsg::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  rfsg::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFSGSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    rfsg::InitWithOptionsResponse init_response;
    call_init_with_options(kRFSGTestInvalidRsrc, "", "", &init_response);
  }, kInvalidRsrc, kRFSGErrorResourceNotFoundMessage);
}

TEST_F(NiRFSGSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    ::grpc::ClientContext context;
    rfsg::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    rfsg::CloseResponse response;
    auto status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidRFSGSession);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/niscope_driver_api_tests.cpp sha256=081de9c504a45461d75c7e921354c9201481bddd0ec79cfaf496dc60e741c7ca bytes=24398 -->
## FILE: source/tests/system/niscope_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/niscope_driver_api_tests.cpp`
- sha256: `081de9c504a45461d75c7e921354c9201481bddd0ec79cfaf496dc60e741c7ca`
- bytes: 24398

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "niscope/niscope_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace scope = niscope_grpc;
namespace pb = ::google::protobuf;

typedef pb::int16 int16;
typedef pb::int32 int32;
typedef pb::int64 int64;
typedef pb::uint32 uint32;
typedef pb::uint16 uint16;

const int kScopeDriverApiSuccess = 0;

class NiScopeDriverApiTest : public ::testing::Test {
 protected:
  NiScopeDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        niscope_stub_(scope::NiScope::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiScopeDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<scope::NiScope::Stub>& GetStub()
  {
    return niscope_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    scope::InitWithOptionsRequest request;
    request.set_resource_name("FakeDevice");
    request.set_option_string("Simulate=1, DriverSetup=Model:5164; BoardType:PXIe");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_id_query(false);
    scope::InitWithOptionsResponse response;

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  }

  void close_driver_session()
  {
    ::grpc::ClientContext context;
    scope::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    scope::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  int get_actual_num_wfms(const char* channel_list)
  {
    ::grpc::ClientContext context;
    scope::ActualNumWfmsRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    scope::ActualNumWfmsResponse response;
    auto status = GetStub()->ActualNumWfms(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    EXPECT_EQ(1, response.num_wfms());
    return response.num_wfms();
  }

  int get_actual_measurement_waveform_size(niscope_grpc::ArrayMeasurement array_measurement)
  {
    ::grpc::ClientContext context;
    scope::ActualMeasWfmSizeRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_array_meas_function(array_measurement);
    scope::ActualMeasWfmSizeResponse response;
    auto status = GetStub()->ActualMeasWfmSize(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.meas_waveform_size();
  }

  void initiate_acquisition()
  {
    ::grpc::ClientContext context;
    scope::InitiateAcquisitionRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    scope::InitiateAcquisitionResponse response;
    auto status = GetStub()->InitiateAcquisition(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void expect_api_success(int error_status)
  {
    EXPECT_EQ(kScopeDriverApiSuccess, error_status) << get_error_message(error_status);
  }

  std::string get_error_message(int error_status)
  {
    ::grpc::ClientContext context;
    scope::GetErrorMessageRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_error_code(error_status);
    scope::GetErrorMessageResponse response;

    ::grpc::Status status = GetStub()->GetErrorMessage(&context, request, &response);
    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kScopeDriverApiSuccess, response.status());
    return response.error_message();
  }

  void auto_setup()
  {
    ::grpc::ClientContext context;
    scope::AutoSetupRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    scope::AutoSetupResponse response;

    ::grpc::Status status = GetStub()->AutoSetup(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  bool get_bool_attribute(const char* channel_list, scope::NiScopeAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    scope::GetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_attribute_id(attribute_id);
    scope::GetAttributeViBooleanResponse response;
    ::grpc::Status status = GetStub()->GetAttributeViBoolean(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.value();
  }

  int32 get_int32_attribute(const char* channel_list, scope::NiScopeAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    scope::GetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_attribute_id(attribute_id);
    scope::GetAttributeViInt32Response response;
    ::grpc::Status status = GetStub()->GetAttributeViInt32(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.value();
  }

  int64 get_int64_attribute(const char* channel_list, scope::NiScopeAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    scope::GetAttributeViInt64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_attribute_id(attribute_id);
    scope::GetAttributeViInt64Response response;
    ::grpc::Status status = GetStub()->GetAttributeViInt64(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.value();
  }

  double get_real64_attribute(const char* channel_list, scope::NiScopeAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    scope::GetAttributeViReal64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_attribute_id(attribute_id);
    scope::GetAttributeViReal64Response response;
    ::grpc::Status status = GetStub()->GetAttributeViReal64(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.value();
  }

  std::string get_string_attribute(const char* channel_list, scope::NiScopeAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    scope::GetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_attribute_id(attribute_id);
    scope::GetAttributeViStringResponse response;
    ::grpc::Status status = GetStub()->GetAttributeViString(&context, request, &response);
    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.value();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<scope::NiScope::Stub> niscope_stub_;
};

TEST_F(NiScopeDriverApiTest, NiScopeSelfTest_SendRequest_SelfTestCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  scope::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  scope::SelfTestResponse response;

  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_LT(0, strlen(response.self_test_message().c_str()));
}

TEST_F(NiScopeDriverApiTest, NiScopeReset_SendRequest_ResetCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  scope::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  scope::ResetResponse response;

  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiScopeDriverApiTest, NiScopeRead_SendRequest_ReadCompletesWithCorrectSizes)
{
  const int32 expected_num_samples = 100000;
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  ::grpc::ClientContext context;
  scope::ReadRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_num_samples(expected_num_samples);
  scope::ReadResponse response;

  ::grpc::Status status = GetStub()->Read(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_samples * expected_num_waveforms, response.waveform_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchArrayMeasurement_SendRequestWithNegativeWfmSize_FetchCompletesUsingActualMeasurementWaveformSize)
{
  auto_setup();
  initiate_acquisition();
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  const niscope_grpc::ArrayMeasurement measurement_func = niscope_grpc::ArrayMeasurement::ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE;
  const int32 expected_waveform_size = get_actual_measurement_waveform_size(measurement_func);
  ::grpc::ClientContext context;
  scope::FetchArrayMeasurementRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_array_meas_function(measurement_func);
  request.set_meas_wfm_size(-1);
  scope::FetchArrayMeasurementResponse response;

  ::grpc::Status status = GetStub()->FetchArrayMeasurement(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_waveforms * expected_waveform_size, response.meas_wfm_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchArrayMeasurement_SendRequestWithoutWfmSize_FetchCompletesUsingActualMeasurementWaveformSize)
{
  auto_setup();
  initiate_acquisition();
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  const niscope_grpc::ArrayMeasurement measurement_func = niscope_grpc::ArrayMeasurement::ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE;
  const int32 expected_waveform_size = get_actual_measurement_waveform_size(measurement_func);
  ::grpc::ClientContext context;
  scope::FetchArrayMeasurementRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_array_meas_function(measurement_func);
  scope::FetchArrayMeasurementResponse response;

  ::grpc::Status status = GetStub()->FetchArrayMeasurement(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_waveforms * expected_waveform_size, response.meas_wfm_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchArrayMeasurement_SendRequestWithZeroMeasWfmSize_FetchCompletesWithZeroMeasurementWaveformSize)
{
  auto_setup();
  initiate_acquisition();
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  const niscope_grpc::ArrayMeasurement measurement_func = niscope_grpc::ArrayMeasurement::ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE;
  const int32 zero_waveform_size = 0;
  ::grpc::ClientContext context;
  scope::FetchArrayMeasurementRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_array_meas_function(measurement_func);
  request.set_meas_wfm_size(zero_waveform_size);
  scope::FetchArrayMeasurementResponse response;

  ::grpc::Status status = GetStub()->FetchArrayMeasurement(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(zero_waveform_size, response.meas_wfm_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchArrayMeasurement_SendRequestWithMeasWfmSize_FetchCompletesWithCorrectSizes)
{
  auto_setup();
  initiate_acquisition();
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  const niscope_grpc::ArrayMeasurement measurement_func = niscope_grpc::ArrayMeasurement::ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE;
  const int32 waveform_size = 42;
  ::grpc::ClientContext context;
  scope::FetchArrayMeasurementRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_array_meas_function(measurement_func);
  request.set_meas_wfm_size(waveform_size);
  scope::FetchArrayMeasurementResponse response;

  ::grpc::Status status = GetStub()->FetchArrayMeasurement(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_waveforms * waveform_size, response.meas_wfm_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchBinary16_SendRequest_FetchCompletesWithCorrectSizes)
{
  auto_setup();
  initiate_acquisition();
  const int32 expected_num_samples = 100000;
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  ::grpc::ClientContext context;
  scope::FetchBinary16Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_num_samples(expected_num_samples);
  scope::FetchBinary16Response response;

  ::grpc::Status status = GetStub()->FetchBinary16(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_waveforms * expected_num_samples, response.waveform_size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeFetchBinary8_SendRequest_FetchCompletesWithCorrectSizes)
{
  auto_setup();
  initiate_acquisition();
  const int32 expected_num_samples = 100000;
  const char* channel_list = "0";
  const int32 expected_num_waveforms = get_actual_num_wfms(channel_list);
  ::grpc::ClientContext context;
  scope::FetchBinary8Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_timeout(10000);
  request.set_num_samples(expected_num_samples);
  scope::FetchBinary8Response response;

  ::grpc::Status status = GetStub()->FetchBinary8(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_num_waveforms * expected_num_samples, response.waveform().size());
  EXPECT_EQ(expected_num_waveforms, response.wfm_info_size());
}

TEST_F(NiScopeDriverApiTest, NiScopeSetViInt32Attribute_SendRequest_GetViInt32AttributeMatches)
{
  const char* channel_list = "";
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_HORZ_NUM_RECORDS;
  const int32 expected_value = 4;
  ::grpc::ClientContext context;
  scope::SetAttributeViInt32Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value_raw(expected_value);
  scope::SetAttributeViInt32Response response;

  ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  int32 get_attribute_value = get_int32_attribute(channel_list, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiScopeDriverApiTest, NiScopeSetViInt64Attribute_SendRequest_GetViInt64AttributeMatches)
{
  const char* channel_list = "";
  // The int64 attributes in niScope.h (p2p ones) can't be used on a simulated device. So
  // we'll just set a int32 attribute to still exercise the get and set int64 methods.
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_FETCH_NUM_RECORDS;
  const int64 expected_value = 4;
  ::grpc::ClientContext context;
  scope::SetAttributeViInt64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value_raw(expected_value);
  scope::SetAttributeViInt64Response response;

  ::grpc::Status status = GetStub()->SetAttributeViInt64(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  int64 get_attribute_value = get_int64_attribute(channel_list, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiScopeDriverApiTest, NiScopeSetViReal64Attribute_SendRequest_GetViReal64AttributeMatches)
{
  const char* channel_list = "";
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_REF_CLK_RATE;
  const double expected_value = 42.24;
  ::grpc::ClientContext context;
  scope::SetAttributeViReal64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value_raw(expected_value);
  scope::SetAttributeViReal64Response response;

  ::grpc::Status status = GetStub()->SetAttributeViReal64(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  double get_attribute_value = get_real64_attribute(channel_list, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiScopeDriverApiTest, NiScopeSetViStringAttribute_SendRequest_GetViStringAttributeMatches)
{
  const char* channel_list = "";
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_TRIGGER_SOURCE;
  const std::string expected_value = "Hello world!";
  ::grpc::ClientContext context;
  scope::SetAttributeViStringRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value_raw(expected_value);
  scope::SetAttributeViStringResponse response;

  ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  std::string get_attribute_value = get_string_attribute(channel_list, attribute_to_set);
  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

TEST_F(NiScopeDriverApiTest, NiScopeSetViStringAttributeUtf8Convert_SendRequest_GetViStringAttributeMatches)
{
  const char* channel_list = "";
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_MEAS_OTHER_CHANNEL;
  const std::string expected_value = "\xC2\xAE \xE2\x80\xA0 \xC3\xAB";  // "\u00AE \u2020 \u00EB"
  ::grpc::ClientContext context;
  scope::SetAttributeViStringRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value_raw(expected_value);
  scope::SetAttributeViStringResponse response;

  ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  std::string get_attribute_value = get_string_attribute(channel_list, attribute_to_set);
  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

TEST_F(NiScopeDriverApiTest, NiScopeSetBoolAttribute_SendRequest_GetBoolAttributeMatches)
{
  const char* channel_list = "0";
  const scope::NiScopeAttribute attribute_to_set = scope::NiScopeAttribute::NISCOPE_ATTRIBUTE_CHANNEL_ENABLED;
  const bool expected_value = true;
  ::grpc::ClientContext context;
  scope::SetAttributeViBooleanRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  request.set_attribute_id(attribute_to_set);
  request.set_value(expected_value);
  scope::SetAttributeViBooleanResponse response;

  ::grpc::Status status = GetStub()->SetAttributeViBoolean(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  bool get_attribute_value = get_bool_attribute(channel_list, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiScopeDriverApiTest, NiScopeConfigureHorizontalTiming_SendRequest_ConfigureCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  scope::ConfigureHorizontalTimingRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_min_sample_rate(1000000);
  request.set_min_num_pts(100000);
  request.set_ref_position(50);
  request.set_num_records(1);
  request.set_enforce_realtime(true);
  scope::ConfigureHorizontalTimingResponse response;

  ::grpc::Status status = GetStub()->ConfigureHorizontalTiming(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiScopeDriverApiTest, NiScopeConfigureVertical_SendRequest_ConfigureCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  scope::ConfigureVerticalRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list("0");
  request.set_range(30.0);
  request.set_offset(0);
  request.set_coupling(scope::VerticalCoupling::VERTICAL_COUPLING_NISCOPE_VAL_DC);
  request.set_enabled(true);
  request.set_probe_attenuation(1);
  scope::ConfigureVerticalResponse response;

  ::grpc::Status status = GetStub()->ConfigureVertical(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiScopeDriverApiTest, NiScopeGetScalingCoefficients_SendRequest_NonZeroCoefficientsReturned)
{
  auto_setup();
  ::grpc::ClientContext context;
  scope::GetScalingCoefficientsRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list("0, 1");
  scope::GetScalingCoefficientsResponse response;

  ::grpc::Status status = GetStub()->GetScalingCoefficients(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(2, response.coefficient_info_size());
  EXPECT_EQ(0, response.coefficient_info(0).offset());
  EXPECT_NE(0, response.coefficient_info(0).gain());
}

TEST_F(NiScopeDriverApiTest, NiScopeGetNormalizationCoefficients_SendRequest_NonZeroCoefficientsReturned)
{
  auto_setup();
  ::grpc::ClientContext context;
  scope::GetNormalizationCoefficientsRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list("0, 1");
  scope::GetNormalizationCoefficientsResponse response;

  ::grpc::Status status = GetStub()->GetNormalizationCoefficients(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(2, response.coefficient_info_size());
  EXPECT_EQ(0, response.coefficient_info(0).offset());
  EXPECT_NE(0, response.coefficient_info(0).gain());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/niscope_restricted_driver_api_tests.cpp sha256=f0380c91ff391905d8745405131cf0dd80c7ff1fffc460800f5b33c1b6e3e2d8 bytes=5644 -->
## FILE: source/tests/system/niscope_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/niscope_restricted_driver_api_tests.cpp`
- sha256: `f0380c91ff391905d8745405131cf0dd80c7ff1fffc460800f5b33c1b6e3e2d8`
- bytes: 5644

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "niscope/niscope_client.h"
#include "niscope_restricted/niscope_restricted_client.h"

using namespace niscope_grpc;
using namespace niscope_restricted_grpc;
namespace client = niscope_grpc::experimental::client;
namespace restricted_client = niscope_restricted_grpc::experimental::client;
using namespace ::testing;

namespace ni {
namespace tests {
namespace system {

const int kScopeDriverApiSuccess = 0;

class NiScopeRestrictedDriverApiTests : public ::testing::Test {
 protected:
  NiScopeRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        niscope_stub_(NiScope::NewStub(device_server_->InProcessChannel())),
        niscope_restricted_stub_(NiScopeRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiScopeRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiScope::Stub>& stub()
  {
    return niscope_stub_;
  }

  std::unique_ptr<NiScopeRestricted::Stub>& restricted_stub()
  {
    return niscope_restricted_stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiScope::Stub> niscope_stub_;
  std::unique_ptr<NiScopeRestricted::Stub> niscope_restricted_stub_;
};

InitWithOptionsResponse init_with_options(const client::StubPtr& stub, const std::string& resource_name, const std::string& option_string)
{
  return client::init_with_options(stub, resource_name, false /*id_query*/, false /*reset_device*/, option_string);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub)
{
  auto response = init_with_options(stub, "FakeDevice", "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe");
  auto session = response.vi();
  EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  return session;
}

nidevice_grpc::Session init_multi_instrument_session(const client::StubPtr& stub)
{
  auto response = init_with_options(stub, "FakeDevice1,FakeDevice2", "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe");
  auto session = response.vi();
  EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  return session;
}

TEST_F(NiScopeRestrictedDriverApiTests, NiScopeRestrictedGetStartTimestampInformation_SendRequest_NonZeroTimestampsReturned)
{
  const auto session = init_session(stub());
  const auto auto_setup_response = client::auto_setup(stub(), session);
  EXPECT_EQ(kScopeDriverApiSuccess, auto_setup_response.status());

  const auto response = restricted_client::get_start_timestamp_information(restricted_stub(), session);

  EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  EXPECT_NE(0, response.sys_time_in_128_bits_t1());
  EXPECT_NE(0, response.sys_time_in_128_bits_t2());
  EXPECT_NE(0, response.sys_time_in_128_bits_t3());
  EXPECT_EQ(0, response.sys_time_in_128_bits_t4()); // Not sure why this is always 0, may be because it's on a simulated device.
  EXPECT_EQ(0, response.device_time_in_absolute_time_units()); // Not sure why this is always 0, may be because it's on a simulated device.
}

TEST_F(NiScopeRestrictedDriverApiTests, NiScopeRestrictedGetStartTimestampInformationWithChannels_SendRequest_NonZeroTimestampsReturned)
{
  GTEST_SKIP() << "This test is disabled until the VM driver runtime is updated to include the new function (added in NI-SCOPE 2025 Q4).";

  const auto session = init_multi_instrument_session(stub());
  const auto auto_setup_response = client::auto_setup(stub(), session);
  EXPECT_EQ(kScopeDriverApiSuccess, auto_setup_response.status());

  const auto response = restricted_client::get_start_timestamp_information_with_channels(restricted_stub(), session, "FakeDevice1/0,FakeDevice2/0", 2);

  EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  EXPECT_NE(0, response.sys_time_in_128_bits_t1_array()[0]);
  EXPECT_NE(0, response.sys_time_in_128_bits_t1_array()[1]);
  EXPECT_NE(0, response.sys_time_in_128_bits_t2_array()[0]);
  EXPECT_NE(0, response.sys_time_in_128_bits_t2_array()[1]);
  EXPECT_NE(0, response.sys_time_in_128_bits_t3_array()[0]);
  EXPECT_NE(0, response.sys_time_in_128_bits_t3_array()[1]);
  EXPECT_EQ(0, response.sys_time_in_128_bits_t4_array()[0]); // Not sure why this is always 0, may be because it's on a simulated device.
  EXPECT_EQ(0, response.sys_time_in_128_bits_t4_array()[1]); // Not sure why this is always 0, may be because it's on a simulated device.
  EXPECT_EQ(0, response.device_time_in_absolute_time_units_array()[0]); // Not sure why this is always 0, may be because it's on a simulated device.
  EXPECT_EQ(0, response.device_time_in_absolute_time_units_array()[1]); // Not sure why this is always 0, may be because it's on a simulated device.
}

TEST_F(NiScopeRestrictedDriverApiTests, NiScopeRestrictedParseNumberOfChannels_SendRequest_NumberOfChannelsParsed)
{
  const auto session = init_multi_instrument_session(stub());
  const auto auto_setup_response = client::auto_setup(stub(), session);
  EXPECT_EQ(kScopeDriverApiSuccess, auto_setup_response.status());

  const auto response = restricted_client::parse_number_of_channels(restricted_stub(), session,"FakeDevice1/0,FakeDevice2/0-1");

  EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  EXPECT_EQ(3, response.num_channels());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/niscope_session_tests.cpp sha256=4a8f57be0b8ca4c6d8cb279eb9ddabf828b98b0e9f7055282ed4a898118128f7 bytes=4964 -->
## FILE: source/tests/system/niscope_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/niscope_session_tests.cpp`
- sha256: `4a8f57be0b8ca4c6d8cb279eb9ddabf828b98b0e9f7055282ed4a898118128f7`
- bytes: 4964

````cpp
#include "device_server.h"
#include "niscope/niscope_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace scope = niscope_grpc;

const int kViErrorRsrcNFound = -1073807343;
const int kInvalidScopeSession = -1074130544;
const char* kViErrorRsrcNFoundMessage = "VISA:  (Hex 0xBFFF0011) Insufficient location information or the device or resource is not present in the system.\n\nInvalid Identifier: ";
const char* kInvalidScopeSessionMessage = "The session handle is not valid.";
const char* kTestResourceName = "FakeDevice";
const char* kSimulatedOptionsString = "Simulate=1, DriverSetup=Model:5164; BoardType:PXIe";
const char* kTestSessionName = "SessionName";
const char* kInvalidResourceName = "";

class NiScopeSessionTest : public ::testing::Test {
 protected:
  NiScopeSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        niscope_stub_(scope::NiScope::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiScopeSessionTest() {}

  std::unique_ptr<scope::NiScope::Stub>& GetStub()
  {
    return niscope_stub_;
  }

  ::grpc::Status call_init_with_options(const char* resource_name, const char* option_string, const char* session_name, scope::InitWithOptionsResponse* response)
  {
    ::grpc::ClientContext context;
    scope::InitWithOptionsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset_device(false);
    request.set_id_query(false);

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  std::string get_error_message(int error_status)
  {
    scope::InitWithOptionsResponse init_response;
    call_init_with_options(kTestResourceName, kSimulatedOptionsString, kTestSessionName, &init_response);
    nidevice_grpc::Session session = init_response.vi();

    ::grpc::ClientContext context;
    scope::GetErrorMessageRequest request;
    request.mutable_vi()->set_name(session.name());
    request.set_error_code(error_status);
    scope::GetErrorMessageResponse error_response;

    ::grpc::Status status = GetStub()->GetErrorMessage(&context, request, &error_response);
    EXPECT_TRUE(status.ok());
    return error_response.error_message();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<scope::NiScope::Stub> niscope_stub_;
};

TEST_F(NiScopeSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  scope::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kTestResourceName, kSimulatedOptionsString, kTestSessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiScopeSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  scope::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kTestResourceName, kSimulatedOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiScopeSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  scope::InitWithOptionsResponse init_response;
  call_init_with_options(kTestResourceName, kSimulatedOptionsString, kTestSessionName, &init_response);
  nidevice_grpc::Session session = init_response.vi();

  ::grpc::ClientContext context;
  scope::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  scope::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiScopeSessionTest, InvalidSession_CloseSession_ReturnsInvalidSesssionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    ::grpc::ClientContext context;
    scope::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    scope::CloseResponse response;
    ::grpc::Status status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidScopeSession, kInvalidScopeSessionMessage);
}

TEST_F(NiScopeSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    scope::InitWithOptionsResponse init_response;
    call_init_with_options(kInvalidResourceName, "", "", &init_response);
  }, kViErrorRsrcNFound, kViErrorRsrcNFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/niswitch_driver_api_tests.cpp sha256=32da6e9241a189fe0a03200c0ea6b6297d2dd91a8e7392e2e02433eadb02aff7 bytes=11376 -->
## FILE: source/tests/system/niswitch_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/niswitch_driver_api_tests.cpp`
- sha256: `32da6e9241a189fe0a03200c0ea6b6297d2dd91a8e7392e2e02433eadb02aff7`
- bytes: 11376

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "niswitch/niswitch_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace niswitch = niswitch_grpc;
namespace pb = ::google::protobuf;

typedef pb::int32 int32;
typedef pb::uint32 uint32;
typedef pb::uint16 uint16;

const int kSwitchDriverApiSuccess = 0;
const int kWaitForDebounceMaxTime = 5000;
const char* kRelayName = "b0r0c0";
const char* firstChannelName = "b0r1";
const char* secondChannelName = "b0c1";
const char* thirdChannelName = "b0r2";
const char* fourthChannelName = "b0c6";

class NiSwitchDriverApiTest : public ::testing::Test {
 protected:
  NiSwitchDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        niswitch_stub_(niswitch::NiSwitch::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiSwitchDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<niswitch::NiSwitch::Stub>& GetStub()
  {
    return niswitch_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  void expect_api_success(int error_status)
  {
    EXPECT_EQ(kSwitchDriverApiSuccess, error_status) << get_error_message(error_status);
  }

  std::string get_error_message(int error_status)
  {
    ::grpc::ClientContext context;
    niswitch::ErrorMessageRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_error_code(error_status);
    niswitch::ErrorMessageResponse response;

    ::grpc::Status status = GetStub()->ErrorMessage(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kSwitchDriverApiSuccess, response.status());
    return response.error_message();
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    niswitch::InitWithTopologyRequest request;
    request.set_resource_name("");
    request.set_topology("2529/2-Wire Dual 4x16 Matrix");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_simulate(true);
    niswitch::InitWithTopologyResponse response;

    ::grpc::Status status = GetStub()->InitWithTopology(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kSwitchDriverApiSuccess, response.status());
  }

  void close_driver_session()
  {
    ::grpc::ClientContext context;
    niswitch::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    niswitch::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void wait_for_debounce()
  {
    ::grpc::ClientContext context;
    niswitch::WaitForDebounceRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_maximum_time_ms(kWaitForDebounceMaxTime);
    niswitch::WaitForDebounceResponse response;

    ::grpc::Status status = GetStub()->WaitForDebounce(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  int can_connect(const char* channel1, const char* channel2)
  {
    ::grpc::ClientContext context;
    niswitch::CanConnectRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel1(channel1);
    request.set_channel2(channel2);
    niswitch::CanConnectResponse response;

    ::grpc::Status status = GetStub()->CanConnect(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.path_capability();
  }

  void connect(const char* channel1, const char* channel2)
  {
    ::grpc::ClientContext context;
    niswitch::ConnectRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel1(channel1);
    request.set_channel2(channel2);
    niswitch::ConnectResponse response;

    ::grpc::Status status = GetStub()->Connect(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void disconnect_all()
  {
    ::grpc::ClientContext context;
    niswitch::DisconnectAllRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    niswitch::DisconnectAllResponse response;

    ::grpc::Status status = GetStub()->DisconnectAll(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  int get_relay_position(const char* relay_name)
  {
    ::grpc::ClientContext context;
    niswitch::GetRelayPositionRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_relay_name(relay_name);
    niswitch::GetRelayPositionResponse response;

    ::grpc::Status status = GetStub()->GetRelayPosition(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.relay_position();
  }

  double get_real64_attribute(const char* channel_name, niswitch::NiSwitchAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    niswitch::GetAttributeViReal64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    niswitch::GetAttributeViReal64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  std::string get_string_attribute(const char* channel_name, niswitch::NiSwitchAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    niswitch::GetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    niswitch::GetAttributeViStringResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViString(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<niswitch::NiSwitch::Stub> niswitch_stub_;
};

TEST_F(NiSwitchDriverApiTest, NiSwitchSelfTest_SendRequest_SelfTestCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  niswitch::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  niswitch::SelfTestResponse response;

  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_LT(0, strlen(response.self_test_message().c_str()));
}

TEST_F(NiSwitchDriverApiTest, NiSwitchReset_SendRequest_ResetCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  niswitch::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  niswitch::ResetResponse response;

  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiSwitchDriverApiTest, NiSwitchSetViReal64Attribute_SendRequest_GetViReal64AttributeMatches)
{
  const char* channel_name = "";
  const niswitch::NiSwitchAttribute attribute_to_set = niswitch::NiSwitchAttribute::NISWITCH_ATTRIBUTE_SCAN_DELAY;
  const double expected_value = 402.24;
  ::grpc::ClientContext context;
  niswitch::SetAttributeViReal64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  niswitch::SetAttributeViReal64Response response;

  ::grpc::Status status = GetStub()->SetAttributeViReal64(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  double get_attribute_value = get_real64_attribute(channel_name, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiSwitchDriverApiTest, NiSwitchSetViStringAttribute_SendRequest_GetViStringAttributeMatches)
{
  const char* channel_name = "";
  const niswitch::NiSwitchAttribute attribute_to_set = niswitch::NiSwitchAttribute::NISWITCH_ATTRIBUTE_SCAN_LIST;
  const std::string expected_value = "b0r1->b0c1;b0r1->b0c2;b0r2->b0c3";
  ::grpc::ClientContext context;
  niswitch::SetAttributeViStringRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  niswitch::SetAttributeViStringResponse response;

  ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  std::string get_attribute_value = get_string_attribute(channel_name, attribute_to_set);
  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

TEST_F(NiSwitchDriverApiTest, NiSwitchRelayControl_SendRequest_RelayPositionMatches)
{
  const niswitch::RelayAction relay_action = niswitch::RelayAction::RELAY_ACTION_NISWITCH_VAL_CLOSE_RELAY;
  const niswitch::RelayPosition expected_value = niswitch::RelayPosition::RELAY_POSITION_NISWITCH_VAL_CLOSED;
  ::grpc::ClientContext context;
  niswitch::RelayControlRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_relay_name(kRelayName);
  request.set_relay_action(relay_action);
  niswitch::RelayControlResponse response;

  ::grpc::Status status = GetStub()->RelayControl(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  wait_for_debounce();
  int get_relay_pos = get_relay_position(kRelayName);
  EXPECT_EQ(expected_value, get_relay_pos);
}

TEST_F(NiSwitchDriverApiTest, NiSwitchChannelsAreUnconnected_CanConnectIsCalled_PathAvailableIsReturned)
{
  const niswitch::PathCapability expected_value = niswitch::PathCapability::PATH_CAPABILITY_NISWITCH_VAL_PATH_AVAILABLE;

  int get_path_capability = can_connect(firstChannelName, secondChannelName);

  EXPECT_EQ(expected_value, get_path_capability);
}

TEST_F(NiSwitchDriverApiTest, NiSwitchChannelsAreAlreadyConnected_CanConnectIsCalled_PathExistsIsReturned)
{
  const niswitch::PathCapability expected_value = niswitch::PathCapability::PATH_CAPABILITY_NISWITCH_VAL_PATH_EXISTS;
  connect(thirdChannelName, fourthChannelName);
  wait_for_debounce();

  int get_path_capability = can_connect(thirdChannelName, fourthChannelName);

  EXPECT_EQ(expected_value, get_path_capability);
  disconnect_all();
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/niswitch_session_tests.cpp sha256=836dd762ff3b79dc7918a2ec647df07c3e2af527b48852d240cc600fb6fe1073 bytes=4863 -->
## FILE: source/tests/system/niswitch_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/niswitch_session_tests.cpp`
- sha256: `836dd762ff3b79dc7918a2ec647df07c3e2af527b48852d240cc600fb6fe1073`
- bytes: 4863

````cpp
#include <gmock/gmock.h>

#include "device_server.h"
#include "niswitch/niswitch_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace niswitch = niswitch_grpc;

const int kViErrorRsrcNotFound = -1074118654;
const int kInvalidSwitchSession = -1074130544;
const char* kViErrorRsrcNotFoundMessage = "Invalid resource name.\n\nInvalid Identifier: InvalidName";
const char* kInvalidSwitchSessionMessage = "The session handle is not valid.";
const char* kTestRsrcName = "";
const char* kTestSessName = "SessionName";
const char* kInvalidRsrcName = "InvalidName";
const char* kTopology = "2529/2-Wire Dual 4x16 Matrix";

class NiSwitchSessionTest : public ::testing::Test {
 protected:
  NiSwitchSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        niswitch_stub_(niswitch::NiSwitch::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiSwitchSessionTest() {}

  std::unique_ptr<niswitch::NiSwitch::Stub>& GetStub()
  {
    return niswitch_stub_;
  }

  ::grpc::Status call_init_with_topology(const char* resource_name, const char* topology, const char* session_name, niswitch::InitWithTopologyResponse* response)
  {
    ::grpc::ClientContext context;
    niswitch::InitWithTopologyRequest request;
    request.set_resource_name(resource_name);
    request.set_topology(topology);
    request.set_session_name(session_name);
    request.set_reset_device(false);
    request.set_simulate(true);

    ::grpc::Status status = GetStub()->InitWithTopology(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  std::string get_error_message(int error_status)
  {
    niswitch::InitWithTopologyResponse init_response;
    call_init_with_topology(kTestRsrcName, kTopology, kTestSessName, &init_response);
    nidevice_grpc::Session session = init_response.vi();

    ::grpc::ClientContext context;
    niswitch::ErrorMessageRequest error_request;
    error_request.mutable_vi()->set_name(session.name());
    error_request.set_error_code(error_status);
    niswitch::ErrorMessageResponse error_response;

    ::grpc::Status status = GetStub()->ErrorMessage(&context, error_request, &error_response);
    EXPECT_TRUE(status.ok());
    return error_response.error_message();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<niswitch::NiSwitch::Stub> niswitch_stub_;
};

TEST_F(NiSwitchSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  niswitch::InitWithTopologyResponse response;
  ::grpc::Status status = call_init_with_topology(kTestRsrcName, kTopology, kTestSessName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiSwitchSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  niswitch::InitWithTopologyResponse response;
  ::grpc::Status status = call_init_with_topology(kTestRsrcName, kTopology, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiSwitchSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  niswitch::InitWithTopologyResponse init_response;
  call_init_with_topology(kTestRsrcName, kTopology, kTestSessName, &init_response);
  nidevice_grpc::Session session = init_response.vi();

  ::grpc::ClientContext context;
  niswitch::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  niswitch::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiSwitchSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    ::grpc::ClientContext context;
    niswitch::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    niswitch::CloseResponse response;
    auto status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidSwitchSession, kInvalidSwitchSessionMessage);
}

TEST_F(NiSwitchSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    niswitch::InitWithTopologyResponse init_response;
    call_init_with_topology(kInvalidRsrcName, "", "", &init_response);
  }, kViErrorRsrcNotFound, kViErrorRsrcNotFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nisync_driver_api_tests.cpp sha256=7238774e6c4be7119110d6d9dd07794a1307f307f5d3eb6a1de2f7a052db14c9 bytes=55691 -->
## FILE: source/tests/system/nisync_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nisync_driver_api_tests.cpp`
- sha256: `7238774e6c4be7119110d6d9dd07794a1307f307f5d3eb6a1de2f7a052db14c9`
- bytes: 55691

````cpp
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nisync/nisync_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace nisync = nisync_grpc;
namespace pb = ::google::protobuf;

typedef pb::int32 int32;
typedef pb::uint32 uint32;
typedef pb::uint16 uint16;

constexpr auto INVALID_SOURCE_TERMINAL = 0xBFFA4032;
constexpr auto SESSION_NAME = "TestSession";
constexpr auto EMPTY_SESSION_NAME = "";
constexpr auto INVALID_RESOURCE_NAME = "InvalidName";
constexpr auto INVALID_TERMINAL = "Invalid";
constexpr auto NISYNC_VAL_OSCILLATOR = "Oscillator";
constexpr auto NISYNC_VAL_CLKOUT = "ClkOut";
constexpr auto NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE = "The specified source terminal is invalid for this operation.";
constexpr auto NISYNC_VAL_CLKIN = "ClkIn";
constexpr auto NISYNC_VAL_SWTRIG_GLOBAL = "GlobalSoftwareTrigger";
constexpr auto NISYNC_VAL_PXIEDSTARC = "PXIe_DStarC";
constexpr auto NISYNC_VAL_SYNC_CLK_FULLSPEED = "SyncClkFullSpeed";
constexpr auto NISYNC_VAL_CLK100 = "PXIe_Clk100";
constexpr auto NISYNC_VAL_PFI0 = "PFI0";
constexpr auto NISYNC_VAL_PFI1 = "PFI1";
constexpr auto NISYNC_VAL_SYNC_CLK_ASYNC = "SyncClkAsync";
constexpr auto NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_USEC = 4;
constexpr auto NISYNC_VAL_CLK10 = "PXI_Clk10";
constexpr auto NISYNC_VAL_IRIG_TYPE_IRIGB_DC = 0;
constexpr auto NISYNC_VAL_GND = "Ground";
constexpr auto NISYNC_ERROR_TERMINAL_INVALID_MESSAGE = "Terminal for the device is invalid.";
constexpr auto NISYNC_ERROR_RSRC_NOT_RESERVED_MESSAGE = "A resource necessary to complete the specified operation is not reserved and should have already been; therefore, the operation cannot be completed";
constexpr auto NISYNC_VAL_EDGE_RISING = 0;
constexpr auto NISYNC_ERROR_DRIVER_TIMEOUT = 0xBFFA400B;
constexpr auto NISYNC_ERROR_DRIVER_TIMEOUT_MESSAGE = "The driver timed out while performing an operation.";
constexpr auto NISYNC_VAL_LEVEL_LOW = 0;
constexpr auto NISYNC_VAL_LEVEL_HIGH = 1;
constexpr auto NISYNC_ERROR_FEATURE_NOT_SUPPORTED_MESSAGE = "This operation requires a feature that is not supported.";
constexpr auto NISYNC_ERROR_DEST_TERMINAL_INVALID_MESSAGE = "The specified destination terminal is invalid for this operation.";

inline static void EXPECT_SYNC_ERROR(const std::string& error_message, const ::grpc::Status& status)
{
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(error_message, status.error_message());
}

class NiSyncDriverApiTest : public ::testing::Test {
 protected:
  std::string test_resource_name;

  NiSyncDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nisync_stub_(nisync::NiSync::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiSyncDriverApiTest() {}

  virtual const char* get_model_name() const = 0;

  virtual bool is_PXI6683H() const = 0;

  void SetUp() override
  {
    for (const auto& device : EnumerateDevices()) {
      if (device.model() == get_model_name()) {
        if (is_PXI6683H())
        {
          // nitsm only supports one PXI-6683H in Linux, when there are multiple PXI-6683Hs, try to find the one nitsm selects
          ::grpc::ClientContext context;
          nisync::InitRequest request;
          nisync::InitResponse response;
          request.set_resource_name(device.name());
          request.set_session_name(SESSION_NAME);
          request.set_reset_device(false);

          ::grpc::Status status = GetStub()->Init(&context, request, &response);
          if (status.ok() && response.status() == VI_SUCCESS)
          {
            test_resource_name = device.name();
            break;
          }
          else
          {
            continue;
          }
        }
        else
        {
          test_resource_name = device.name();
        }
        break;
      }
    }

    if (test_resource_name.empty()) {
      GTEST_SKIP() << "No device found";
    }

    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<nisync::NiSync::Stub>& GetStub()
  {
    return nisync_stub_;
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    nisync::InitRequest request;
    nisync::InitResponse response;
    request.set_resource_name(test_resource_name);
    request.set_session_name(SESSION_NAME);
    request.set_reset_device(false);

    ::grpc::Status status = GetStub()->Init(&context, request, &response);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void close_driver_session()
  {
    if (!driver_session_) return;

    ::grpc::ClientContext context;
    nisync::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    nisync::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  ::grpc::Status call_RevisionQuery(std::string* driverRevision, std::string* firmwareRevision, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::RevisionQueryRequest request;
    nisync::RevisionQueryResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->RevisionQuery(&clientContext, request, &response);
    *driverRevision = response.driver_revision();
    *firmwareRevision = response.firmware_revision();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SendSoftwareTrigger(const std::string& srcTerminal, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SendSoftwareTriggerRequest request;
    nisync::SendSoftwareTriggerResponse response;
    request.set_src_terminal(srcTerminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SendSoftwareTrigger(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_ConnectClkTerminals(const std::string& srcTerminal, const std::string& destTerminal, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ConnectClkTerminalsRequest request;
    nisync::ConnectClkTerminalsResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ConnectClkTerminals(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_DisconnectClkTerminals(const std::string& srcTerminal, const std::string& destTerminal, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::DisconnectClkTerminalsRequest request;
    nisync::DisconnectClkTerminalsResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->DisconnectClkTerminals(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_ConnectSWTrigToTerminal(
      const std::string& srcTerminal,
      const std::string& destTerminal,
      const std::string& syncClock,
      int32 invert,
      int32 updateEdge,
      double delay,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ConnectSWTrigToTerminalRequest request;
    nisync::ConnectSWTrigToTerminalResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.set_sync_clock(syncClock);
    request.set_invert(invert);
    request.set_update_edge(updateEdge);
    request.set_delay(delay);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ConnectSWTrigToTerminal(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_DisconnectSWTrigFromTerminal(const std::string& srcTerminal, const std::string& destTerminal, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::DisconnectSWTrigFromTerminalRequest request;
    nisync::DisconnectSWTrigFromTerminalResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->DisconnectSWTrigFromTerminal(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_ConnectTrigTerminals(
      const std::string& srcTerminal,
      const std::string& destTerminal,
      const std::string& syncClock,
      int32 invert,
      int32 updateEdge,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ConnectTrigTerminalsRequest request;
    nisync::ConnectTrigTerminalsResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.set_sync_clock(syncClock);
    request.set_invert(invert);
    request.set_update_edge(updateEdge);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ConnectTrigTerminals(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_DisconnectTrigTerminals(const std::string& srcTerminal, const std::string& destTerminal, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::DisconnectTrigTerminalsRequest request;
    nisync::DisconnectTrigTerminalsResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_dest_terminal(destTerminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->DisconnectTrigTerminals(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetAttributeViInt32(const std::string& activeItem, uint32 attribute, int32 value, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetAttributeViInt32Request request;
    nisync::SetAttributeViInt32Response response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.set_value_raw(value);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetAttributeViInt32(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetAttributeViInt32(const std::string& activeItem, uint32 attribute, int32* valueOut, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetAttributeViInt32Request request;
    nisync::GetAttributeViInt32Response response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->GetAttributeViInt32(&clientContext, request, &response);
    *valueOut = response.value();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetAttributeViString(const std::string& activeItem, uint32 attribute, const std::string& value, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetAttributeViStringRequest request;
    nisync::SetAttributeViStringResponse response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.set_value_raw(value);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetAttributeViString(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetAttributeViString(const std::string& activeItem, uint32 attribute, std::string* valueOut, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetAttributeViStringRequest request;
    nisync::GetAttributeViStringResponse response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->GetAttributeViString(&clientContext, request, &response);
    *valueOut = response.value();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetAttributeViBoolean(const std::string& activeItem, uint32 attribute, bool value, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetAttributeViBooleanRequest request;
    nisync::SetAttributeViBooleanResponse response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.set_value(value);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetAttributeViBoolean(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetAttributeViBoolean(const std::string& activeItem, uint32 attribute, bool* valueOut, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetAttributeViBooleanRequest request;
    nisync::GetAttributeViBooleanResponse response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->GetAttributeViBoolean(&clientContext, request, &response);
    *valueOut = response.value();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetAttributeViReal64(const std::string& activeItem, uint32 attribute, double value, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetAttributeViReal64Request request;
    nisync::SetAttributeViReal64Response response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.set_value_raw(value);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetAttributeViReal64(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetAttributeViReal64(const std::string& activeItem, uint32 attribute, double* valueOut, int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetAttributeViReal64Request request;
    nisync::GetAttributeViReal64Response response;
    request.set_active_item(activeItem);
    request.set_attribute(static_cast<nisync::NiSyncAttribute>(attribute));
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->GetAttributeViReal64(&clientContext, request, &response);
    *valueOut = response.value();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_MeasureFrequencyEx(
      const std::string& srcTerminal,
      double duration,
      uint32 decimationCount,
      double* actualDurationOut,
      double* frequencyOut,
      double* frequencyErrorOut,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::MeasureFrequencyExRequest request;
    nisync::MeasureFrequencyExResponse response;
    request.set_src_terminal(srcTerminal);
    request.set_duration(duration);
    request.set_decimation_count(decimationCount);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->MeasureFrequencyEx(&clientContext, request, &response);
    *actualDurationOut = response.actual_duration();
    *frequencyOut = response.frequency();
    *frequencyErrorOut = response.frequency_error();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetTime(
      uint32* timeSeconds,
      uint32* timeNanoseconds,
      uint16* timeFractionalNanoseconds,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetTimeRequest request;
    nisync::GetTimeResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->GetTime(&clientContext, request, &response);
    *timeSeconds = response.time_seconds();
    *timeNanoseconds = response.time_nanoseconds();
    *timeFractionalNanoseconds = response.time_fractional_nanoseconds();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReferenceFreeRunning(int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReferenceFreeRunningRequest request;
    nisync::SetTimeReferenceFreeRunningResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReferenceFreeRunning(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReferenceGPS(int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReferenceGPSRequest request;
    nisync::SetTimeReferenceGPSResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReferenceGPS(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReferenceIRIG(
      int32 irigType,
      const std::string& terminalName,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReferenceIRIGRequest request;
    nisync::SetTimeReferenceIRIGResponse response;
    request.set_irig_type(irigType);
    request.set_terminal_name(terminalName);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReferenceIRIG(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReferencePPS(
      const std::string& terminalName,
      bool useManualTime,
      uint32 initialTimeSeconds,
      uint32 initialTimeNanoseconds,
      uint16 initialTimeFractionalNanoseconds,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReferencePPSRequest request;
    nisync::SetTimeReferencePPSResponse response;
    request.set_terminal_name(terminalName);
    request.set_use_manual_time(useManualTime);
    request.set_initial_time_seconds(initialTimeSeconds);
    request.set_initial_time_nanoseconds(initialTimeNanoseconds);
    request.set_initial_time_fractional_nanoseconds(initialTimeFractionalNanoseconds);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReferencePPS(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReference1588OrdinaryClock(int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReference1588OrdinaryClockRequest request;
    nisync::SetTimeReference1588OrdinaryClockResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReference1588OrdinaryClock(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_SetTimeReference8021AS(int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::SetTimeReference8021ASRequest request;
    nisync::SetTimeReference8021ASResponse response;
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->SetTimeReference8021AS(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_CreateFutureTimeEvent(
      const std::string& terminal,
      int32 outputLevel,
      uint32 timeSeconds,
      uint32 timeNanoseconds,
      uint16 timeFractionalNanoseconds,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::CreateFutureTimeEventRequest request;
    nisync::CreateFutureTimeEventResponse response;
    request.set_terminal(terminal);
    request.set_output_level(outputLevel);
    request.set_time_seconds(timeSeconds);
    request.set_time_nanoseconds(timeNanoseconds);
    request.set_time_fractional_nanoseconds(timeFractionalNanoseconds);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->CreateFutureTimeEvent(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  void CreateFutureTimeEvent(
      const std::string& terminal,
      int32 outputLevel,
      uint32 timeSeconds,
      uint32 timeNanoseconds,
      uint16 timeFractionalNanoseconds)
  {
    int32 viStatus;
    auto grpcStatus = call_CreateFutureTimeEvent(
        terminal,
        outputLevel,
        timeSeconds,
        timeNanoseconds,
        timeFractionalNanoseconds,
        &viStatus);
    EXPECT_TRUE(grpcStatus.ok());
    EXPECT_EQ(VI_SUCCESS, viStatus);
  }

  ::grpc::Status call_ClearFutureTimeEvents(
      const std::string& terminal,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ClearFutureTimeEventsRequest request;
    nisync::ClearFutureTimeEventsResponse response;
    request.set_terminal(terminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ClearFutureTimeEvents(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_CreateClock(
      const std::string& terminal,
      uint32 highTicks,
      uint32 lowTicks,
      uint32 startTimeSeconds,
      uint32 startTimeNanoseconds,
      uint16 startTimeFractionalNanoseconds,
      uint32 stopTimeSeconds,
      uint32 stopTimeNanoseconds,
      uint16 stopTimeFractionalNanoseconds,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::CreateClockRequest request;
    nisync::CreateClockResponse response;
    request.set_terminal(terminal);
    request.set_high_ticks(highTicks);
    request.set_low_ticks(lowTicks);
    request.set_start_time_seconds(startTimeSeconds);
    request.set_start_time_nanoseconds(startTimeNanoseconds);
    request.set_start_time_fractional_nanoseconds(startTimeFractionalNanoseconds);
    request.set_stop_time_seconds(stopTimeSeconds);
    request.set_stop_time_nanoseconds(stopTimeNanoseconds);
    request.set_stop_time_fractional_nanoseconds(stopTimeFractionalNanoseconds);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->CreateClock(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_ClearClock(
      const std::string& terminal,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ClearClockRequest request;
    nisync::ClearClockResponse response;
    request.set_terminal(terminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ClearClock(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_GetTimeReferenceNames(
      std::string* valueOut,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::GetTimeReferenceNamesRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    nisync::GetTimeReferenceNamesResponse response;
    auto grpcStatus = GetStub()->GetTimeReferenceNames(&clientContext, request, &response);
    *valueOut = response.time_reference_names();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_EnableTimeStampTrigger(
      const std::string& terminal,
      int32 activeEdge,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::EnableTimeStampTriggerRequest request;
    nisync::EnableTimeStampTriggerResponse response;
    request.set_terminal(terminal);
    request.set_active_edge(activeEdge);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->EnableTimeStampTrigger(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  void EnableTimeStampTrigger(
      const std::string& terminal,
      int32 activeEdge)
  {
    int32 viStatus;
    auto grpcStatus = call_EnableTimeStampTrigger(terminal, activeEdge, &viStatus);
    EXPECT_TRUE(grpcStatus.ok());
    EXPECT_EQ(VI_SUCCESS, viStatus);
  }

  ::grpc::Status call_ReadTriggerTimeStamp(
      const std::string& terminal,
      double timeout,
      uint32* timeSeconds,
      uint32* timeNanoseconds,
      uint16* timeFractionalNanoseconds,
      int32* detectedEdge,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ReadTriggerTimeStampRequest request;
    nisync::ReadTriggerTimeStampResponse response;
    request.set_terminal(terminal);
    request.set_timeout(timeout);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ReadTriggerTimeStamp(&clientContext, request, &response);
    *timeSeconds = response.time_seconds();
    *timeNanoseconds = response.time_nanoseconds();
    *timeFractionalNanoseconds = response.time_fractional_nanoseconds();
    *detectedEdge = response.detected_edge();
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_ReadMultipleTriggerTimeStamp(
      const std::string& terminal,
      double timeout,
      uint32 timestampsToRead,
      uint32* timeSecondsBuffer,
      uint32* timeNanosecondsBuffer,
      uint16* timeFractionalNanosecondsBuffer,
      int32* detectedEdgeBuffer,
      uint32* timestampsRead,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::ReadMultipleTriggerTimeStampRequest request;
    nisync::ReadMultipleTriggerTimeStampResponse response;
    request.set_terminal(terminal);
    request.set_timeout(timeout);
    request.set_timestamps_to_read(timestampsToRead);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->ReadMultipleTriggerTimeStamp(&clientContext, request, &response);
    *timestampsRead = response.timestamps_read();
    std::copy(response.time_seconds_buffer().begin(), response.time_seconds_buffer().end(), timeSecondsBuffer);
    std::copy(response.time_nanoseconds_buffer().begin(), response.time_nanoseconds_buffer().end(), timeNanosecondsBuffer);
    std::copy(response.time_fractional_nanoseconds_buffer().begin(), response.time_fractional_nanoseconds_buffer().end(), timeFractionalNanosecondsBuffer);
    std::copy(response.detected_edge_buffer().begin(), response.detected_edge_buffer().end(), detectedEdgeBuffer);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  ::grpc::Status call_DisableTimeStampTrigger(
      const std::string& terminal,
      int32* viStatusOut)
  {
    ::grpc::ClientContext clientContext;
    nisync::DisableTimeStampTriggerRequest request;
    nisync::DisableTimeStampTriggerResponse response;
    request.set_terminal(terminal);
    request.mutable_vi()->set_name(driver_session_->name());
    auto grpcStatus = GetStub()->DisableTimeStampTrigger(&clientContext, request, &response);
    *viStatusOut = response.status();
    return grpcStatus;
  }

  uint32 GetCurrentBoardTimeSeconds()
  {
    int32 viStatus;
    uint32 timeSeconds = 0, timeNanoseconds;
    uint16 timeFractionalNanoseconds;
    auto grpcStatus = call_GetTime(
        &timeSeconds,
        &timeNanoseconds,            // ignored
        &timeFractionalNanoseconds,  // ignored
        &viStatus);
    EXPECT_TRUE(grpcStatus.ok());
    EXPECT_EQ(VI_SUCCESS, viStatus);
    return timeSeconds;
  }

  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<nisync::NiSync::Stub> nisync_stub_;
};

class NiSyncDriver6674Test : public NiSyncDriverApiTest {
 public:
  NiSyncDriver6674Test() : NiSyncDriverApiTest() {}
  bool is_PXI6683H() const { return false; }
  const char* get_model_name() const override { return "NI PXIe-6674T"; }
};

class NiSyncDriver6683Test : public NiSyncDriverApiTest {
 public:
  bool is_PXI6683H() const { return true; }
  NiSyncDriver6683Test() : NiSyncDriverApiTest() {}
  const char* get_model_name() const override { return "NI PXI-6683H"; }
};

TEST_F(NiSyncDriver6674Test, RevisionQuery_ReturnsNonEmptyRevisions)
{
  int32 viStatus;
  std::string driverRevision, firmwareRevision;
  auto grpcStatus = call_RevisionQuery(&driverRevision, &firmwareRevision, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_FALSE(driverRevision.empty());
  EXPECT_FALSE(firmwareRevision.empty());
}

TEST_F(NiSyncDriver6674Test, ConnectClkTerminals_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_OSCILLATOR, destTerminal = NISYNC_VAL_CLKOUT;
  auto grpcStatus = call_ConnectClkTerminals(srcTerminal, destTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectClkTerminals(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectInvalidClkTerminals_ReturnsInvalidSrcTerminal)
{
  int32 viStatus;
  auto srcTerminal = INVALID_TERMINAL, destTerminal = NISYNC_VAL_CLKOUT;
  auto grpcStatus = call_ConnectClkTerminals(srcTerminal, destTerminal, &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectedClkTerminals_DisconnectClkTerminals_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_OSCILLATOR, destTerminal = NISYNC_VAL_CLKOUT;
  auto grpcStatus = call_ConnectClkTerminals(srcTerminal, destTerminal, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  grpcStatus = call_DisconnectClkTerminals(srcTerminal, destTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectedClkTerminals_DisconnectNotConnectedClkTerminals_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_OSCILLATOR, destTerminal = NISYNC_VAL_CLKOUT;
  auto grpcStatus = call_ConnectClkTerminals(srcTerminal, destTerminal, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  auto notConnectedSrcTerminal = NISYNC_VAL_CLKIN;
  grpcStatus = call_DisconnectClkTerminals(notConnectedSrcTerminal, destTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectClkTerminals(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectSWTrigToTerminal_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_SWTRIG_GLOBAL, destTerminal = NISYNC_VAL_PXIEDSTARC;
  auto syncClock = NISYNC_VAL_SYNC_CLK_FULLSPEED;
  int32 invert = true, updateEdge = false;
  double delay = 0;
  auto grpcStatus = call_ConnectSWTrigToTerminal(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      delay,
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectSWTrigFromTerminal(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectInvalidSWTrigToTerminal_ReturnsInvalidSrcTerminal)
{
  int32 viStatus;
  auto srcTerminal = INVALID_TERMINAL, destTerminal = NISYNC_VAL_PXIEDSTARC;
  auto syncClock = NISYNC_VAL_SYNC_CLK_FULLSPEED;
  int32 invert = true, updateEdge = false;
  double delay = 0;
  auto grpcStatus = call_ConnectSWTrigToTerminal(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      delay,
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectedSWTrigToTerminal_DisconnectSWTrigFromTerminal_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_SWTRIG_GLOBAL, destTerminal = NISYNC_VAL_PXIEDSTARC;
  auto syncClock = NISYNC_VAL_SYNC_CLK_FULLSPEED;
  int32 invert = true, updateEdge = false;
  double delay = 0;
  auto grpcStatus = call_ConnectSWTrigToTerminal(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      delay,
      &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  grpcStatus = call_DisconnectSWTrigFromTerminal(srcTerminal, destTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, SWTrigConnectedToTerminal_DisconnectSWTrigFromNotConnectedTerminal_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_SWTRIG_GLOBAL, destTerminal = NISYNC_VAL_PXIEDSTARC;
  auto syncClock = NISYNC_VAL_SYNC_CLK_FULLSPEED;
  int32 invert = true, updateEdge = false;
  double delay = 0;
  auto grpcStatus = call_ConnectSWTrigToTerminal(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      delay,
      &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  auto notConnectedDestTerminal = NISYNC_VAL_CLK100;
  grpcStatus = call_DisconnectSWTrigFromTerminal(srcTerminal, notConnectedDestTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectSWTrigFromTerminal(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, SendSoftwareTrigger_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_SWTRIG_GLOBAL;
  auto grpcStatus = call_SendSoftwareTrigger(srcTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, SendSoftwareTriggerOnInvalidTerminal_ReturnsInvalidSrcTerminal)
{
  int32 viStatus;
  auto srcTerminal = INVALID_TERMINAL;
  auto grpcStatus = call_SendSoftwareTrigger(srcTerminal, &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectTrigTerminals_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_PFI0, destTerminal = NISYNC_VAL_PFI1;
  auto syncClock = NISYNC_VAL_SYNC_CLK_ASYNC;
  int32 invert = false, updateEdge = false;
  auto grpcStatus = call_ConnectTrigTerminals(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectTrigTerminals(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectInvalidTrigTerminals_ReturnsInvalidSrcTerminal)
{
  int32 viStatus;
  auto srcTerminal = INVALID_TERMINAL, destTerminal = NISYNC_VAL_CLKOUT;
  auto syncClock = NISYNC_VAL_SYNC_CLK_ASYNC;
  int32 invert = false, updateEdge = false;
  auto grpcStatus = call_ConnectTrigTerminals(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, ConnectedTrigTerminals_DisconnectTrigTerminals_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_PFI0, destTerminal = NISYNC_VAL_PFI1;
  auto syncClock = NISYNC_VAL_SYNC_CLK_ASYNC;
  int32 invert = false, updateEdge = false;
  auto grpcStatus = call_ConnectTrigTerminals(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  grpcStatus = call_DisconnectTrigTerminals(srcTerminal, destTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6674Test, NotConnectedTrigTerminals_DisconnectSWTrigFromTerminal_ReturnsSuccess)
{
  int32 viStatus;
  auto srcTerminal = NISYNC_VAL_PFI0, destTerminal = NISYNC_VAL_PFI1;
  auto syncClock = NISYNC_VAL_SYNC_CLK_ASYNC;
  int32 invert = false, updateEdge = false;
  auto grpcStatus = call_ConnectTrigTerminals(
      srcTerminal,
      destTerminal,
      syncClock,
      invert,
      updateEdge,
      &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  auto notConnectedDestTerminal = NISYNC_VAL_CLK100;
  grpcStatus = call_DisconnectTrigTerminals(srcTerminal, notConnectedDestTerminal, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  call_DisconnectTrigTerminals(srcTerminal, destTerminal, &viStatus);
}

TEST_F(NiSyncDriver6674Test, AttributeSet_GetAttributeViInt32_ReturnsValue)
{
  int32 viStatus;
  auto activeItem = "";
  uint32 attribute = nisync_grpc::NISYNC_ATTRIBUTE_SYNC_CLK_DIV1;
  int32 expectedValue = NISYNC_VAL_1588_CLK_ACCURACY_WITHIN_1_USEC;
  auto grpcStatus = call_SetAttributeViInt32(activeItem, attribute, expectedValue, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  int32 value;
  grpcStatus = call_GetAttributeViInt32(activeItem, attribute, &value, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_EQ(expectedValue, value);
}

TEST_F(NiSyncDriver6674Test, AttributeSet_GetAttributeViString_ReturnsValue)
{
  int32 viStatus;
  auto activeItem = "";
  uint32 attribute = nisync_grpc::NISYNC_ATTRIBUTE_FRONT_SYNC_CLK_SRC;
  const std::string& expectedValue = NISYNC_VAL_CLK10;
  auto grpcStatus = call_SetAttributeViString(activeItem, attribute, expectedValue, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  std::string value;
  grpcStatus = call_GetAttributeViString(activeItem, attribute, &value, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_STREQ(expectedValue.c_str(), value.c_str());
}

TEST_F(NiSyncDriver6674Test, AttributeSet_GetAttributeViBoolean_ReturnsValue)
{
  int32 viStatus;
  auto activeItem = "";
  uint32 attribute = nisync_grpc::NISYNC_ATTRIBUTE_CLKIN_ATTENUATION_DISABLE;
  bool expectedValue = true;
  auto grpcStatus = call_SetAttributeViBoolean(activeItem, attribute, expectedValue, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  bool value;
  grpcStatus = call_GetAttributeViBoolean(activeItem, attribute, &value, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_EQ(expectedValue, value);
}

TEST_F(NiSyncDriver6674Test, AttributeSet_GetAttributeViReal64_ReturnsValue)
{
  int32 viStatus;
  auto activeItem = "";
  uint32 attribute = nisync_grpc::NISYNC_ATTRIBUTE_PFI0_THRESHOLD;
  double expectedValue = 2.3;
  auto grpcStatus = call_SetAttributeViReal64(activeItem, attribute, expectedValue, &viStatus);
  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  double value;
  grpcStatus = call_GetAttributeViReal64(activeItem, attribute, &value, &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  // 6674T has up to 16.8mV of resolution for PFI threshold. We'll loosen our
  // validation to a bit more than twice that to ensure we aren't testing
  // driver implementation details.
  EXPECT_NEAR(expectedValue, value, 50e-3);
}

TEST_F(NiSyncDriver6674Test, MeasureFrequencyExOnTerminalWithNoFrequency_ReturnsNoFrequency)
{
  int32 viStatus;
  const std::string& srcTerminal = NISYNC_VAL_PFI0;
  double duration = 0.1;       // duration is in seconds
  uint32 decimationCount = 0;  // ignored for 6674
  double actualDuration, frequency, frequencyError;
  auto grpcStatus = call_MeasureFrequencyEx(
      srcTerminal,
      duration,
      decimationCount,
      &actualDuration,
      &frequency,
      &frequencyError,
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_EQ(0, actualDuration);
  EXPECT_EQ(0, frequency);
}

TEST_F(NiSyncDriver6674Test, MeasureFrequencyExOnOscillatorWithFrequency_ReturnsFrequency)
{
  int32 viStatus;
  const std::string& srcTerminal = NISYNC_VAL_OSCILLATOR;
  double duration = 0.1;       // duration is in seconds
  uint32 decimationCount = 0;  // ignored for 6674
  double actualDuration, frequency, frequencyError;
  auto grpcStatus = call_MeasureFrequencyEx(
      srcTerminal,
      duration,
      decimationCount,
      &actualDuration,
      &frequency,
      &frequencyError,
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_GT(actualDuration, 0);
  EXPECT_GT(frequency, 0);
}

TEST_F(NiSyncDriver6683Test, GetTime_ReturnsTime)
{
  int32 viStatus;
  uint32 timeSeconds, timeNanoseconds;
  uint16 timeFractionalNanoseconds;
  auto grpcStatus = call_GetTime(
      &timeSeconds,
      &timeNanoseconds,
      &timeFractionalNanoseconds,  // ignored
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
  EXPECT_GT(timeSeconds, (uint32)0);
  EXPECT_GT(timeNanoseconds, (uint32)0);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferenceFreeRunning_ReturnsSuccess)
{
  int32 viStatus;
  auto grpcStatus = call_SetTimeReferenceFreeRunning(&viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferenceGPS_ReturnsSuccess)
{
  int32 viStatus;
  auto grpcStatus = call_SetTimeReferenceGPS(&viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferenceIRIG_ReturnsSuccess)
{
  int32 viStatus;
  auto grpcStatus = call_SetTimeReferenceIRIG(
      NISYNC_VAL_IRIG_TYPE_IRIGB_DC,  // irigType
      NISYNC_VAL_PFI0,                // terminalName
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferenceIRIGWithInvalidTerminal_ReturnsError)
{
  int32 viStatus;
  auto grpcStatus = call_SetTimeReferenceIRIG(
      NISYNC_VAL_IRIG_TYPE_IRIGB_DC,  // irigType
      NISYNC_VAL_GND,                 // terminalName
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferencePPS_ReturnsSuccess)
{
  int32 viStatus;
  uint32 initialTimeSeconds = 30, initialTimeNanoseconds = 500;
  auto grpcStatus = call_SetTimeReferencePPS(
      NISYNC_VAL_PFI1,  // terminalName
      true,             // useManualTime
      initialTimeSeconds,
      initialTimeNanoseconds,
      0,  // initialTimeFractionalNanoseconds, ignored
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);

  // Switch back to free-running to free up the PFI line.
  viStatus = VI_SUCCESS;
  grpcStatus = call_SetTimeReferenceFreeRunning(&viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReferencePPSWithInvalidTerminal_ReturnsError)
{
  int32 viStatus;
  uint32 initialTimeSeconds = 30, initialTimeNanoseconds = 500;
  auto grpcStatus = call_SetTimeReferencePPS(
      NISYNC_VAL_GND,  // terminalName
      true,            // useManualTime
      initialTimeSeconds,
      initialTimeNanoseconds,
      0,  // initialTimeFractionalNanoseconds, ignored
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReference1588OrdinaryClock_ReturnsSuccess)
{
  int32 viStatus;
  auto grpcStatus = call_SetTimeReference1588OrdinaryClock(&viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, SetTimeReference8021AS_ReturnsSuccess)
{
  // SetTimeReference8021AS is only supported in LinuxRT targets.
  int32 viStatus;
  auto grpcStatus = call_SetTimeReference8021AS(&viStatus);

#if defined(_MSC_VER)
  // SetTimeReference8021AS is only supported on Linux RT targets.
  EXPECT_SYNC_ERROR(NISYNC_ERROR_FEATURE_NOT_SUPPORTED_MESSAGE, grpcStatus);
#else
  EXPECT_TRUE(grpcStatus.ok());
#endif
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, CreateClearFutureTimeEvent_ReturnsSuccess)
{
  int32 viStatusCreate;
  uint32 timeSeconds = GetCurrentBoardTimeSeconds() + 30;
  auto grpcStatusCreate = call_CreateFutureTimeEvent(
      NISYNC_VAL_PFI1,       // terminalName
      NISYNC_VAL_LEVEL_LOW,  // outputLevel
      timeSeconds,
      0,  // timeNanoseconds, ignored
      0,  // timeFractionalNanoseconds, ignored
      &viStatusCreate);
  EXPECT_TRUE(grpcStatusCreate.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusCreate);

  int32 viStatusClear;
  auto grpcStatusClear = call_ClearFutureTimeEvents(
      NISYNC_VAL_PFI1,
      &viStatusClear);
  EXPECT_TRUE(grpcStatusClear.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusClear);
}

TEST_F(NiSyncDriver6683Test, CreateFutureTimeEventWithInvalidTerminal_ReturnsError)
{
  int32 viStatus;
  uint32 timeSeconds = GetCurrentBoardTimeSeconds() + 30;
  auto grpcStatus = call_CreateFutureTimeEvent(
      NISYNC_VAL_GND,        // terminalName
      NISYNC_VAL_LEVEL_LOW,  // outputLevel
      timeSeconds,
      0,  // timeNanoseconds, ignored
      0,  // timeFractionalNanoseconds, ignored
      &viStatus);

// Bug 1462752: 6683 CreateFutureTimeEvent has different error behavior on Linux RT
#if defined(_MSC_VER)
  EXPECT_SYNC_ERROR(NISYNC_ERROR_TERMINAL_INVALID_MESSAGE, grpcStatus);
#else
  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
#endif
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, ClearFutureTimeEventsNotReserved_ReturnsError)
{
  int32 viStatus;
  auto grpcStatus = call_ClearFutureTimeEvents(
      NISYNC_VAL_PFI1,  // terminalName
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_RSRC_NOT_RESERVED_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, CreateClearClock_ReturnsSuccess)
{
  int32 viStatusCreate;
  uint32 highTicks = 50, lowTicks = 50;
  uint32 startTimeSeconds = GetCurrentBoardTimeSeconds() + 30;
  uint32 stopTimeSeconds = startTimeSeconds + 30;
  auto grpcStatusCreate = call_CreateClock(
      NISYNC_VAL_PFI1,  // terminalName
      highTicks,
      lowTicks,
      startTimeSeconds,
      0,  // startTimeNanoseconds, ignored
      0,  // startTimeFractionalNanoseconds, ignored
      stopTimeSeconds,
      0,  // stopTimeNanoseconds, ignored
      0,  // stopTimeFractionalNanoseconds, ignored
      &viStatusCreate);
  EXPECT_TRUE(grpcStatusCreate.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusCreate);

  int32 viStatusClear;
  auto grpcStatusClear = call_ClearClock(
      NISYNC_VAL_PFI1,
      &viStatusClear);
  EXPECT_TRUE(grpcStatusClear.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusClear);
}

TEST_F(NiSyncDriver6683Test, CreateClockWithInvalidTerminal_ReturnsError)
{
  int32 viStatus;
  uint32 highTicks = 50, lowTicks = 50;
  uint32 startTimeSeconds = GetCurrentBoardTimeSeconds() + 30;
  uint32 stopTimeSeconds = startTimeSeconds + 30;
  auto grpcStatus = call_CreateClock(
      NISYNC_VAL_GND,  // terminalName
      highTicks,
      lowTicks,
      startTimeSeconds,
      0,  // startTimeNanoseconds, ignored
      0,  // startTimeFractionalNanoseconds, ignored
      stopTimeSeconds,
      0,  // stopTimeNanoseconds, ignored
      0,  // stopTimeFractionalNanoseconds, ignored
      &viStatus);

// Bug 1462754: 6683 CreateClock has different error behavior on Linux RT
#if defined(_MSC_VER)
  EXPECT_SYNC_ERROR(NISYNC_ERROR_TERMINAL_INVALID_MESSAGE, grpcStatus);
#else
  EXPECT_SYNC_ERROR(NISYNC_ERROR_SRC_TERMINAL_INVALID_MESSAGE, grpcStatus);
#endif
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, ClearClockNotReserved_ReturnsError)
{
  int32 viStatus;
  auto grpcStatus = call_ClearClock(
      NISYNC_VAL_PFI1,  // terminalName
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_RSRC_NOT_RESERVED_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, GetTimeReferenceNames_ReturnsSuccess)
{
  int32 viStatus;
  std::string timeReferenceNames;
  auto grpcStatus = call_GetTimeReferenceNames(
      &timeReferenceNames,
      &viStatus);

  EXPECT_TRUE(grpcStatus.ok());
  EXPECT_GT(timeReferenceNames.length(), 0);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, EnableTimeStampTrigger_ReturnsSuccess)
{
  int32 viStatusEnable;
  auto grpcStatusEnable = call_EnableTimeStampTrigger(
      NISYNC_VAL_PFI1,         // terminalName
      NISYNC_VAL_EDGE_RISING,  // activeEdge
      &viStatusEnable);
  EXPECT_TRUE(grpcStatusEnable.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusEnable);

  int32 viStatusDisable;
  auto grpcStatusDisable = call_DisableTimeStampTrigger(
      NISYNC_VAL_PFI1,
      &viStatusDisable);
  EXPECT_TRUE(grpcStatusDisable.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusDisable);
}

TEST_F(NiSyncDriver6683Test, EnableTimeStampTriggerWithInvalidTerminal_ReturnsError)
{
  int32 viStatus;
  auto grpcStatus = call_EnableTimeStampTrigger(
      NISYNC_VAL_GND,          // terminalName
      NISYNC_VAL_EDGE_RISING,  // activeEdge
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_TERMINAL_INVALID_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, DisableTimeStampTriggerNotReserved_ReturnsError)
{
  int32 viStatus;
  auto grpcStatus = call_DisableTimeStampTrigger(
      NISYNC_VAL_PFI1,  // terminalName
      &viStatus);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_RSRC_NOT_RESERVED_MESSAGE, grpcStatus);
  EXPECT_EQ(VI_SUCCESS, viStatus);
}

TEST_F(NiSyncDriver6683Test, GivenNoTrigger_ReadTriggerTimeStamp_ReturnsTimeoutError)
{
  auto terminal = NISYNC_VAL_PFI1;
  EnableTimeStampTrigger(terminal, NISYNC_VAL_EDGE_RISING);

  int32 viStatusRead;
  double timeout = 0.1;
  uint32 timeSeconds, timeNanoseconds;
  uint16 timeFractionalNanoseconds;
  int32 detectedEdge;
  auto grpcStatusRead = call_ReadTriggerTimeStamp(
      terminal,
      timeout,
      &timeSeconds,
      &timeNanoseconds,
      &timeFractionalNanoseconds,
      &detectedEdge,
      &viStatusRead);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_DRIVER_TIMEOUT_MESSAGE, grpcStatusRead);
  EXPECT_EQ(VI_SUCCESS, viStatusRead);
}

TEST_F(NiSyncDriver6683Test, GivenNoTrigger_ReadMultipleTriggerTimeStamp_ReturnsTimeoutError)
{
  auto terminal = NISYNC_VAL_PFI1;
  EnableTimeStampTrigger(terminal, NISYNC_VAL_EDGE_RISING);

  int32 viStatusRead;
  double timeout = 0.1;
  uint32 timestampsToRead = 1;
  uint32 timeSeconds, timeNanoseconds;
  uint16 timeFractionalNanoseconds;
  int32 detectedEdge;
  uint32 timestampsRead;
  auto grpcStatusRead = call_ReadMultipleTriggerTimeStamp(
      terminal,
      timeout,
      timestampsToRead,
      &timeSeconds,
      &timeNanoseconds,
      &timeFractionalNanoseconds,
      &detectedEdge,
      &timestampsRead,
      &viStatusRead);

  EXPECT_TRUE(grpcStatusRead.ok());
  EXPECT_EQ(NISYNC_ERROR_DRIVER_TIMEOUT, viStatusRead);
}

TEST_F(NiSyncDriver6683Test, GivenOneTrigger_ReadMultipleTriggerTimeStamp_ReturnsOneTimeStampAndTimeoutError)
{
  auto terminal = NISYNC_VAL_PFI1;
  // Ensure terminal level is low before enabling timestamping
  CreateFutureTimeEvent(terminal, NISYNC_VAL_LEVEL_LOW, 0, 0, 0);
  EnableTimeStampTrigger(terminal, NISYNC_VAL_EDGE_RISING);
  CreateFutureTimeEvent(terminal, NISYNC_VAL_LEVEL_HIGH, 0, 0, 0);
  CreateFutureTimeEvent(terminal, NISYNC_VAL_LEVEL_LOW, 0, 0, 0);

  int32 viStatusRead;
  double timeout = 1.0;
  const uint32 timestampsToRead = 5;
  uint32 timeSeconds[timestampsToRead] = {}, timeNanoseconds[timestampsToRead] = {};
  uint16 timeFractionalNanoseconds[timestampsToRead] = {};
  int32 detectedEdge[timestampsToRead] = {};
  uint32 timestampsRead = 0;
  auto grpcStatusRead = call_ReadMultipleTriggerTimeStamp(
      terminal,
      timeout,
      timestampsToRead,
      timeSeconds,
      timeNanoseconds,
      timeFractionalNanoseconds,
      detectedEdge,
      &timestampsRead,
      &viStatusRead);

  const uint32 expectedTimestampsRead = 1;
  EXPECT_TRUE(grpcStatusRead.ok());
  EXPECT_EQ(NISYNC_ERROR_DRIVER_TIMEOUT, viStatusRead);
  EXPECT_EQ(expectedTimestampsRead, timestampsRead);
  EXPECT_NE(0, timeSeconds[0]);
  EXPECT_EQ(NISYNC_VAL_EDGE_RISING, detectedEdge[0]);
}

TEST_F(NiSyncDriver6683Test, GivenFiveTriggers_ReadMultipleTriggerTimeStamp_ReturnsFiveTimeStamps)
{
  auto terminal = NISYNC_VAL_PFI1;
  // Ensure terminal level is low before enabling timestamping
  CreateFutureTimeEvent(terminal, NISYNC_VAL_LEVEL_LOW, 0, 0, 0);
  EnableTimeStampTrigger(terminal, NISYNC_VAL_EDGE_RISING);
  // Create 5 pulses
  int32 level = NISYNC_VAL_LEVEL_HIGH;
  for (int i = 0; i < 10; ++i) {
    SCOPED_TRACE(::testing::Message("i=") << i);
    CreateFutureTimeEvent(terminal, level, 0, 0, 0);
    level = (level == NISYNC_VAL_LEVEL_LOW) ? NISYNC_VAL_LEVEL_HIGH : NISYNC_VAL_LEVEL_LOW;
  }

  int32 viStatusRead;
  double timeout = 1.0;
  const uint32 timestampsToRead = 5;
  uint32 timeSeconds[timestampsToRead] = {}, timeNanoseconds[timestampsToRead] = {};
  uint16 timeFractionalNanoseconds[timestampsToRead] = {};
  int32 detectedEdge[timestampsToRead] = {};
  uint32 timestampsRead = 0;
  auto grpcStatusRead = call_ReadMultipleTriggerTimeStamp(
      terminal,
      timeout,
      timestampsToRead,
      timeSeconds,
      timeNanoseconds,
      timeFractionalNanoseconds,
      detectedEdge,
      &timestampsRead,
      &viStatusRead);

  EXPECT_TRUE(grpcStatusRead.ok());
  EXPECT_EQ(VI_SUCCESS, viStatusRead);
  EXPECT_EQ(timestampsToRead, timestampsRead);
  for (uint32 i = 0; i < timestampsRead; ++i) {
    SCOPED_TRACE(::testing::Message("i=") << i);
    EXPECT_NE(0, timeSeconds[i]);
    EXPECT_EQ(NISYNC_VAL_EDGE_RISING, detectedEdge[i]);
  }
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nisync_session_tests.cpp sha256=416f2bdbf3d18ae766c24112c9a57a151a40fce68ef181f89a177dbf648ae093 bytes=4199 -->
## FILE: source/tests/system/nisync_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nisync_session_tests.cpp`
- sha256: `416f2bdbf3d18ae766c24112c9a57a151a40fce68ef181f89a177dbf648ae093`
- bytes: 4199

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nisync/nisync_client.h"

namespace ni {
namespace tests {
namespace system {

namespace nisync = nisync_grpc;

constexpr auto NISYNC_ERROR_DEVICE_NOT_FOUND_MESSAGE = "The specified device was not found.";
static const int kSyncDeviceNotFound = -1074118634;
static const char* kTestSessionName = "TestSession";
static const char* kEmptySessionName = "";
static const char* kInvalidRsrcName = "InvalidName";

inline static void EXPECT_SYNC_ERROR(const std::string& error_message, const ::grpc::Status& status)
{
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(error_message, status.error_message());
}

class NiSyncSessionTest : public ::testing::Test {
 protected:
  std::string test_resource_name;

  NiSyncSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nisync_stub_(nisync::NiSync::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  void SetUp() override
  {
    for (const auto& device : EnumerateDevices()) {
      if ((device.model() == "NI PXI-6683H") || (device.model() == "NI PXIe-6674T")) {
        test_resource_name = device.name();
        break;
      }
    }

    if (test_resource_name.empty()) {
      GTEST_SKIP() << "No device found";
    }
  }

  virtual ~NiSyncSessionTest() {}

  std::unique_ptr<nisync::NiSync::Stub>& GetStub()
  {
    return nisync_stub_;
  }

  ::grpc::Status call_init(const char* resource_name, const char* session_name, nisync::InitResponse* response)
  {
    ::grpc::ClientContext context;
    nisync::InitRequest request;
    request.set_resource_name(resource_name);
    request.set_session_name(session_name);
    request.set_reset_device(false);

    ::grpc::Status status = GetStub()->Init(&context, request, response);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<nisync::NiSync::Stub> nisync_stub_;
};

TEST_F(NiSyncSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  nisync::InitResponse response;
  ::grpc::Status status = call_init(test_resource_name.c_str(), kTestSessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiSyncSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  nisync::InitResponse response;
  ::grpc::Status status = call_init(test_resource_name.c_str(), kEmptySessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiSyncSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  nisync::InitResponse response;
  ::grpc::Status status = call_init(kInvalidRsrcName, kEmptySessionName, &response);

  EXPECT_SYNC_ERROR(NISYNC_ERROR_DEVICE_NOT_FOUND_MESSAGE, status);
  EXPECT_EQ("", response.vi().name());
}

TEST_F(NiSyncSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  nisync::InitResponse init_response;
  call_init(test_resource_name.c_str(), kEmptySessionName, &init_response);
  nidevice_grpc::Session session = init_response.vi();
  EXPECT_EQ(0, init_response.status());

  ::grpc::ClientContext context;
  nisync::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  nisync::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiSyncSessionTest, InvalidSession_CloseSession_NoErrorReported)
{
  nidevice_grpc::Session session;
  session.set_name("");

  ::grpc::ClientContext context;
  nisync::CloseRequest request;
  request.mutable_vi()->set_name(session.name());
  nisync::CloseResponse response;
  ::grpc::Status status = GetStub()->Close(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nitclk_driver_api_tests.cpp sha256=57ebba46bb76258efe2c03379f404b7433244845fc6625c7be79e255741a60ee bytes=9160 -->
## FILE: source/tests/system/nitclk_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nitclk_driver_api_tests.cpp`
- sha256: `57ebba46bb76258efe2c03379f404b7433244845fc6625c7be79e255741a60ee`
- bytes: 9160

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "niscope/niscope_client.h"
#include "nitclk/nitclk_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace scope = niscope_grpc;
namespace tclk = nitclk_grpc;
namespace pb = ::google::protobuf;

typedef pb::int32 int32;
typedef pb::uint32 uint32;
typedef pb::uint16 uint16;

const int kScopeDriverApiSuccess = 0;
const int kTClkDriverApiSuccess = 0;

class NiTClkDriverApiTest : public ::testing::Test {
 protected:
  NiTClkDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nitclk_stub_(tclk::NiTClk::NewStub(device_server_->InProcessChannel())),
        niscope_stub_(scope::NiScope::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiTClkDriverApiTest() {}

  void SetUp() override
  {
    initialize_scope_session();
  }

  void TearDown() override
  {
    close_scope_session();
  }

  std::unique_ptr<scope::NiScope::Stub>& GetScopeStub()
  {
    return niscope_stub_;
  }

  std::unique_ptr<tclk::NiTClk::Stub>& GetTClkStub()
  {
    return nitclk_stub_;
  }

  std::string GetScopeSessionName()
  {
    return scope_session_->name();
  }

  void initialize_scope_session()
  {
    ::grpc::ClientContext context;
    scope::InitWithOptionsRequest request;
    request.set_resource_name("FakeDevice");
    request.set_option_string("Simulate=1, DriverSetup=Model:5164; BoardType:PXIe");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_id_query(false);
    scope::InitWithOptionsResponse response;

    ::grpc::Status status = GetScopeStub()->InitWithOptions(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    scope_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  }

  void close_scope_session()
  {
    ::grpc::ClientContext context;
    scope::CloseRequest request;
    request.mutable_vi()->set_name(scope_session_->name());
    scope::CloseResponse response;

    ::grpc::Status status = GetScopeStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kScopeDriverApiSuccess, response.status());
  }

  double get_real64_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    tclk::GetAttributeViReal64Request request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    tclk::GetAttributeViReal64Response response;

    ::grpc::Status status = GetTClkStub()->GetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
    return response.value();
  }

  std::string get_session_name_from_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    tclk::GetAttributeViSessionRequest request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    tclk::GetAttributeViSessionResponse response;

    ::grpc::Status status = GetTClkStub()->GetAttributeViSession(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
    return response.value().name();
  }

  std::string get_string_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    tclk::GetAttributeViStringRequest request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    tclk::GetAttributeViStringResponse response;

    ::grpc::Status status = GetTClkStub()->GetAttributeViString(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
    return response.value();
  }

  void set_real64_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id, const double attribute_value)
  {
    ::grpc::ClientContext context;
    tclk::SetAttributeViReal64Request request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    request.set_value_raw(attribute_value);
    tclk::SetAttributeViReal64Response response;

    ::grpc::Status status = GetTClkStub()->SetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
  }

  void set_session_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id, const std::string& session_name)
  {
    ::grpc::ClientContext context;
    tclk::SetAttributeViSessionRequest request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    request.mutable_value()->set_name(session_name);
    tclk::SetAttributeViSessionResponse response;

    ::grpc::Status status = GetTClkStub()->SetAttributeViSession(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
  }

  void set_string_attribute(const char* channel_name, tclk::NiTClkAttribute attribute_id, const std::string attribute_value)
  {
    ::grpc::ClientContext context;
    tclk::SetAttributeViStringRequest request;
    request.mutable_session()->set_name(GetScopeSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    request.set_value_raw(attribute_value);
    tclk::SetAttributeViStringResponse response;

    ::grpc::Status status = GetTClkStub()->SetAttributeViString(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kTClkDriverApiSuccess, response.status());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> scope_session_;
  std::unique_ptr<scope::NiScope::Stub> niscope_stub_;
  std::unique_ptr<tclk::NiTClk::Stub> nitclk_stub_;
};

TEST_F(NiTClkDriverApiTest, ConfigureForHomogeneousTriggers_ReturnsStatusAsSuccessful)
{
  ::grpc::ClientContext context;
  tclk::ConfigureForHomogeneousTriggersRequest request;
  request.add_sessions()->set_name(GetScopeSessionName());
  tclk::ConfigureForHomogeneousTriggersResponse response;
  ::grpc::Status status = GetTClkStub()->ConfigureForHomogeneousTriggers(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kTClkDriverApiSuccess, response.status());
}

TEST_F(NiTClkDriverApiTest, SetupForSyncPulseSenderSynchronize_ReturnsStatusAsSuccessful)
{
  ::grpc::ClientContext context;
  tclk::SetupForSyncPulseSenderSynchronizeRequest request;
  request.add_sessions()->set_name(GetScopeSessionName());
  tclk::SetupForSyncPulseSenderSynchronizeResponse response;
  ::grpc::Status status = GetTClkStub()->SetupForSyncPulseSenderSynchronize(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kTClkDriverApiSuccess, response.status());
}

TEST_F(NiTClkDriverApiTest, SetAttributeViReal64_CallGetAttributeViReal64_ValuesMatch)
{
  const char* channel_name = "";
  const tclk::NiTClkAttribute attribute_to_set = tclk::NiTClkAttribute::NITCLK_ATTRIBUTE_SAMPLE_CLOCK_DELAY;
  const double expected_value = 4.24;
  set_real64_attribute(channel_name, attribute_to_set, expected_value);

  double get_attribute_value = get_real64_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiTClkDriverApiTest, SetAttributeViSession_CallGetAttributeViSession_ValuesMatch)
{
  const char* channel_name = "";
  const tclk::NiTClkAttribute attribute_to_set = tclk::NiTClkAttribute::NITCLK_ATTRIBUTE_START_TRIGGER_MASTER_SESSION;
  auto expected_value = GetScopeSessionName();
  set_session_attribute(channel_name, attribute_to_set, expected_value);

  auto get_attribute_value = get_session_name_from_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiTClkDriverApiTest, SetAttributeViString_CallGetAttributeViString_ValuesMatch)
{
  const char* channel_name = "";
  const tclk::NiTClkAttribute attribute_to_set = tclk::NiTClkAttribute::NITCLK_ATTRIBUTE_SYNC_PULSE_SOURCE;
  const std::string expected_value = "Hello world!";
  set_string_attribute(channel_name, attribute_to_set, expected_value);

  std::string get_attribute_value = get_string_attribute(channel_name, attribute_to_set);

  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nixnet_can_driver_api_tests.cpp sha256=549ee8842c8a62df5e04973ef9890bccc5a55d25ede56789063bfa18de168502 bytes=6619 -->
## FILE: source/tests/system/nixnet_can_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nixnet_can_driver_api_tests.cpp`
- sha256: `549ee8842c8a62df5e04973ef9890bccc5a55d25ede56789063bfa18de168502`
- bytes: 6619

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nixnet/nixnet_client.h>

#include <iostream>
#include <string>
#include <vector>

#include "device_server.h"
#include "nixnet_utilities.h"

using namespace nixnet_grpc;
namespace client = nixnet_grpc::experimental::client;
using namespace ::testing;
using namespace ::nixnet_utilities;

namespace ni {
namespace tests {
namespace system {
namespace {

using u8 = ::google::protobuf::uint8;
using u32 = ::google::protobuf::uint32;
using u64 = ::google::protobuf::uint64;
using f64 = double;

class NiXnetCANDriverApiTests : public ::testing::Test {
 protected:
  NiXnetCANDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiXnet::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiXnetCANDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiXnet::Stub>& stub()
  {
    return stub_;
  }

  void assert_can_frames_are_equal(nixnet_grpc::FrameRequest* frame1, nixnet_grpc::FrameResponse* frame2)
  {
    int frame1_flags = calculate_bitwise_or_of_flags(frame1->flags());
    int frame2_flags = calculate_bitwise_or_of_flags(frame2->flags());
    EXPECT_EQ(frame1_flags, frame2_flags);

    EXPECT_EQ(frame1->type(), frame2->type());
    EXPECT_EQ(frame1->identifier(), frame2->identifier());
    EXPECT_EQ(frame1->payload(), frame2->payload());
  }

  void set_frame_data(nixnet_grpc::FrameRequest* frame, u64 timestamp, nixnet_grpc::FrameFlags frame_flag, u32 identifier, nixnet_grpc::FrameType frame_type, const char* payload)
  {
    frame->set_timestamp(timestamp);
    frame->add_flags(frame_flag);
    frame->set_identifier(identifier);
    frame->set_type(frame_type);
    frame->set_payload(payload);
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiXnet::Stub> stub_;
};

TEST_F(NiXnetCANDriverApiTests, TwoFrameExample_ConvertFramesToSignalAndBackToFramesSinglePoint_InputAndOutputFramesAreEquivalent)
{
  constexpr auto NUM_FRAMES = 2;
  constexpr auto NUM_SIGNALS = 2;
  std::vector<nixnet_grpc::FrameBufferRequest> frames;
  auto session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_example", "CAN_Cluster", "CANEventSignal1,CANEventSignal3", "", CREATE_SESSION_MODE_SIGNAL_CONVERSION_SINGLE_POINT)).session();
  nixnet_grpc::FrameRequest* frame_in_1 = new nixnet_grpc::FrameRequest();
  nixnet_grpc::FrameRequest* frame_in_2 = new nixnet_grpc::FrameRequest();
  set_frame_data(frame_in_1, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 66, FrameType::FRAME_TYPE_CAN_DATA, "\2\1\2\3\4\5\6\7");
  set_frame_data(frame_in_2, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 67, FrameType::FRAME_TYPE_CAN_DATA, "\4\1");
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_can(frame_in_1);
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_can(frame_in_2);

  auto convert_frames_to_signals_single_point_response = EXPECT_SUCCESS(client::convert_frames_to_signals_single_point(stub(), session, NUM_SIGNALS, frames));
  std::vector<f64> value_buffer_copy(convert_frames_to_signals_single_point_response.value_buffer().begin(), convert_frames_to_signals_single_point_response.value_buffer().end());
  auto convert_signals_to_frames_single_point_response = EXPECT_SUCCESS(client::convert_signals_to_frames_single_point(stub(), session, value_buffer_copy, NUM_FRAMES, 8, Protocol::PROTOCOL_CAN));

  EXPECT_EQ(2, convert_frames_to_signals_single_point_response.value_buffer_size());
  EXPECT_EQ(2, convert_frames_to_signals_single_point_response.value_buffer().size());
  EXPECT_EQ(2, convert_signals_to_frames_single_point_response.buffer_size());
  EXPECT_EQ(2, convert_signals_to_frames_single_point_response.buffer().size());
  auto frame_out_1 = convert_signals_to_frames_single_point_response.buffer()[0];
  auto frame_out_2 = convert_signals_to_frames_single_point_response.buffer()[1];
  auto can_1 = frame_out_1.can();
  auto can_2 = frame_out_2.can();
  assert_can_frames_are_equal(frame_in_1, &can_1);
  assert_can_frames_are_equal(frame_in_2, &can_2);
  EXPECT_SUCCESS(client::clear(stub(), session));
}

TEST_F(NiXnetCANDriverApiTests, TwoFrameExample_ConvertFramesToSignalAndBackToFramesSinglePoint_SecondFramePayloadDoesNotContainDataFromFirstFramePayload)
{
  constexpr auto NUM_FRAMES = 2;
  constexpr auto NUM_SIGNALS = 2;
  std::vector<nixnet_grpc::FrameBufferRequest> frames;
  auto session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_example", "CAN_Cluster", "CANEventSignal1,CANEventSignal3", "", CREATE_SESSION_MODE_SIGNAL_CONVERSION_SINGLE_POINT)).session();
  nixnet_grpc::FrameRequest* frame_in_1 = new nixnet_grpc::FrameRequest();
  nixnet_grpc::FrameRequest* frame_in_2 = new nixnet_grpc::FrameRequest();
  set_frame_data(frame_in_1, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 66, FrameType::FRAME_TYPE_CAN_DATA, "\2\1\2\3\4\5\6\7");
  set_frame_data(frame_in_2, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 67, FrameType::FRAME_TYPE_CAN_DATA, "\4");
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_can(frame_in_1);
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_can(frame_in_2);

  auto convert_frames_to_signals_single_point_response = EXPECT_SUCCESS(client::convert_frames_to_signals_single_point(stub(), session, NUM_SIGNALS, frames));
  std::vector<f64> value_buffer_copy(convert_frames_to_signals_single_point_response.value_buffer().begin(), convert_frames_to_signals_single_point_response.value_buffer().end());
  auto convert_signals_to_frames_single_point_response = EXPECT_SUCCESS(client::convert_signals_to_frames_single_point(stub(), session, value_buffer_copy, NUM_FRAMES, 8, Protocol::PROTOCOL_CAN));

  // This assertion is specifically for a bug where payload data from previous frame was being copied over to the next frame.
  auto frame_out_2 = convert_signals_to_frames_single_point_response.buffer()[1];
  auto payload_2 = frame_out_2.can().payload();
  EXPECT_EQ(2, payload_2.length());
  EXPECT_EQ('\4', payload_2[0]);
  EXPECT_NE('\1', payload_2[1]);
  EXPECT_SUCCESS(client::clear(stub(), session));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nixnet_ethernet_driver_api_tests.cpp sha256=19c206eb3db957e180de68c9faaa05188efeb9bae3912ffcbf349f9bf53b7df8 bytes=4817 -->
## FILE: source/tests/system/nixnet_ethernet_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nixnet_ethernet_driver_api_tests.cpp`
- sha256: `19c206eb3db957e180de68c9faaa05188efeb9bae3912ffcbf349f9bf53b7df8`
- bytes: 4817

````cpp
#include <gmock/gmock.h>
#include <google/protobuf/util/time_util.h>
#include <gtest/gtest.h>
#include <nixnet/nixnet_client.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <string>
#include <vector>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nixnet.h"
#include "nixnet_utilities.h"

using namespace nixnet_grpc;
namespace client = nixnet_grpc::experimental::client;
using namespace ::testing;
using namespace ::nixnet_utilities;
using nlohmann::json;

namespace ni {
namespace tests {
namespace system {
namespace {

using u8 = ::google::protobuf::uint8;
using u16 = ::google::protobuf::uint16;
using u32 = ::google::protobuf::uint32;
using u64 = ::google::protobuf::uint64;

class NiXnetEthernetDriverApiTestsWithHardware : public ::testing::Test {
 protected:
  NiXnetEthernetDriverApiTestsWithHardware()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiXnet::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiXnetEthernetDriverApiTestsWithHardware() {}
  void SetUp() override
  {
    const auto discovered_devices = EnumerateDevices();
    const auto required_interfaces = {"ENET1,ENET2,ENET3,ENET4"};

    for (const auto& required_name : required_interfaces) {
      auto found = std::find_if(
          discovered_devices.cbegin(),
          discovered_devices.cend(),
          [&required_name](const nidevice_grpc::DeviceProperties& properties) {
            return properties.name() == required_name;
          });

      if (found == discovered_devices.cend()) {
        GTEST_SKIP() << "Interface not found: " << required_name;
      }
    }
  }

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiXnet::Stub>& stub()
  {
    return stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiXnet::Stub> stub_;
};

void set_enet_frame_data(nixnet_grpc::EnetFrameRequest* frame, nixnet_grpc::EnetFrameType frame_type, u64 device_timestamp, u64 network_timestamp, nixnet_grpc::EnetFlags frame_flags)
{
  u16 payloadSize = 150;
  u32 payloadOffset = kEnetFrameVlanTaggedHeaderSize;
  frame->mutable_frame_data()->resize(payloadSize, 0);
  char* frame_data = const_cast<char*>(frame->mutable_frame_data()->data());
  EncodeEnetFrameHeader((u8*)frame_data, true, kVlanId);
  // The payload is constructed with incrementing values
  for (int i = payloadOffset; i < payloadSize; i++) {
    frame_data[i] = (u8)i;
  }

  frame->set_type(frame_type);
  frame->set_device_timestamp(device_timestamp);
  frame->set_network_timestamp(network_timestamp);
  frame->add_flags_mapped(frame_flags);
}

TEST_F(NiXnetEthernetDriverApiTestsWithHardware, WriteFrameData_ReadFrameData_ValidateFrameData)
{
  constexpr auto NUM_OF_FRAMES = 1;
  constexpr auto MAX_PAYLOAD_PER_FRAME = 150;
  std::vector<nixnet_grpc::FrameBufferRequest> frames_in;
  nixnet_grpc::EnetFlags flags[] = {EnetFlags::ENET_FLAGS_TRANSMIT};
  nixnet_grpc::EnetFrameRequest* frame = new nixnet_grpc::EnetFrameRequest();
  auto write_session = EXPECT_SUCCESS(client::create_session(stub(), "", "", "", "ENET1", CREATE_SESSION_MODE_FRAME_OUT_STREAM)).session();
  auto read_session = EXPECT_SUCCESS(client::create_session(stub(), "", "", "", "ENET2", CREATE_SESSION_MODE_FRAME_IN_STREAM)).session();
  EXPECT_SUCCESS(client::start(stub(), read_session, START_STOP_SCOPE_NORMAL));
  set_enet_frame_data(frame, EnetFrameType::ENET_FRAME_TYPE_DATA, 0, 0, flags[0]);
  frames_in.push_back(nixnet_grpc::FrameBufferRequest());
  frames_in.back().set_allocated_enet(frame);
  auto write_frame_response = EXPECT_SUCCESS(client::write_frame(stub(), write_session, frames_in, TIME_OUT_NONE));

  auto read_frame_response = EXPECT_SUCCESS(client::read_frame(stub(), read_session, NUM_OF_FRAMES, MAX_PAYLOAD_PER_FRAME, PROTOCOL_ENET, TIME_OUT_INFINITE));
  auto frame_out = read_frame_response.buffer()[0];
  // The frame that is read will contain mac address of the source on which the test is being run. For comparison purposes, we will be masking it.
  for (int i = 6; i < 12; i++) {
    const_cast<char*>(frame_out.mutable_enet()->mutable_frame_data()->data())[i] = 0xFFU;
  }

  EXPECT_EQ(frame->type(), frame_out.enet().type());
  EXPECT_EQ(frame->frame_data(), frame_out.enet().frame_data());
  EXPECT_SUCCESS(client::clear(stub(), write_session));
  EXPECT_SUCCESS(client::clear(stub(), read_session));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nixnet_lin_driver_api_tests.cpp sha256=f86db90f5ed30edff8be74af9fca12dbd41f836cee7d13b0a6f3039994d5905e bytes=9813 -->
## FILE: source/tests/system/nixnet_lin_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nixnet_lin_driver_api_tests.cpp`
- sha256: `f86db90f5ed30edff8be74af9fca12dbd41f836cee7d13b0a6f3039994d5905e`
- bytes: 9813

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nixnet/nixnet_client.h>

#include <chrono>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nixnet_utilities.h"

using namespace nixnet_grpc;
namespace client = nixnet_grpc::experimental::client;
using namespace ::testing;
using namespace ::nixnet_utilities;

namespace ni {
namespace tests {
namespace system {
namespace {

using u8 = ::google::protobuf::uint8;
using u32 = ::google::protobuf::uint32;
using u64 = ::google::protobuf::uint64;
using f64 = double;

class NiXnetLINDriverApiTests : public ::testing::Test {
 protected:
  NiXnetLINDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiXnet::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiXnetLINDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiXnet::Stub>& stub()
  {
    return stub_;
  }

  void assert_lin_frames_are_equal(nixnet_grpc::FrameRequest* frame1, nixnet_grpc::FrameResponse* frame2)
  {
    int frame1_flags = calculate_bitwise_or_of_flags(frame1->flags());
    int frame2_flags = calculate_bitwise_or_of_flags(frame2->flags());
    EXPECT_EQ(frame1_flags, frame2_flags);

    EXPECT_EQ(frame1->type(), frame2->type());
    EXPECT_EQ(frame1->identifier(), frame2->identifier());
    EXPECT_EQ(frame1->payload(), frame2->payload());
  }

  void set_frame_data(nixnet_grpc::FrameRequest* frame, u64 timestamp, nixnet_grpc::FrameFlags frame_flag, u32 identifier, nixnet_grpc::FrameType frame_type, const char* payload)
  {
    frame->set_timestamp(timestamp);
    frame->add_flags(frame_flag);
    frame->set_identifier(identifier);
    frame->set_type(frame_type);
    frame->set_payload(payload);
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiXnet::Stub> stub_;
};

class NiXnetLINDriverApiTestsWithHardware : public NiXnetLINDriverApiTests {
 protected:
  void SetUp() override
  {
    const auto discovered_devices = EnumerateDevices();
    const auto required_interfaces = {"LIN1,LIN2"};

    for (const auto& required_name : required_interfaces) {
      auto found = std::find_if(
          discovered_devices.cbegin(),
          discovered_devices.cend(),
          [&required_name](const nidevice_grpc::DeviceProperties& properties) {
            return properties.name() == required_name;
          });

      if (found == discovered_devices.cend()) {
        GTEST_SKIP() << "Interface not found: " << required_name;
      }
    }
  }
};

TEST_F(NiXnetLINDriverApiTests, ConvertFramesToFromSignalsFromExample_CompareFrames_ValuesMatch)
{
  constexpr auto NUM_FRAMES = 2;
  constexpr auto NUM_SIGNALS = 2;
  std::vector<nixnet_grpc::FrameBufferRequest> frames;
  auto session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "SlaveSignal1_U16,MasterSignal3_U8", "", CREATE_SESSION_MODE_SIGNAL_CONVERSION_SINGLE_POINT)).session();
  nixnet_grpc::FrameRequest* frame1 = new nixnet_grpc::FrameRequest();
  nixnet_grpc::FrameRequest* frame2 = new nixnet_grpc::FrameRequest();
  set_frame_data(frame1, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 4, FrameType::FRAME_TYPE_LIN_DATA, "\2\1\2\3\4\5\6\7");
  set_frame_data(frame2, 0, FrameFlags::FRAME_FLAGS_UNSPECIFIED, 3, FrameType::FRAME_TYPE_LIN_DATA, "\4\1");
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_lin(frame1);
  frames.push_back(nixnet_grpc::FrameBufferRequest());
  frames.back().set_allocated_lin(frame2);

  auto convert_frames_to_signals_single_point_response = EXPECT_SUCCESS(client::convert_frames_to_signals_single_point(stub(), session, NUM_SIGNALS, frames));
  std::vector<f64> value_buffer_copy(convert_frames_to_signals_single_point_response.value_buffer().begin(), convert_frames_to_signals_single_point_response.value_buffer().end());
  auto convert_signals_to_frames_single_point_response = EXPECT_SUCCESS(client::convert_signals_to_frames_single_point(stub(), session, value_buffer_copy, NUM_FRAMES, 8, Protocol::PROTOCOL_LIN));
  auto frame_out_1 = convert_signals_to_frames_single_point_response.buffer()[0];
  auto frame_out_2 = convert_signals_to_frames_single_point_response.buffer()[1];
  auto lin_1 = frame_out_1.lin();
  auto lin_2 = frame_out_2.lin();

  EXPECT_EQ(2, convert_frames_to_signals_single_point_response.timestamp_buffer().size());
  EXPECT_EQ(2, convert_frames_to_signals_single_point_response.value_buffer().size());
  EXPECT_EQ(2, convert_signals_to_frames_single_point_response.buffer().size());
  assert_lin_frames_are_equal(frame1, &lin_1);
  assert_lin_frames_are_equal(frame2, &lin_2);
  EXPECT_SUCCESS(client::clear(stub(), session));
  frames.clear();
}

TEST_F(NiXnetLINDriverApiTestsWithHardware, FrameStreamInputFromExample_ReadFrame_Succeeds)
{
  constexpr auto NUM_FRAMES = 2;
  auto session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "", "LIN2", CREATE_SESSION_MODE_FRAME_IN_STREAM)).session();
  EXPECT_SUCCESS(set_property(stub(), session, PROPERTY_SESSION_INTF_LIN_NO_RESPONSE_TO_IN_STRM, true));

  auto read_frame_response = EXPECT_SUCCESS(client::read_frame(stub(), session, NUM_FRAMES, 8, Protocol::PROTOCOL_LIN, TimeOut::TIME_OUT_NONE));
  EXPECT_SUCCESS(client::clear(stub(), session));
}

TEST_F(NiXnetLINDriverApiTestsWithHardware, LoopbackSignalSinglePointTestFromExample_WriteAndReadSignal_SignalMatches)
{
  constexpr auto NUM_SIGNALS_OUT = 2;
  constexpr auto NUM_SIGNALS_IN = 2;
  constexpr auto MAX_READ_ATTEMPTS = 100;
  std::vector<f64> output_value_vtr(NUM_SIGNALS_OUT);
  auto input_session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "MasterSignal1_U16,MasterSignal2_U16", "LIN1", CREATE_SESSION_MODE_SIGNAL_IN_SINGLE_POINT)).session();
  auto output_session = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "MasterSignal1_U16,MasterSignal2_U16", "LIN2", CREATE_SESSION_MODE_SIGNAL_OUT_SINGLE_POINT)).session();
  WriteStateValue state_value;
  state_value.set_lin_schedule_change(0);
  EXPECT_SUCCESS(client::write_state(stub(), output_session, WRITE_STATE_LIN_SCHEDULE_CHANGE, state_value));
  EXPECT_SUCCESS(client::start(stub(), input_session, START_STOP_SCOPE_NORMAL));
  output_value_vtr[0] = 5;
  output_value_vtr[1] = 50;

  auto write_signal_single_point_response = EXPECT_SUCCESS(client::write_signal_single_point(stub(), output_session, output_value_vtr));
  int i = 0;
  ReadSignalSinglePointResponse read_signal_single_point_response;
  while (true) {
    read_signal_single_point_response = EXPECT_SUCCESS(client::read_signal_single_point(stub(), input_session, NUM_SIGNALS_IN));
    if (output_value_vtr[0] == read_signal_single_point_response.value_buffer()[0] || i >= MAX_READ_ATTEMPTS) {
      break;
    }
    i++;
    std::this_thread::sleep_for(std::chrono::milliseconds(10));
  }

  EXPECT_SUCCESS(client::clear(stub(), output_session));
  EXPECT_SUCCESS(client::clear(stub(), input_session));
  EXPECT_EQ(output_value_vtr[0], read_signal_single_point_response.value_buffer()[0]) << "LIN1 and LIN2 must be connected together. Couldn't read valid signals after " << MAX_READ_ATTEMPTS << " attempts.";
  EXPECT_EQ(output_value_vtr[1], read_signal_single_point_response.value_buffer()[1]) << "LIN1 and LIN2 must be connected together. Couldn't read valid signals after " << MAX_READ_ATTEMPTS << " attempts.";
}

TEST_F(NiXnetLINDriverApiTestsWithHardware, LoopbackSignalXYTestFromExample_WriteAndReadSignalXY_SignalMatches)
{
  constexpr auto NUM_SAMPLES = 2;
  constexpr auto NUM_SIGNALS = 2;
  std::vector<u32> num_pairs_buffer(NUM_SIGNALS);
  std::vector<f64> value_buffer(NUM_SAMPLES * NUM_SIGNALS);
  auto session_for_writing = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "MasterSignal1_U16,MasterSignal2_U16", "LIN1", CREATE_SESSION_MODE_SIGNAL_OUT_XY)).session();
  auto session_for_reading = EXPECT_SUCCESS(client::create_session(stub(), "NIXNET_exampleLDF", "Cluster", "MasterSignal1_U16,MasterSignal2_U16,", "LIN2", CREATE_SESSION_MODE_SIGNAL_IN_XY)).session();
  WriteStateValue state_value;
  state_value.set_lin_schedule_change(0);
  EXPECT_SUCCESS(client::write_state(stub(), session_for_writing, WRITE_STATE_LIN_SCHEDULE_CHANGE, state_value));
  EXPECT_SUCCESS(client::start(stub(), session_for_reading, START_STOP_SCOPE_NORMAL));
  for (int i = 0; i < NUM_SIGNALS; ++i) {
    for (int j = 0; j < NUM_SAMPLES; ++j) {
      value_buffer[i * NUM_SAMPLES + j] = i * NUM_SAMPLES + j + 1;
    }
  }
  num_pairs_buffer[0] = NUM_SAMPLES;
  num_pairs_buffer[1] = NUM_SAMPLES;

  auto write_signal_xy_response = EXPECT_SUCCESS(client::write_signal_xy(stub(), session_for_writing, 10, value_buffer, std::vector<u64>(), num_pairs_buffer));
  auto read_signal_xy_response = EXPECT_SUCCESS(client::read_signal_xy(stub(), session_for_reading, -1, NUM_SAMPLES, NUM_SIGNALS));

  EXPECT_SUCCESS(client::clear(stub(), session_for_reading));
  EXPECT_SUCCESS(client::clear(stub(), session_for_writing));
  for (int i = 0; i < NUM_SAMPLES * NUM_SIGNALS; ++i) {
    EXPECT_EQ(value_buffer[i], read_signal_xy_response.value_buffer()[i]) << "LIN1 and LIN2 must be connected together.";
  }
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nixnet_utilities.h sha256=3d769ed89f319d0d3583d05d509021bf042e705301b01933abf0f0091abd6d75 bytes=10604 -->
## FILE: source/tests/system/nixnet_utilities.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nixnet_utilities.h`
- sha256: `3d769ed89f319d0d3583d05d509021bf042e705301b01933abf0f0091abd6d75`
- bytes: 10604

````c
#ifndef NIXNET_UTILITIES_H
#define NIXNET_UTILITIES_H

#include <gtest/gtest.h>
#undef interface
#include <custom/nixnet_converters.h>
#include <nixnet.h>
#include <nixnet/nixnet_client.h>

#include <string>
#include <vector>

#define EXPECT_SUCCESS(response_)    \
  ([](const auto& response) {        \
    EXPECT_EQ(0, response.status()); \
    return response;                 \
  })(response_)

#define EXPECT_XNET_ERROR(error, response) \
  if (1) {                                 \
    EXPECT_EQ(error, (response).status()); \
  }

#define FCS_SIZE 4

using namespace nixnet_grpc;
namespace client = nixnet_grpc::experimental::client;

static const u8 kEnetFrameOffsetEtherType = 12;
static const u8 kEnetFrameOffsetVlanEtherType = 16;
static const u8 kEnetFrameOffsetVlanTag = 12;
static const u8 kEnetFrameOffsetDstMacAddr = 0;
static const u8 kEnetFrameOffsetSrcMacAddr = 6;
static const u8 kPcp = 3;
static const u32 kEnetFrameHeaderSize = 14;
static const u32 kEnetFrameVlanTaggedHeaderSize = 18;
static const u32 kEnetMacAddrSize = 6;
static const u32 kFcsSize = FCS_SIZE;
static const u16 kVlanId = 2;

using u8 = ::google::protobuf::uint8;
using u16 = ::google::protobuf::uint16;
using u32 = ::google::protobuf::uint32;

namespace nixnet_utilities {

inline GetPropertyResponse get_property(const client::StubPtr& stub, const nidevice_grpc::Session& session_ref, const client::simple_variant<nixnet_grpc::Property, ::google::protobuf::uint32>& property_id)
{
  ::grpc::ClientContext context;

  auto request = GetPropertyRequest{};
  request.mutable_session()->CopyFrom(session_ref);
  const auto property_id_ptr = property_id.get_if<nixnet_grpc::Property>();
  const auto property_id_raw_ptr = property_id.get_if<::google::protobuf::uint32>();
  if (property_id_ptr) {
    request.set_property_id(*property_id_ptr);
  }
  else if (property_id_raw_ptr) {
    request.set_property_id_raw(*property_id_raw_ptr);
  }

  auto response = GetPropertyResponse{};

  client::raise_if_error(
      stub->GetProperty(&context, request, &response),
      context);

  return response;
}

inline void _set_property_value(SetPropertyRequest& request, const ::google::protobuf::uint32& value)
{
  request.set_u32_scalar(value);
}

inline void _set_property_value(SetPropertyRequest& request, const bool& value)
{
  request.set_bool_scalar(value);
}

inline void _set_property_value(SetPropertyRequest& request, const std::string& value)
{
  request.set_str(value);
}

inline void _set_property_value(SetPropertyRequest& request, const ::google::protobuf::uint64& value)
{
  request.set_u64_scalar(value);
}

inline void _set_property_value(SetPropertyRequest& request, const ::google::protobuf::int32& value)
{
  request.set_i32_scalar(value);
}

inline void _set_property_value(SetPropertyRequest& request, const double& value)
{
  request.set_f64_scalar(value);
}

inline void _set_property_value(SetPropertyRequest& request, const std::vector<::google::protobuf::uint32>& value)
{
  request.mutable_u32_array()->clear_u32_array();
  request.mutable_u32_array()->mutable_u32_array()->Add(value.begin(), value.end());
}

inline void _set_property_value(SetPropertyRequest& request, const nidevice_grpc::Session& value)
{
  request.mutable_db_ref()->CopyFrom(value);
}

inline void _set_property_value(SetPropertyRequest& request, const std::vector<nidevice_grpc::Session>& value)
{
  request.mutable_db_ref_array()->clear_db_ref();
  request.mutable_db_ref_array()->mutable_db_ref()->Reserve(static_cast<int>(value.size()));
  for (int i = 0; i < value.size(); ++i) {
    request.mutable_db_ref_array()->mutable_db_ref()->at(i) = value[i];
  }
}

inline void _set_property_value(SetPropertyRequest& request, const std::vector<EptRxFilter>& value)
{
  request.mutable_ept_rx_filter_array()->clear_ept_rx_filter();
  request.mutable_ept_rx_filter_array()->mutable_ept_rx_filter()->Reserve(static_cast<int>(value.size()));
  for (int i = 0; i < value.size(); ++i) {
    request.mutable_ept_rx_filter_array()->mutable_ept_rx_filter()->at(i) = value[i];
  }
}

template <typename T>
inline SetPropertyResponse set_property(
    const client::StubPtr& stub,
    const nidevice_grpc::Session& session,
    const client::simple_variant<nixnet_grpc::Property, ::google::protobuf::uint32>& property_id,
    const T& value)
{
  ::grpc::ClientContext context;

  auto request = SetPropertyRequest{};
  request.mutable_session()->CopyFrom(session);
  const auto property_id_ptr = property_id.get_if<nixnet_grpc::Property>();
  const auto property_id_raw_ptr = property_id.get_if<::google::protobuf::uint32>();
  if (property_id_ptr) {
    request.set_property_id(*property_id_ptr);
  }
  else if (property_id_raw_ptr) {
    request.set_property_id_raw(*property_id_raw_ptr);
  }
  _set_property_value(request, value);

  auto response = SetPropertyResponse{};

  client::raise_if_error(
      stub->SetProperty(&context, request, &response),
      context);

  return response;
}

inline DbGetPropertyResponse db_get_property(const client::StubPtr& stub, const nidevice_grpc::Session& dbobject_ref, const client::simple_variant<nixnet_grpc::DBProperty, ::google::protobuf::uint32>& property_id)
{
  ::grpc::ClientContext context;

  auto request = DbGetPropertyRequest{};
  request.mutable_dbobject()->CopyFrom(dbobject_ref);
  const auto property_id_ptr = property_id.get_if<nixnet_grpc::DBProperty>();
  const auto property_id_raw_ptr = property_id.get_if<::google::protobuf::uint32>();
  if (property_id_ptr) {
    request.set_property_id(*property_id_ptr);
  }
  else if (property_id_raw_ptr) {
    request.set_property_id_raw(*property_id_raw_ptr);
  }

  auto response = DbGetPropertyResponse{};

  client::raise_if_error(
      stub->DbGetProperty(&context, request, &response),
      context);

  return response;
}

inline std::vector<u32> get_property_u32_vtr(const client::StubPtr& stub, const nidevice_grpc::Session& session_ref, const client::simple_variant<nixnet_grpc::Property, ::google::protobuf::uint32>& property_id)
{
  auto array = EXPECT_SUCCESS(get_property(stub, session_ref, property_id)).u32_array().u32_array();
  return std::vector<u32>(array.begin(), array.end());
}

inline std::vector<nidevice_grpc::Session> get_property_db_ref_vtr(const client::StubPtr& stub, const nidevice_grpc::Session& session_ref, const client::simple_variant<nixnet_grpc::Property, ::google::protobuf::uint32>& property_id)
{
  auto array = EXPECT_SUCCESS(get_property(stub, session_ref, property_id)).db_ref_array().db_ref();
  return std::vector<nidevice_grpc::Session>(array.begin(), array.end());
}

inline std::vector<u32> db_get_property_u32_vtr(const client::StubPtr& stub, const nidevice_grpc::Session& database_ref, const client::simple_variant<nixnet_grpc::DBProperty, ::google::protobuf::uint32>& property_id)
{
  auto array = EXPECT_SUCCESS(db_get_property(stub, database_ref, property_id)).u32_array().u32_array();
  return std::vector<u32>(array.begin(), array.end());
}

inline std::vector<nidevice_grpc::Session> db_get_property_db_ref_vtr(const client::StubPtr& stub, const nidevice_grpc::Session& database_ref, const client::simple_variant<nixnet_grpc::DBProperty, ::google::protobuf::uint32>& property_id)
{
  auto array = EXPECT_SUCCESS(db_get_property(stub, database_ref, property_id)).db_ref_array().db_ref();
  return std::vector<nidevice_grpc::Session>(array.begin(), array.end());
}

inline int calculate_bitwise_or_of_flags(::google::protobuf::RepeatedField<::google::protobuf::int32> flags)
{
  int bitwise_or_of_flags = 0;
  for (int i = 0; i < flags.size(); i++) {
    bitwise_or_of_flags = bitwise_or_of_flags | flags[i];
  }
  return bitwise_or_of_flags;
}

struct EthernetHeader {
  u8 DestinationMacAddress[6];
  u8 SourceMacAddress[6];
  u16 EtherType;
};

inline u16 ChangeByteOrderU16(u16 value)
{
  return BigToHostOrder16(value);
}

inline u32 ChangeByteOrderU32(u32 value)
{
  return (value & 0x000000FF) << 24 |
      (value & 0x0000FF00) << 8 |
      (value & 0x00FF0000) >> 8 |
      (value & 0xFF000000) >> 24;
}

inline void AssignVlanId(u32* pVlan, u16 vlanId)
{
  u16 vidMask = 0x0FFF;
  *pVlan = ((*pVlan) & ~(vidMask));
  *pVlan = ((*pVlan) | (vlanId & vidMask));
}

inline void AssignPriorityCodePoint(u32* pVlan, u8 pcp)
{
  u16 pcpMask = 0xE000;
  u8 pcpLsb = 13;
  *pVlan = ((*pVlan) & ~(pcpMask));
  *pVlan = ((*pVlan) | (((u16)pcp << pcpLsb) & pcpMask));
}

inline u32 GenerateVlanTag(u16 vlanId)
{
  u32 vlanTag = 0x81000000;
  AssignVlanId(&vlanTag, vlanId);
  AssignPriorityCodePoint(&vlanTag, kPcp);
  return vlanTag;
}

inline void EncodeEnetFrameHeader(u8* FrameData, bool hasVlan, u16 vlanId)
{
  struct EthernetHeader EnetHead =
      {
          {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
          {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF},
          0x88B5 /* Local Experimental Ethertype */
      };

  u16 ethertypeBigEndian = ChangeByteOrderU16(EnetHead.EtherType);
  u32 vlanTagBigEndian = ChangeByteOrderU32(GenerateVlanTag(vlanId));

  memcpy(FrameData + kEnetFrameOffsetDstMacAddr, &EnetHead.DestinationMacAddress, kEnetMacAddrSize);
  memcpy(FrameData + kEnetFrameOffsetSrcMacAddr, &EnetHead.SourceMacAddress, kEnetMacAddrSize);

  if (hasVlan) {
    memcpy(FrameData + kEnetFrameOffsetVlanTag, &vlanTagBigEndian, sizeof(vlanTagBigEndian));
    memcpy(FrameData + kEnetFrameOffsetVlanEtherType, &ethertypeBigEndian, sizeof(EnetHead.EtherType));
  }
  else {
    memcpy(FrameData + kEnetFrameOffsetEtherType, &ethertypeBigEndian, sizeof(EnetHead.EtherType));
  }
}

inline void EncodeEnetFrame(nxFrameEnet_t* pFrame, u16 payloadSize, bool hasVlan, u16 vlanId)
{
  u16 frameSize = 0;
  u32 payloadOffset = 0;

  EncodeEnetFrameHeader(pFrame->FrameData, hasVlan, vlanId);
  pFrame->DeviceTimestamp = 0;
  pFrame->NetworkTimestamp = 0;
  pFrame->Flags = nxEnetFlags_Transmit;
  pFrame->Type = nxEnetFrameType_Data;

  if (hasVlan) {
    payloadOffset = kEnetFrameVlanTaggedHeaderSize;
  }
  else {
    payloadOffset = kEnetFrameHeaderSize;
  }

  frameSize = (u16)(nixnet_grpc::ENET_FRAME_HEADER_LENGTH + payloadOffset + payloadSize + kFcsSize);
  pFrame->Length = frameSize;

  for (u16 i = 0; i < payloadSize; i++) {
    pFrame->FrameData[payloadOffset + i] = (u8)i;
  }
}

}  // namespace nixnet_utilities

#endif  // NIXNET_UTILITIES_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nixnetsocket_driver_api_tests.cpp sha256=a86fc6b9640a94282407f5ce61d288b1a27e24f65874b7795de530f30675e174 bytes=39374 -->
## FILE: source/tests/system/nixnetsocket_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nixnetsocket_driver_api_tests.cpp`
- sha256: `a86fc6b9640a94282407f5ce61d288b1a27e24f65874b7795de530f30675e174`
- bytes: 39374

````cpp
#include <gmock/gmock.h>
#include <google/protobuf/util/time_util.h>
#include <nixnetsocket/nixnetsocket_client.h>

#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

#include "device_server.h"
#include "enumerate_devices.h"
#include "tests/utilities/test_helpers.h"
#if defined(__linux__)
  #include <netinet/in.h>
#endif

using namespace nixnetsocket_grpc;
namespace client = nixnetsocket_grpc::experimental::client;
using namespace ::testing;
using nlohmann::json;
using namespace std::string_literals;  // for trailing ""s string literal syntax;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto INVALID_XNET_SOCKET = -1;
constexpr auto GENERIC_NXSOCKET_ERROR = -1;
constexpr auto INVALID_SOCKET_ERROR = -13008;
constexpr auto INVALID_SOCKET_MESSAGE = "The specified socket could not be found.";
constexpr auto INVALID_IP_STACK_ERROR = -13009;
constexpr auto INVALID_IP_STACK_MESSAGE = "The specified IP Stack could not be found.";
constexpr auto INVALID_ARGUMENT_ERROR = 13822;
constexpr auto INVALID_ARGUMENT_MESSAGE = "Invalid argument";
constexpr auto NXSOCKET_FALSE = 0;
constexpr auto NXSOCKET_TRUE = 1;
constexpr auto IPV4_LOCALHOST_ADDR = 0x0100007FU;
constexpr auto IPV4_LOCALHOST_ADDRESS_STR = "127.0.0.1";
constexpr auto IPV6_LOCALHOST_ADDRESS_STR = "::1";
const auto IPV6_LOCALHOST_ADDR = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x1"s;
const auto IPV6_ZERO_ADDR = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"s;

constexpr auto SCHEMA = "file:///NIXNET_Documentation/xnetIpStackSchema-03.json";
const auto SIMPLE_INTERFACE_CONFIG = R"(
        {
          "address": "generated",
          "name": "",
          "VLANs": [
            {
              "IPv4": {
                "DAD": false,
                "mode": "static",
                "staticAddresses": [
                  {
                    "address": "192.22.33.44",
                    "subnetMask": "255.0.0.0"
                  }
                ]
              },
              "IPv6": {
                  "mode": "enabled"
              },
              "isTagged": false,
              "name": ""
            }
          ]
        }
)"s;

const auto MULTI_ADDRESS_INTERFACE_CONFIG = R"(
        {
          "address": "inherit",
          "VLANs": [
            {
              "name": "testVlan",
              "IPv4": {
                "mode": "static",
                "staticAddresses": [
                  {
                    "address": "192.22.11.22",
                    "subnetMask": "255.0.0.0"
                  },
                  {
                    "address": "10.23.45.67",
                    "subnetMask": "255.0.0.0"
                  }
                ],
                "gatewayAddresses": [
                  {
                    "address": "10.2.129.1"
                  }
                ]
              },
              "IPv6": {
                "mode": "enabled",
                "staticAddresses": [
                  {
                    "address": "2001:DB8:0:0:8:800:200C:417A/32"
                  }
                ],
                "gatewayAddresses": [
                  {
                    "address": "FF01::1"
                  }
                ]
              }
            }
          ]
        }
)"s;

std::string unique_static_ipv4_address()
{
  static std::atomic<uint32_t> instance_id_counter;
  const auto instance_id = instance_id_counter++;
  ASSERT_EQ(0, instance_id & 0xFF000000), "instance-id must fit in 24 bits.";
  auto ipv4_addr = std::stringstream{};
  ipv4_addr << std::dec << "10." << ((instance_id >> 16) & 0xFF) << "." << ((instance_id >> 8) & 0xFF) << "." << (instance_id & 0xFF);
  return ipv4_addr.str();
}

json create_interface_config(const std::string& interface_name, const std::string& interface_macs_config, const std::string& static_ip_address = {})
{
  auto interface_config = json{};
  interface_config["name"] = interface_name;
  interface_config["MACs"] = std::vector<json>{json::parse(interface_macs_config)};
  if (!static_ip_address.empty()) {
    interface_config["MACs"][0]["VLANs"][0]["IPv4"]["staticAddresses"][0]["address"] = static_ip_address;
  }
  return interface_config;
}

std::string create_config(const std::vector<json>& interfaces_config)
{
  auto config = json{};
  config["schema"] = SCHEMA;
  config["xnetInterfaces"] = interfaces_config;

  return config.dump();
}

std::string create_simple_config(const std::string& interface_name, const std::string& static_ip_address = unique_static_ipv4_address())
{
  return create_config({create_interface_config(interface_name, SIMPLE_INTERFACE_CONFIG, static_ip_address)});
}

class NiXnetSocketDriverApiTests : public ::testing::Test {
 protected:
  NiXnetSocketDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiXnetSocket::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiXnetSocketDriverApiTests() {}

  void SetUp() override
  {
    const auto discovered_devices = EnumerateDevices();

    for (const auto& required_name : required_interfaces()) {
      auto found = std::find_if(
          discovered_devices.cbegin(),
          discovered_devices.cend(),
          [&required_name](const nidevice_grpc::DeviceProperties& properties) {
            return properties.name() == required_name;
          });

      if (found == discovered_devices.cend()) {
        GTEST_SKIP() << "Interface not found: " << required_name;
      }
    }
  }

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiXnetSocket::Stub>& stub()
  {
    return stub_;
  }

  virtual std::vector<std::string> required_interfaces() const = 0;

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiXnetSocket::Stub> stub_;
};

class NiXnetSocketLoopbackTests : public NiXnetSocketDriverApiTests {
  virtual std::vector<std::string> required_interfaces() const override
  {
    return {"ENET1,ENET2,ENET3,ENET4"};
  }
};

class NiXnetSocketNoHardwareTests : public NiXnetSocketDriverApiTests {
  virtual std::vector<std::string> required_interfaces() const override
  {
    return {};
  }
};

// Like EXPECT_SUCCESS for responses that exclude_from_get_last_error.
#define EXPECT_SUCCESS_STATUS_ONLY(response) \
  if (1) {                                   \
    EXPECT_EQ(0, (response).status());       \
  }

#define EXPECT_SUCCESS(response)               \
  if (1) {                                     \
    EXPECT_EQ(0, (response).status());         \
  }

#define EXPECT_SUCCESS_WITH_STATUS(expected_status, response) \
  if (1) {                                                    \
    EXPECT_EQ(expected_status, (response).status());          \
  }

#define EXPECT_XNET_STATUS(error, response) \
  if (1) {                                  \
    EXPECT_EQ(error, (response).status());  \
  }

#define EXPECT_XNET_ERROR_NUMBER(expected, ex)                            \
  const auto& socket_err = ex.Trailers().find("ni-socket-error")->second; \
  EXPECT_EQ(expected, std::stoi(socket_err));

#define EXPECT_XNET_ERROR(expected_status, error, message, response) \
  if (1) {                                                           \
    EXPECT_EQ(expected_status, (response).status());                 \
  }

#define EXPECT_INVALID_ARGUMENT_ERROR(response)                                                              \
  if (1) {                                                                                                   \
    EXPECT_XNET_ERROR(GENERIC_NXSOCKET_ERROR, INVALID_ARGUMENT_ERROR, INVALID_ARGUMENT_MESSAGE, (response)); \
  }

#define ARRAY_ARG(...) \
  {                    \
    __VA_ARGS__        \
  }

#define EXPECT_ADDR_EQ(expected_family, expected_addr, addr_info)                                                      \
  {                                                                                                                    \
    EXPECT_EQ(expected_family, addr_info.family());                                                                    \
    uint8_t expected_as_array[16] = ARRAY_ARG expected_addr;                                                           \
    if (addr_info.family() == AddressFamily::ADDRESS_FAMILY_INET) {                                                    \
      uint32_t addr = addr_info.addr().ipv4().addr().addr();                                                           \
      uint8_t* addr_byte_array = reinterpret_cast<uint8_t*>(&addr);                                                    \
      std::vector<uint8_t> addr_bytes{addr_byte_array[0], addr_byte_array[1], addr_byte_array[2], addr_byte_array[3]}; \
      EXPECT_THAT(addr_bytes, ElementsAreArray(expected_as_array, 4));                                                 \
    }                                                                                                                  \
    else {                                                                                                             \
      EXPECT_THAT(addr_info.addr().ipv6().addr().addr(), ElementsAreArray(expected_as_array, 16));                     \
    }                                                                                                                  \
  }

SocketResponse
socket(client::StubPtr& stub, const nidevice_grpc::Session& stack)
{
  return client::socket(stub, stack, ADDRESS_FAMILY_INET, SOCKET_PROTOCOL_TYPE_STREAM, IP_PROTOCOL_TCP);
}

SocketResponse socket(client::StubPtr& stub)
{
  return socket(stub, nidevice_grpc::Session{});
}

TEST_F(NiXnetSocketNoHardwareTests, InitWithInvalidIpStack_Close_ReturnsAndSetsExpectedErrors)
{
  SocketResponse invalid_socket;
  invalid_socket.mutable_socket()->set_name("");

  EXPECT_THROW({
    try {
      client::close(stub(), invalid_socket.socket());
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_DRIVER_ERROR_WITH_SUBSTR(ex, GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_MESSAGE);
      EXPECT_XNET_ERROR_NUMBER(INVALID_SOCKET_ERROR, ex);
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);
}

TEST_F(NiXnetSocketNoHardwareTests, InitWithInvalidIpStack_Bind_ReturnsAndSetsExpectedErrors)
{
  SocketResponse invalid_socket;
  invalid_socket.mutable_socket()->set_name("");
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv4()->mutable_addr()->set_addr(0x7F000001);
  sock_addr.mutable_ipv4()->set_port(31764);

  EXPECT_THROW({
    try {
      client::bind(stub(), invalid_socket.socket(), sock_addr);
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_DRIVER_ERROR_WITH_SUBSTR(ex, GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_MESSAGE);
      EXPECT_XNET_ERROR_NUMBER(INVALID_SOCKET_ERROR, ex);
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);
}

TEST_F(NiXnetSocketNoHardwareTests, SocketAndEmptySet_IsSet_ReturnsFalse)
{
  SocketResponse invalid_socket;
  invalid_socket.mutable_socket()->set_name("");

  auto is_set_response = client::fd_is_set(stub(), invalid_socket.socket(), {});

  EXPECT_SUCCESS(is_set_response);
  EXPECT_EQ(NXSOCKET_FALSE, is_set_response.is_set());
}

TEST_F(NiXnetSocketNoHardwareTests, SocketAndSetContainingSocket_IsSet_ReturnsTrue)
{
  SocketResponse invalid_socket;
  invalid_socket.mutable_socket()->set_name("");

  auto is_set_response = client::fd_is_set(stub(), invalid_socket.socket(), {invalid_socket.socket()});

  EXPECT_SUCCESS(is_set_response);
  EXPECT_EQ(NXSOCKET_TRUE, is_set_response.is_set());
}

TEST_F(NiXnetSocketNoHardwareTests, InvalidSocket_Select_ReturnsAndSetsExpectedErrors)
{
  SocketResponse invalid_socket;
  invalid_socket.mutable_socket()->set_name("");
  auto duration = ::google::protobuf::Duration{};
  duration.set_seconds(1);
  duration.set_nanos(500000);

  EXPECT_THROW({
    try {
      client::select(stub(), {invalid_socket.socket()}, {invalid_socket.socket()}, {}, duration);
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_DRIVER_ERROR_WITH_SUBSTR(ex, GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_MESSAGE);
      EXPECT_XNET_ERROR_NUMBER(INVALID_SOCKET_ERROR, ex);
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);
}

TEST_F(NiXnetSocketNoHardwareTests, InvalidEmptyConfigJson_IpStackCreate_ReturnsInvalidInterfaceNameError)
{
  constexpr auto TEST_CONFIG = "{}";
  constexpr auto JSON_OBJECT_MISSING_VALUE = -13017;

  EXPECT_THROW_DRIVER_ERROR({
    client::ip_stack_create(stub(), "", "{}");
  }, JSON_OBJECT_MISSING_VALUE);
}

TEST_F(NiXnetSocketNoHardwareTests, ValidConfigJsonForMissingDevice_IpStackCreate_ReturnsInvalidInterfaceNameError)
{
  const auto TEST_CONFIG = create_simple_config("ENET6");
  constexpr auto INVALID_INTERFACE_NAME = -1074384758;

  EXPECT_THROW_DRIVER_ERROR({
    client::ip_stack_create(stub(), "", TEST_CONFIG);
  }, INVALID_INTERFACE_NAME);
}

TEST_F(NiXnetSocketNoHardwareTests, StackAlreadyExistsError_StrErrR_ReturnsExpectedMessage)
{
  constexpr auto STACK_ALREADY_EXISTS = static_cast<int32_t>(0xFFFFCD24);

  const auto str_err = client::str_err_r(stub(), STACK_ALREADY_EXISTS, 512);

  EXPECT_SUCCESS_STATUS_ONLY(str_err);
  EXPECT_EQ("An IP Stack with the specified name already exists. The name provided to IP Stack create must be a system-wide unique name.", str_err.error());
}

TEST_F(NiXnetSocketNoHardwareTests, StackAlreadyExistsError_StrErrRWithZeroBuffer_ReturnsGenericSocketError)
{
  constexpr auto STACK_ALREADY_EXISTS = static_cast<int32_t>(0xFFFFCD24);

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    client::str_err_r(stub(), STACK_ALREADY_EXISTS, 0);
  }, GENERIC_NXSOCKET_ERROR, "Unknown");
}

TEST_F(NiXnetSocketLoopbackTests, IPv4LocalhostAddress_AToNAndPToNRoundtrip_ReturnsCorrectAddr)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto a_to_n = client::inet_a_to_n(stub(), stack.stack_ref(), IPV4_LOCALHOST_ADDRESS_STR);
  const auto p_to_n = client::inet_p_to_n(stub(), stack.stack_ref(), 2 /* nxAF_INET */, IPV4_LOCALHOST_ADDRESS_STR);
  const auto n_to_a = client::inet_n_to_a(stub(), stack.stack_ref(), a_to_n.name());
  const auto n_to_p = client::inet_n_to_p(stub(), stack.stack_ref(), p_to_n.addr());

  EXPECT_SUCCESS_WITH_STATUS(1, a_to_n);
  EXPECT_SUCCESS_WITH_STATUS(1, p_to_n);
  EXPECT_SUCCESS(n_to_a);
  EXPECT_SUCCESS(n_to_p);
  EXPECT_EQ(IPV4_LOCALHOST_ADDR, a_to_n.name().addr());
  EXPECT_EQ(IPV4_LOCALHOST_ADDR, p_to_n.addr().ipv4().addr());
  EXPECT_EQ(IPV4_LOCALHOST_ADDRESS_STR, n_to_a.address());
  EXPECT_EQ(IPV4_LOCALHOST_ADDRESS_STR, n_to_p.address());
}

TEST_F(NiXnetSocketLoopbackTests, IPv6LocalhostAddress_PToNRoundtrip_ReturnsCorrectAddr)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto p_to_n = client::inet_p_to_n(stub(), stack.stack_ref(), 10 /* nxAF_INET6 */, IPV6_LOCALHOST_ADDRESS_STR);
  const auto n_to_p = client::inet_n_to_p(stub(), stack.stack_ref(), p_to_n.addr());

  EXPECT_SUCCESS_WITH_STATUS(1, p_to_n);
  EXPECT_SUCCESS(n_to_p);
  EXPECT_EQ(IPV6_LOCALHOST_ADDR, p_to_n.addr().ipv6().addr());
  EXPECT_EQ(IPV6_LOCALHOST_ADDRESS_STR, n_to_p.address());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4LocalhostAddress_InetAddr_ReturnsCorrectAddr)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto addr = client::inet_addr(stub(), stack.stack_ref(), IPV4_LOCALHOST_ADDRESS_STR);

  EXPECT_SUCCESS(addr);
  EXPECT_EQ(IPV4_LOCALHOST_ADDR, addr.addr());
}

TEST_F(NiXnetSocketLoopbackTests, PToNWithInvalidFamily_ReturnsError)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto p_to_n_in6_with_in_addr = client::inet_p_to_n(stub(), stack.stack_ref(), 10 /* nxAF_INET6 */, "127.0.0.1");
  const auto p_to_n_UNSPEC = client::inet_p_to_n(stub(), stack.stack_ref(), 0 /* nxAF_UNSPEC */, IPV4_LOCALHOST_ADDRESS_STR);
  const auto p_to_n_42 = client::inet_p_to_n(stub(), stack.stack_ref(), 42 /* bogus */, "10.0.0.1");

  // Invalid address is a zero status (1 is success; -1 is invalid family)
  // https://man7.org/linux/man-pages/man3/inet_pton.3.html
  EXPECT_XNET_STATUS(0, p_to_n_in6_with_in_addr);
  EXPECT_EQ(IPV6_ZERO_ADDR, p_to_n_in6_with_in_addr.addr().ipv6().addr());
  EXPECT_INVALID_ARGUMENT_ERROR(p_to_n_UNSPEC);
  EXPECT_INVALID_ARGUMENT_ERROR(p_to_n_42);
}

TEST_F(NiXnetSocketLoopbackTests, NToPWithAddrCaseNotSet_ReturnsError)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto n_to_p_unset = client::inet_n_to_p(stub(), stack.stack_ref(), Addr{});

  EXPECT_INVALID_ARGUMENT_ERROR(n_to_p_unset);
}

TEST_F(NiXnetSocketLoopbackTests, InetAddrWithInvalidAddress_ReturnsZero)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto addr = client::inet_addr(stub(), stack.stack_ref(), "NOT AN ADDRESS");

  EXPECT_EQ(0, addr.addr());
}

TEST_F(NiXnetSocketLoopbackTests, IpStackCreate_CreateSocketWithIpStack_Succeeds)
{
  const auto stack_response = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));

  const auto socket_response = socket(stub(), stack_response.stack_ref());

  EXPECT_SUCCESS(stack_response);
  EXPECT_SUCCESS(socket_response);
}

TEST_F(NiXnetSocketLoopbackTests, IpStackCreateAndClear_CreateSocketWithIpStack_Fails)
{
  const auto create_stack_response = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto clear_stack_response = client::ip_stack_clear(stub(), create_stack_response.stack_ref());

  const auto socket_response = socket(stub(), create_stack_response.stack_ref());

  EXPECT_SUCCESS(create_stack_response);
  EXPECT_SUCCESS(clear_stack_response);
  EXPECT_XNET_STATUS(GENERIC_NXSOCKET_ERROR, socket_response);
}

TEST_F(NiXnetSocketLoopbackTests, MultiAddressIpStack_GetInfo_ReturnsExpectedInfo)
{
  const auto create_stack_response = client::ip_stack_create(
      stub(),
      "",
      create_config(
          {create_interface_config("ENET1", MULTI_ADDRESS_INTERFACE_CONFIG)}));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), create_stack_response.stack_ref(), "", 5000);

  const auto stack_info_response = client::ip_stack_get_info(stub(), create_stack_response.stack_ref());

  EXPECT_SUCCESS(create_stack_response);
  EXPECT_SUCCESS(stack_info_response);
  EXPECT_SUCCESS(wait_response);
  EXPECT_EQ(1, stack_info_response.virtual_interfaces_size());
  const auto virtual_interface = stack_info_response.virtual_interfaces()[0];
  EXPECT_EQ("ENET1", virtual_interface.xnet_interface_name());
  EXPECT_EQ("testVlan", virtual_interface.vlan_name());
  EXPECT_EQ("00:80:2f:30:f4:58", virtual_interface.mac_address());
  EXPECT_EQ(1500, virtual_interface.mac_mtu());
  EXPECT_EQ(1, virtual_interface.if_index());
  EXPECT_EQ(4, virtual_interface.ip_addresses_size());
  const auto ipv4_address = virtual_interface.ip_addresses()[0];
  EXPECT_EQ(2 /* nxAF_INET */, ipv4_address.family());
  EXPECT_EQ("192.22.11.22", ipv4_address.address());
  EXPECT_EQ("255.0.0.0", ipv4_address.net_mask());
  EXPECT_EQ(8, ipv4_address.prefix_length());
  const auto second_ipv4_address = virtual_interface.ip_addresses()[1];
  EXPECT_EQ(2 /* nxAF_INET */, second_ipv4_address.family());
  EXPECT_EQ("10.23.45.67", second_ipv4_address.address());
  EXPECT_EQ("255.0.0.0", second_ipv4_address.net_mask());
  EXPECT_EQ(8, second_ipv4_address.prefix_length());
  const auto ipv6_address = virtual_interface.ip_addresses()[2];
  EXPECT_EQ(10 /* nxAF_INET6 */, ipv6_address.family());
  EXPECT_EQ("2001:db8::8:800:200c:417a", ipv6_address.address());
  EXPECT_EQ("ffff:ffff::", ipv6_address.net_mask());
  EXPECT_EQ(32, ipv6_address.prefix_length());
  EXPECT_EQ(2, virtual_interface.gateway_addresses_size());
  const auto ipv4_gateway_address = virtual_interface.gateway_addresses()[0];
  EXPECT_EQ(2 /* nxAF_INET */, ipv4_gateway_address.family());
  EXPECT_EQ("10.2.129.1", ipv4_gateway_address.address());
  const auto ipv6_gateway_address = virtual_interface.gateway_addresses()[1];
  EXPECT_EQ(10 /* nxAF_INET6 */, ipv6_gateway_address.family());
  EXPECT_EQ("ff01::1", ipv6_gateway_address.address());
}

TEST_F(NiXnetSocketLoopbackTests, MultiAddressIpStack_GetInfoString_ReturnsReasonablyExpectedInfo)
{
  const auto create_stack_response = client::ip_stack_create(
      stub(),
      "",
      create_config(
          {create_interface_config("ENET1", MULTI_ADDRESS_INTERFACE_CONFIG)}));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), create_stack_response.stack_ref(), "", 5000);

  const auto json_stack_info = client::ip_stack_get_all_stacks_info_str(stub(), IPStackInfoStringFormat::IPSTACK_INFO_STR_FORMAT_JSON);
  const auto text_stack_info = client::ip_stack_get_all_stacks_info_str(stub(), IPStackInfoStringFormat::IPSTACK_INFO_STR_FORMAT_TEXT);

  EXPECT_SUCCESS(create_stack_response);
  EXPECT_SUCCESS(wait_response);
  for (const auto response : {json_stack_info, text_stack_info}) {
    EXPECT_SUCCESS(response);
    for (const auto expected_sub_str : {"ENET1"s, "10.23.45.67"s, "ff01::1"s}) {
      EXPECT_THAT(response.info(), HasSubstr(expected_sub_str));
    }
  }
  EXPECT_THAT(text_stack_info.info(), HasSubstr("IPv4 addresses"));
  EXPECT_THAT(json_stack_info.info(), HasSubstr("ipv4Addresses"));
}

TEST_F(NiXnetSocketLoopbackTests, OpenedStackThenCloseOriginal_GetStackInfoFromOpenedStack_ReturnsInfoFromOriginalConfig)
{
  const auto CONFIGURED_STATIC_ADDRESS = "10.56.45.67"s;
  const auto STACK_NAME = "STACK_NAME"s;
  const auto original_stack = client::ip_stack_create(stub(), STACK_NAME, create_simple_config("ENET1", CONFIGURED_STATIC_ADDRESS));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), original_stack.stack_ref(), "", 5000);
  const auto reopened_stack = client::ip_stack_open(stub(), STACK_NAME);
  const auto closed_original_stack = client::ip_stack_clear(stub(), original_stack.stack_ref());

  const auto stack_info = client::ip_stack_get_all_stacks_info_str(stub(), IPStackInfoStringFormat::IPSTACK_INFO_STR_FORMAT_JSON);

  EXPECT_THAT(stack_info.info(), HasSubstr(CONFIGURED_STATIC_ADDRESS));
}

TEST_F(NiXnetSocketLoopbackTests, OpenedStack_CloseOpenedAndOriginal_BothStacksAreClosed)
{
  const auto CONFIGURED_STATIC_ADDRESS = "10.56.45.67"s;
  const auto STACK_NAME = "STACK_NAME"s;
  const auto original_stack = client::ip_stack_create(stub(), STACK_NAME, create_simple_config("ENET1", CONFIGURED_STATIC_ADDRESS));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), original_stack.stack_ref(), "", 5000);
  const auto reopened_stack = client::ip_stack_open(stub(), STACK_NAME);
  const auto closed_reopened_stack = client::ip_stack_clear(stub(), reopened_stack.stack_ref());
  const auto closed_original_stack = client::ip_stack_clear(stub(), original_stack.stack_ref());

  const auto stack_info = client::ip_stack_get_info(stub(), original_stack.stack_ref());
  const auto reopened_stack_info = client::ip_stack_get_info(stub(), reopened_stack.stack_ref());
  EXPECT_XNET_ERROR(INVALID_IP_STACK_ERROR, INVALID_IP_STACK_ERROR, INVALID_IP_STACK_MESSAGE, stack_info);
  EXPECT_XNET_ERROR(INVALID_IP_STACK_ERROR, INVALID_IP_STACK_ERROR, INVALID_IP_STACK_MESSAGE, reopened_stack_info);
}

SockAddr lookup_ipv4_sock_addr(client::StubPtr& stub, const nidevice_grpc::Session& stack, const std::string& addr, int32_t port)
{
  const auto p_to_n = client::inet_p_to_n(stub, stack, 2 /* AF INET*/, addr);
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv4()->mutable_addr()->CopyFrom(p_to_n.addr().ipv4());
  sock_addr.mutable_ipv4()->set_port(port);
  return sock_addr;
}

SockOptData create_membership_request(const SockAddr& multicast_addr, const SockAddr& interface_addr)
{
  auto opt_data = SockOptData{};
  auto mreq = opt_data.mutable_data_ip_mreq();
  mreq->mutable_multiaddr()->CopyFrom(multicast_addr.ipv4().addr());
  mreq->mutable_imr_interface()->CopyFrom(interface_addr.ipv4().addr());
  return opt_data;
}

TEST_F(NiXnetSocketLoopbackTests, IPv4SocketsOnWiredPhysicalLoopback_SendAndReceiveData_ReceivesExpectedData)
{
  const auto MESSAGE = "HelloWorld"s;
  const auto RX_ADDR = "10.0.0.1"s;
  const auto rx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1", RX_ADDR));
  const auto tx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET4", "10.0.0.2"));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), rx_stack.stack_ref(), "", 5000);
  const auto rx_socket = socket(stub(), rx_stack.stack_ref());
  auto sock_addr = lookup_ipv4_sock_addr(stub(), rx_stack.stack_ref(), RX_ADDR, 0);
  const auto bind = client::bind(stub(), rx_socket.socket(), sock_addr);
  const auto get_name = client::get_sock_name(stub(), rx_socket.socket());
  const auto listen = client::listen(stub(), rx_socket.socket(), 10);
  const auto tx_socket = socket(stub(), tx_stack.stack_ref());
  EXPECT_SUCCESS(tx_stack);
  EXPECT_SUCCESS(rx_stack);
  EXPECT_SUCCESS(wait_response);
  EXPECT_SUCCESS(rx_socket);
  EXPECT_SUCCESS(bind);
  EXPECT_SUCCESS(get_name);
  EXPECT_SUCCESS(listen);
  EXPECT_SUCCESS(tx_socket);

  const auto connect = client::connect(stub(), tx_socket.socket(), get_name.addr());
  const auto accept = client::accept(stub(), rx_socket.socket());
  const auto send = client::send(stub(), tx_socket.socket(), MESSAGE, 0);
  const auto recv = client::recv(stub(), accept.socket(), static_cast<::google::protobuf::int32>(MESSAGE.size()), 0);

  EXPECT_SUCCESS(connect);
  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), send);
  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), recv);
  EXPECT_EQ(MESSAGE, recv.data());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4TwoWaySession_CloseAllSockets_SocketsAreClosed)
{
  const auto MESSAGE = "HelloWorld"s;
  const auto RX_ADDR = "10.0.0.1"s;
  const auto rx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1", RX_ADDR));
  const auto tx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET4", "10.0.0.2"));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), rx_stack.stack_ref(), "", 5000);
  const auto rx_socket = socket(stub(), rx_stack.stack_ref());
  const auto sock_addr = lookup_ipv4_sock_addr(stub(), rx_stack.stack_ref(), RX_ADDR, 0);
  const auto bind = client::bind(stub(), rx_socket.socket(), sock_addr);
  const auto get_name = client::get_sock_name(stub(), rx_socket.socket());
  const auto listen = client::listen(stub(), rx_socket.socket(), 10);
  const auto tx_socket = socket(stub(), tx_stack.stack_ref());
  const auto connect = client::connect(stub(), tx_socket.socket(), get_name.addr());
  const auto accept = client::accept(stub(), rx_socket.socket());
  const auto send = client::send(stub(), tx_socket.socket(), MESSAGE, 0);
  const auto recv = client::recv(stub(), accept.socket(), static_cast<::google::protobuf::int32>(MESSAGE.size()), 0);

  const auto close_tx = client::close(stub(), tx_socket.socket());
  const auto close_rx = client::close(stub(), rx_socket.socket());
  const auto close_accepted = client::close(stub(), accept.socket());

  EXPECT_SUCCESS(close_tx);
  EXPECT_SUCCESS(close_rx);
  EXPECT_SUCCESS(close_accepted);
  EXPECT_XNET_ERROR(GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_ERROR, INVALID_SOCKET_MESSAGE, client::get_sock_name(stub(), tx_socket.socket()));
  EXPECT_XNET_ERROR(GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_ERROR, INVALID_SOCKET_MESSAGE, client::get_sock_name(stub(), rx_socket.socket()));
  EXPECT_XNET_ERROR(GENERIC_NXSOCKET_ERROR, INVALID_SOCKET_ERROR, INVALID_SOCKET_MESSAGE, client::get_sock_name(stub(), accept.socket()));
}

TEST_F(NiXnetSocketLoopbackTests, UdpSocketsOnWiredPhysicalLoopback_SendAndReceiveData_ReceivesExpectedData)
{
  constexpr auto RX_ADDR = "10.0.0.1";
  constexpr auto TX_ADDR = "10.0.0.2";
  const auto MESSAGE = "HelloWorld"s;
  const auto rx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1", RX_ADDR));
  const auto tx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET4", TX_ADDR));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), rx_stack.stack_ref(), "", 5000);
  auto multicast_sock_addr = lookup_ipv4_sock_addr(stub(), rx_stack.stack_ref(), "233.252.0.1", 5544);
  auto rx_sock_addr = lookup_ipv4_sock_addr(stub(), rx_stack.stack_ref(), RX_ADDR, 5544);
  auto tx_sock_addr = lookup_ipv4_sock_addr(stub(), tx_stack.stack_ref(), TX_ADDR, 5544);
  const auto rx_socket = client::socket(stub(), rx_stack.stack_ref(), ADDRESS_FAMILY_INET, SOCKET_PROTOCOL_TYPE_DGRAM, IP_PROTOCOL_UDP);
  const auto rx_bind = client::bind(stub(), rx_socket.socket(), rx_sock_addr);
  const auto rx_add_member = client::set_sock_opt(stub(), rx_socket.socket(), 0, OPT_NAME_IP_ADD_MEMBERSHIP, create_membership_request(multicast_sock_addr, rx_sock_addr));
  const auto tx_socket = client::socket(stub(), tx_stack.stack_ref(), ADDRESS_FAMILY_INET, SOCKET_PROTOCOL_TYPE_DGRAM, IP_PROTOCOL_UDP);
  const auto tx_bind = client::bind(stub(), tx_socket.socket(), tx_sock_addr);
  const auto tx_add_member = client::set_sock_opt(stub(), tx_socket.socket(), 0, OPT_NAME_IP_ADD_MEMBERSHIP, create_membership_request(multicast_sock_addr, tx_sock_addr));
  EXPECT_SUCCESS(tx_stack);
  EXPECT_SUCCESS(rx_stack);
  EXPECT_SUCCESS(wait_response);
  EXPECT_SUCCESS(rx_socket);
  EXPECT_SUCCESS(rx_bind);
  EXPECT_SUCCESS(rx_add_member);
  EXPECT_SUCCESS(tx_socket);
  EXPECT_SUCCESS(tx_bind);
  EXPECT_SUCCESS(tx_add_member);

  const auto send = client::send_to(stub(), tx_socket.socket(), MESSAGE, 0, multicast_sock_addr);
  const auto recv = client::recv(stub(), rx_socket.socket(), static_cast<::google::protobuf::int32>(MESSAGE.size()), 0);

  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), send);
  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), recv);
  EXPECT_EQ(MESSAGE, recv.data());
}

TEST_F(NiXnetSocketLoopbackTests, IPv6OnLoopbackAddress_SendAndReceiveData_ReceivesExpectedData)
{
  const auto MESSAGE = "HelloWorld"s;
  const auto rx_stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto wait_response = client::ip_stack_wait_for_interface(stub(), rx_stack.stack_ref(), "", 5000);
  const auto rx_socket = client::socket(stub(), rx_stack.stack_ref(), ADDRESS_FAMILY_INET6, SOCKET_PROTOCOL_TYPE_STREAM, IP_PROTOCOL_TCP);
  const auto rx_p_to_n = client::inet_p_to_n(stub(), rx_stack.stack_ref(), 10 /* AF INET*/, "::1");
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv6()->mutable_addr()->CopyFrom(rx_p_to_n.addr().ipv6());
  const auto bind = client::bind(stub(), rx_socket.socket(), sock_addr);
  const auto get_name = client::get_sock_name(stub(), rx_socket.socket());
  const auto listen = client::listen(stub(), rx_socket.socket(), 10);
  const auto tx_socket = client::socket(stub(), rx_stack.stack_ref(), ADDRESS_FAMILY_INET6, SOCKET_PROTOCOL_TYPE_STREAM, IP_PROTOCOL_TCP);
  EXPECT_SUCCESS(rx_stack);
  EXPECT_SUCCESS(wait_response);
  EXPECT_SUCCESS_WITH_STATUS(1, rx_p_to_n);
  EXPECT_SUCCESS(rx_socket);
  EXPECT_SUCCESS(bind);
  EXPECT_SUCCESS(get_name);
  EXPECT_SUCCESS(listen);
  EXPECT_SUCCESS(tx_socket);

  const auto connect = client::connect(stub(), tx_socket.socket(), get_name.addr());
  const auto accept = client::accept(stub(), rx_socket.socket());
  const auto send = client::send(stub(), tx_socket.socket(), MESSAGE, 0);
  const auto recv = client::recv(stub(), accept.socket(), static_cast<::google::protobuf::int32>(MESSAGE.size()), 0);

  EXPECT_SUCCESS(connect);
  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), send);
  EXPECT_SUCCESS_WITH_STATUS(MESSAGE.size(), recv);
  EXPECT_EQ(MESSAGE, recv.data());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4Address_GetAddrInfo_ReturnsExpectedAddrInfo)
{
  const auto ADDRESS = "127.0.0.1"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));

  const auto addr_info_response = client::get_addr_info(stub(), stack.stack_ref(), ADDRESS, "", {});

  EXPECT_SUCCESS(addr_info_response);
  EXPECT_EQ(1, addr_info_response.res().size());
  auto addr_info = addr_info_response.res()[0];
  EXPECT_EQ(0, addr_info.addr().ipv4().port());
  EXPECT_ADDR_EQ(AddressFamily::ADDRESS_FAMILY_INET, (127, 0, 0, 1), addr_info);
}

TEST_F(NiXnetSocketLoopbackTests, IPv6Address_GetAddrInfo_ReturnsExpectedAddrInfo)
{
  const auto ADDRESS = "fd00::1"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));

  const auto addr_info_response = client::get_addr_info(stub(), stack.stack_ref(), ADDRESS, "", {});

  EXPECT_SUCCESS(addr_info_response);
  EXPECT_EQ(1, addr_info_response.res().size());
  auto addr_info = addr_info_response.res()[0];
  EXPECT_EQ(0, addr_info.addr().ipv6().port());
  EXPECT_ADDR_EQ(AddressFamily::ADDRESS_FAMILY_INET6, (0xfd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01), addr_info);
}

TEST_F(NiXnetSocketLoopbackTests, NumericPortTranslation_GetAddrInfo_ReturnsExpectedAddrInfo)
{
  const auto PORT = "21"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));

  AddrInfoHint hints{};
  hints.set_family(AddressFamily::ADDRESS_FAMILY_INET);
  int32_t flags = GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_V4MAPPED |
      GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_ADDRCONFIG |
      GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_NUMERICHOST |
      GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_NUMERICSERV |
      GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_PASSIVE;
  hints.set_flags_raw(flags);
  const auto addr_info_response = client::get_addr_info(stub(), stack.stack_ref(), "", PORT, hints);

  EXPECT_SUCCESS(addr_info_response);
  EXPECT_EQ(1, addr_info_response.res().size());
  auto addr_info = addr_info_response.res()[0];
  EXPECT_ADDR_EQ(AddressFamily::ADDRESS_FAMILY_INET, (0, 0, 0, 0), addr_info);
  EXPECT_EQ(htons(21), addr_info.addr().ipv4().port());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4SockAddr_GetNameInfo_ReturnsExpectedNameInfo)
{
  const auto ADDRESS = "192.168.0.1"s;
  constexpr auto PORT_BYTE_SWAPPED = 0xD204;  // Network endian 1234;
  const auto EXPECTED_PORT = "1234"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto p_to_n = client::inet_p_to_n(stub(), stack.stack_ref(), 2 /* AF INET*/, ADDRESS);
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv4()->mutable_addr()->CopyFrom(p_to_n.addr().ipv4());
  sock_addr.mutable_ipv4()->set_port(PORT_BYTE_SWAPPED);

  const auto name_info = client::get_name_info(stub(), stack.stack_ref(), sock_addr, 256, 256, 0);

  EXPECT_SUCCESS(name_info);
  EXPECT_EQ(ADDRESS, name_info.host());
  EXPECT_EQ("1234", name_info.serv());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4SockAddr_GetNameInfoWithZeroServLen_ReturnsHostNameAndEmptyServ)
{
  const auto ADDRESS = "192.168.0.1"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto p_to_n = client::inet_p_to_n(stub(), stack.stack_ref(), 2 /* AF INET*/, ADDRESS);
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv4()->mutable_addr()->CopyFrom(p_to_n.addr().ipv4());
  sock_addr.mutable_ipv4()->set_port(0x1234);

  const auto name_info = client::get_name_info(stub(), stack.stack_ref(), sock_addr, 256, 0, 0);

  EXPECT_SUCCESS(name_info);
  EXPECT_EQ(ADDRESS, name_info.host());
  EXPECT_THAT(name_info.serv(), IsEmpty());
}

TEST_F(NiXnetSocketLoopbackTests, IPv4SockAddr_GetNameInfoWithFlags_ReturnsExpectedNameInfo)
{
  const auto ADDRESS = "192.168.0.1"s;
  constexpr auto PORT_BYTE_SWAPPED = 0xD204;  // Network endian 1234;
  const auto EXPECTED_PORT = "1234"s;
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto p_to_n = client::inet_p_to_n(stub(), stack.stack_ref(), 2 /* AF INET*/, ADDRESS);
  auto sock_addr = SockAddr{};
  sock_addr.mutable_ipv4()->mutable_addr()->CopyFrom(p_to_n.addr().ipv4());
  sock_addr.mutable_ipv4()->set_port(PORT_BYTE_SWAPPED);

  // Note: These flags don't change the behavior of this test.
  const auto name_info = client::get_name_info(
      stub(),
      stack.stack_ref(),
      sock_addr,
      256,
      256,
      std::vector<GetNameInfoFlags>{
          GetNameInfoFlags::GET_NAME_INFO_FLAGS_NUMERICHOST,
          GetNameInfoFlags::GET_NAME_INFO_FLAGS_NUMERICSERV});

  EXPECT_SUCCESS(name_info);
  EXPECT_EQ(ADDRESS, name_info.host());
  EXPECT_EQ("1234", name_info.serv());
}

TEST_F(NiXnetSocketLoopbackTests, SetRcvBufSockOpt_Succeeds)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto sock = socket(stub(), stack.stack_ref());
  auto data = SockOptData{};
  data.set_data_int32(4096);
  const auto set_sock_opt = client::set_sock_opt(
      stub(),
      sock.socket(),
      SocketOptionLevel::SOCKET_OPTION_LEVEL_SOCKET,
      OptName::OPT_NAME_SO_RCVBUF, data);

  EXPECT_SUCCESS(set_sock_opt);
}

TEST_F(NiXnetSocketLoopbackTests, SetTcpNoDelaySockOpt_Succeeds)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto sock = socket(stub(), stack.stack_ref());
  auto data = SockOptData{};
  data.set_data_bool(true);
  const auto set_sock_opt = client::set_sock_opt(
      stub(),
      sock.socket(),
      SocketOptionLevel::SOCKET_OPTION_LEVEL_PROTO_TCP,
      OptName::OPT_NAME_TCP_NODELAY, data);

  EXPECT_SUCCESS(set_sock_opt);
}

TEST_F(NiXnetSocketLoopbackTests, SetTcpNoDelaySockOptWithInvalidLevel_ReportsError)
{
  const auto stack = client::ip_stack_create(stub(), "", create_simple_config("ENET1"));
  const auto sock = socket(stub(), stack.stack_ref());
  for (const auto invalid_level : {
           SocketOptionLevel::SOCKET_OPTION_LEVEL_PROTO_IP,
           SocketOptionLevel::SOCKET_OPTION_LEVEL_SOCKET}) {
    auto data = SockOptData{};
    data.set_data_bool(true);
    const auto set_sock_opt = client::set_sock_opt(stub(), sock.socket(), invalid_level, OptName::OPT_NAME_TCP_NODELAY, data);

    EXPECT_XNET_ERROR(-1, 13844, "Protocol not available", set_sock_opt);
  }
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/rfmx_macros.h sha256=d55077da734ec3d4159da167f36ccf75a8b0fea57ca487c7d3629d2cf732a1bd bytes=3786 -->
## FILE: source/tests/system/rfmx_macros.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/rfmx_macros.h`
- sha256: `d55077da734ec3d4159da167f36ccf75a8b0fea57ca487c7d3629d2cf732a1bd`
- bytes: 3786

````c
#ifndef NIDEVICE_GRPC_TESTS_RFMX_EXPECT_MACROS
#define NIDEVICE_GRPC_TESTS_RFMX_EXPECT_MACROS

#include <gmock/gmock.h>

#include <nlohmann/json.hpp>

#include "tests/utilities/test_helpers.h"

#define EXPECT_NO_ERROR_MESSAGE(session, response)                                                  \
  if (1) {                                                                                          \
    if ((response).status() != 0) {                                                                 \
      auto error_message_response = client::get_error_string(stub(), session, (response).status()); \
      EXPECT_EQ("", std::string(error_message_response.error_description().c_str()));               \
    }                                                                                               \
    auto error_response = client::get_error(stub(), session);                                       \
    EXPECT_EQ("", std::string(error_response.error_description().c_str()));                         \
  }

#define EXPECT_ERROR_SUBSTRING(message_substring, session)                \
  if (1) {                                                                \
    const auto error = client::get_error(stub(), (session));              \
    EXPECT_THAT(error.error_description(), HasSubstr(message_substring)); \
  }

#define EXPECT_RESPONSE_SUCCESS(response) \
  if (1) {                                \
    EXPECT_EQ(0, (response).status());    \
  }

#define EXPECT_RESPONSE_WARNING(expected_warning, response) \
  if (1) {                                                  \
    EXPECT_GT(expected_warning, 0);                         \
    EXPECT_EQ(expected_warning, (response).status());       \
  }

#define EXPECT_SUCCESS(session_, response_)     \
  ([this](auto& session, auto& response) {      \
    EXPECT_RESPONSE_SUCCESS(response);          \
    EXPECT_NO_ERROR_MESSAGE(session, response); \
    return response;                            \
  })((session_), (response_))

#define EXPECT_ERROR(expected_error_, message_substring_, session_, response_call_) \
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR(response_call_, expected_error_, message_substring_)

#define EXPECT_WARNING(expected_warning_, message_substring_, session_, response_)               \
  ([this](auto expected_warning, const auto& message_substring, auto& session, auto& response) { \
    EXPECT_RESPONSE_WARNING(expected_warning, response)                                          \
    EXPECT_ERROR_SUBSTRING(message_substring, session);                                          \
    return response;                                                                             \
  })(expected_warning_, message_substring_, session_, response_)

#define GET_ATTR_(get_attr_fn, session_, selector_string_, attribute_id_)                \
  ([this](auto& session, auto& selector_string, auto attribute_id) {                     \
    auto response = client::get_attr_fn(stub(), session, selector_string, attribute_id); \
    EXPECT_SUCCESS(session, response);                                                   \
    return response.attr_val();                                                          \
  })(session_, selector_string_, attribute_id_)

#define GET_ATTR_I32(session_, selector_string_, attribute_id_) \
  GET_ATTR_(get_attribute_i32, session_, selector_string_, attribute_id_)

#define GET_ATTR_F64(session_, selector_string_, attribute_id_) \
  GET_ATTR_(get_attribute_f64, session_, selector_string_, attribute_id_)

#define GET_ATTR_STR(session_, selector_string_, attribute_id_) \
  GET_ATTR_(get_attribute_string, session_, selector_string_, attribute_id_)

#endif  // NIDEVICE_GRPC_TESTS_RFMX_EXPECT_MACROS
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/session_utilities_service_tests.cpp sha256=49df29fea5aa21dff3ca9f1e6dd6723221aedcf037c0e9032cad40d1a78b9327 bytes=2009 -->
## FILE: source/tests/system/session_utilities_service_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/session_utilities_service_tests.cpp`
- sha256: `49df29fea5aa21dff3ca9f1e6dd6723221aedcf037c0e9032cad40d1a78b9327`
- bytes: 2009

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/session_utilities_service.h>

#include "device_server.h"

namespace ni {
namespace tests {
namespace system {

using ::testing::IsEmpty;
using ::testing::Not;

class SessionUtilitiesServiceTests : public ::testing::Test {
 protected:
  SessionUtilitiesServiceTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(nidevice_grpc::SessionUtilities::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~SessionUtilitiesServiceTests() {}

  std::unique_ptr<nidevice_grpc::SessionUtilities::Stub>& GetStub()
  {
    return stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::SessionUtilities::Stub> stub_;
};

TEST_F(SessionUtilitiesServiceTests, SysCfgLibraryPresent_EnumerateDevices_ResponseContainsAtLeastOneDevice)
{
  nidevice_grpc::EnumerateDevicesRequest request;
  nidevice_grpc::EnumerateDevicesResponse response;
  ::grpc::ClientContext context;

  ::grpc::Status status = GetStub()->EnumerateDevices(&context, request, &response);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_GE(response.devices_size(), 1);
}

TEST_F(SessionUtilitiesServiceTests, SysCfgLibraryPresent_EnumerateDevices_DevicePropertiesIncludesNameModelVendorSerialNumberProductId)
{
  nidevice_grpc::EnumerateDevicesRequest request;
  nidevice_grpc::EnumerateDevicesResponse response;
  ::grpc::ClientContext context;

  ::grpc::Status status = GetStub()->EnumerateDevices(&context, request, &response);

  for (auto device : response.devices()) {
    EXPECT_THAT(device.name(), Not(IsEmpty()));
    EXPECT_NE(device.model().c_str(), nullptr);
    EXPECT_THAT(device.vendor(), Not(IsEmpty()));
    EXPECT_NE(device.serial_number().c_str(), nullptr);
    EXPECT_NE(device.product_id(), 0);
  }
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/visa_driver_api_tests.cpp sha256=be1fd0c512490d973e77ed0beff6e0fa76f6ce0e2f69516acc88360e8b12188b bytes=28683 -->
## FILE: source/tests/system/visa_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/visa_driver_api_tests.cpp`
- sha256: `be1fd0c512490d973e77ed0beff6e0fa76f6ce0e2f69516acc88360e8b12188b`
- bytes: 28683

````cpp
#include "device_server.h"
#include "tests/utilities/tcp_echo_server.h"
#include "tests/utilities/test_helpers.h"
#include "visa/visa_client.h"

namespace ni {
namespace tests {
namespace system {

namespace visa = visa_grpc;
namespace client = visa_grpc::experimental::client;

class VisaDriverApiTest : public ::testing::Test {
 protected:
  VisaDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        visa_stub_(visa::Visa::NewStub(device_server_->InProcessChannel())),
        instrument_descriptor_ni_com_("TCPIP::www.ni.com::80::SOCKET")
  {
    device_server_->ResetServer();
  }

  virtual ~VisaDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session(instrument_descriptor_ni_com_);
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<visa::Visa::Stub>& GetStub()
  {
    return visa_stub_;
  }

  nidevice_grpc::Session GetNamedSession()
  {
    nidevice_grpc::Session vi;
    vi.set_name(driver_session_->name());
    return vi;
  }


  void initialize_driver_session(const std::string& instrument_descriptor)
  {
    ::grpc::ClientContext context;
    visa::OpenRequest request;
    visa::OpenResponse response;
    request.set_instrument_descriptor(instrument_descriptor);
    request.set_access_mode(visa::LOCK_STATE_NO_LOCK);
    request.set_session_name("SessionName");
    request.set_open_timeout(VI_TMO_IMMEDIATE);
    ::grpc::Status status = GetStub()->Open(&context, request, &response);
    client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    ASSERT_TRUE(status.ok());
    ASSERT_EQ(VI_SUCCESS, response.status());
  }

  void close_driver_session()
  {
    if (!driver_session_) {
      return;
    }
    auto response = client::close(GetStub(), GetNamedSession());
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void set_bool_attribute(visa::VisaAttribute attribute, bool value)
  {
    visa_grpc::AttributeValueData data;
    data.set_value_bool(value);
    auto response = client::set_attribute(GetStub(), GetNamedSession(), attribute, data);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void set_uint32_attribute(visa::VisaAttribute attribute, uint32_t value)
  {
    visa_grpc::AttributeValueData data;
    data.set_value_u32(value);
    auto response = client::set_attribute(GetStub(), GetNamedSession(), attribute, data);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  bool get_bool_attribute(visa::VisaAttribute attribute)
  {
    auto response = client::get_attribute(GetStub(), GetNamedSession(), attribute);
    EXPECT_EQ(VI_SUCCESS, response.status());
    EXPECT_TRUE(response.has_attribute_value());
    EXPECT_TRUE(response.attribute_value().has_value_bool());
    return response.attribute_value().value_bool();
  }

  int32 get_uint32_attribute(visa::VisaAttribute attribute)
  {
    auto response = client::get_attribute(GetStub(), GetNamedSession(), attribute);
    EXPECT_EQ(VI_SUCCESS, response.status());
    EXPECT_TRUE(response.has_attribute_value());
    EXPECT_TRUE(response.attribute_value().has_value_u32());
    return response.attribute_value().value_u32();
  }

  std::string get_string_attribute(visa::VisaAttribute attribute)
  {
    auto response = client::get_attribute(GetStub(), GetNamedSession(), attribute);
    EXPECT_EQ(VI_SUCCESS, response.status());
    EXPECT_TRUE(response.has_attribute_value());
    EXPECT_TRUE(response.attribute_value().has_value_string());
    return response.attribute_value().value_string();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<visa::Visa::Stub> visa_stub_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::string instrument_descriptor_ni_com_;
};

TEST_F(VisaDriverApiTest, GetOriginalTimeout_TwoSeconds)
{
  uint32_t originalTimeout = get_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE);

  EXPECT_EQ(2000, originalTimeout);
}

TEST_F(VisaDriverApiTest, SetTimeout_GetTimeout_MeetsSpecRequirement)
{
  uint32_t specifiedTimeout = 7500;
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE, specifiedTimeout);

  uint32_t newTimeout = get_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE);

  EXPECT_TRUE(newTimeout >= specifiedTimeout);
}

TEST_F(VisaDriverApiTest, GetHostname_Matches)
{
  std::string hostname = get_string_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TCPIP_HOSTNAME);

  EXPECT_EQ("www.ni.com", hostname);
}

TEST_F(VisaDriverApiTest, SetNonTcpipAttribute_ReturnsAttributeError)
{
  EXPECT_THROW_DRIVER_ERROR(
    set_bool_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_ASRL_ALLOW_TRANSMIT, true),
    VI_ERROR_NSUP_ATTR
  );
}

class VisaMessageBasedLoopbackTest : public VisaDriverApiTest {
  public:
  VisaMessageBasedLoopbackTest()
  {
  }
  virtual ~VisaMessageBasedLoopbackTest()
  {
  }

  void SetUp() override
  {
    ASSERT_EQ(0, echoserver_.start());

    std::string portNumber(std::to_string(echoserver_.get_server_port()));
    std::string instrument_descriptor("TCPIP0::localhost::" + portNumber + "::SOCKET");
    initialize_driver_session(instrument_descriptor);
    auto response = client::enable_event(GetStub(), GetNamedSession(), VI_EVENT_IO_COMPLETION, VI_QUEUE, VI_NULL);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void TearDown() override
  {
    echoserver_.prepare_stop();
    // Sending any single byte at this point will stop the server loop.
    client::write(GetStub(), GetNamedSession(), " ");

    close_driver_session();
    echoserver_.stop();
  }

  const uint32_t kWaitTimeoutMsec = 2000;
  const uint32_t kFastTimeoutMsec = 500;

  void write(const std::string& data)
  {
    auto response = client::write(GetStub(), GetNamedSession(), data);
    EXPECT_EQ(VI_SUCCESS, response.status());
    EXPECT_EQ(data.size(), response.return_count());
  }

  void write_async(const std::string& data)
  {
    auto asyncResponse = client::write_async(GetStub(), GetNamedSession(), data);
    EXPECT_THAT((std::array<ViStatus, 2>{ VI_SUCCESS, VI_SUCCESS_SYNC }), testing::Contains(asyncResponse.status()));
    auto waitResponse = client::wait_on_event(GetStub(), GetNamedSession(), VI_EVENT_IO_COMPLETION, kWaitTimeoutMsec);
    EXPECT_EQ(VI_SUCCESS, waitResponse.status());
    auto eventResponse = client::get_attribute_event(GetStub(), waitResponse.event_handle(), visa::VisaAttribute::VISA_ATTRIBUTE_STATUS);
    EXPECT_EQ(VI_SUCCESS, eventResponse.status());
    EXPECT_EQ(VI_SUCCESS, eventResponse.attribute_value().value_i32());
    eventResponse = client::get_attribute_event(GetStub(), waitResponse.event_handle(), visa::VisaAttribute::VISA_ATTRIBUTE_RET_COUNT);
    EXPECT_EQ(VI_SUCCESS, eventResponse.status());
    EXPECT_EQ(data.size(), eventResponse.attribute_value().value_u32());
    auto closeResponse = client::close_event(GetStub(), waitResponse.event_handle());
    EXPECT_EQ(VI_SUCCESS, closeResponse.status());
  }

  void read(size_t count, const std::string& expectedData, ViStatus expectedStatus)
  {
    auto response = client::read(GetStub(), GetNamedSession(), static_cast<uint32_t>(count));
    EXPECT_EQ(expectedStatus, response.status());
    EXPECT_EQ(expectedData.size(), response.return_count());
    EXPECT_EQ(expectedData, response.buffer());
  }

  void read_async(size_t count, const std::string& expectedData, ViStatus expectedStatus, bool requiresTerminate = false)
  {
    auto asyncResponse = client::read_async(GetStub(), GetNamedSession(), static_cast<uint32_t>(count));
    EXPECT_THAT((std::array<ViStatus, 2>{ VI_SUCCESS, VI_SUCCESS_SYNC }), testing::Contains(asyncResponse.status()));
    if (requiresTerminate) {
      std::this_thread::sleep_for(std::chrono::milliseconds(kFastTimeoutMsec));
      auto terminateResponse = client::terminate(GetStub(), GetNamedSession(), 0, asyncResponse.job_identifier());
      EXPECT_EQ(VI_SUCCESS, terminateResponse.status());
    }
    auto waitResponse = client::wait_on_event(GetStub(), GetNamedSession(), VI_EVENT_IO_COMPLETION, kWaitTimeoutMsec);
    EXPECT_EQ(VI_SUCCESS, waitResponse.status());
    auto eventResponse = client::get_attribute_event(GetStub(), waitResponse.event_handle(), visa::VisaAttribute::VISA_ATTRIBUTE_STATUS);
    EXPECT_EQ(VI_SUCCESS, eventResponse.status());
    EXPECT_EQ(expectedStatus, eventResponse.attribute_value().value_i32());
    eventResponse = client::get_attribute_event(GetStub(), waitResponse.event_handle(), visa::VisaAttribute::VISA_ATTRIBUTE_RET_COUNT);
    EXPECT_EQ(VI_SUCCESS, eventResponse.status());
    EXPECT_EQ(expectedData.size(), eventResponse.attribute_value().value_u32());
    eventResponse = client::get_attribute_event(GetStub(), waitResponse.event_handle(), visa::VisaAttribute::VISA_ATTRIBUTE_BUFFER);
    EXPECT_EQ(VI_SUCCESS, eventResponse.status());
    EXPECT_EQ(expectedData, eventResponse.attribute_value().value_bytes());
    auto closeResponse = client::close_event(GetStub(), waitResponse.event_handle());
    EXPECT_EQ(VI_SUCCESS, closeResponse.status());
  }

  void assert_trigger(visa::TriggerProtocol protocol)
  {
    auto response = client::assert_trigger(GetStub(), GetNamedSession(), protocol);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void flush(visa::BufferMask mask)
  {
    auto response = client::flush(GetStub(), GetNamedSession(), mask);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  private:
    TcpEchoServer echoserver_;
};

TEST_F(VisaMessageBasedLoopbackTest, WriteAndRead_Matches)
{
  std::string writeData = "Visa gRPC read/write test";
  write(writeData);
  read(writeData.size(), writeData, VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, WriteAsyncAndReadAsync_Matches)
{
  std::string writeData = "Visa gRPC read/write test";
  write_async(writeData);
  read_async(writeData.size(), writeData, VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, WriteTwice_ReadOnce_Matches)
{
  std::string writeData = "Visa gRPC read/write test";
  write(writeData + "1 ");
  write(writeData + "2");
  std::string expectedReadData = writeData + "1 " + writeData + "2";
  read(expectedReadData.size(), expectedReadData, VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadMoreThanWritten_ReturnTimeoutErrorWithDataInResponsePacket)
{
  std::string writeData = "Visa gRPC read/write test";
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE, kFastTimeoutMsec);
  write(writeData);
  read(writeData.size() + 1, writeData, VI_ERROR_TMO);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadAsyncMoreThanWritten_ReturnTimeoutErrorWithDataInResponsePacket)
{
  std::string writeData = "Visa gRPC read/write test";
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE, kFastTimeoutMsec);
  write(writeData);
  read_async(writeData.size() + 1, writeData, VI_ERROR_ABORT, true);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadLessThanWritten_ReturnSuccess)
{
  std::string writeData = "Visa gRPC read/write test";
  write(writeData);
  read(writeData.size() - 1, writeData.substr(0, writeData.size() - 1), VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadAsyncLessThanWritten_ReturnSuccess)
{
  std::string writeData = "Visa gRPC read/write test";
  write(writeData);
  read_async(writeData.size() - 1, writeData.substr(0, writeData.size() - 1), VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadZeroBytes_ReturnSuccess)
{
  std::string writeData = "Visa gRPC read/write test";
  write(writeData);
  read(0, "", VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadAsyncZeroBytes_ReturnSuccess)
{
  std::string writeData = "Visa gRPC read/write test";
  write_async(writeData);
  read_async(0, "", VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, ReadWithoutWrite_ThrowsError)
{
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE, kFastTimeoutMsec);
  EXPECT_THROW_DRIVER_ERROR(
    read(10, "", -1),
    VI_ERROR_TMO);
}

TEST_F(VisaMessageBasedLoopbackTest, WriteSpecialData_ReadMatches)
{
  const char buffer[] = {'A', '\0', 'B', '\0', 'C'};
  std::string writeData(buffer, sizeof(buffer));
  write(writeData);
  read(writeData.size(), writeData, VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, WriteAsyncSpecialData_ReadAsyncMatches)
{
  const char buffer[] = {'A', '\0', 'B', '\0', 'C'};
  std::string writeData(buffer, sizeof(buffer));
  write_async(writeData);
  read_async(writeData.size(), writeData, VI_SUCCESS_MAX_CNT);
}

TEST_F(VisaMessageBasedLoopbackTest, WriteWithTermChar_ReadMatches)
{
  std::string writeData = "Hello\nWorld\n";

  write(writeData);
  set_bool_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TERMCHAR_EN, true);
  read(255, "Hello\n", VI_SUCCESS_TERM_CHAR);
  read(255, "World\n", VI_SUCCESS_TERM_CHAR);
}

TEST_F(VisaMessageBasedLoopbackTest, AssertTrigger_SendsCommand)
{
  set_bool_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TERMCHAR_EN, true);
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_IO_PROT, 4); // VI_PROT_4882_STRS 
  assert_trigger(visa::TRIGGER_PROTOCOL_PROT_DEFAULT);
  read(255, "*TRG\n", VI_SUCCESS_TERM_CHAR);
}

TEST_F(VisaMessageBasedLoopbackTest, Flush_ClearsBuffer)
{
  set_uint32_attribute(visa::VisaAttribute::VISA_ATTRIBUTE_TMO_VALUE, kFastTimeoutMsec);
  write("Some data in the pipe\n");
  flush(visa::BUFFER_MASK_IO_IN_BUF_DISCARD);
  EXPECT_THROW_DRIVER_ERROR(
    read(10, "", -1),
    VI_ERROR_TMO);
}

class VisaRegisterBasedLoopbackTest : public VisaDriverApiTest {
  public:
  VisaRegisterBasedLoopbackTest() : allocatedBase_(0), mappedBase_(0)
  {
  }
  virtual ~VisaRegisterBasedLoopbackTest()
  {
  }

  void SetUp() override
  {
    initialize_driver_session("PXI::MEMACC");
    auto response = client::mem_alloc_ex(GetStub(), GetNamedSession(), 4096);
    ASSERT_EQ(VI_SUCCESS, response.status());
    allocatedBase_ = response.offset();
  }

  void TearDown() override
  {
    free(allocatedBase_);
    close_driver_session();
  }

  void free(uint64_t offset)
  {
    auto response = client::mem_free(GetStub(), GetNamedSession(), offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  ViUInt8 in8(uint64_t offset)
  {
    auto response = client::in8(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt16 in16(uint64_t offset)
  {
    auto response = client::in16(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt32 in32(uint64_t offset)
  {
    auto response = client::in32(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt64 in64(uint64_t offset)
  {
    auto response = client::in64(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  void out8(uint64_t offset, ViUInt8 value)
  {
    auto response = client::out8(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void out16(uint64_t offset, ViUInt16 value)
  {
    auto response = client::out16(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void out32(uint64_t offset, ViUInt32 value)
  {
    auto response = client::out32(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void out64(uint64_t offset, ViUInt64 value)
  {
    auto response = client::out64(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  std::vector<ViUInt8> moveIn8(uint64_t offset, int length)
  {
    auto response = client::move_in8(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, length);
    EXPECT_EQ(VI_SUCCESS, response.status());
    std::vector<ViUInt8> retval;
    const std::string& responseBuffer = response.buffer();
    for (int i = 0; i < responseBuffer.length(); i++) {
      retval.push_back(responseBuffer[i]);
    }
    return retval;
  }

  google::protobuf::RepeatedField<uint32_t> moveIn16(uint64_t offset, int length)
  {
    auto response = client::move_in16(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, length);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.buffer();
  }

  google::protobuf::RepeatedField<uint32_t> moveIn32(uint64_t offset, int length)
  {
    auto response = client::move_in32(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, length);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.buffer();
  }

  google::protobuf::RepeatedField<uint64_t> moveIn64(uint64_t offset, int length)
  {
    auto response = client::move_in64(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, length);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.buffer();
  }

  void moveOut8(uint64_t offset, ViUInt8 data[], int length)
  {
    std::string buffer(reinterpret_cast<char*>(data), length);
    auto response = client::move_out8(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, buffer);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void moveOut16(uint64_t offset, ViUInt16 data[], int length)
  {
    std::vector<uint32_t> buffer;
    for (int i = 0; i < length; i++) {
      buffer.push_back(data[i]);
    }
    auto response = client::move_out16(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, buffer);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void moveOut32(uint64_t offset, ViUInt32 data[], int length)
  {
    std::vector<uint32_t> buffer;
    for (int i = 0; i < length; i++) {
      buffer.push_back(data[i]);
    }
    auto response = client::move_out32(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, buffer);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void moveOut64(uint64_t offset, ViUInt64 data[], int length)
  {
    std::vector<uint64_t> buffer;
    for (int i = 0; i < length; i++) {
      buffer.push_back(data[i]);
    }
    auto response = client::move_out64(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_ + offset, buffer);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void map()
  {
    auto response = client::map_address(GetStub(), GetNamedSession(), visa::ADDRESS_SPACE_PXI_ALLOC_SPACE, allocatedBase_, 4096, false, 0);
    EXPECT_EQ(VI_SUCCESS, response.status());
    mappedBase_ = response.address();
  }

  void unmap()
  {
    auto response = client::unmap_address(GetStub(), GetNamedSession());
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  ViUInt8 peek8(uint64_t offset)
  {
    auto response = client::peek8(GetStub(), GetNamedSession(), mappedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt16 peek16(uint64_t offset)
  {
    auto response = client::peek16(GetStub(), GetNamedSession(), mappedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt32 peek32(uint64_t offset)
  {
    auto response = client::peek32(GetStub(), GetNamedSession(), mappedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  ViUInt64 peek64(uint64_t offset)
  {
    auto response = client::peek64(GetStub(), GetNamedSession(), mappedBase_ + offset);
    EXPECT_EQ(VI_SUCCESS, response.status());
    return response.value();
  }

  void poke8(uint64_t offset, ViUInt8 value)
  {
    auto response = client::poke8(GetStub(), GetNamedSession(), mappedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void poke16(uint64_t offset, ViUInt16 value)
  {
    auto response = client::poke16(GetStub(), GetNamedSession(), mappedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void poke32(uint64_t offset, ViUInt32 value)
  {
    auto response = client::poke32(GetStub(), GetNamedSession(), mappedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  void poke64(uint64_t offset, ViUInt64 value)
  {
    auto response = client::poke64(GetStub(), GetNamedSession(), mappedBase_ + offset, value);
    EXPECT_EQ(VI_SUCCESS, response.status());
  }

  private:
    uint64_t allocatedBase_;
    uint64_t mappedBase_;
};

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut8_In8_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 11;
  ViUInt8 buffer[testLength] = { 0x01, 0x02, 0x00, 0x03, 0xFE };
  moveOut8(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], in8(startingOffset + i));
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut16_In16_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 14;
  ViUInt16 buffer[testLength] = { 0x0123, 0x0234, 0x00, 0x8675, 0xFEDC };
  moveOut16(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], in16(startingOffset + i * 2));
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut32_In32_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt32 buffer[testLength] = { 0x01234567, 0x02340234, 0x00, 0x86754321, 0xC0FFEE };
  moveOut32(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], in32(startingOffset + i * 4));
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut64_In64_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt64 buffer[testLength] = { 0x01234567DEADBEEF, 0x02340234, 0x00, 0x867543210ABCDEF, 0xC0FFEE };
  moveOut64(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], in64(startingOffset + i * 8));
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithOut8_MoveIn8_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 11;
  ViUInt8 buffer[testLength] = { 0x01, 0x02, 0x00, 0x03, 0xFE };
  for (int i = 0; i < testLength; ++i) {
    out8(startingOffset + i, buffer[i]);
  }
  auto readBuffer = moveIn8(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithOut16_MoveIn16_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 14;
  ViUInt16 buffer[testLength] = { 0x0123, 0x0234, 0x00, 0x8675, 0xFEDC };
  for (int i = 0; i < testLength; ++i) {
    out16(startingOffset + i * 2, buffer[i]);
  }
  auto readBuffer = moveIn16(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithOut32_MoveIn32_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt32 buffer[testLength] = { 0x01234567, 0x02340234, 0x00, 0x86754321, 0xC0FFEE };
  for (int i = 0; i < testLength; ++i) {
    out32(startingOffset + i * 4, buffer[i]);
  }
  auto readBuffer = moveIn32(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithOut64_MoveIn64_ReadsData)
{
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt64 buffer[testLength] = { 0x01234567DEADBEEF, 0x02340234, 0x00, 0x867543210ABCDEF, 0xC0FFEE };
  for (int i = 0; i < testLength; ++i) {
    out64(startingOffset + i * 8, buffer[i]);
  }
  auto readBuffer = moveIn64(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut8_Peek8_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 11;
  ViUInt8 buffer[testLength] = { 0x01, 0x02, 0x00, 0x03, 0xFE };
  moveOut8(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], peek8(startingOffset + i));
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut16_Peek16_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 14;
  ViUInt16 buffer[testLength] = { 0x0123, 0x0234, 0x00, 0x8675, 0xFEDC };
  moveOut16(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], peek16(startingOffset + i * 2));
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut32_Peek32_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt32 buffer[testLength] = { 0x01234567, 0x02340234, 0x00, 0x86754321, 0xC0FFEE };
  moveOut32(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], peek32(startingOffset + i * 4));
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithMoveOut64_Peek64_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt64 buffer[testLength] = { 0x01234567DEADBEEF, 0x02340234, 0x00, 0x867543210ABCDEF, 0xC0FFEE };
  moveOut64(startingOffset, buffer, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(buffer[i], peek64(startingOffset + i * 8));
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithPoke8_MoveIn8_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 11;
  ViUInt8 buffer[testLength] = { 0x01, 0x02, 0x00, 0x03, 0xFE };
  for (int i = 0; i < testLength; ++i) {
    poke8(startingOffset + i, buffer[i]);
  }
  auto readBuffer = moveIn8(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithPoke16_MoveIn16_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 14;
  ViUInt16 buffer[testLength] = { 0x0123, 0x0234, 0x00, 0x8675, 0xFEDC };
  for (int i = 0; i < testLength; ++i) {
    poke16(startingOffset + i * 2, buffer[i]);
  }
  auto readBuffer = moveIn16(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithPoke32_MoveIn32_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt32 buffer[testLength] = { 0x01234567, 0x02340234, 0x00, 0x86754321, 0xC0FFEE };
  for (int i = 0; i < testLength; ++i) {
    poke32(startingOffset + i * 4, buffer[i]);
  }
  auto readBuffer = moveIn32(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
  unmap();
}

TEST_F(VisaRegisterBasedLoopbackTest, DataWrittenWithPoke64_MoveIn64_ReadsData)
{
  map();
  const int testLength = 5;
  const int startingOffset = 16;
  ViUInt64 buffer[testLength] = { 0x01234567DEADBEEF, 0x02340234, 0x00, 0x867543210ABCDEF, 0xC0FFEE };
  for (int i = 0; i < testLength; ++i) {
    poke64(startingOffset + i * 8, buffer[i]);
  }
  auto readBuffer = moveIn64(startingOffset, testLength);
  for (int i = 0; i < testLength; ++i) {
    EXPECT_EQ(readBuffer[i], buffer[i]);
  }
  unmap();
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/visa_session_tests.cpp sha256=a1e3e5254c46b4e2c8f545481fe2efc64dd801745660bc5612d2ff5d5e79f37a bytes=4269 -->
## FILE: source/tests/system/visa_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/visa_session_tests.cpp`
- sha256: `a1e3e5254c46b4e2c8f545481fe2efc64dd801745660bc5612d2ff5d5e79f37a`
- bytes: 4269

````cpp
#include "device_server.h"
#include "tests/utilities/test_helpers.h"
#include "visa/visa_client.h"

namespace ni {
namespace tests {
namespace system {

namespace visa = visa_grpc;

const int kInvalidRsrc = -1073807343;
const int kInvalidVisaSessionWarning = 1073676418;
const char* kVisaErrorInstrumentDescriptorNotFoundMessage = "Insufficient location information or the device or resource is not present in the system.";
const char* kInstrumentDescriptor = "TCPIP::www.ni.com::80::SOCKET";
const char* kVisaTestSession = "SessionName";
const char* kVisaTestInvalidInstrumentDescriptor = "FOO::BAR";

class VisaSessionTest : public ::testing::Test {
 protected:
  VisaSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        visa_stub_(visa::Visa::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~VisaSessionTest() {}

  std::unique_ptr<visa::Visa::Stub>& GetStub()
  {
    return visa_stub_;
  }

  ::grpc::Status call_open(const char* instrument_descriptor, visa::LockState access_mode, const char* session_name, uint32_t open_timeout, visa::OpenResponse* response)
  {
    ::grpc::ClientContext context;
    visa::OpenRequest request;
    request.set_instrument_descriptor(instrument_descriptor);
    request.set_access_mode(access_mode);
    request.set_session_name(session_name);
    request.set_open_timeout(open_timeout);

    ::grpc::Status status = GetStub()->Open(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<visa::Visa::Stub> visa_stub_;
};

TEST_F(VisaSessionTest, OpenSessionWithInstrumentDescriptor_CreatesDriverSession)
{
  visa::OpenResponse response;
  ::grpc::Status status = call_open(kInstrumentDescriptor, visa::LOCK_STATE_NO_LOCK, kVisaTestSession, 0, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_EQ(kVisaTestSession, response.vi().name());
}

TEST_F(VisaSessionTest, OpenSessionWithInstrumentDescriptorAndNoSessionName_CreatesDriverSession)
{
  visa::OpenResponse response;
  ::grpc::Status status = call_open(kInstrumentDescriptor, visa::LOCK_STATE_NO_LOCK, "", 0, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(VisaSessionTest, OpenSession_CloseSession_ClosesDriverSession)
{
  visa::OpenResponse open_response;
  call_open(kInstrumentDescriptor, visa::LOCK_STATE_NO_LOCK, kVisaTestSession, 0, &open_response);

  nidevice_grpc::Session session = open_response.vi();
  ::grpc::ClientContext context;
  visa::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  visa::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(VisaSessionTest, OpenWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR(
    {
      visa::OpenResponse init_response;
      call_open(kVisaTestInvalidInstrumentDescriptor, visa::LOCK_STATE_NO_LOCK, "", 0, &init_response);
    },
    kInvalidRsrc,
    kVisaErrorInstrumentDescriptorNotFoundMessage);
}

TEST_F(VisaSessionTest, OpenWithErrorFromDriver_ReturnsDriverErrorWithResourceDescriptor)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR(
    {
      visa::OpenResponse init_response;
      call_open(kVisaTestInvalidInstrumentDescriptor, visa::LOCK_STATE_NO_LOCK, "", 0, &init_response);
    },
    kInvalidRsrc,
    kVisaTestInvalidInstrumentDescriptor);
}

TEST_F(VisaSessionTest, InvalidSession_CloseSession_ReturnsWarning)
{
  nidevice_grpc::Session session;
  session.set_name("");

  ::grpc::ClientContext context;
  visa::CloseRequest request;
  request.mutable_vi()->set_name(session.name());
  visa::CloseResponse response;
  auto status = GetStub()->Close(&context, request, &response);
  EXPECT_EQ(kInvalidVisaSessionWarning, response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/waveform_helpers.h sha256=f64af33485fa90531e23a211eaf6469ab88244b79dc9edac8c93f94476700918 bytes=3232 -->
## FILE: source/tests/system/waveform_helpers.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/waveform_helpers.h`
- sha256: `f64af33485fa90531e23a211eaf6469ab88244b79dc9edac8c93f94476700918`
- bytes: 3232

````c
#ifndef NIDEVICE_GRPC_TESTS_WAVEFORM_HELPERS
#define NIDEVICE_GRPC_TESTS_WAVEFORM_HELPERS

#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <vector>

namespace ni {
namespace tests {
namespace system {

template <typename TComplex>
struct TestWaveform {
  double t0;
  double dt;
  std::vector<TComplex> data;
};

template <typename TFloat>
struct TestIQData {
  double t0;
  double dt;
  std::vector<TFloat> I;
  std::vector<TFloat> Q;
};

template <typename TFloat, typename TComplex>
TComplex complex(TFloat real, TFloat imaginary)
{
  auto c = TComplex{};
  c.set_real(real);
  c.set_imaginary(imaginary);
  return c;
}

template <typename TFloat, typename TComplex>
std::vector<TComplex> complex_array(
    const std::vector<TFloat>& reals,
    const std::vector<TFloat>& imaginaries)
{
  auto c = std::vector<TComplex>{};
  c.reserve(reals.size());
  std::transform(
      reals.begin(),
      reals.end(),
      imaginaries.begin(),
      std::back_inserter(c),
      [](TFloat real, TFloat imaginary) { return complex<TFloat, TComplex>(real, imaginary); });
  return c;
}

template <typename TFloat>
TestIQData<TFloat> load_iq_data_from_json(nlohmann::json json)
{
  auto t0 = json.find("t0")->get<double>();
  auto dt = json.find("dt")->get<double>();
  auto reals = json.find("reals")->get<std::vector<TFloat>>();
  auto imaginaries = json.find("imaginaries")->get<std::vector<TFloat>>();
  return {t0, dt, reals, imaginaries};
}

template <typename TFloat>
TestIQData<TFloat> load_test_iq_data(const std::string& file_name)
{
  std::ifstream input_stream(file_name);
  auto json = nlohmann::json::parse(input_stream);
  return load_iq_data_from_json<TFloat>(json);
}

template <typename TFloat, typename TComplex>
TestWaveform<TComplex> load_test_waveform_data(const std::string& file_name)
{
  const auto iq_data = load_test_iq_data<TFloat>(file_name);
  return {iq_data.t0, iq_data.dt, complex_array<TFloat, TComplex>(iq_data.I, iq_data.Q)};
}

template <typename TFloat>
std::vector<TestIQData<TFloat>> load_test_multiple_iq_data(const std::string& file_name, const int count)
{
  auto iq_data = std::vector<TestIQData<TFloat>>{};
  std::ifstream input_stream(file_name);
  auto json = nlohmann::json::parse(input_stream);
  for (int i = 1; i <= count; i++) {
    auto key = "waveform" + std::to_string(i);
    auto waveform_json = json.at(key);
    auto data = load_iq_data_from_json<TFloat>(waveform_json);
    iq_data.push_back(data);
  }
  return iq_data;
}

template <typename TFloat, typename TComplex>
std::vector<TestWaveform<TComplex>> load_test_multiple_waveforms_data(const std::string& file_name, const int count)
{
  auto waveforms = std::vector<TestWaveform<TComplex>>{};
  const auto iq_data = load_test_multiple_iq_data<TFloat>(file_name, count);
  for (int i = 0; i < count; i++) {
    auto waveform = iq_data[i];
    waveforms.push_back({waveform.t0, waveform.dt, complex_array<TFloat, TComplex>(waveform.I, waveform.Q)});
  }
  return waveforms;
}

}  // namespace system
}  // namespace tests
}  // namespace ni

#endif  // NIDEVICE_GRPC_TESTS_WAVEFORM_HELPERS
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/calibration_operations_tests.cpp sha256=e804a6422527d3ada5a321ceb0cd4617224d0af9c75f6666691bbc172ff76b1b bytes=33204 -->
## FILE: source/tests/unit/calibration_operations_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/calibration_operations_tests.cpp`
- sha256: `e804a6422527d3ada5a321ceb0cd4617224d0af9c75f6666691bbc172ff76b1b`
- bytes: 33204

````cpp
#include <grpcpp/test/server_context_test_spouse.h>
#include <gtest/gtest.h>
#include <server/calibration_operations_restricted_service.h>
#include <server/converters.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>

namespace ni {
namespace tests {
namespace unit {

using ::ni::tests::utilities::CastAndSetArgPointee;
using ::testing::_;
using ::testing::Action;
using ::testing::DoAll;
using ::testing::Invoke;
using ::testing::NiceMock;
using ::testing::Return;
using ::testing::Throw;
using ::testing::WithArg;

const std::string kIntCalName0 = "Gain Reference";
const std::string kIntCalName1 = "Amplitude Accuracy";
const std::string kIntCalName2 = "Residual LO Power";
const std::string kIntCalName3 = "Image Suppression";

const double kIntCalLastTemp0 = 51.2;
const double kIntCalLastTemp1 = 52.3;
const double kIntCalLastTemp2 = 53.4;
const double kIntCalLastTemp3 = 54.5;

const NISysCfgTimestampUTC kIntCalLastTime0 = {{1}};
const NISysCfgTimestampUTC kIntCalLastTime1 = {{2}};
const NISysCfgTimestampUTC kIntCalLastTime2 = {{3}};
const NISysCfgTimestampUTC kIntCalLastTime3 = {{4}};

static google::protobuf::Timestamp convert_syscfg_timestamp_to_protobuf_timestamp(const NISysCfgTimestampUTC& syscfg_timestamp)
{
  google::protobuf::Timestamp protobuf_timestamp;
  nidevice_grpc::converters::convert_to_grpc(*reinterpret_cast<const CVIAbsoluteTime*>(&syscfg_timestamp), &protobuf_timestamp);
  return protobuf_timestamp;
}

const google::protobuf::Timestamp kIntCalLastTimeProtobufTimestamp0 = convert_syscfg_timestamp_to_protobuf_timestamp(kIntCalLastTime0);
const google::protobuf::Timestamp kIntCalLastTimeProtobufTimestamp1 = convert_syscfg_timestamp_to_protobuf_timestamp(kIntCalLastTime1);
const google::protobuf::Timestamp kIntCalLastTimeProtobufTimestamp2 = convert_syscfg_timestamp_to_protobuf_timestamp(kIntCalLastTime2);
const google::protobuf::Timestamp kIntCalLastTimeProtobufTimestamp3 = convert_syscfg_timestamp_to_protobuf_timestamp(kIntCalLastTime3);

const double kExtCalLastTemp0 = 45.6;
const double kExtCalLastTemp1 = 56.7;

const NISysCfgTimestampUTC kExtCalLastTime0 = {{5}};
const NISysCfgTimestampUTC kExtCalLastTime1 = {{6}};

const google::protobuf::Timestamp kExtCalLastTimeProtobufTimestamp0 = convert_syscfg_timestamp_to_protobuf_timestamp(kExtCalLastTime0);
const google::protobuf::Timestamp kExtCalLastTimeProtobufTimestamp1 = convert_syscfg_timestamp_to_protobuf_timestamp(kExtCalLastTime1);

const NISysCfgTimestampUTC kNextCalTime0 = {{7}};
const NISysCfgTimestampUTC kNextCalTime1 = {{8}};

const google::protobuf::Timestamp kNextCalTimeProtobufTimestamp0 = convert_syscfg_timestamp_to_protobuf_timestamp(kNextCalTime0);
const google::protobuf::Timestamp kNextCalTimeProtobufTimestamp1 = convert_syscfg_timestamp_to_protobuf_timestamp(kNextCalTime1);

ACTION_P(CopyStringToArg3, value)
{
  strcpy(static_cast<char*>(arg3), value);
}

static void configure_mock_library_calibration_properties_do_not_exist(NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library)
{ 
  EXPECT_CALL(*mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsInternalCalibration, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyNumberOfInternalCalibrationDetails, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsExternalCalibration, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTemp, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTime, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyRecommendedNextCalibrationTime, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
}

static void configure_mock_library_no_calibration_support(NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library)
{ 
  unsigned int number_of_internal_calibration_regions = 0;

  EXPECT_CALL(*mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsInternalCalibration, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(NISysCfgBoolFalse), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyNumberOfInternalCalibrationDetails, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(number_of_internal_calibration_regions), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, _, _))
      .Times(0);
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsExternalCalibration, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(false), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTemp, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTime, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyRecommendedNextCalibrationTime, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
}

static void configure_mock_library_no_indexed_properties(
  NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library,
  NISysCfgBool internal_calibration_supported,
  unsigned int number_of_internal_calibration_regions,
  NISysCfgBool external_calibration_supported,
  double external_calibration_last_temperature,
  NISysCfgTimestampUTC external_calibration_last_time,
  NISysCfgTimestampUTC next_calibration_time)
{ 
  EXPECT_CALL(*mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsInternalCalibration, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(internal_calibration_supported), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyNumberOfInternalCalibrationDetails, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(number_of_internal_calibration_regions), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertySupportsExternalCalibration, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(external_calibration_supported), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTemp, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(external_calibration_last_temperature), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyExternalCalibrationLastTime, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(external_calibration_last_time), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceProperty(_, NISysCfgResourcePropertyRecommendedNextCalibrationTime, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(next_calibration_time), Return(NISysCfg_OK)));
}

static void configure_mock_library_one_internal_calibration_region(NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library)
{
  configure_mock_library_no_indexed_properties(
    mock_library,
    NISysCfgBoolTrue, //internal_calibration_supported
    1, //number_of_internal_calibration_regions
    NISysCfgBoolTrue, //external_calibration_supported
    kExtCalLastTemp0,
    kExtCalLastTime0,
    kNextCalTime0);

  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, 0, _))
      .WillOnce(DoAll(CopyStringToArg3(kIntCalName0.c_str()), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, 0, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTemp0), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, 0, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTime0), Return(NISysCfg_OK)));
}

static void configure_mock_library_three_internal_calibration_regions(NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library)
{
  configure_mock_library_no_indexed_properties(
    mock_library,
    NISysCfgBoolTrue, //internal_calibration_supported
    3, //number_of_internal_calibration_regions
    NISysCfgBoolTrue, //external_calibration_supported
    kExtCalLastTemp1,
    kExtCalLastTime1,
    kNextCalTime1);

  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, 0, _))
      .WillOnce(DoAll(CopyStringToArg3(kIntCalName1.c_str()), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, 1, _))
      .WillOnce(DoAll(CopyStringToArg3(kIntCalName2.c_str()), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, 2, _))
      .WillOnce(DoAll(CopyStringToArg3(kIntCalName3.c_str()), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, 0, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTemp1), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, 1, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTemp2), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, 2, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTemp3), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, 0, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTime1), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, 1, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTime2), Return(NISysCfg_OK)));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, 2, _))
      .WillOnce(DoAll(CastAndSetArgPointee<3>(kIntCalLastTime3), Return(NISysCfg_OK)));
}

static void configure_mock_library_three_internal_calibration_regions_indexed_properties_do_not_exist(NiceMock<ni::tests::utilities::SysCfgMockLibrary>* mock_library)
{
  configure_mock_library_no_indexed_properties(
    mock_library,
    NISysCfgBoolTrue, //internal_calibration_supported
    3, //number_of_internal_calibration_regions
    NISysCfgBoolTrue, //external_calibration_supported
    kExtCalLastTemp1,
    kExtCalLastTime1,
    kNextCalTime1);

  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationName, _, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTemp, _, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(*mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyInternalCalibrationLastTime, _, _))
      .WillOnce(Return(NISysCfg_PropDoesNotExist));
}

TEST(CalibrationOperationsTests, SupportsIntCal_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_supports_internal_calibration());
  EXPECT_TRUE(response.supports_internal_calibration());
}

TEST(CalibrationOperationsTests, DoesNotSupportIntCal_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_no_calibration_support(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_supports_internal_calibration());
  EXPECT_FALSE(response.supports_internal_calibration());
}

TEST(CalibrationOperationsTests, SupportsIntCalPropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_supports_internal_calibration());
  EXPECT_FALSE(response.supports_internal_calibration());
}

TEST(CalibrationOperationsTests, NoIntCalRegions_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_no_calibration_support(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_number_of_internal_calibration_details());
  EXPECT_EQ(0, response.number_of_internal_calibration_details());
}

TEST(CalibrationOperationsTests, OneIntCalRegion_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_number_of_internal_calibration_details());
  EXPECT_EQ(1, response.number_of_internal_calibration_details());
}

TEST(CalibrationOperationsTests, ThreeIntCalRegions_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_number_of_internal_calibration_details());
  EXPECT_EQ(3, response.number_of_internal_calibration_details());
}

TEST(CalibrationOperationsTests, NumberOfIntCalDetailsPropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_number_of_internal_calibration_details());
  EXPECT_EQ(0, response.number_of_internal_calibration_details());
}

TEST(CalibrationOperationsTests, OneIntCalName_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, response.internal_calibration_names().size());
  if (response.internal_calibration_names().size() == 1)
  {
    EXPECT_EQ(kIntCalName0, response.internal_calibration_names()[0]);
  }
}

TEST(CalibrationOperationsTests, ThreeIntCalNames_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(3, response.internal_calibration_names().size());
  if (response.internal_calibration_names().size() == 3)
  {
    EXPECT_EQ(kIntCalName1, response.internal_calibration_names()[0]);
    EXPECT_EQ(kIntCalName2, response.internal_calibration_names()[1]);
    EXPECT_EQ(kIntCalName3, response.internal_calibration_names()[2]);
  }
}

TEST(CalibrationOperationsTests, IntCalNamePropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions_indexed_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.internal_calibration_names().size());
}

TEST(CalibrationOperationsTests, OneIntCalLastTemp_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, response.internal_calibration_last_temperatures().size());
  if (response.internal_calibration_last_temperatures().size() == 1)
  {
    EXPECT_EQ(kIntCalLastTemp0, response.internal_calibration_last_temperatures()[0]);
  }
}

TEST(CalibrationOperationsTests, ThreeIntCalLastTemps_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(3, response.internal_calibration_last_temperatures().size());
  if (response.internal_calibration_last_temperatures().size() == 3)
  {
    EXPECT_EQ(kIntCalLastTemp1, response.internal_calibration_last_temperatures()[0]);
    EXPECT_EQ(kIntCalLastTemp2, response.internal_calibration_last_temperatures()[1]);
    EXPECT_EQ(kIntCalLastTemp3, response.internal_calibration_last_temperatures()[2]);
  }
}

TEST(CalibrationOperationsTests, IntCalLastTempPropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions_indexed_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.internal_calibration_last_temperatures().size());
}

TEST(CalibrationOperationsTests, OneIntCalLastTime_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, response.internal_calibration_last_times().size());
  if (response.internal_calibration_last_times().size() == 1)
  {
    EXPECT_EQ(kIntCalLastTimeProtobufTimestamp0, response.internal_calibration_last_times()[0]);
  }
}

TEST(CalibrationOperationsTests, ThreeIntCalLastTimes_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(3, response.internal_calibration_last_times().size());
  if (response.internal_calibration_last_times().size() == 3)
  {
    EXPECT_EQ(kIntCalLastTimeProtobufTimestamp1, response.internal_calibration_last_times()[0]);
    EXPECT_EQ(kIntCalLastTimeProtobufTimestamp2, response.internal_calibration_last_times()[1]);
    EXPECT_EQ(kIntCalLastTimeProtobufTimestamp3, response.internal_calibration_last_times()[2]);
  }
}

TEST(CalibrationOperationsTests, IntCalLastTimePropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_three_internal_calibration_regions_indexed_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.internal_calibration_last_times().size());
}

TEST(CalibrationOperationsTests, SupportsExtCal_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_supports_external_calibration());
  EXPECT_TRUE(response.supports_external_calibration());
}

TEST(CalibrationOperationsTests, DoesNotSupportExtCal_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_no_calibration_support(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_supports_external_calibration());
  EXPECT_FALSE(response.supports_external_calibration());
}

TEST(CalibrationOperationsTests, SupportsExtCalPropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_supports_external_calibration());
  EXPECT_FALSE(response.supports_external_calibration());
}

TEST(CalibrationOperationsTests, ExtCalLastTempPropExists_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_external_calibration_last_temperature());
  EXPECT_EQ(kExtCalLastTemp0, response.external_calibration_last_temperature());
}

TEST(CalibrationOperationsTests, ExtCalLastTempPropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_external_calibration_last_temperature());
  EXPECT_EQ(0.0, response.external_calibration_last_temperature());
}

TEST(CalibrationOperationsTests, ExtCalLastTimePropExists_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_external_calibration_last_time());
  EXPECT_EQ(kExtCalLastTimeProtobufTimestamp0, response.external_calibration_last_time());
}

TEST(CalibrationOperationsTests, ExtCalLastTimePropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_external_calibration_last_time());
  EXPECT_EQ(::google::protobuf::Timestamp::default_instance(), response.external_calibration_last_time());
}

TEST(CalibrationOperationsTests, NextCalTimePropExists_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_one_internal_calibration_region(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.has_recommended_next_calibration_time());
  EXPECT_EQ(kNextCalTimeProtobufTimestamp0, response.recommended_next_calibration_time());
}

TEST(CalibrationOperationsTests, NextCalTimePropDoesNotExist_GetCalibrationInformation_ResponseWritten)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_restricted_grpc::CalibrationOperationsRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::GetCalibrationInformationRequest request;
  nidevice_restricted_grpc::GetCalibrationInformationResponse response;
  configure_mock_library_calibration_properties_do_not_exist(&mock_library);

  ::grpc::Status status = service.GetCalibrationInformation(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_FALSE(response.has_recommended_next_calibration_time());
  EXPECT_EQ(::google::protobuf::Timestamp::default_instance(), response.recommended_next_calibration_time());
}

}  // namespace unit

}  // namespace tests

}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/callback_router_tests.cpp sha256=44856c3d1e69653df67dd4eb656f40499332846073d9f2c44f542f672fef22fc bytes=5480 -->
## FILE: source/tests/unit/callback_router_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/callback_router_tests.cpp`
- sha256: `44856c3d1e69653df67dd4eb656f40499332846073d9f2c44f542f672fef22fc`
- bytes: 5480

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/callback_router.h>

#include <cstdint>
#include <string>

using namespace nidevice_grpc;
using namespace ::testing;

namespace ni {
namespace tests {
namespace unit {

const int TEST_SUCCESS = 0;
static void* BOGUS_TOKEN = reinterpret_cast<void*>(123456);

using TestStatus = int32_t;
using IntCallbackRouter = CallbackRouter<TestStatus, int32_t>;
using BoolAndStringCallbackRouter = CallbackRouter<TestStatus, bool, std::string>;

using MockIntHandler = MockFunction<TestStatus(int32_t)>;
using MockBoolAndStringHandler = MockFunction<TestStatus(bool, std::string)>;

template <typename THandler, typename... TArgs>
void EXPECT_CALLBACK(THandler& handler, TArgs... args)
{
  EXPECT_CALL(handler, Call(args...))
      .WillOnce(Return(TEST_SUCCESS));
}

// FAIL is a returning macro so it cannot be used in non-void functions.
void fail(const std::string& message)
{
  FAIL() << message;
}

TestStatus fail_on_callback(...)
{
  fail("unexpected callback");
  return 0;
}

TEST(CallbackRouterTests, IntCallbackHandlerRegistered_HandleCallback_CallsHandler)
{
  MockIntHandler handler;
  const int32_t CALLBACK_VAL = 0x1234;
  auto registration = IntCallbackRouter::register_handler(handler.AsStdFunction());

  EXPECT_CALLBACK(handler, CALLBACK_VAL);
  auto result = IntCallbackRouter::handle_callback(CALLBACK_VAL, registration->token());

  EXPECT_EQ(TEST_SUCCESS, result);
}

TEST(CallbackRouterTests, IntCallbackHandlerRegistered_HandleCallbackMultipleTimes_CallsHandlerMultipleTimes)
{
  MockIntHandler handler;
  auto registration = IntCallbackRouter::register_handler(handler.AsStdFunction());

  const int32_t FIRST_CALLBACK_VAL = 0x1234;
  EXPECT_CALLBACK(handler, FIRST_CALLBACK_VAL);
  auto first_result = IntCallbackRouter::handle_callback(FIRST_CALLBACK_VAL, registration->token());
  const int32_t SECOND_CALLBACK_VAL = 0xABAB;
  EXPECT_CALLBACK(handler, SECOND_CALLBACK_VAL);
  auto second_result = IntCallbackRouter::handle_callback(SECOND_CALLBACK_VAL, registration->token());

  EXPECT_EQ(TEST_SUCCESS, first_result);
  EXPECT_EQ(TEST_SUCCESS, second_result);
}

TEST(CallbackRouterTests, BoolAndStringCallbackHandlerRegistered_HandleCallback_CallsHandler)
{
  MockBoolAndStringHandler handler;
  auto registration = BoolAndStringCallbackRouter::register_handler(handler.AsStdFunction());

  const bool CALLBACK_BOOL = true;
  const std::string CALLBACK_STRING = "HelloCallback";
  EXPECT_CALLBACK(handler, CALLBACK_BOOL, CALLBACK_STRING);
  auto result = BoolAndStringCallbackRouter::handle_callback(CALLBACK_BOOL, CALLBACK_STRING, registration->token());

  EXPECT_EQ(TEST_SUCCESS, result);
}

TEST(CallbackRouterTests, BoolAndStringCallbackHandlerRegistered_HandleCallbackWithBogusAsyncOperationToken_DoesNotCallHandler)
{
  auto registration = BoolAndStringCallbackRouter::register_handler(
      fail_on_callback);

  auto result = BoolAndStringCallbackRouter::handle_callback(false, "MessageToNoOne", BOGUS_TOKEN);

  EXPECT_EQ(TEST_SUCCESS, result);
}

TEST(CallbackRouterTests, MultipleHandlersRegistered_HandleOneCallback_SignalsCorrectHandler)
{
  MockBoolAndStringHandler handler;
  auto first_registration = BoolAndStringCallbackRouter::register_handler(
      fail_on_callback);
  auto second_registration = BoolAndStringCallbackRouter::register_handler(
      handler.AsStdFunction());

  const bool CALLBACK_BOOL = true;
  const std::string CALLBACK_STRING = "HelloSecondHandler";
  EXPECT_CALLBACK(handler, CALLBACK_BOOL, CALLBACK_STRING);
  auto result = BoolAndStringCallbackRouter::handle_callback(CALLBACK_BOOL, CALLBACK_STRING, second_registration->token());

  EXPECT_EQ(TEST_SUCCESS, result);
}

TEST(CallbackRouterTests, MultipleHandlersRegistered_HandleBothCallbacks_SignalsBothHandler)
{
  MockBoolAndStringHandler first_handler;
  MockBoolAndStringHandler second_handler;
  auto first_registration = BoolAndStringCallbackRouter::register_handler(
      first_handler.AsStdFunction());
  auto second_registration = BoolAndStringCallbackRouter::register_handler(
      second_handler.AsStdFunction());

  const bool FIRST_CALLBACK_BOOL = false;
  const std::string FIRST_CALLBACK_STRING = "HelloFirstHandler";
  EXPECT_CALLBACK(first_handler, FIRST_CALLBACK_BOOL, FIRST_CALLBACK_STRING);
  auto first_result = BoolAndStringCallbackRouter::handle_callback(FIRST_CALLBACK_BOOL, FIRST_CALLBACK_STRING, first_registration->token());
  const bool SECOND_CALLBACK_BOOL = true;
  const std::string SECOND_CALLBACK_STRING = "HelloSecondHandler";
  EXPECT_CALLBACK(second_handler, SECOND_CALLBACK_BOOL, SECOND_CALLBACK_STRING);
  auto second_result = BoolAndStringCallbackRouter::handle_callback(SECOND_CALLBACK_BOOL, SECOND_CALLBACK_STRING, second_registration->token());

  EXPECT_EQ(TEST_SUCCESS, first_result);
  EXPECT_EQ(TEST_SUCCESS, second_result);
}

TEST(CallbackRouterTests, CallbackRegisteredAndUnregistered_HandleCallback_DoesNotCallHandler)
{
  CallbackRegistration::Token token;
  {
    auto registration = BoolAndStringCallbackRouter::register_handler(
        fail_on_callback);
    token = registration->token();
  }

  auto result = BoolAndStringCallbackRouter::handle_callback(false, "MessageToNoOne", token);

  EXPECT_EQ(TEST_SUCCESS, result);
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/converters_tests.cpp sha256=711f564497a9c319dc9de8b5111299542c8a8f3de99ed82e86b81663d3fdeb30 bytes=8904 -->
## FILE: source/tests/unit/converters_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/converters_tests.cpp`
- sha256: `711f564497a9c319dc9de8b5111299542c8a8f3de99ed82e86b81663d3fdeb30`
- bytes: 8904

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/converters.h>

#include <array>
#include <nlohmann/json.hpp>

using namespace nidevice_grpc::converters;
using namespace ::testing;
using nlohmann::json;

namespace ni {
namespace tests {
namespace unit {
namespace {
TEST(ConvertersTests, StringWithNoTrailingNulls_TrimTrailingNulls_StringIsTheSame)
{
  const auto INITIAL = std::string("regular_string");
  auto copy = INITIAL;

  trim_trailing_nulls(copy);

  EXPECT_EQ(copy, INITIAL);
}

TEST(ConvertersTests, StringResizedToAddTrailingNulls_TrimTrailingNulls_StringNoLongerHasTrailingNulls)
{
  const auto DATA = std::string("actual_string");
  auto big_string = DATA;
  big_string.resize(100, 0);
  auto copy = big_string;

  trim_trailing_nulls(copy);

  EXPECT_NE(DATA, big_string);
  EXPECT_EQ(DATA, copy);
}

TEST(ConvertersTests, AllEqualSizesAllowOptional_Match)
{
  constexpr auto SIZES = std ::array<int, 3>{3, 3, 3};
  const auto calculation = calculate_linked_array_size(SIZES, true);

  EXPECT_EQ(3, calculation.size);
  EXPECT_EQ(MatchState::MATCH, calculation.match_state);
}

TEST(ConvertersTests, AllEqualSizesDisallowOptional_Match)
{
  constexpr auto SIZES = std ::array<int, 3>{3, 3, 3};
  const auto calculation = calculate_linked_array_size(SIZES, false);

  EXPECT_EQ(3, calculation.size);
  EXPECT_EQ(MatchState::MATCH, calculation.match_state);
}

TEST(ConvertersTests, DifferentSizesAllowOptional_Mismatch)
{
  constexpr auto SIZES = std ::array<int, 5>{4, 3, 0, 3, 3};
  const auto calculation = calculate_linked_array_size(SIZES, true);

  EXPECT_EQ(MatchState::MISMATCH, calculation.match_state);
}

TEST(ConvertersTests, DifferentSizesDisallowOptional_Mismatch)
{
  constexpr auto SIZES = std ::array<int, 5>{3, 3, 4};
  const auto calculation = calculate_linked_array_size(SIZES, false);

  EXPECT_EQ(MatchState::MISMATCH, calculation.match_state);
}

TEST(ConvertersTests, ZeroSizesAllowOptional_MatchOrZero)
{
  constexpr auto SIZES = std ::array<int, 5>{3, 0, 3, 0, 0};
  const auto calculation = calculate_linked_array_size(SIZES, true);

  EXPECT_EQ(MatchState::MATCH_OR_ZERO, calculation.match_state);
}

TEST(ConvertersTests, ZeroSizesDisallowOptional_Mismatch)
{
  constexpr auto SIZES = std ::array<int, 5>{3, 0, 3, 3, 3};
  const auto calculation = calculate_linked_array_size(SIZES, false);

  EXPECT_EQ(MatchState::MISMATCH, calculation.match_state);
}

#if !WIN32
class TempIsoLocale {
 public:
  TempIsoLocale()
  {
    old_locale = strdup(setlocale(LC_ALL, NULL));
    updated_locale = true;
    char* new_locale = setlocale(LC_ALL, "en_US.ISO8859-1");
    if (new_locale == NULL) {
      new_locale = setlocale(LC_ALL, "en_US.ISO8859-15");
      if (new_locale == NULL) {
        updated_locale = false;
      }
    }
  }
  ~TempIsoLocale()
  {
    if (updated_locale) {
      setlocale(LC_ALL, old_locale);
    }
    free(old_locale);
  }
  char* old_locale;
  bool updated_locale;
};
#endif

TEST(ConvertersTests, AsciiString_ConvertFromGrpc_Unchanged)
{
  std::string ascii = "Hello, world";

  std::string result = convert_from_grpc<std::string>(ascii);

  EXPECT_EQ(result, ascii);
}

TEST(ConvertersTests, Utf8String_ConvertFromGrpc_LocalizedString)
{
#if WIN32
  if (GetACP() != 1252) {
    GTEST_SKIP() << "Test requires a Windows-1252 codepage";
  }
#else
  TempIsoLocale temp_locale;
  if (!temp_locale.updated_locale) {
    GTEST_SKIP() << "ISO-8859 locale not installed";
  }
#endif
  std::string utf8 = "\xC3\xAB";  // Latin Small Letter E with Diaeresis
  std::string localized = "\xEB";

  std::string result = convert_from_grpc<std::string>(utf8);

  EXPECT_EQ(result, localized);
}

TEST(ConvertersTests, AsciiString_ConvertToGrpc_Unchanged)
{
  std::string ascii = "Hello, world";

  std::string result;
  convert_to_grpc(ascii, &result);

  EXPECT_EQ(result, ascii);
}

TEST(ConvertersTests, LocalizedString_ConvertToGrpc_Utf8String)
{
#if WIN32
  if (GetACP() != 1252) {
    GTEST_SKIP() << "Test requires a Windows-1252 codepage";
  }
#else
  TempIsoLocale temp_locale;
  if (!temp_locale.updated_locale) {
    GTEST_SKIP() << "ISO-8859 locale not installed";
  }
#endif
  std::string utf8 = "\xC3\xAB";  // Latin Small Letter E with Diaeresis
  std::string localized = "\xEB";

  std::string result;
  convert_to_grpc(localized, &result);

  EXPECT_EQ(result, utf8);
}

TEST(ConvertersTests, NullableVectorInitializedNull_GetData_ReturnsNull)
{
  const auto vec = nullable_vector<int32_t>(nullptr);

  const auto data = vec.data();

  EXPECT_EQ(nullptr, data);
}

TEST(ConvertersTests, NullableVectorInitializedWithData_GetData_ReturnPointerToData)
{
  constexpr auto DATA = std::array<int32_t, 4>{1, 2, 3, 4};
  const auto vec = nullable_vector<int32_t>({DATA.cbegin(), DATA.cend()});

  const auto data = vec.data();

  EXPECT_THAT(std::vector<int32_t>(data, data + DATA.size()), ElementsAreArray(DATA));
}

TEST(ConvertersTests, NullableVectorInitializedWithData_AssignNull_DataIsNull)
{
  auto vec = nullable_vector<int32_t>({1, 2, 3, 4});

  vec = nullptr;

  EXPECT_EQ(nullptr, vec.data());
}

TEST(ConvertersTests, NullableVectorInitializedWithData_ConditionallyAssignNull_DataIsNull)
{
  constexpr auto CONDITION = false;
  auto vec = nullable_vector<int32_t>({1, 2, 3, 4});

  vec = CONDITION ? std::move(vec) : nullptr;

  EXPECT_EQ(nullptr, vec.data());
}

TEST(ConvertersTests, NullableVectorInitializedWithData_ConditionallyAssignMovedSelf_DataIsPointerToData)
{
  constexpr auto CONDITION = true;
  constexpr auto DATA = std::array<int32_t, 4>{1, 2, 3, 4};
  auto vec = nullable_vector<int32_t>({DATA.cbegin(), DATA.cend()});

  vec = CONDITION ? std::move(vec) : nullptr;

  const auto data = vec.data();
  EXPECT_THAT(std::vector<int32_t>(data, data + DATA.size()), ElementsAreArray(DATA));
}

enum TestEnum {
  ONE = 1,
  TWO = 2,
  FOUR = 4
};

TEST(ConvertersTests, EnumArray_ConvertBitfieldAsEnumArrayInput_ReturnsOrOfValues)
{
  const auto input = std::vector<TestEnum>{TestEnum::ONE, TestEnum::FOUR};

  const auto converted = convert_bitfield_as_enum_array_input(input, 0);

  EXPECT_EQ(0x1 | 0x4, converted);
}

TEST(ConvertersTests, RawValue_ConvertBitfieldAsEnumArrayInput_ReturnsRawValue)
{
  constexpr auto INPUT_RAW = 0x7;

  const auto converted = convert_bitfield_as_enum_array_input(std::vector<TestEnum>{}, INPUT_RAW);

  EXPECT_EQ(INPUT_RAW, converted);
}

TEST(ConvertersTests, ArrayAndRawValue_ConvertBitfieldAsEnumArrayInput_ReturnsOrOfValues)
{
  constexpr auto INPUT_RAW = 0x8;
  const auto input_array = std::vector<TestEnum>{TestEnum::TWO, TestEnum::FOUR};

  const auto converted = convert_bitfield_as_enum_array_input(input_array, INPUT_RAW);

  EXPECT_EQ(0x2 | 0x4 | 0x8, converted);
}

TEST(ConvertersTests, SizeWithinRange_ConvertSize_ReturnsCastedValue)
{
  constexpr size_t INPUT = 12;

  auto result = convert_size<int32_t>(INPUT, "test_parameter");

  EXPECT_EQ(12, result);
}

TEST(ConvertersTests, SizeExceedsRange_ConvertSize_ThrowsInvalidArgument)
{
  const auto input = static_cast<size_t>(std::numeric_limits<int32_t>::max()) + 1;

  try {
    (void)convert_size<int32_t>(input, "test_parameter");
    FAIL() << "Expected NonDriverException";
  } catch (nidevice_grpc::NonDriverException& ex) {
    EXPECT_EQ(::grpc::StatusCode::INVALID_ARGUMENT, ex.GetStatus().error_code());
    EXPECT_THAT(ex.GetStatus().error_message(), HasSubstr("test_parameter"));
  }
}

class MockServerContext {
 public:
  MOCK_METHOD2(AddTrailingMetadata, void(const std::string& key, const std::string& value));
};

TEST(ConvertersTests, ApiErrorToStatus_ContextIncludesCodeAndStatusIncludesUnknownMessage)
{
  const auto TEST_STATUS = -12345;
  const auto EXPECTED_MESSAGE = std::string("Unknown");

  MockServerContext serverContext;
  EXPECT_CALL(serverContext, AddTrailingMetadata("ni-error", std::to_string(TEST_STATUS)));
  auto status = nidevice_grpc::ApiErrorToStatus(&serverContext, TEST_STATUS);

  EXPECT_EQ(EXPECTED_MESSAGE, status.error_message());
}

TEST(ConvertersTests, ApiErrorAndDescriptionToStatus_ContextIncludesCodeAndStatusIncludesMessage)
{
  const auto TEST_STATUS = -12345;
  const auto TEST_MESSAGE = std::string("regular_string");
  std::string description(TEST_MESSAGE);

  MockServerContext serverContext;
  EXPECT_CALL(serverContext, AddTrailingMetadata("ni-error", std::to_string(TEST_STATUS)));
  auto status = nidevice_grpc::ApiErrorAndDescriptionToStatus(&serverContext, TEST_STATUS, description);

  EXPECT_EQ(TEST_MESSAGE, status.error_message());
}

}  // namespace
}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/debug_session_properties_tests.cpp sha256=25a2c2bfc624bf10b8c9f7e2d3e92d6c6ae183b873ff819b9adb208caa1104f4 bytes=10585 -->
## FILE: source/tests/unit/debug_session_properties_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/debug_session_properties_tests.cpp`
- sha256: `25a2c2bfc624bf10b8c9f7e2d3e92d6c6ae183b873ff819b9adb208caa1104f4`
- bytes: 10585

````cpp
#include <grpcpp/test/server_context_test_spouse.h>
#include <gtest/gtest.h>
#include <server/debug_session_properties_restricted_service.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>

namespace ni {
namespace tests {
namespace unit {

using ::ni::tests::utilities::CastAndSetArgPointee;
using ::testing::_;
using ::testing::DoAll;
using ::testing::Invoke;
using ::testing::NiceMock;
using ::testing::Return;
using ::testing::Throw;
using ::testing::WithArg;

class DebugSessionPropertiesSysCfgMockLibrary : public NiceMock<ni::tests::utilities::SysCfgMockLibrary> {
 public:
  DebugSessionPropertiesSysCfgMockLibrary()
  {
    expect_debug_enabled_ = false;
    debug_enabled_set_ = false;
    debug_enabled_ = 0;
    expect_out_of_process_ = false;
    out_of_process_set_ = false;
    out_of_process_ = NISysCfgBoolFalse;
  }
  ~DebugSessionPropertiesSysCfgMockLibrary() {}

  NISysCfgStatus SetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      ...)
  {
    NISysCfgStatus status = NISysCfg_InvalidArg;
    va_list args;
    va_start(args, property_ID);
    switch(property_ID) {
      case nidevice_restricted_grpc::kDebugSessionEnabledPropertyId: {
        if (expect_debug_enabled_)
        {
          debug_enabled_set_ = true;
          debug_enabled_ = va_arg(args, unsigned int);
          status = NISysCfg_OK;
        }
        break;
      }
      case nidevice_restricted_grpc::kDebugSessionServerOutOfProcessPropertyId: {
        if (expect_out_of_process_)
        {
          out_of_process_set_ = true;
          out_of_process_ = (NISysCfgBool)va_arg(args, int);
          status = NISysCfg_OK;
        }
        break;
      }
      default:
        break;
    }
    va_end(args);

    return status;
  }

  void set_expect_debug_enabled() { expect_debug_enabled_ = true; }
  bool debug_enabled_set() const { return debug_enabled_set_; }
  unsigned int debug_enabled() const { return debug_enabled_; }
  void set_expect_out_of_process() { expect_out_of_process_ = true; }
  bool out_of_process_set() const { return out_of_process_set_; }
  NISysCfgBool out_of_process() const { return out_of_process_; }

 private:
  bool expect_debug_enabled_;
  bool debug_enabled_set_;
  unsigned int debug_enabled_;
  bool expect_out_of_process_;
  bool out_of_process_set_;
  NISysCfgBool out_of_process_;
};

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionSupported_ResponseIsWritten)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionSupportedRequest request;
  nidevice_restricted_grpc::IsDebugSessionSupportedResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, nidevice_restricted_grpc::kDebugSessionSupportedPropertyId, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(NISysCfgBoolTrue), Return(NISysCfg_OK)));

  ::grpc::Status status = service.IsDebugSessionSupported(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.supported());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionEnabled_ResponseIsWritten)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionEnabledRequest request;
  nidevice_restricted_grpc::IsDebugSessionEnabledResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, nidevice_restricted_grpc::kDebugSessionEnabledPropertyId, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>((unsigned int)1), Return(NISysCfg_OK)));

  ::grpc::Status status = service.IsDebugSessionEnabled(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.enabled());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionServerOutOfProcess_ResponseIsWritten)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionServerOutOfProcessRequest request;
  nidevice_restricted_grpc::IsDebugSessionServerOutOfProcessResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, nidevice_restricted_grpc::kDebugSessionServerOutOfProcessPropertyId, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(NISysCfgBoolTrue), Return(NISysCfg_OK)));

  ::grpc::Status status = service.IsDebugSessionServerOutOfProcess(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(response.out_of_process());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_SetDebugSessionEnabled_EnabledIsSet)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  mock_library.set_expect_debug_enabled();
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::SetDebugSessionEnabledRequest request;
  request.set_enabled(true);
  nidevice_restricted_grpc::SetDebugSessionEnabledResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = service.SetDebugSessionEnabled(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(mock_library.debug_enabled_set());
  EXPECT_EQ(1, mock_library.debug_enabled());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_SetDebugSessionServerOutOfProcess_OutOfProcessIsSet)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  mock_library.set_expect_out_of_process();
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::SetDebugSessionServerOutOfProcessRequest request;
  request.set_out_of_process(true);
  nidevice_restricted_grpc::SetDebugSessionServerOutOfProcessResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = service.SetDebugSessionServerOutOfProcess(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(mock_library.out_of_process_set());
  EXPECT_EQ(NISysCfgBoolTrue, mock_library.out_of_process());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionSupported_SaveNotCalled)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionSupportedRequest request;
  nidevice_restricted_grpc::IsDebugSessionSupportedResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .Times(0);

  ::grpc::Status status = service.IsDebugSessionSupported(&context, &request, &response);

  EXPECT_TRUE(status.ok());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionEnabled_SaveNotCalled)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionEnabledRequest request;
  nidevice_restricted_grpc::IsDebugSessionEnabledResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .Times(0);

  ::grpc::Status status = service.IsDebugSessionEnabled(&context, &request, &response);

  EXPECT_TRUE(status.ok());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_QueryDebugSessionServerOutOfProcess_SaveNotCalled)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::IsDebugSessionServerOutOfProcessRequest request;
  nidevice_restricted_grpc::IsDebugSessionServerOutOfProcessResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .Times(0);

  ::grpc::Status status = service.IsDebugSessionServerOutOfProcess(&context, &request, &response);

  EXPECT_TRUE(status.ok());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_SetDebugSessionEnabled_SaveIsCalled)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  mock_library.set_expect_debug_enabled();
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::SetDebugSessionEnabledRequest request;
  nidevice_restricted_grpc::SetDebugSessionEnabledResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = service.SetDebugSessionEnabled(&context, &request, &response);

  EXPECT_TRUE(status.ok());
}

TEST(DebugSessionPropertiesTests, DeviceIsPresent_SetDebugSessionServerOutOfProcess_SaveIsCalled)
{
  DebugSessionPropertiesSysCfgMockLibrary mock_library;
  mock_library.set_expect_out_of_process();
  nidevice_restricted_grpc::DebugSessionPropertiesRestrictedService service(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::SetDebugSessionServerOutOfProcessRequest request;
  nidevice_restricted_grpc::SetDebugSessionServerOutOfProcessResponse response;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = service.SetDebugSessionServerOutOfProcess(&context, &request, &response);

  EXPECT_TRUE(status.ok());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/device_enumerator_tests.cpp sha256=a626a34289fa6a89e25fc4324b4d64a34090f80c288544c00a206023580aa90a bytes=22525 -->
## FILE: source/tests/unit/device_enumerator_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/device_enumerator_tests.cpp`
- sha256: `a626a34289fa6a89e25fc4324b4d64a34090f80c288544c00a206023580aa90a`
- bytes: 22525

````cpp
#include <gtest/gtest.h>
#include <server/device_enumerator.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>
#include <tests/utilities/syscfg_test_helpers.h>

namespace ni {
namespace tests {
namespace unit {

using ::testing::_;
using ::testing::Invoke;
using ::testing::NiceMock;
using ::testing::Return;
using ::testing::Throw;
using ::testing::WithArg;

static const char* kScopeName = "MyScope";
static const char* kModel = "NI PXIe-5122";
static const char* kVendor = "NI";
static const char* kSerialNumber = "37ED39FC0D17";
static const uint32_t kProductId = 0x42;

TEST(DeviceEnumeratorTests, SysCfgApiNotInstalled_EnumerateDevices_ReturnsNotFoundGrpcStatusCode)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST(DeviceEnumeratorTests, SysCfgApiNotInstalled_EnumerateDevices_ListOfDevicesIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(0, devices.size());
}

TEST(DeviceEnumeratorTests, InitializeSessionReturnsError_EnumerateDevices_ReturnsInternalGrpcStatusCode)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Return(NISysCfg_InvalidLoginCredentials));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::INTERNAL, status.error_code());
  EXPECT_EQ(nidevice_grpc::kDeviceEnumerationFailedMessage, status.error_message());
}

TEST(DeviceEnumeratorTests, InitializeSessionReturnsError_EnumerateDevices_ListOfDevicesIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Return(NISysCfg_InvalidLoginCredentials));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(0, devices.size());
}

TEST(DeviceEnumeratorTests, InitializeSessionSucceeds_EnumerateDevices_CallsInitializeButNotClose)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(WithArg<7>(Invoke(SetSessionHandleToOne)));
  EXPECT_CALL(mock_library, CloseHandle(_))
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .Times(0);

  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
}

TEST(DeviceEnumeratorTests, CreateFilterReturnsError_EnumerateDevices_ListOfDevicesIsEmptyAndReturnsInternalError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, CreateFilter)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, FindHardware)
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::INTERNAL, status.error_code());
  EXPECT_EQ(nidevice_grpc::kDeviceEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, devices.size());
}

static NISysCfgStatus SetFilterHandleToOne(NISysCfgFilterHandle* filter_handle)
{
  *filter_handle = (NISysCfgFilterHandle)1;
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, CreateFilterSetsFilterHandle_EnumerateDevices_FilterHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, CreateFilter)
      .WillOnce(WithArg<1>(Invoke(SetFilterHandleToOne)));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
}

TEST(DeviceEnumeratorTests, FindHardwareReturnsError_EnumerateDevices_ListOfDevicesIsEmptyAndReturnsInternalError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, NextResource)
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::INTERNAL, status.error_code());
  EXPECT_EQ(nidevice_grpc::kDeviceEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, devices.size());
}

static NISysCfgStatus SetResourceEnumHandleToOne(NISysCfgEnumResourceHandle* resource_enum_handle)
{
  *resource_enum_handle = (NISysCfgEnumResourceHandle)1;
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, FindHardwareSetsResourceEnumHandle_EnumerateDevices_ResourceEnumHandleIsPassedToNextResource)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(WithArg<4>(Invoke(SetResourceEnumHandleToOne)));
  EXPECT_CALL(mock_library, NextResource(_, (void*)1, _))
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
}

TEST(DeviceEnumeratorTests, FindHardwareSetsResourceEnumHandle_EnumerateDevices_ResourceEnumHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(WithArg<4>(Invoke(SetResourceEnumHandleToOne)));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
}

TEST(DeviceEnumeratorTests, NextResourceReturnsError_EnumerateDevices_ListOfDevicesIsEmptyAndReturnsInternalError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty)
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::INTERNAL, status.error_code());
  EXPECT_EQ(nidevice_grpc::kDeviceEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, devices.size());
}

static NISysCfgStatus SetResourceHandleToOne(NISysCfgResourceHandle* resource_handle)
{
  *resource_handle = (NISysCfgResourceHandle)1;
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, NextResourceSetsResourceHandle_EnumerateDevices_ResourceHandleIsPassedToGetPropertyApis)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(WithArg<2>(Invoke(SetResourceHandleToOne)))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty((void*)1, _, _, _))
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty((void*)1, _, _))
      .WillRepeatedly(Return(NISysCfg_OK));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
}

TEST(DeviceEnumeratorTests, NextResourceSetsResourceHandle_EnumerateDevices_ResourceHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(WithArg<2>(Invoke(SetResourceHandleToOne)))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
}

TEST(DeviceEnumeratorTests, SysCfgApiInstalledAndNoDevicesPresent_EnumerateDevices_ListOfDevicesIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_EQ(0, devices.size());
}

static NISysCfgStatus SetIsNIProductToTrue(void* value)
{
  NISysCfgBool* is_ni_product = (NISysCfgBool*)value;
  *is_ni_product = NISysCfgBoolTrue;
  return NISysCfg_OK;
}

static NISysCfgStatus SetIsNIProductToFalse(void* value)
{
  NISysCfgBool* is_ni_product = (NISysCfgBool*)value;
  *is_ni_product = NISysCfgBoolFalse;
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, LocalHostContainsNonNiDevices_EnumerateDevices_ListOfDevicesContainsOnlyNiDevices)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToFalse)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_EQ(1, devices.size());
}

static NISysCfgStatus SetExpertNameToNetwork(void* value)
{
  char* expert_name = (char*)value;
  strcpy(expert_name, nidevice_grpc::kNetworkExpertName);
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, LocalHostContainsNetworkDevice_EnumerateDevices_ListOfDevicesReturnedDoesNotContainNetworkDevices)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty)
      .WillOnce(WithArg<3>(Invoke(SetExpertNameToNetwork)));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyExpertUserAlias, _, _))
      .Times(0);

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_EQ(0, devices.size());
}

TEST(DeviceEnumeratorTests, GetResourcePropertyApisReturnError_EnumerateDevices_DevicePropertiesAreSetToEmptyString)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty)
      .WillRepeatedly(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_PropDoesNotExist));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ("", devices.Get(0).name());
  EXPECT_EQ("", devices.Get(0).model());
  EXPECT_EQ("", devices.Get(0).serial_number());
}

TEST(DeviceEnumeratorTests, NISysCfgLibraryIsLoaded_GetSysCfgSession_CallsInitializeSessionOnceAndReturnsOK)
{
  ni::tests::utilities::SysCfgMockLibrary mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(WithArg<7>(Invoke(SetSessionHandleToOne)));
  NISysCfgSessionHandle session1 = nullptr;
  NISysCfgStatus status = device_enumerator.open_or_get_localhost_syscfg_session(&session1);

  NISysCfgSessionHandle session2 = nullptr;
  status = device_enumerator.open_or_get_localhost_syscfg_session(&session2);

  EXPECT_EQ(session1, session2);
  EXPECT_EQ(NISysCfg_OK, status);
}

TEST(DeviceEnumeratorTests, NISysCfgLibraryIsLoaded_ClearSysCfgSession_CalledCloseHandleOnce)
{
  ni::tests::utilities::SysCfgMockLibrary mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillRepeatedly(WithArg<7>(Invoke(SetSessionHandleToOne)));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(1);
  NISysCfgSessionHandle session = nullptr;
  NISysCfgStatus status = device_enumerator.open_or_get_localhost_syscfg_session(&session);

  device_enumerator.clear_syscfg_session();
  device_enumerator.clear_syscfg_session();

  status = device_enumerator.open_or_get_localhost_syscfg_session(&session);
}

static NISysCfgStatus SetAliasName(void* value)
{
  char* name = (char*)value;
  strcpy(name, kScopeName);
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, GetResourceIndexedPropertySetsName_EnumerateDevices_ResponseContainsThatName)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty(_, NISysCfgIndexedPropertyExpertUserAlias, _, _))
      .WillOnce(WithArg<3>(Invoke(SetAliasName)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ(kScopeName, devices.Get(0).name());
}

static NISysCfgStatus SetModelName(void* value)
{
  char* model = (char*)value;
  strcpy(model, kModel);
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, GetResourcePropertySetsModelName_EnumerateDevices_ResponseContainsThatModelName)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyProductName, _))
      .WillOnce(WithArg<2>(Invoke(SetModelName)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ(kModel, devices.Get(0).model());
}

static NISysCfgStatus SetVendorName(void* value)
{
  char* vendor = (char*)value;
  strcpy(vendor, kVendor);
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, GetResourcePropertySetsVendorName_EnumerateDevices_ResponseContainsThatVendorName)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyVendorName, _))
      .WillOnce(WithArg<2>(Invoke(SetVendorName)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ(kVendor, devices.Get(0).vendor());
}

static NISysCfgStatus SetSerialNumber(void* value)
{
  char* serial_number = (char*)value;
  strcpy(serial_number, kSerialNumber);
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, GetResourcePropertySetsSerialNumber_EnumerateDevices_ResponseContainsThatSerialNumber)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertySerialNumber, _))
      .WillOnce(WithArg<2>(Invoke(SetSerialNumber)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ(kSerialNumber, devices.Get(0).serial_number());
}

static NISysCfgStatus SetProductId(void* value)
{
  uint32_t* product_id = (uint32_t*)value;
  *product_id = kProductId;
  return NISysCfg_OK;
}

TEST(DeviceEnumeratorTests, GetResourcePropertySetsProductId_EnumerateDevices_ResponseContainsThatProductId)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&mock_library);
  google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK))
      .WillOnce(Return(NISysCfg_EndOfEnum));
  EXPECT_CALL(mock_library, GetResourceProperty)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyIsNIProduct, _))
      .WillOnce(WithArg<2>(Invoke(SetIsNIProductToTrue)));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyProductId, _))
      .WillOnce(WithArg<2>(Invoke(SetProductId)));

  ::grpc::Status status = device_enumerator.enumerate_devices(&devices);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, devices.size());
  EXPECT_EQ(kProductId, devices.Get(0).product_id());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/library_set_runtime_environment_tests.cpp sha256=1e0ff1324d290275ec293512ded0fd283302a5e9fa124a68d1d4ede756cba333 bytes=2152 -->
## FILE: source/tests/unit/library_set_runtime_environment_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/library_set_runtime_environment_tests.cpp`
- sha256: `1e0ff1324d290275ec293512ded0fd283302a5e9fa124a68d1d4ede756cba333`
- bytes: 2152

````cpp
#include <gtest/gtest.h>
// Use NI-SWITCH instead of NI-FAKE because nifake.h is missing a bunch of functions specified in metadata
// and they're difficult to properly add in source.
#include <niswitch/niswitch_library.h>

#include "mock_shared_library.h"
#include "version.h"

namespace ni {
namespace tests {
namespace unit {

using ::testing::_;
using ::testing::Return;

void FunctionToPointAt() {}

TEST(LibrarySetRuntimeEnvironmentTests, Library_SetRuntimeEnvironmentFound_CallsSetRuntimeEnvironment)
{
  auto p_shared_library = std::make_shared<MockSharedLibrary>();
  EXPECT_CALL(*p_shared_library, set_library_name(_));
  EXPECT_CALL(*p_shared_library, load());
  EXPECT_CALL(*p_shared_library, is_loaded())
      .WillOnce(Return(true));  // the constructor will bail out early if false

  const char* func_name = "niSwitch_SetRuntimeEnvironment";

  EXPECT_CALL(*p_shared_library, get_function_pointer(_))
      .WillRepeatedly(Return(nullptr));
  // We must return an address for SetRuntimeEnvironment or we won't call it.
  EXPECT_CALL(*p_shared_library, get_function_pointer(::testing::StrEq(func_name)))
      .WillOnce(Return(const_cast<const void*>(reinterpret_cast<void*>(&FunctionToPointAt))));

  auto library = std::make_shared<niswitch_grpc::NiSwitchLibrary>(p_shared_library);
  EXPECT_TRUE(library->is_runtime_environment_set());
}

TEST(LibrarySetRuntimeEnvironmentTests, Library_SetRuntimeEnvironmentNotFound_DoesNotCallSetRuntimeEnvironment)
{
  auto p_shared_library = std::make_shared<MockSharedLibrary>();
  EXPECT_CALL(*p_shared_library, set_library_name(_));
  EXPECT_CALL(*p_shared_library, load());
  EXPECT_CALL(*p_shared_library, is_loaded())
      .WillOnce(Return(true));  // the constructor will bail out early if false
  EXPECT_CALL(*p_shared_library, get_function_pointer(_))
      .WillRepeatedly(Return(nullptr));  // means a function wasn't found

  auto library = std::make_shared<niswitch_grpc::NiSwitchLibrary>(p_shared_library);
  EXPECT_FALSE(library->is_runtime_environment_set());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/ni_fake_non_ivi_service_tests.cpp sha256=4230843744cb8c5d1de7a90ee84ab4c1f71a9969d188a77c182cfc9d39ff4c0d bytes=69721 -->
## FILE: source/tests/unit/ni_fake_non_ivi_service_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/ni_fake_non_ivi_service_tests.cpp`
- sha256: `4230843744cb8c5d1de7a90ee84ab4c1f71a9969d188a77c182cfc9d39ff4c0d`
- bytes: 69721

````cpp
#include <google/protobuf/util/time_util.h>
#include <grpcpp/impl/grpc_library.h>
#include <gtest/gtest.h>
#include <nifake_non_ivi/nifake_non_ivi_mock_library.h>
#include <nifake_non_ivi/nifake_non_ivi_service.h>
#include <server/feature_toggles.h>
#include <server/session_resource_repository.h>

#include <iostream>
#include <numeric>
#include <string>

using namespace nifake_non_ivi_grpc;
using namespace ::testing;

bool operator==(const StructWithCoercion_struct& left, const StructWithCoercion& right)
{
  return left.first == right.first() && left.second == right.second() && left.third == right.third();
}
bool operator==(const StructWithCoercion_struct& left, const StructWithCoercion_struct& right)
{
  return left.first == right.first && left.second == right.second && left.third == right.third;
}

namespace ni {
namespace tests {
namespace unit {

MATCHER(CustomU16Data, "")
{
  myUInt16 const* write_data_array = std::get<0>(arg);
  return write_data_array[0] == 0 && write_data_array[1] == UINT16_MAX && write_data_array[2] == 16;
}

MATCHER(CustomI16Data, "")
{
  myInt16 const* write_data_array = std::get<1>(arg);
  return write_data_array[0] == 0 && write_data_array[1] == INT16_MAX && write_data_array[2] == INT16_MIN;
}

MATCHER(CustomI8Data, "")
{
  myInt8 const* write_data_array = std::get<2>(arg);
  return write_data_array[0] == 0 && write_data_array[1] == INT8_MAX && write_data_array[2] == INT8_MIN;
}

MATCHER(CustomU8Data, "")
{
  myUInt8 const* write_data_array = std::get<0>(arg);
  return write_data_array[0] == 0 && write_data_array[1] == UINT8_MAX && write_data_array[2] == 16;
}

void SetU16Data(Unused, myUInt16* u16_data, Unused, Unused, Unused, Unused)
{
  u16_data[0] = 0;
  u16_data[1] = UINT16_MAX;
  u16_data[2] = 16;
};

void SetI16Data(Unused, Unused, Unused, myInt16* i16_data, Unused, Unused)
{
  i16_data[0] = 0;
  i16_data[1] = INT16_MAX;
  i16_data[2] = INT16_MIN;
};

void SetI8Data(Unused, Unused, Unused, Unused, Unused, myInt8* i8_data)
{
  i8_data[0] = 0;
  i8_data[1] = INT8_MAX;
  i8_data[2] = INT8_MIN;
};

void SetU8Data(Unused, myUInt8* u8_data)
{
  u8_data[0] = 0;
  u8_data[1] = UINT8_MAX;
  u8_data[2] = 16;
}

void SetArraysByPtrData(int32* int32_data, myUInt16* u16_data, int32* size)
{
  int32_data[0] = -1;
  int32_data[1] = 1;
  int32_data[2] = 128;
  u16_data[0] = 0;
  u16_data[1] = UINT16_MAX;
  u16_data[2] = 16;
  *size = 3;
}

void SetSingleStructWithCoercionData(StructWithCoercion_struct* data, int index)
{
  switch (index) {
    case 0:
      data->first = 0;
      data->second = 0;
      data->third = 0;
      break;
    case 1:
      data->first = INT16_MAX;
      data->second = UINT16_MAX;
      data->third = INT8_MAX;
      break;
    case 2:
      data->first = INT16_MIN;
      data->second = 16;
      data->third = INT8_MIN;
      break;
    default:
      EXPECT_TRUE(false);
  }
}

void SetSingleStructWithCoercionData(StructWithCoercion* data, int index)
{
  switch (index) {
    case 0:
      data->set_first(0);
      data->set_second(0);
      data->set_third(0);
      break;
    case 1:
      data->set_first(INT16_MAX);
      data->set_second(UINT16_MAX);
      data->set_third(INT8_MAX);
      break;
    case 2:
      data->set_first(INT16_MIN);
      data->set_second(16);
      data->set_third(INT8_MIN);
      break;
    default:
      EXPECT_TRUE(false);
  }
}

void SetStructWithCoercionData(Unused, StructWithCoercion_struct* data)
{
  SetSingleStructWithCoercionData(&data[0], 0);
  SetSingleStructWithCoercionData(&data[1], 1);
  SetSingleStructWithCoercionData(&data[2], 2);
}

MATCHER(CustomStructWithCoercionData, "")
{
  StructWithCoercion_struct const* data_array = std::get<0>(arg);
  StructWithCoercion_struct expected_data[3];
  SetSingleStructWithCoercionData(&expected_data[0], 0);
  SetSingleStructWithCoercionData(&expected_data[1], 1);
  SetSingleStructWithCoercionData(&expected_data[2], 2);

  return expected_data[0] == data_array[0] && expected_data[1] == data_array[1] && expected_data[2] == data_array[2];
}

MATCHER_P(CVIAbsoluteTimeEq, lhs, "")
{
  return lhs.cviTime.msb == arg.cviTime.msb &&
      lhs.cviTime.lsb == arg.cviTime.lsb;
}

class NiFakeNonIviServiceTests : public ::testing::Test {
 public:
  using FakeResourceRepository = nidevice_grpc::SessionResourceRepository<FakeHandle>;
  using SecondaryResourceRepository = nidevice_grpc::SessionResourceRepository<SecondarySessionHandle>;
  using FakeCrossDriverResourceRepository = nidevice_grpc::SessionResourceRepository<FakeCrossDriverHandle>;
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::shared_ptr<nidevice_grpc::SessionRepository> secondary_session_repository_;
  std::shared_ptr<FakeCrossDriverResourceRepository> cross_driver_resource_repository_;
  std::shared_ptr<FakeResourceRepository> resource_repository_;
  std::shared_ptr<SecondaryResourceRepository> secondary_resource_repository_;
  std::shared_ptr<NiFakeNonIviMockLibrary> library_;
  NiFakeNonIviService service_;

  NiFakeNonIviServiceTests(const nidevice_grpc::FeatureToggles& feature_toggles = {})
      : session_repository_(std::make_shared<nidevice_grpc::SessionRepository>()),
        secondary_session_repository_(std::make_shared<nidevice_grpc::SessionRepository>()),
        cross_driver_resource_repository_(std::make_shared<FakeCrossDriverResourceRepository>(session_repository_)),
        resource_repository_(std::make_shared<FakeResourceRepository>(session_repository_)),
        secondary_resource_repository_(std::make_shared<SecondaryResourceRepository>(secondary_session_repository_)),
        library_(std::make_shared<NiFakeNonIviMockLibrary>()),
        service_(
            library_,
            resource_repository_,
            secondary_resource_repository_,
            cross_driver_resource_repository_,
            feature_toggles)
  {
  }

  virtual ~NiFakeNonIviServiceTests() {}

  std::string init(const std::string& session_name, FakeHandle handle)
  {
    EXPECT_CALL(*library_, Init(StrEq(session_name.c_str()), _))
        .WillOnce(DoAll(SetArgPointee<1>(handle), Return(kDriverSuccess)));

    ::grpc::ServerContext context;
    InitRequest request;
    request.set_session_name(session_name);
    InitResponse response;

    service_.Init(&context, &request, &response);

    return response.handle().name();
  }

  std::string init_secondary_session(const std::string& session_name, SecondarySessionHandle handle)
  {
    EXPECT_CALL(*library_, InitSecondarySession(_))
        .WillOnce(DoAll(SetArgPointee<0>(handle), Return(kDriverSuccess)));

    ::grpc::ServerContext context;
    InitSecondarySessionRequest request;
    request.set_session_name(session_name.c_str());
    InitSecondarySessionResponse response;

    service_.InitSecondarySession(&context, &request, &response);

    return response.secondary_session_handle().name();
  }

  std::string init_with_handle_name_as_session_name(const std::string& handle_name, FakeHandle handle)
  {
    EXPECT_CALL(*library_, InitWithHandleNameAsSessionName(StrEq(handle_name.c_str()), _))
        .WillOnce(DoAll(SetArgPointee<1>(handle), Return(kDriverSuccess)));

    ::grpc::ServerContext context;
    InitWithHandleNameAsSessionNameRequest request;
    request.set_handle_name(handle_name.c_str());
    InitWithHandleNameAsSessionNameResponse response;

    service_.InitWithHandleNameAsSessionName(&context, &request, &response);

    return response.handle().name();
  }

  int32 close_secondary_session_with_expected_handle(std::string session_name, SecondarySessionHandle expected_closed_handle)
  {
    EXPECT_CALL(*library_, CloseSecondarySession(expected_closed_handle))
        .WillOnce(Return(kDriverSuccess));
    ::grpc::ServerContext context;
    CloseSecondarySessionRequest request;
    request.mutable_secondary_session_handle()->set_name(session_name);
    CloseSecondarySessionResponse response;
    service_.CloseSecondarySession(&context, &request, &response);

    return response.status();
  }

  int32 close_with_expected_handle(std::string session_name, FakeHandle expected_closed_handle)
  {
    EXPECT_CALL(*library_, Close(expected_closed_handle))
        .WillOnce(Return(kDriverSuccess));
    ::grpc::ServerContext context;
    CloseRequest request;
    request.mutable_handle()->set_name(session_name);
    CloseResponse response;
    service_.Close(&context, &request, &response);

    return response.status();
  }

  void setup_iota_with_custom_size()
  {
    auto set_iota_data = [](int32 size_one, int32 size_two, int32* data) {
      auto out_size = (size_one == -1) ? size_two : size_one + 1;
      std::iota(data, data + out_size, 0);
    };

    EXPECT_CALL(*library_, IotaWithCustomSize(_, _, _))
        .WillOnce(DoAll(
            Invoke(set_iota_data),
            Return(kDriverSuccess)));
  }

  static void EXPECT_IOTA_OF_SIZE(IotaWithCustomSizeResponse response, size_t size)
  {
    std::vector<int32> expected(size);
    std::iota(expected.begin(), expected.end(), 0);
    std::vector<int32> actual{response.data().cbegin(), response.data().cend()};
    EXPECT_THAT(actual, ContainerEq(expected));
  }
};

TEST_F(NiFakeNonIviServiceTests, InitSecondarySession_AddsSessionHandleToSecondaryRepository)
{
  const SecondarySessionHandle kHandle = 1234UL;
  auto session = init_secondary_session("test", kHandle);

  EXPECT_NE("", session);
  EXPECT_EQ(kHandle, secondary_resource_repository_->access_session(session));
}

TEST_F(NiFakeNonIviServiceTests, InitSecondarySession_CloseSecondarySession_ClosesSecondarySession)
{
  const SecondarySessionHandle kHandle = 1234UL;
  auto session = init_secondary_session("test", kHandle);

  EXPECT_NE("", session);
  EXPECT_EQ(kDriverSuccess, close_secondary_session_with_expected_handle(session, kHandle));
}

TEST_F(NiFakeNonIviServiceTests, InitSession_CloseSession_ClosesHandleAndSucceeds)
{
  const FakeHandle kHandle = 1234UL;
  auto session = init("test", kHandle);
  EXPECT_NE("", session);

  auto status = close_with_expected_handle(session, kHandle);

  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InitWithHandleNameAsSessionName_CloseSession_ClosesHandleAndSucceeds)
{
  const FakeHandle kHandle = 99999UL;
  auto session = init_with_handle_name_as_session_name("test", kHandle);
  EXPECT_NE("", session);

  auto status = close_with_expected_handle(session, kHandle);

  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_U16DataGetsCoerced)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .With(CustomU16Data())
      .Times(1);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_u16_array(0);
  request.add_u16_array(UINT16_MAX);
  request.add_u16_array(16);
  InputArraysWithNarrowIntegerTypesResponse response;

  service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_U16DataOutOfRange_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_u16_array(UINT16_MAX + 1);
  InputArraysWithNarrowIntegerTypesResponse response;

  auto status = service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(UINT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I16DataGetsCoerced)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .With(CustomI16Data())
      .Times(1);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i16_array(0);
  request.add_i16_array(INT16_MAX);
  request.add_i16_array(INT16_MIN);
  InputArraysWithNarrowIntegerTypesResponse response;

  service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I16DataOutOfRangeTooHigh_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);

  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i16_array(INT16_MAX + 1);
  InputArraysWithNarrowIntegerTypesResponse response;

  auto status = service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);
  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I16DataOutOfRangeTooLow_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);

  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i16_array(INT16_MIN - 1);
  InputArraysWithNarrowIntegerTypesResponse response;

  auto status = service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);
  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT16_MIN - 1)));
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I8DataGetsCoerced)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .With(CustomI8Data())
      .Times(1);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i8_array(0);
  request.add_i8_array(INT8_MAX);
  request.add_i8_array(INT8_MIN);
  InputArraysWithNarrowIntegerTypesResponse response;

  service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I8DataOutOfRangeTooHigh_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i8_array(INT8_MAX + 1);
  InputArraysWithNarrowIntegerTypesResponse response;

  auto status = service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT8_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, InputArraysWithNarrowIntegerTypes_I8DataOutOfRangeTooLow_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  InputArraysWithNarrowIntegerTypesRequest request;
  request.add_i8_array(INT8_MIN - 1);
  InputArraysWithNarrowIntegerTypesResponse response;

  auto status = service_.InputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT8_MIN - 1)));
}

TEST_F(NiFakeNonIviServiceTests, ScalarsWithNarrowIntegerTypes_I8DataOutOfRangeTooLow_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  ScalarsWithNarrowIntegerTypesRequest request;
  request.set_i8(INT8_MIN - 1);
  ScalarsWithNarrowIntegerTypesResponse response;
  auto status = service_.ScalarsWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT8_MIN - 1)));
}

TEST_F(NiFakeNonIviServiceTests, ScalarsWithNarrowIntegerTypes_I16DataOutOfRangeTooHigh_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  ScalarsWithNarrowIntegerTypesRequest request;
  request.set_i16(INT16_MAX + 1);
  ScalarsWithNarrowIntegerTypesResponse response;
  auto status = service_.ScalarsWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, ScalarsWithNarrowIntegerTypes_U16DataOutOfRangeTooHigh_ReturnsError)
{
  EXPECT_CALL(*library_, InputArraysWithNarrowIntegerTypes(_, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  ScalarsWithNarrowIntegerTypesRequest request;
  request.set_u16(UINT16_MAX + 1);
  ScalarsWithNarrowIntegerTypesResponse response;
  auto status = service_.ScalarsWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(UINT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, ScalarsWithNarrowIntegerTypes_AllFieldsInRange_PassesThroughData)
{
  constexpr myUInt16 u16_val = UINT16_MAX;
  constexpr myInt16 i16_val = INT16_MAX;
  constexpr myInt8 i8_val = INT8_MAX;
  EXPECT_CALL(*library_, ScalarsWithNarrowIntegerTypes(u16_val, i16_val, i8_val))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  ScalarsWithNarrowIntegerTypesRequest request;
  request.set_u16(u16_val);
  request.set_i16(i16_val);
  request.set_i8(i8_val);
  ScalarsWithNarrowIntegerTypesResponse response;
  auto status = service_.ScalarsWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithNarrowIntegerTypes_U16)
{
  ::grpc::ServerContext context;
  OutputArraysWithNarrowIntegerTypesRequest request;
  request.set_number_of_u16_samples(3);
  OutputArraysWithNarrowIntegerTypesResponse response;
  EXPECT_CALL(*library_, OutputArraysWithNarrowIntegerTypes(_, _, _, _, _, _))
      .WillOnce(DoAll(
          Invoke(SetU16Data),
          Return(kDriverSuccess)));

  service_.OutputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(3, response.u16_data_size());
  EXPECT_EQ(0, response.u16_data().Get(0));
  EXPECT_EQ(UINT16_MAX, response.u16_data().Get(1));
  EXPECT_EQ(16, response.u16_data().Get(2));
  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithNarrowIntegerTypes_I16)
{
  ::grpc::ServerContext context;
  OutputArraysWithNarrowIntegerTypesRequest request;
  request.set_number_of_i16_samples(3);
  OutputArraysWithNarrowIntegerTypesResponse response;
  EXPECT_CALL(*library_, OutputArraysWithNarrowIntegerTypes(_, _, _, _, _, _))
      .WillOnce(DoAll(
          Invoke(SetI16Data),
          Return(kDriverSuccess)));

  service_.OutputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(3, response.i16_data_size());
  EXPECT_EQ(0, response.i16_data().Get(0));
  EXPECT_EQ(INT16_MAX, response.i16_data().Get(1));
  EXPECT_EQ(INT16_MIN, response.i16_data().Get(2));
  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithNarrowIntegerTypes_I8)
{
  ::grpc::ServerContext context;
  OutputArraysWithNarrowIntegerTypesRequest request;
  request.set_number_of_i8_samples(3);
  OutputArraysWithNarrowIntegerTypesResponse response;
  EXPECT_CALL(*library_, OutputArraysWithNarrowIntegerTypes(_, _, _, _, _, _))
      .WillOnce(DoAll(
          Invoke(SetI8Data),
          Return(kDriverSuccess)));

  service_.OutputArraysWithNarrowIntegerTypes(&context, &request, &response);

  EXPECT_EQ(3, response.i8_data_size());
  EXPECT_EQ(0, response.i8_data().Get(0));
  EXPECT_EQ(INT8_MAX, response.i8_data().Get(1));
  EXPECT_EQ(INT8_MIN, response.i8_data().Get(2));
  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, InputArrayOfBytes)
{
  EXPECT_CALL(*library_, InputArrayOfBytes(_))
      .With(CustomU8Data())
      .Times(1);
  ::grpc::ServerContext context;
  InputArrayOfBytesRequest request;
  request.mutable_u8_array()->push_back(0);
  request.mutable_u8_array()->push_back(UINT8_MAX);
  request.mutable_u8_array()->push_back(16);
  InputArrayOfBytesResponse response;

  service_.InputArrayOfBytes(&context, &request, &response);

  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, OutputArrayOfBytes)
{
  EXPECT_CALL(*library_, OutputArrayOfBytes(_, _))
      .WillOnce(DoAll(
          Invoke(SetU8Data),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputArrayOfBytesRequest request;
  request.set_number_of_u8_samples(3);
  OutputArrayOfBytesResponse response;

  service_.OutputArrayOfBytes(&context, &request, &response);

  EXPECT_EQ(3, response.u8_data().size());
  EXPECT_EQ(0, (myUInt8)response.u8_data()[0]);
  EXPECT_EQ(UINT8_MAX, (myUInt8)response.u8_data()[1]);
  EXPECT_EQ(16, (myUInt8)response.u8_data()[2]);
  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, IotaWithCustomSizeUsingFirstSizeOption_ReturnsIotaDataOfFirstSizePlusOne)
{
  const auto SIZE_ONE = 10;
  setup_iota_with_custom_size();
  ::grpc::ServerContext context;
  IotaWithCustomSizeRequest request;
  request.set_size_one(SIZE_ONE);
  request.set_size_two(100000);
  IotaWithCustomSizeResponse response;
  service_.IotaWithCustomSize(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_IOTA_OF_SIZE(response, SIZE_ONE + 1);
}

TEST_F(NiFakeNonIviServiceTests, IotaWithCustomSizeUsingSecondSizeOption_ReturnsIotaDataOfSecondSize)
{
  const auto SIZE_TWO = 20;
  setup_iota_with_custom_size();
  ::grpc::ServerContext context;
  IotaWithCustomSizeRequest request;
  request.set_size_one(-1);
  request.set_size_two(SIZE_TWO);
  IotaWithCustomSizeResponse response;

  service_.IotaWithCustomSize(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_IOTA_OF_SIZE(response, SIZE_TWO);
}

TEST_F(NiFakeNonIviServiceTests, InputVarArgs_OneArgumentPair)
{
  EXPECT_CALL(*library_, InputVarArgs(StrEq("inputName"), StrEq("channel"), BEAUTIFUL_COLOR_PINK, 1.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputVarArgsRequest request;
  request.set_input_name("inputName");
  auto arg = request.add_string_and_enums();
  arg->set_channel_name("channel");
  arg->set_color(BEAUTIFUL_COLOR_PINK);
  arg->set_power_up_state(1.0);
  InputVarArgsResponse response;

  service_.InputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputVarArgs_TwoArgumentPairs)
{
  EXPECT_CALL(*library_, InputVarArgs(StrEq("inputName"), StrEq("channel0"), BEAUTIFUL_COLOR_PINK, 1.0, StrEq("channel1"), BEAUTIFUL_COLOR_AQUA, 2.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputVarArgsRequest request;
  request.set_input_name("inputName");
  auto arg = request.add_string_and_enums();
  arg->set_channel_name("channel0");
  arg->set_color(BEAUTIFUL_COLOR_PINK);
  arg->set_power_up_state(1.0);
  arg = request.add_string_and_enums();
  arg->set_channel_name("channel1");
  arg->set_color(BEAUTIFUL_COLOR_AQUA);
  arg->set_power_up_state(2.0);
  InputVarArgsResponse response;

  service_.InputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputVarArgs_ThreeArgumentPairs)
{
  EXPECT_CALL(*library_, InputVarArgs(StrEq("inputName"), StrEq("channel0"), BEAUTIFUL_COLOR_PINK, 1.0, StrEq("channel1"), BEAUTIFUL_COLOR_AQUA, 2.0, StrEq("channel2"), BEAUTIFUL_COLOR_GREEN, 3.0, nullptr, BEAUTIFUL_COLOR_UNSPECIFIED, 0.0))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputVarArgsRequest request;
  request.set_input_name("inputName");
  auto arg = request.add_string_and_enums();
  arg->set_channel_name("channel0");
  arg->set_color(BEAUTIFUL_COLOR_PINK);
  arg->set_power_up_state(1.0);
  arg = request.add_string_and_enums();
  arg->set_channel_name("channel1");
  arg->set_color(BEAUTIFUL_COLOR_AQUA);
  arg->set_power_up_state(2.0);
  arg = request.add_string_and_enums();
  arg->set_channel_name("channel2");
  arg->set_color(BEAUTIFUL_COLOR_GREEN);
  arg->set_power_up_state(3.0);
  InputVarArgsResponse response;

  service_.InputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputVarArgs_NoArgumentPairs)
{
  EXPECT_CALL(*library_, InputVarArgs(_, _, _, _, _, _, _, _, _, _, _, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  InputVarArgsRequest request;
  request.set_input_name("inputName");
  InputVarArgsResponse response;

  auto status = service_.InputVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
}

TEST_F(NiFakeNonIviServiceTests, InputVarArgs_FourArgumentPairs)
{
  EXPECT_CALL(*library_, InputVarArgs(_, _, _, _, _, _, _, _, _, _, _, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  InputVarArgsRequest request;
  request.set_input_name("inputName");
  for (auto i = 0; i < 4; i++) {
    request.add_string_and_enums();
  }
  InputVarArgsResponse response;

  auto status = service_.InputVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
}

TEST_F(NiFakeNonIviServiceTests, OutputVarArgs_OneArgumentPair)
{
  EXPECT_CALL(*library_, OutputVarArgs(StrEq("inputName"), StrEq("channel"), _, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr))
      .WillOnce(DoAll(
          SetArgPointee<2>(BEAUTIFUL_COLOR_PINK),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputVarArgsRequest request;
  request.set_input_name("inputName");
  request.add_channel_names("channel");
  OutputVarArgsResponse response;

  service_.OutputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(1, response.colors_size());
  EXPECT_EQ(BEAUTIFUL_COLOR_PINK, response.colors(0));
}

TEST_F(NiFakeNonIviServiceTests, OutputVarArgs_TwoArgumentPairs)
{
  EXPECT_CALL(*library_, OutputVarArgs(StrEq("inputName"), StrEq("channel1"), _, StrEq("channel2"), _, nullptr, nullptr, nullptr, nullptr))
      .WillOnce(DoAll(
          SetArgPointee<2>(BEAUTIFUL_COLOR_PINK),
          SetArgPointee<4>(BEAUTIFUL_COLOR_AQUA),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputVarArgsRequest request;
  request.set_input_name("inputName");
  request.add_channel_names("channel1");
  request.add_channel_names("channel2");
  OutputVarArgsResponse response;

  service_.OutputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(2, response.colors_size());
  EXPECT_EQ(BEAUTIFUL_COLOR_PINK, response.colors(0));
  EXPECT_EQ(BEAUTIFUL_COLOR_AQUA, response.colors(1));
}

TEST_F(NiFakeNonIviServiceTests, OutputVarArgs_ThreeArgumentPairs)
{
  EXPECT_CALL(*library_, OutputVarArgs(StrEq("inputName"), StrEq("channel1"), _, StrEq("channel2"), _, StrEq("channel3"), _, nullptr, nullptr))
      .WillOnce(DoAll(
          SetArgPointee<2>(BEAUTIFUL_COLOR_PINK),
          SetArgPointee<4>(BEAUTIFUL_COLOR_AQUA),
          SetArgPointee<6>(BEAUTIFUL_COLOR_GREEN),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputVarArgsRequest request;
  request.set_input_name("inputName");
  request.add_channel_names("channel1");
  request.add_channel_names("channel2");
  request.add_channel_names("channel3");
  OutputVarArgsResponse response;

  service_.OutputVarArgs(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(3, response.colors_size());
  EXPECT_EQ(BEAUTIFUL_COLOR_PINK, response.colors(0));
  EXPECT_EQ(BEAUTIFUL_COLOR_AQUA, response.colors(1));
  EXPECT_EQ(BEAUTIFUL_COLOR_GREEN, response.colors(2));
}

TEST_F(NiFakeNonIviServiceTests, OutputVarArgs_NoArgumentPairs)
{
  EXPECT_CALL(*library_, OutputVarArgs(_, _, _, _, _, _, _, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  OutputVarArgsRequest request;
  request.set_input_name("inputName");
  OutputVarArgsResponse response;

  auto status = service_.OutputVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
}

TEST_F(NiFakeNonIviServiceTests, OutputVarArgs_FourArgumentPairs)
{
  EXPECT_CALL(*library_, OutputVarArgs(_, _, _, _, _, _, _, _, _))
      .Times(0);
  ::grpc::ServerContext context;
  OutputVarArgsRequest request;
  request.set_input_name("inputName");
  for (auto i = 0; i < 4; i++) {
    request.add_channel_names("channel");
  }
  OutputVarArgsResponse response;

  auto status = service_.OutputVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
}

const int64 SecondsFromCVI1904EpochTo1970Epoch = 2082844800LL;
TEST_F(NiFakeNonIviServiceTests, InputTimestamp_UnixEpoch)
{
  CVIAbsoluteTime timestamp;
  timestamp.cviTime.msb = SecondsFromCVI1904EpochTo1970Epoch;
  timestamp.cviTime.lsb = 0;
  EXPECT_CALL(*library_, InputTimestamp(CVIAbsoluteTimeEq(timestamp)))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputTimestampRequest request;
  google::protobuf::Timestamp* timestamp_pb = request.mutable_when();
  timestamp_pb->set_seconds(0);
  timestamp_pb->set_nanos(0);
  InputTimestampResponse response;

  service_.InputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputTimestamp_UnixEpochWithFractionalSeconds)
{
  CVIAbsoluteTime timestamp;
  timestamp.cviTime.msb = SecondsFromCVI1904EpochTo1970Epoch;
  timestamp.cviTime.lsb = 0x8000000000000000LL;
  EXPECT_CALL(*library_, InputTimestamp(CVIAbsoluteTimeEq(timestamp)))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputTimestampRequest request;
  google::protobuf::Timestamp* timestamp_pb = request.mutable_when();
  timestamp_pb->set_seconds(0);
  // exactly .5 seconds
  timestamp_pb->set_nanos(500 * 1000 * 1000);
  InputTimestampResponse response;

  service_.InputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

// Determined from CVI:
// CVIAbsoluteTime msb: 3709898694
// UTC time string: "2021-07-23T15:24:54.00Z
CVIAbsoluteTime cviKnownTimestamp = {0, 3709898694LL};
const std::string cviKnownTimestampString = "2021-07-23T15:24:54.00Z";

TEST_F(NiFakeNonIviServiceTests, InputTimestamp_KnownValue)
{
  EXPECT_CALL(*library_, InputTimestamp(CVIAbsoluteTimeEq(cviKnownTimestamp)))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  InputTimestampRequest request;
  google::protobuf::util::TimeUtil::FromString(cviKnownTimestampString, request.mutable_when());
  InputTimestampResponse response;

  service_.InputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, OutputTimestamp_UnixEpoch)
{
  CVIAbsoluteTime timestamp;
  timestamp.cviTime.msb = SecondsFromCVI1904EpochTo1970Epoch;
  timestamp.cviTime.lsb = 0;
  EXPECT_CALL(*library_, OutputTimestamp(_))
      .WillOnce(DoAll(SetArgPointee<0>(timestamp), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputTimestampRequest request;
  OutputTimestampResponse response;

  service_.OutputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(0, response.when().seconds());
  EXPECT_EQ(0, response.when().nanos());
}

TEST_F(NiFakeNonIviServiceTests, OutputTimestamp_UnixEpochWithFractionalSeconds)
{
  CVIAbsoluteTime timestamp;
  timestamp.cviTime.msb = SecondsFromCVI1904EpochTo1970Epoch;
  timestamp.cviTime.lsb = 0x8000000000000000LL;
  EXPECT_CALL(*library_, OutputTimestamp(_))
      .WillOnce(DoAll(SetArgPointee<0>(timestamp), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputTimestampRequest request;
  OutputTimestampResponse response;

  service_.OutputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(0, response.when().seconds());
  EXPECT_EQ(500 * 1000 * 1000, response.when().nanos());
}

TEST_F(NiFakeNonIviServiceTests, OutputTimestamp_KnownValue)
{
  EXPECT_CALL(*library_, OutputTimestamp(_))
      .WillOnce(DoAll(SetArgPointee<0>(cviKnownTimestamp), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputTimestampRequest request;
  OutputTimestampResponse response;

  service_.OutputTimestamp(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  google::protobuf::Timestamp timestamp;
  google::protobuf::util::TimeUtil::FromString(cviKnownTimestampString, &timestamp);
  EXPECT_EQ(timestamp, response.when());
}

TEST_F(NiFakeNonIviServiceTests, SetMarbleAttributeDouble_Succeeds)
{
  const auto ATTRIBUTE = MarbleDoubleAttribute::MARBLE_ATTRIBUTE_WEIGHT;
  const auto VALUE = 1.2345;
  EXPECT_CALL(*library_, SetMarbleAttributeDouble(_, ATTRIBUTE, VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeDoubleRequest request;
  request.set_attribute(ATTRIBUTE);
  request.set_value(VALUE);
  SetMarbleAttributeDoubleResponse response;
  service_.SetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, SetMarbleAttributeInt32_Succeeds)
{
  const auto ATTRIBUTE = MarbleInt32Attribute::MARBLE_ATTRIBUTE_COLOR;
  const auto VALUE = MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_GREEN;
  EXPECT_CALL(*library_, SetMarbleAttributeInt32(_, ATTRIBUTE, VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeInt32Request request;
  request.set_attribute(ATTRIBUTE);
  request.set_value(VALUE);
  SetMarbleAttributeInt32Response response;
  service_.SetMarbleAttributeInt32(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, SetMarbleAttributeInt32Raw_Succeeds)
{
  const auto ATTRIBUTE = MarbleInt32Attribute::MARBLE_ATTRIBUTE_COLOR;
  const auto VALUE = 9999;
  EXPECT_CALL(*library_, SetMarbleAttributeInt32(_, ATTRIBUTE, VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeInt32Request request;
  request.set_attribute(ATTRIBUTE);
  request.set_value_raw(VALUE);
  SetMarbleAttributeInt32Response response;
  service_.SetMarbleAttributeInt32(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, GetMarbleAttributeInt32Enum_ReturnsValueAndValueRaw)
{
  const auto ATTRIBUTE = MarbleInt32Attribute::MARBLE_ATTRIBUTE_COLOR;
  const auto VALUE = MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_AQUA;
  EXPECT_CALL(*library_, GetMarbleAttributeInt32(_, ATTRIBUTE, _))
      .WillOnce(DoAll(SetArgPointee<2>(VALUE), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetMarbleAttributeInt32Request request;
  request.set_attribute(ATTRIBUTE);
  GetMarbleAttributeInt32Response response;
  service_.GetMarbleAttributeInt32(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(VALUE, response.value());
  EXPECT_EQ(VALUE, response.value_raw());
}

template <typename TValueEnum, typename TIterator>
auto convert_to_enum_vector(TIterator begin, TIterator end)
{
  auto vec = std::vector<TValueEnum>{};
  std::transform(
      begin,
      end,
      std::back_inserter(vec),
      [](auto x) { return static_cast<TValueEnum>(x); });
  return vec;
}

template <typename TValueEnum, typename TResponse>
auto get_value_enum_vector(const TResponse& response)
{
  // Repeated enums are just ints in the c++ generated code: cast/convert them.
  return convert_to_enum_vector<TValueEnum>(
      response.value().cbegin(),
      response.value().cend());
}

template <typename TRaw = int32, typename TResponse>
auto get_value_raw_vector(const TResponse& response)
{
  return std::vector<TRaw>{response.value_raw().cbegin(), response.value_raw().cend()};
}

TEST_F(NiFakeNonIviServiceTests, GetMarbleAttributeInt32ArrayNonEnum_ReturnsValueRawAndUnspecifiedValue)
{
  const auto ATTRIBUTE = MarbleInt32ArrayAttribute::MARBLE_ATTRIBUTE_TEN_RANDOM_NUMBERS;
  int VALUE[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
  EXPECT_CALL(*library_, GetMarbleAttributeInt32Array(_, ATTRIBUTE, _))
      .WillOnce(DoAll(SetArrayArgument<2>(VALUE, VALUE + 10), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetMarbleAttributeInt32ArrayRequest request;
  request.set_attribute(ATTRIBUTE);
  GetMarbleAttributeInt32ArrayResponse response;
  service_.GetMarbleAttributeInt32Array(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  auto expected_raw = std::vector<int32>(VALUE, VALUE + 10);
  auto raw_result = get_value_raw_vector(response);
  EXPECT_THAT(raw_result, ContainerEq(expected_raw));
  auto expected = std::vector<MarbleInt32AttributeValues>(10, MarbleInt32AttributeValues::MARBLE_INT32_UNSPECIFIED);
  auto result = get_value_enum_vector<MarbleInt32AttributeValues>(response);
  EXPECT_THAT(result, ContainerEq(expected));
}

TEST_F(NiFakeNonIviServiceTests, GetMarbleAttributeInt32NonEnum_ReturnsValueRawAndUnspecifiedValue)
{
  const auto ATTRIBUTE = MarbleInt32Attribute::MARBLE_ATTRIBUTE_NUMBER_OF_FAILED_ATTEMPTS;
  const auto VALUE = 1000;
  EXPECT_CALL(*library_, GetMarbleAttributeInt32(_, ATTRIBUTE, _))
      .WillOnce(DoAll(SetArgPointee<2>(VALUE), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetMarbleAttributeInt32Request request;
  request.set_attribute(ATTRIBUTE);
  GetMarbleAttributeInt32Response response;
  service_.GetMarbleAttributeInt32(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(MarbleInt32AttributeValues::MARBLE_INT32_UNSPECIFIED, response.value());
  EXPECT_EQ(VALUE, response.value_raw());
}

TEST_F(NiFakeNonIviServiceTests, GetMarbleAttributeInt32ArrayEnum_ReturnsValueAndValueRaw)
{
  const auto ATTRIBUTE = MarbleInt32ArrayAttribute::MARBLE_ATTRIBUTE_TEN_FAVORITE_COLORS;
  int VALUE[] = {
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_AQUA,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_BLACK,
      MarbleInt32AttributeValues::MARBLE_INT32_BEAUTIFUL_COLOR_PINK,
  };
  EXPECT_CALL(*library_, GetMarbleAttributeInt32Array(_, ATTRIBUTE, _))
      .WillOnce(DoAll(SetArrayArgument<2>(VALUE, VALUE + 10), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetMarbleAttributeInt32ArrayRequest request;
  request.set_attribute(ATTRIBUTE);
  GetMarbleAttributeInt32ArrayResponse response;
  service_.GetMarbleAttributeInt32Array(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  auto expected_raw = std::vector<int32>(VALUE, VALUE + 10);
  auto raw_result = get_value_raw_vector(response);
  EXPECT_THAT(raw_result, ContainerEq(expected_raw));
  auto expected = convert_to_enum_vector<MarbleInt32AttributeValues>(VALUE, VALUE + 10);
  auto result = get_value_enum_vector<MarbleInt32AttributeValues>(response);
  EXPECT_THAT(result, ContainerEq(expected));
}

TEST_F(NiFakeNonIviServiceTests, ResetMarbleAttribute_Succeeds)
{
  const auto ATTRIBUTE = MarbleResetAttribute::MARBLE_RESET_ATTRIBUTE_WEIGHT;
  EXPECT_CALL(*library_, ResetMarbleAttribute(_, ATTRIBUTE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  ResetMarbleAttributeRequest request;
  request.set_attribute(ATTRIBUTE);
  ResetMarbleAttributeResponse response;
  service_.ResetMarbleAttribute(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, SetMarbleAttributeRaw_PassesAttributeAndValueToLibrary)
{
  const auto RAW_ATTRIBUTE = static_cast<int32>(MarbleDoubleAttribute::MARBLE_ATTRIBUTE_WEIGHT);
  const auto DOUBLE_VALUE = 1.234;
  EXPECT_CALL(*library_, SetMarbleAttributeDouble(_, RAW_ATTRIBUTE, DOUBLE_VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeDoubleRequest request;
  request.set_attribute_raw(RAW_ATTRIBUTE);
  request.set_value(DOUBLE_VALUE);
  SetMarbleAttributeDoubleResponse response;
  service_.SetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, SetMarbleAttributeRawWithInvalidAttribute_PassesZeroAttributeToLibrary)
{
  const auto RAW_ATTRIBUTE = 9999;
  const auto DOUBLE_VALUE = 1.234;
  EXPECT_CALL(*library_, SetMarbleAttributeDouble(_, 0, DOUBLE_VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeDoubleRequest request;
  request.set_attribute_raw(RAW_ATTRIBUTE);
  request.set_value(DOUBLE_VALUE);
  SetMarbleAttributeDoubleResponse response;
  service_.SetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

struct NiFakeNonIviServiceAllowUndefinedAttributesTests : public NiFakeNonIviServiceTests {
  NiFakeNonIviServiceAllowUndefinedAttributesTests()
      : NiFakeNonIviServiceTests(
            nidevice_grpc::FeatureToggles({{"nifake_non_ivi.allow_undefined_attributes", true}}))
  {
  }
};

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, SetMarbleAttributeRawWithInvalidAttribute_PassesRawAttributeToLibrary)
{
  const auto RAW_ATTRIBUTE = 9999;
  const auto DOUBLE_VALUE = 1.234;
  EXPECT_CALL(*library_, SetMarbleAttributeDouble(_, RAW_ATTRIBUTE, DOUBLE_VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeDoubleRequest request;
  request.set_attribute_raw(RAW_ATTRIBUTE);
  request.set_value(DOUBLE_VALUE);
  SetMarbleAttributeDoubleResponse response;
  service_.SetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, SetMarbleAttributeWithTypeCastedInvalidAttribute_PassesZeroAttributeToLibrary)
{
  const auto CASTED_INVALID_ATTRIBUTE = static_cast<MarbleDoubleAttribute>(9999);
  const auto DOUBLE_VALUE = 1.234;
  EXPECT_CALL(*library_, SetMarbleAttributeDouble(_, 0, DOUBLE_VALUE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetMarbleAttributeDoubleRequest request;
  request.set_attribute(CASTED_INVALID_ATTRIBUTE);
  request.set_value(DOUBLE_VALUE);
  SetMarbleAttributeDoubleResponse response;
  service_.SetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, GetMarbleAttributeRawWithInvalidAttribute_PassesRawAttributeToLibrary)
{
  const auto RAW_ATTRIBUTE = 9999;
  EXPECT_CALL(*library_, GetMarbleAttributeDouble(_, RAW_ATTRIBUTE, _))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  GetMarbleAttributeDoubleRequest request;
  request.set_attribute_raw(RAW_ATTRIBUTE);
  GetMarbleAttributeDoubleResponse response;
  service_.GetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, GetMarbleAttributeWithTypeCastedInvalidAttribute_PassesZeroAttributeToLibrary)
{
  const auto CASTED_INVALID_ATTRIBUTE = static_cast<MarbleDoubleAttribute>(9999);
  EXPECT_CALL(*library_, GetMarbleAttributeDouble(_, 0, _))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  GetMarbleAttributeDoubleRequest request;
  request.set_attribute(CASTED_INVALID_ATTRIBUTE);
  GetMarbleAttributeDoubleResponse response;
  service_.GetMarbleAttributeDouble(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, ResetMarbleAttributeRawWithInvalidAttribute_PassesRawAttributeToLibrary)
{
  const auto RAW_ATTRIBUTE = 9999;
  EXPECT_CALL(*library_, ResetMarbleAttribute(_, RAW_ATTRIBUTE))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  ResetMarbleAttributeRequest request;
  request.set_attribute_raw(RAW_ATTRIBUTE);
  ResetMarbleAttributeResponse response;
  service_.ResetMarbleAttribute(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceAllowUndefinedAttributesTests, ResetMarbleAttributeWithTypeCastedInvalidAttribute_PassesZeroAttributeToLibrary)
{
  const auto CASTED_INVALID_ATTRIBUTE = static_cast<MarbleResetAttribute>(9999);
  EXPECT_CALL(*library_, ResetMarbleAttribute(_, 0))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  ResetMarbleAttributeRequest request;
  request.set_attribute(CASTED_INVALID_ATTRIBUTE);
  ResetMarbleAttributeResponse response;
  service_.ResetMarbleAttribute(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, SetColors_PassesColorsArrayToLibrary)
{
  const auto COLORS = std::vector<BeautifulColor>{
      BeautifulColor::BEAUTIFUL_COLOR_AQUA,
      BeautifulColor::BEAUTIFUL_COLOR_GREEN,
      BeautifulColor::BEAUTIFUL_COLOR_PINK};
  EXPECT_CALL(*library_, SetColors(_, _))
      .With(Args<0, 1>(ElementsAreArray(COLORS.data(), COLORS.size())))
      .WillOnce(Return(kDriverSuccess));
  ::grpc::ServerContext context;
  SetColorsRequest request;
  request.mutable_colors()->CopyFrom({COLORS.begin(), COLORS.end()});
  request.set_size(static_cast<int32>(COLORS.size()));
  SetColorsResponse response;
  service_.SetColors(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, UnreleasedServiceWithToggleEnabled_IsEnabled_ReturnsTrue)
{
  const auto feature_toggles = nidevice_grpc::FeatureToggles({{"nifake_non_ivi", true}});
  const auto fake_toggles = NiFakeNonIviFeatureToggles{feature_toggles};

  EXPECT_TRUE(fake_toggles.is_enabled);
}

TEST_F(NiFakeNonIviServiceTests, UnreleasedServiceWithNoToggles_IsEnabled_ReturnsFalse)
{
  const auto feature_toggles = nidevice_grpc::FeatureToggles();
  const auto fake_toggles = NiFakeNonIviFeatureToggles{feature_toggles};

  EXPECT_FALSE(fake_toggles.is_enabled);
}

TEST_F(NiFakeNonIviServiceTests, GetStructsWithCoercion_ReturnsInRangeData)
{
  ::grpc::ServerContext context;
  GetStructsWithCoercionRequest request;
  request.set_number_of_structs(3);
  GetStructsWithCoercionResponse response;
  EXPECT_CALL(*library_, GetStructsWithCoercion(_, _))
      .WillOnce(DoAll(
          Invoke(SetStructWithCoercionData),
          Return(kDriverSuccess)));

  service_.GetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(3, response.structs().size());
  EXPECT_EQ(3, response.structs_size());
  StructWithCoercion_struct expected_struct;
  SetSingleStructWithCoercionData(&expected_struct, 0);
  EXPECT_EQ(expected_struct, response.structs(0));
  EXPECT_EQ(expected_struct, response.structs()[0]);
  SetSingleStructWithCoercionData(&expected_struct, 1);
  EXPECT_EQ(expected_struct, response.structs(1));
  EXPECT_EQ(expected_struct, response.structs()[1]);
  SetSingleStructWithCoercionData(&expected_struct, 2);
  EXPECT_EQ(expected_struct, response.structs(2));
  EXPECT_EQ(expected_struct, response.structs()[2]);
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_DataGetsCoerced)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .With(CustomStructWithCoercionData())
      .Times(1);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  SetStructsWithCoercionResponse response;

  service_.SetStructsWithCoercion(&context, &request, &response);

  auto status = response.status();
  EXPECT_EQ(kDriverSuccess, status);
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_TooLargeInt16_Error)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .Times(0);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  request.mutable_structs(1)->set_first(INT16_MAX + 1);
  SetStructsWithCoercionResponse response;

  auto status = service_.SetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_TooSmallInt16_Error)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .Times(0);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  request.mutable_structs(1)->set_first(INT16_MIN - 1);
  SetStructsWithCoercionResponse response;

  auto status = service_.SetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT16_MIN - 1)));
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_TooLargeUInt16_Error)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .Times(0);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  request.mutable_structs(1)->set_second(UINT16_MAX + 1);
  SetStructsWithCoercionResponse response;

  auto status = service_.SetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(UINT16_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_TooLargeInt8_Error)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .Times(0);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  request.mutable_structs(1)->set_third(INT8_MAX + 1);
  SetStructsWithCoercionResponse response;

  auto status = service_.SetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT8_MAX + 1)));
}

TEST_F(NiFakeNonIviServiceTests, SetStructsWithCoercion_TooSmallInt8_Error)
{
  EXPECT_CALL(*library_, SetStructsWithCoercion(_))
      .Times(0);
  ::grpc::ServerContext context;
  SetStructsWithCoercionRequest request;
  SetSingleStructWithCoercionData(request.add_structs(), 0);
  SetSingleStructWithCoercionData(request.add_structs(), 1);
  SetSingleStructWithCoercionData(request.add_structs(), 2);
  request.mutable_structs(1)->set_third(INT8_MIN - 1);
  SetStructsWithCoercionResponse response;

  auto status = service_.SetStructsWithCoercion(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::OUT_OF_RANGE, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr(std::to_string(INT8_MIN - 1)));
}

void ExpectOutputArraysWithPassedInByPtrMechanismResponseData(const OutputArraysWithPassedInByPtrMechanismResponse& response)
{
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(3, response.i32_data_size());
  EXPECT_EQ(3, response.i32_data().size());
  EXPECT_EQ(-1, response.i32_data(0));
  EXPECT_EQ(1, response.i32_data(1));
  EXPECT_EQ(128, response.i32_data(2));
  EXPECT_EQ(3, response.u16_data_size());
  EXPECT_EQ(3, response.u16_data().size());
  EXPECT_EQ(0, response.u16_data(0));
  EXPECT_EQ(UINT16_MAX, response.u16_data(1));
  EXPECT_EQ(16, response.u16_data(2));
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithPassedInByPtrMechanism_SizeMatches_ArraysReturnedAreThatSize)
{
  EXPECT_CALL(*library_, OutputArraysWithPassedInByPtrMechanism(_, _, Pointee(3)))
      .WillOnce(DoAll(
          Invoke(SetArraysByPtrData),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputArraysWithPassedInByPtrMechanismRequest request;
  request.set_array_size(3);
  OutputArraysWithPassedInByPtrMechanismResponse response;

  service_.OutputArraysWithPassedInByPtrMechanism(&context, &request, &response);

  ExpectOutputArraysWithPassedInByPtrMechanismResponseData(response);
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithPassedInByPtrMechanism_SizeIsTooBig_ArraysReturnedAreShrunkToCorrectSize)
{
  EXPECT_CALL(*library_, OutputArraysWithPassedInByPtrMechanism(_, _, Pointee(5)))
      .WillOnce(DoAll(
          Invoke(SetArraysByPtrData),
          Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  OutputArraysWithPassedInByPtrMechanismRequest request;
  request.set_array_size(5);
  OutputArraysWithPassedInByPtrMechanismResponse response;

  service_.OutputArraysWithPassedInByPtrMechanism(&context, &request, &response);

  ExpectOutputArraysWithPassedInByPtrMechanismResponseData(response);
}

TEST_F(NiFakeNonIviServiceTests, OutputArraysWithPassedInByPtrMechanism_SizeIsTooSmall_ReturnsError)
{
  const int32 SOME_ERROR = 10;
  EXPECT_CALL(*library_, OutputArraysWithPassedInByPtrMechanism(_, _, Pointee(5)))
      .WillOnce(
          Return(SOME_ERROR));
  ::grpc::ServerContext context;
  OutputArraysWithPassedInByPtrMechanismRequest request;
  request.set_array_size(5);
  OutputArraysWithPassedInByPtrMechanismResponse response;

  service_.OutputArraysWithPassedInByPtrMechanism(&context, &request, &response);

  EXPECT_EQ(SOME_ERROR, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputStringValuedEnum_PassMappedEnum_CorrectStringPassedToFunction)
{
  EXPECT_CALL(*library_, InputStringValuedEnum(StrEq("iOS")))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  InputStringValuedEnumRequest request;
  request.set_a_name_mapped(MobileOSNames::MOBILE_OS_NAMES_IOS);
  InputStringValuedEnumResponse response;

  service_.InputStringValuedEnum(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InputStringValuedEnum_PassNonMappedValue_CorrectStringPassedToFunction)
{
  EXPECT_CALL(*library_, InputStringValuedEnum(StrEq("Windows Phone")))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  InputStringValuedEnumRequest request;
  request.set_a_name_raw("Windows Phone");
  InputStringValuedEnumResponse response;

  service_.InputStringValuedEnum(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, WriteBooleanArray_PassesBooleansAsInt32s)
{
  const auto BOOLS = std::vector<bool>{true, false, true, true, false, false, true, true, true, false, false, false};
  const auto BOOLS_AS_INT32S = std::vector<int32>{1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0};
  EXPECT_CALL(*library_, WriteBooleanArray(_, _))
      .With(Args<0, 1>(ElementsAreArray(BOOLS_AS_INT32S.data(), BOOLS_AS_INT32S.size())))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  WriteBooleanArrayRequest request;
  request.mutable_bools()->CopyFrom({BOOLS.begin(), BOOLS.end()});
  WriteBooleanArrayResponse response;

  service_.WriteBooleanArray(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

template <typename TSessionRepository, typename TResource>
void add_session(TSessionRepository& repository, TResource resource_handle, const std::string name)
{
  std::string session_name = name;
  repository->add_session(
      session_name,
      [resource_handle]() { return std::make_tuple(0, resource_handle); },
      [](TResource handle) {});
}

TEST_F(NiFakeNonIviServiceTests, InitFromCrossDriverSession_PassesSessionResourcesAndSucceeds)
{
  constexpr FakeCrossDriverHandle CROSS_DRIVER_HANDLE = 1234;
  constexpr auto CROSS_DRIVER_SESSION_NAME = "cross_driver_session";
  constexpr auto DRIVER_SESSION = 9876;
  add_session(cross_driver_resource_repository_, CROSS_DRIVER_HANDLE, CROSS_DRIVER_SESSION_NAME);
  EXPECT_CALL(*library_, InitFromCrossDriverSession(CROSS_DRIVER_HANDLE, _))
      .WillOnce(DoAll(
          SetArgPointee<1, FakeHandle>(DRIVER_SESSION), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  InitFromCrossDriverSessionRequest request;
  InitFromCrossDriverSessionResponse response;
  request.set_session_name("fake_session");
  request.mutable_cross_driver_session()->set_name(CROSS_DRIVER_SESSION_NAME);
  service_.InitFromCrossDriverSession(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(DRIVER_SESSION, resource_repository_->access_session(response.handle().name()));
}

template <size_t N>
InitFromCrossDriverSessionArrayRequest create_init_from_cross_driver_session_array_request(const std::array<std::string, N>& session_names)
{
  InitFromCrossDriverSessionArrayRequest request;
  request.set_session_name("fake_session");
  for (const auto& session_name : session_names) {
    auto session_in = request.add_cross_driver_session_array();
    session_in->set_name(session_name);
  }
  return request;
}

TEST_F(NiFakeNonIviServiceTests, InitFromCrossDriverSessionArray_PassesSessionResourcesAndSucceeds)
{
  constexpr auto CROSS_DRIVER_HANDLES = std::array<FakeCrossDriverHandle, 2>{1234, 5678};
  const auto CROSS_DRIVER_SESSION_NAMES = std::array<std::string, 2>{"cross_driver_session", "cross_driver_session_2"};
  constexpr auto DRIVER_SESSION = 9876;
  add_session(cross_driver_resource_repository_, CROSS_DRIVER_HANDLES[0], CROSS_DRIVER_SESSION_NAMES[0]);
  add_session(cross_driver_resource_repository_, CROSS_DRIVER_HANDLES[1], CROSS_DRIVER_SESSION_NAMES[1]);
  EXPECT_CALL(*library_, InitFromCrossDriverSessionArray(_, _, _))
      .With(Args<0, 1>(ElementsAreArray(CROSS_DRIVER_HANDLES.data(), CROSS_DRIVER_HANDLES.size())))
      .WillOnce(DoAll(
          SetArgPointee<2, FakeHandle>(DRIVER_SESSION), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  auto request = create_init_from_cross_driver_session_array_request(CROSS_DRIVER_SESSION_NAMES);
  InitFromCrossDriverSessionArrayResponse response;
  service_.InitFromCrossDriverSessionArray(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(DRIVER_SESSION, resource_repository_->access_session(response.handle().name()));
}

TEST_F(NiFakeNonIviServiceTests, GetCrossDriverSession_CloseInitiatingSession_RemovesBothSessions)
{
  constexpr auto INITIATING_DRIVER_HANDLE = 5678;
  constexpr auto CROSS_DRIVER_HANDLE = 1234;
  constexpr auto INITIATING_SESSION_NAME = "initiating_session";
  constexpr auto CROSS_DRIVER_SESSION_NAME = "cross_driver_session";
  const auto initiating_session_name = init(INITIATING_SESSION_NAME, INITIATING_DRIVER_HANDLE);
  EXPECT_CALL(*library_, GetCrossDriverSession(INITIATING_DRIVER_HANDLE, _))
      .WillOnce(DoAll(
          SetArgPointee<1, FakeCrossDriverHandle>(CROSS_DRIVER_HANDLE), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetCrossDriverSessionRequest request;
  GetCrossDriverSessionResponse response;
  request.mutable_handle()->set_name(INITIATING_SESSION_NAME);
  request.set_session_name(CROSS_DRIVER_SESSION_NAME);
  service_.GetCrossDriverSession(&context, &request, &response);
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(cross_driver_resource_repository_->access_session(CROSS_DRIVER_SESSION_NAME), CROSS_DRIVER_HANDLE);

  close_with_expected_handle(initiating_session_name, INITIATING_DRIVER_HANDLE);

  EXPECT_EQ(cross_driver_resource_repository_->access_session(CROSS_DRIVER_SESSION_NAME), 0);
}

TEST_F(NiFakeNonIviServiceTests, GetCrossDriverSession_ResetServer_RemovesBothSessions)
{
  constexpr auto INITIATING_DRIVER_HANDLE = 5678;
  constexpr auto CROSS_DRIVER_HANDLE = 1234;
  constexpr auto INITIATING_SESSION_NAME = "initiating_session";
  constexpr auto CROSS_DRIVER_SESSION_NAME = "cross_driver_session";
  const auto initiating_session_name = init(INITIATING_SESSION_NAME, INITIATING_DRIVER_HANDLE);
  EXPECT_CALL(*library_, GetCrossDriverSession(INITIATING_DRIVER_HANDLE, _))
      .WillOnce(DoAll(
          SetArgPointee<1, FakeCrossDriverHandle>(CROSS_DRIVER_HANDLE), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetCrossDriverSessionRequest request;
  GetCrossDriverSessionResponse response;
  request.mutable_handle()->set_name(INITIATING_SESSION_NAME);
  request.set_session_name(CROSS_DRIVER_SESSION_NAME);
  service_.GetCrossDriverSession(&context, &request, &response);

  session_repository_->reset_server();

  EXPECT_EQ(cross_driver_resource_repository_->access_session(CROSS_DRIVER_SESSION_NAME), 0);
  EXPECT_EQ(resource_repository_->access_session(INITIATING_SESSION_NAME), 0);
}

TEST_F(NiFakeNonIviServiceTests, SessionAlreadyInCrossDriverSessionRepository_GetCrossDriverSessionForSameResourceHandle_ReverseLookupStillReturnsOriginalSession)
{
  constexpr auto INITIATING_DRIVER_HANDLE = 5678;
  constexpr auto CROSS_DRIVER_HANDLE = 1234;
  constexpr auto INITIATING_SESSION_NAME = "initiating_session";
  constexpr auto CROSS_DRIVER_SESSION_NAME = "cross_driver_session";
  constexpr auto ORIGINAL_NAME_FOR_CROSS_DRIVER_RESOURCE = "original_cross_driver_resource_name";

  std::string session_name = ORIGINAL_NAME_FOR_CROSS_DRIVER_RESOURCE;
  cross_driver_resource_repository_->add_session(
      session_name,
      [&]() { return std::make_tuple(0, CROSS_DRIVER_HANDLE); },
      [](FakeCrossDriverHandle handle) {});

  const auto initiating_session_name = init(INITIATING_SESSION_NAME, INITIATING_DRIVER_HANDLE);
  EXPECT_CALL(*library_, GetCrossDriverSession(INITIATING_DRIVER_HANDLE, _))
      .WillOnce(DoAll(
          SetArgPointee<1, FakeCrossDriverHandle>(CROSS_DRIVER_HANDLE), Return(kDriverSuccess)));
  ::grpc::ServerContext context;
  GetCrossDriverSessionRequest request;
  GetCrossDriverSessionResponse response;
  request.mutable_handle()->set_name(INITIATING_SESSION_NAME);
  request.set_session_name(CROSS_DRIVER_SESSION_NAME);
  service_.GetCrossDriverSession(&context, &request, &response);

  EXPECT_EQ(session_name, cross_driver_resource_repository_->resolve_session_name(CROSS_DRIVER_HANDLE));
}

TEST_F(NiFakeNonIviServiceTests, InitWithReturnedSession_AccessSession_ReturnsInitializeSessionHandle)
{
  constexpr auto SESSION_NAME = "session";
  constexpr auto SESSION_HANDLE = 0x1234UL;
  EXPECT_CALL(*library_, InitWithReturnedSession(StrEq(SESSION_NAME)))
      .WillOnce(Return(SESSION_HANDLE));
  ::grpc::ServerContext context;
  InitWithReturnedSessionRequest request;
  InitWithReturnedSessionResponse response;
  request.set_handle_name(SESSION_NAME);
  service_.InitWithReturnedSession(&context, &request, &response);

  const auto accessed_handle = resource_repository_->access_session(response.handle().name());

  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(SESSION_HANDLE, accessed_handle);
}

TEST_F(NiFakeNonIviServiceTests, InitWithReturnedSessionFailsInit_AccessSession_SessionIsNotInMap)
{
  constexpr auto SESSION_NAME = "session";
  constexpr auto BAD_SESSION_HANDLE = 0xDEADBEEF;  // Fake non-ivi uses 0xDEADBEEF as failed/null session (See functions.py).
  constexpr auto FAILED_INIT = -1;
  EXPECT_CALL(*library_, InitWithReturnedSession(StrEq(SESSION_NAME)))
      .WillOnce(Return(BAD_SESSION_HANDLE));
  ::grpc::ServerContext context;
  InitWithReturnedSessionRequest request;
  InitWithReturnedSessionResponse response;
  request.set_handle_name(SESSION_NAME);
  auto status = service_.InitWithReturnedSession(&context, &request, &response);

  const auto accessed_handle = resource_repository_->access_session(response.handle().name());

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_NE(FAILED_INIT, response.status());
  EXPECT_EQ(0, accessed_handle);
}

TEST_F(NiFakeNonIviServiceTests, GetStringAsReturnedValue_ReturnsString)
{
  constexpr auto STRING_VAL = "Hello Returned World!";
  EXPECT_CALL(*library_, GetStringAsReturnedValue(_))
      .WillOnce(Return(STRING_VAL));
  ::grpc::ServerContext context;
  GetStringAsReturnedValueRequest request;
  GetStringAsReturnedValueResponse response;
  service_.GetStringAsReturnedValue(&context, &request, &response);

  EXPECT_EQ(std::string(STRING_VAL), response.string_out());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeNonIviServiceTests, GetStringAsReturnedValueReturnsNull_ReturnsError)
{
  constexpr auto FAILED_GET = -1;
  EXPECT_CALL(*library_, GetStringAsReturnedValue(_))
      .WillOnce(Return(nullptr));
  ::grpc::ServerContext context;
  GetStringAsReturnedValueRequest request;
  GetStringAsReturnedValueResponse response;
  auto status = service_.GetStringAsReturnedValue(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_NE(FAILED_GET, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InitWithError_CallsGetLatestErrorAndReturnsMessage)
{
  constexpr auto SOME_ERROR = -1;
  const auto ERROR_MESSAGE = std::string("Some error occurred!");
  const auto ERROR_MESSAGE_BUFFER_SIZE = static_cast<int32>(ERROR_MESSAGE.size() + 1);
  EXPECT_CALL(*library_, Init(_, _))
      .WillOnce(Return(SOME_ERROR));
  EXPECT_CALL(*library_, GetLatestErrorMessage(_, 2048))
      .WillOnce(
          DoAll(
              SetArrayArgument<0>(ERROR_MESSAGE.c_str(), ERROR_MESSAGE.c_str() + ERROR_MESSAGE_BUFFER_SIZE),
              Return(0)));
  ::grpc::ServerContext context;
  InitRequest request;
  InitResponse response;
  auto status = service_.Init(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(ERROR_MESSAGE, status.error_message());
  EXPECT_NE(SOME_ERROR, response.status());
}

TEST_F(NiFakeNonIviServiceTests, InitWithNoError_DoesNotCallGetLatestError)
{
  EXPECT_CALL(*library_, Init(_, _))
      .WillOnce(Return(kDriverSuccess));
  EXPECT_CALL(*library_, GetLatestErrorMessage(_, _))
      .Times(0);
  ::grpc::ServerContext context;
  InitRequest request;
  InitResponse response;
  service_.Init(&context, &request, &response);

  EXPECT_EQ(kDriverSuccess, response.status());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/ni_fake_service_tests.cpp sha256=22c0f27481e3048840de93771019191c481ec5e8c03fb507db0dc198b0877123 bytes=141960 -->
## FILE: source/tests/unit/ni_fake_service_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/ni_fake_service_tests.cpp`
- sha256: `22c0f27481e3048840de93771019191c481ec5e8c03fb507db0dc198b0877123`
- bytes: 141960

````cpp
#include <gtest/gtest.h>
#include <nifake/nifake_mock_library.h>
#pragma warning(push)
#pragma warning(disable : 4616)
#pragma warning(disable : 4146)
#pragma warning(disable : 4244)
#include <nifake/nifake_service.h>
#pragma warning(pop)
#include <nifake_extension/nifake_extension_mock_library.h>
#include <nifake_extension/nifake_extension_service.h>
#include <server/session_repository.h>

#include <array>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

using namespace ::nlohmann;

namespace nifake_grpc {
bool operator==(const nifake_grpc::FakeCustomStruct& first, const nifake_grpc::FakeCustomStruct& second)
{
  return first.struct_int() == second.struct_int() && first.struct_double() == second.struct_double();
}
bool operator==(const nifake_grpc::CustomStructTypedef& first, const nifake_grpc::CustomStructTypedef& second)
{
  return first.struct_int() == second.struct_int() && first.struct_double() == second.struct_double();
}
bool operator==(const nifake_grpc::CustomStructNestedTypedef& first, const nifake_grpc::CustomStructNestedTypedef& second)
{
  return first.struct_custom_struct() == second.struct_custom_struct() && first.struct_custom_struct_typedef() == second.struct_custom_struct_typedef();
}
}  // namespace nifake_grpc
// Adding operator for matching Custom Structs
bool operator==(const CustomStruct& first, const CustomStruct& second)
{
  return first.structInt == second.structInt && first.structDouble == second.structDouble;
}

bool operator==(const nifake_grpc::FakeCustomStruct& first, const CustomStruct& second)
{
  return first.struct_int() == second.structInt && first.struct_double() == second.structDouble;
}

bool operator==(const CustomStruct& first, const nifake_grpc::FakeCustomStruct& second)
{
  return second == first;
}

// Adding operator for matching CustomStructTypedef
bool operator==(const CustomStructTypedef_struct& first, const CustomStructTypedef_struct& second)
{
  return first.structDouble == second.structDouble && first.structInt == second.structInt;
}

bool operator==(const nifake_grpc::CustomStructTypedef& first, const CustomStructTypedef_struct& second)
{
  return first.struct_double() == second.structDouble && first.struct_int() == second.structInt;
}

bool operator==(const CustomStructTypedef_struct& first, const nifake_grpc::CustomStructTypedef& second)
{
  return second == first;
}

// Adding operator for matching CustomStructNestedTypedef
bool operator==(const CustomStructNestedTypedef_struct& first, const CustomStructNestedTypedef_struct& second)
{
  return first.structCustomStruct == second.structCustomStruct && first.structCustomStructTypedef == second.structCustomStructTypedef;
}

bool operator==(const nifake_grpc::CustomStructNestedTypedef& first, const CustomStructNestedTypedef_struct& second)
{
  return first.struct_custom_struct() == second.structCustomStruct && first.struct_custom_struct_typedef() == second.structCustomStructTypedef;
}

bool operator==(const CustomStructNestedTypedef_struct& first, const nifake_grpc::CustomStructNestedTypedef& second)
{
  return second == first;
}

using ::testing::StrEq;

namespace ni {
namespace tests {
namespace unit {

using namespace nifake_grpc;
namespace pb = google::protobuf;

using ::testing::_;
using ::testing::AllOf;
using ::testing::Args;
using ::testing::DoAll;
using ::testing::ElementsAre;
using ::testing::ElementsAreArray;
using ::testing::Eq;
using ::testing::HasSubstr;
using ::testing::IsEmpty;
using ::testing::Pointee;
using ::testing::Return;
using ::testing::SetArgPointee;
using ::testing::SetArrayArgument;
using ::testing::Throw;

using FakeResourceRepository = nidevice_grpc::SessionResourceRepository<ViSession>;

const std::uint32_t kTestViSession = 12345678;
const std::uint32_t kDriverSuccess = 0;
const std::uint32_t kDriverFailure = -1;
const std::uint32_t kDriverWarning = 123456;
const char* kTestChannelName = "channel";

std::string create_session(
    const std::shared_ptr<NiFakeMockLibrary>& library,
    nifake_grpc::NiFakeService& service,
    const std::string& session_name)
{
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;
  EXPECT_CALL(*library, InitWithOptions(Pointee(*resource_name), id_query, reset_device, Pointee(*option_string), _))
      .WillOnce(DoAll(SetArgPointee<4>(std::atoi(session_name.c_str())), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name.c_str());
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  return response.vi().name();
}

std::string create_session(
    const std::shared_ptr<NiFakeMockLibrary>& library,
    nifake_grpc::NiFakeService& service,
    std::uint32_t session_name)
{
  return create_session(library, service, std::to_string(session_name));
}

// Init and Close function tests
TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsSucceeds_CreatesAndStoresSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;
  const char* session_name = "sessionName";
  EXPECT_CALL(*library, InitWithOptions(Pointee(*resource_name), id_query, reset_device, Pointee(*option_string), _))
      .WillOnce(DoAll(SetArgPointee<4>(kTestViSession), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  EXPECT_TRUE(response.new_session_initialized());
}

TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsWithAttachBehavior_DoesNotCallIntoDriverAndReturnsFailedPreconditionError)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;
  const char* session_name = "sessionName";
  EXPECT_CALL(*library, InitWithOptions)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name);
  request.set_initialization_behavior(nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_ATTACH_TO_EXISTING);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::FAILED_PRECONDITION, status.error_code());
  const char* expected_error_message = "Cannot attach to 'sessionName' because a session has not been initialized.";
  EXPECT_STREQ(expected_error_message, status.error_message().c_str());
}

TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsWithInitializeBehavior_CreatesAndStoresSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;
  const char* session_name = "sessionName";
  EXPECT_CALL(*library, InitWithOptions(Pointee(*resource_name), id_query, reset_device, Pointee(*option_string), _))
      .WillOnce(DoAll(SetArgPointee<4>(kTestViSession), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name);
  request.set_initialization_behavior(nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  EXPECT_TRUE(response.new_session_initialized());
}

TEST(NiFakeServiceTests, NiFakeServiceWithSession_InitWithOptionsWithInitializeBehavior_ReturnsAlreadyExistsError)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* default_session_name = "sessionName";
  auto session_name = create_session(library, service, default_session_name);
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;
  EXPECT_CALL(*library, InitWithOptions)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name);
  request.set_initialization_behavior(nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::ALREADY_EXISTS, status.error_code());
  const char* expected_error_message = "Cannot initialize 'sessionName' when a session already exists.";
  EXPECT_STREQ(expected_error_message, status.error_message().c_str());
}

TEST(NiFakeServiceTests, NiFakeServiceWithSession_InitWithOptionsWithAttachBehavior_ReturnsAlreadyInitializedSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* default_session_name = "sessionName";
  auto session_name = create_session(library, service, default_session_name);
  const char* resource_name = "Dev0";
  const char* option_string = "Simulate = 1";
  bool id_query = false, reset_device = true;

  EXPECT_CALL(*library, InitWithOptions)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_resource_name(resource_name);
  request.set_id_query(id_query);
  request.set_reset_device(reset_device);
  request.set_option_string(option_string);
  request.set_session_name(session_name);
  request.set_initialization_behavior(nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_ATTACH_TO_EXISTING);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  EXPECT_FALSE(response.new_session_initialized());
}

TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsFails_NoSessionIsStored)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* message = "Exception!";
  EXPECT_CALL(*library, InitWithOptions)
      .WillOnce(DoAll(SetArgPointee<4>(kTestViSession), Throw(nidevice_grpc::LibraryLoadException(message))));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status status = service.InitWithOptions(&context, &request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(message, status.error_message());
  nidevice_grpc::Session session = response.vi();
  EXPECT_EQ("", session_repository->access_session(session.name()));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsAndResetServer_SessionIsClosed)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* session_name = "sessionName";
  EXPECT_CALL(*library, InitWithOptions)
      .WillOnce(DoAll(SetArgPointee<4>(kTestViSession), Return(kDriverSuccess)));
  EXPECT_CALL(*library, Close(kTestViSession))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest request;
  request.set_session_name(session_name);
  nifake_grpc::InitWithOptionsResponse response;
  ::grpc::Status init_status = service.InitWithOptions(&context, &request, &response);
  EXPECT_TRUE(init_status.ok());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  bool reset_status = session_repository->reset_server();

  EXPECT_TRUE(reset_status);
  EXPECT_EQ("", session_repository->access_session(session.name()));
}

TEST(NiFakeServiceTests, NiFakeService_InitExtCalAndResetServer_SessionIsClosed)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* session_name = "sessionName";
  EXPECT_CALL(*library, InitExtCal)
      .WillOnce(DoAll(SetArgPointee<2>(kTestViSession), Return(kDriverSuccess)));
  EXPECT_CALL(*library, CloseExtCal(kTestViSession, 0))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::InitExtCalRequest request;
  request.set_session_name(session_name);
  nifake_grpc::InitExtCalResponse response;
  ::grpc::Status init_status = service.InitExtCal(&context, &request, &response);
  EXPECT_TRUE(init_status.ok());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  bool reset_status = session_repository->reset_server();

  EXPECT_TRUE(reset_status);
  EXPECT_EQ("", session_repository->access_session(session.name()));
  EXPECT_EQ("", session_repository->access_session(session_name));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithOptionsThenClose_SessionIsClosed)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  std::string session_name = "sessionName";
  EXPECT_CALL(*library, InitWithOptions)
      .WillOnce(DoAll(SetArgPointee<4>(kTestViSession), Return(kDriverSuccess)));
  EXPECT_CALL(*library, Close(kTestViSession))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithOptionsRequest init_request;
  init_request.set_session_name(session_name);
  nifake_grpc::InitWithOptionsResponse init_response;
  ::grpc::Status init_status = service.InitWithOptions(&context, &init_request, &init_response);
  EXPECT_TRUE(init_status.ok());
  nidevice_grpc::Session session = init_response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  nifake_grpc::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  nifake_grpc::CloseResponse close_response;
  ::grpc::Status close_status = service.Close(&context, &close_request, &close_response);

  EXPECT_TRUE(close_status.ok());
  EXPECT_EQ(kDriverSuccess, close_response.status());
  EXPECT_EQ("", session_repository->access_session(session.name()));
}

TEST(NiFakeServiceTests, NiFakeService_InitExtCalThenCloseExtCal_SessionIsClosed)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  std::string session_name = "sessionName";
  ViInt32 action = 1;
  EXPECT_CALL(*library, InitExtCal)
      .WillOnce(DoAll(SetArgPointee<2>(kTestViSession), Return(kDriverSuccess)));
  EXPECT_CALL(*library, CloseExtCal(kTestViSession, action))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::InitExtCalRequest init_request;
  init_request.set_session_name(session_name);
  nifake_grpc::InitExtCalResponse init_response;
  ::grpc::Status init_status = service.InitExtCal(&context, &init_request, &init_response);
  EXPECT_TRUE(init_status.ok());
  nidevice_grpc::Session session = init_response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
  nifake_grpc::CloseExtCalRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  close_request.set_action(action);
  nifake_grpc::CloseExtCalResponse close_response;
  ::grpc::Status close_status = service.CloseExtCal(&context, &close_request, &close_response);

  EXPECT_TRUE(close_status.ok());
  EXPECT_EQ(kDriverSuccess, close_response.status());
  EXPECT_EQ("", session_repository->access_session(session.name()));
  EXPECT_EQ("", session_repository->access_session(session_name));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithVarArgsWithOneArgument_SucceedsAndCreatesAndStoresSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* session_name = "sessionName";
  nifake_grpc::Turtle defaultTurtle = nifake_grpc::Turtle::TURTLE_LEONARDO;
  EXPECT_CALL(*library, InitWithVarArgs(Pointee(*resource_name), _, StrEq("SomeStringArg"), nifake_grpc::Turtle::TURTLE_DONATELLO, nullptr, defaultTurtle, nullptr, defaultTurtle, nullptr, defaultTurtle))
      .WillOnce(DoAll(SetArgPointee<1>(kTestViSession), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithVarArgsRequest request;
  request.set_resource_name(resource_name);
  request.set_session_name(session_name);
  auto nameAndTurtle = request.add_name_and_turtle();
  nameAndTurtle->set_string_arg("SomeStringArg");
  nameAndTurtle->set_turtle(nifake_grpc::Turtle::TURTLE_DONATELLO);
  nifake_grpc::InitWithVarArgsResponse response;
  ::grpc::Status status = service.InitWithVarArgs(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithVarArgsWithThreeArguments_SucceedsAndCreatesAndStoresSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* session_name = "sessionName";
  nifake_grpc::Turtle defaultTurtle = nifake_grpc::Turtle::TURTLE_LEONARDO;
  EXPECT_CALL(*library, InitWithVarArgs(Pointee(*resource_name), _, StrEq("SomeStringArg"), nifake_grpc::Turtle::TURTLE_DONATELLO, StrEq("SomeStringArg2"), nifake_grpc::Turtle::TURTLE_MICHELANGELO, StrEq("SomeStringArg3"), nifake_grpc::Turtle::TURTLE_RAPHAEL, nullptr, defaultTurtle))
      .WillOnce(DoAll(SetArgPointee<1>(kTestViSession), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::InitWithVarArgsRequest request;
  request.set_resource_name(resource_name);
  request.set_session_name(session_name);
  auto nameAndTurtle = request.add_name_and_turtle();
  nameAndTurtle->set_string_arg("SomeStringArg");
  nameAndTurtle->set_turtle(nifake_grpc::Turtle::TURTLE_DONATELLO);
  nameAndTurtle = request.add_name_and_turtle();
  nameAndTurtle->set_string_arg("SomeStringArg2");
  nameAndTurtle->set_turtle(nifake_grpc::Turtle::TURTLE_MICHELANGELO);
  nameAndTurtle = request.add_name_and_turtle();
  nameAndTurtle->set_string_arg("SomeStringArg3");
  nameAndTurtle->set_turtle(nifake_grpc::Turtle::TURTLE_RAPHAEL);
  nifake_grpc::InitWithVarArgsResponse response;
  ::grpc::Status status = service.InitWithVarArgs(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  nidevice_grpc::Session session = response.vi();
  EXPECT_NE("", session_repository->access_session(session.name()));
  EXPECT_NE("", session_repository->access_session(session_name));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithVarArgsWithNoArguments_FailsAndDoesNotStoreSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* session_name = "sessionName";
  nifake_grpc::Turtle defaultTurtle = nifake_grpc::Turtle::TURTLE_LEONARDO;
  EXPECT_CALL(*library, InitWithVarArgs)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::InitWithVarArgsRequest request;
  request.set_resource_name(resource_name);
  request.set_session_name(session_name);
  nifake_grpc::InitWithVarArgsResponse response;
  ::grpc::Status status = service.InitWithVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
  nidevice_grpc::Session session = response.vi();
  EXPECT_EQ("", session_repository->access_session(session.name()));
}

TEST(NiFakeServiceTests, NiFakeService_InitWithVarArgsWithFourArguments_FailsAndDoesNotStoreSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const char* resource_name = "Dev0";
  const char* session_name = "sessionName";
  nifake_grpc::Turtle defaultTurtle = nifake_grpc::Turtle::TURTLE_LEONARDO;
  EXPECT_CALL(*library, InitWithVarArgs)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::InitWithVarArgsRequest request;
  request.set_resource_name(resource_name);
  request.set_session_name(session_name);
  for (int i = 0; i < 4; ++i) {
    request.add_name_and_turtle();
  }
  nifake_grpc::InitWithVarArgsResponse response;
  ::grpc::Status status = service.InitWithVarArgs(&context, &request, &response);

  EXPECT_EQ(grpc::StatusCode::INVALID_ARGUMENT, status.error_code());
  nidevice_grpc::Session session = response.vi();
  EXPECT_EQ("", session_repository->access_session(session.name()));
}

// Error logic tests using GetABoolean
TEST(NiFakeServiceTests, NiFakeService_FunctionNotFound_DoesNotCallFunction)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* message = "Exception!";
  EXPECT_CALL(*library, GetABoolean)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(message)));

  ::grpc::ServerContext context;
  nifake_grpc::GetABooleanRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetABooleanResponse response;
  ::grpc::Status status = service.GetABoolean(&context, &request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(message, status.error_message());
}

TEST(NiFakeServiceTests, NiFakeService_FunctionCallErrors_ResponseValuesNotSet)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  EXPECT_CALL(*library, GetABoolean(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_boolean), Return(kDriverFailure)));

  ::grpc::ServerContext context;
  nifake_grpc::GetABooleanRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetABooleanResponse response;
  ::grpc::Status status = service.GetABoolean(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_NE(kDriverFailure, response.status());
  EXPECT_NE(a_boolean, response.a_boolean());
}

TEST(NiFakeServiceTests, NiFakeService_FunctionCallReturnsWarning_ResponseValueSet)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  EXPECT_CALL(*library, GetABoolean(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_boolean), Return(kDriverWarning)));

  ::grpc::ServerContext context;
  nifake_grpc::GetABooleanRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetABooleanResponse response;
  ::grpc::Status status = service.GetABoolean(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverWarning, response.status());
  EXPECT_EQ(a_boolean, response.a_boolean());
}

TEST(NiFakeServiceTests, NiFakeService_GetABoolean_CallsGetABoolean)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  EXPECT_CALL(*library, GetABoolean(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_boolean), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetABooleanRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetABooleanResponse response;
  ::grpc::Status status = service.GetABoolean(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_boolean, response.a_boolean());
}

// Simple Input and Output Type Function Tests
TEST(NiFakeServiceTests, NiFakeService_Abort_CallsAbort)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  EXPECT_CALL(*library, Abort(kTestViSession))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::AbortRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::AbortResponse response;
  ::grpc::Status status = service.Abort(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_GetANumber_CallsGetANumber)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int16_t a_number = 15;
  EXPECT_CALL(*library, GetANumber(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_number), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetANumberRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetANumberResponse response;
  ::grpc::Status status = service.GetANumber(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_number, response.a_number());
}

TEST(NiFakeServiceTests, NiFakeService_GetArraySizeForCustomCode_CallsGetArraySizeForCustomCode)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int32_t array_size = 1000;
  EXPECT_CALL(*library, GetArraySizeForCustomCode(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(array_size), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetArraySizeForCustomCodeRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetArraySizeForCustomCodeResponse response;
  ::grpc::Status status = service.GetArraySizeForCustomCode(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(array_size, response.size_out());
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViBoolean_CallsGetAttributeViBoolean)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_BOOL;
  bool attribute_value = true;
  EXPECT_CALL(*library, GetAttributeViBoolean(kTestViSession, Pointee(*kTestChannelName), attribute_id, _))
      .WillOnce(DoAll(SetArgPointee<3>(attribute_value), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViBooleanRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_channel_name(kTestChannelName);
  request.set_attribute_id(attribute_id);
  nifake_grpc::GetAttributeViBooleanResponse response;
  ::grpc::Status status = service.GetAttributeViBoolean(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(attribute_value, response.attribute_value());
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViInt32_CallsGetAttributeViInt32)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER;
  std::int32_t attribute_value = 12345;
  EXPECT_CALL(*library, GetAttributeViInt32(kTestViSession, Pointee(*kTestChannelName), attribute_id, _))
      .WillOnce(DoAll(SetArgPointee<3>(attribute_value), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViInt32Request request;
  request.mutable_vi()->set_name(session_name);
  request.set_channel_name(kTestChannelName);
  request.set_attribute_id(attribute_id);
  nifake_grpc::GetAttributeViInt32Response response;
  ::grpc::Status status = service.GetAttributeViInt32(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(attribute_value, response.attribute_value());
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViInt64_CallsGetAttributeViInt64)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_INT64;
  std::int64_t attribute_value = -12345;
  EXPECT_CALL(*library, GetAttributeViInt64(kTestViSession, Pointee(*kTestChannelName), attribute_id, _))
      .WillOnce(DoAll(SetArgPointee<3>(attribute_value), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViInt64Request request;
  request.mutable_vi()->set_name(session_name);
  request.set_channel_name(kTestChannelName);
  request.set_attribute_id(attribute_id);
  nifake_grpc::GetAttributeViInt64Response response;
  ::grpc::Status status = service.GetAttributeViInt64(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(attribute_value, response.attribute_value());
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViReal64_CallsGetAttributeViReal64)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE;
  double attribute_value = 12.345;
  EXPECT_CALL(*library, GetAttributeViReal64(kTestViSession, Pointee(*kTestChannelName), attribute_id, _))
      .WillOnce(DoAll(SetArgPointee<3>(attribute_value), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViReal64Request request;
  request.mutable_vi()->set_name(session_name);
  request.set_channel_name(kTestChannelName);
  request.set_attribute_id(attribute_id);
  nifake_grpc::GetAttributeViReal64Response response;
  ::grpc::Status status = service.GetAttributeViReal64(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(attribute_value, response.attribute_value());
}

TEST(NiFakeServiceTests, NiFakeService_GetCalDateAndTime_CallsGetCalDateAndTime)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int32_t cal_type = 0;
  std::int32_t month = 1, day = 17, year = 2021, hour = 0, minute = 0;
  EXPECT_CALL(*library, GetCalDateAndTime(kTestViSession, cal_type, _, _, _, _, _))
      .WillOnce(DoAll(
          SetArgPointee<2>(month),
          SetArgPointee<3>(day),
          SetArgPointee<4>(year),
          SetArgPointee<5>(hour),
          SetArgPointee<6>(minute),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetCalDateAndTimeRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_cal_type(cal_type);
  nifake_grpc::GetCalDateAndTimeResponse response;
  ::grpc::Status status = service.GetCalDateAndTime(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(month, response.month());
  EXPECT_EQ(day, response.day());
  EXPECT_EQ(year, response.year());
  EXPECT_EQ(hour, response.hour());
  EXPECT_EQ(minute, response.minute());
}

TEST(NiFakeServiceTests, NiFakeService_GetCalInterval_CallsGetCalInterval)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE;
  std::int32_t months = 24;
  EXPECT_CALL(*library, GetCalInterval(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(months), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetCalIntervalRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetCalIntervalResponse response;
  ::grpc::Status status = service.GetCalInterval(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(months, response.months());
}

TEST(NiFakeServiceTests, NiFakeService_GetEnumValue_CallsGetEnumValue)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int32_t a_quantity = 123;
  std::int16_t a_turtle = NIFAKE_VAL_LEONARDO;
  EXPECT_CALL(*library, GetEnumValue(kTestViSession, _, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_quantity), SetArgPointee<2>(a_turtle), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetEnumValueRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetEnumValueResponse response;
  ::grpc::Status status = service.GetEnumValue(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_quantity, response.a_quantity());
  EXPECT_EQ(a_turtle, response.a_turtle());
  EXPECT_EQ(a_turtle, response.a_turtle_raw());
}

TEST(NiFakeServiceTests, NiFakeService_GetEnumValueNotInEnum_CallsGetEnumValue)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int32_t a_quantity = 123;
  std::int16_t a_turtle = 5;
  EXPECT_CALL(*library, GetEnumValue(kTestViSession, _, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_quantity), SetArgPointee<2>(a_turtle), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetEnumValueRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetEnumValueResponse response;
  ::grpc::Status status = service.GetEnumValue(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_quantity, response.a_quantity());
  EXPECT_EQ(a_turtle, response.a_turtle());
  EXPECT_EQ(a_turtle, response.a_turtle_raw());
}

// Array input and output tests
TEST(NiFakeServiceTests, NiFakeService_AcceptListOfDurationsInSeconds_CallsAcceptListOfDurationsInSeconds)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const double delays[] = {1, 2, 3, 4, 5};
  std::int32_t expected_size = 5;
  EXPECT_CALL(*library, AcceptListOfDurationsInSeconds(kTestViSession, expected_size, _))
      .With(Args<2, 1>(ElementsAreArray(delays)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::AcceptListOfDurationsInSecondsRequest request;
  request.mutable_vi()->set_name(session_name);
  for (double delay : delays) {
    request.add_delays(delay);
  }
  nifake_grpc::AcceptListOfDurationsInSecondsResponse response;
  ::grpc::Status status = service.AcceptListOfDurationsInSeconds(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_BoolArrayOutputFunction_CallsBoolArrayOutputFunction)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  ViBoolean an_array[] = {VI_FALSE, VI_TRUE, VI_TRUE};
  EXPECT_CALL(*library, BoolArrayOutputFunction(kTestViSession, number_of_elements, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(an_array, an_array + number_of_elements),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::BoolArrayOutputFunctionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(number_of_elements);
  nifake_grpc::BoolArrayOutputFunctionResponse response;
  ::grpc::Status status = service.BoolArrayOutputFunction(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  bool expected_response_booleans[] = {false, true, true};
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(response.an_array_size(), number_of_elements);
  EXPECT_THAT(response.an_array(), ElementsAreArray(expected_response_booleans, number_of_elements));
}

TEST(NiFakeServiceTests, NiFakeService_BoolArrayInputFunction_CallsBoolArrayInputFunction)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  ViBoolean expected_array[] = {VI_FALSE, VI_TRUE, VI_TRUE};
  EXPECT_CALL(*library, BoolArrayInputFunction(kTestViSession, number_of_elements, _))
      .With(Args<2, 1>(ElementsAreArray(expected_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::BoolArrayInputFunctionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(number_of_elements);
  request.add_an_array(false);
  request.add_an_array(true);
  request.add_an_array(true);
  nifake_grpc::BoolArrayInputFunctionResponse response;
  ::grpc::Status status = service.BoolArrayInputFunction(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_DoubleAllTheNums_CallsDoubleAllTheNums)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const double numbers[] = {1, 2, 3, 4, 5};
  std::int32_t expected_size = 5;
  EXPECT_CALL(*library, DoubleAllTheNums(kTestViSession, expected_size, _))
      .With(Args<2, 1>(ElementsAreArray(numbers)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::DoubleAllTheNumsRequest request;
  request.mutable_vi()->set_name(session_name);
  for (double number : numbers) {
    request.add_numbers(number);
  }
  nifake_grpc::DoubleAllTheNumsResponse response;
  ::grpc::Status status = service.DoubleAllTheNums(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_GetAStringOfFixedMaximumSize_CallsGetAStringOfFixedMaximumSize)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  char output_string[256] = "Hello World!";
  EXPECT_CALL(*library, GetAStringOfFixedMaximumSize(kTestViSession, _))
      .WillOnce(DoAll(
          SetArrayArgument<1>(output_string, output_string + 256),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAStringOfFixedMaximumSizeRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAStringOfFixedMaximumSizeResponse response;
  ::grpc::Status status = service.GetAStringOfFixedMaximumSize(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_STREQ(output_string, response.a_string().c_str());
}

TEST(NiFakeServiceTests, NiFakeService_GetCustomTypeArray_CallsGetCustomTypeArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  std::vector<CustomStruct> cs(number_of_elements);
  EXPECT_CALL(*library, GetCustomTypeArray(kTestViSession, number_of_elements, _))
      .WillOnce(DoAll(SetArgPointee<2>(*(cs.data())), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetCustomTypeArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(3);
  nifake_grpc::GetCustomTypeArrayResponse response;
  ::grpc::Status status = service.GetCustomTypeArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(response.cs_size(), cs.size());
}

TEST(NiFakeServiceTests, NiFakeService_ImportAttributeConfigurationBuffer_CallsImportAttributeConfigurationBuffer)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::int8_t char_array[] = {'a', 'b', 'c'};
  std::int32_t expected_size = 3;
  EXPECT_CALL(*library, ImportAttributeConfigurationBuffer(kTestViSession, expected_size, _))
      .With(Args<2, 1>(ElementsAreArray(char_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ImportAttributeConfigurationBufferRequest request;
  request.mutable_vi()->set_name(session_name);
  for (std::int8_t character : char_array) {
    request.mutable_configuration()->push_back(character);
  }
  nifake_grpc::ImportAttributeConfigurationBufferResponse response;
  ::grpc::Status status = service.ImportAttributeConfigurationBuffer(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

template <typename TRequest>
TRequest create_linked_array_request(
    std::string session_name,
    const std::vector<double>& values1,
    const std::vector<double>& values2,
    const std::vector<double>& values3,
    const std::vector<double>& values4)
{
  auto request = TRequest{};
  request.mutable_vi()->set_name(session_name);
  request.mutable_values1()->CopyFrom({values1.cbegin(), values1.cend()});
  request.mutable_values2()->CopyFrom({values2.cbegin(), values2.cend()});
  request.mutable_values3()->CopyFrom({values3.cbegin(), values3.cend()});
  request.mutable_values4()->CopyFrom({values4.cbegin(), values4.cend()});
  return request;
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSize_CallsMultipleArraysSameSize)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> doubles = {0.2, -2.3, 4.5};
  const auto expected_size = static_cast<std::int32_t>(doubles.size());
  EXPECT_CALL(*library, MultipleArraysSameSize(kTestViSession, _, _, _, _, expected_size))
      .With(AllOf(
          Args<1, 5>(ElementsAreArray(doubles.data(), expected_size)),
          Args<2, 5>(ElementsAreArray(doubles.data(), expected_size)),
          Args<3, 5>(ElementsAreArray(doubles.data(), expected_size)),
          Args<4, 5>(ElementsAreArray(doubles.data(), expected_size))))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  auto request = create_linked_array_request<MultipleArraysSameSizeRequest>(session_name, doubles, doubles, doubles, doubles);
  nifake_grpc::MultipleArraysSameSizeResponse response;
  ::grpc::Status status = service.MultipleArraysSameSize(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSize_OneArrayDifferentSizeFails)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> doubles = {0.2, -2.3, 4.5};
  EXPECT_CALL(*library, MultipleArraysSameSize)
      .Times(0);

  ::grpc::ServerContext context;
  const auto request = create_linked_array_request<MultipleArraysSameSizeRequest>(session_name, doubles, {doubles.begin() + 1, doubles.end()}, doubles, doubles);
  nifake_grpc::MultipleArraysSameSizeResponse response;
  ::grpc::Status status = service.MultipleArraysSameSize(&context, &request, &response);

  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSize_OneArrayWithZeroSizeFails)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> doubles = {0.2, -2.3, 4.5};
  EXPECT_CALL(*library, MultipleArraysSameSize)
      .Times(0);

  ::grpc::ServerContext context;
  const auto request = create_linked_array_request<MultipleArraysSameSizeRequest>(session_name, {}, doubles, doubles, doubles);
  nifake_grpc::MultipleArraysSameSizeResponse response;
  ::grpc::Status status = service.MultipleArraysSameSize(&context, &request, &response);

  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
}

FakeCustomStruct create_custom_struct(pb::int32 struct_int, double struct_double)
{
  auto custom_struct = FakeCustomStruct{};
  custom_struct.set_struct_int(struct_int);
  custom_struct.set_struct_double(struct_double);
  return custom_struct;
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSizeWithOptionals_OneArrayWithZeroSizePassesNull)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const auto doubles = std::vector<double>{0.2, -2.3, 4.5};
  const auto fake_structs = std::vector<FakeCustomStruct>{
      create_custom_struct(1, 3.2),
      create_custom_struct(0, 10.0),
      create_custom_struct(100, 0.)};
  const auto expected_size = static_cast<std::int32_t>(doubles.size());
  EXPECT_CALL(*library, MultipleArraysSameSizeWithOptional(kTestViSession, _, _, _, nullptr, _, expected_size))
      .With(AllOf(
          Args<1, 6>(ElementsAreArray(doubles.data(), expected_size)),
          Args<2, 6>(ElementsAreArray(doubles.data(), expected_size)),
          Args<3, 6>(ElementsAreArray(doubles.data(), expected_size)),
          Args<5, 6>(ElementsAreArray(fake_structs.data(), expected_size))))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  auto request = create_linked_array_request<MultipleArraysSameSizeWithOptionalRequest>(session_name, doubles, doubles, doubles, {});
  request.mutable_values5()->CopyFrom({fake_structs.cbegin(), fake_structs.cend()});
  nifake_grpc::MultipleArraysSameSizeWithOptionalResponse response;
  ::grpc::Status status = service.MultipleArraysSameSizeWithOptional(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSizeWithOptionals_TwoZeroSizeArraysPassesNull)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> doubles = {0.2, -2.3, 4.5};
  const auto expected_size = static_cast<std::int32_t>(doubles.size());
  EXPECT_CALL(*library, MultipleArraysSameSizeWithOptional(kTestViSession, _, nullptr, nullptr, _, nullptr, expected_size))
      .With(AllOf(
          Args<1, 6>(ElementsAreArray(doubles.data(), expected_size)),
          Args<4, 6>(ElementsAreArray(doubles.data(), expected_size))))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  const auto request = create_linked_array_request<MultipleArraysSameSizeWithOptionalRequest>(session_name, doubles, {}, {}, doubles);
  nifake_grpc::MultipleArraysSameSizeWithOptionalResponse response;
  ::grpc::Status status = service.MultipleArraysSameSizeWithOptional(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSizeWithOptionals_DifferentNonZeroSizesFails)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> doubles = {1.2, 2.3, 4.5, 6};
  const auto expected_size = static_cast<std::int32_t>(doubles.size());
  EXPECT_CALL(*library, MultipleArraysSameSize)
      .Times(0);

  ::grpc::ServerContext context;
  const auto request = create_linked_array_request<MultipleArraysSameSizeWithOptionalRequest>(session_name, {}, doubles, {}, {doubles.begin() + 1, doubles.end()});
  nifake_grpc::MultipleArraysSameSizeWithOptionalResponse response;
  ::grpc::Status status = service.MultipleArraysSameSizeWithOptional(&context, &request, &response);

  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
}

TEST(NiFakeServiceTests, NiFakeService_MultipleArraysSameSizeWithOptionals_AllEmptyArraysPassesEmpty)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const std::vector<double> empty_doubles = {};
  const auto expected_size = static_cast<std::int32_t>(empty_doubles.size());
  EXPECT_CALL(*library, MultipleArraysSameSizeWithOptional(kTestViSession, _, _, _, _, nullptr, expected_size))
      .With(AllOf(
          Args<1, 6>(ElementsAreArray(empty_doubles.data(), expected_size)),
          Args<2, 6>(ElementsAreArray(empty_doubles.data(), expected_size)),
          Args<3, 6>(ElementsAreArray(empty_doubles.data(), expected_size)),
          Args<4, 6>(ElementsAreArray(empty_doubles.data(), expected_size))))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  const auto request = create_linked_array_request<MultipleArraysSameSizeWithOptionalRequest>(session_name, empty_doubles, empty_doubles, empty_doubles, empty_doubles);
  nifake_grpc::MultipleArraysSameSizeWithOptionalResponse response;
  ::grpc::Status status = service.MultipleArraysSameSizeWithOptional(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_ParametersAreMultipleTypes_CallsParametersAreMultipleTypes)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  std::int32_t an_int_32 = 35;
  std::int64_t an_int_64 = 42;
  nifake_grpc::Turtle an_int_enum = nifake_grpc::Turtle::TURTLE_MICHELANGELO;
  double a_float = 4.2;
  nifake_grpc::FloatEnum a_float_enum = nifake_grpc::FloatEnum::FLOAT_ENUM_SIX_POINT_FIVE;
  float expected_float_enum_value = 6.5;
  std::int32_t expected_string_size = 12;
  char a_string[] = "Hello There!";
  EXPECT_CALL(
      *library,
      ParametersAreMultipleTypes(
          kTestViSession,
          a_boolean,
          an_int_32,
          an_int_64,
          an_int_enum,
          a_float,
          expected_float_enum_value,
          StrEq(a_string)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ParametersAreMultipleTypesRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_boolean(a_boolean);
  request.set_an_int32(an_int_32);
  request.set_an_int64(an_int_64);
  request.set_an_int_enum(an_int_enum);
  request.set_a_float(a_float);
  request.set_a_float_enum_mapped(a_float_enum);
  request.set_a_string(a_string);
  nifake_grpc::ParametersAreMultipleTypesResponse response;
  ::grpc::Status status = service.ParametersAreMultipleTypes(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_ParametersAreMultipleTypesWithRawValues_CallsParametersAreMultipleTypes)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  std::int32_t an_int_32 = 35;
  std::int64_t an_int_64 = 42;
  nifake_grpc::Turtle an_int_enum = nifake_grpc::Turtle::TURTLE_MICHELANGELO;
  double a_float = 4.2;
  float expected_float_enum_value = 6.5;
  std::int32_t expected_string_size = 12;
  char a_string[] = "Hello There!";
  EXPECT_CALL(
      *library,
      ParametersAreMultipleTypes(
          kTestViSession,
          a_boolean,
          an_int_32,
          an_int_64,
          an_int_enum,
          a_float,
          expected_float_enum_value,
          StrEq(a_string)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ParametersAreMultipleTypesRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_boolean(a_boolean);
  request.set_an_int32(an_int_32);
  request.set_an_int64(an_int_64);
  request.set_an_int_enum_raw(an_int_enum);
  request.set_a_float(a_float);
  request.set_a_float_enum_raw(expected_float_enum_value);
  request.set_a_string(a_string);
  nifake_grpc::ParametersAreMultipleTypesResponse response;
  ::grpc::Status status = service.ParametersAreMultipleTypes(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_ParametersAreMultipleTypesWithRawValuesNotInEnum_CallsParametersAreMultipleTypes)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  bool a_boolean = true;
  std::int32_t an_int_32 = 35;
  std::int64_t an_int_64 = 42;
  std::int32_t expected_int_enum_value = 5;  // value not in enum
  double a_float = 4.2;
  float expected_float_enum_value = 8.5;  // value not in enum
  std::int32_t expected_string_size = 12;
  char a_string[] = "Hello There!";
  EXPECT_CALL(
      *library,
      ParametersAreMultipleTypes(
          kTestViSession,
          a_boolean,
          an_int_32,
          an_int_64,
          expected_int_enum_value,
          a_float,
          expected_float_enum_value,
          StrEq(a_string)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ParametersAreMultipleTypesRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_boolean(a_boolean);
  request.set_an_int32(an_int_32);
  request.set_an_int64(an_int_64);
  request.set_an_int_enum_raw(expected_int_enum_value);
  request.set_a_float(a_float);
  request.set_a_float_enum_raw(expected_float_enum_value);
  request.set_a_string(a_string);
  nifake_grpc::ParametersAreMultipleTypesResponse response;
  ::grpc::Status status = service.ParametersAreMultipleTypes(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_ReturnANumberAndAString_CallsReturnANumberAndAString)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int16_t a_number = 42;
  char a_string[256] = "Hello World!";
  EXPECT_CALL(*library, ReturnANumberAndAString(kTestViSession, _, _))
      .WillOnce(DoAll(
          SetArgPointee<1>(a_number),
          SetArrayArgument<2>(a_string, a_string + 256),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::ReturnANumberAndAStringRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::ReturnANumberAndAStringResponse response;
  ::grpc::Status status = service.ReturnANumberAndAString(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_number, response.a_number());
  EXPECT_STREQ(a_string, response.a_string().c_str());
}

TEST(NiFakeServiceTests, NiFakeService_ReturnListOfDurationsInSeconds_CallsReturnListOfDurationsInSeconds)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  ViReal64 timedeltas[] = {1.0, 2, -3.0};
  EXPECT_CALL(*library, ReturnListOfDurationsInSeconds(kTestViSession, number_of_elements, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(timedeltas, timedeltas + number_of_elements),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::ReturnListOfDurationsInSecondsRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(3);
  nifake_grpc::ReturnListOfDurationsInSecondsResponse response;
  ::grpc::Status status = service.ReturnListOfDurationsInSeconds(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  double expected_response_doubles[] = {1.0, 2, -3.0};
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(response.timedeltas_size(), number_of_elements);
  EXPECT_THAT(response.timedeltas(), ElementsAreArray(expected_response_doubles, number_of_elements));
}

TEST(NiFakeServiceTests, NiFakeService_ReturnMultipleTypes_CallsReturnMultipleTypes)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 array_size = 3;
  ViBoolean a_boolean = false;
  ViInt32 an_int32 = 4;
  ViInt64 an_int64 = 5;
  ViInt16 an_int_enum = nifake_grpc::Turtle::TURTLE_MICHELANGELO;
  ViReal64 a_float = 7.2;
  ViReal64 a_float_enum = 6.5f;
  ViReal64 an_array[] = {1.0, 2, -3.0};
  char a_string[] = "Hello!";
  ViInt32 string_size = sizeof(a_string);
  // ivi-dance call
  EXPECT_CALL(*library, ReturnMultipleTypes(kTestViSession, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, 0, nullptr, 0, nullptr))
      .WillOnce(Return(string_size));
  EXPECT_CALL(*library, ReturnMultipleTypes(kTestViSession, _, _, _, _, _, _, array_size, _, string_size, _))
      .WillOnce(DoAll(
          SetArgPointee<1>(a_boolean),
          SetArgPointee<2>(an_int32),
          SetArgPointee<3>(an_int64),
          SetArgPointee<4>(an_int_enum),
          SetArgPointee<5>(a_float),
          SetArgPointee<6>(a_float_enum),
          SetArrayArgument<8>(an_array, an_array + array_size),
          SetArrayArgument<10>(a_string, a_string + string_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::ReturnMultipleTypesRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_array_size(3);
  nifake_grpc::ReturnMultipleTypesResponse response;
  ::grpc::Status status = service.ReturnMultipleTypes(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_boolean, response.a_boolean());
  EXPECT_EQ(an_int32, response.an_int32());
  EXPECT_EQ(an_int64, response.an_int64());
  EXPECT_EQ(an_int_enum, response.an_int_enum());
  EXPECT_EQ(an_int_enum, response.an_int_enum_raw());
  EXPECT_EQ(a_float, response.a_float());
  EXPECT_EQ(nifake_grpc::FloatEnum::FLOAT_ENUM_SIX_POINT_FIVE, response.a_float_enum_mapped());
  EXPECT_EQ(a_float_enum, response.a_float_enum_raw());
  EXPECT_THAT(response.an_array(), ElementsAreArray(an_array, array_size));
  EXPECT_STREQ(response.a_string().c_str(), a_string);
  EXPECT_EQ(response.a_string().length(), string_size - 1);
}

TEST(NiFakeServiceTests, NiFakeService_WriteWaveform_CallsWriteWaveform)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViReal64 waveforms[] = {53.4, 42, -120.3};
  std::int32_t expected_number_of_samples = 3;
  EXPECT_CALL(*library, WriteWaveform(kTestViSession, expected_number_of_samples, _))
      .With(Args<2, 1>(ElementsAreArray(waveforms)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::WriteWaveformRequest request;
  request.mutable_vi()->set_name(session_name);
  for (double waveform : waveforms) {
    request.add_waveform(waveform);
  }
  nifake_grpc::WriteWaveformResponse response;
  ::grpc::Status status = service.WriteWaveform(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_FetchWaveform_CallsFetchWaveform)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 request_number_of_samples = 4;
  ViReal64 actual_doubles[] = {53.4, 42, -120.3};
  ViInt32 actual_number_of_samples = 3;
  EXPECT_CALL(*library, FetchWaveform(kTestViSession, request_number_of_samples, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(actual_doubles, actual_doubles + actual_number_of_samples),
          SetArgPointee<3>(actual_number_of_samples),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::FetchWaveformRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_samples(request_number_of_samples);
  nifake_grpc::FetchWaveformResponse response;
  ::grpc::Status status = service.FetchWaveform(&context, &request, &response);

  double expected_response_doubles[] = {actual_doubles[0], actual_doubles[1], actual_doubles[2], 0.0};
  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(response.actual_number_of_samples(), actual_number_of_samples);
  EXPECT_EQ(response.waveform_data_size(), request_number_of_samples);
  EXPECT_THAT(response.waveform_data(), ElementsAreArray(expected_response_doubles, request_number_of_samples));
}

// Non-int enum Tests
TEST(NiFakeServiceTests, NiFakeService_StringValuedEnumInputFunctionWithDefaultsWithInvalidEnumInput_ReturnsInvalidArgument)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::MobileOSNames a_mobile_o_s_name = nifake_grpc::MOBILE_OS_NAMES_UNSPECIFIED;
  EXPECT_CALL(*library, StringValuedEnumInputFunctionWithDefaults)
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::StringValuedEnumInputFunctionWithDefaultsRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_mobile_os_name_mapped(a_mobile_o_s_name);
  nifake_grpc::StringValuedEnumInputFunctionWithDefaultsResponse response;
  ::grpc::Status status = service.StringValuedEnumInputFunctionWithDefaults(&context, &request, &response);

  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
  EXPECT_EQ(NULL, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_StringValuedEnumInputFunctionWithDefaultsWithValidEnumInput_CallsStringValuedEnumInputFunctionWithDefaults)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::MobileOSNames a_mobile_o_s_name = nifake_grpc::MOBILE_OS_NAMES_ANDROID;
  const char* expected_enum_value = NIFAKE_VAL_ANDROID;
  EXPECT_CALL(*library, StringValuedEnumInputFunctionWithDefaults(kTestViSession, Pointee(*expected_enum_value)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::StringValuedEnumInputFunctionWithDefaultsRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_mobile_os_name_mapped(a_mobile_o_s_name);
  nifake_grpc::StringValuedEnumInputFunctionWithDefaultsResponse response;
  ::grpc::Status status = service.StringValuedEnumInputFunctionWithDefaults(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

// Array methods using ivi-dance mechanism
TEST(NiFakeServiceTests, NiFakeService_ExportAttributeConfigurationBuffer_CallsExportAttributeConfigurationBuffer)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt8 config_buffer[] = {'A', 'B', 'C'};
  ViInt32 expected_size = 3;
  // ivi-dance call
  EXPECT_CALL(*library, ExportAttributeConfigurationBuffer(kTestViSession, 0, nullptr))
      .WillOnce(Return(expected_size));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, ExportAttributeConfigurationBuffer(kTestViSession, expected_size, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(config_buffer, config_buffer + expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::ExportAttributeConfigurationBufferRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::ExportAttributeConfigurationBufferResponse response;
  ::grpc::Status status = service.ExportAttributeConfigurationBuffer(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.configuration(), ElementsAreArray(config_buffer, expected_size));
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceCharArray_CallsGetAnIviDanceCharArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViChar char_array[] = {'H', 'E', 'L', 'L', 'O', '\0'};
  ViInt32 expected_size = sizeof(char_array);
  // ivi-dance call
  EXPECT_CALL(*library, GetAnIviDanceCharArray(kTestViSession, 0, nullptr))
      .WillOnce(Return(expected_size));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, GetAnIviDanceCharArray(kTestViSession, expected_size, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(char_array, char_array + expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceCharArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAnIviDanceCharArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceCharArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_STREQ(response.char_array().c_str(), char_array);
  EXPECT_EQ(response.char_array().length(), expected_size - 1);
}

TEST(NiFakeServiceTests, NiFakeService_GetArrayUsingIviDance_CallsGetArrayUsingIviDance)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViReal64 doubles[] = {53.4, 42, -120.3};
  ViInt32 expected_size = 3;
  // ivi-dance call
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, 0, nullptr))
      .WillOnce(Return(expected_size));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, expected_size, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(doubles, doubles + expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetArrayUsingIviDanceRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetArrayUsingIviDanceResponse response;
  ::grpc::Status status = service.GetArrayUsingIviDance(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(doubles, expected_size));
}

TEST(NiFakeServiceTests, NiFakeService_GetArrayUsingIviDanceWithChangingSizesByReturnValue_CallsGetArrayUsingIviDance)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViReal64 doubles[] = {53.4, 42, -120.3};
  ViInt32 expected_old_size = 2;
  ViInt32 expected_new_size = 3;
  // ivi-dance call
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, 0, nullptr))
      .WillOnce(Return(expected_old_size))
      .WillOnce(Return(expected_new_size));
  // follow up call - return that the array now needs to be bigger, so the ivi-dance
  // call will be made again.
  ::testing::Expectation first_real_call = EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, expected_old_size, _))
                                               .WillOnce(Return(expected_new_size));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, expected_new_size, _))
      .After(first_real_call)
      .WillOnce(DoAll(
          SetArrayArgument<2>(doubles, doubles + expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetArrayUsingIviDanceRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetArrayUsingIviDanceResponse response;
  ::grpc::Status status = service.GetArrayUsingIviDance(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(doubles, expected_new_size));
}

TEST(NiFakeServiceTests, NiFakeService_GetArrayUsingIviDanceWithChangingSizesByError_CallsGetArrayUsingIviDance)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViReal64 doubles[] = {53.4, 42, -120.3};
  ViInt32 expected_old_size = 2;
  ViInt32 expected_new_size = 3;
  // ivi-dance call
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, 0, nullptr))
      .WillOnce(Return(expected_old_size))
      .WillOnce(Return(expected_new_size));
  // follow up call - return that the array now needs to be bigger, so the ivi-dance
  // call will be made again.
  // Use the value of the error here to ensure that it doesn't change.
  ::testing::Expectation first_real_call = EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, expected_old_size, _))
                                               .WillOnce(Return(-200229));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, GetArrayUsingIviDance(kTestViSession, expected_new_size, _))
      .After(first_real_call)
      .WillOnce(DoAll(
          SetArrayArgument<2>(doubles, doubles + expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetArrayUsingIviDanceRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetArrayUsingIviDanceResponse response;
  ::grpc::Status status = service.GetArrayUsingIviDance(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(doubles, expected_new_size));
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViString_CallsGetAttributeViString)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attributeId = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE;
  ViChar attribute_char_array[] = {'H', 'E', 'L', 'L', 'O', '\0'};
  ViInt32 expected_size = sizeof(attribute_char_array);
  // ivi-dance call
  EXPECT_CALL(*library, GetAttributeViString(kTestViSession, Pointee(*kTestChannelName), attributeId, 0, nullptr))
      .WillOnce(Return(expected_size));
  // follow up call with size returned from ivi-dance setup.
  EXPECT_CALL(*library, GetAttributeViString(kTestViSession, Pointee(*kTestChannelName), attributeId, expected_size, _))
      .WillOnce(DoAll(
          SetArrayArgument<4>(attribute_char_array, attribute_char_array + expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViStringRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_channel_name(kTestChannelName);
  request.set_attribute_id(attributeId);
  nifake_grpc::GetAttributeViStringResponse response;
  ::grpc::Status status = service.GetAttributeViString(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_STREQ(response.attribute_value().c_str(), attribute_char_array);
  EXPECT_EQ(response.attribute_value().length(), expected_size - 1);
}

TEST(NiFakeServiceTests, NiFakeService_GetViUInt8_CallsGetViUInt8)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViUInt8 a_ViUInt8_number = 0xFF;
  EXPECT_CALL(*library, GetViUInt8(kTestViSession, _))
      .WillOnce(DoAll(SetArgPointee<1>(a_ViUInt8_number), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetViUInt8Request request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetViUInt8Response response;
  ::grpc::Status status = service.GetViUInt8(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(a_ViUInt8_number, response.a_uint8_number());
}

TEST(NiFakeServiceTests, NiFakeService_ViUInt8ArrayInputFunction_CallsViUInt8ArrayInputFunction)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  ViUInt8 expected_array[] = {0, 127, 0xFF};
  EXPECT_CALL(*library, ViUInt8ArrayInputFunction(kTestViSession, number_of_elements, _))
      .With(Args<2, 1>(ElementsAreArray(expected_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ViUInt8ArrayInputFunctionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(number_of_elements);
  std::string input_array;
  input_array.push_back(0);
  input_array.push_back(127);
  input_array.push_back(static_cast<char>(0xFF));
  request.set_an_array(input_array);
  nifake_grpc::ViUInt8ArrayInputFunctionResponse response;
  ::grpc::Status status = service.ViUInt8ArrayInputFunction(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_ViUInt8ArrayOutputFunction_CallsViUInt8ArrayOutputFunction)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 3;
  ViUInt8 an_array[] = {0, 127, 0xFF};
  EXPECT_CALL(*library, ViUInt8ArrayOutputFunction(kTestViSession, number_of_elements, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(an_array, an_array + number_of_elements),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::ViUInt8ArrayOutputFunctionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_number_of_elements(number_of_elements);
  nifake_grpc::ViUInt8ArrayOutputFunctionResponse response;
  ::grpc::Status status = service.ViUInt8ArrayOutputFunction(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(response.an_array().size(), number_of_elements);
  EXPECT_THAT(response.an_array(), ElementsAreArray(an_array, number_of_elements));
}

TEST(NiFakeServiceTests, NiFakeService_AcceptViUInt32Array_CallsAcceptViUInt32Array)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::uint32_t uint32_array[] = {0, 1, 0xFFFFFFFD, 0xFFFFFFFE, 0xFFFFFFFF};
  std::int32_t array_len = 5;
  EXPECT_CALL(*library, AcceptViUInt32Array(kTestViSession, array_len, _))
      .With(Args<2, 1>(ElementsAreArray(uint32_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::AcceptViUInt32ArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.mutable_u_int32_array()->CopyFrom(google::protobuf::RepeatedField<google::protobuf::uint32>(uint32_array, uint32_array + 5));
  nifake_grpc::AcceptViUInt32ArrayResponse response;
  ::grpc::Status status = service.AcceptViUInt32Array(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_GetViInt32Array_CallsGetViInt32Array)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  int array_len = 4;
  std::int32_t int32_array[] = {-2147483646, -2147483645, 2147483646, 2147483647};
  EXPECT_CALL(*library, GetViInt32Array(kTestViSession, array_len, _))
      .WillOnce(DoAll(SetArrayArgument<2>(int32_array, int32_array + array_len), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetViInt32ArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_array_len(array_len);
  nifake_grpc::GetViInt32ArrayResponse response;
  ::grpc::Status status = service.GetViInt32Array(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.int32_array(), ElementsAreArray(int32_array, array_len));
}

TEST(NiFakeServiceTests, NiFakeService_GetViUInt32Array_CallsGetViUInt32Array)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  int array_len = 4;
  std::uint32_t uint32_array[] = {0, 1, 0xFFFFFFFE, 0xFFFFFFFF};
  EXPECT_CALL(*library, GetViUInt32Array(kTestViSession, array_len, _))
      .WillOnce(DoAll(SetArrayArgument<2>(uint32_array, uint32_array + array_len), Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetViUInt32ArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_array_len(array_len);
  nifake_grpc::GetViUInt32ArrayResponse response;
  ::grpc::Status status = service.GetViUInt32Array(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.u_int32_array(), ElementsAreArray(uint32_array, array_len));
}

TEST(NiFakeServiceTests, NiFakeService_AcceptViSessionArray_CallsAcceptViSessionArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  std::array<std::uint32_t, 3> vi_session_array{12345671, 12345672, 12345673};
  auto session_name1 = create_session(library, service, vi_session_array[0]);
  auto session_name2 = create_session(library, service, vi_session_array[1]);
  auto session_name3 = create_session(library, service, vi_session_array[2]);

  std::uint32_t session_count = 3;
  EXPECT_CALL(*library, AcceptViSessionArray(session_count, _))
      .With(Args<1, 0>(ElementsAreArray(vi_session_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::AcceptViSessionArrayRequest request;
  request.set_session_count(session_count);
  request.add_session_array()->set_name(session_name1);
  request.add_session_array()->set_name(session_name2);
  request.add_session_array()->set_name(session_name3);
  nifake_grpc::AcceptViSessionArrayResponse response;
  ::grpc::Status status = service.AcceptViSessionArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

MATCHER_P2(MatchesArray, array, array_size, "")
{
  for (int i = 0; i < array_size; i++) {
    if (arg[i] != array[i]) {
      return false;
    }
  }
  return true;
}

// Test for two-dimension mechanism to ensure we validate size correctly
TEST(NiFakeServiceTests, NiFakeService_UseTwoDimensionWithCorrectSize_CallsUseATwoDimensionParameter)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 array[] = {1, 2, 2, 3, 3, 3};
  ViInt32 array_lengths[] = {1, 2, 3};
  ViInt32 array_size = 3;
  // two-dimension call
  EXPECT_CALL(*library, UseATwoDimensionParameter(kTestViSession, MatchesArray(array, 6), _, array_size))
      .With(Args<2, 3>(ElementsAreArray(array_lengths)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::UseATwoDimensionParameterRequest request;
  request.mutable_vi()->set_name(session_name);
  for (int arrayval : array) {
    request.add_array(arrayval);
  }
  for (int length : array_lengths) {
    request.add_array_lengths(length);
  }
  nifake_grpc::UseATwoDimensionParameterResponse response;
  ::grpc::Status status = service.UseATwoDimensionParameter(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

// Test for two-dimension mechanism failure when the sum of array sizes of the two dimensional array don't match the actual size
TEST(NiFakeServiceTests, NiFakeService_UseTwoDimensionWithIncorrectSize_FailsUseATwoDimensionParameter)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 array[] = {1, 2, 2, 3, 3, 3};
  ViInt32 array_lengths[] = {2, 5, 6};

  EXPECT_CALL(*library, UseATwoDimensionParameter(kTestViSession, _, _, _))
      .Times(0);

  ::grpc::ServerContext context;
  nifake_grpc::UseATwoDimensionParameterRequest request;
  request.mutable_vi()->set_name(session_name);
  for (int arrayval : array) {
    request.add_array(arrayval);
  }
  for (int length : array_lengths) {
    request.add_array_lengths(length);
  }
  nifake_grpc::UseATwoDimensionParameterResponse response;
  ::grpc::Status status = service.UseATwoDimensionParameter(&context, &request, &response);

  EXPECT_FALSE(status.ok());
  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
  EXPECT_THAT(status.error_message(), HasSubstr("The total size of the two-dimensional array"));
}

// Test for ivi-dance-with-a-twist mechanism
TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArray_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* a_string = "abc";
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_size = 3;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_size),
          Return(kDriverSuccess)));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_size, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_size),
          SetArgPointee<4>(expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_string(a_string);
  nifake_grpc::GetAnIviDanceWithATwistArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_size));
  EXPECT_EQ(response.actual_size(), expected_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayWithWarning_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* a_string = "abc";
  const auto data_in = std::array<ViInt32, 4>{0, -1, 100, 5};
  ViInt32 input_size = 2;
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_size = 3;

  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_size),
          Return(kDriverSuccess)));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_size, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_size),
          SetArgPointee<4>(expected_size),
          Return(kDriverWarning)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_string(a_string);
  nifake_grpc::GetAnIviDanceWithATwistArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverWarning, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_size));
  EXPECT_EQ(response.actual_size(), expected_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayWithInputArray_PassesArrayInputOnFirstPass_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const auto data_in = std::array<ViInt32, 4>{0, -1, 100, 5};
  ViInt32 input_size = 2;
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_size = 3;
  // ivi-dance-with-a-twist call: ensure that data and size are passed in.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayWithInputArray(_, _, 0, nullptr, _))
      .With(Args<0, 1>(ElementsAreArray(data_in)))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_size),
          Return(kDriverSuccess)));
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayWithInputArray(_, _, expected_size, _, _))
      .With(Args<0, 1>(ElementsAreArray(data_in)))
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_size),
          SetArgPointee<4>(expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayWithInputArrayRequest request;
  request.mutable_data_in()->CopyFrom({data_in.begin(), data_in.end()});
  nifake_grpc::GetAnIviDanceWithATwistArrayWithInputArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArrayWithInputArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_size));
  EXPECT_EQ(response.actual_size(), expected_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayWithBiggerSizes_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* a_string = "abc";
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_old_size = 2;
  ViInt32 expected_new_size = 3;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_old_size),
          Return(kDriverSuccess)))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_new_size),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be bigger, so the ivi-dance
  // call will be made again.
  // Use the value of the error here to ensure that it doesn't change.
  ::testing::Expectation first_real_call = EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_old_size, _, _))
                                               .WillOnce(Return(-200229));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_new_size, _, _))
      .After(first_real_call)
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_new_size),
          SetArgPointee<4>(expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_string(a_string);
  nifake_grpc::GetAnIviDanceWithATwistArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_new_size));
  EXPECT_EQ(response.actual_size(), expected_new_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayWithSmallerSizes_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* a_string = "abc";
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_old_size = 3;
  ViInt32 expected_new_size = 2;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_old_size),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be smaller.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_old_size, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_new_size),
          SetArgPointee<4>(expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_string(a_string);
  nifake_grpc::GetAnIviDanceWithATwistArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_new_size));
  EXPECT_EQ(response.actual_size(), expected_new_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistByteArrayWithSmallerSizes_CallsGetAnIviDanceWithATwistByteArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const auto DATA = std::vector<char>{'a', 'b'};
  const auto NEW_SIZE = static_cast<ViInt32>(DATA.size());
  const auto OLD_SIZE = NEW_SIZE + 1;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistByteArray(0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<2>(OLD_SIZE),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be smaller.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistByteArray(OLD_SIZE, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<1>(DATA.cbegin(), DATA.cend()),
          SetArgPointee<2>(NEW_SIZE),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistByteArrayRequest request;
  nifake_grpc::GetAnIviDanceWithATwistByteArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistByteArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(
      DATA,
      std::vector<char>(response.array_out().cbegin(), response.array_out().cend()));
  EXPECT_EQ(response.actual_size(), NEW_SIZE);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistStringWithSmallerSizes_CallsGetAnIviDanceWithATwistString)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const auto DATA = std::string("ab");
  // +1 to include null terminator.
  const auto NEW_SIZE = static_cast<ViInt32>(DATA.size() + 1);
  const auto OLD_SIZE = NEW_SIZE + 1;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistString(kTestViSession, 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<3>(OLD_SIZE),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be smaller.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistString(kTestViSession, OLD_SIZE, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(DATA.c_str(), DATA.c_str() + NEW_SIZE),
          SetArgPointee<3>(NEW_SIZE),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistStringRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAnIviDanceWithATwistStringResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistString(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(DATA, response.a_string());
  EXPECT_EQ(response.actual_size(), NEW_SIZE);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistStrlenBug_ReturnsCorrectString)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const auto DATA = std::string("abcdef");
  // Oops forgot the +1!
  const auto SIZE = static_cast<ViInt32>(DATA.size());
  EXPECT_CALL(*library, GetAnIviDanceWithATwistStringStrlenBug(0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<2>(SIZE),
          Return(kDriverSuccess)));
  EXPECT_CALL(*library, GetAnIviDanceWithATwistStringStrlenBug(SIZE, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<1>(DATA.c_str(), DATA.c_str() + SIZE + 1),
          SetArgPointee<2>(SIZE),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistStringStrlenBugRequest request;
  nifake_grpc::GetAnIviDanceWithATwistStringStrlenBugResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistStringStrlenBug(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(DATA, response.string_out());
  EXPECT_EQ(response.actual_size(), SIZE);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistStrlenBugIsFixed_ReturnsCorrectString)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  const auto DATA = std::string("abcdef");
  // Someone fixed the bug to add the null terminator!
  const auto SIZE = static_cast<ViInt32>(DATA.size() + 1);
  EXPECT_CALL(*library, GetAnIviDanceWithATwistStringStrlenBug(0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<2>(SIZE),
          Return(kDriverSuccess)));
  EXPECT_CALL(*library, GetAnIviDanceWithATwistStringStrlenBug(SIZE, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<1>(DATA.c_str(), DATA.c_str() + SIZE + 1),
          SetArgPointee<2>(SIZE),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistStringStrlenBugRequest request;
  nifake_grpc::GetAnIviDanceWithATwistStringStrlenBugResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistStringStrlenBug(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(DATA, response.string_out());
  EXPECT_EQ(response.actual_size(), SIZE);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayWithChangingSizesAndWarning_CallsGetAnIviDanceWithATwistArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const char* a_string = "abc";
  ViInt32 array_out[] = {1, 2, 3};
  ViInt32 expected_old_size = 2;
  ViInt32 expected_new_size = 3;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_old_size),
          Return(kDriverSuccess)))
      .WillOnce(DoAll(
          SetArgPointee<4>(expected_new_size),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be bigger, so the ivi-dance
  // call will be made again.
  // Use the value of the warning here to ensure that it doesn't change.
  ::testing::Expectation first_real_call = EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_old_size, _, _))
                                               .WillOnce(Return(200026));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArray(kTestViSession, Pointee(*a_string), expected_new_size, _, _))
      .After(first_real_call)
      .WillOnce(DoAll(
          SetArrayArgument<3>(array_out, array_out + expected_new_size),
          SetArgPointee<4>(expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_a_string(a_string);
  nifake_grpc::GetAnIviDanceWithATwistArrayResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_new_size));
  EXPECT_EQ(response.actual_size(), expected_new_size);
}

// Test for ivi-dance-with-a-twist mechanism
TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayOfCustomType_CallsGetAnIviDanceWithATwistArrayOfCustomType)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  CustomStruct array_out[] = {{-1, -2.0}, {0, 0.5}, {70000, 32768.0}};
  ViInt32 expected_size = 3;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<3>(expected_size),
          Return(kDriverSuccess)));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, expected_size, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(array_out, array_out + expected_size),
          SetArgPointee<3>(expected_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArrayOfCustomType(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_size));
  EXPECT_EQ(response.actual_size(), expected_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayOfCustomTypeWithBiggerSizes_CallsGetAnIviDanceWithATwistArrayOfCustomType)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  CustomStruct array_out[] = {{-1, -2.0}, {0, 0.5}, {70000, 32768.0}};
  ViInt32 expected_old_size = 2;
  ViInt32 expected_new_size = 3;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<3>(expected_old_size),
          Return(kDriverSuccess)))
      .WillOnce(DoAll(
          SetArgPointee<3>(expected_new_size),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be bigger, so the ivi-dance
  // call will be made again.
  // Use the value of the error here to ensure that it doesn't change.
  ::testing::Expectation first_real_call = EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, expected_old_size, _, _))
                                               .WillOnce(Return(-200229));
  // follow up call with size returned from ivi-dance-with-a-twist setup.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, expected_new_size, _, _))
      .After(first_real_call)
      .WillOnce(DoAll(
          SetArrayArgument<2>(array_out, array_out + expected_new_size),
          SetArgPointee<3>(expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArrayOfCustomType(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_new_size));
  EXPECT_EQ(response.actual_size(), expected_new_size);
}

TEST(NiFakeServiceTests, NiFakeService_GetAnIviDanceWithATwistArrayOfCustomTypeWithSmallerSizes_CallsGetAnIviDanceWithATwistArrayOfCustomType)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  CustomStruct array_out[] = {{-1, -2.0}, {0, 0.5}};
  ViInt32 expected_old_size = 3;
  ViInt32 expected_new_size = 2;
  // ivi-dance-with-a-twist call
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, 0, nullptr, _))
      .WillOnce(DoAll(
          SetArgPointee<3>(expected_old_size),
          Return(kDriverSuccess)));
  // follow up call - return that the array now needs to be smaller.
  EXPECT_CALL(*library, GetAnIviDanceWithATwistArrayOfCustomType(kTestViSession, expected_old_size, _, _))
      .WillOnce(DoAll(
          SetArrayArgument<2>(array_out, array_out + expected_new_size),
          SetArgPointee<3>(expected_new_size),
          Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::GetAnIviDanceWithATwistArrayOfCustomTypeResponse response;
  ::grpc::Status status = service.GetAnIviDanceWithATwistArrayOfCustomType(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(array_out, expected_new_size));
  EXPECT_EQ(response.actual_size(), expected_new_size);
}

TEST(NiFakeServiceTests, NiFakeService_AcceptViInt16Array_CallsAcceptViInt16Array)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  std::int16_t int16_array[] = {0, 1, -0x8000, 0x7FFF};
  std::int32_t array_len = 4;
  EXPECT_CALL(*library, ViInt16ArrayInputFunction(kTestViSession, array_len, _))
      .With(Args<2, 1>(ElementsAreArray(int16_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::ViInt16ArrayInputFunctionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.mutable_an_array()->CopyFrom(google::protobuf::RepeatedField<google::protobuf::int32>(int16_array, int16_array + 4));
  nifake_grpc::ViInt16ArrayInputFunctionResponse response;
  ::grpc::Status status = service.ViInt16ArrayInputFunction(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_SetCustomTypeArray_CallsSetCustomTypeArray)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  ViInt32 number_of_elements = 2;
  CustomStruct cs_array[] = {{5, 8.0}, {15, 19.7}};
  EXPECT_CALL(*library, SetCustomTypeArray(kTestViSession, number_of_elements, _))
      .With(Args<2, 1>(ElementsAreArray(cs_array)))
      .WillOnce(Return(kDriverSuccess));

  ::grpc::ServerContext context;
  nifake_grpc::SetCustomTypeArrayRequest request;
  request.mutable_vi()->set_name(session_name);
  for (int i = 0; i < number_of_elements; i++) {
    request.add_cs();
    request.mutable_cs(i)->set_struct_int(cs_array[i].structInt);
    request.mutable_cs(i)->set_struct_double(cs_array[i].structDouble);
  }
  nifake_grpc::SetCustomTypeArrayResponse response;
  ::grpc::Status status = service.SetCustomTypeArray(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_GetArrayViUInt8WithEnum_CallsGetArrayViUInt8WithEnum)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  int array_len = 3;
  ViUInt8 uint8_array[] = {
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_RED,
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_BLACK,
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_BLUE,
  };
  nifake_grpc::GrpcColorOverride enum_array[] = {
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_RED,
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_BLACK,
      nifake_grpc::GrpcColorOverride::GRPC_COLOR_OVERRIDE_BLUE,
  };
  EXPECT_CALL(*library, GetArrayViUInt8WithEnum(kTestViSession, array_len, _))
      .WillOnce(
          DoAll(
              SetArrayArgument<2>(uint8_array, uint8_array + array_len),
              Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetArrayViUInt8WithEnumRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_array_len(array_len);
  nifake_grpc::GetArrayViUInt8WithEnumResponse response;
  ::grpc::Status status = service.GetArrayViUInt8WithEnum(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_THAT(response.u_int8_enum_array(), ElementsAreArray(enum_array, array_len));
  EXPECT_EQ(std::string(uint8_array, uint8_array + array_len), response.u_int8_enum_array_raw());
}

TEST(NiFakeServiceTests, NiFakeService_GetAttributeViSession_ReturnsSessionId)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  nifake_grpc::NiFakeAttribute attribute_id = nifake_grpc::NIFAKE_ATTRIBUTE_READ_WRITE_STRING;
  EXPECT_CALL(*library, GetAttributeViSession(kTestViSession, Pointee(*kTestChannelName), attribute_id, _))
      .WillOnce(
          DoAll(
              SetArgPointee<3>(kTestViSession),
              Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::GetAttributeViSessionRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_attribute_id(attribute_id);
  request.set_channel_name(kTestChannelName);
  nifake_grpc::GetAttributeViSessionResponse response;
  auto status = service.GetAttributeViSession(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(session_name, response.attribute_value().name());
}

TEST(NiFakeServiceTests, NiFakeExtensionService_CallMethodWithSesionStartedByNIFakeService_PassesThroughSession)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto extension_library = std::make_shared<NiFakeExtensionMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  nifake_extension_grpc::NiFakeExtensionService extension_service(extension_library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  const ViInt32 kParam = 1234;
  EXPECT_CALL(*extension_library, AddCoolFunctionality(kTestViSession, kParam))
      .WillOnce(
          DoAll(
              Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_extension_grpc::AddCoolFunctionalityRequest request;
  request.mutable_vi()->set_name(session_name);
  request.set_param(kParam);
  nifake_extension_grpc::AddCoolFunctionalityResponse response;
  auto status = extension_service.AddCoolFunctionality(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST(NiFakeServiceTests, NiFakeService_CallMethodWithReservedPassNullParam_PassesNull)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<NiFakeMockLibrary>();
  auto resource_repository = std::make_shared<FakeResourceRepository>(session_repository);
  nifake_grpc::NiFakeService service(library, resource_repository);
  auto session_name = create_session(library, service, kTestViSession);
  EXPECT_CALL(*library, CommandWithReservedParam(kTestViSession, nullptr))
      .WillOnce(
          DoAll(
              Return(kDriverSuccess)));

  ::grpc::ServerContext context;
  nifake_grpc::CommandWithReservedParamRequest request;
  request.mutable_vi()->set_name(session_name);
  nifake_grpc::CommandWithReservedParamResponse response;
  auto status = service.CommandWithReservedParam(&context, &request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kDriverSuccess, response.status());
}

struct FakeServiceHolder {
  FakeServiceHolder()
      : session_repository(std::make_shared<nidevice_grpc::SessionRepository>()),
        library(std::make_shared<NiFakeMockLibrary>()),
        resource_repository(std::make_shared<FakeResourceRepository>(session_repository)),
        service(library, resource_repository)
  {
  }
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository;
  std::shared_ptr<NiFakeMockLibrary> library;
  std::shared_ptr<FakeResourceRepository> resource_repository;
  nifake_grpc::NiFakeService service;
  grpc::ServerContext context;
};

// "In/Out" ivi-dance-with-a-twist is when the "value_twist" output is also the "value" input,
// I.e., it's a single in/out param instead of a separate input and output.
TEST(NiFakeServiceTests, FakeService_ReadDataWithInOutIviTwist_DoesTwistAndReturnsCorrectData)
{
  const auto BUFFER_SIZE = 10;
  ::google::protobuf::int32 DATA[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  FakeServiceHolder service_holder;
  // First call expects pointer-to-zero and sets the size.
  EXPECT_CALL(*service_holder.library, ReadDataWithInOutIviTwist(nullptr, Pointee(0)))
      .WillOnce(
          DoAll(
              SetArgPointee<1>(BUFFER_SIZE),
              Return(kDriverSuccess)));
  // Second call expects pointer-to-size and sets the output data.
  EXPECT_CALL(*service_holder.library, ReadDataWithInOutIviTwist(_, Pointee(BUFFER_SIZE)))
      .WillOnce(
          DoAll(
              SetArrayArgument<0>(DATA, DATA + BUFFER_SIZE),
              Return(kDriverSuccess)));

  auto request = ReadDataWithInOutIviTwistRequest{};
  auto response = ReadDataWithInOutIviTwistResponse{};
  service_holder.service.ReadDataWithInOutIviTwist(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_THAT(response.data(), ElementsAreArray(DATA, BUFFER_SIZE));
}

TEST(NiFakeServiceTests, FakeService_ReadDataWithMultipleIviTwistParamSets_DoesTwistAndReturnsCorrectData)
{
  const auto DATA = std::vector<::google::protobuf::int32>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  const auto OTHER_DATA = std::vector<::google::protobuf::int32>{100, 200, 300, 400};
  FakeServiceHolder service_holder;
  // First call expects pointer-to-zero and sets the size.
  EXPECT_CALL(*service_holder.library, ReadDataWithMultipleIviTwistParamSets(0, nullptr, _, 0, nullptr, _))
      .WillOnce(
          DoAll(
              SetArgPointee<2>(DATA.size()),
              SetArgPointee<5>(OTHER_DATA.size()),
              Return(kDriverSuccess)));
  // Second call expects pointer-to-size and sets the output data.
  EXPECT_CALL(*service_holder.library, ReadDataWithMultipleIviTwistParamSets(static_cast<ViInt32>(DATA.size()), _, _, static_cast<ViInt32>(OTHER_DATA.size()), _, _))
      .WillOnce(
          DoAll(
              SetArrayArgument<1>(DATA.cbegin(), DATA.cend()),
              SetArrayArgument<4>(OTHER_DATA.cbegin(), OTHER_DATA.cend()),
              Return(kDriverSuccess)));

  auto request = ReadDataWithMultipleIviTwistParamSetsRequest{};
  auto response = ReadDataWithMultipleIviTwistParamSetsResponse{};
  service_holder.service.ReadDataWithMultipleIviTwistParamSets(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_THAT(response.array_out(), ElementsAreArray(DATA.data(), DATA.size()));
  EXPECT_THAT(response.other_array_out(), ElementsAreArray(OTHER_DATA.data(), OTHER_DATA.size()));
}

TEST(NiFakeServiceTests, FakeService_CreateConfigurationList_PassesAttributeArray)
{
  const auto ATTRIBUTES = std::vector<NiFakeAttribute>{NiFakeAttribute::NIFAKE_ATTRIBUTE_READ_WRITE_BOOL, NiFakeAttribute::NIFAKE_ATTRIBUTE_READ_WRITE_COLOR};
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, CreateConfigurationList(_, _))
      .With(Args<1, 0>(ElementsAreArray(ATTRIBUTES.data(), ATTRIBUTES.size())))
      .WillOnce(Return(kDriverSuccess));

  auto request = CreateConfigurationListRequest{};
  request.mutable_list_attribute_ids()->CopyFrom({ATTRIBUTES.cbegin(), ATTRIBUTES.cend()});
  auto response = CreateConfigurationListResponse{};
  service_holder.service.CreateConfigurationList(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
}

TEST(NiFakeServiceTests, FakeService_GetCustomStruct_ReturnsCustomStruct)
{
  auto EXPECTED = CustomStruct{};
  EXPECTED.structDouble = 1.234;
  EXPECTED.structInt = 9999;
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, GetCustomType(_, _))
      .WillOnce(DoAll(SetArgPointee<1>(EXPECTED), Return(kDriverSuccess)));

  auto request = GetCustomTypeRequest{};
  auto response = GetCustomTypeResponse{};
  service_holder.service.GetCustomType(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_EQ(response.cs(), EXPECTED);
}

TEST(NiFakeServiceTests, FakeService_GetCustomStructWithWarning_ReturnsCustomStruct)
{
  auto EXPECTED = CustomStruct{};
  EXPECTED.structDouble = 1.234;
  EXPECTED.structInt = 9999;
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, GetCustomType(_, _))
      .WillOnce(DoAll(SetArgPointee<1>(EXPECTED), Return(kDriverWarning)));

  auto request = GetCustomTypeRequest{};
  auto response = GetCustomTypeResponse{};
  service_holder.service.GetCustomType(&service_holder.context, &request, &response);

  EXPECT_EQ(kDriverWarning, response.status());
  EXPECT_EQ(response.cs(), EXPECTED);
}

TEST(NiFakeServiceTests, FakeService_SetCustomStruct_PassesCustomStruct)
{
  auto EXPECTED = nifake_grpc::FakeCustomStruct{};
  EXPECTED.set_struct_double(1e6);
  EXPECTED.set_struct_int(500);
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, SetCustomType(_, Eq(EXPECTED)))
      .WillOnce(Return(kDriverSuccess));

  auto request = SetCustomTypeRequest{};
  request.mutable_cs()->CopyFrom(EXPECTED);
  auto response = SetCustomTypeResponse{};
  service_holder.service.SetCustomType(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
}

TEST(NiFakeServiceTests, FakeService_CustomNestedStructRoundtrip_PassesAndReceivesStruct)
{
  auto EXPECTED_INPUT = nifake_grpc::CustomStructNestedTypedef{};
  auto NESTED_CUSTOM_STRUCT = nifake_grpc::FakeCustomStruct();
  NESTED_CUSTOM_STRUCT.set_struct_double(1e6);
  NESTED_CUSTOM_STRUCT.set_struct_int(500);
  auto NESTED_CUSTOM_STRUCT_TYPEDEF = nifake_grpc::CustomStructTypedef();
  NESTED_CUSTOM_STRUCT_TYPEDEF.set_struct_double(2e6);
  NESTED_CUSTOM_STRUCT_TYPEDEF.set_struct_int(600);
  EXPECTED_INPUT.mutable_struct_custom_struct()->CopyFrom(NESTED_CUSTOM_STRUCT);
  EXPECTED_INPUT.mutable_struct_custom_struct_typedef()->CopyFrom(NESTED_CUSTOM_STRUCT_TYPEDEF);
  auto EXPECTED_OUTPUT = CustomStructNestedTypedef_struct{};
  EXPECTED_OUTPUT.structCustomStruct.structDouble = 1e6;
  EXPECTED_OUTPUT.structCustomStruct.structInt = 500;
  EXPECTED_OUTPUT.structCustomStructTypedef.structDouble = 2e6;
  EXPECTED_OUTPUT.structCustomStructTypedef.structInt = 600;
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, CustomNestedStructRoundtrip(Eq(EXPECTED_INPUT), _))
      .WillOnce(DoAll(SetArgPointee<1>(EXPECTED_OUTPUT), Return(kDriverSuccess)));

  auto request = CustomNestedStructRoundtripRequest{};
  request.mutable_nested_custom_type_in()->CopyFrom(EXPECTED_INPUT);
  auto response = CustomNestedStructRoundtripResponse{};
  service_holder.service.CustomNestedStructRoundtrip(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_EQ(response.nested_custom_type_out(), EXPECTED_OUTPUT);
}

TEST(NiFakeServiceTests, GetBitfieldAsEnumArray_ZeroBitfield_ReturnsEmptyArray)
{
  constexpr auto ZERO_BITFIELD = 0x0;
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, GetBitfieldAsEnumArray(_))
      .WillOnce(
          DoAll(
              SetArgPointee<0>(ZERO_BITFIELD),
              Return(kDriverSuccess)));
  auto request = GetBitfieldAsEnumArrayRequest{};
  auto response = GetBitfieldAsEnumArrayResponse{};
  service_holder.service.GetBitfieldAsEnumArray(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_THAT(response.flags_array(), IsEmpty());
  EXPECT_EQ(ZERO_BITFIELD, response.flags_raw());
}

TEST(NiFakeServiceTests, GetBitfieldAsEnumArray_MultipleFlagsSet_ReturnsArrayOfFlags)
{
  constexpr google::protobuf::int64 A_AND_C = 0x1ULL | 0x4ULL;
  const auto EXPECTED = std::vector<Bitfield>{Bitfield::BITFIELD_FLAG_A, Bitfield::BITFIELD_FLAG_C};
  FakeServiceHolder service_holder;
  EXPECT_CALL(*service_holder.library, GetBitfieldAsEnumArray(_))
      .WillOnce(
          DoAll(
              SetArgPointee<0>(A_AND_C),
              Return(kDriverSuccess)));
  auto request = GetBitfieldAsEnumArrayRequest{};
  auto response = GetBitfieldAsEnumArrayResponse{};
  service_holder.service.GetBitfieldAsEnumArray(&service_holder.context, &request, &response);

  EXPECT_EQ(0, response.status());
  EXPECT_THAT(
      response.flags_array(),
      ElementsAre(Bitfield::BITFIELD_FLAG_A, Bitfield::BITFIELD_FLAG_C));
  EXPECT_EQ(A_AND_C, response.flags_raw());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/nimxlc_terminal_adaptor_converters_tests.cpp sha256=044a54350c3640b23488aa26fd3e5b7593b9872ad09a238b6c3e4cf1c1cba05e bytes=2274 -->
## FILE: source/tests/unit/nimxlc_terminal_adaptor_converters_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/nimxlc_terminal_adaptor_converters_tests.cpp`
- sha256: `044a54350c3640b23488aa26fd3e5b7593b9872ad09a238b6c3e4cf1c1cba05e`
- bytes: 2274

````cpp
#include <custom/nimxlcterminaladaptor_restricted_converters.h>
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nimxlcterminaladaptor_restricted/nimxlcterminaladaptor_restricted_mock_library.h>

#include <algorithm>
#include <numeric>
#include <string>
#include <iostream>

using namespace nimxlcterminaladaptor_restricted_grpc;
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

namespace ni {
namespace tests {
namespace unit {
namespace {

const std::string description = "test&%_string[";
const std::string encoded_description = "test%26%25_string%5b";

class MockServerContext {
 public:
  MOCK_METHOD2(AddTrailingMetadata, void(const std::string& key, const std::string& value));
};

void initialize_status(nierr_Status *status, int32_t code, std::string description)
{
  status->code = code;
  status->reallocJson(status, static_cast<uint32_t>(description.length() + JSONZ_TERMINATOR_SIZE));
  strcpy(status->json, description.c_str());
}

TEST(nimxlcterminaladaptor_restricted_tests, nierr_StatusFatal_ConvertToGrpc_TrailingMetadataIsAdded)
{
  int32_t errorCode = -12345;
  MockServerContext serverContext;
  NIErrStatusOutputConverter<MockServerContext> status(&serverContext);
  initialize_status(&status, errorCode, description);

  nimxlcterminaladaptor_restricted_grpc::NIErrStatus output;
  EXPECT_CALL(serverContext, AddTrailingMetadata("ni-error", std::to_string(errorCode)));
  EXPECT_CALL(serverContext, AddTrailingMetadata("ni-error-json", encoded_description));
  status.to_grpc(output);

  EXPECT_EQ(errorCode, output.code());
  EXPECT_EQ(std::string(), output.json());
}

TEST(nimxlcterminaladaptor_restricted_tests, nierr_StatusNotFatal_ConvertToGrpc_JsonAddedToStatus)
{
  int32_t errorCode = 12345;
  MockServerContext serverContext;
  NIErrStatusOutputConverter<MockServerContext> status(&serverContext);
  initialize_status(&status, errorCode, description);

  nimxlcterminaladaptor_restricted_grpc::NIErrStatus output;
  status.to_grpc(output);

  EXPECT_EQ(errorCode, output.code());
  EXPECT_EQ(encoded_description, output.json());
}

}  // namespace
}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/precision_timestamp_converter_tests.cpp sha256=ad9dff467e0c3bd4c287a2b1732dd83448a0281f828cddb123d8c549a8ea70b8 bytes=5794 -->
## FILE: source/tests/unit/precision_timestamp_converter_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/precision_timestamp_converter_tests.cpp`
- sha256: `ad9dff467e0c3bd4c287a2b1732dd83448a0281f828cddb123d8c549a8ea70b8`
- bytes: 5794

````cpp
#include <gtest/gtest.h>
#include <cstdint>
#include <limits>
#include <server/converters.h>

namespace ni {
namespace tests {
namespace unit {
namespace {

using nidevice_grpc::converters::convert_dot_net_ticks_to_precision_timestamp;
using nidevice_grpc::converters::DotNetTicksPerSecond;
using nidevice_grpc::converters::TwoToSixtyFour;
using nidevice_grpc::converters::SecondsFromDotNet0001EpochToCVI1904Epoch;
using ::ni::protobuf::types::PrecisionTimestamp;

const int64 EpochTicks = SecondsFromDotNet0001EpochToCVI1904Epoch * DotNetTicksPerSecond;

TEST(PrecisionTimestampConverterTests, ConvertZeroTicks_ReturnsNegativeEpochTimestamp)
{
  PrecisionTimestamp timestamp;  
  convert_dot_net_ticks_to_precision_timestamp(0, &timestamp);
  
  EXPECT_EQ(timestamp.seconds(), -SecondsFromDotNet0001EpochToCVI1904Epoch);
  EXPECT_EQ(timestamp.fractional_seconds(), 0);
}

TEST(PrecisionTimestampConverterTests, ConvertEpochTicks_ReturnsZeroTimestamp)
{
  PrecisionTimestamp timestamp;  
  convert_dot_net_ticks_to_precision_timestamp(EpochTicks, &timestamp);
  
  EXPECT_EQ(timestamp.seconds(), 0);
  EXPECT_EQ(timestamp.fractional_seconds(), 0);
}

TEST(PrecisionTimestampConverterTests, ConvertOneSecondOfTicks_ReturnsOneSecond)
{
  PrecisionTimestamp timestamp;  
  const int64_t one_second_ticks = EpochTicks + 1 * DotNetTicksPerSecond;
  convert_dot_net_ticks_to_precision_timestamp(one_second_ticks, &timestamp);
  
  EXPECT_EQ(timestamp.seconds(), 1);
  EXPECT_EQ(timestamp.fractional_seconds(), 0);
}

// Parameterized test for seconds and fractional combinations
struct SecondsAndFractionalTestParam {
  int64_t ticks_offset;
  int64_t seconds;
  uint64_t btf_fractional_ticks;
};

class PrecisionTimestampConverterSecondsAndFractionalTests : public ::testing::TestWithParam<SecondsAndFractionalTestParam> {};

TEST_P(PrecisionTimestampConverterSecondsAndFractionalTests, ConvertSecondsAndFractional_ReturnsCorrectValues)
{
  const auto& param = GetParam();
  PrecisionTimestamp timestamp;
  convert_dot_net_ticks_to_precision_timestamp(EpochTicks + param.ticks_offset, &timestamp);

  EXPECT_EQ(timestamp.seconds(), param.seconds) << "Failed for ticks_offset: " << param.ticks_offset;
  EXPECT_EQ(timestamp.fractional_seconds(), param.btf_fractional_ticks) << "Failed for ticks_offset: " << param.ticks_offset;
}

INSTANTIATE_TEST_SUITE_P(
  SecondsAndFractionalTests,
  PrecisionTimestampConverterSecondsAndFractionalTests,
  ::testing::Values(
    SecondsAndFractionalTestParam{  0000000,  0, 0x0000000000000000ULL},
    SecondsAndFractionalTestParam{  2500000,  0, 0x4000000000000000ULL},
    SecondsAndFractionalTestParam{  5000000,  0, 0x8000000000000000ULL},
    SecondsAndFractionalTestParam{  7500000,  0, 0xC000000000000000ULL},
    SecondsAndFractionalTestParam{  9999999,  0, 0xFFFFFE5280D65800ULL},
    SecondsAndFractionalTestParam{ 12500000,  1, 0x4000000000000000ULL},
    SecondsAndFractionalTestParam{ 25000000,  2, 0x8000000000000000ULL},
    SecondsAndFractionalTestParam{ 37500000,  3, 0xC000000000000000ULL},
    SecondsAndFractionalTestParam{ -2500000, -0, 0x4000000000000000ULL},
    SecondsAndFractionalTestParam{ -5000000, -0, 0x8000000000000000ULL},
    SecondsAndFractionalTestParam{ -7500000, -0, 0xC000000000000000ULL},
    SecondsAndFractionalTestParam{ -9999999, -0, 0xFFFFFE5280D65800ULL},
    SecondsAndFractionalTestParam{-12500000, -1, 0x4000000000000000ULL},
    SecondsAndFractionalTestParam{-25000000, -2, 0x8000000000000000ULL},
    SecondsAndFractionalTestParam{-37500000, -3, 0xC000000000000000ULL}
  )
);

// Parameterized test for large timestamps across different years
struct LargeTimestampTestParam {
  int year;
  int64_t days_from_1904_epoch;
  std::string description;
};

class PrecisionTimestampConverterLargeTimestampTests : public ::testing::TestWithParam<LargeTimestampTestParam> {};

TEST_P(PrecisionTimestampConverterLargeTimestampTests, ConvertLargeTimestamp_HandlesCorrectly)
{
  const auto& param = GetParam();
  PrecisionTimestamp timestamp;
  const int64 SecondsFromNiBtfEpochToYear = param.days_from_1904_epoch * 24 * 60 * 60;
  const int64 YearTicks = EpochTicks + SecondsFromNiBtfEpochToYear * DotNetTicksPerSecond;
  
  convert_dot_net_ticks_to_precision_timestamp(YearTicks + DotNetTicksPerSecond / 4, &timestamp);
  
  if (SecondsFromNiBtfEpochToYear < 0) {
    EXPECT_EQ(timestamp.seconds(), SecondsFromNiBtfEpochToYear + 1) << "Failed for " << param.description;
    EXPECT_EQ(timestamp.fractional_seconds(), static_cast<uint64_t>(0.75 * TwoToSixtyFour)) << "Failed for " << param.description;
  } else {
    EXPECT_EQ(timestamp.seconds(), SecondsFromNiBtfEpochToYear) << "Failed for " << param.description;
    EXPECT_EQ(timestamp.fractional_seconds(), static_cast<uint64_t>(0.25 * TwoToSixtyFour)) << "Failed for " << param.description;
  }
}

INSTANTIATE_TEST_SUITE_P(
  LargeTimestampTests,
  PrecisionTimestampConverterLargeTimestampTests,
  ::testing::Values(
    LargeTimestampTestParam{2025, 44196, "January 1, 2025"},  // 121 years from 1904 = 44196 days (accounting for leap years)
    LargeTimestampTestParam{2002, 35794, "January 1, 2002"},  // 98 years from 1904 = 35794 days (accounting for leap years)
    LargeTimestampTestParam{1950, 16801, "January 1, 1950"},  // 46 years from 1904 = 16801 days (accounting for leap years)
    LargeTimestampTestParam{1850, -19723, "January 1, 1850"}, // 54 years before 1904 = -19723 days (accounting for leap years)
    LargeTimestampTestParam{1066, -306022, "January 1, 1066"} // 838 years before 1904 = -306022 days (accounting for leap years)
  )
);

}  // namespace
}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/server_configuration_parser_tests.cpp sha256=e418237505f501d4e13880411d5f50a311f4bf177b7d94fbe6d4fce58fab023a bytes=27581 -->
## FILE: source/tests/unit/server_configuration_parser_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/server_configuration_parser_tests.cpp`
- sha256: `e418237505f501d4e13880411d5f50a311f4bf177b7d94fbe6d4fce58fab023a`
- bytes: 27581

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/server_configuration_parser.h>

#include <typeinfo>

namespace ni {
namespace tests {
namespace unit {

using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;
using FeatureState = nidevice_grpc::FeatureToggles::FeatureState;

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromDefaultConfigFile_ParseAddress_ReturnsDefaultLocalAddressAndPort)
{
  nidevice_grpc::ServerConfigurationParser server_config_parser;

  auto address = server_config_parser.parse_address();

  EXPECT_EQ(address, "[::1]:31763");
}

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromPathToDefaultConfigFile_ParseAddress_NotEmpty)
{
  std::string config_file_path = nidevice_grpc::ServerConfigurationParser::get_exe_path() + "server_config.json";
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_file_path);

  auto address = server_config_parser.parse_address();

  EXPECT_FALSE(address.empty());
}

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromPathToLocalhostConfigFile_ParseAddress_ReturnsLocalhostAddressAndPort)
{
  std::string config_file_path = nidevice_grpc::ServerConfigurationParser::get_exe_path() + "test_localhost_config.json";
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_file_path);

  auto address = server_config_parser.parse_address();

  EXPECT_EQ(address, "[::1]:0");
}

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromPathToMutualTlsConfigFile_ParseAllSecurityKeys_NoneEmpty)
{
  std::string config_file_path = nidevice_grpc::ServerConfigurationParser::get_exe_path() + "test_mutual_tls_config.json";
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_file_path);

  auto server_key = server_config_parser.parse_server_key();
  auto server_cert = server_config_parser.parse_server_cert();
  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_FALSE(server_key.empty());
  EXPECT_FALSE(server_cert.empty());
  EXPECT_FALSE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromMissingConfigFile_ThrowsConfigFileNotFoundException)
{
  std::string missing_file_path = "fake.json";
  try {
    nidevice_grpc::ServerConfigurationParser server_config_parser(missing_file_path);

    FAIL() << "ConfigFileNotFoundException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::ConfigFileNotFoundException& ex) {
    EXPECT_EQ(nidevice_grpc::kConfigFileNotFoundMessage + std::string(missing_file_path), ex.what());
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithIntegerAddress_ParseAddress_ThrowsWrongAddressTypeException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "address": 0, "port": 0 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();

    FAIL() << "WrongAddressTypeException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::WrongAddressTypeException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kWrongAddressTypeMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithEmptyAddress_ParseAddress_ThrowsInvalidAddressException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "address": "", "port": 0 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();

    FAIL() << "InvalidAddressException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::InvalidAddressException& ex) {
    EXPECT_EQ(std::string(nidevice_grpc::kInvalidAddressMessage), ex.what());
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithNoAddress_ParseAddress_DefaultsToLoopback)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "port": 50051 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto address = server_config_parser.parse_address();

  EXPECT_EQ(address, "[::1]:50051");
}

TEST(ServerConfigurationParserTests, JsonConfigWithExplicitAllInterfacesAddress_ParseAddress_ReturnsAllInterfaces)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "address": "[::]", "port": 50051 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto address = server_config_parser.parse_address();

  EXPECT_EQ(address, "[::]:50051");
}

TEST(ServerConfigurationParserTests, JsonConfigWithNegativePortNumber_ParseAddress_ThrowsInvalidPortException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "port": -1 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();

    FAIL() << "InvalidPortException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::InvalidPortException& ex) {
    EXPECT_EQ(std::string(nidevice_grpc::kInvalidPortMessage), ex.what());
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithPortNumberExceedingMax_ParseAddress_ThrowsInvalidPortException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "port": 65536 })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();

    FAIL() << "InvalidPortException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::InvalidPortException& ex) {
    EXPECT_EQ(std::string(nidevice_grpc::kInvalidPortMessage), ex.what());
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithPortAsString_ParseAddress_ThrowsWrongPortTypeException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "port" : "9090" })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();

    FAIL() << "WrongPortTypeException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::WrongPortTypeException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kWrongPortTypeMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithoutPortKey_ParseAddress_ThrowsUnspecifiedPortException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({ "foo" : "bar" })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_address();
    FAIL() << "UnspecifiedPortException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::UnspecifiedPortException& ex) {
    EXPECT_EQ(std::string(nidevice_grpc::kUnspecifiedPortMessage), ex.what());
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithServerSideTls_ParseServerCert_NotEmpty)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
  {
    "security" : {
        "server_cert": "test_server_self_signed_crt.pem",
        "server_key": "test_server_privatekey.pem",
        "root_cert": ""
    }
  })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto server_cert = server_config_parser.parse_server_cert();

  EXPECT_FALSE(server_cert.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithServerSideTls_ParseServerKey_NotEmpty)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
  {
    "security" : {
        "server_cert": "test_server_self_signed_crt.pem",
        "server_key": "test_server_privatekey.pem",
        "root_cert": ""
    }
  })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto server_key = server_config_parser.parse_server_key();

  EXPECT_FALSE(server_key.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithServerSideTls_ParseRootCert_Empty)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
  {
    "security" : {
        "server_cert": "test_server_self_signed_crt.pem",
        "server_key": "test_server_privatekey.pem",
        "root_cert": ""
    }
  })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_TRUE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithMutualTls_ParseAllSecurityKeys_NoneEmpty)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_cert": "test_server_self_signed_crt.pem",
          "server_key": "test_server_privatekey.pem",
          "root_cert": "test_client_self_signed_crt.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto server_key = server_config_parser.parse_server_key();
  auto server_cert = server_config_parser.parse_server_cert();
  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_FALSE(server_key.empty());
  EXPECT_FALSE(server_cert.empty());
  EXPECT_FALSE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, CreateConfigurationParserFromDefaultConfigFile_ParseAllSecurityKeys_AllEmpty)
{
  nidevice_grpc::ServerConfigurationParser server_config_parser;

  auto server_key = server_config_parser.parse_server_key();
  auto server_cert = server_config_parser.parse_server_cert();
  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_TRUE(server_key.empty());
  EXPECT_TRUE(server_cert.empty());
  EXPECT_TRUE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithServerCertAsInteger_ParseServerCert_ValueTypeNotStringException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_cert": 9,
          "server_key": "test_server_privatekey.pem",
          "root_cert": "test_client_self_signed_crt.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_server_cert();

    FAIL() << "ValueTypeNotStringException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::ValueTypeNotStringException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kValueTypeNotStringMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithServerKeyAsNull_ParseServerKey_ValueTypeNotStringException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_cert": "test_server_self_signed_crt.pem",
          "server_key": null,
          "root_cert": "test_client_self_signed_crt.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_server_key();

    FAIL() << "ValueTypeNotStringException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::ValueTypeNotStringException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kValueTypeNotStringMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithRootCertAsBoolean_ParseRootCert_ValueTypeNotStringException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_cert": "test_server_self_signed_crt.pem",
          "server_key": "test_server_privatekey.pem",
          "root_cert": true
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_root_cert();

    FAIL() << "ValueTypeNotStringException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::ValueTypeNotStringException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kValueTypeNotStringMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithValidPemFilesButWithoutSecurityParentKey_ParseAllSecurityKeys_AllEmpty)
{
  // This JSON configuration is missing the "security" parent key
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "server_cert": "test_server_self_signed_crt.pem",
      "server_key": "test_server_privatekey.pem",
      "root_cert": "test_client_self_signed_crt.pem"
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto server_key = server_config_parser.parse_server_key();
  auto server_cert = server_config_parser.parse_server_cert();
  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_TRUE(server_key.empty());
  EXPECT_TRUE(server_cert.empty());
  EXPECT_TRUE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, EmptyJsonConfig_ParseAllSecurityKeys_AllEmpty)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({})");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto server_key = server_config_parser.parse_server_key();
  auto server_cert = server_config_parser.parse_server_cert();
  auto root_cert = server_config_parser.parse_root_cert();

  EXPECT_TRUE(server_key.empty());
  EXPECT_TRUE(server_cert.empty());
  EXPECT_TRUE(root_cert.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithMissingServerCertFile_ParseServerCert_ThrowsFileNotFoundException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_cert": "missing_server_cert.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_server_cert();

    FAIL() << "FileNotFoundException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::FileNotFoundException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kFileNotFoundMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithMissingServerKeyFile_ParseServerKey_ThrowsFileNotFoundException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "server_key": "missing_server_key.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_server_key();

    FAIL() << "FileNotFoundException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::FileNotFoundException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kFileNotFoundMessage));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithMissingRootCertFile_ParseRootCert_ThrowsFileNotFoundException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "security" : {
          "root_cert": "missing_root_cert.pem"
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  try {
    auto address = server_config_parser.parse_root_cert();

    FAIL() << "FileNotFoundException not thrown";
  }
  catch (const nidevice_grpc::ServerConfigurationParser::FileNotFoundException& ex) {
    EXPECT_THAT(ex.what(), testing::HasSubstr(nidevice_grpc::kFileNotFoundMessage));
  }
}

const auto ALL_READINESS = {
    CodeReadiness::kRelease,
    CodeReadiness::kNextRelease,
    CodeReadiness::kIncomplete,
    CodeReadiness::kPrototype};

TEST(ServerConfigurationParserTests, JsonConfigWithEnabledFeature_ParseFeatureToggles_FeatureIsEnabled)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : {
        "feature": true
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto features = server_config_parser.parse_feature_toggles();

  EXPECT_EQ(FeatureState::kEnabled, features.get_feature_state("feature"));
  for (auto readiness : ALL_READINESS) {
    EXPECT_TRUE(features.is_feature_enabled("feature", readiness));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithEnabledFeature_ParseFeatureToggles_SomeOtherFeatureIsUnspecified)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : {
        "feature": true
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto features = server_config_parser.parse_feature_toggles();

  EXPECT_EQ(FeatureState::kUnspecified, features.get_feature_state("someOtherFeature"));
}

TEST(ServerConfigurationParserTests, JsonConfigWithDisabledFeature_ParseFeatureToggles_FeatureIsDisabled)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : {
        "feature": false
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto features = server_config_parser.parse_feature_toggles();

  EXPECT_EQ(FeatureState::kDisabled, features.get_feature_state("feature"));
  for (auto readiness : ALL_READINESS) {
    EXPECT_FALSE(features.is_feature_enabled("feature", readiness));
  }
}

TEST(ServerConfigurationParserTests, JsonConfigWithMultipleFeaturesWithDifferentEnabledState_ParseFeatureToggles_FeaturesAreEnabledAndDisabled)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : {
        "feature1": false,
        "feature2": true,
        "feature3": false,
        "feature4": true
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto features = server_config_parser.parse_feature_toggles();

  EXPECT_EQ(FeatureState::kDisabled, features.get_feature_state("feature1"));
  EXPECT_EQ(FeatureState::kEnabled, features.get_feature_state("feature2"));
  EXPECT_EQ(FeatureState::kDisabled, features.get_feature_state("feature3"));
  EXPECT_EQ(FeatureState::kEnabled, features.get_feature_state("feature4"));
  EXPECT_EQ(FeatureState::kUnspecified, features.get_feature_state("someOtherFeature"));
}

TEST(ServerConfigurationParserTests, JsonConfigWithInvalidFeatureToggleValue_ParseFeatureToggles_ThrowsInvalidFeatureToggleException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : {
        "feature": 12345
      }
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  EXPECT_THROW(
      {
        auto features = server_config_parser.parse_feature_toggles();
      },
      nidevice_grpc::ServerConfigurationParser::InvalidFeatureToggleException);
}

TEST(ServerConfigurationParserTests, JsonConfigWithFeatureTogglesAsArray_ParseFeatureToggles_ThrowsInvalidFeatureToggleException)
{
  nlohmann::json config_json = nlohmann::json::parse(R"(
    {
      "feature_toggles" : [ { "feature": true } ]
    })");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  EXPECT_THROW(
      {
        auto features = server_config_parser.parse_feature_toggles();
      },
      nidevice_grpc::ServerConfigurationParser::InvalidFeatureToggleException);
}

TEST(ServerConfigurationParserTests, JsonConfigWithNoFeatureToggles_ParseFeatureToggles_ReturnsValidFeatureTogglesWithCorrectDefaults)
{
  nlohmann::json config_json = nlohmann::json::parse(R"({})");
  nidevice_grpc::ServerConfigurationParser server_config_parser(config_json);

  auto features = server_config_parser.parse_feature_toggles();

  EXPECT_EQ(FeatureState::kUnspecified, features.get_feature_state("dummy_feature"));
  EXPECT_TRUE(features.is_feature_enabled("cool_release_feature", CodeReadiness::kRelease));
  EXPECT_FALSE(features.is_feature_enabled("cool_unreleased_feature", CodeReadiness::kNextRelease));
  EXPECT_FALSE(features.is_feature_enabled("enigmatic_incomplete_feature", CodeReadiness::kIncomplete));
  EXPECT_FALSE(features.is_feature_enabled("scary_prototype_feature", CodeReadiness::kPrototype));
}

TEST(ServerConfigurationParserTests, JsonConfigWithNoMaxMessageSize_ParseMaxMessageSize_MaxMessageSizeIsUnlimited)
{
  const auto config_json = nlohmann::json::parse(R"({})");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto message_size = server_config_parser.parse_max_message_size();

  EXPECT_EQ(nidevice_grpc::UNLIMITED_MAX_MESSAGE_SIZE, message_size);
}

TEST(ServerConfigurationParserTests, JsonConfigWithMaxMessageSize_ParseMaxMessageSize_MaxMessageSizeIsParsed)
{
  const auto config_json = nlohmann::json::parse(R"(
  {
    "max_message_size": 8000000
  })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto message_size = server_config_parser.parse_max_message_size();

  EXPECT_EQ(8000000, message_size);
}

TEST(ServerConfigurationParserTests, JsonConfigWithNegativeMaxMessageSize_ParseMaxMessageSize_MaxMessageSizeIsParsed)
{
  const auto config_json = nlohmann::json::parse(R"(
  {
    "max_message_size": -12345
  })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto message_size = server_config_parser.parse_max_message_size();

  EXPECT_EQ(-12345, message_size);
}

TEST(ServerConfigurationParserTests, JsonConfigWitIllFormedMaxMessageSize_ParseMaxMessageSize_ThrowsInvalidMaxMessageSizeException)
{
  const auto config_json = nlohmann::json::parse(R"(
  {
    "max_message_size": "something_else"
  })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  EXPECT_THROW(
      {
        const auto message_size = server_config_parser.parse_max_message_size();
      },
      nidevice_grpc::ServerConfigurationParser::InvalidMaxMessageSizeException);
}

using Readiness = nidevice_grpc::FeatureToggles::CodeReadiness;
using ReadinessTestPair = std::tuple<std::string, nidevice_grpc::FeatureToggles::CodeReadiness>;
class ServerConfigurationParserCodeReadinessTests
    : public ::testing::TestWithParam<ReadinessTestPair> {
};

INSTANTIATE_TEST_SUITE_P(
    CodeReadinessTestCases,
    ServerConfigurationParserCodeReadinessTests,
    ::testing::ValuesIn(std::vector<ReadinessTestPair>{
        {R"({"code_readiness": "release"})", Readiness::kRelease},
        {R"({})", Readiness::kRelease},
        {R"({"code_readiness": "NEXTRELEASE"})", Readiness::kNextRelease},
        {R"({"code_readiness": "next_release"})", Readiness::kNextRelease},
        {R"({"code_readiness": "NextRelease"})", Readiness::kNextRelease},
        {R"({"code_readiness": "Prototype"})", Readiness::kPrototype},
        {R"({"code_readiness": "prototype"})", Readiness::kPrototype},
        {R"({"code_readiness": "iNcOmPlete"})", Readiness::kIncomplete},
        {R"({"code_readiness": "RestrictedRelease"})", Readiness::kRelease},
        {R"({"code_readiness": "restricted_Release"})", Readiness::kRelease},
        {R"({"code_readiness": "restricted_next_release"})", Readiness::kNextRelease},
        {R"({"code_readiness": "RestrictedNextRelease"})", Readiness::kNextRelease},
    }));

TEST_P(ServerConfigurationParserCodeReadinessTests, CodeReadinessConfiguration_ParseCodeReadiness_ReturnsExpectedReadiness)
{
  const auto config_json = nlohmann::json::parse(std::get<0>(GetParam()));
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto readiness = server_config_parser.parse_code_readiness();

  EXPECT_EQ(std::get<1>(GetParam()), readiness);
}

TEST_P(ServerConfigurationParserCodeReadinessTests, CodeReadinessConfiguration_ParseFeatureToggles_FeatureOfCorrespondingReadinessIsEnabled)
{
  const auto config_json = nlohmann::json::parse(std::get<0>(GetParam()));
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto feature_toggles = server_config_parser.parse_feature_toggles();

  EXPECT_TRUE(feature_toggles.is_feature_enabled("some_feature", /* feature_readiness = */ std::get<1>(GetParam())));
}

class ServerConfigurationParserInvalidCodeReadinessTests
    : public ::testing::TestWithParam<std::string> {
};

INSTANTIATE_TEST_SUITE_P(
    InvalidCodeReadinessTestCases,
    ServerConfigurationParserInvalidCodeReadinessTests,
    ::testing::ValuesIn(std::vector<std::string>{
        R"({"code_readiness": 10})",
        R"({"code_readiness": "notAReadiness"})",
        R"({"code_readiness": "next-release"})",
        R"({"code_readiness": {}})"}));

TEST_P(ServerConfigurationParserInvalidCodeReadinessTests, InvalidCodeReadinessConfiguration_ParseCodeReadiness_ThrowsInvalidCodeReadinessException)
{
  const auto config_json = nlohmann::json::parse(GetParam());
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  EXPECT_THROW(
      {
        const auto feature_toggles = server_config_parser.parse_code_readiness();
      },
      nidevice_grpc::ServerConfigurationParser::InvalidCodeReadinessException);
}

TEST_P(ServerConfigurationParserInvalidCodeReadinessTests, InvalidCodeReadinessConfiguration_ParseFeatureToggles_ThrowsInvalidCodeReadinessException)
{
  const auto config_json = nlohmann::json::parse(GetParam());
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  EXPECT_THROW(
      {
        const auto feature_toggles = server_config_parser.parse_feature_toggles();
      },
      nidevice_grpc::ServerConfigurationParser::InvalidCodeReadinessException);
}

TEST(ServerConfigurationParserTests, JsonConfigWithSecurityModeString_ParseSecurityMode_ReturnsModeString)
{
  const auto config_json = nlohmann::json::parse(R"({ "port": 31763, "security": "ni-tls-config" })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto security_mode = server_config_parser.parse_security_mode();

  EXPECT_EQ("ni-tls-config", security_mode);
}

TEST(ServerConfigurationParserTests, JsonConfigWithSecurityObject_ParseSecurityMode_ReturnsEmpty)
{
  const auto config_json = nlohmann::json::parse(R"({ "port": 31763, "security": { "server_cert": "cert.pem" } })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto security_mode = server_config_parser.parse_security_mode();

  EXPECT_TRUE(security_mode.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithNoSecurityKey_ParseSecurityMode_ReturnsEmpty)
{
  const auto config_json = nlohmann::json::parse(R"({ "port": 31763 })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  const auto security_mode = server_config_parser.parse_security_mode();

  EXPECT_TRUE(security_mode.empty());
}

TEST(ServerConfigurationParserTests, JsonConfigWithSecurityModeString_ParseServerCert_ReturnsEmpty)
{
  const auto config_json = nlohmann::json::parse(R"({ "port": 31763, "security": "ni-tls-config" })");
  const auto server_config_parser = nidevice_grpc::ServerConfigurationParser(config_json);

  EXPECT_TRUE(server_config_parser.parse_server_cert().empty());
  EXPECT_TRUE(server_config_parser.parse_server_key().empty());
  EXPECT_TRUE(server_config_parser.parse_root_cert().empty());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/server_security_configuration_tests.cpp sha256=a0ccd60c4a0fed8a3d218822b0cd64cd5dc1f15b4d6367f507dc21074c1cf9ac bytes=5102 -->
## FILE: source/tests/unit/server_security_configuration_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/server_security_configuration_tests.cpp`
- sha256: `a0ccd60c4a0fed8a3d218822b0cd64cd5dc1f15b4d6367f507dc21074c1cf9ac`
- bytes: 5102

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/server_security_configuration.h>

#include <typeinfo>

namespace ni {
namespace tests {
namespace unit {

static const char* kEmptyServerCertData = "";
static const char* kEmptyServerKeyData = "";
static const char* kEmptyRootCertData = "";

std::shared_ptr<::grpc::ServerCredentials> get_secure_credentials_comparison()
{
  return ::grpc::SslServerCredentials(::grpc::SslServerCredentialsOptions());
}

std::shared_ptr<::grpc::ServerCredentials> get_insecure_credentials_comparison()
{
  return ::grpc::InsecureServerCredentials();
}

TEST(ServerSecurityConfigurationTests, DefaultServerSecurityConfiguration_GetCredentials_InsecureServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config;

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_insecure_credentials_comparison()) == typeid(*credentials));
  EXPECT_TRUE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertEmptyAndServerKeyNotEmpty_GetCredentials_InsecureServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config(kEmptyServerCertData, "server key data", kEmptyRootCertData);

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_insecure_credentials_comparison()) == typeid(*credentials));
  EXPECT_TRUE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertNotEmptyAndServerKeyEmpty_GetCredentials_InsecureServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config("server cert data", kEmptyServerKeyData, kEmptyRootCertData);

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_insecure_credentials_comparison()) == typeid(*credentials));
  EXPECT_TRUE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertAndKeyEmptyAndRootCertNotEmpty_GetCredentials_InsecureServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config(kEmptyServerCertData, kEmptyServerKeyData, "root cert data");

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_insecure_credentials_comparison()) == typeid(*credentials));
  EXPECT_TRUE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertAndKeyNotEmpty_GetCredentials_SslServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config("server cert data", "server key data", kEmptyRootCertData);

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_secure_credentials_comparison()) == typeid(*credentials));
  EXPECT_FALSE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertServerKeyAndRootCertNotEmpty_GetCredentials_SslServerCredentials)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config("server cert data", "server key data", "root cert data");

  auto credentials = server_security_config.get_credentials();

  EXPECT_TRUE(typeid(*get_secure_credentials_comparison()) == typeid(*credentials));
  EXPECT_FALSE(server_security_config.is_insecure_credentials());
}

TEST(ServerSecurityConfigurationTests, ServerCertServerKeyAndRootCertEmpty_TryGetOptions_Unsuccessful)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config(kEmptyServerCertData, kEmptyServerKeyData, kEmptyRootCertData);

  auto credentials_options = server_security_config.try_get_options();

  EXPECT_EQ(nullptr, credentials_options);
}

TEST(ServerSecurityConfigurationTests, ServerCertServerKeyAndRootCertNotEmpty_TryGetOptions_RequestsAndVerifiesClientCertificate)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config("server cert data", "server key data", "root cert data");

  auto credentials_options = server_security_config.try_get_options();

  EXPECT_NE(nullptr, credentials_options);
  EXPECT_EQ(GRPC_SSL_REQUEST_AND_REQUIRE_CLIENT_CERTIFICATE_AND_VERIFY, credentials_options->client_certificate_request);
  EXPECT_FALSE(credentials_options->pem_key_cert_pairs.empty());
  EXPECT_FALSE(credentials_options->pem_root_certs.empty());
}

TEST(ServerSecurityConfigurationTests, ServerCertAndKeyNotEmptyAndRootCertEmpty_TryGetOptions_DoesNotRequestClientCertificate)
{
  nidevice_grpc::ServerSecurityConfiguration server_security_config("server cert data", "server key data", kEmptyRootCertData);

  auto credentials_options = server_security_config.try_get_options();

  EXPECT_NE(nullptr, credentials_options);
  EXPECT_EQ(GRPC_SSL_DONT_REQUEST_CLIENT_CERTIFICATE, credentials_options->client_certificate_request);
  EXPECT_FALSE(credentials_options->pem_key_cert_pairs.empty());
  EXPECT_TRUE(credentials_options->pem_root_certs.empty());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/session_repository_tests.cpp sha256=170af78440fcb7c41dfa867b5c80cb2a380cee569d32eb325e27c67a42c5a1be bytes=7183 -->
## FILE: source/tests/unit/session_repository_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/session_repository_tests.cpp`
- sha256: `170af78440fcb7c41dfa867b5c80cb2a380cee569d32eb325e27c67a42c5a1be`
- bytes: 7183

````cpp
#include <gtest/gtest.h>
#include <server/exceptions.h>
#include <server/semaphore.h>
#include <server/session_repository.h>

namespace ni {
namespace tests {
namespace unit {

// Starting with session_name 1 isn't functionally important, but we want to start with
// something intentional. NOT an uninitialized uint.
constexpr auto EXPECTED_FIRST_SESSION_ID = 1;

TEST(SessionRepositoryTests, AddSessionWithNonZeroStatus_ReturnsStatusAndDoesNotStoreSession)
{
  nidevice_grpc::SessionRepository session_repository;
  std::string session_name = "42";
  int status = session_repository.add_session(
      session_name,
      [session_name]() { return 1; },
      NULL);

  EXPECT_EQ(status, 1);
  EXPECT_EQ("" , session_repository.access_session(session_name));
}

TEST(SessionRepositoryTests, AddSessionWithNonZeroStatus_InitializedNewSessionIsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  std::string session_name = "42";
  bool initialized_new_session;
  int status = session_repository.add_session(
      session_name,
      [session_name]() { return 1; },
      NULL,
      nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      &initialized_new_session);

  EXPECT_FALSE(initialized_new_session);
}

TEST(SessionRepositoryTests, AddSession_StoresSessionWithGivenId)
{
  nidevice_grpc::SessionRepository session_repository;
  std::string session_name;
  bool initialized_new_session;
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL,
      nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      &initialized_new_session);

  EXPECT_EQ(status, 0);
  EXPECT_EQ(session_repository.access_session(session_name), session_name);
  EXPECT_TRUE(initialized_new_session);
}

TEST(SessionRepositoryTests, NoSessions_AddSessionWithAttachToExistingBehavior_ExceptionThrown)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;

  EXPECT_THROW({
    try {
      session_repository.add_session(
          session_name,
          []() { return 0; },
          NULL,
          nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_ATTACH_TO_EXISTING);
    }
    catch (const nidevice_grpc::NonDriverException& e) {
      auto exception_status = e.GetStatus();
      EXPECT_EQ(::grpc::StatusCode::FAILED_PRECONDITION, exception_status.error_code());
      throw;
    }
  }, nidevice_grpc::NonDriverException);
}

TEST(SessionRepositoryTests, AddNamedSession_StoresSessionWithGivenIdAndName)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  bool initialized_new_session;
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL,
      nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      &initialized_new_session);

  EXPECT_EQ(status, 0);
  EXPECT_EQ(session_repository.access_session(session_name), session_name);
  EXPECT_TRUE(initialized_new_session);
}

TEST(SessionRepositoryTests, UnnamedSessionAdded_RemoveSession_RemovesSession)
{
  nidevice_grpc::SessionRepository session_repository;
  std::string session_name;
  session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  session_repository.remove_session(session_name);

  EXPECT_EQ("",  session_repository.access_session(session_name));
}

TEST(SessionRepositoryTests, NamedSessionAdded_RemoveSession_RemovesSession)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  session_repository.remove_session(session_name);

  EXPECT_EQ("", session_repository.access_session(session_name));
}

TEST(SessionRepositoryTests, NamedSessionAdded_AddSessionWithSameName_ReturnsFirstSessionIdAndDoesNotCallInit)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  bool init_called = false;
  bool initialized_new_session;
  session_repository.add_session(
      session_name,
      [init_called]() mutable {
        init_called = true;
        return 0;
      },
      NULL,
      nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED,
      &initialized_new_session);

  EXPECT_FALSE(init_called);
  EXPECT_FALSE(initialized_new_session);
}

TEST(SessionRepositoryTests, NamedSessionAdded_AddSessionWithSameNameWithInitializeNewBehavior_ExceptionThrown)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  bool init_called = false;
  EXPECT_THROW({
    try {
      session_repository.add_session(
          session_name,
          [init_called]() mutable {
            init_called = true;
            return 0;
          },
          NULL,
          nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW);
    }
    catch (const nidevice_grpc::NonDriverException& e) {
      auto exception_status = e.GetStatus();
      EXPECT_EQ(::grpc::StatusCode::ALREADY_EXISTS, exception_status.error_code());
      throw;
    }
  }, nidevice_grpc::NonDriverException);
}

TEST(SessionRepositoryTests, NamedSessionAdded_ResetServer_RemovesSession)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  bool is_server_reset = session_repository.reset_server();

  EXPECT_EQ("", session_repository.access_session(session_name));
  EXPECT_TRUE(is_server_reset);
}

TEST(SessionRepositoryTests, UnnamedSessionAdded_ResetServer_RemovesSession)
{
  nidevice_grpc::SessionRepository session_repository;
  std::string session_name;
  session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);

  bool is_server_reset = session_repository.reset_server();

  EXPECT_EQ("", session_repository.access_session(session_name));
  EXPECT_TRUE(is_server_reset);
}

TEST(SessionRepositoryTests, NamedAndUnnamedSessionsAdded_ResetServer_RemovesBothSessions)
{
  std::string session_name = "session_name";
  nidevice_grpc::SessionRepository session_repository;
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);
  std::string unnamed_session_name;
  session_repository.add_session(
      unnamed_session_name,
      []() { return 0; },
      NULL);

  bool is_server_reset = session_repository.reset_server();

  EXPECT_EQ("", session_repository.access_session(session_name));
  EXPECT_EQ("", session_repository.access_session(unnamed_session_name));
  EXPECT_TRUE(is_server_reset);
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/session_resource_repository_tests.cpp sha256=09ec888afc12fc66bd9808bcf4163f3a026934ded7859c88d71682a2f0c3a9d0 bytes=14353 -->
## FILE: source/tests/unit/session_resource_repository_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/session_resource_repository_tests.cpp`
- sha256: `09ec888afc12fc66bd9808bcf4163f3a026934ded7859c88d71682a2f0c3a9d0`
- bytes: 14353

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <server/session_repository.h>
#include <server/session_resource_repository.h>

using namespace nidevice_grpc;

namespace ni {
namespace tests {
namespace unit {

const uint32_t kNoSession = 0;
std::string kNoSessionName;
const int32_t kNoError = 0;

template <typename TResourceHandle>
std::string add_session_resource(
    SessionResourceRepository<TResourceHandle>& resource_repository,
    const TResourceHandle& resource)
{
  std::string session_name;
  auto result = resource_repository.add_session(
     session_name,
      [=]() { return std::make_tuple(kNoError, resource); },
      [](TResourceHandle handle) {});
  EXPECT_EQ(kNoError, result);
  return session_name;
}

TEST(SessionResourceRepositoryTests, AddSessionResource_ResourceIsAdded)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint64_t> resource_repository(repository);

  const uint64_t kResourceHandle = 0x1111222233334444;
  std::string session_name("session");
  auto result = resource_repository.add_session(
      session_name,
      [=]() { return std::make_tuple(kNoError, kResourceHandle); },
      [](uint64_t handle) {});

  EXPECT_EQ(kNoError, result);
  EXPECT_NE(kNoSessionName, session_name);
  EXPECT_EQ(
      kResourceHandle,
      resource_repository.access_session(session_name));
  EXPECT_EQ(
      kResourceHandle,
      resource_repository.access_session(session_name));
  EXPECT_EQ(
      session_name,
      repository->access_session(session_name));
}

TEST(SessionResourceRepositoryTests, AddTwoSessionsWithSameResourceHandle_RemoveOneSession_ResourceStillAccessible)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint64_t> resource_repository(repository);
  const uint64_t kResourceHandle = 0x1234;
  auto session_name_one = add_session_resource(resource_repository, kResourceHandle);
  auto session_name_two = add_session_resource(resource_repository, kResourceHandle);
  EXPECT_NE(session_name_one, session_name_two);
  EXPECT_EQ(
      kResourceHandle,
      resource_repository.access_session(session_name_one));
  EXPECT_EQ(
      kResourceHandle,
      resource_repository.access_session(session_name_two));

  resource_repository.remove_session(session_name_one);

  EXPECT_EQ(
      kNoSession,
      resource_repository.access_session(session_name_one));
  EXPECT_EQ(
      kResourceHandle,
      resource_repository.access_session(session_name_two));
}

TEST(SessionResourceRepositoryTests, SessionResource_RemoveSession_ResourceIsRemoved)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint16_t> resource_repository(repository);
  const uint16_t kResourceHandle = 0x1234;
  auto session_name = add_session_resource(resource_repository, kResourceHandle);

  repository->remove_session(session_name);

  EXPECT_EQ(
      kNoSession,
      resource_repository.access_session(session_name));
  EXPECT_EQ(
      kNoSessionName,
      repository->access_session(session_name));
}

TEST(SessionResourceRepositoryTests, SessionResource_RemoveFromResourceRepository_ResourceIsRemoved)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int64_t> resource_repository(repository);
  const int64_t kResourceHandle = 68686868;
  auto session_name = add_session_resource(resource_repository, kResourceHandle);

  // Remove from the SessionResourceRepository and ensure that it removes from the
  // SessionRepository and SessionResourceRepository->
  resource_repository.remove_session(session_name);

  EXPECT_EQ(
      kNoSessionName,
      repository->access_session(session_name));
  EXPECT_EQ(
      0,
      resource_repository.access_session(session_name));
  EXPECT_EQ(
      kNoSessionName,
      resource_repository.resolve_session_name(kResourceHandle));
}

TEST(SessionResourceRepositoryTests, SessionResource_ResetServer_ResourceIsRemoved)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int64_t> resource_repository(repository);
  const int64_t kResourceHandle = -9847465247263584;
  auto session_name = add_session_resource(resource_repository, kResourceHandle);

  repository->reset_server();

  EXPECT_EQ(
      kNoSession,
      resource_repository.access_session(session_name));
}

TEST(SessionResourceRepositoryTests, SessionResource_ResetServer_CleanupIsCalled)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int64_t> resource_repository(repository);
  bool cleanup_called = false;
  std::string session_name;
  resource_repository.add_session(
      session_name,
      [=]() { return std::make_tuple(kNoError, 12345678); },
      [&](int64_t) { cleanup_called = true; });
  EXPECT_FALSE(cleanup_called);

  repository->reset_server();

  EXPECT_TRUE(cleanup_called);
}

TEST(SessionResourceRepositoryTests, AddSessionResourceWithErrrOnInit_ResourceIsNotAdded)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int32_t> resource_repository(repository);

  const int32_t kErrorCode = 9999;
  std::string session_name;
  auto result = resource_repository.add_session(
      session_name,
      [=]() { return std::make_tuple(kErrorCode, 5555); },
      [](uint64_t handle) {});

  EXPECT_EQ(kErrorCode, result);
  EXPECT_EQ(kNoSessionName, session_name);
}

TEST(SessionResourceRepositoryTests, MultipleResourceRepositories_AddResourceToEach_ResourcesAreAded)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int32_t> int_resource_repository(repository);
  SessionResourceRepository<std::string> string_resource_repository(repository);

  const int32_t kIntResourceHandle = -123456;
  auto int_session_name = add_session_resource(
      int_resource_repository,
      kIntResourceHandle);
  const std::string kStringResourceHandle("RESOURCE_HANDLE");
  auto string_session_name = add_session_resource(
      string_resource_repository,
      kStringResourceHandle);

  EXPECT_EQ(
      kIntResourceHandle,
      int_resource_repository.access_session(int_session_name));
  EXPECT_EQ(
      kStringResourceHandle,
      string_resource_repository.access_session(string_session_name));
}

TEST(SessionResourceRepositoryTests, AddMultipleResources_ResourcesAreAdded)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int32_t> resource_repository(repository);

  const int32_t kResourceHandle1 = -123456;
  auto session_name_1 = add_session_resource(
      resource_repository,
      kResourceHandle1);
  const int32_t kResourceHandle2 = 654321;
  auto session_name_2 = add_session_resource(
      resource_repository,
      kResourceHandle2);

  EXPECT_EQ(
      kResourceHandle1,
      resource_repository.access_session(session_name_1));
  EXPECT_EQ(
      kResourceHandle2,
      resource_repository.access_session(session_name_2));
}

TEST(SessionResourceRepositoryTests, AddSessionResource_AccessFromDifferentRepository_DoesNotReturnSession)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int32_t> resource_repository(repository);
  SessionResourceRepository<int32_t> other_resource_repository(repository);
  const int32_t kResourceHandle1 = -123456;
  auto session_name = add_session_resource(
      resource_repository,
      kResourceHandle1);

  auto session_from_other_repository =
      other_resource_repository.access_session(session_name);

  EXPECT_EQ(kNoSession, session_from_other_repository);
}

TEST(SessionResourceRepositoryTests, AddSessionResource_AddSessionWithSameNameFromDifferentRepository_ThrowsSessionException)
{
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<int32_t> resource_repository(repository);
  SessionResourceRepository<int32_t> other_resource_repository(repository);
  const int32_t kResourceHandle1 = -123456;
  std::string kTestResource("test_resource");
  auto result = resource_repository.add_session(
      kTestResource,
      []() { return std::make_tuple(0, 5555); },
      [](int32_t handle) {});

  const int32_t kErrorCode = 9999;
  using MockInitDelegate = ::testing::MockFunction<std::tuple<int32_t, int32_t>(void)>;
  MockInitDelegate mock_init;
  EXPECT_THROW({
    try {
      result = other_resource_repository.add_session(
          kTestResource,
          mock_init.AsStdFunction(),
          [](int32_t handle) { FAIL() << "Unexpected Cleanup"; });
    }
    catch (const nidevice_grpc::SessionException& ex) {
      const std::string expected_message("The session name \"" + kTestResource + "\" is being used by a different driver.");
      EXPECT_STREQ(expected_message.c_str(), ex.what());
      throw;
    }
  }, nidevice_grpc::SessionException);
}

template <typename TResource>
std::string simple_add_session(SessionResourceRepository<TResource> resource_repository, const std::string& session_name, TResource new_resource_handle)
{
  std::string mutable_session_name = session_name;
  const auto status = resource_repository.add_session(
      mutable_session_name,
      [new_resource_handle]() { return std::make_tuple(0, new_resource_handle); },
      [](TResource handle) {});
  EXPECT_EQ(0, status);
  return mutable_session_name;
}

template <typename TResource>
std::string simple_add_dependent_session(
    SessionResourceRepository<TResource> resource_repository,
    const std::string& session_name,
    const std::string& initiating_session_name,
    TResource new_resource_handle)
{
  std::string mutable_session_name = session_name;
  std::string mutable_initiating_session_name = initiating_session_name;
  const auto status = resource_repository.add_dependent_session(
      mutable_session_name,
      [new_resource_handle]() { return std::make_tuple(0, new_resource_handle); },
      mutable_initiating_session_name);
  EXPECT_EQ(0, status);
  return mutable_session_name;
}

// Note: this is the key functional criteria. Make sure that dependent sessions can't "overwrite" primary sessions in the reverse lookup.
// This ensures that any reverse lookups are consistently scoped to the owning service's lifetime management/etc.
TEST(SessionResourceRepositoryTests, SessionAlreadyInResourceRepository_AddDependentSessionWithSameHandle_ResolveSessionByHandleGivesOriginalSession)
{
  constexpr auto DUPE_SESSION_HANDLE = 1234U;
  constexpr auto INITIATING_SESSION_HANDLE = 5678U;
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint32_t> resource_repository(repository);
  const auto initiating_session_name = simple_add_session(resource_repository, "initiating_session", INITIATING_SESSION_HANDLE);
  const auto primary_with_dupe_session_name = simple_add_session(resource_repository, "primary_session_with_dupe_handle", DUPE_SESSION_HANDLE);

  const auto dupe_dependent_session_name = simple_add_dependent_session(resource_repository, "dependent_session", initiating_session_name, DUPE_SESSION_HANDLE);

  EXPECT_EQ(primary_with_dupe_session_name, resource_repository.resolve_session_name(DUPE_SESSION_HANDLE));
}

// Note: This is how the above criteria (SessionAlreadyInResourceRepository_AddDependentSessionWithSameHandle_ResolveSessionByHandleGivesOriginalSession)
// is implemented.
// If there is no dupe primary session, it's probably OK to include the dependent session in the reverse lookup. But it's simpler to leave it out
// completely. This also gives us more wiggle room to change behavior in the future because we are exposing less functionality.
TEST(SessionResourceRepositoryTests, AddDependentSession_DependentSessionIsNotResolvableByHandle)
{
  constexpr auto DEPENDENT_SESSION_HANDLE = 1234U;
  constexpr auto INITIATING_SESSION_HANDLE = 5678U;
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint32_t> resource_repository(repository);
  const auto initiating_session_name = simple_add_session(resource_repository, "initiating_session", INITIATING_SESSION_HANDLE);
  const auto dupe_dependent_session_name = simple_add_dependent_session(resource_repository, "dependent_session", initiating_session_name, DEPENDENT_SESSION_HANDLE);

  EXPECT_EQ("", resource_repository.resolve_session_name(DEPENDENT_SESSION_HANDLE));
}

TEST(SessionResourceRepositoryTests, AddDependentSession_RemoveDependentSession_SessionIsRemoved)
{
  constexpr auto DEPENDENT_SESSION_HANDLE = 1234U;
  constexpr auto INITIATING_SESSION_HANDLE = 5678U;
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint32_t> resource_repository(repository);
  const auto initiating_session_name = simple_add_session(resource_repository, "initiating_session", INITIATING_SESSION_HANDLE);
  const auto dependent_session_name = simple_add_dependent_session(resource_repository, "dependent_session", initiating_session_name, DEPENDENT_SESSION_HANDLE);

  resource_repository.remove_session(dependent_session_name);

  EXPECT_EQ(0, resource_repository.access_session(dependent_session_name));
}

TEST(SessionResourceRepositoryTests, AddDependentSession_RemoveInitiatingSession_BothSessionsAreRemoved)
{
  constexpr auto DEPENDENT_SESSION_HANDLE = 1234U;
  constexpr auto INITIATING_SESSION_HANDLE = 5678U;
  auto repository = std::make_shared<SessionRepository>();
  SessionResourceRepository<uint32_t> resource_repository(repository);
  const auto initiating_session_name = simple_add_session(resource_repository, "initiating_session", INITIATING_SESSION_HANDLE);
  const auto dependent_session_name = simple_add_dependent_session(resource_repository, "dependent_session", initiating_session_name, DEPENDENT_SESSION_HANDLE);

  resource_repository.remove_session(initiating_session_name);

  EXPECT_EQ(0, resource_repository.access_session(initiating_session_name));
  EXPECT_EQ(0, resource_repository.access_session(dependent_session_name));
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/shared_library_tests.cpp sha256=e805ed7f83966707db4bef77fc19cfbf7292b8f83cf9b1ea6fbfd7560e3a045a bytes=5800 -->
## FILE: source/tests/unit/shared_library_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/shared_library_tests.cpp`
- sha256: `e805ed7f83966707db4bef77fc19cfbf7292b8f83cf9b1ea6fbfd7560e3a045a`
- bytes: 5800

````cpp
#include <gtest/gtest.h>
#include <server/shared_library.h>

#if defined(__GNUC__)
  #include <dlfcn.h>
#endif

namespace ni {
namespace tests {
namespace unit {

using TestSession = void*;
using TestApiCreateSessionPtr = int (*)(TestSession* session);
using TestApiCloseSessionPtr = int (*)(TestSession session);
using TestApiWriteSessionDataPtr = int (*)(TestSession session, int attribute_id, const char* value);
using TestApiReadSessionDataPtr = int (*)(TestSession session, int attribute_id, size_t* value_length, char* value_buffer);
using TestApiRemoveSessionDataPtr = int (*)(TestSession session, int attribute_id);

#if defined(_MSC_VER)
static const char* test_library_name = "TestApi.dll";
static const char* wrong_library_name = "WrongTestApi.dll";
#else
static const char* test_library_name = "./libTestApi.so";
static const char* wrong_library_name = "./libWrongTestApi.so";
#endif

TEST(SharedLibraryTests, ValidNameForLibrary_Load_IsLoadedReturnsTrue)
{
  nidevice_grpc::SharedLibrary library(test_library_name);

  library.load();

  EXPECT_TRUE(library.is_loaded()) << "The library should have loaded.";
}

TEST(SharedLibraryTests, ValidNameForLibrary_Load_GetHandleReturnsValue)
{
  nidevice_grpc::SharedLibrary library(test_library_name);

  library.load();

  EXPECT_NE(nullptr, library.get_handle());
}

TEST(SharedLibraryTests, LibraryLoaded_Unload_UnloadsLibrary)
{
  nidevice_grpc::SharedLibrary library(test_library_name);
  library.load();

  library.unload();

  EXPECT_FALSE(library.is_loaded());
  EXPECT_EQ(nullptr, library.get_handle());
}

TEST(SharedLibraryTests, InvalidNameForLibrary_Load_IsLoadedReturnsFalse)
{
  nidevice_grpc::SharedLibrary library(wrong_library_name);

  library.load();

  EXPECT_FALSE(library.is_loaded());
}

TEST(SharedLibraryTests, InvalidNameForLibrary_Load_GetHandleReturnsNull)
{
  nidevice_grpc::SharedLibrary library(wrong_library_name);

  library.load();

  EXPECT_EQ(nullptr, library.get_handle());
}

TEST(SharedLibraryTests, LibraryNotLoaded_GetFunctionPointerWithExistingFunctionName_ReturnsNull)
{
  nidevice_grpc::SharedLibrary library(test_library_name);

  auto createSession = library.get_function_pointer("niTestApiCreateSession");

  EXPECT_EQ(nullptr, createSession);
}

TEST(SharedLibraryTests, LibraryLoaded_GetFunctionPointersWithExistingFunctionName_ReturnsValidFunctionPointers)
{
  nidevice_grpc::SharedLibrary library(test_library_name);
  library.load();

  auto createSession = reinterpret_cast<TestApiCreateSessionPtr>(library.get_function_pointer("niTestApiCreateSession"));
  auto closeSession = reinterpret_cast<TestApiCloseSessionPtr>(library.get_function_pointer("niTestApiCloseSession"));
  auto writeData = reinterpret_cast<TestApiWriteSessionDataPtr>(library.get_function_pointer("niTestApiWriteSessionData"));
  auto readData = reinterpret_cast<TestApiReadSessionDataPtr>(library.get_function_pointer("niTestApiReadSessionData"));

  EXPECT_NE(nullptr, createSession);
  EXPECT_NE(nullptr, closeSession);
  EXPECT_NE(nullptr, writeData);
  EXPECT_NE(nullptr, readData);
}

TEST(SharedLibraryTests, LibraryLoaded_GetFunctionPointerWithNonExistentFunctionName_ReturnsNull)
{
  nidevice_grpc::SharedLibrary library(test_library_name);

  auto createSession = library.get_function_pointer("niTestApiNonExistentFunctionName");

  EXPECT_EQ(nullptr, createSession);
}

TEST(SharedLibraryTests, LibraryAndFunctionsLoaded_FunctionCallsSucceed)
{
  nidevice_grpc::SharedLibrary library(test_library_name);
  library.load();
  ASSERT_TRUE(library.is_loaded());
  auto createSession = reinterpret_cast<TestApiCreateSessionPtr>(library.get_function_pointer("niTestApiCreateSession"));
  auto closeSession = reinterpret_cast<TestApiCloseSessionPtr>(library.get_function_pointer("niTestApiCloseSession"));
  auto writeData = reinterpret_cast<TestApiWriteSessionDataPtr>(library.get_function_pointer("niTestApiWriteSessionData"));
  auto readData = reinterpret_cast<TestApiReadSessionDataPtr>(library.get_function_pointer("niTestApiReadSessionData"));

  const int attribute = 5;
  const char* value = "my data";
  TestSession session = nullptr;
  size_t buffer_length = 0;
  char* buffer = nullptr;
  EXPECT_EQ(0, createSession(&session));
  EXPECT_NE(nullptr, session);
  EXPECT_EQ(0, writeData(session, attribute, "my data"));
  EXPECT_EQ(0, readData(session, attribute, &buffer_length, nullptr));
  EXPECT_EQ(strlen(value) + 1, buffer_length);
  buffer = new char[buffer_length];
  EXPECT_EQ(0, readData(session, attribute, &buffer_length, buffer));
  EXPECT_STREQ(value, buffer);
  delete[] buffer;
}

TEST(SharedLibraryTests, LoadedLibrary_SetLibraryName_DoesNotUpdateLibraryName)
{
  nidevice_grpc::SharedLibrary library(test_library_name);
  library.load();
  std::string initial_library_name = library.get_library_name();
  ASSERT_STREQ(test_library_name, initial_library_name.c_str());

  ASSERT_TRUE(library.is_loaded());
  const char* new_library_name = "hello";
  library.set_library_name(new_library_name);

  std::string name_after_attempted_rename = library.get_library_name();
  EXPECT_STREQ(initial_library_name.c_str(), name_after_attempted_rename.c_str());
}

TEST(SharedLibraryTests, UnloadedLibrary_SetLibraryName_UpdatesLibraryName)
{
  nidevice_grpc::SharedLibrary library(test_library_name);

  ASSERT_FALSE(library.is_loaded());
  const char* new_library_name = "hello";
  library.set_library_name(new_library_name);

  std::string name_after_attempted_rename = library.get_library_name();
  EXPECT_STREQ(new_library_name, name_after_attempted_rename.c_str());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/software_enumerator_tests.cpp sha256=50aecb263bf3a089f372f7057f688d24ab73e3b50597177bdff27e03082a1019 bytes=18524 -->
## FILE: source/tests/unit/software_enumerator_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/software_enumerator_tests.cpp`
- sha256: `50aecb263bf3a089f372f7057f688d24ab73e3b50597177bdff27e03082a1019`
- bytes: 18524

````cpp
#include <grpcpp/test/server_context_test_spouse.h>
#include <gtest/gtest.h>
#include <server/software_enumerator.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>
#include <tests/utilities/syscfg_test_helpers.h>

namespace ni {
namespace tests {
namespace unit {

using ::testing::_;
using ::testing::NiceMock;
using ::testing::Return;
using ::testing::Throw;
using ::testing::WithArg;
using ::testing::WithArgs;

static const char* kPackageId = "ni-iotrace";
static const char* kProductName = "NI I/O Trace";
static const char* kPackageVersion = "22.5.0.49215-0+f63";

TEST(SoftwareEnumeratorTests, SysCfgApiNotInstalled_EnumerateInstalledSoftware_ReturnsNotFoundGrpcStatusCode)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST(SoftwareEnumeratorTests, SysCfgApiNotInstalled_EnumerateInstalledSoftware_SoftwareListIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(0, software.size());
}

TEST(SoftwareEnumeratorTests, InitializeSessionReturnsError_EnumerateInstalledSoftware_ReturnsUnknownGrpcStatusCodeWithSysCfgErrorInMetadata)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Return(NISysCfg_InvalidLoginCredentials));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSoftwareEnumerationFailedMessage, status.error_message());
  ::grpc::testing::ServerContextTestSpouse spouse(&context);
  auto trailing_metadata = spouse.GetTrailingMetadata();
  auto error_iterator = trailing_metadata.find("ni-error");
  EXPECT_NE(trailing_metadata.end(), error_iterator);
  if (error_iterator != trailing_metadata.end()) {
    EXPECT_EQ(NISysCfg_InvalidLoginCredentials, std::stoi(error_iterator->second));
  }
}

TEST(SoftwareEnumeratorTests, InitializeSessionReturnsError_EnumerateInstalledSoftware_SoftwareListIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Return(NISysCfg_InvalidLoginCredentials));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(0, software.size());
}

TEST(SoftwareEnumeratorTests, InitializeSessionSucceeds_EnumerateInstalledSoftware_CallsInitializeButNotClose)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(WithArg<7>(SetSessionHandleToOne));
  EXPECT_CALL(mock_library, CloseHandle(_))
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .Times(0);

  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
}

TEST(SoftwareEnumeratorTests, GetInstalledSoftwareComponentsReturnsError_EnumerateInstalledSoftware_SoftwareListIsEmptyAndReturnsUnknownErrorWithSysCfgErrorInMetadata)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .Times(0);
  EXPECT_CALL(mock_library, NextComponentInfo)
      .Times(0);

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSoftwareEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, software.size());
  ::grpc::testing::ServerContextTestSpouse spouse(&context);
  auto trailing_metadata = spouse.GetTrailingMetadata();
  auto error_iterator = trailing_metadata.find("ni-error");
  EXPECT_NE(trailing_metadata.end(), error_iterator);
  if (error_iterator != trailing_metadata.end()) {
    EXPECT_EQ(NISysCfg_InvalidArg, std::stoi(error_iterator->second));
  }
}

NISysCfgStatus SetEnumSoftwareComponentHandleToOne(NISysCfgEnumSoftwareComponentHandle* enum_software_component_handle)
{
  *enum_software_component_handle = (NISysCfgEnumSoftwareComponentHandle)1;
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, GetInstalledSoftwareComponentsSetsEnumSoftwareComponentHandle_EnumerateInstalledSoftware_SoftwareComponentHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
}

NISysCfgStatus SetEnumeratorCountToOne(unsigned int* numInstalledComps)
{
  *numInstalledComps = 1;
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, GetInstalledSoftwareComponentsSetsEnumSoftwareComponentHandle_EnumerateDevices_ComponentHandleIsPassedToNextComponentInfo)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(WithArg<1>(SetEnumeratorCountToOne));
  EXPECT_CALL(mock_library, NextComponentInfo((void*)1, _, _, _, _, _))
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
}

TEST(SoftwareEnumeratorTests, ResetEnumeratorGetCountReturnsError_EnumerateInstalledSoftware_SoftwareListIsEmptyAndReturnsUnknownErrorWithSysCfgErrorInMetadata)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, NextComponentInfo)
      .Times(0);

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSoftwareEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, software.size());
  ::grpc::testing::ServerContextTestSpouse spouse(&context);
  auto trailing_metadata = spouse.GetTrailingMetadata();
  auto error_iterator = trailing_metadata.find("ni-error");
  EXPECT_NE(trailing_metadata.end(), error_iterator);
  if (error_iterator != trailing_metadata.end()) {
    EXPECT_EQ(NISysCfg_InvalidArg, std::stoi(error_iterator->second));
  }
}

TEST(SoftwareEnumeratorTests, NextComponentInfoReturnsError_EnumerateInstalledSoftware_SoftwareListIsEmptyAndReturnsUnknownErrorWithSysCfgErrorInMetadata)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(WithArg<1>(SetEnumeratorCountToOne));
  EXPECT_CALL(mock_library, NextComponentInfo((void*)1, _, _, _, _, _))
      .WillOnce(Return(NISysCfg_InvalidArg));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSoftwareEnumerationFailedMessage, status.error_message());
  EXPECT_EQ(0, software.size());
  ::grpc::testing::ServerContextTestSpouse spouse(&context);
  auto trailing_metadata = spouse.GetTrailingMetadata();
  auto error_iterator = trailing_metadata.find("ni-error");
  EXPECT_NE(trailing_metadata.end(), error_iterator);
  if (error_iterator != trailing_metadata.end()) {
    EXPECT_EQ(NISysCfg_InvalidArg, std::stoi(error_iterator->second));
  }
}

NISysCfgStatus SetEnumeratorCountToZero(unsigned int* numInstalledComps)
{
  *numInstalledComps = 0;
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, SysCfgApiInstalledAndNoNISoftwarePresent_EnumerateInstalledSoftware_SoftwareListIsEmpty)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount((void*)1, _))
      .WillOnce(WithArg<1>(SetEnumeratorCountToZero));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
  EXPECT_EQ(0, software.size());
}

TEST(SoftwareEnumeratorTests, NISysCfgLibraryIsLoaded_GetSysCfgSession_CallsInitializeSessionOnceAndReturnsOK)
{
  ni::tests::utilities::SysCfgMockLibrary mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(WithArg<7>(SetSessionHandleToOne));
  NISysCfgSessionHandle session1 = nullptr;
  NISysCfgStatus status = software_enumerator.open_or_get_localhost_syscfg_session(&session1);

  NISysCfgSessionHandle session2 = nullptr;
  status = software_enumerator.open_or_get_localhost_syscfg_session(&session2);

  EXPECT_EQ(session1, session2);
  EXPECT_EQ(NISysCfg_OK, status);
}

TEST(SoftwareEnumeratorTests, NISysCfgLibraryIsLoaded_ClearSysCfgSession_CalledCloseHandleOnce)
{
  ni::tests::utilities::SysCfgMockLibrary mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillRepeatedly(WithArg<7>(SetSessionHandleToOne));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(1);
  NISysCfgSessionHandle session = nullptr;
  NISysCfgStatus status = software_enumerator.open_or_get_localhost_syscfg_session(&session);

  software_enumerator.clear_syscfg_session();
  software_enumerator.clear_syscfg_session();

  status = software_enumerator.open_or_get_localhost_syscfg_session(&session);
}

NISysCfgStatus SetPackageId(void* value)
{
  char* id = (char*)value;
  strcpy(id, kPackageId);
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, NextComponentInfoSetsPackageId_EnumerateInstalledSoftware_ResponseContainsThatPackageId)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(WithArg<1>(SetEnumeratorCountToOne));
  EXPECT_CALL(mock_library, NextComponentInfo((void*)1, _, _, _, _, _))
      .WillOnce(WithArg<1>(SetPackageId))
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, software.size());
  EXPECT_EQ(kPackageId, software.Get(0).package_id());
}

NISysCfgStatus SetVersion(void* value)
{
  char* version = (char*)value;
  strcpy(version, kPackageVersion);
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, NextComponentInfoSetsVersion_EnumerateInstalledSoftware_ResponseContainsThatVersion)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(WithArg<1>(SetEnumeratorCountToOne));
  EXPECT_CALL(mock_library, NextComponentInfo((void*)1, _, _, _, _, _))
      .WillOnce(WithArg<2>(SetVersion))
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, software.size());
  EXPECT_EQ(kPackageVersion, software.Get(0).package_version());
}

NISysCfgStatus SetProductName(void* value)
{
  char* name = (char*)value;
  strcpy(name, kProductName);
  return NISysCfg_OK;
}

TEST(SoftwareEnumeratorTests, NextComponentInfoSetsProductName_EnumerateInstalledSoftware_ResponseContainsThatProductName)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents)
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));
  EXPECT_CALL(mock_library, ResetEnumeratorGetCount)
      .WillOnce(WithArg<1>(SetEnumeratorCountToOne));
  EXPECT_CALL(mock_library, NextComponentInfo((void*)1, _, _, _, _, _))
      .WillOnce(WithArg<3>(SetProductName))
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(1, software.size());
  EXPECT_EQ(kProductName, software.Get(0).product_name());
}

TEST(SoftwareEnumeratorTests, DoNotIncludeHiddenPackages_EnumerateInstalledSoftware_GetInstalledSoftwareComponentsUsesAllVisible)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents(_, NISysCfgIncludeItemsAllVisible, _, _))
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, false, &software);

  EXPECT_TRUE(status.ok());
}

TEST(SoftwareEnumeratorTests, IncludeHiddenPackages_EnumerateInstalledSoftware_GetInstalledSoftwareComponentsUsesAllVisibleAndHidden)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  nidevice_grpc::SoftwareEnumerator software_enumerator(&mock_library);
  ::grpc::ServerContext context;
  google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software;
  EXPECT_CALL(mock_library, GetInstalledSoftwareComponents(_, NISysCfgIncludeItemsAllVisibleAndHidden, _, _))
      .WillOnce(WithArg<3>(SetEnumSoftwareComponentHandleToOne));

  ::grpc::Status status = software_enumerator.enumerate_installed_software(&context, true, &software);

  EXPECT_TRUE(status.ok());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/syscfg_library_tests.cpp sha256=291043380def109b7285b7b35ede3c368a7452abcf01ecdb7878423e9a963b79 bytes=483 -->
## FILE: source/tests/unit/syscfg_library_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/syscfg_library_tests.cpp`
- sha256: `291043380def109b7285b7b35ede3c368a7452abcf01ecdb7878423e9a963b79`
- bytes: 483

````cpp
#include <gtest/gtest.h>
#include <server/syscfg_library.h>

namespace ni {
namespace tests {
namespace unit {

TEST(SysCfgLibraryTests, CreateSysCfgLibrary_SharedLibraryNameIsSetToSysCfgLibrary)
{
  nidevice_grpc::SysCfgLibrary syscfg_library;
  std::string shared_library_name = syscfg_library.get_library_name();

  EXPECT_STREQ(nidevice_grpc::kSysCfgApiLibraryName, shared_library_name.c_str());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/syscfg_resource_accessor_tests.cpp sha256=a3aaecff165b636d57df8c071f6dcf2960ba62228c46801695a94e7dafe75d6b bytes=22408 -->
## FILE: source/tests/unit/syscfg_resource_accessor_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/syscfg_resource_accessor_tests.cpp`
- sha256: `a3aaecff165b636d57df8c071f6dcf2960ba62228c46801695a94e7dafe75d6b`
- bytes: 22408

````cpp
#include <grpcpp/test/server_context_test_spouse.h>
#include <gtest/gtest.h>
#include <server/syscfg_library.h>
#include <server/syscfg_resource_accessor.h>
#include <tests/utilities/syscfg_mock_library.h>

namespace ni {
namespace tests {
namespace unit {

using ::ni::tests::utilities::CastAndSetArgPointee;
using ::testing::_;
using ::testing::DoAll;
using ::testing::Invoke;
using ::testing::NiceMock;
using ::testing::Return;
using ::testing::SetArgPointee;
using ::testing::Throw;
using ::testing::WithArg;

static const char* kTestFailureMessage = "SysCfg access has failed.";

class SysCfgResourceAccessorTestImpl final :
  public ::nidevice_restricted_grpc::SysCfgResourceAccessor {
 public:
  SysCfgResourceAccessorTestImpl(::nidevice_grpc::SysCfgLibraryInterface* library) : SysCfgResourceAccessor(library) { }

  ::grpc::Status get_tcp_polling_interval(
    ::grpc::ServerContext* context,
    const nidevice_restricted_grpc::DeviceId& device_id,
    unsigned int* value)
  {
    auto get_tcp_polling_interval_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
      return library->GetResourceProperty(resource, NISysCfgResourcePropertyTcpPollingInterval, value);
    };
    return access_syscfg_resource_by_device_id_filter(context, device_id, kTestFailureMessage, get_tcp_polling_interval_lambda);
  }

  ::grpc::Status set_tcp_polling_interval(
    ::grpc::ServerContext* context,
    const nidevice_restricted_grpc::DeviceId& device_id,
    unsigned int value)
  {
    auto set_tcp_polling_interval_lambda = [&] (nidevice_grpc::SysCfgLibraryInterface* library, NISysCfgResourceHandle resource, bool* save_changes) {
      *save_changes = true;
      return library->SetResourceProperty(resource, NISysCfgResourcePropertyTcpPollingInterval, value);
    };
    return access_syscfg_resource_by_device_id_filter(context, device_id, kTestFailureMessage, set_tcp_polling_interval_lambda);
  }
};

static const unsigned int kTcpPollingIntervalDefault = 10;

class SysCfgResourceAccessorSysCfgMockLibrary : public NiceMock<ni::tests::utilities::SysCfgMockLibrary> {
 public:
  SysCfgResourceAccessorSysCfgMockLibrary()
  {
    is_device_set_ = false;
    is_device_ = NISysCfgBoolFalse;
    user_alias_set_ = false;
    user_alias_ = "";
    serial_number_set_ = false;
    serial_number_ = "";
    product_id_set_ = false;
    product_id_ = 0;
    expect_tcp_polling_interval_ = false;
    tcp_polling_interval_set_ = false;
    tcp_polling_interval_ = kTcpPollingIntervalDefault;
  }
  ~SysCfgResourceAccessorSysCfgMockLibrary() {}

  NISysCfgStatus SetFilterProperty(
      NISysCfgFilterHandle filter_handle,
      NISysCfgFilterProperty property_ID,
      ...)
  {
    NISysCfgStatus status = NISysCfg_InvalidArg;
    va_list args;
    va_start(args, property_ID);
    switch(property_ID) {
      case NISysCfgFilterPropertyIsDevice: {
        is_device_set_ = true;
        is_device_ = (NISysCfgBool)va_arg(args, int);
        status = NISysCfg_OK;
        break;
      }
      case NISysCfgFilterPropertyUserAlias: {
        user_alias_set_ = true;
        user_alias_ = std::string(va_arg(args, const char*));
        status = NISysCfg_OK;
        break;
      }
      case NISysCfgFilterPropertySerialNumber: {
        serial_number_set_ = true;
        serial_number_ = std::string(va_arg(args, const char*));
        status = NISysCfg_OK;
        break;
      }
      case NISysCfgFilterPropertyProductId: {
        product_id_set_ = true;
        product_id_ = va_arg(args, unsigned int);
        status = NISysCfg_OK;
        break;
      }
      default:
        break;
    }
    va_end(args);

    return status;
  }

  NISysCfgStatus SetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      ...)
  {
    NISysCfgStatus status = NISysCfg_InvalidArg;
    va_list args;
    va_start(args, property_ID);
    switch(property_ID) {
      case NISysCfgResourcePropertyTcpPollingInterval: {
        if (expect_tcp_polling_interval_)
        {
          tcp_polling_interval_set_ = true;
          tcp_polling_interval_ = va_arg(args, unsigned int);
          status = NISysCfg_OK;
        }
        break;
      }
      default:
        break;
    }
    va_end(args);

    return status;
  }

  bool is_device_set() const { return is_device_set_; }
  NISysCfgBool is_device() const { return is_device_; }
  bool user_alias_set() const { return user_alias_set_; }
  const std::string& user_alias() const { return user_alias_; }
  bool serial_number_set() const { return serial_number_set_; }
  const std::string& serial_number() const { return serial_number_; }
  bool product_id_set() const { return product_id_set_; }
  unsigned int product_id() const { return product_id_; }
  void set_expect_tcp_polling_interval() { expect_tcp_polling_interval_ = true; }
  bool tcp_polling_interval_set() const { return tcp_polling_interval_set_; }
  unsigned int tcp_polling_interval() const { return tcp_polling_interval_; }

 private:
  bool is_device_set_;
  NISysCfgBool is_device_;
  bool user_alias_set_;
  std::string user_alias_;
  bool serial_number_set_;
  std::string serial_number_;
  bool product_id_set_;
  unsigned int product_id_;
  bool expect_tcp_polling_interval_;
  bool tcp_polling_interval_set_;
  unsigned int tcp_polling_interval_;
};

TEST(SysCfgResourceAccessorTests, SysCfgApiNotInstalled_QueryTcpPollingInterval_ReturnsNotFoundGrpcStatusCode)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST(SysCfgResourceAccessorTests, InitializeSessionReturnsError_QueryTcpPollingInterval_ReturnsUnknownGrpcStatusCode)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(Return(NISysCfg_InvalidLoginCredentials));
  EXPECT_CALL(mock_library, CloseHandle)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(kTestFailureMessage, status.error_message());
}

TEST(SysCfgResourceAccessorTests, InitializeSessionSucceeds_QueryTcpPollingInterval_CallsInitializeButNotClose)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, InitializeSession)
      .WillOnce(DoAll(SetArgPointee<7>((NISysCfgSessionHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle(_))
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::OK, status.error_code());
}

TEST(SysCfgResourceAccessorTests, CreateFilterReturnsError_QueryTcpPollingInterval_ReturnsUnknownErrorSysCfgErrorInMetadata)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, CreateFilter)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, FindHardware)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(kTestFailureMessage, status.error_message());
  ::grpc::testing::ServerContextTestSpouse spouse(&context);
  auto trailing_metadata = spouse.GetTrailingMetadata();
  auto error_iterator = trailing_metadata.find("ni-error");
  EXPECT_NE(trailing_metadata.end(), error_iterator);
  if (error_iterator != trailing_metadata.end())
  {
    EXPECT_EQ(NISysCfg_InvalidArg, std::stoi(error_iterator->second));
  }
}

TEST(SysCfgResourceAccessorTests, CreateFilterSetsFilterHandle_QueryTcpPollingInterval_FilterHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, CreateFilter)
      .WillOnce(DoAll(SetArgPointee<1>((NISysCfgFilterHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, FindHardwareReturnsError_QueryTcpPollingInterval_ReturnsUnknownError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, NextResource)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(kTestFailureMessage, status.error_message());
}

TEST(SysCfgResourceAccessorTests, FindHardwareSetsResourceEnumHandle_QueryTcpPollingInterval_ResourceEnumHandleIsPassedToNextResource)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(DoAll(SetArgPointee<4>((NISysCfgEnumResourceHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, NextResource(_, (void*)1, _))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, FindHardwareSetsResourceEnumHandle_QueryTcpPollingInterval_ResourceEnumHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, FindHardware)
      .WillOnce(DoAll(SetArgPointee<4>((NISysCfgEnumResourceHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, NextResourceReturnsError_QueryTcpPollingInterval_ReturnsUnknownError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_InvalidArg));
  EXPECT_CALL(mock_library, GetResourceIndexedProperty)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(kTestFailureMessage, status.error_message());
}

TEST(SysCfgResourceAccessorTests, NextResourceSetsResourceHandle_QueryTcpPollingInterval_ResourceHandleIsPassedToGetPropertyApis)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(DoAll(SetArgPointee<2>((NISysCfgResourceHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, GetResourceProperty((void*)1, _, _))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, NextResourceSetsResourceHandle_QueryTcpPollingInterval_ResourceHandleIsPassedToCloseHandle)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(DoAll(SetArgPointee<2>((NISysCfgResourceHandle)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, CloseHandle)
      .WillRepeatedly(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, CloseHandle((void*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, NoMatchForFilter_QueryTcpPollingInterval_ReturnsNotFoundError)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_EndOfEnum));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(kTestFailureMessage, status.error_message());
}

static const char* kDeviceName = "MyVST";
static const char* kSerialNumber = "FEDCBA98";
static const uint32_t kProductId = 0x7991;

TEST(SysCfgResourceAccessorTests, DeviceIdPopulated_QueryTcpPollingInterval_FilterConfigured)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  device_id.set_name(kDeviceName);
  device_id.set_serial_number(kSerialNumber);
  device_id.set_product_id(kProductId);
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(mock_library.is_device_set());
  EXPECT_EQ(NISysCfgBoolTrue, mock_library.is_device());
  EXPECT_TRUE(mock_library.user_alias_set());
  EXPECT_EQ(kDeviceName, mock_library.user_alias());
  EXPECT_TRUE(mock_library.serial_number_set());
  EXPECT_EQ(kSerialNumber, mock_library.serial_number());
  EXPECT_TRUE(mock_library.product_id_set());
  EXPECT_EQ(kProductId, mock_library.product_id());
}

TEST(SysCfgResourceAccessorTests, DeviceIsPresent_QueryTcpPollingInterval_FilterModeMatchIsAll)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, FindHardware(_, NISysCfgFilterModeMatchValuesAll, _, _, _))
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, DeviceIsPresent_QueryTcpPollingInterval_ValueIsWritten)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  unsigned int expected_tcp_polling_interval = 125;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, GetResourceProperty(_, NISysCfgResourcePropertyTcpPollingInterval, _))
      .WillOnce(DoAll(CastAndSetArgPointee<2>(expected_tcp_polling_interval), Return(NISysCfg_OK)));

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(expected_tcp_polling_interval, tcp_polling_interval);
}

TEST(SysCfgResourceAccessorTests, DeviceIsPresent_QueryTcpPollingInterval_SaveNotCalled)
{
  NiceMock<ni::tests::utilities::SysCfgMockLibrary> mock_library;
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int tcp_polling_interval;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .Times(0);

  ::grpc::Status status = testImpl.get_tcp_polling_interval(&context, device_id, &tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, DeviceIsPresent_SetTcpPollingInterval_TcpPollingIntervalIsSet)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  mock_library.set_expect_tcp_polling_interval();
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int expected_tcp_polling_interval = 250;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.set_tcp_polling_interval(&context, device_id, expected_tcp_polling_interval);

  EXPECT_TRUE(status.ok());
  EXPECT_TRUE(mock_library.tcp_polling_interval_set());
  EXPECT_EQ(expected_tcp_polling_interval, mock_library.tcp_polling_interval());
}

TEST(SysCfgResourceAccessorTests, DeviceIsPresent_SetTcpPollingInterval_SaveIsCalled)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  mock_library.set_expect_tcp_polling_interval();
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int expected_tcp_polling_interval = 500;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.set_tcp_polling_interval(&context, device_id, expected_tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, SaveDetailedResultStringIsNotNull_SetTcpPollingInterval_StringPassedToFreeDetailedString)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  mock_library.set_expect_tcp_polling_interval();
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int expected_tcp_polling_interval = 500;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .WillOnce(DoAll(SetArgPointee<2>((char*)1), Return(NISysCfg_OK)));
  EXPECT_CALL(mock_library, FreeDetailedString((char*)1))
      .WillOnce(Return(NISysCfg_OK));

  ::grpc::Status status = testImpl.set_tcp_polling_interval(&context, device_id, expected_tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

TEST(SysCfgResourceAccessorTests, SaveDetailedResultStringIsNull_SetTcpPollingInterval_NullPassedToFreeDetailedString)
{
  SysCfgResourceAccessorSysCfgMockLibrary mock_library;
  mock_library.set_expect_tcp_polling_interval();
  SysCfgResourceAccessorTestImpl testImpl(&mock_library);
  ::grpc::ServerContext context;
  nidevice_restricted_grpc::DeviceId device_id;
  unsigned int expected_tcp_polling_interval = 500;
  EXPECT_CALL(mock_library, NextResource)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, SaveResourceChanges)
      .WillOnce(Return(NISysCfg_OK));
  EXPECT_CALL(mock_library, FreeDetailedString(NULL))
      .WillOnce(Return(NISysCfg_EndOfEnum));  // Function returns S_FALSE casted to NISysCfgStatus when str is NULL

  ::grpc::Status status = testImpl.set_tcp_polling_interval(&context, device_id, expected_tcp_polling_interval);

  EXPECT_TRUE(status.ok());
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/tls_config_loader_tests.cpp sha256=93d5ee09f7250d93e4a9ae22f1935cb7c65813c5ddb57236be5642894ca6b739 bytes=608 -->
## FILE: source/tests/unit/tls_config_loader_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/tls_config_loader_tests.cpp`
- sha256: `93d5ee09f7250d93e4a9ae22f1935cb7c65813c5ddb57236be5642894ca6b739`
- bytes: 608

````cpp
#include <gtest/gtest.h>
#include <server/tls_config_loader.h>

namespace ni {
namespace tests {
namespace unit {

TEST(TlsConfigLoaderTests, CreateLoader_WhenNiTlsConfigNotInstalled_IsAvailableReturnsFalse)
{
  nidevice_grpc::TlsConfigLoader loader;

  EXPECT_FALSE(loader.is_available());
}

TEST(TlsConfigLoaderTests, CreateLoader_WhenNiTlsConfigNotInstalled_GetServerCredentialsThrows)
{
  nidevice_grpc::TlsConfigLoader loader;

  EXPECT_THROW(loader.get_server_credentials("ni-grpc-device"), std::runtime_error);
}

}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/xnet_converters_tests.cpp sha256=a8d1acc5ebabc2a564674cbc74e4b2d81110f8d192f2817b617139259263a468 bytes=7601 -->
## FILE: source/tests/unit/xnet_converters_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/xnet_converters_tests.cpp`
- sha256: `a8d1acc5ebabc2a564674cbc74e4b2d81110f8d192f2817b617139259263a468`
- bytes: 7601

````cpp
#include <custom/nixnet_converters.h>
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nixnet/nixnet_mock_library.h>
#include <tests/system/nixnet_utilities.h>

#include <algorithm>
#include <numeric>
#include <string>

using namespace nixnet_grpc;
using namespace nixnet_grpc::converters;
using namespace nixnet_utilities;
using namespace ::testing;
using namespace std::string_literals;
using ni::tests::unit::NiXnetMockLibrary;

namespace ni {
namespace tests {
namespace unit {
namespace {

void assert_enet_frames_are_equal(nxFrameEnet_t* frame1, nixnet_grpc::EnetFrameResponse frame2)
{
  EXPECT_EQ(nixnet_grpc::EnetFrameType::ENET_FRAME_TYPE_DATA, frame2.type());
  EXPECT_EQ(frame1->Type, frame2.type_raw());
  EXPECT_EQ(frame1->DeviceTimestamp, frame2.device_timestamp());
  EXPECT_EQ(frame1->NetworkTimestamp, frame2.network_timestamp());
  EXPECT_EQ(nixnet_grpc::EnetFlags::ENET_FLAGS_TRANSMIT, frame2.flags_mapped()[0]);
  EXPECT_EQ(frame1->Flags, frame2.flags_raw());
  EXPECT_EQ(frame1->Length - nixnet_grpc::ENET_FRAME_HEADER_LENGTH - nixnet_grpc::ENET_FRAME_FCS_SIZE, frame2.frame_data().size());
  ASSERT_THAT(std::vector<u8>(frame1->FrameData, frame1->FrameData + frame1->Length - nixnet_grpc::ENET_FRAME_HEADER_LENGTH - nixnet_grpc::ENET_FRAME_FCS_SIZE), ::testing::ElementsAreArray(frame2.frame_data()));
}

void assert_frames_are_equal(nxFrameVar_t* frame1, nixnet_grpc::FrameResponse frame2)
{
  EXPECT_EQ(frame1->Timestamp, frame2.timestamp());
  EXPECT_EQ(frame1->Identifier, frame2.identifier());
  EXPECT_EQ(nixnet_grpc::FrameType::FRAME_TYPE_LIN_DATA, frame2.type());
  EXPECT_EQ(frame1->Type, frame2.type_raw());
  EXPECT_EQ(1, frame2.flags().size());
  EXPECT_EQ(nixnet_grpc::FrameFlags::FRAME_FLAGS_LIN_EVENT_SLOT, frame2.flags()[0]);
  EXPECT_EQ(frame1->Flags, frame2.flags_raw());
  EXPECT_EQ(frame1->Info, frame2.info());
  EXPECT_EQ(frame1->PayloadLength, frame2.payload().size());
  ASSERT_THAT(std::vector<u8>(frame1->Payload, frame1->Payload + frame1->PayloadLength), ::testing::ElementsAreArray(frame2.payload()));
}

TEST(XnetConvertersTests, CANCommStateValue_SetCANCommResponse_ExtractBitfields)
{
  u32 canCommunicationState = 0;
  u32 transcieverError = 0;
  u32 sleep = 0;
  u32 lastError = 3;
  u32 transmitErrorCounter = 3;
  u32 receiveErrorCounter = 3;
  // This value is obtained by combining above bit fields.
  u32 canCommStateValue = 0x03030300;

  nixnet_grpc::CanCommResponse output;
  SetCanCommResponse(canCommStateValue, &output);

  EXPECT_EQ(nixnet_grpc::CanCommState::CAN_COMM_STATE_ERROR_ACTIVE, output.comm_state());
  EXPECT_EQ(canCommunicationState, output.comm_state_raw());
  EXPECT_EQ(transcieverError, output.transceiver_error());
  EXPECT_EQ(sleep, output.sleep());
  EXPECT_EQ(nixnet_grpc::CanLastErr::CAN_LAST_ERR_ACK, output.last_error());
  EXPECT_EQ(lastError, output.last_error_raw());
  EXPECT_EQ(transmitErrorCounter, output.transmit_error_counter());
  EXPECT_EQ(receiveErrorCounter, output.receive_error_counter());
}

TEST(XnetConvertersTests, FlexRayCommStateValue_SetFlexRayCommResponse_ExtractBitFields)
{
  u32 pocState = 2;
  u32 clockCorrectionFailed = 5;
  u32 passiveToActiveCount = 15;
  u32 channelASleep = 0;
  u32 channelBSleep = 0;
  // This value is obtained by combining above bit fields.
  u32 flexRayCommStateValue = 0x00000F52;

  nixnet_grpc::FlexRayCommResponse output;
  SetFlexRayCommResponse(flexRayCommStateValue, &output);

  EXPECT_EQ(nixnet_grpc::FlexRayPocState::FLEX_RAY_POC_STATE_NORMAL_ACTIVE, output.poc_state());
  EXPECT_EQ(pocState, output.poc_state_raw());
  EXPECT_EQ(clockCorrectionFailed, output.clock_correction_failed());
  EXPECT_EQ(passiveToActiveCount, output.passive_to_active_count());
  EXPECT_EQ(channelASleep, output.channel_a_sleep());
  EXPECT_EQ(channelBSleep, output.channel_b_sleep());
}

TEST(XnetConvertersTests, LINCommStateValue_SetLINCommResponse_ExtractBitFields)
{
  u32 reserved = 0;
  u32 sleep = 1;
  u32 linCommunicationState = 1;
  u32 lastError = 3;
  u32 lastErrorReceived = 0;
  u32 lastErrorExpected = 3;
  u32 lastErrorID = 1;
  u32 transcieverReady = 1;
  // This value is obtained by combining above bit fields.
  u32 communicationState = 0x81030036;
  u32 scheduleIndex = 3;
  u32 linCommState[] = {communicationState, scheduleIndex};

  nixnet_grpc::LinCommResponse output;
  SetLinCommResponse(linCommState, &output);

  EXPECT_EQ(sleep, output.sleep());
  EXPECT_EQ(nixnet_grpc::LinCommState::LIN_COMM_STATE_ACTIVE, output.comm_state());
  EXPECT_EQ(linCommunicationState, output.comm_state_raw());
  EXPECT_EQ(lastError, output.last_error());
  EXPECT_EQ(lastErrorReceived, output.last_error_received());
  EXPECT_EQ(lastErrorExpected, output.last_error_expected());
  EXPECT_EQ(lastErrorID, output.last_error_id());
  EXPECT_EQ(transcieverReady, output.transceiver_ready());
  EXPECT_EQ(scheduleIndex, output.schedule_index());
}

TEST(XnetConvertersTests, SessionInfoStateValue_SetSessionInfoResponse_ExtractSessionInfoState)
{
  u32 sessionInfoState = 1;

  nixnet_grpc::SessionInfoResponse output;
  SetSessionInfoResponse(sessionInfoState, &output);

  EXPECT_EQ(nixnet_grpc::SessionInfoState::SESSION_INFO_STATE_STARTED, output.info());
  EXPECT_EQ(sessionInfoState, output.info_raw());
}

TEST(XnetConvertersTests, FrameBufferArray_ConvertToGrpc_FrameBufferResponse)
{
  std::vector<u8> buffer(48);
  nxFrameVar_t* pFrame = (nxFrameVar_t*)buffer.data();
  pFrame->Timestamp = 0;
  pFrame->Flags = nxFrameFlags_LIN_EventSlot;
  pFrame->Info = 0;
  pFrame->Identifier = 66;
  pFrame->Type = nxFrameType_LIN_Data;
  pFrame->PayloadLength = 8;
  for (u16 j = 0; j < pFrame->PayloadLength; ++j) {
    pFrame->Payload[j] = (u8)(j + 1);
  }

  pFrame = nxFrameIterate(pFrame);
  pFrame->Timestamp = 0;
  pFrame->Flags = nxFrameFlags_LIN_EventSlot;
  pFrame->Info = 0;
  pFrame->Identifier = 67;
  pFrame->Type = nxFrameType_LIN_Data;
  pFrame->PayloadLength = 2;
  for (u16 j = 0; j < pFrame->PayloadLength; ++j) {
    pFrame->Payload[j] = (u8)(j + 1);
  }

  ::google::protobuf::RepeatedPtrField<nixnet_grpc::FrameBufferResponse> output;
  nixnet_grpc::convert_to_grpc(buffer, &output, static_cast<u32>(buffer.size()), nixnet_grpc::Protocol::PROTOCOL_LIN, std::map<int32_t, int32_t>());

  pFrame = (nxFrameVar_t*)buffer.data();
  assert_frames_are_equal(pFrame, output[0].lin());
  pFrame = nxFrameIterate(pFrame);
  assert_frames_are_equal(pFrame, output[1].lin());
}

TEST(XnetConvertersTests, EnetFrameBuffer_ConvertToGrpc_EnetFrameResponse)
{
  std::vector<u8> buffer(3092);
  nxFrameEnet_t* pFrame = (nxFrameEnet_t*)buffer.data();
  EncodeEnetFrame(pFrame, 150, false, 0);
  u16 buffer_length = pFrame->Length;
  pFrame = nxFrameIterateEthernetRead(pFrame);
  EncodeEnetFrame(pFrame, 150, true, 2);
  buffer_length += pFrame->Length;
  std::map<int32_t, int32_t> enet_flags_map = {{nxEnetFlags_Transmit, nixnet_grpc::EnetFlags::ENET_FLAGS_TRANSMIT}};

  ::google::protobuf::RepeatedPtrField<nixnet_grpc::FrameBufferResponse> output;
  nixnet_grpc::convert_to_grpc(buffer, &output, buffer_length, nixnet_grpc::Protocol::PROTOCOL_ENET, enet_flags_map);

  pFrame = (nxFrameEnet_t*)buffer.data();
  assert_enet_frames_are_equal(pFrame, output[0].enet());
  pFrame = nxFrameIterateEthernetRead(pFrame);
  assert_enet_frames_are_equal(pFrame, output[1].enet());
}
}  // namespace
}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/unit/xnet_socket_converters_tests.cpp sha256=25bd88497c8675a5588e8bf11d7e6d78d851eb012ae0ee55f9e4e2fdb8c93d51 bytes=33423 -->
## FILE: source/tests/unit/xnet_socket_converters_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/unit/xnet_socket_converters_tests.cpp`
- sha256: `25bd88497c8675a5588e8bf11d7e6d78d851eb012ae0ee55f9e4e2fdb8c93d51`
- bytes: 33423

````cpp
#include <custom/xnetsocket_converters.h>
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nixnetsocket/nixnetsocket_mock_library.h>

#include <algorithm>
#include <numeric>
#include <string>

using namespace nixnetsocket_grpc;
using namespace ::testing;
using namespace std::string_literals;
using ni::tests::unit::NiXnetSocketMockLibrary;
using nidevice_grpc::converters::allocate_output_storage;
using nidevice_grpc::converters::convert_from_grpc;
using nidevice_grpc::converters::convert_to_grpc;

namespace ni {
namespace tests {
namespace unit {
namespace {
TEST(XnetSocketConvertersTests, IPv4GrpcSockAddr_ConvertFromGrpc_CreatesIPv4NXSockAddr)
{
  constexpr auto PORT = 1234;
  constexpr auto ADDRESS = 0xAABBCCDD;
  auto grpc_sock_addr = SockAddr{};
  grpc_sock_addr.mutable_ipv4()->set_port(PORT);
  grpc_sock_addr.mutable_ipv4()->mutable_addr()->set_addr(ADDRESS);

  auto converted_addr = convert_from_grpc<nxsockaddr>(grpc_sock_addr);
  auto addr_ptr = static_cast<nxsockaddr*>(converted_addr);
  auto reinterpreted_ipv4_addr = reinterpret_cast<nxsockaddr_in*>(addr_ptr);

  EXPECT_EQ(sizeof(nxsockaddr_in), converted_addr.size());
  EXPECT_EQ(nxAF_INET, addr_ptr->sa_family);
  EXPECT_EQ(PORT, reinterpreted_ipv4_addr->sin_port);
  EXPECT_EQ(ADDRESS, reinterpreted_ipv4_addr->sin_addr.addr);
}

SockAddr create_addr_ipv6(::google::protobuf::uint32 port, ::google::protobuf::uint32 flowinfo, const std::vector<char>& address, ::google::protobuf::uint32 scope_id)
{
  auto grpc_sock_addr = SockAddr{};
  auto ipv6_addr = SockAddrIn6{};
  ipv6_addr.set_port(port);
  ipv6_addr.set_flowinfo(flowinfo);
  ipv6_addr.mutable_addr()->set_addr({address.cbegin(), address.cend()});
  ipv6_addr.set_scope_id(scope_id);
  grpc_sock_addr.mutable_ipv6()->CopyFrom(ipv6_addr);
  return grpc_sock_addr;
}

void EXPECT_IPV6_ADDR(
    const SockAddrInputConverter& converted_addr,
    ::google::protobuf::uint32 port,
    ::google::protobuf::uint32 flowinfo,
    const std::vector<char>& address,
    ::google::protobuf::uint32 scope_id)
{
  auto addr_ptr = static_cast<const nxsockaddr*>(converted_addr);
  auto reinterpreted_ipv6_addr = reinterpret_cast<const nxsockaddr_in6*>(addr_ptr);

  EXPECT_EQ(sizeof(nxsockaddr_in6), converted_addr.size());
  EXPECT_EQ(nxAF_INET6, addr_ptr->sa_family);
  EXPECT_EQ(port, reinterpreted_ipv6_addr->sin6_port);
  EXPECT_EQ(flowinfo, reinterpreted_ipv6_addr->sin6_flowinfo);
  EXPECT_THAT(reinterpreted_ipv6_addr->sin6_addr.addr, ElementsAreArray(address.data(), address.size()));
  EXPECT_EQ(scope_id, reinterpreted_ipv6_addr->sin6_scope_id);
}

TEST(XnetSocketConvertersTests, IPv6GrpcSockAddr_ConvertFromGrpc_CreatesIPv6NXSockAddr)
{
  constexpr auto PORT = 1234;
  constexpr auto FLOWINFO = 9999;
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  constexpr auto SCOPE_ID = 8888;
  auto grpc_sock_addr = create_addr_ipv6(PORT, FLOWINFO, ADDRESS, SCOPE_ID);

  auto converted_addr = convert_from_grpc<nxsockaddr>(grpc_sock_addr);

  EXPECT_IPV6_ADDR(converted_addr, PORT, FLOWINFO, ADDRESS, SCOPE_ID);
}

TEST(XnetSocketConvertersTests, IPv6GrpcSockAddrWithTooShortAddress_ConvertFromGrpc_CreatesAddrWithZeroesInMissingBytes)
{
  constexpr auto PORT = 1234;
  constexpr auto FLOWINFO = 9999;
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9};
  const auto ADDRESS_WITH_ZEROES = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0};
  constexpr auto SCOPE_ID = 8888;
  auto grpc_sock_addr = create_addr_ipv6(PORT, FLOWINFO, ADDRESS, SCOPE_ID);

  auto converted_addr = convert_from_grpc<nxsockaddr>(grpc_sock_addr);

  EXPECT_IPV6_ADDR(converted_addr, PORT, FLOWINFO, ADDRESS_WITH_ZEROES, SCOPE_ID);
}

TEST(XnetSocketConvertersTests, IPv6GrpcSockAddrTooLongAddress_ConvertFromGrpc_CreatesIPv6NXSockAddrWithExtraBytesTruncated)
{
  constexpr auto PORT = 1234;
  constexpr auto FLOWINFO = 9999;
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x10, 0x11};
  const auto TRUNCATED_ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  constexpr auto SCOPE_ID = 8888;
  auto grpc_sock_addr = create_addr_ipv6(PORT, FLOWINFO, ADDRESS, SCOPE_ID);

  auto converted_addr = convert_from_grpc<nxsockaddr>(grpc_sock_addr);

  EXPECT_IPV6_ADDR(converted_addr, PORT, FLOWINFO, TRUNCATED_ADDRESS, SCOPE_ID);
}

TEST(XnetSocketConvertersTests, UnsetGrpcSockAddr_ConvertFromGrpc_CreatesEmptySockAddrWithUnspecifiedAddressFamily)
{
  auto grpc_sock_addr = SockAddr{};

  auto converted_addr = convert_from_grpc<nxsockaddr>(grpc_sock_addr);
  auto addr_ptr = static_cast<nxsockaddr*>(converted_addr);

  // Note: these are the values for a zeroed out nxsockaddr struct from our initial std::memset.
  EXPECT_EQ(0, converted_addr.size());
  EXPECT_EQ(nxAF_UNSPEC, addr_ptr->sa_family);
}

using ResourceRepositorySharedPtr = ResourceRepositorySharedPtr_;
struct ResourceRepositoryHolder {
  ResourceRepositoryHolder()
      : session_repository(std::make_shared<nidevice_grpc::SessionRepository>()),
        resource_repository(std::make_shared<nidevice_grpc::SessionResourceRepository<nxSOCKET>>(session_repository))
  {
  }
  operator ResourceRepositorySharedPtr()
  {
    return resource_repository;
  }
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository;
  ResourceRepositorySharedPtr resource_repository;
};

ResourceRepositoryHolder create_resource_repository(std::unordered_map<std::string, nxSOCKET> socket_sessions)
{
  auto repository = ResourceRepositoryHolder{};
  for (const auto pair : socket_sessions) {
    std::string session_name = pair.first;
    repository.resource_repository->add_session(
        session_name, [pair]() { return std::make_tuple(0, pair.second); }, nullptr);
  }

  return repository;
}

nidevice_grpc::Session create_session(std::string name)
{
  auto session = nidevice_grpc::Session{};
  session.set_name(name);
  return session;
}

TEST(XnetSocketConvertersTests, EmptyListOfSockets_ConvertFromGrpc_CreatesZeroedOutSocketSet)
{
  auto resource_repository = create_resource_repository({});
  auto grpc_socket_list = ::google::protobuf::RepeatedPtrField<nidevice_grpc::Session>{};

  auto converted_set = convert_from_grpc<nxfd_set>(grpc_socket_list, resource_repository);
  auto set_ptr = static_cast<nxfd_set*>(converted_set);

  EXPECT_EQ(0, set_ptr->fd_count);
}

TEST(XnetSocketConvertersTests, ListOfTwoSockets_ConvertFromGrpc_CreateSocketSetWithBothSockets)
{
  constexpr auto SESSION_NAME_1 = "one";
  constexpr auto SESSION_NAME_2 = "two";
  constexpr auto SOCKET_1 = 1001;
  constexpr auto SOCKET_2 = 2002;
  auto resource_repository = create_resource_repository({{SESSION_NAME_1, SOCKET_1}, {SESSION_NAME_2, SOCKET_2}});
  auto grpc_socket_list = ::google::protobuf::RepeatedPtrField<nidevice_grpc::Session>{};
  grpc_socket_list.Add(create_session(SESSION_NAME_1));
  grpc_socket_list.Add(create_session(SESSION_NAME_2));

  auto converted_set = convert_from_grpc<nxfd_set>(grpc_socket_list, resource_repository);
  auto set_ptr = static_cast<nxfd_set*>(converted_set);

  EXPECT_EQ(2, set_ptr->fd_count);
  EXPECT_EQ(SOCKET_1, set_ptr->fd_array[0]);
  EXPECT_EQ(SOCKET_2, set_ptr->fd_array[1]);
}

TEST(XnetSocketConvertersTests, ListWithSocketNotInRepository_ConvertFromGrpc_CreatesListWithOneZeroValuedSocket)
{
  constexpr auto SESSION_NAME = "test";
  auto resource_repository = create_resource_repository({});
  auto grpc_socket_list = ::google::protobuf::RepeatedPtrField<nidevice_grpc::Session>{};
  grpc_socket_list.Add(create_session(SESSION_NAME));

  auto converted_set = convert_from_grpc<nxfd_set>(grpc_socket_list, resource_repository);
  auto set_ptr = static_cast<nxfd_set*>(converted_set);

  EXPECT_EQ(1, set_ptr->fd_count);
  EXPECT_EQ(0, set_ptr->fd_array[0]);
}

TEST(XnetSocketConvertersTests, EmptyDuration_ConvertFromGrpc_CreatesEmptyTimeVal)
{
  const auto duration = ::google::protobuf::Duration{};

  auto converted_timeval = convert_from_grpc<nxtimeval>(duration);
  auto timeval_ptr = static_cast<nxtimeval*>(converted_timeval);

  EXPECT_EQ(0, timeval_ptr->tv_sec);
  EXPECT_EQ(0, timeval_ptr->tv_usec);
}

TEST(XnetSocketConvertersTests, Duration_ConvertFromGrpc_CreatesCorrespondingTimeVal)
{
  constexpr auto SECONDS = 100;
  constexpr auto MICROS = 500;
  auto duration = ::google::protobuf::Duration{};
  duration.set_seconds(SECONDS);
  duration.set_nanos(MICROS * 1000);

  auto converted_timeval = convert_from_grpc<nxtimeval>(duration);
  auto timeval_ptr = static_cast<nxtimeval*>(converted_timeval);

  EXPECT_EQ(SECONDS, timeval_ptr->tv_sec);
  EXPECT_EQ(MICROS, timeval_ptr->tv_usec);
}

TEST(XnetSocketConvertersTests, DurationWithSubMicroSecondResolution_ConvertFromGrpc_CreatesCorrespondingTimeValWithFlooredValue)
{
  constexpr auto SECONDS = 100;
  constexpr auto NANOS = 5555;
  constexpr auto MICROS = 5;
  auto duration = ::google::protobuf::Duration{};
  duration.set_seconds(SECONDS);
  duration.set_nanos(NANOS);

  auto converted_timeval = convert_from_grpc<nxtimeval>(duration);
  auto timeval_ptr = static_cast<nxtimeval*>(converted_timeval);

  EXPECT_EQ(SECONDS, timeval_ptr->tv_sec);
  EXPECT_EQ(MICROS, timeval_ptr->tv_usec);
}

TEST(XnetSocketConvertersTests, IPv4Address_ConvertToGrpc_ConvertsToIPv4Address)
{
  constexpr auto PORT = 100;
  constexpr auto ADDR = 1234567;
  auto storage = allocate_output_storage<nxsockaddr, SockAddr>();
  auto ptr_to_storage = reinterpret_cast<nxsockaddr_in*>(&storage);
  ptr_to_storage->sin_family = nxAF_INET;
  ptr_to_storage->sin_port = PORT;
  ptr_to_storage->sin_addr.addr = ADDR;

  auto grpc_data = SockAddr{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockAddr::AddrCase::kIpv4, grpc_data.addr_case());
  EXPECT_EQ(PORT, grpc_data.ipv4().port());
  EXPECT_EQ(ADDR, grpc_data.ipv4().addr().addr());
}

void copy_ipv6_addr(unsigned char* dst, const char* src)
{
  std::memcpy(
      dst,
      src,
      sizeof(nxin6_addr::addr));
}

TEST(XnetSocketConvertersTests, IPv6Address_ConvertToGrpc_ConvertsToIPv6Address)
{
  constexpr auto PORT = 100;
  constexpr auto FLOWINFO = 999;
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  constexpr auto SCOPE_ID = 777;
  auto storage = allocate_output_storage<nxsockaddr, SockAddr>();
  auto ptr_to_storage = reinterpret_cast<nxsockaddr_in6*>(&storage);
  ptr_to_storage->sin6_family = nxAF_INET6;
  ptr_to_storage->sin6_port = PORT;
  copy_ipv6_addr(ptr_to_storage->sin6_addr.addr, ADDRESS.data());
  ptr_to_storage->sin6_flowinfo = FLOWINFO;
  ptr_to_storage->sin6_scope_id = SCOPE_ID;

  auto grpc_data = SockAddr{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockAddr::AddrCase::kIpv6, grpc_data.addr_case());
  EXPECT_EQ(PORT, grpc_data.ipv6().port());
  EXPECT_EQ(FLOWINFO, grpc_data.ipv6().flowinfo());
  EXPECT_THAT(
      grpc_data.ipv6().addr().addr(),
      ElementsAreArray(ADDRESS.data(), ADDRESS.size()));
  EXPECT_EQ(SCOPE_ID, grpc_data.ipv6().scope_id());
}

TEST(XnetSocketConvertersTests, UnknownAddress_ConvertToGrpc_ConvertsToUnsetAddress)
{
  auto storage = allocate_output_storage<nxsockaddr, SockAddr>();
  auto ptr_to_storage = &storage;
  ptr_to_storage->sa_family = nxAF_UNSPEC;

  auto grpc_data = SockAddr{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockAddr::AddrCase::ADDR_NOT_SET, grpc_data.addr_case());
}

TEST(XnetSocketConvertersTests, SockOptDataWithInt_ConvertFromGrpc_DataLooksReasonable)
{
  const int32_t RCV_BUF_SIZE = 1000;
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.set_data_int32(RCV_BUF_SIZE);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(RCV_BUF_SIZE, opt_data.data_int);
  EXPECT_EQ(sizeof(int32_t), opt_data.size());
  EXPECT_EQ(&(opt_data.data_int), opt_data.data());
}

TEST(XnetSocketConvertersTests, SockOptDataWithBool_ConvertFromGrpc_DataLooksReasonable)
{
  const bool REUSE_ADDR = true;
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.set_data_bool(REUSE_ADDR);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  // Bools get translated to ints for the API (0 for False, 1 for True)
  EXPECT_EQ(1, opt_data.data_int);
  EXPECT_EQ(sizeof(int32_t), opt_data.size());
  EXPECT_EQ(&(opt_data.data_int), opt_data.data());
}

TEST(XnetSocketConvertersTests, SockOptDataWithString_ConvertFromGrpc_DataLooksReasonable)
{
  const std::string DEVICE_NAME = "I'm a Device";
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.set_data_string(DEVICE_NAME);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(DEVICE_NAME, opt_data.data_string);
  EXPECT_EQ(DEVICE_NAME.size(), opt_data.size());
  EXPECT_EQ(opt_data.data_string.data(), opt_data.data());
  char* dereferenced_data = (char*)(opt_data.data());
  EXPECT_STREQ(DEVICE_NAME.c_str(), dereferenced_data);
}

TEST(XnetSocketConvertersTests, SockOptDataWithLinger_ConvertFromGrpc_DataLooksReasonable)
{
  constexpr auto L_LINGER = 42;
  constexpr auto L_ONOFF = 1;
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.mutable_data_linger()->set_linger(L_LINGER);
  sock_opt_data.mutable_data_linger()->set_onoff(L_ONOFF);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(sizeof(nxlinger), opt_data.size());
  EXPECT_EQ(&opt_data.data_linger, opt_data.data());
  nxlinger* dereferenced_data = (nxlinger*)(opt_data.data());
  EXPECT_EQ(L_LINGER, dereferenced_data->l_linger);
  EXPECT_EQ(L_ONOFF, dereferenced_data->l_onoff);
}

TEST(XnetSocketConvertersTests, SockOptDataWithIPMReq_ConvertFromGrpc_DataLooksReasonable)
{
  constexpr auto IMR_MULTIADDR = 22;
  constexpr auto IMR_INTERFACE = 1;
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.mutable_data_ip_mreq()->mutable_multiaddr()->set_addr(IMR_MULTIADDR);
  sock_opt_data.mutable_data_ip_mreq()->mutable_imr_interface()->set_addr(IMR_INTERFACE);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(sizeof(nxip_mreq), opt_data.size());
  EXPECT_EQ(&opt_data.data_ipmreq, opt_data.data());
  nxip_mreq* dereferenced_data = (nxip_mreq*)(opt_data.data());
  EXPECT_EQ(IMR_MULTIADDR, dereferenced_data->imr_multiaddr.addr);
  EXPECT_EQ(IMR_INTERFACE, dereferenced_data->imr_interface.addr);
}

TEST(XnetSocketConvertersTests, SockOptDataWithIPV6MReq_ConvertFromGrpc_DataLooksReasonable)
{
  const auto IPV6MR_MULTIADDR = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  constexpr auto IPV6MR_INTERFACE = 1;
  SockOptData sock_opt_data = SockOptData{};
  sock_opt_data.mutable_data_ipv6_mreq()->mutable_multiaddr()->set_addr({IPV6MR_MULTIADDR.cbegin(), IPV6MR_MULTIADDR.cend()});
  sock_opt_data.mutable_data_ipv6_mreq()->set_ipv6mr_interface(IPV6MR_INTERFACE);

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(sizeof(nxipv6_mreq), opt_data.size());
  EXPECT_EQ(&opt_data.data_ipv6mreq, opt_data.data());
  nxipv6_mreq* dereferenced_data = (nxipv6_mreq*)(opt_data.data());
  EXPECT_THAT(dereferenced_data->ipv6mr_multiaddr.addr, ElementsAreArray(IPV6MR_MULTIADDR.data(), IPV6MR_MULTIADDR.size()));
  EXPECT_EQ(IPV6MR_INTERFACE, dereferenced_data->ipv6mr_interface);
}

TEST(XnetSocketConvertersTests, SockOptDataWithDataUnset_ConvertFromGrpc_NullPtrDataAndZeroSize)
{
  SockOptData sock_opt_data = SockOptData{};
  // Avoid setting the oneof data field

  auto opt_data = convert_from_grpc<SockOptDataInputConverter>(sock_opt_data);

  EXPECT_EQ(0, opt_data.size());
  EXPECT_EQ(nullptr, opt_data.data());
}

TEST(XnetSocketConvertersTests, Int32SockOptData_ConvertToGrpc_ConvertsToSockOptDataWithIntValue)
{
  constexpr auto RX_DATA = 100;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_SO_RXDATA);
  void* data_pointer = storage.data();
  EXPECT_EQ(data_pointer, &(storage.data_int));
  auto int_pointer = reinterpret_cast<int32_t*>(data_pointer);
  *int_pointer = RX_DATA;

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataInt32, grpc_data.data_case());
  EXPECT_EQ(RX_DATA, grpc_data.data_int32());
}

TEST(XnetSocketConvertersTests, BoolSockOptData_ConvertToGrpc_ConvertsToSockOptDataWithBoolValue)
{
  constexpr auto REUSE_ADDR = 1;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_SO_REUSEADDR);
  void* data_pointer = storage.data();
  EXPECT_EQ(data_pointer, &(storage.data_int));
  auto int_pointer = reinterpret_cast<int32_t*>(data_pointer);
  *int_pointer = REUSE_ADDR;

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataBool, grpc_data.data_case());
  // 1 from API is translated to true bool for gRPC.
  EXPECT_EQ(true, grpc_data.data_bool());
}

TEST(XnetSocketConvertersTests, StringSockOptData_ConvertToGrpc_ConvertsToSockOptDataWithStringValue)
{
  const std::string DEVICE_NAME = "I'm a Device";
  constexpr auto DEFAULT_SOCK_OPT_STRING_SIZE = 255;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_SO_BINDTODEVICE);
  void* data_pointer = storage.data();
  EXPECT_EQ(DEFAULT_SOCK_OPT_STRING_SIZE, storage.data_string.size());
  EXPECT_EQ(data_pointer, &(storage.data_string[0]));
  auto string_pointer = reinterpret_cast<char*>(data_pointer);
  strncpy(string_pointer, DEVICE_NAME.c_str(), DEVICE_NAME.size() + 1);

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataString, grpc_data.data_case());
  EXPECT_EQ(DEVICE_NAME, grpc_data.data_string());
}

TEST(XnetSocketConvertersTests, LingerSockOptData_ConvertToGrpc_ConvertsToSockOptDataWithLingerValue)
{
  constexpr auto L_LINGER = 42;
  constexpr auto L_ONOFF = 1;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_SO_LINGER);
  void* data_pointer = storage.data();
  EXPECT_EQ(data_pointer, &(storage.data_linger));
  auto linger_pointer = reinterpret_cast<nxlinger*>(data_pointer);
  linger_pointer->l_linger = L_LINGER;
  linger_pointer->l_onoff = L_ONOFF;

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataLinger, grpc_data.data_case());
  EXPECT_EQ(L_LINGER, grpc_data.data_linger().linger());
  EXPECT_EQ(L_ONOFF, grpc_data.data_linger().onoff());
}

TEST(XnetSocketConvertersTests, IPMReqSockOptData_ConvertToGrpc_ConvertsToSockOptDataWithIPMReqValue)
{
  constexpr auto IMR_MULTIADDR = 22;
  constexpr auto IMR_INTERFACE = 1;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_IP_ADD_MEMBERSHIP);
  void* data_pointer = storage.data();
  EXPECT_EQ(data_pointer, &(storage.data_ipmreq));
  auto ipmreq_pointer = reinterpret_cast<nxip_mreq*>(data_pointer);
  ipmreq_pointer->imr_multiaddr.addr = IMR_MULTIADDR;
  ipmreq_pointer->imr_interface.addr = IMR_INTERFACE;

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataIpMreq, grpc_data.data_case());
  EXPECT_EQ(IMR_MULTIADDR, grpc_data.data_ip_mreq().multiaddr().addr());
  EXPECT_EQ(IMR_INTERFACE, grpc_data.data_ip_mreq().imr_interface().addr());
}

TEST(XnetSocketConvertersTests, IPV6MReqSockOptData_ConvertToGrpc_ConvertsToSockOptDataWithIPMReqValue)
{
  const auto IPV6MR_MULTIADDR = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  constexpr auto IPV6MR_INTERFACE = 1;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_IPV6_ADD_MEMBERSHIP);
  void* data_pointer = storage.data();
  EXPECT_EQ(data_pointer, &(storage.data_ipv6mreq));
  auto ipv6mreq_pointer = reinterpret_cast<nxipv6_mreq*>(data_pointer);
  std::memcpy(
      ipv6mreq_pointer->ipv6mr_multiaddr.addr,
      IPV6MR_MULTIADDR.data(),
      sizeof(ipv6mreq_pointer->ipv6mr_multiaddr.addr));
  ipv6mreq_pointer->ipv6mr_interface = IPV6MR_INTERFACE;

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::kDataIpv6Mreq, grpc_data.data_case());
  EXPECT_EQ(grpc_data.data_ipv6_mreq().multiaddr().addr().size(), IPV6MR_MULTIADDR.size());
  EXPECT_THAT(grpc_data.data_ipv6_mreq().multiaddr().addr(), ElementsAreArray(IPV6MR_MULTIADDR.data(), IPV6MR_MULTIADDR.size()));
  EXPECT_EQ(IPV6MR_INTERFACE, grpc_data.data_ipv6_mreq().ipv6mr_interface());
}

TEST(XnetSocketConvertersTests, SockOptDataWithUnknownOptName_ConvertToGrpc_ConvertsToUnsetSockOptData)
{
  constexpr auto UNKNOWN_OPT_NAME = -1;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, UNKNOWN_OPT_NAME);
  void* data_pointer = storage.data();
  EXPECT_EQ(nullptr, data_pointer);

  auto grpc_data = SockOptData{};
  convert_to_grpc(storage, &grpc_data);

  EXPECT_EQ(SockOptData::DataCase::DATA_NOT_SET, grpc_data.data_case());
}

TEST(XnetSocketConvertersTests, AddrOutputConverterWithIPv4Address_ConvertToGrpc_ConvertsToIPv4Address)
{
  constexpr auto ADDRESS = 0x55667788;
  auto converter = allocate_output_storage<void, Addr>(nxAF_INET);
  auto data_ptr = reinterpret_cast<nxin_addr*>(static_cast<void*>(&converter));
  data_ptr->addr = ADDRESS;

  auto grpc_addr = nixnetsocket_grpc::Addr{};
  converter.to_grpc(grpc_addr);

  EXPECT_EQ(nixnetsocket_grpc::Addr::AddrCase::kIpv4, grpc_addr.addr_case());
  EXPECT_EQ(ADDRESS, grpc_addr.ipv4().addr());
}

TEST(XnetSocketConvertersTests, AddrOutputConverterWithIPv6Address_ConvertToGrpc_ConvertsToIPv6Address)
{
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  auto converter = allocate_output_storage<void, Addr>(nxAF_INET6);
  auto data_ptr = reinterpret_cast<nxin6_addr*>(static_cast<void*>(&converter));
  copy_ipv6_addr(data_ptr->addr, ADDRESS.data());

  auto grpc_addr = nixnetsocket_grpc::Addr{};
  converter.to_grpc(grpc_addr);

  EXPECT_EQ(nixnetsocket_grpc::Addr::AddrCase::kIpv6, grpc_addr.addr_case());
  EXPECT_THAT(
      grpc_addr.ipv6().addr(),
      ElementsAreArray(ADDRESS.data(), ADDRESS.size()));
}

TEST(XnetSocketConvertersTests, AddrOutputConverterWithUnspecifiedFamily_ConvertToGrpc_DoesNotSetAddrCase)
{
  auto converter = allocate_output_storage<void, Addr>(nxAF_UNSPEC);
  auto data_ptr = reinterpret_cast<nxin6_addr*>(static_cast<void*>(&converter));

  auto grpc_addr = nixnetsocket_grpc::Addr{};
  converter.to_grpc(grpc_addr);

  EXPECT_EQ(nixnetsocket_grpc::Addr::AddrCase::ADDR_NOT_SET, grpc_addr.addr_case());
}

TEST(XnetSocketConvertersTests, AddrOutputConverterWithBogusFamily_ConvertToGrpc_DoesNotSetAddrCase)
{
  auto converter = allocate_output_storage<void, Addr>(42);
  auto data_ptr = reinterpret_cast<nxin6_addr*>(static_cast<void*>(&converter));

  auto grpc_addr = nixnetsocket_grpc::Addr{};
  converter.to_grpc(grpc_addr);

  EXPECT_EQ(nixnetsocket_grpc::Addr::AddrCase::ADDR_NOT_SET, grpc_addr.addr_case());
}

TEST(XnetSocketConvertersTests, IPv4AddrOutputConverter_ConvertToGrpc_ConvertsToAddress)
{
  constexpr auto ADDRESS = 0x11001122;
  auto converter = allocate_output_storage<nxin_addr, InAddr>();
  auto data_ptr = &converter;
  data_ptr->addr = ADDRESS;

  auto grpc_addr = nixnetsocket_grpc::InAddr{};
  converter.to_grpc(grpc_addr);

  EXPECT_EQ(ADDRESS, grpc_addr.addr());
}

TEST(XnetSocketConvertersTests, StringSockOptData_GetSize_FetchesSizeFromLibrary)
{
  const auto DEFAULT_SOCK_OPT_STRING_SIZE = 255;
  const auto ACTUAL_SOCK_OPT_STRING_SIZE = 12;
  NiXnetSocketMockLibrary library;
  auto storage = allocate_output_storage<void*, SockOptData>(&library, OptName::OPT_NAME_SO_BINDTODEVICE);
  EXPECT_EQ(DEFAULT_SOCK_OPT_STRING_SIZE, storage.string_length);

  nxSOCKET SOCKET = nxINVALID_SOCKET;
  const int LEVEL = 3;
  nxsocklen_t actual_length;

  EXPECT_CALL(library, GetSockOpt(SOCKET, LEVEL, OptName::OPT_NAME_SO_BINDTODEVICE, nullptr, _))
      .WillOnce(DoAll(SetArgPointee<4>(ACTUAL_SOCK_OPT_STRING_SIZE), Return(0)));

  actual_length = storage.size(SOCKET, LEVEL);
  EXPECT_EQ(ACTUAL_SOCK_OPT_STRING_SIZE, actual_length);
}

TEST(XnetSocketConvertersTests, AddrInfoHintInputConverter_ConvertFromGrpc_ConvertsToAddrInfoHint)
{
  constexpr auto FAMILY = AddressFamily::ADDRESS_FAMILY_INET6;
  constexpr auto PROTOCOL = IPProtocol::IP_PROTOCOL_IPV6;
  constexpr auto SOCKET_TYPE = SocketProtocolType::SOCKET_PROTOCOL_TYPE_STREAM;
  AddrInfoHint hints{};
  constexpr auto EXPECTED_FLAGS = nxAI_PASSIVE | nxAI_V4MAPPED;
  hints.set_family(FAMILY);
  hints.add_flags_array(GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_PASSIVE);
  hints.add_flags_array(GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_V4MAPPED);
  hints.set_protocol(PROTOCOL);
  hints.set_sock_type(SOCKET_TYPE);

  auto addr_info_hints_input_converter = convert_from_grpc<nxaddrinfo>(hints);
  auto hints_ptr = static_cast<nxaddrinfo*>(addr_info_hints_input_converter);

  EXPECT_EQ(FAMILY, hints_ptr->ai_family);
  EXPECT_EQ(EXPECTED_FLAGS, hints_ptr->ai_flags);
  EXPECT_EQ(PROTOCOL, hints_ptr->ai_protocol);
  EXPECT_EQ(SOCKET_TYPE, hints_ptr->ai_socktype);
  // For the conversion from AddrInfoHint to nxaddrinfo, the following fields are expected to be 0 or nullptr.
  EXPECT_EQ(0, hints_ptr->ai_addrlen);
  EXPECT_EQ(nullptr, hints_ptr->ai_addr);
  EXPECT_EQ(nullptr, hints_ptr->ai_canonname);
  EXPECT_EQ(nullptr, hints_ptr->ai_next);
}

void EXPECT_ADDR_INFO(
    const std::vector<GetAddrInfoFlags>& flags,
    AddressFamily family,
    SocketProtocolType sock_type,
    IPProtocol protocol,
    const char* canon_name,
    ::google::protobuf::uint32 address,
    ::google::protobuf::uint32 port,
    AddrInfo& addr_info)
{
  int expected_flags_raw = std::accumulate(flags.begin(), flags.end(), 0, std::bit_or<int>());
  EXPECT_EQ(expected_flags_raw, addr_info.flags_raw());
  EXPECT_EQ(flags.size(), addr_info.flags_array().size());
  for (int i = 0; i < std::min<size_t>(flags.size(), addr_info.flags_array().size()); i++) {
    EXPECT_EQ(flags.at(i), addr_info.flags_array(i));
  }
  EXPECT_EQ(family, addr_info.family());
  EXPECT_EQ(sock_type, addr_info.sock_type());
  EXPECT_EQ(protocol, addr_info.protocol());
  EXPECT_STREQ(canon_name, addr_info.canon_name().c_str());
  EXPECT_EQ(address, addr_info.addr().ipv4().addr().addr());
  EXPECT_EQ(port, addr_info.addr().ipv4().port());
}

TEST(XnetSocketConvertersTests, AddrInfoOutputConverter_ConvertToGrpc_ConvertsToAddrInfoMessage)
{
  constexpr auto PORT = 100;
  constexpr auto ADDR = 1234567;
  constexpr auto NEXT_PORT = 101;
  constexpr auto NEXT_ADDR = 1234568;
  nxsockaddr_in next_addr{nxAF_INET, NEXT_PORT, {NEXT_ADDR}};
  nxsockaddr_in addr{nxAF_INET, PORT, {ADDR}};
  std::string nextAddrHostName("NextAddrHostName");
  std::string addrHostName("AddrHostName");
  nxaddrinfo addr_info_next{
      nxAI_PASSIVE | nxAI_ADDRCONFIG,
      nxAF_INET,
      nxSOCK_DGRAM,
      nxIPPROTO_UDP,
      (nxsocklen_t)sizeof(next_addr),
      reinterpret_cast<nxsockaddr*>(&next_addr),
      &nextAddrHostName[0],
      nullptr};
  nxaddrinfo addr_info{
      nxAI_ALL,
      nxAF_INET,
      nxSOCK_STREAM,
      nxIPPROTO_TCP,
      (nxsocklen_t)sizeof(addr),
      reinterpret_cast<nxsockaddr*>(&addr),
      &addrHostName[0],
      &addr_info_next};
  NiXnetSocketMockLibrary library;
  auto converter = allocate_output_storage<nxaddrinfo, google::protobuf::RepeatedPtrField<AddrInfo>>(&library);
  converter.addr_info_ptr = &addr_info;

  EXPECT_CALL(library, FreeAddrInfo(converter.addr_info_ptr))
      .Times(1);
  google::protobuf::RepeatedPtrField<nixnetsocket_grpc::AddrInfo> grpc_output;
  convert_to_grpc(converter, &grpc_output);

  EXPECT_EQ(2, grpc_output.size());
  EXPECT_ADDR_INFO(
      {GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_ALL},
      AddressFamily::ADDRESS_FAMILY_INET,
      SocketProtocolType::SOCKET_PROTOCOL_TYPE_STREAM,
      IPProtocol::IP_PROTOCOL_TCP,
      "AddrHostName",
      ADDR,
      PORT,
      grpc_output[0]);
  EXPECT_ADDR_INFO(
      {GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_PASSIVE, GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_ADDRCONFIG},
      AddressFamily::ADDRESS_FAMILY_INET,
      SocketProtocolType::SOCKET_PROTOCOL_TYPE_DGRAM,
      IPProtocol::IP_PROTOCOL_UDP,
      "NextAddrHostName",
      NEXT_ADDR,
      NEXT_PORT,
      grpc_output[1]);
}

TEST(XnetSocketConvertersTests, AddrInfoFlagsAsInt_ConvertToRepeatedFlagsEnum_AllFlagsPresentInAscendingOrder)
{
  int32_t flags = nxAI_BYPASS_CACHE | nxAI_V4MAPPED | nxAI_PASSIVE;

  AddrInfo grpc_addr_info{};
  convert_to_addr_info_flags(flags, *(grpc_addr_info.mutable_flags_array()));

  EXPECT_EQ(3, grpc_addr_info.flags_array().size());
  EXPECT_EQ(GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_BYPASS_CACHE, grpc_addr_info.flags_array(2));
  EXPECT_EQ(GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_V4MAPPED, grpc_addr_info.flags_array(1));
  EXPECT_EQ(GetAddrInfoFlags::GET_ADDR_INFO_FLAGS_PASSIVE, grpc_addr_info.flags_array(0));
}

TEST(XnetSocketConvertersTests, IpStackInfoStringOutputConverter_ConvertToGrpc_ConvertsToAndFreesInfoString)
{
  const auto IP_INFO_STRING = "This is the info about the driver!"s;
  // Copy to buffer including null terminator.
  auto IP_INFO_BUFFER = std::vector<char>{
      IP_INFO_STRING.c_str(),
      IP_INFO_STRING.c_str() + IP_INFO_STRING.length() + 1};
  NiXnetSocketMockLibrary library;
  auto converter = allocate_output_storage<nixnetsocket_grpc::IpStackInfoString, std::string>(&library);
  auto data_ptr = converter.data();
  *data_ptr = IP_INFO_BUFFER.data();

  EXPECT_CALL(library, IpStackFreeAllStacksInfoStr(IP_INFO_BUFFER.data()));
  auto converted_data = std::string{};
  converter.to_grpc(converted_data);

  EXPECT_EQ(IP_INFO_STRING, converted_data);
}

TEST(XnetSocketConvertersTests, AddrWithIPv4Address_ConvertFromGrpc_ConvertsToNxInAddr)
{
  constexpr auto ADDRESS = 0x66778899;
  auto addr = nixnetsocket_grpc::Addr{};
  addr.mutable_ipv4()->set_addr(ADDRESS);

  const auto converted_data = convert_from_grpc<void>(addr);
  const auto data_ptr = reinterpret_cast<const nxin_addr*>(static_cast<const void*>(converted_data));

  EXPECT_EQ(ADDRESS, data_ptr->addr);
}

TEST(XnetSocketConvertersTests, AddrWithIPv6Address_ConvertFromGrpc_ConvertsToNxIn6Addr)
{
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  auto addr = nixnetsocket_grpc::Addr{};
  addr.mutable_ipv6()->set_addr({ADDRESS.data(), ADDRESS.size()});

  const auto converted_data = convert_from_grpc<void>(addr);
  const auto data_ptr = reinterpret_cast<const nxin6_addr*>(static_cast<const void*>(converted_data));

  EXPECT_THAT(
      data_ptr->addr,
      ElementsAreArray(ADDRESS.data(), ADDRESS.size()));
}

TEST(XnetSocketConvertersTests, AddrWithNoAddress_ConvertFromGrpc_ConvertsToNxIn6Addr)
{
  const auto ADDRESS = std::vector<char>{0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF};
  const auto ZERO_ADDRESS = std::vector<char>(ADDRESS.size(), 0x0);
  auto addr = nixnetsocket_grpc::Addr{};

  const auto converted_data = convert_from_grpc<void>(addr);
  const auto data_ptr = reinterpret_cast<const nxin6_addr*>(static_cast<const void*>(converted_data));

  EXPECT_THAT(
      data_ptr->addr,
      ElementsAreArray(ZERO_ADDRESS.data(), ZERO_ADDRESS.size()));
}

TEST(XnetSocketConvertersTests, GrpcAddrCase_GetAddressFamily_ReturnsCorrectDriverFamily)
{
  using AddrCase = nixnetsocket_grpc::Addr::AddrCase;
  EXPECT_EQ(nxAF_UNSPEC, get_address_family(AddrCase::ADDR_NOT_SET));
  EXPECT_EQ(nxAF_INET, get_address_family(AddrCase::kIpv4));
  EXPECT_EQ(nxAF_INET6, get_address_family(AddrCase::kIpv6));
}

TEST(XnetSocketConvertersTests, GrpcIpv4Addr_ConvertFromGrpc_ConvertsToCorrectNxInAddr)
{
  constexpr auto ADDRESS = 0x55443322;
  auto addr = nixnetsocket_grpc::InAddr{};
  addr.set_addr(ADDRESS);

  const auto converted_data = convert_from_grpc<nxin_addr>(addr);

  EXPECT_EQ(ADDRESS, converted_data.addr);
}
}  // namespace
}  // namespace unit
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/async_helpers.h sha256=ed5d77d5e02c48e5d86f919291880f9dcf26107d9d3a19e3d9a7747679a01e7a bytes=2228 -->
## FILE: source/tests/utilities/async_helpers.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/async_helpers.h`
- sha256: `ed5d77d5e02c48e5d86f919291880f9dcf26107d9d3a19e3d9a7747679a01e7a`
- bytes: 2228

````c
#ifndef ASYNC_HELPERS
#define ASYNC_HELPERS

#include <grpcpp/grpcpp.h>

typedef std::tuple<void*, bool> Completion;

inline Completion get_next_completion(::grpc::CompletionQueue& completion_queue)
{
  Completion completion;
  if (!completion_queue.Next(&std::get<0>(completion), &std::get<1>(completion))) {
    throw std::runtime_error("Completion queue error");
  }
  return completion;
}

template <typename TDuration>
inline bool try_get_next_completion(::grpc::CompletionQueue& completion_queue, Completion& completion, TDuration timeout)
{
  auto deadline = std::chrono::system_clock::now() + timeout;
  switch (completion_queue.AsyncNext(&std::get<0>(completion), &std::get<1>(completion), deadline)) {
    case ::grpc::CompletionQueue::NextStatus::GOT_EVENT:
      return true;
    case ::grpc::CompletionQueue::NextStatus::TIMEOUT:
      return false;
    case ::grpc::CompletionQueue::NextStatus::SHUTDOWN:
    default:
      throw std::runtime_error("Completion queue error");
  }
}

inline bool try_get_next_completion_without_blocking(::grpc::CompletionQueue& completion_queue, Completion& completion)
{
    return try_get_next_completion(completion_queue, completion, std::chrono::milliseconds(0));
}

inline void* get_completion_tag(const Completion& completion)
{
  return std::get<0>(completion);
}

inline bool is_completion_ok(const Completion& completion)
{
  return std::get<1>(completion);
}

// Shut down the completion queue and wait for it to drain. Use this to ensure that the test
// function does not return while pending async operations have references to stack variables.
// If you do not shut down the completion queue, pending async operations may have dangling
// references to stack variables and canceling them may corrupt the stack.
inline void shut_down_completion_queue(::grpc::CompletionQueue& completion_queue)
{
  completion_queue.Shutdown();

  // Wait until Next() returns false, which indicates that the completion queue has been shut
  // down and fully drained.
  Completion completion;
  while (completion_queue.Next(&std::get<0>(completion), &std::get<1>(completion))) {
    // Discard the completion.
  }
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/client_helpers.h sha256=e52cca4b9d9a9447b1988900751b8b352876f3d32d12ee7dc1fe65ab19369f75 bytes=3430 -->
## FILE: source/tests/utilities/client_helpers.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/client_helpers.h`
- sha256: `e52cca4b9d9a9447b1988900751b8b352876f3d32d12ee7dc1fe65ab19369f75`
- bytes: 3430

````c
#ifndef CLIENT_HELPERS
#define CLIENT_HELPERS

#include <grpcpp/grpcpp.h>
#include <server/converters.h>

#include <cstdint>

// EXPERIMENTAL client helpers for grpc-device testing.
namespace nidevice_grpc::experimental::client {

// Simplified (EXPERIMENTAL) version of std::variant that we can use on compilers with
// incomplete C++17 support.
// Note: this is semantically similar to a 2 item variant, but doesn't have the same
// internal characteristics (i.e, it's not an actual union).
template <typename TFirst, typename TSecond>
class simple_variant {
 public:
  // Implicit constructors allow passing arguments of either type to methods
  // accepting a simple_variant.
  simple_variant(const TFirst& first) : first_(first), slot_(0) {}
  simple_variant(const TSecond& second) : second_(second), slot_(1) {}

  template <typename T>
  const T* get_if() const
  {
    return get_if(type_selection<T>{});
  }

  // If T is the active slot: return a copy of the data. Else return default initialized T.
  template <typename T>
  T unpack() const
  {
    auto ptr_to_data = get_if<T>();
    return ptr_to_data ? *ptr_to_data : T{};
  }

 private:
  template <typename T>
  struct type_selection {
  };

  const TFirst* get_if(type_selection<TFirst>&& selection) const
  {
    return slot_ == 0 ? &first_ : nullptr;
  }

  const TSecond* get_if(type_selection<TSecond>&& selection) const
  {
    return slot_ == 1 ? &second_ : nullptr;
  }

  TFirst first_;
  TSecond second_;
  int8_t slot_{-1};
};

class grpc_driver_error : public std::runtime_error {
 private:
  ::grpc::StatusCode code_;
  std::multimap<std::string, std::string> trailers_;

 public:
  grpc_driver_error(const std::string& message, ::grpc::StatusCode code, const std::multimap<grpc::string_ref, grpc::string_ref>& trailers)
      : std::runtime_error(message), code_(code)
  {
    for (const auto& trailer : trailers) {
      trailers_.emplace(
          std::string(trailer.first.data(), trailer.first.length()),
          std::string(trailer.second.data(), trailer.second.length()));
    }
  }
  ::grpc::StatusCode StatusCode() const
  {
    return code_;
  }
  const std::multimap<std::string, std::string>& Trailers() const
  {
    return trailers_;
  }
};

inline void
raise_if_error(const ::grpc::Status& status, const ::grpc::ClientContext& context)
{
  if (!status.ok()) {
    throw grpc_driver_error(status.error_message(), status.error_code(), context.GetServerTrailingMetadata());
  }
}

template <typename TSource, typename TDestination>
inline void copy_array(const TSource& source, TDestination* destination)
{
  destination->CopyFrom({source.cbegin(), source.cend()});
}

template <typename TArray, typename TBitfield>
inline google::protobuf::int32 copy_bitfield_as_enum_array(const simple_variant<TArray, TBitfield>& input)
{
  // Note: "template" qualifiers required for dependent name:
  // https://stackoverflow.com/questions/610245/where-and-why-do-i-have-to-put-the-template-and-typename-keywords
  const auto unpacked_array = input.template unpack<TArray>();
  const auto unpacked_bitfield = input.template unpack<TBitfield>();
  return nidevice_grpc::converters::convert_bitfield_as_enum_array_input(unpacked_array, unpacked_bitfield);
}

}  // namespace nidevice_grpc::experimental::client

#endif /* CLIENT_HELPERS */
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/run_all_tests.cpp sha256=a9ef03070d40fc0cfc5fd9e5123b054875b201c6f80c0d63a8e012f23c795ff0 bytes=163 -->
## FILE: source/tests/utilities/run_all_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/run_all_tests.cpp`
- sha256: `a9ef03070d40fc0cfc5fd9e5123b054875b201c6f80c0d63a8e012f23c795ff0`
- bytes: 163

````cpp
#include <gtest/gtest.h>

int main(int argc, char** argv)
{
  setlocale(LC_ALL, "");
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/scope_exit.h sha256=9b4fcfc8253dc4931f8b7b8bc67834d19e0e32896371ab6d4ea1e64c414a5a77 bytes=799 -->
## FILE: source/tests/utilities/scope_exit.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/scope_exit.h`
- sha256: `9b4fcfc8253dc4931f8b7b8bc67834d19e0e32896371ab6d4ea1e64c414a5a77`
- bytes: 799

````c
#ifndef SCOPE_EXIT
#define SCOPE_EXIT

// A basic implementation of std::experimental::scope_exit
template <typename Fn>
class scope_exit
{
public:
  explicit scope_exit(Fn&& fn) noexcept
    : fn_(std::move(fn)),
      active_(true)
  {
  }

  scope_exit(scope_exit&& that) noexcept
    : fn_(std::move(that.fn_)),
      active_(that.active_)
  {
    that.release();
  }

  scope_exit(const scope_exit&) = delete;
  scope_exit& operator=(const scope_exit&) = delete;

  ~scope_exit()
  {
    if (active_) {
      fn_();
    }
  }

  void release() noexcept
  {
    active_ = false;
  }

private:
  Fn fn_;
  bool active_;
};

template <typename Fn>
scope_exit<Fn> make_scope_exit(Fn&& fn) noexcept
{
  return scope_exit<Fn>(std::move(fn));
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/syscfg_mock_library.h sha256=1274e862c77cc826becdf2718da94cd9b690316ad5ddce2c7d06af4fd0f39d9c bytes=3759 -->
## FILE: source/tests/utilities/syscfg_mock_library.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/syscfg_mock_library.h`
- sha256: `1274e862c77cc826becdf2718da94cd9b690316ad5ddce2c7d06af4fd0f39d9c`
- bytes: 3759

````c
#ifndef NI_TESTS_UTILITIES_SYSCFGMOCKLIBRARY_H
#define NI_TESTS_UTILITIES_SYSCFGMOCKLIBRARY_H

#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nisyscfg.h>

namespace ni {
namespace tests {
namespace utilities {

using ::testing::Return;

class SysCfgMockLibrary : public nidevice_grpc::SysCfgLibraryInterface {
 public:
  SysCfgMockLibrary()
  {
    ON_CALL(*this, NextResource)
        .WillByDefault(Return(NISysCfg_EndOfEnum));
  }
  MOCK_METHOD(NISysCfgStatus, InitializeSession, (const char* target_name, const char* username, const char* password, NISysCfgLocale language, NISysCfgBool force_property_refresh, unsigned int connect_timeout_msec, NISysCfgEnumExpertHandle* expert_enum_handle, NISysCfgSessionHandle* session_handle), (override));
  MOCK_METHOD(NISysCfgStatus, CloseHandle, (void* syscfg_handle), (override));
  MOCK_METHOD(NISysCfgStatus, CreateFilter, (NISysCfgSessionHandle session_handle, NISysCfgFilterHandle* filter_handle), (override));
  NISysCfgStatus SetFilterProperty(
      NISysCfgFilterHandle filter_handle,
      NISysCfgFilterProperty property_ID,
      ...)
  {
    return NISysCfg_OK;
  }
  MOCK_METHOD(NISysCfgStatus, FindHardware, (NISysCfgSessionHandle session_handle, NISysCfgFilterMode filter_mode, NISysCfgFilterHandle filter_handle, const char* expert_names, NISysCfgEnumResourceHandle* resource_enum_handle), (override));
  MOCK_METHOD(NISysCfgStatus, NextResource, (NISysCfgSessionHandle session_handle, NISysCfgEnumResourceHandle resource_enum_handle, NISysCfgResourceHandle* resource_handle), (override));
  MOCK_METHOD(NISysCfgStatus, GetResourceIndexedProperty, (NISysCfgResourceHandle resource_handle, NISysCfgIndexedProperty property_ID, unsigned int index, void* value), (override));
  MOCK_METHOD(NISysCfgStatus, GetResourceProperty, (NISysCfgResourceHandle resource_handle, NISysCfgResourceProperty property_ID, void* value), (override));
  NISysCfgStatus SetResourceProperty(
      NISysCfgResourceHandle resource_handle,
      NISysCfgResourceProperty property_ID,
      ...)
  {
    return NISysCfg_OK;
  }
  MOCK_METHOD(NISysCfgStatus, SaveResourceChanges, (NISysCfgResourceHandle resource_handle, NISysCfgBool* changes_require_restart, char** detailed_result), (override));
  MOCK_METHOD(NISysCfgStatus, FreeDetailedString, (char str[]), (override));
  MOCK_METHOD(NISysCfgStatus, GetInstalledSoftwareComponents, (NISysCfgSessionHandle session_handle, NISysCfgIncludeComponentTypes item_types, NISysCfgBool cached, NISysCfgEnumSoftwareComponentHandle* component_enum_handle), (override));
  MOCK_METHOD(NISysCfgStatus, ResetEnumeratorGetCount, (void* enumHandle, unsigned int* count), (override));
  MOCK_METHOD(NISysCfgStatus, NextComponentInfo, (NISysCfgEnumSoftwareComponentHandle component_enum_handle, char* id, char* version, char* title, NISysCfgComponentType* itemType, char** detailedDescription), (override));
};

// SysCfg GetResourceProperty and GetResourceIndexedProperty require assigning to a void* parameter.
// The standard gmock action SetArgPointee fails due to mismatched types.  The following action
// casts the void* to a pointer of the type of the value passed in prior to assignment.
template <size_t N, typename A, typename = void>
struct CastAndSetArgumentPointeeAction {
  A value;

  template <typename... Args>
  void operator()(const Args&... args) const
  {
    *static_cast<A*>(::std::get<N>(std::tie(args...))) = value;
  }
};

template <size_t N, typename T>
CastAndSetArgumentPointeeAction<N, T> CastAndSetArgPointee(T value)
{
  return {std::move(value)};
}

}  // namespace utilities
}  // namespace tests
}  // namespace ni

#endif  // NI_TESTS_UTILITIES_SYSCFGMOCKLIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/syscfg_test_helpers.h sha256=2e1a7c28ccb39049ec8ac3189e9544d0c8053f322abd84623589cd1b3af4e9cc bytes=262 -->
## FILE: source/tests/utilities/syscfg_test_helpers.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/syscfg_test_helpers.h`
- sha256: `2e1a7c28ccb39049ec8ac3189e9544d0c8053f322abd84623589cd1b3af4e9cc`
- bytes: 262

````c
#ifndef SYSCFG_TEST_HELPERS
#define SYSCFG_TEST_HELPERS

#include <nisyscfg.h>

inline static NISysCfgStatus SetSessionHandleToOne(NISysCfgSessionHandle* session_handle)
{
  *session_handle = (NISysCfgSessionHandle)1;
  return NISysCfg_OK;
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/tcp_echo_server.h sha256=5e449daafee74159fb670e512496832b64501d0e3014200a0c45db6d81ba3779 bytes=3314 -->
## FILE: source/tests/utilities/tcp_echo_server.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/tcp_echo_server.h`
- sha256: `5e449daafee74159fb670e512496832b64501d0e3014200a0c45db6d81ba3779`
- bytes: 3314

````c
#include <cstring>
#include <memory>
#include <string>
#include <thread>
#ifdef _WIN32
#include <winsock2.h>
#else
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#endif

#ifdef _WIN32
typedef int socklen_t;
#else
typedef int SOCKET;
#endif

class TcpEchoSession : public std::enable_shared_from_this<TcpEchoSession> {
public:
    TcpEchoSession(SOCKET socket_fd)
    : socket_fd_(socket_fd)
    , stop_echoing_(false)
    {
    }

    ~TcpEchoSession()
    {
#ifdef _WIN32
        closesocket(socket_fd_);
#else
        close(socket_fd_);
#endif
    }

    void run()
    {
        while (!stop_echoing_) {
            do_echo();
        }
    }

    void prepare_stop()
    {
        stop_echoing_ = true;
    }

private:
    void do_echo()
    {
        auto self(shared_from_this());
        char buffer[max_length] = {0};
        int n = recv(socket_fd_, buffer, max_length, 0);
        if (n > 0) {
            send(socket_fd_, buffer, n, 0);
        }
    }

    static const int max_length = 256;
    SOCKET socket_fd_;
    bool stop_echoing_;
};

class TcpEchoServer
{
public:
    TcpEchoServer()
    : listening_fd_(-1)
    {
    }

    ~TcpEchoServer()
    {
    }

    int start()
    {
        return start_server_session();
    }

    void prepare_stop()
    {
        session_->prepare_stop();
    }

    void stop()
    {
        close_server_session();
    }

    int get_server_port()
    {
        struct sockaddr_in assigned_address;
        socklen_t len = sizeof(assigned_address);
        if (getsockname(listening_fd_, (struct sockaddr *)&assigned_address, &len) == -1) {
            return -1;
        }
        else {
            return ntohs(assigned_address.sin_port);
        }
    }

private:
    int start_server_session()
    {
#ifdef _WIN32
        WSADATA wsa_data;
        WSAStartup(MAKEWORD(2, 2), &wsa_data);
#endif
        listening_fd_ = socket(AF_INET, SOCK_STREAM, 0);
        if (listening_fd_ == -1) {
            return -1;
        }
        struct sockaddr_in server_address;
        std::memset(&server_address, 0, sizeof(server_address));
        server_address.sin_family = AF_INET;
        server_address.sin_addr.s_addr = inet_addr("127.0.0.1");
        server_address.sin_port = htons(0);

        if (bind(listening_fd_, (struct sockaddr*)&server_address, sizeof(server_address)) != 0) {
            return -1;
        }
        if (listen(listening_fd_, 1) != 0) {
            return -1;
        }
        server_thread_ = std::thread(&TcpEchoServer::handle_client, this);
        return 0;
    }

    void close_server_session()
    {
        server_thread_.join();
        session_.reset();

#ifdef _WIN32
        closesocket(listening_fd_);
        WSACleanup();
#else
        close(listening_fd_);
#endif
    }

    void handle_client()
    {
        SOCKET client_fd = accept(listening_fd_, NULL, NULL);
        if (client_fd != -1) {
            session_ = std::make_shared<TcpEchoSession>(client_fd);
            session_->run();
        }
    }

    SOCKET listening_fd_;
    std::thread server_thread_;
    std::shared_ptr<TcpEchoSession> session_;
};
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/test_api.cpp sha256=d678e72a9e894bfd6231cad162c51e9fd565003c310d5d050730106a90dbf07d bytes=1897 -->
## FILE: source/tests/utilities/test_api.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/test_api.cpp`
- sha256: `d678e72a9e894bfd6231cad162c51e9fd565003c310d5d050730106a90dbf07d`
- bytes: 1897

````cpp
#include "test_api.h"

#include <string.h>

#include <map>
#include <string>

using DataMap = std::map<int, std::string>;

static DataMap& GetDataMapFromSession(TestSession session)
{
  DataMap* map = reinterpret_cast<DataMap*>(session);
  return *map;
}

int niTestApiCreateSession(TestSession* session)
{
  if (!session) {
    return 1;
  }
  *session = nullptr;
  try {
    DataMap* map = new DataMap();
    *session = reinterpret_cast<TestSession>(map);
    return 0;
  }
  catch (const std::bad_alloc&) {
    return 1;
  }
}

int niTestApiCloseSession(TestSession session)
{
  if (!session) {
    return 1;
  }
  DataMap& map = GetDataMapFromSession(session);
  delete &map;
  return 0;
}

int niTestApiWriteSessionData(TestSession session, int attribute_id, const char* value)
{
  if (!session || !value) {
    return 1;
  }
  DataMap& map = GetDataMapFromSession(session);
  map[attribute_id] = value;
  return 0;
}

int niTestApiReadSessionData(TestSession session, int attribute_id, size_t* value_length, char* value_buffer)
{
  if (!session || !value_length) {
    return 1;
  }
  DataMap& map = GetDataMapFromSession(session);
  DataMap::const_iterator it = map.find(attribute_id);
  if (it == map.end()) {
    return 1;
  }
  const std::string& value = it->second;
  if (*value_length) {
    if (!value_buffer || *value_length < value.length() + 1) {
      return 1;
    }
    strncpy(value_buffer, value.c_str(), *value_length);
  }
  else {
    if (value_buffer) {
      return 1;
    }
    *value_length = value.length() + 1;
  }
  return 0;
}

int niTestApiRemoveSessionData(TestSession session, int attribute_id)
{
  if (!session) {
    return 1;
  }
  DataMap& map = GetDataMapFromSession(session);
  size_t elements_removed = map.erase(attribute_id);
  return elements_removed > 0 ? 0 : 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/test_api.h sha256=f3e2580e7800307beec74e7ee98139ad1abb3d66206465dd8ef588967bba7198 bytes=882 -->
## FILE: source/tests/utilities/test_api.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/test_api.h`
- sha256: `f3e2580e7800307beec74e7ee98139ad1abb3d66206465dd8ef588967bba7198`
- bytes: 882

````c

#include <cstddef>

#if defined(_MSC_VER)
  #define EXPORT __declspec(dllexport)
  #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
  #define EXPORT __attribute__((visibility("default")))
  #define IMPORT
#endif

#if defined(TEST_API_BUILDING)
  #define TEST_API_FUNCTION extern "C" EXPORT
#else
  #define TEST_API_FUNCTION extern "C" IMPORT
#endif

typedef void* TestSession;

TEST_API_FUNCTION int niTestApiCreateSession(TestSession* session);

TEST_API_FUNCTION int niTestApiCloseSession(TestSession session);

TEST_API_FUNCTION int niTestApiWriteSessionData(TestSession session, int attribute_id, const char* value);

TEST_API_FUNCTION int niTestApiReadSessionData(TestSession session, int attribute_id, size_t* value_length, char* value_buffer);

TEST_API_FUNCTION int niTestApiRemoveSessionData(TestSession session, int attribute_id);
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/utilities/test_helpers.h sha256=73d5517d1427f974a092bdbcb90260c441cd9c95b4a2053592d3c2d6a2b618cf bytes=5138 -->
## FILE: source/tests/utilities/test_helpers.h

- repository: `ni/grpc-device`
- source_path: `source/tests/utilities/test_helpers.h`
- sha256: `73d5517d1427f974a092bdbcb90260c441cd9c95b4a2053592d3c2d6a2b618cf`
- bytes: 5138

````c
#ifndef TEST_HELPERS
#define TEST_HELPERS

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "client_helpers.h"

#define EXPECT_THROW_DRIVER_ERROR(statement_, expected_error_)                 \
  EXPECT_THROW({                                                               \
    try {                                                                      \
      statement_;                                                              \
    }                                                                          \
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) { \
      EXPECT_DRIVER_ERROR(ex, expected_error_);                                \
      throw;                                                                   \
    }                                                                          \
  }, nidevice_grpc::experimental::client::grpc_driver_error)

#define EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR(statement_, expected_error_, message_substring_) \
  EXPECT_THROW({                                                                               \
    try {                                                                                      \
      statement_;                                                                              \
    }                                                                                          \
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {                 \
      EXPECT_DRIVER_ERROR_WITH_SUBSTR(ex, expected_error_, message_substring_);                \
      throw;                                                                                   \
    }                                                                                          \
  }, nidevice_grpc::experimental::client::grpc_driver_error)

#define EXPECT_THROW_GRPC_CANCELLED(statement_)                                \
  EXPECT_THROW({                                                               \
    try {                                                                      \
      statement_;                                                              \
    }                                                                          \
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) { \
      EXPECT_EQ(::grpc::CANCELLED, ex.StatusCode());                           \
      throw;                                                                   \
    }                                                                          \
  }, nidevice_grpc::experimental::client::grpc_driver_error)

#define EXPECT_THROW_GRPC_INVALID_ARGUMENT(statement_)                         \
  EXPECT_THROW({                                                               \
    try {                                                                      \
      statement_;                                                              \
    }                                                                          \
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) { \
      EXPECT_EQ(::grpc::StatusCode::INVALID_ARGUMENT, ex.StatusCode());        \
      throw;                                                                   \
    }                                                                          \
  }, nidevice_grpc::experimental::client::grpc_driver_error)

#define EXPECT_DRIVER_ERROR(exception_, expected_error_)             \
  do {                                                               \
    EXPECT_EQ(::grpc::StatusCode::UNKNOWN, exception_.StatusCode()); \
    EXPECT_LT(expected_error_, 0);                                   \
    EXPECT_EQ(expected_error_, get_driver_error(exception_));        \
  } while(false)

#define EXPECT_DRIVER_ERROR_WITH_SUBSTR(exception_, expected_error_, message_substring_) \
  do {                                                                                   \
    EXPECT_DRIVER_ERROR(exception_, expected_error_);                                    \
    EXPECT_THAT(exception_.what(), ::testing::HasSubstr(message_substring_));            \
  } while(false)

inline int get_driver_error(const std::multimap<std::string, std::string>& metadata)
{
  auto iterator = metadata.find("ni-error");
  if (iterator != metadata.end())
  {
    return std::stoi(iterator->second);
  }
  ADD_FAILURE() << "ni-error key not found in metadata.";
  return 0;
}

inline int get_driver_error(const std::multimap<grpc::string_ref, grpc::string_ref>& metadata)
{
  auto iterator = metadata.find("ni-error");
  if (iterator != metadata.end())
  {
    // grpc::string_ref is not NUL-terminated, so make a copy.
    std::string value(iterator->second.begin(), iterator->second.end());
    return std::stoi(value);
  }
  ADD_FAILURE() << "ni-error key not found in metadata.";
  return 0;
}

inline int get_driver_error(const nidevice_grpc::experimental::client::grpc_driver_error& ex)
{
  return get_driver_error(ex.Trailers());
}

#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=ThirdPartyNotices.txt sha256=b50bd1fd885a5fb70c24208fee26bebe095d05b6dbc661a43a7e1abcff2fec39 bytes=3359 -->
## FILE: ThirdPartyNotices.txt

- repository: `ni/grpc-device`
- source_path: `ThirdPartyNotices.txt`
- sha256: `b50bd1fd885a5fb70c24208fee26bebe095d05b6dbc661a43a7e1abcff2fec39`
- bytes: 3359

````text
THIRD-PARTY SOFTWARE NOTICES AND INFORMATION
Do Not Translate or Localize

NI gRPC Device Server uses third party material from the projects listed below.

****** gRPC (https://github.com/grpc/grpc) ******

Copyright 2014 gRPC authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

****** json (https://github.com/nlohmann/json) ******

MIT License

Copyright (c) 2013-2021 Niels Lohmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

****** utfcpp (https://github.com/nemtrif/utfcpp) ******

Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=grpc-device path=utils/copilot-build.ps1 sha256=12013d6c0e1ed5d8f6b730a5546bb3bb379b40baee6a22e50edb62ddf7e3b03b bytes=989 -->
## FILE: utils/copilot-build.ps1

- repository: `ni/grpc-device`
- source_path: `utils/copilot-build.ps1`
- sha256: `12013d6c0e1ed5d8f6b730a5546bb3bb379b40baee6a22e50edb62ddf7e3b03b`
- bytes: 989

````powershell
#!/usr/bin/env pwsh
# Build script for grpc-device project
# This script sets up the Visual Studio environment and builds the project
#
# This script is particularly useful for GitHub Copilot since the complex
# cmd.exe command with vcvars64.bat setup often requires manual approval.
# Using this script allows for easier auto-approval of build commands.

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$BuildArgs
)

# Convert BuildArgs array to a single string for passing to cmake
$cmakeArgs = if ($BuildArgs) { $BuildArgs -join " " } else { "--config Debug" }

# Run the build command with Visual Studio environment setup
$command = "call `"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvars64.bat`" && cd /d `"$PWD\build`" && cmake --build . $cmakeArgs"

Write-Host "Running build command: cmake --build . $cmakeArgs"
Write-Host "Setting up Visual Studio environment and building..."

cmd.exe /c $command
````
