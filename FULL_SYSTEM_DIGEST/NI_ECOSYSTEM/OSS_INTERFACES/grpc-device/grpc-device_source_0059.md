# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/test_localhost_config.json sha256=4128e2b305afed8dabe3a14018eac29835eb856bc07c3ead34faaf3adc93139a bytes=44 -->
## FILE: source/tests/assets/test_localhost_config.json

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/test_localhost_config.json`
- sha256: `4128e2b305afed8dabe3a14018eac29835eb856bc07c3ead34faaf3adc93139a`
- bytes: 44

````json
{
    "address": "[::1]",
    "port": 0
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/assets/test_mutual_tls_config.json sha256=b88ad896c1cb46bf955153478aee4f1e1792ccb2119afc293efb6f17e8e0f209 bytes=189 -->
## FILE: source/tests/assets/test_mutual_tls_config.json

- repository: `ni/grpc-device`
- source_path: `source/tests/assets/test_mutual_tls_config.json`
- sha256: `b88ad896c1cb46bf955153478aee4f1e1792ccb2119afc293efb6f17e8e0f209`
- bytes: 189

````json
{
  "security" : {
      "server_cert": "test_server_self_signed_crt.pem",
      "server_key": "test_server_privatekey.pem",
      "root_cert": "test_client_self_signed_crt.pem"
  }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/ni_fake_daqmx_streaming_tests.cpp sha256=a70b358490aa5ee6d255361cea24ad5ecca967b8de82395e01341b95df05cd7b bytes=15374 -->
## FILE: source/tests/integration/ni_fake_daqmx_streaming_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/ni_fake_daqmx_streaming_tests.cpp`
- sha256: `a70b358490aa5ee6d255361cea24ad5ecca967b8de82395e01341b95df05cd7b`
- bytes: 15374

````cpp
#include <NIDAQmx.h>
#include <nidaqmx/nidaqmx_mock_library.h>
#include <nidaqmx/nidaqmx_client.h>

#include <gmock/gmock-spec-builders.h>
#include <google/protobuf/stubs/port.h>
#include <grpcpp/client_context.h>
#include <grpcpp/server_builder.h>
#include <gtest/gtest.h>
#include <nidaqmx.grpc.pb.h>
#include <nidaqmx.pb.h>
#include <nidaqmx/nidaqmx_service.h>
#include <register_all_services.h>
#include <server/data_moniker_service.h>
#include <server/session_resource_repository.h>
#include <sideband_grpc.h>
#include <thread>

namespace ni {
namespace tests {
namespace integration {

using namespace ::testing;
using namespace nidevice_grpc;
namespace pb = ::google::protobuf;
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

// This test class is used to test the NiDAQmxService using a mocked daqmx library(NiDAQmxMockLibrary)
// We intend to use this class to test streaming apis in NiDAQmxService
class NiFakeDAQmxStreamingTests : public ::testing::Test {
 private:
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::shared_ptr<ni::tests::unit::NiDAQmxMockLibrary> library_;
  std::shared_ptr<nidaqmx_grpc::NiDAQmxService> daqmxService_;
  std::shared_ptr<ni::data_monikers::DataMonikerService> moniker_service_;
  std::unique_ptr<::grpc::Server> server_;
  std::unique_ptr<nidaqmx_grpc::NiDAQmx::Stub> stub_;
  std::unique_ptr<ni::data_monikers::DataMoniker::Stub> moniker_service_stub_;
  std::atomic<bool> shutdown_{false};

 public:
  NiFakeDAQmxStreamingTests()
  {
    session_repository_ = std::make_shared<nidevice_grpc::SessionRepository>();
    library_ = std::make_shared<ni::tests::unit::NiDAQmxMockLibrary>();
    auto ni_daqmx_session_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<TaskHandle>>(session_repository_);
    daqmxService_ = std::make_shared<nidaqmx_grpc::NiDAQmxService>(library_, ni_daqmx_session_repository, FeatureToggles({}, CodeReadiness::kNextRelease));
    moniker_service_ = std::make_shared<ni::data_monikers::DataMonikerService>();
    server_ = start_server();
    nidaqmx_grpc::RegisterMonikerEndpoints();
    stub_ = nidaqmx_grpc::NiDAQmx::NewStub(server_->InProcessChannel(::grpc::ChannelArguments()));
    moniker_service_stub_ = ni::data_monikers::DataMoniker::NewStub(server_->InProcessChannel(::grpc::ChannelArguments()));
    Mock::AllowLeak(library_.get());
  }

  virtual ~NiFakeDAQmxStreamingTests()
  {
    shutdown();
  }

  void shutdown()
  {
    if (!shutdown_) {
      shutdown_ = true;
      server_->Shutdown();
    }
  }

  std::unique_ptr<nidaqmx_grpc::NiDAQmx::Stub>& stub()
  {
    return stub_;
  }

  std::unique_ptr<ni::data_monikers::DataMoniker::Stub>& moniker_stub()
  {
    return moniker_service_stub_;
  }

  std::shared_ptr<ni::tests::unit::NiDAQmxMockLibrary> library()
  {
    return library_;
  }

  std::unique_ptr<::grpc::Server> start_server()
  {
    ::grpc::ServerBuilder builder;
    builder.RegisterService(daqmxService_.get());
    builder.RegisterService(moniker_service_.get());
    return builder.BuildAndStart();
  }
};

TEST_F(NiFakeDAQmxStreamingTests, StreamRead_Scalar)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // Set expectation on the mocked daqmx lib method.
  EXPECT_CALL(*library(), ReadDigitalScalarU32(_, 0, ::testing::_, _))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(1), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(2), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(3), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(4), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(5), ::testing::Return(0)))
      .WillRepeatedly(::testing::DoAll(::testing::SetArgPointee<2>(999), ::testing::Return(0)));

  // Dont worry about deleting read_moniker_u32 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_u32_response = nidaqmx_grpc::experimental::client::begin_read_digital_scalar_u32(stub(), *session, 0);
  ni::data_monikers::Moniker* read_moniker_u32 = new ni::data_monikers::Moniker(begin_read_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerList read_requests;
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_u32);
  auto stream = moniker_stub().get()->StreamRead(&moniker_context, read_requests);

  for (int i = 0; i < 5; i++) {
    // Read data
    nidaqmx_grpc::MonikerReadDigitalScalarU32Response read_value_u32;
    ni::data_monikers::MonikerReadResponse read_result;
    stream->Read(&read_result);
    read_result.data().values(0).UnpackTo(&read_value_u32);
    EXPECT_EQ(read_value_u32.value(), i + 1);
  }

  moniker_context.TryCancel();
}

TEST_F(NiFakeDAQmxStreamingTests, StreamRead_Array)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // create some data for the array
  std::vector<pb::uint32> data_u32 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int size = data_u32.size();

  // Set expectation on the mocked daqmx lib method.
  EXPECT_CALL(*library(), ReadDigitalU32(_, 1, 0, DAQmx_Val_GroupByChannel, ::testing::_, 10, _, _))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<4>(data_u32.begin(), data_u32.begin() + size), ::testing::Return(0)));

  // Dont worry about deleting read_moniker_u32 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_digital_u32_response = nidaqmx_grpc::experimental::client::begin_read_digital_u32(stub(), *session, 1, 0, DAQmx_Val_GroupByChannel, 10);
  auto read_moniker_u32 = new ni::data_monikers::Moniker(begin_read_digital_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerList read_requests;
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_u32);

  auto stream = moniker_stub().get()->StreamRead(&moniker_context, read_requests);

  for (int i = 0; i < 5; i++) {
    // Read data
    nidaqmx_grpc::MonikerReadDigitalU32Response read_values_u32;
    ni::data_monikers::MonikerReadResponse read_result;
    stream->Read(&read_result);
    read_result.data().values(0).UnpackTo(&read_values_u32);
    ASSERT_THAT(read_values_u32.read_array(), ElementsAreArray(data_u32));
  }

  moniker_context.TryCancel();
}

TEST_F(NiFakeDAQmxStreamingTests, StreamWrite_Array)
{
  // create some setup for writing
  auto session = std::make_unique<nidevice_grpc::Session>();
  std::vector<pb::uint32> data_int_u32 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int size = data_int_u32.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), WriteDigitalU32(_, 10, TRUE, 0, DAQmx_Val_GroupByChannel, ::testing::_, _, _))
      .With(Args<5, 1>(ElementsAreArray(data_int_u32)))
      .WillRepeatedly(::testing::Return(0));

  // Dont worry about deleting write_moniker_u32 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_write_digital_u32_response = nidaqmx_grpc::experimental::client::begin_write_digital_u32(stub(), *session, 10, TRUE, 0, DAQmx_Val_GroupByChannel);
  auto write_moniker_u32 = new ni::data_monikers::Moniker(begin_write_digital_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest write_request;
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_u32);

  auto write_stream = moniker_stub().get()->StreamWrite(&moniker_context);
  write_stream->Write(write_request);

  for (int i = 0; i < 5; i++) {
    // Write data
    nidaqmx_grpc::MonikerWriteDigitalU32Request write_digital_u32_request;
    write_digital_u32_request.mutable_write_array()->Add(data_int_u32.begin(), data_int_u32.end());
    ni::data_monikers::MonikerWriteRequest write_data_request;
    write_data_request.mutable_data()->add_values()->PackFrom(write_digital_u32_request);
    write_stream->Write(write_data_request);
  }

  write_stream->WritesDone();
  moniker_context.TryCancel();
}

TEST_F(NiFakeDAQmxStreamingTests, StreamReadWrite_Array)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // create some data for the array
  std::vector<pb::uint32> data_int_u32 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), WriteDigitalU32(_, 10, TRUE, 0, DAQmx_Val_GroupByChannel, ::testing::_, _, _))
      .With(Args<5, 1>(ElementsAreArray(data_int_u32)))
      .WillRepeatedly(::testing::Return(0));

  // create some setup for reading
  std::vector<pb::uint32> data_u32 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int read_size = data_u32.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), ReadDigitalU32(_, 1, 0, DAQmx_Val_GroupByChannel, ::testing::_, 10, _, _))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<4>(data_u32.begin(), data_u32.begin() + read_size), ::testing::Return(0)));

  // Dont worry about deleting write_moniker_u32 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_write_digital_u32_response = nidaqmx_grpc::experimental::client::begin_write_digital_u32(stub(), *session, 10, TRUE, 0, DAQmx_Val_GroupByChannel);
  auto write_moniker_u32 = new ni::data_monikers::Moniker(begin_write_digital_u32_response.moniker());

  // Dont worry about deleting read_moniker_u32 and read_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_digital_u32_response = nidaqmx_grpc::experimental::client::begin_read_digital_u32(stub(), *session, 1, 0, DAQmx_Val_GroupByChannel, 10);
  auto read_moniker_u32 = new ni::data_monikers::Moniker(begin_read_digital_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest write_request;
  write_request.mutable_monikers()->mutable_read_monikers()->AddAllocated(read_moniker_u32);
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_u32);

  auto write_stream = moniker_stub().get()->StreamReadWrite(&moniker_context);
  write_stream->Write(write_request);

  for (int i = 0; i < 5; i++) {
    // Write data
    nidaqmx_grpc::MonikerWriteDigitalU32Request write_digital_u32_request;
    write_digital_u32_request.mutable_write_array()->Add(data_int_u32.begin(), data_int_u32.end());
    ni::data_monikers::MonikerWriteRequest write_data_request;
    write_data_request.mutable_data()->add_values()->PackFrom(write_digital_u32_request);
    write_stream->Write(write_data_request);

    // Read data
    nidaqmx_grpc::MonikerReadDigitalU32Response read_values_u32;
    ni::data_monikers::MonikerReadResponse read_result;
    write_stream->Read(&read_result);
    read_result.data().values(0).UnpackTo(&read_values_u32);
    ASSERT_THAT(read_values_u32.read_array(), SizeIs(read_size));
    ASSERT_THAT(read_values_u32.read_array(), ElementsAreArray(data_u32));
  }

  write_stream->WritesDone();
  moniker_context.TryCancel();
}

TEST_F(NiFakeDAQmxStreamingTests, InvalidSidebandStrategy_BeginSidebandStream_ReturnsInvalidArgument)
{
  grpc::ClientContext moniker_context;
  ni::data_monikers::BeginMonikerSidebandStreamRequest request;
  ni::data_monikers::BeginMonikerSidebandStreamResponse response;

  request.set_strategy(static_cast<ni::data_monikers::SidebandStrategy>(999));

  auto status = moniker_stub().get()->BeginSidebandStream(&moniker_context, request, &response);

  EXPECT_EQ(status.error_code(), grpc::StatusCode::INVALID_ARGUMENT);
  EXPECT_THAT(status.error_message(), HasSubstr("Invalid sideband strategy: 999"));
}

TEST_F(NiFakeDAQmxStreamingTests, UnknownMonikerSource_StreamRead_ReturnsInvalidArgument)
{
  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerList read_requests;
  auto read_moniker = read_requests.add_read_monikers();
  read_moniker->set_data_source("unknown_endpoint");
  read_moniker->set_data_instance(1);

  auto stream = moniker_stub().get()->StreamRead(&moniker_context, read_requests);

  ni::data_monikers::MonikerReadResponse read_result;
  EXPECT_FALSE(stream->Read(&read_result)) << "Server should have closed the stream with an error";

  auto status = stream->Finish();
  EXPECT_EQ(status.error_code(), grpc::StatusCode::INVALID_ARGUMENT);
  EXPECT_THAT(status.error_message(), HasSubstr("Unknown moniker data_source: unknown_endpoint"));
}

TEST_F(NiFakeDAQmxStreamingTests, MismatchedValueCount_StreamReadWrite_ReturnsInvalidArgument)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  auto begin_write_digital_u32_response = nidaqmx_grpc::experimental::client::begin_write_digital_u32(stub(), *session, 10, TRUE, 0, DAQmx_Val_GroupByChannel);
  auto write_moniker_u32 = new ni::data_monikers::Moniker(begin_write_digital_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest setup_request;
  setup_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_u32);

  auto write_stream = moniker_stub().get()->StreamReadWrite(&moniker_context);
  write_stream->Write(setup_request);

  // One write moniker is configured, but no values are provided in the payload.
  ni::data_monikers::MonikerWriteRequest mismatched_data_request;
  write_stream->Write(mismatched_data_request);

  ni::data_monikers::MonikerReadResponse read_result;
  EXPECT_FALSE(write_stream->Read(&read_result)) << "Server should have closed the stream with an error";

  auto status = write_stream->Finish();
  EXPECT_EQ(status.error_code(), grpc::StatusCode::INVALID_ARGUMENT);
  EXPECT_THAT(status.error_message(), HasSubstr("Value count does not match writer count"));
}

TEST_F(NiFakeDAQmxStreamingTests, MismatchedValueCount_StreamWrite_ReturnsInvalidArgument)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  auto begin_write_digital_u32_response = nidaqmx_grpc::experimental::client::begin_write_digital_u32(stub(), *session, 10, TRUE, 0, DAQmx_Val_GroupByChannel);
  auto write_moniker_u32 = new ni::data_monikers::Moniker(begin_write_digital_u32_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest setup_request;
  setup_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_u32);

  auto write_stream = moniker_stub().get()->StreamWrite(&moniker_context);
  write_stream->Write(setup_request);

  // One write moniker is configured, but no values are provided in the payload.
  ni::data_monikers::MonikerWriteRequest mismatched_data_request;
  write_stream->Write(mismatched_data_request);

  write_stream->WritesDone();
  auto status = write_stream->Finish();
  EXPECT_EQ(status.error_code(), grpc::StatusCode::INVALID_ARGUMENT);
  EXPECT_THAT(status.error_message(), HasSubstr("Value count does not match writer count"));
}
}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/ni_fake_fpga_streaming_tests.cpp sha256=8c92a92b0fd88bcb9272d90f8df9a2f56702c7a296749a346a0002036d65365d bytes=21572 -->
## FILE: source/tests/integration/ni_fake_fpga_streaming_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/ni_fake_fpga_streaming_tests.cpp`
- sha256: `8c92a92b0fd88bcb9272d90f8df9a2f56702c7a296749a346a0002036d65365d`
- bytes: 21572

````cpp
#include <../generated/nifpga/nifpga_mock_library.h>
#include <NiFpga.h>
#include <gmock/gmock-spec-builders.h>
#include <google/protobuf/stubs/port.h>
#include <grpcpp/client_context.h>
#include <grpcpp/server_builder.h>
#include <gtest/gtest.h>
#include <nifpga.grpc.pb.h>
#include <nifpga.pb.h>
#include <nifpga/nifpga_service.h>
#include <register_all_services.h>
#include <server/data_moniker_service.h>
#include <server/session_resource_repository.h>
#include <sideband_grpc.h>

#include <thread>

#include "../generated/nifpga/nifpga_client.h"

namespace ni {
namespace tests {
namespace integration {

using namespace ::testing;
using namespace nidevice_grpc;
namespace pb = ::google::protobuf;
using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

// This test class is used to test the NiFpgaService using a using a mocked fpga library(NiFpgaMockLibrary)
// We intend to use this class to test streaming apis in NiFpgaService
class NiFakeFpgaStreamingTests : public ::testing::Test {
 private:
  grpc::ServerBuilder builder_;
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::shared_ptr<ni::tests::unit::NiFpgaMockLibrary> library_;
  std::shared_ptr<std::vector<std::shared_ptr<void>>> services_;
  std::shared_ptr<nifpga_grpc::NiFpgaService> fpgaService_;
  std::shared_ptr<ni::data_monikers::DataMonikerService> moniker_service_;
  std::unique_ptr<::grpc::Server> server_;
  std::unique_ptr<nifpga_grpc::NiFpga::Stub> stub_;
  std::unique_ptr<ni::data_monikers::DataMoniker::Stub> moniker_service_stub_;
  std::thread* sideband_socket_thread_;
  std::atomic<bool> shutdown_{false};

 public:
  NiFakeFpgaStreamingTests()
  {
    session_repository_ = std::make_shared<nidevice_grpc::SessionRepository>();
    library_ = std::make_shared<ni::tests::unit::NiFpgaMockLibrary>();
    auto ni_fpga_session_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<NiFpga_Session>>(session_repository_);
    fpgaService_ = std::make_shared<nifpga_grpc::NiFpgaService>(library_, ni_fpga_session_repository, FeatureToggles({}, CodeReadiness::kNextRelease));
    moniker_service_ = std::make_shared<ni::data_monikers::DataMonikerService>();
    server_ = start_server();
    nifpga_grpc::RegisterMonikerEndpoints();
    stub_ = nifpga_grpc::NiFpga::NewStub(server_->InProcessChannel(::grpc::ChannelArguments()));
    moniker_service_stub_ = ni::data_monikers::DataMoniker::NewStub(server_->InProcessChannel(::grpc::ChannelArguments()));
    Mock::AllowLeak(library_.get());

    // TODO: Implement sideband socket thread when we could support testing sideband streaming inprocess
    // sideband_socket_thread_ = new std::thread(RunSidebandSocketsAccept, "localhost", 50055);
  }

  virtual ~NiFakeFpgaStreamingTests()
  {
    shutdown();
  }

  void shutdown()
  {
    if (!shutdown_) {
      shutdown_ = true;
      server_->Shutdown();
    }
  }

  std::unique_ptr<nifpga_grpc::NiFpga::Stub>& stub()
  {
    return stub_;
  }

  std::unique_ptr<ni::data_monikers::DataMoniker::Stub>& moniker_stub()
  {
    return moniker_service_stub_;
  }

  std::shared_ptr<ni::tests::unit::NiFpgaMockLibrary> library()
  {
    return library_;
  }

  std::unique_ptr<::grpc::Server> start_server()
  {
    ::grpc::ServerBuilder builder;
    builder.RegisterService(fpgaService_.get());
    builder.RegisterService(moniker_service_.get());
    return builder.BuildAndStart();
  }
};

TEST_F(NiFakeFpgaStreamingTests, StreamRead_scalar)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), ReadI16(_, 0, ::testing::_))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(1), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(2), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(3), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(4), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(5), ::testing::Return(0)))
      .WillRepeatedly(::testing::DoAll(::testing::SetArgPointee<2>(999), ::testing::Return(0)));
  EXPECT_CALL(*library(), ReadI64(_, 0, ::testing::_))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(11), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(12), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(13), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(14), ::testing::Return(0)))
      .WillOnce(::testing::DoAll(::testing::SetArgPointee<2>(15), ::testing::Return(0)))
      .WillRepeatedly(::testing::DoAll(::testing::SetArgPointee<2>(999), ::testing::Return(0)));

  // Dont worry about deleting read_moniker_i16 and read_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_i16_response = nifpga_grpc::experimental::client::begin_read_i16(stub(), *session, 0);
  ni::data_monikers::Moniker* read_moniker_i16 = new ni::data_monikers::Moniker(begin_read_i16_response.moniker());
  auto begin_read_i64_response = nifpga_grpc::experimental::client::begin_read_i64(stub(), *session, 0);
  ni::data_monikers::Moniker* read_moniker_i64 = new ni::data_monikers::Moniker(begin_read_i64_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerList read_requests;
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_i16);
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_i64);

  auto stream = moniker_stub().get()->StreamRead(&moniker_context, read_requests);

  for (int i = 0; i < 5; i++) {
    // Read data
    nifpga_grpc::MonikerReadI16Response read_value_i16;
    nifpga_grpc::MonikerReadI64Response read_value_i64;

    ni::data_monikers::MonikerReadResponse read_result;
    stream->Read(&read_result);

    read_result.data().values(0).UnpackTo(&read_value_i16);
    EXPECT_EQ(read_value_i16.value(), i + 1);
    read_result.data().values(1).UnpackTo(&read_value_i64);
    EXPECT_EQ(read_value_i64.value(), i + 11);
  }

  moniker_context.TryCancel();
}

TEST_F(NiFakeFpgaStreamingTests, StreamRead_Array)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // create some data for the array
  std::vector<int16_t> data_int_i16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<int64_t> data_int_i64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int size_i16 = data_int_i16.size();
  int size_i64 = data_int_i64.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), ReadArrayI16(_, 0, ::testing::_, size_i16))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(data_int_i16.begin(), data_int_i16.begin() + size_i16), ::testing::Return(0)));
  EXPECT_CALL(*library(), ReadArrayI64(_, 0, ::testing::_, 9))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(data_int_i64.begin(), data_int_i64.begin() + size_i64), ::testing::Return(0)));

  // Dont worry about deleting read_moniker_i16 and read_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_i16_array_response = nifpga_grpc::experimental::client::begin_read_array_i16(stub(), *session, 0, 10);
  auto read_moniker_i16 = new ni::data_monikers::Moniker(begin_read_i16_array_response.moniker());

  auto begin_read_i64_response = nifpga_grpc::experimental::client::begin_read_array_i64(stub(), *session, 0, 9);
  auto read_moniker_i64 = new ni::data_monikers::Moniker(begin_read_i64_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerList read_requests;
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_i16);
  read_requests.mutable_read_monikers()->AddAllocated(read_moniker_i64);

  auto stream = moniker_stub().get()->StreamRead(&moniker_context, read_requests);

  for (int i = 0; i < 5; i++) {
    // Read data
    nifpga_grpc::MonikerReadArrayI16Response read_values_i16;
    nifpga_grpc::MonikerReadArrayI64Response read_values_i64;

    ni::data_monikers::MonikerReadResponse read_result;
    stream->Read(&read_result);

    read_result.data().values(0).UnpackTo(&read_values_i16);
    read_result.data().values(1).UnpackTo(&read_values_i64);
    ASSERT_THAT(read_values_i16.array(), SizeIs(10));
    ASSERT_THAT(read_values_i16.array(), ElementsAreArray(data_int_i16));
    ASSERT_THAT(read_values_i64.array(), SizeIs(9));
    ASSERT_THAT(read_values_i64.array(), ElementsAreArray(data_int_i64));
  }

  moniker_context.TryCancel();
}

TEST_F(NiFakeFpgaStreamingTests, StreamWrite_Array)
{
  // create some setup for writing
  auto session = std::make_unique<nidevice_grpc::Session>();
  std::vector<pb::int16> data_int_i16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<pb::int64> data_int_i64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int control = 1;
  int size_i16 = data_int_i16.size();
  int size_i64 = data_int_i64.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), WriteArrayI16(_, control, _, size_i16))
      .With(Args<2, 3>(ElementsAreArray(data_int_i16)))
      .WillRepeatedly(::testing::Return(0));
  EXPECT_CALL(*library(), WriteArrayI64(_, control, _, size_i64))
      .With(Args<2, 3>(ElementsAreArray(data_int_i64)))
      .WillRepeatedly(::testing::Return(0));

  // Dont worry about deleting write_moniker_i16 and write_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_write_i16_array_response = nifpga_grpc::experimental::client::begin_write_array_i16(stub(), *session, control);
  auto write_moniker_i16 = new ni::data_monikers::Moniker(begin_write_i16_array_response.moniker());
  auto begin_write_i64_response = nifpga_grpc::experimental::client::begin_write_array_i64(stub(), *session, control);
  auto write_moniker_i64 = new ni::data_monikers::Moniker(begin_write_i64_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest write_request;
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i16);
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i64);

  auto write_stream = moniker_stub().get()->StreamWrite(&moniker_context);
  write_stream->Write(write_request);

  for (int i = 0; i < 5; i++) {
    // Write data
    nifpga_grpc::MonikerWriteArrayI16Request  write_values_array_i16;
    nifpga_grpc::MonikerWriteArrayI64Request  write_values_array_i64;

    write_values_array_i16.mutable_array()->Add(data_int_i16.begin(), data_int_i16.end());
    write_values_array_i64.mutable_array()->Add(data_int_i64.begin(), data_int_i64.end());

    ni::data_monikers::MonikerWriteRequest write_data_request;
    write_data_request.mutable_data()->add_values()->PackFrom(write_values_array_i16);
    write_data_request.mutable_data()->add_values()->PackFrom(write_values_array_i64);

    write_stream->Write(write_data_request);
  }

  write_stream->WritesDone();
  moniker_context.TryCancel();
}

TEST_F(NiFakeFpgaStreamingTests, StreamReadWrite_Array)
{
  auto session = std::make_unique<nidevice_grpc::Session>();

  // create some data for the array
  std::vector<pb::int16> write_data_int16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<pb::int64> write_data_int64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int control = 1;
  int write_size_i16 = write_data_int16.size();
  int write_size_i64 = write_data_int64.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), WriteArrayI16(_, control, _, write_size_i16))
      .With(Args<2, 3>(ElementsAreArray(write_data_int16)))
      .WillRepeatedly(::testing::Return(0));
  EXPECT_CALL(*library(), WriteArrayI64(_, control, _, write_size_i64))
      .With(Args<2, 3>(ElementsAreArray(write_data_int64)))
      .WillRepeatedly(::testing::Return(0));

  // create some setup for reading
  std::vector<int16_t> read_data_int16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<int64_t> read_data_int64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int read_size_i16 = read_data_int16.size();
  int read_size_i64 = read_data_int64.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), ReadArrayI16(_, 0, ::testing::_, 10))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(read_data_int16.begin(), read_data_int16.begin() + read_size_i16), ::testing::Return(0)));
  EXPECT_CALL(*library(), ReadArrayI64(_, 0, ::testing::_, 9))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(read_data_int64.begin(), read_data_int64.begin() + read_size_i64), ::testing::Return(0)));

  // Dont worry about deleting write_moniker_i16 and write_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_write_i16_array_response = nifpga_grpc::experimental::client::begin_write_array_i16(stub(), *session, control);
  auto write_moniker_i16 = new ni::data_monikers::Moniker(begin_write_i16_array_response.moniker());
  auto begin_write_i64_response = nifpga_grpc::experimental::client::begin_write_array_i64(stub(), *session, control);
  auto write_moniker_i64 = new ni::data_monikers::Moniker(begin_write_i64_response.moniker());

  // Dont worry about deleting read_moniker_i16 and read_moniker_i64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_i16_array__response = nifpga_grpc::experimental::client::begin_read_array_i16(stub(), *session, 0, read_data_int16.size());
  auto read_moniker_i16 = new ni::data_monikers::Moniker(begin_read_i16_array__response.moniker());
  auto begin_read_i64_response = nifpga_grpc::experimental::client::begin_read_array_i64(stub(), *session, 0, read_data_int64.size());
  auto read_moniker_i64 = new ni::data_monikers::Moniker(begin_read_i64_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::MonikerWriteRequest write_request;
  write_request.mutable_monikers()->mutable_read_monikers()->AddAllocated(read_moniker_i16);
  write_request.mutable_monikers()->mutable_read_monikers()->AddAllocated(read_moniker_i64);
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i16);
  write_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i64);

  auto write_stream = moniker_stub().get()->StreamReadWrite(&moniker_context);
  write_stream->Write(write_request);

  for (int i = 0; i < 5; i++) {
    // Write data
    nifpga_grpc::MonikerWriteArrayI16Request write_values_array_i16;
    nifpga_grpc::MonikerWriteArrayI64Request write_values_array_i64;

    write_values_array_i16.mutable_array()->Add(write_data_int16.begin(), write_data_int16.end());
    write_values_array_i64.mutable_array()->Add(write_data_int64.begin(), write_data_int64.end());

    ni::data_monikers::MonikerWriteRequest write_data_request;
    write_data_request.mutable_data()->add_values()->PackFrom(write_values_array_i16);
    write_data_request.mutable_data()->add_values()->PackFrom(write_values_array_i64);

    write_stream->Write(write_data_request);

    nifpga_grpc::MonikerReadArrayI16Response read_values_i16;
    nifpga_grpc::MonikerReadArrayI64Response read_values_i64;

    ni::data_monikers::MonikerReadResponse read_result;
    write_stream->Read(&read_result);

    read_result.data().values(0).UnpackTo(&read_values_i16);
    read_result.data().values(1).UnpackTo(&read_values_i64);
    ASSERT_THAT(read_values_i16.array(), SizeIs(read_size_i16));
    ASSERT_THAT(read_values_i16.array(), ElementsAreArray(read_data_int16));
    ASSERT_THAT(read_values_i64.array(), SizeIs(read_size_i64));
    ASSERT_THAT(read_values_i64.array(), ElementsAreArray(read_data_int64));
  }

  write_stream->WritesDone();
  moniker_context.TryCancel();
}

// disable this test since we are not supporting sideband streaming inprocess

TEST_F(NiFakeFpgaStreamingTests, DISABLED_SidebandStreamReadWrite_Array)
{
  auto session = std::make_unique<nidevice_grpc::Session>();
  // create some data for the array
  std::vector<pb::int16> write_data_int16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<pb::int64> write_data_int64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  int control = 1;
  int size_i16 = write_data_int16.size();
  int size_i64 = write_data_int64.size();

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), WriteArrayI16(_, control, _, size_i16))
      .With(Args<2, 3>(ElementsAreArray(write_data_int16)))
      .WillRepeatedly(::testing::Return(0));
  EXPECT_CALL(*library(), WriteArrayI64(_, control, _, size_i64))
      .With(Args<2, 3>(ElementsAreArray(write_data_int64)))
      .WillRepeatedly(::testing::Return(0));

  // create some setup for reading
  std::vector<pb::int16> data_int16 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::vector<pb::int64> data_int64 = {11, 22, 33, 44, 55, 66, 77, 88, 99};

  // Set expectation on the mocked fpga lib method.
  EXPECT_CALL(*library(), ReadArrayI16(_, 0, ::testing::_, 10))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(data_int16.begin(), data_int16.begin() + 10), ::testing::Return(0)));
  EXPECT_CALL(*library(), ReadArrayI64(_, 0, ::testing::_, 9))
      .WillRepeatedly(::testing::DoAll(::testing::SetArrayArgument<2>(data_int64.begin(), data_int64.begin() + 9), ::testing::Return(0)));

  // Dont worry about deleting read_moniker16 and read_moniker64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_write_i16_array_response = nifpga_grpc::experimental::client::begin_write_array_i16(stub(), *session, control);
  auto write_moniker_i16 = new ni::data_monikers::Moniker(begin_write_i16_array_response.moniker());
  auto begin_write_i64_response = nifpga_grpc::experimental::client::begin_write_array_i64(stub(), *session, control);
  auto write_moniker_i64 = new ni::data_monikers::Moniker(begin_write_i64_response.moniker());

  // Dont worry about deleting read_moniker16 and read_moniker64 since AddAllocated takes ownership of the ptr being passed in ensuring its destruction.
  auto begin_read_i16_array__response = nifpga_grpc::experimental::client::begin_read_array_i16(stub(), *session, 0, data_int16.size());
  auto read_moniker_i16 = new ni::data_monikers::Moniker(begin_read_i16_array__response.moniker());
  auto begin_read_i64_response = nifpga_grpc::experimental::client::begin_read_array_i64(stub(), *session, 0, data_int64.size());
  auto read_moniker_i64 = new ni::data_monikers::Moniker(begin_read_i64_response.moniker());

  grpc::ClientContext moniker_context;
  ni::data_monikers::BeginMonikerSidebandStreamRequest sideband_request;
  ni::data_monikers::BeginMonikerSidebandStreamResponse sideband_response;
  sideband_request.set_strategy(ni::data_monikers::SidebandStrategy::SOCKETS);
  sideband_request.mutable_monikers()->mutable_read_monikers()->AddAllocated(read_moniker_i16);
  sideband_request.mutable_monikers()->mutable_read_monikers()->AddAllocated(read_moniker_i64);
  sideband_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i16);
  sideband_request.mutable_monikers()->mutable_write_monikers()->AddAllocated(write_moniker_i64);

  auto write_stream = moniker_stub().get()->BeginSidebandStream(&moniker_context, sideband_request, &sideband_response);
  auto sideband_token = InitClientSidebandData(sideband_response);

  for (int i = 0; i < 5; i++) {
    // Write data
    nifpga_grpc::MonikerWriteArrayI16Request write_values_array_i16;
    nifpga_grpc::MonikerWriteArrayI64Request write_values_array_i64;

    write_values_array_i16.mutable_array()->Add(write_data_int16.begin(), write_data_int16.end());
    write_values_array_i64.mutable_array()->Add(write_data_int64.begin(), write_data_int64.end());

    ni::data_monikers::SidebandWriteRequest write_data_request;
    write_data_request.mutable_values()->add_values()->PackFrom(write_values_array_i16);
    write_data_request.mutable_values()->add_values()->PackFrom(write_values_array_i64);

    WriteSidebandMessage(sideband_token, write_data_request);

    nifpga_grpc::MonikerReadArrayI16Response read_values_i16;
    nifpga_grpc::MonikerReadArrayI64Response read_values_i64;

    ni::data_monikers::SidebandReadResponse read_result;
    ReadSidebandMessage(sideband_token, &read_result);

    read_result.values().values(0).UnpackTo(&read_values_i16);
    read_result.values().values(1).UnpackTo(&read_values_i64);
    ASSERT_THAT(read_values_i16.array(), SizeIs(10));
    ASSERT_THAT(read_values_i16.array(), ElementsAreArray(data_int16));
    ASSERT_THAT(read_values_i64.array(), SizeIs(9));
    ASSERT_THAT(read_values_i64.array(), ElementsAreArray(data_int64));
  }

  ni::data_monikers::SidebandWriteRequest cancel_request;
  cancel_request.set_cancel(true);
  WriteSidebandMessage(sideband_token, cancel_request);
  CloseSidebandData(sideband_token);
}

}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/ni_fake_non_ivi_service_tests_endtoend.cpp sha256=1fdf31535d99a73270847b7a4764156273e4e2a35caaa167975a11404c993672 bytes=18448 -->
## FILE: source/tests/integration/ni_fake_non_ivi_service_tests_endtoend.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/ni_fake_non_ivi_service_tests_endtoend.cpp`
- sha256: `1fdf31535d99a73270847b7a4764156273e4e2a35caaa167975a11404c993672`
- bytes: 18448

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <nifake_non_ivi/nifake_non_ivi_mock_library.h>
#include <nifake_non_ivi/nifake_non_ivi_service.h>

#include <atomic>
#include <memory>
#include <thread>

#include <tests/utilities/async_helpers.h>

namespace ni {
namespace tests {
namespace integration {

using namespace ::testing;
using namespace nifake_non_ivi_grpc;

static const char* const kStartOutOfRangeErrorMessage = "The value for start is out of range.";
static const char* const kStopOutOfRangeErrorMessage = "The value for stop is out of range.";
static const char* const kStartAndStopReversedErrorMessage = "The values for start and stop are reversed.";

// Test NiFakeNonIviService using a client stub.
class NiFakeNonIviServiceTests_EndToEnd : public ::testing::Test {
 public:
  using FakeResourceRepository = nidevice_grpc::SessionResourceRepository<FakeHandle>;
  using SecondaryResourceRepository = nidevice_grpc::SessionResourceRepository<SecondarySessionHandle>;
  using FakeCrossDriverResourceRepository = nidevice_grpc::SessionResourceRepository<FakeCrossDriverHandle>;
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::shared_ptr<nidevice_grpc::SessionRepository> secondary_session_repository_;
  std::shared_ptr<FakeResourceRepository> resource_repository_;
  std::shared_ptr<SecondaryResourceRepository> secondary_resource_repository_;
  std::shared_ptr<ni::tests::unit::NiFakeNonIviMockLibrary> library_;
  NiFakeNonIviService service_;
  std::unique_ptr<::grpc::Server> server_;
  std::unique_ptr<NiFakeNonIvi::Stub> stub_;
  std::atomic<bool> shutdown_{false};

  NiFakeNonIviServiceTests_EndToEnd()
      : session_repository_(std::make_shared<nidevice_grpc::SessionRepository>()),
        resource_repository_(std::make_shared<FakeResourceRepository>(session_repository_)),
        secondary_session_repository_(std::make_shared<nidevice_grpc::SessionRepository>()),
        secondary_resource_repository_(std::make_shared<SecondaryResourceRepository>(secondary_session_repository_)),
        library_(std::make_shared<ni::tests::unit::NiFakeNonIviMockLibrary>()),
        service_(library_, resource_repository_, std::make_shared<FakeCrossDriverResourceRepository>(session_repository_), std::make_shared<FakeCrossDriverResourceRepository>(secondary_session_repository_)),
        server_(start_server()),
        stub_(NiFakeNonIvi::NewStub(server_->InProcessChannel(::grpc::ChannelArguments())))
  {
  }

  virtual ~NiFakeNonIviServiceTests_EndToEnd()
  {
    shutdown();
  }

  void shutdown()
  {
    if (!shutdown_) {
      shutdown_ = true;
      server_->Shutdown();
    }
  }

  std::unique_ptr<::grpc::Server> start_server()
  {
    ::grpc::ServerBuilder builder;
    builder.RegisterService(&service_);
    return builder.BuildAndStart();
  }

  std::unique_ptr<NiFakeNonIvi::Stub>& stub()
  {
    return stub_;
  }

  auto start_read_stream(
    ::grpc::ClientContext& context,
    int32_t start,
    int32_t stop)
  {
    ReadStreamRequest request;
    request.set_start(start);
    request.set_stop(stop);
    return stub()->ReadStream(&context, request);
  }

  auto async_start_read_stream(
    ::grpc::ClientContext& context,
    ::grpc::CompletionQueue& completion_queue,
    void* tag,
    int32_t start,
    int32_t stop)
  {
    ReadStreamRequest request;
    request.set_start(start);
    request.set_stop(stop);
    return stub()->AsyncReadStream(&context, request, &completion_queue, tag);
  }

  template <typename TResponse>
  bool read_stream(
    ::grpc::ClientReader<TResponse>& reader,
    size_t count,
    std::vector<TResponse>* responses = nullptr)
  {
    TResponse response;
    for (size_t i = 0; i < count; ++i) {
      if (!reader.Read(&response)) {
        return false;
      }
      if (responses) {
        responses->push_back(response);
      }
    }
    return true;
  }

  size_t get_range_length(int32_t start, int32_t stop)
  {
    return static_cast<size_t>(stop - start + 1);
  }

  std::vector<int32_t> make_range(int32_t start, int32_t stop)
  {
    std::vector<int32_t> range;
    range.reserve(get_range_length(start, stop));
    for (int32_t i = start; i <= stop; ++i) {
      range.push_back(i);
    }
    return range;
  }

  std::vector<int32_t> get_values(const std::vector<ReadStreamResponse>& responses) {
    std::vector<int32_t> values;
    for (auto& response : responses) {
      values.push_back(response.value());
    }
    return values;
  }
};

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadStream_ReturnsExpectedSequence)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 100;
  auto reader = start_read_stream(context, START, STOP);
  auto expected_values = make_range(START, STOP);

  std::vector<ReadStreamResponse> responses;
  bool read_success = read_stream(*reader, expected_values.size(), &responses);

  EXPECT_TRUE(read_success);
  EXPECT_THAT(get_values(responses), ContainerEq(expected_values));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadPartialStream_ReturnsExpectedSequence)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 100;
  auto reader = start_read_stream(context, START, STOP);
  auto expected_values = make_range(START, STOP / 2);

  std::vector<ReadStreamResponse> responses;
  bool read_success = read_stream(*reader, expected_values.size(), &responses);

  EXPECT_TRUE(read_success);
  EXPECT_THAT(get_values(responses), ContainerEq(expected_values));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadTwoStreamsConsecutively_ReturnsExpectedSequences)
{
  ::grpc::ClientContext context1, context2;
  const auto START = 0;
  const auto STOP = 100;
  const auto OFFSET = 100;
  auto reader1 = start_read_stream(context1, START, STOP);
  auto reader2 = start_read_stream(context2, START + OFFSET, STOP + OFFSET);
  reader1->WaitForInitialMetadata();
  reader2->WaitForInitialMetadata();
  auto expected_values1 = make_range(START, STOP);
  auto expected_values2 = make_range(START + OFFSET, STOP + OFFSET);

  std::vector<ReadStreamResponse> responses1, responses2;
  bool read_success1 = read_stream(*reader1, expected_values1.size(), &responses1);
  bool read_success2 = read_stream(*reader2, expected_values2.size(), &responses2);

  EXPECT_TRUE(read_success1);
  EXPECT_TRUE(read_success2);
  EXPECT_THAT(get_values(responses1), ContainerEq(expected_values1));
  EXPECT_THAT(get_values(responses2), ContainerEq(expected_values2));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadPartialStream_ShutdownServerBeforeCancel_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 100;
  auto reader = start_read_stream(context, START, STOP);
  ASSERT_TRUE(read_stream(*reader, get_range_length(START, STOP / 2)));

  shutdown();
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadStream_ShutdownServerBeforeCancel_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 100;
  auto reader = start_read_stream(context, START, STOP);
  ASSERT_TRUE(read_stream(*reader, get_range_length(START, STOP)));

  shutdown();
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, ReadTwoStreamsInterleaved_ReturnsExpectedSequences)
{
  ::grpc::ClientContext context1, context2;
  const auto START = 0;
  const auto STOP = 100;
  const auto OFFSET = 100;
  auto reader1 = start_read_stream(context1, START, STOP);
  auto reader2 = start_read_stream(context2, START + OFFSET, STOP + OFFSET);
  reader1->WaitForInitialMetadata();
  reader2->WaitForInitialMetadata();
  auto expected_values1 = make_range(START, STOP);
  auto expected_values2 = make_range(START + OFFSET, STOP + OFFSET);

  std::vector<ReadStreamResponse> responses1, responses2;
  bool read_success1 = true, read_success2 = true;
  for (auto i = START; i <= STOP; ++i) {
    read_success1 = read_success1 && read_stream(*reader1, 1, &responses1);
    read_success2 = read_success2 && read_stream(*reader2, 1, &responses2);
  }

  EXPECT_TRUE(read_success1);
  EXPECT_TRUE(read_success2);
  EXPECT_THAT(get_values(responses1), ContainerEq(expected_values1));
  EXPECT_THAT(get_values(responses2), ContainerEq(expected_values2));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, StartReadStream_ShutdownBeforeRead_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);

  reader.reset();
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, WaitForMetadata_Cancel_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);
  reader->WaitForInitialMetadata();

  reader.reset();
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, WaitForMetadata_ShutdownAndRead_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 0;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);
  reader->WaitForInitialMetadata();

  shutdown();
  (void) read_stream(*reader, get_range_length(START, STOP));
}

const auto CALLBACK_DATA_OUT = 1234;
ACTION(ImmediatelyCallCallback)
{
  auto& callback_function = arg1;
  auto& callback_token = arg2;
  callback_function(CALLBACK_DATA_OUT, callback_token);
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, RegisterCallbackAndImmediatelyCall_ReadAsyncResponse_CallbackDataIncludedInResponse)
{
  const myInt16 TEST_VALUE = 25;
  ::grpc::ClientContext context;
  RegisterCallbackRequest request;
  request.set_input_data(TEST_VALUE);
  EXPECT_CALL(*library_, RegisterCallback(TEST_VALUE, _, _))
      .WillOnce(DoAll(
          ImmediatelyCallCallback(),
          Return(kDriverSuccess)));
  auto reader = stub()->RegisterCallback(&context, request);
  reader->WaitForInitialMetadata();

  RegisterCallbackResponse response;
  bool read_success = reader->Read(&response);

  EXPECT_TRUE(read_success);
  EXPECT_EQ(kDriverSuccess, response.status());
  EXPECT_EQ(CALLBACK_DATA_OUT, response.data_out());
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, InvalidArgument_ReadStream_ReturnsInvalidArgumentError)
{
  ::grpc::ClientContext context;
  const auto START = -1;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);

  bool read_success = read_stream(*reader, 1);

  EXPECT_FALSE(read_success);
  auto status = reader->Finish();
  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
  EXPECT_EQ(kStartOutOfRangeErrorMessage, status.error_message());
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, InvalidArgument_Finish_ReturnsInvalidArgumentError)
{
  ::grpc::ClientContext context;
  const auto START = -1;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);

  auto status = reader->Finish();

  EXPECT_EQ(::grpc::INVALID_ARGUMENT, status.error_code());
  EXPECT_EQ(kStartOutOfRangeErrorMessage, status.error_message());
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, InvalidArgument_Cancel_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = -1;
  const auto STOP = 10;
  auto reader = start_read_stream(context, START, STOP);

  context.TryCancel();
}

// When NiFakeNonIviService::ReadStream() reports a "start and stop reversed" error, it adds an
// arbitrary 100 ms delay before returning the error. WaitForInitialMetadata() should wait for
// this delay to complete.

TEST_F(NiFakeNonIviServiceTests_EndToEnd, StartAndStopReversedAndWaitForMetadata_ReadStream_ReturnsStartAndStopReversedError)
{
  ::grpc::ClientContext context;
  const auto START = 10;
  const auto STOP = 0;
  auto reader = start_read_stream(context, START, STOP);
  reader->WaitForInitialMetadata();

  bool read_success = read_stream(*reader, 1);

  EXPECT_FALSE(read_success);
  auto status = reader->Finish();
  EXPECT_EQ(::grpc::UNKNOWN, status.error_code());
  EXPECT_EQ(kStartAndStopReversedErrorMessage, status.error_message());
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, StartAndStopReversedAndWaitForMetadata_Finish_ReturnsStartAndStopReversedError)
{
  ::grpc::ClientContext context;
  const auto START = 10;
  const auto STOP = 0;
  auto reader = start_read_stream(context, START, STOP);
  reader->WaitForInitialMetadata();

  auto status = reader->Finish();

  EXPECT_EQ(::grpc::UNKNOWN, status.error_code());
  EXPECT_EQ(kStartAndStopReversedErrorMessage, status.error_message());
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, StartAndStopReversedAndWaitForMetadata_Cancel_CleanShutdown)
{
  ::grpc::ClientContext context;
  const auto START = 10;
  const auto STOP = 0;
  auto reader = start_read_stream(context, START, STOP);
  reader->WaitForInitialMetadata();

  context.TryCancel();
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, AsyncReadStream_ReturnsExpectedSequence)
{
  ::grpc::ClientContext context;
  ::grpc::CompletionQueue completion_queue;
  const auto START = 0;
  const auto STOP = 100;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_TAG = (void*)2;
  auto reader = async_start_read_stream(context, completion_queue, START_CALL_TAG, START, STOP);
  auto expected_values = make_range(START, STOP);

  ReadStreamResponse response;
  reader->Read(&response, READ_TAG);
  std::vector<ReadStreamResponse> responses;
  bool read_success = true;
  while (read_success && responses.size() < expected_values.size()) {
    auto completion = get_next_completion(completion_queue);
    if (get_completion_tag(completion) == START_CALL_TAG) {
       ASSERT_TRUE(is_completion_ok(completion));
    }
    else if (get_completion_tag(completion) == READ_TAG) {
      read_success = read_success && is_completion_ok(completion);
      if (is_completion_ok(completion)) {
        responses.push_back(response);
        if (responses.size() < expected_values.size()) {
          reader->Read(&response, READ_TAG);
        }
      }
    }
    else {
      FAIL() << "Unexpected completion: " << PrintToString(completion);
    }
  }

  EXPECT_TRUE(read_success);
  EXPECT_THAT(get_values(responses), ContainerEq(expected_values));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, AsyncReadTwoStreams_ReturnsExpectedSequences)
{
  ::grpc::ClientContext context1, context2;
  ::grpc::CompletionQueue completion_queue;
  const auto START = 0;
  const auto STOP = 100;
  const auto OFFSET = 100;
  const auto START_CALL_TAG1 = (void*)1;
  const auto START_CALL_TAG2 = (void*)2;
  const auto READ_TAG1 = (void*)3;
  const auto READ_TAG2 = (void*)4;
  auto reader1 = async_start_read_stream(context1, completion_queue, START_CALL_TAG1, START, STOP);
  auto reader2 = async_start_read_stream(context2, completion_queue, START_CALL_TAG2, START + OFFSET, STOP + OFFSET);
  auto expected_values1 = make_range(START, STOP);
  auto expected_values2 = make_range(START + OFFSET, STOP + OFFSET);

  ReadStreamResponse response1, response2;
  reader1->Read(&response1, READ_TAG1);
  reader2->Read(&response2, READ_TAG2);
  std::vector<ReadStreamResponse> responses1, responses2;
  bool read_success1 = true, read_success2 = true;
  while (read_success1 && read_success2 && (responses1.size() < expected_values1.size() || responses2.size() < expected_values2.size())) {
    auto completion = get_next_completion(completion_queue);
    if (get_completion_tag(completion) == START_CALL_TAG1 || get_completion_tag(completion) == START_CALL_TAG2) {
       ASSERT_TRUE(is_completion_ok(completion));
    }
    else if (get_completion_tag(completion) == READ_TAG1) {
      read_success1 = read_success1 && is_completion_ok(completion);
      if (is_completion_ok(completion)) {
        responses1.push_back(response1);
        if (responses1.size() < expected_values1.size()) {
          reader1->Read(&response1, READ_TAG1);
        }
      }
    }
    else if (get_completion_tag(completion) == READ_TAG2) {
      read_success2 = read_success2 && is_completion_ok(completion);
      if (is_completion_ok(completion)) {
        responses2.push_back(response2);
        if (responses2.size() < expected_values2.size()) {
          reader2->Read(&response2, READ_TAG2);
        }
      }
    }
    else {
      FAIL() << "Unexpected completion: " << PrintToString(completion);
    }
  }

  EXPECT_TRUE(read_success1);
  EXPECT_TRUE(read_success2);
  EXPECT_THAT(get_values(responses1), ContainerEq(expected_values1));
  EXPECT_THAT(get_values(responses2), ContainerEq(expected_values2));
}

TEST_F(NiFakeNonIviServiceTests_EndToEnd, AsyncStartAndStopReversedAndWaitForMetadata_ReadStreamWithoutBlocking_ReturnsStartAndStopReversedErrorWithoutBlocking)
{
  ::grpc::ClientContext context;
  ::grpc::CompletionQueue completion_queue;
  const auto START = 10;
  const auto STOP = 0;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_INITIAL_METADATA_TAG = (void*)2;
  const auto READ_TAG = (void*)3;
  const auto FINISH_TAG = (void*)4;
  auto reader = async_start_read_stream(context, completion_queue, START_CALL_TAG, START, STOP);
  reader->ReadInitialMetadata(READ_INITIAL_METADATA_TAG);
  ASSERT_EQ(Completion(START_CALL_TAG, true), get_next_completion(completion_queue));
  ASSERT_EQ(Completion(READ_INITIAL_METADATA_TAG, true), get_next_completion(completion_queue));

  ReadStreamResponse response;
  reader->Read(&response, READ_TAG);
  Completion read_completion;
  bool read_completed = try_get_next_completion_without_blocking(completion_queue, read_completion);

  EXPECT_TRUE(read_completed);
  EXPECT_EQ(Completion(READ_TAG, false), read_completion); // read_completion should NOT be OK
  ::grpc::Status status;
  reader->Finish(&status, FINISH_TAG);
  Completion finish_completion;
  bool finish_completed = try_get_next_completion_without_blocking(completion_queue, finish_completion);
  EXPECT_TRUE(finish_completed);
  EXPECT_EQ(Completion(FINISH_TAG, true), finish_completion);
  EXPECT_EQ(::grpc::UNKNOWN, status.error_code());
  EXPECT_EQ(kStartAndStopReversedErrorMessage, status.error_message());
}

}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/ni_fake_service_tests_endtoend.cpp sha256=40c48e3e29f564236f9ba3794afce0b6cde9f2178250d93301f13201766783af bytes=3267 -->
## FILE: source/tests/integration/ni_fake_service_tests_endtoend.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/ni_fake_service_tests_endtoend.cpp`
- sha256: `40c48e3e29f564236f9ba3794afce0b6cde9f2178250d93301f13201766783af`
- bytes: 3267

````cpp
#include <gtest/gtest.h>
#include <nifake/nifake_client.h>
#include <nifake/nifake_mock_library.h>
#pragma warning(push)
#pragma warning(disable : 4616)
#pragma warning(disable : 4146)
#pragma warning(disable : 4244)
#include <nifake/nifake_service.h>
#pragma warning(pop)

#include <atomic>
#include <memory>
#include <thread>

namespace ni {
namespace tests {
namespace integration {

namespace client = nifake_grpc::experimental::client;
using namespace ::testing;
using namespace nifake_grpc;
const auto kDriverSuccess = 0U;

// Test NiFakeService using a client stub.
class NiFakeServiceTests_EndToEnd : public ::testing::Test {
 public:
  using FakeResourceRepository = nidevice_grpc::SessionResourceRepository<ViSession>;
  std::shared_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::shared_ptr<FakeResourceRepository> resource_repository_;
  std::shared_ptr<ni::tests::unit::NiFakeMockLibrary> library_;
  NiFakeService service_;
  std::unique_ptr<::grpc::Server> server_;
  std::unique_ptr<NiFake::Stub> stub_;
  std::atomic<bool> shutdown_{false};

  NiFakeServiceTests_EndToEnd()
      : session_repository_(std::make_shared<nidevice_grpc::SessionRepository>()),
        resource_repository_(std::make_shared<FakeResourceRepository>(session_repository_)),
        library_(std::make_shared<ni::tests::unit::NiFakeMockLibrary>()),
        service_(library_, resource_repository_),
        server_(start_server()),
        stub_(NiFake::NewStub(server_->InProcessChannel(::grpc::ChannelArguments())))
  {
  }

  virtual ~NiFakeServiceTests_EndToEnd()
  {
    shutdown();
  }

  void shutdown()
  {
    if (!shutdown_) {
      shutdown_ = true;
      server_->Shutdown();
    }
  }

  std::unique_ptr<::grpc::Server> start_server()
  {
    ::grpc::ServerBuilder builder;
    builder.RegisterService(&service_);
    return builder.BuildAndStart();
  }

  std::unique_ptr<NiFake::Stub>& stub()
  {
    return stub_;
  }
};

InitWithOptionsResponse init(const client::StubPtr& stub)
{
  return client::init_with_options(stub, "", false, false, "");
}

TEST_F(NiFakeServiceTests_EndToEnd, PassMappedEnumToGeneratedClient_PassesStringValueToLibraryAndSucceeds)
{
  auto init_response = init(stub());
  const auto EXPECTED = NIFAKE_VAL_ANDROID;
  EXPECT_CALL(*library_, StringValuedEnumInputFunctionWithDefaults(_, Pointee(*EXPECTED)))
      .WillOnce(Return(kDriverSuccess));
  auto response = client::string_valued_enum_input_function_with_defaults(stub(), init_response.vi(), MobileOSNames::MOBILE_OS_NAMES_ANDROID);

  EXPECT_EQ(kDriverSuccess, response.status());
}

TEST_F(NiFakeServiceTests_EndToEnd, PassMappedEnumRawValueToGeneratedClient_PassesStringValueToLibraryAndSucceeds)
{
  auto init_response = init(stub());
  const auto RAW_VALUE = NIFAKE_VAL_IOS;
  EXPECT_CALL(*library_, StringValuedEnumInputFunctionWithDefaults(_, Pointee(*RAW_VALUE)))
      .WillOnce(Return(kDriverSuccess));
  auto response = client::string_valued_enum_input_function_with_defaults(stub(), init_response.vi(), std::string(RAW_VALUE));

  EXPECT_EQ(kDriverSuccess, response.status());
}
}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/session_utilities_service_tests.cpp sha256=4321b2a3490c3ba2ea81c145bb2668acc5fd74cf51445d0adac2642a15eb27d4 bytes=28206 -->
## FILE: source/tests/integration/session_utilities_service_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/session_utilities_service_tests.cpp`
- sha256: `4321b2a3490c3ba2ea81c145bb2668acc5fd74cf51445d0adac2642a15eb27d4`
- bytes: 28206

````cpp
#include <grpcpp/impl/grpc_library.h>
#include <gtest/gtest.h>
#include <server/device_enumerator.h>
#include <server/software_enumerator.h>
#include <server/semaphore.h>
#include <server/session_repository.h>
#include <server/session_utilities_service.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>

#include <thread>

namespace ni {
namespace tests {
namespace integration {

using ::testing::Throw;

TEST(SessionUtilitiesServiceTests, SysCfgLibraryNotPresent_EnumerateDevices_ReturnsNotFoundGrpcStatusError)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  EXPECT_CALL(syscfg_mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));

  ::grpc::ServerContext context;
  nidevice_grpc::EnumerateDevicesRequest request;
  nidevice_grpc::EnumerateDevicesResponse response;
  ::grpc::Status status = service.EnumerateDevices(&context, &request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST(SessionUtilitiesServiceTests, SysCfgLibraryNotPresent_EnumerateInstalledSoftware_ReturnsNotFoundGrpcStatusError)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  EXPECT_CALL(syscfg_mock_library, InitializeSession)
      .WillOnce(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));

  ::grpc::ServerContext context;
  nidevice_grpc::EnumerateInstalledSoftwareRequest request;
  nidevice_grpc::EnumerateInstalledSoftwareResponse response;
  ::grpc::Status status = service.EnumerateInstalledSoftware(&context, &request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST(SessionUtilitiesServiceTests, EmptyReserveId_Reserve_ReturnsInvalidId)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest request;

  ::grpc::ServerContext context;
  nidevice_grpc::ReserveResponse response;
  ::grpc::Status status = service.Reserve(&context, &request, &response);

  EXPECT_FALSE(response.is_reserved());
  EXPECT_EQ(status.error_code(), ::grpc::INVALID_ARGUMENT);
}

TEST(SessionUtilitiesServiceTests, EmptyClientId_Reserve_ReturnsInvalidId)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest request;
  request.set_reservation_id("foo");

  ::grpc::ServerContext context;
  nidevice_grpc::ReserveResponse response;
  ::grpc::Status status = service.Reserve(&context, &request, &response);

  EXPECT_FALSE(response.is_reserved());
  EXPECT_EQ(status.error_code(), ::grpc::INVALID_ARGUMENT);
}

TEST(SessionUtilitiesServiceTests, NewReserveIdAndClientId_Reserve_ReservesSession)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest request;
  request.set_reservation_id("foo");
  request.set_client_id("a");

  ::grpc::ServerContext context;
  nidevice_grpc::ReserveResponse response;
  auto status = service.Reserve(&context, &request, &response);

  EXPECT_TRUE(response.is_reserved());
  EXPECT_EQ(status.error_code(), ::grpc::OK);
}

void call_reserve_task(
    nidevice_grpc::SessionUtilitiesService* service,
    nidevice_grpc::ReserveRequest* request,
    nidevice_grpc::ReserveResponse* response,
    ::grpc::Status* status,
    std::atomic<bool>* is_thread_started)
{
  ::grpc::ServerContext context;
  *is_thread_started = true;
  *status = service->Reserve(&context, request, response);
}

bool call_unreserve(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id, ::grpc::Status& status)
{
  nidevice_grpc::UnreserveRequest unreserve_request;
  unreserve_request.set_reservation_id(reservation_id);
  unreserve_request.set_client_id(client_id);
  nidevice_grpc::UnreserveResponse unreserve_response;
  ::grpc::ServerContext context;
  status = service->Unreserve(&context, &unreserve_request, &unreserve_response);
  return unreserve_response.is_unreserved();
}

bool call_unreserve(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id)
{
  ::grpc::Status status;
  return call_unreserve(service, reservation_id, client_id, status);
}

bool call_is_reserved(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id, ::grpc::Status& status)
{
  nidevice_grpc::IsReservedByClientRequest is_reserved_request;
  is_reserved_request.set_reservation_id(reservation_id);
  is_reserved_request.set_client_id(client_id);
  nidevice_grpc::IsReservedByClientResponse is_reserved_response;
  ::grpc::ServerContext context;
  status = service->IsReservedByClient(&context, &is_reserved_request, &is_reserved_response);
  return is_reserved_response.is_reserved();
}

bool call_is_reserved(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id)
{
  ::grpc::Status status;
  return call_is_reserved(service, reservation_id, client_id, status);
}

bool call_reserve(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id, ::grpc::Status& status)
{
  nidevice_grpc::ReserveRequest reserve_request;
  reserve_request.set_reservation_id("foo");
  reserve_request.set_client_id("a");
  ::grpc::ServerContext context;
  nidevice_grpc::ReserveResponse reserve_response;
  status = service->Reserve(&context, &reserve_request, &reserve_response);
  return reserve_response.is_reserved();
}

bool call_reserve(nidevice_grpc::SessionUtilitiesService* service, std::string reservation_id, std::string client_id)
{
  ::grpc::Status status;
  return call_reserve(service, reservation_id, client_id, status);
}

void set_reserve_request(nidevice_grpc::ReserveRequest& request, const char* reservation_id, const char* client_id)
{
  request.set_reservation_id(reservation_id);
  request.set_client_id(client_id);
}

void wait_until_true(
    const std::atomic<bool>& client_one_started,
    const std::atomic<bool>& client_two_started)
{
  while (!client_one_started || !client_two_started) {
    std::this_thread::sleep_for(std::chrono::milliseconds(5));
  }
  std::this_thread::sleep_for(std::chrono::milliseconds(5));
}

void wait_until_true(const std::atomic<bool>& client_started)
{
  const std::atomic<bool> true_atomic(true);
  wait_until_true(client_started, true_atomic);
}

TEST(SessionUtilitiesServiceTests, IdReserved_ReserveWithNewClientId_WaitsForUnreserveThenReserves)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  nidevice_grpc::ReserveRequest clientb_request;
  nidevice_grpc::ReserveResponse clientb_response;
  ::grpc::Status clientb_status;
  std::atomic<bool> clientb_started(false);
  set_reserve_request(clientb_request, "foo", "b");
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  wait_until_true(clientb_started);

  bool is_reserved = call_is_reserved(&service, "foo", "b");
  EXPECT_FALSE(clientb_response.is_reserved());
  EXPECT_FALSE(is_reserved);
  call_unreserve(&service, "foo", "a");
  reserve_b.join();
  EXPECT_TRUE(clientb_response.is_reserved());
  is_reserved = call_is_reserved(&service, "foo", "b");
  EXPECT_TRUE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, IdReserved_ReserveWithNewClientIdTwice_WaitsForTwoUnreservesThenReservesLastClient)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest request;
  call_reserve(&service, "foo", "a");

  nidevice_grpc::ReserveRequest clientb_request, clientc_request;
  nidevice_grpc::ReserveResponse clientb_response, clientc_response;
  ::grpc::Status clientb_status, clientc_status;
  std::atomic<bool> clientb_started(false), clientc_started(false);
  set_reserve_request(clientb_request, "foo", "b");
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  wait_until_true(clientb_started);
  set_reserve_request(clientc_request, "foo", "c");
  std::thread reserve_c(call_reserve_task, &service, &clientc_request, &clientc_response, &clientc_status, &clientc_started);
  wait_until_true(clientc_started);

  EXPECT_FALSE(clientc_response.is_reserved());
  call_unreserve(&service, "foo", "a");
  reserve_b.join();
  EXPECT_FALSE(clientc_response.is_reserved());
  call_unreserve(&service, "foo", "b");
  reserve_c.join();
  EXPECT_TRUE(clientc_response.is_reserved());
  EXPECT_TRUE(call_is_reserved(&service, "foo", "c"));
}

TEST(SessionUtilitiesServiceTests, IdReserved_ReserveWithSameClientId_ReturnsReserved)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest request;
  request.set_reservation_id("foo");
  request.set_client_id("a");
  ::grpc::ServerContext context;
  nidevice_grpc::ReserveResponse response;
  service.Reserve(&context, &request, &response);

  response.set_is_reserved(false);
  service.Reserve(&context, &request, &response);

  EXPECT_TRUE(response.is_reserved());
}

TEST(SessionUtilitiesServiceTests, IdReserved_ReserveWithSameClientId_ReturnsFailedPrecondition)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  ::grpc::Status status;
  call_reserve(&service, "foo", "a", status);

  EXPECT_EQ(status.error_code(), ::grpc::FAILED_PRECONDITION);
}

TEST(SessionUtilitiesServiceTests, NoReservations_IsReserved_ReturnsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);

  bool is_reserved = call_is_reserved(&service, "foo", "a");

  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_IsReservedWithDifferentReservationId_ReturnsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  bool is_reserved = call_is_reserved(&service, "bar", "a");

  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_IsReservedWithDifferentClientId_ReturnsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  bool is_reserved = call_is_reserved(&service, "foo", "b");

  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_IsReservedWithSameClientId_ReturnsTrue)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  ::grpc::Status status;
  bool is_reserved = call_is_reserved(&service, "foo", "a", status);

  EXPECT_EQ(status.error_code(), ::grpc::OK);
  EXPECT_TRUE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, NoReservations_Unreserve_ReturnsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);

  bool is_unreserved = call_unreserve(&service, "foo", "a");

  EXPECT_FALSE(is_unreserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_UnreserveWithDifferentReservationId_ReturnsFalseAndKeepsReservation)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest reserve_request;
  call_reserve(&service, "foo", "a");

  bool is_unreserved = call_unreserve(&service, "bar", "a");

  EXPECT_FALSE(is_unreserved);
  bool is_reserved = call_is_reserved(&service, "foo", "a");
  EXPECT_TRUE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_UnreserveWithDifferentClientId_ReturnsFalseAndKeepsReservation)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  bool is_unreserved = call_unreserve(&service, "foo", "b");

  EXPECT_FALSE(is_unreserved);
  bool is_reserved = call_is_reserved(&service, "foo", "a");
  EXPECT_TRUE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, Reservation_Unreserve_Unreserves)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  ::grpc::Status status;
  bool is_unreserved = call_unreserve(&service, "foo", "a", status);

  EXPECT_TRUE(is_unreserved);
  bool is_reserved = call_is_reserved(&service, "foo", "a");
  EXPECT_FALSE(is_reserved);
  EXPECT_EQ(status.error_code(), ::grpc::OK);
}

TEST(SessionUtilitiesServiceTests, Reservation_ResetServer_Unreserves)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  auto status = service.ResetServer(&context, NULL, &reset_response);

  EXPECT_TRUE(reset_response.is_server_reset());
  EXPECT_EQ(status.error_code(), ::grpc::OK);
  bool is_reserved = call_is_reserved(&service, "foo", "a");
  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, ReservationAndSession_ResetServer_UnreservesAndRemovesSession)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  std::string session_name = "session_name";
  int status = session_repository.add_session(
      session_name,
      []() { return 0; },
      NULL);
  call_reserve(&service, session_name, "a");

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  EXPECT_TRUE(reset_response.is_server_reset());
  bool is_reserved = call_is_reserved(&service, session_name, "a");
  EXPECT_FALSE(is_reserved);
  EXPECT_EQ("", session_repository.access_session(session_name));
}

TEST(SessionUtilitiesServiceTests, TwoReservations_ResetServer_Unreserves)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");
  call_reserve(&service, "bar", "b");

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  EXPECT_TRUE(reset_response.is_server_reset());
  bool is_a_reserved = call_is_reserved(&service, "foo", "a");
  EXPECT_FALSE(is_a_reserved);
  bool is_b_reserved = call_is_reserved(&service, "bar", "b");
  EXPECT_FALSE(is_b_reserved);
}

TEST(SessionUtilitiesServiceTests, ReservationWithClientWaiting_ResetServer_ClientReturnsAndDoesNotReserve)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");
  nidevice_grpc::ReserveRequest clientb_request;
  nidevice_grpc::ReserveResponse clientb_response;
  ::grpc::Status clientb_status;
  std::atomic<bool> clientb_started(false);
  set_reserve_request(clientb_request, "foo", "b");
  clientb_response.set_is_reserved(true);
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  wait_until_true(clientb_started);

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  EXPECT_TRUE(reset_response.is_server_reset());
  reserve_b.join();
  EXPECT_FALSE(clientb_response.is_reserved());
  bool is_reserved = call_is_reserved(&service, "foo", "b");
  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, ReservationWithMultipleClientsWaiting_ResetServer_AllClientsReturnAndDoNotReserve)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest clientb_request, clientc_request;
  nidevice_grpc::ReserveResponse clientb_response, clientc_response;
  ::grpc::Status clientb_status, clientc_status;
  std::atomic<bool> clientb_started(false), clientc_started(false);
  call_reserve(&service, "foo", "a");
  set_reserve_request(clientb_request, "foo", "b");
  clientb_response.set_is_reserved(true);
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  set_reserve_request(clientc_request, "foo", "c");
  clientc_response.set_is_reserved(true);
  std::thread reserve_c(call_reserve_task, &service, &clientc_request, &clientc_response, &clientc_status, &clientc_started);
  wait_until_true(clientb_started, clientc_started);

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  EXPECT_TRUE(reset_response.is_server_reset());
  reserve_b.join();
  EXPECT_FALSE(clientb_response.is_reserved());
  reserve_c.join();
  EXPECT_FALSE(clientc_response.is_reserved());
  bool is_reserved = call_is_reserved(&service, "foo", "b");
  EXPECT_FALSE(is_reserved);
  is_reserved = call_is_reserved(&service, "foo", "c");
  EXPECT_FALSE(is_reserved);
}

TEST(SessionUtilitiesServiceTests, ReservationWithClientWaiting_ResetServer_WaitingClientReturnsAborted)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  call_reserve(&service, "foo", "a");
  nidevice_grpc::ReserveRequest clientb_request;
  nidevice_grpc::ReserveResponse clientb_response;
  ::grpc::Status clientb_status;
  std::atomic<bool> clientb_started(false);
  set_reserve_request(clientb_request, "foo", "b");
  clientb_response.set_is_reserved(true);
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  wait_until_true(clientb_started);

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  reserve_b.join();
  EXPECT_FALSE(clientb_response.is_reserved());
  EXPECT_EQ(::grpc::ABORTED, clientb_status.error_code());
}

TEST(SessionUtilitiesServiceTests, ReservationWithMultipleClientsWaiting_ResetServer_AllClientsReturnAborted)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  nidevice_grpc::ReserveRequest clientb_request, clientc_request;
  nidevice_grpc::ReserveResponse clientb_response, clientc_response;
  ::grpc::Status clientb_status, clientc_status;
  std::atomic<bool> clientb_started(false), clientc_started(false);
  call_reserve(&service, "foo", "a");
  set_reserve_request(clientb_request, "foo", "b");
  clientb_response.set_is_reserved(true);
  std::thread reserve_b(call_reserve_task, &service, &clientb_request, &clientb_response, &clientb_status, &clientb_started);
  set_reserve_request(clientc_request, "foo", "c");
  clientc_response.set_is_reserved(true);
  std::thread reserve_c(call_reserve_task, &service, &clientc_request, &clientc_response, &clientc_status, &clientc_started);
  wait_until_true(clientb_started, clientc_started);

  ::grpc::ServerContext context;
  nidevice_grpc::ResetServerResponse reset_response;
  service.ResetServer(&context, NULL, &reset_response);

  reserve_b.join();
  EXPECT_FALSE(clientb_response.is_reserved());
  EXPECT_EQ(clientb_status.error_code(), ::grpc::ABORTED);
  reserve_c.join();
  EXPECT_FALSE(clientc_response.is_reserved());
  EXPECT_EQ(clientc_status.error_code(), ::grpc::ABORTED);
}

TEST(SessionUtilitiesServiceTests, SysCfgLibraryPresent_ClearSysCfgSession_IsSessionOpenReturnsFalse)
{
  nidevice_grpc::SessionRepository session_repository;
  ni::tests::utilities::SysCfgMockLibrary syscfg_mock_library;
  nidevice_grpc::DeviceEnumerator device_enumerator(&syscfg_mock_library);
  nidevice_grpc::SoftwareEnumerator software_enumerator(&syscfg_mock_library);
  nidevice_grpc::SessionUtilitiesService service(&session_repository, &device_enumerator, &software_enumerator);
  ::grpc::ServerContext context;
  nidevice_grpc::EnumerateDevicesRequest request;
  nidevice_grpc::EnumerateDevicesResponse response;
  ::grpc::Status status = service.EnumerateDevices(&context, &request, &response);

  device_enumerator.clear_syscfg_session();
  software_enumerator.clear_syscfg_session();

  EXPECT_FALSE(device_enumerator.is_session_open());
  EXPECT_FALSE(software_enumerator.is_session_open());
}

}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/session_utilities_service_tests_endtoend.cpp sha256=57e8567ba1a464144c4f93e22ee7ff7bf43d47fde6aecd0687b8495e221e7f23 bytes=7170 -->
## FILE: source/tests/integration/session_utilities_service_tests_endtoend.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/session_utilities_service_tests_endtoend.cpp`
- sha256: `57e8567ba1a464144c4f93e22ee7ff7bf43d47fde6aecd0687b8495e221e7f23`
- bytes: 7170

````cpp
#include <gtest/gtest.h>
#include <server/semaphore.h>
#include <server/session_utilities_service.h>
#include <server/syscfg_library.h>
#include <tests/utilities/syscfg_mock_library.h>

#include <thread>

namespace ni {
namespace tests {
namespace integration {

using ::testing::NiceMock;
using ::testing::Throw;

class SessionUtilitiesServiceTests_EndToEnd : public ::testing::Test {
 public:
  virtual ~SessionUtilitiesServiceTests_EndToEnd() {}

  void SetUp() override
  {
    ::grpc::ServerBuilder builder;
    session_repository_ = std::make_unique<nidevice_grpc::SessionRepository>();
    syscfg_mock_library_ = std::make_unique<NiceMock<ni::tests::utilities::SysCfgMockLibrary>>();
    ON_CALL(*(syscfg_mock_library_.get()), InitializeSession)
        .WillByDefault(Throw(nidevice_grpc::LibraryLoadException(nidevice_grpc::kSysCfgApiNotInstalledMessage)));
    device_enumerator_ = std::make_unique<nidevice_grpc::DeviceEnumerator>(syscfg_mock_library_.get());
    software_enumerator_ = std::make_unique<nidevice_grpc::SoftwareEnumerator>(syscfg_mock_library_.get());
    service_ = std::make_unique<nidevice_grpc::SessionUtilitiesService>(session_repository_.get(), device_enumerator_.get(), software_enumerator_.get());
    builder.RegisterService(service_.get());
    server_ = builder.BuildAndStart();
    ResetStub();
  }

  void TearDown() override
  {
    server_->Shutdown();
  }

  void ResetStub()
  {
    channel_ = server_->InProcessChannel(::grpc::ChannelArguments());
    stub_ = nidevice_grpc::SessionUtilities::NewStub(channel_);
  }

  std::unique_ptr<nidevice_grpc::SessionUtilities::Stub>& GetStub()
  {
    return stub_;
  }

  ::grpc::Status call_reserve(
      std::string reservation_id,
      std::string client_id,
      const std::chrono::system_clock::time_point& deadline =
          std::chrono::system_clock::now() + std::chrono::seconds(1),
      std::atomic<bool>* is_thread_started = nullptr)
  {
    nidevice_grpc::ReserveRequest request;
    nidevice_grpc::ReserveResponse response;
    request.set_reservation_id(reservation_id);
    request.set_client_id(client_id);
    ::grpc::ClientContext context;
    context.set_deadline(deadline);
    if (is_thread_started != nullptr) {
      *is_thread_started = true;
    }
    return GetStub()->Reserve(&context, request, &response);
  }

  bool call_is_reserved(std::string reservation_id, std::string client_id)
  {
    nidevice_grpc::IsReservedByClientRequest request;
    nidevice_grpc::IsReservedByClientResponse response;
    request.set_reservation_id(reservation_id);
    request.set_client_id(client_id);
    ::grpc::ClientContext context;
    GetStub()->IsReservedByClient(&context, request, &response);
    return response.is_reserved();
  }

  bool call_unreserve(std::string reservation_id, std::string client_id)
  {
    nidevice_grpc::UnreserveRequest request;
    nidevice_grpc::UnreserveResponse response;
    request.set_reservation_id(reservation_id);
    request.set_client_id(client_id);
    ::grpc::ClientContext context;
    GetStub()->Unreserve(&context, request, &response);
    return response.is_unreserved();
  }

 protected:
  SessionUtilitiesServiceTests_EndToEnd() {}

 private:
  std::shared_ptr<::grpc::Channel> channel_;
  std::unique_ptr<::nidevice_grpc::SessionUtilities::Stub> stub_;
  std::unique_ptr<nidevice_grpc::SessionRepository> session_repository_;
  std::unique_ptr<NiceMock<ni::tests::utilities::SysCfgMockLibrary>> syscfg_mock_library_;
  std::unique_ptr<nidevice_grpc::DeviceEnumerator> device_enumerator_;
  std::unique_ptr<nidevice_grpc::SoftwareEnumerator> software_enumerator_;
  std::unique_ptr<nidevice_grpc::SessionUtilitiesService> service_;
  std::unique_ptr<::grpc::Server> server_;
};

TEST_F(SessionUtilitiesServiceTests_EndToEnd, SessionUtilitiesServiceClient_RequestIsServerRunning_ResponseIsTrue)
{
  nidevice_grpc::IsReservedByClientRequest request;
  nidevice_grpc::IsReservedByClientResponse response;

  ::grpc::ClientContext context;
  ::grpc::Status s = GetStub()->IsReservedByClient(&context, request, &response);

  EXPECT_FALSE(response.is_reserved());
  EXPECT_TRUE(s.ok());
}

TEST_F(SessionUtilitiesServiceTests_EndToEnd, ClientTimesOutWaitingForReservation_FreeReservation_DoesNotReserve)
{
  auto status_a = call_reserve("foo", "a");
  auto status_b = call_reserve("foo", "b", std::chrono::system_clock::now() + std::chrono::milliseconds(5));

  call_unreserve("foo", "a");

  EXPECT_FALSE(call_is_reserved("foo", "b"));
  EXPECT_TRUE(status_a.ok());
  EXPECT_FALSE(status_b.ok());
  EXPECT_EQ(status_b.error_code(), ::grpc::DEADLINE_EXCEEDED);
}

TEST_F(SessionUtilitiesServiceTests_EndToEnd, MultipleClientsTimeOutWaitingForReservation_FreeReservation_DoNotReserve)
{
  call_reserve("foo", "a");
  call_reserve("foo", "b", std::chrono::system_clock::now() + std::chrono::milliseconds(5));
  call_reserve("foo", "c", std::chrono::system_clock::now() + std::chrono::milliseconds(5));

  call_unreserve("foo", "a");

  EXPECT_FALSE(call_is_reserved("foo", "b"));
  EXPECT_FALSE(call_is_reserved("foo", "c"));
}

TEST_F(SessionUtilitiesServiceTests_EndToEnd, ClientTimesOutWaitingForReservationWithOtherClientWaitingBehind_FreeReservation_ReservesLastClient)
{
  call_reserve("foo", "a");
  call_reserve("foo", "b", std::chrono::system_clock::now() + std::chrono::milliseconds(5));
  std::atomic<bool> clientc_started(false);
  std::thread reserve_c([this, &clientc_started] {
    call_reserve("foo", "c", std::chrono::system_clock::now() + std::chrono::seconds(1), &clientc_started);
  });
  while (!clientc_started) {
    std::this_thread::sleep_for(std::chrono::milliseconds(5));
  }
  std::this_thread::sleep_for(std::chrono::milliseconds(5));

  call_unreserve("foo", "a");

  reserve_c.join();
  EXPECT_FALSE(call_is_reserved("foo", "b"));
  EXPECT_TRUE(call_is_reserved("foo", "c"));
}

TEST_F(SessionUtilitiesServiceTests_EndToEnd, SysCfgLibraryNotPresent_ClientCallsEnumerateDevices_ReturnsNotFoundGrpcStatusError)
{
  nidevice_grpc::EnumerateDevicesRequest request;
  nidevice_grpc::EnumerateDevicesResponse response;
  ::grpc::ClientContext context;

  ::grpc::Status status = GetStub()->EnumerateDevices(&context, request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

TEST_F(SessionUtilitiesServiceTests_EndToEnd, SysCfgLibraryNotPresent_ClientCallsEnumerateInstalledSoftware_ReturnsNotFoundGrpcStatusError)
{
  nidevice_grpc::EnumerateInstalledSoftwareRequest request;
  nidevice_grpc::EnumerateInstalledSoftwareResponse response;
  ::grpc::ClientContext context;

  ::grpc::Status status = GetStub()->EnumerateInstalledSoftware(&context, request, &response);

  EXPECT_EQ(::grpc::StatusCode::NOT_FOUND, status.error_code());
  EXPECT_EQ(nidevice_grpc::kSysCfgApiNotInstalledMessage, status.error_message());
}

}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/integration/visa_resource_manager_tests.cpp sha256=2ea3e0de37d624ffb099674429f27bdcacaf4b423f41642f0a18a08cdb5f8619 bytes=6547 -->
## FILE: source/tests/integration/visa_resource_manager_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/integration/visa_resource_manager_tests.cpp`
- sha256: `2ea3e0de37d624ffb099674429f27bdcacaf4b423f41642f0a18a08cdb5f8619`
- bytes: 6547

````cpp
#include <server/session_repository.h>
#include "visa/visa_mock_library.h"
#include "visa/visa_service.h"

using namespace testing;
using namespace visa_grpc;

namespace ni {
namespace tests {
namespace integration {

static const char* test_descriptor = "fake::descriptor";

OpenResponse call_open(VisaService& service, const char* session_name)
{
    ::grpc::ServerContext context;
    OpenRequest request;
    OpenResponse response;
    request.set_instrument_descriptor(test_descriptor);
    request.set_access_mode(visa_grpc::LOCK_STATE_NO_LOCK);
    request.set_session_name(session_name);
    request.set_open_timeout(0);

    auto status = service.Open(&context, &request, &response);
    EXPECT_TRUE(status.ok());
    EXPECT_EQ(0, response.status());
    return response;
}

FindRsrcResponse call_find(VisaService& service)
{
    ::grpc::ServerContext context;
    FindRsrcRequest request;
    FindRsrcResponse response;
    request.set_expression("?*");

    auto status = service.FindRsrc(&context, &request, &response);
    EXPECT_TRUE(status.ok());
    EXPECT_EQ(0, response.status());
    return response;
}

void call_parse(VisaService& service)
{
    ::grpc::ServerContext context;
    ParseRsrcRequest request;
    ParseRsrcResponse response;
    request.set_resource_name(test_descriptor);

    auto status = service.ParseRsrc(&context, &request, &response);
    EXPECT_TRUE(status.ok());
    EXPECT_EQ(0, response.status());
}

ViStatus SetSessionToOne(ViSession* session)
{
  *session = (ViSession)1;
  return VI_SUCCESS;
}

ViStatus SetFindHandleToTwo(ViSession rsrcManagerHandle, ViConstString expression, ViFindList* findHandle, ViUInt32* returnCount, ViChar instrumentDescriptor[256])
{
  *findHandle = (ViSession)2;
  *returnCount = 1;
  strcpy(instrumentDescriptor, "RSRC");
  return VI_SUCCESS;
}

ViStatus SetNumberEventsToOne(void* attributeValue)
{
  *(ViUInt16*)attributeValue = 1;
  return VI_SUCCESS;
}

ViStatus SetEventTypeToServiceRequest(void* attributeValue)
{
  *(ViEventType*)attributeValue = VI_EVENT_SERVICE_REQ;
  return VI_SUCCESS;
}

TEST(VisaResourceManagerTest, FindRsrc_OpensResourceManagerOnceAndClosesFindHandle)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<ni::tests::unit::VisaMockLibrary>();
  auto resource_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<ViSession>>(session_repository);
  auto object_repository = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>();
  VisaService service(library, resource_repository, object_repository);

  EXPECT_CALL(*library, OpenDefaultRM)
    .WillOnce(WithArg<0>(Invoke(SetSessionToOne)));
  EXPECT_CALL(*library, FindRsrc)
    .WillOnce(Invoke(SetFindHandleToTwo));
  EXPECT_CALL(*library, Close(2))
    .Times(1);

  auto response = call_find(service);
  EXPECT_EQ(1, response.instrument_descriptor_size());

  EXPECT_CALL(*library, Close(1))
    .Times(1);
  session_repository->reset_server();
}

TEST(VisaResourceManagerTest, ParsePlusOpen_OpensResourceManagerOnce)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<ni::tests::unit::VisaMockLibrary>();
  auto resource_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<ViSession>>(session_repository);
  auto object_repository = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>();
  VisaService service(library, resource_repository, object_repository);

  EXPECT_CALL(*library, OpenDefaultRM)
    .WillOnce(WithArg<0>(Invoke(SetSessionToOne)));
  EXPECT_CALL(*library, ParseRsrc)
    .Times(1);
  EXPECT_CALL(*library, Open)
    .Times(1);
  EXPECT_CALL(*library, GetAttribute(_, static_cast<ViAttr>(0x3FFF019CUL), _))
    .WillOnce(WithArg<2>(Invoke(SetNumberEventsToOne)));
  EXPECT_CALL(*library, GetAttribute(_, static_cast<ViAttr>(0x3FFF019DUL), _))
    .WillOnce(WithArg<2>(Invoke(SetEventTypeToServiceRequest)));

  call_parse(service);
  auto response = call_open(service, "name2");
  EXPECT_EQ(1, response.supported_events_size());
  EXPECT_EQ(VI_EVENT_SERVICE_REQ, response.supported_events(0));

  EXPECT_CALL(*library, Close)
    .Times(2);
  session_repository->reset_server();
}

TEST(VisaResourceManagerTest, OpenTwoSessions_OpensResourceManagerOnce)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<ni::tests::unit::VisaMockLibrary>();
  auto resource_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<ViSession>>(session_repository);
  auto object_repository = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>();
  VisaService service(library, resource_repository, object_repository);

  EXPECT_CALL(*library, OpenDefaultRM)
    .WillOnce(WithArg<0>(Invoke(SetSessionToOne)));
  EXPECT_CALL(*library, Open)
    .Times(2);
  EXPECT_CALL(*library, GetAttribute)
    .Times(2)
    .WillRepeatedly(Return(VI_ERROR_NSUP_ATTR));

  auto response = call_open(service, "name1");
  EXPECT_EQ(0, response.supported_events_size());
  response = call_open(service, "name2");
  EXPECT_EQ(0, response.supported_events_size());

  EXPECT_CALL(*library, Close)
    .Times(3);
  session_repository->reset_server();
}

TEST(VisaResourceManagerTest, ResetServerWithOpenSession_OpenNewSession_OpensResourceManagerAgain)
{
  auto session_repository = std::make_shared<nidevice_grpc::SessionRepository>();
  auto library = std::make_shared<ni::tests::unit::VisaMockLibrary>();
  auto resource_repository = std::make_shared<nidevice_grpc::SessionResourceRepository<ViSession>>(session_repository);
  auto object_repository = std::shared_ptr<nidevice_grpc::SessionResourceRepository<ViObject>>();
  VisaService service(library, resource_repository, object_repository);

  EXPECT_CALL(*library, OpenDefaultRM)
    .Times(2)
    .WillRepeatedly(WithArg<0>(Invoke(SetSessionToOne)));
  EXPECT_CALL(*library, Open)
    .Times(2);
  EXPECT_CALL(*library, GetAttribute)
    .Times(2)
    .WillRepeatedly(Return(VI_ERROR_NSUP_ATTR));
  EXPECT_CALL(*library, Close)
    .Times(4);

  call_open(service, "name1");
  session_repository->reset_server();

  call_open(service, "name2");
  session_repository->reset_server();
}

}  // namespace integration
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/device_server.cpp sha256=b3ea13ebca38a6bbbe8ea4a4dd49e8bd93f8a9267a55049d4cd1f3f88b785496 bytes=2103 -->
## FILE: source/tests/system/device_server.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/device_server.cpp`
- sha256: `b3ea13ebca38a6bbbe8ea4a4dd49e8bd93f8a9267a55049d4cd1f3f88b785496`
- bytes: 2103

````cpp
#include "device_server.h"

#include <grpcpp/grpcpp.h>
#include <register_all_services.h>
#include <server/feature_toggles.h>
#include <session.grpc.pb.h>
#include <session_utilities.grpc.pb.h>

namespace ni {
namespace tests {
namespace system {

using CodeReadiness = nidevice_grpc::FeatureToggles::CodeReadiness;

DeviceServerInterface::~DeviceServerInterface() {}

class DeviceServer : public DeviceServerInterface {
 public:
  DeviceServer();
  ~DeviceServer() override;

  // DeviceServerInterface overrides
  void ResetServer() override;
  std::shared_ptr<::grpc::Channel> InProcessChannel() override;

 private:
  grpc::ServerBuilder builder_;
  std::shared_ptr<std::vector<std::shared_ptr<void>>> services_;
  std::unique_ptr<::grpc::Server> server_;
  std::shared_ptr<::grpc::Channel> channel_;
  std::unique_ptr<nidevice_grpc::SessionUtilities::Stub> session_stub_;
};

DeviceServer::DeviceServer()
    : builder_(),
      services_(
          nidevice_grpc::register_all_services(
              builder_,
              // Tests run with NextRelease CodeReadiness.
              nidevice_grpc::FeatureToggles({}, CodeReadiness::kNextRelease))),
      server_(builder_.BuildAndStart()),
      channel_(server_->InProcessChannel(::grpc::ChannelArguments())),
      session_stub_(nidevice_grpc::SessionUtilities::NewStub(channel_))
{
}

DeviceServer::~DeviceServer()
{
  // destroy services in reverse order
  while (!services_->empty())
  {
    services_->pop_back();
  }
}

void DeviceServer::ResetServer()
{
  grpc::ClientContext context;
  auto request = nidevice_grpc::ResetServerRequest{};
  auto response = nidevice_grpc::ResetServerResponse{};
  session_stub_->ResetServer(&context, request, &response);
}

std::shared_ptr<::grpc::Channel> DeviceServer::InProcessChannel()
{
  return channel_;
}

DeviceServerInterface* DeviceServerInterface::Singleton()
{
  static auto singleton = std::make_unique<DeviceServer>();
  return singleton.get();
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/device_server.h sha256=331084c014c894935a43d6b1d1462fcb59e19adbee87a8cb0f71f2079b5a9594 bytes=559 -->
## FILE: source/tests/system/device_server.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/device_server.h`
- sha256: `331084c014c894935a43d6b1d1462fcb59e19adbee87a8cb0f71f2079b5a9594`
- bytes: 559

````c
#ifndef NIDEVICE_GRPC_TESTS_DEVICE_SERVER
#define NIDEVICE_GRPC_TESTS_DEVICE_SERVER

#include <memory>

namespace grpc {
class Channel;
}

namespace ni {
namespace tests {
namespace system {

class DeviceServerInterface {
 public:
  virtual ~DeviceServerInterface() = 0;
  virtual void ResetServer() = 0;
  virtual std::shared_ptr<::grpc::Channel> InProcessChannel() = 0;

  static DeviceServerInterface* Singleton();
};

}  // namespace system
}  // namespace tests
}  // namespace ni

#endif  // NIDEVICE_GRPC_TESTS_DEVICE_SERVER
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/enumerate_devices.cpp sha256=d71c67dde9e193f1fe007cc809541a0d6def4af522e9632afdba6ec96a66aa66 bytes=1092 -->
## FILE: source/tests/system/enumerate_devices.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/enumerate_devices.cpp`
- sha256: `d71c67dde9e193f1fe007cc809541a0d6def4af522e9632afdba6ec96a66aa66`
- bytes: 1092

````cpp
#include "enumerate_devices.h"

#include <stdexcept>

#include "device_server.h"

namespace ni {
namespace tests {
namespace system {

const google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> EnumerateDevices(bool clear_cache)
{
  static bool devices_are_cached = false;
  static google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> devices_cache;

  if (!devices_are_cached || clear_cache) {
    devices_are_cached = false;

    ::nidevice_grpc::SessionUtilities::Stub stub(DeviceServerInterface::Singleton()->InProcessChannel());

    nidevice_grpc::EnumerateDevicesRequest request;
    nidevice_grpc::EnumerateDevicesResponse response;
    ::grpc::ClientContext context;

    if (::grpc::StatusCode::OK != stub.EnumerateDevices(&context, request, &response).error_code()) {
      throw std::runtime_error("Failed to enumerate devices");
    }

    devices_cache.CopyFrom(response.devices());
    devices_are_cached = true;
  }

  return devices_cache;
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/enumerate_devices.h sha256=55b04ca0261b715b9835306da0ff8e235b427430603d6288dee8b0f5f7e8bd51 bytes=434 -->
## FILE: source/tests/system/enumerate_devices.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/enumerate_devices.h`
- sha256: `55b04ca0261b715b9835306da0ff8e235b427430603d6288dee8b0f5f7e8bd51`
- bytes: 434

````c
#ifndef NIDEVICE_GRPC_TESTS_ENUMERATE_DEVICES
#define NIDEVICE_GRPC_TESTS_ENUMERATE_DEVICES

#include <server/device_enumerator.h>

namespace ni {
namespace tests {
namespace system {

const google::protobuf::RepeatedPtrField<nidevice_grpc::DeviceProperties> EnumerateDevices(bool clear_cache = false);

}  // namespace system
}  // namespace tests
}  // namespace ni

#endif  // NIDEVICE_GRPC_TESTS_ENUMERATE_DEVICES
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/enumerate_software.cpp sha256=7435cd1e021abefce9918551dc5d51da7caa5f220ec745c0256b96c816eeee2e bytes=1142 -->
## FILE: source/tests/system/enumerate_software.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/enumerate_software.cpp`
- sha256: `7435cd1e021abefce9918551dc5d51da7caa5f220ec745c0256b96c816eeee2e`
- bytes: 1142

````cpp
#include "enumerate_software.h"

#include <stdexcept>

#include "device_server.h"

namespace ni {
namespace tests {
namespace system {

const google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> EnumerateInstalledSoftware(bool clear_cache)
{
  static bool software_is_cached = false;
  static google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> software_cache;

  if (!software_is_cached || clear_cache) {
    software_is_cached = false;

    ::nidevice_grpc::SessionUtilities::Stub stub(DeviceServerInterface::Singleton()->InProcessChannel());

    nidevice_grpc::EnumerateInstalledSoftwareRequest request;
    nidevice_grpc::EnumerateInstalledSoftwareResponse response;
    ::grpc::ClientContext context;

    if (::grpc::StatusCode::OK != stub.EnumerateInstalledSoftware(&context, request, &response).error_code()) {
      throw std::runtime_error("Failed to enumerate software");
    }

    software_cache.CopyFrom(response.software());
    software_is_cached = true;
  }

  return software_cache;
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/enumerate_software.h sha256=701eb9c837d0c1bc878f0271eed60994235a64c2a20e2aab63795d0be5bfbdf6 bytes=451 -->
## FILE: source/tests/system/enumerate_software.h

- repository: `ni/grpc-device`
- source_path: `source/tests/system/enumerate_software.h`
- sha256: `701eb9c837d0c1bc878f0271eed60994235a64c2a20e2aab63795d0be5bfbdf6`
- bytes: 451

````c
#ifndef NIDEVICE_GRPC_TESTS_ENUMERATE_SOFTWARE
#define NIDEVICE_GRPC_TESTS_ENUMERATE_SOFTWARE

#include <server/software_enumerator.h>

namespace ni {
namespace tests {
namespace system {

const google::protobuf::RepeatedPtrField<nidevice_grpc::SoftwareProperties> EnumerateInstalledSoftware(bool clear_cache = false);

}  // namespace system
}  // namespace tests
}  // namespace ni

#endif  // NIDEVICE_GRPC_TESTS_ENUMERATE_SOFTWARE
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidaqmx_driver_api_tests.cpp sha256=2748399fc1b82f1a368ee4bc6acd872c17d406ec23098763f14766e18a4c3d85 bytes=147213 -->
## FILE: source/tests/system/nidaqmx_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidaqmx_driver_api_tests.cpp`
- sha256: `2748399fc1b82f1a368ee4bc6acd872c17d406ec23098763f14766e18a4c3d85`
- bytes: 147213

````cpp
#include <gmock/gmock.h>
#include <google/protobuf/util/time_util.h>

#include <algorithm>
#include <chrono>
#include <cstring>
#include <nlohmann/json.hpp>
#include <random>
#include <stdexcept>
#include <vector>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nidaqmx/nidaqmx_client.h"
#include "server/converters.h"
#include "tests/utilities/async_helpers.h"
#include "tests/utilities/scope_exit.h"
#include "tests/utilities/test_helpers.h"
#include "NIDAQmxInternalWaveform.h"

using namespace ::testing;
using namespace nidaqmx_grpc;
using google::protobuf::uint32;
using nidevice_grpc::converters::SecondsFromCVI1904EpochTo1970Epoch;
namespace client = nidaqmx_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

typedef ::google::protobuf::int16 int16;
typedef ::google::protobuf::int32 int32;
typedef ::google::protobuf::int64 int64;
typedef ::google::protobuf::uint64 uInt64;
typedef double float64;

constexpr auto DAQMX_SUCCESS = 0;
constexpr auto READ_ALL_AVAILABLE = -1;
constexpr auto DAQMX_ERROR_INVALID_NUMBER_SAMPLES_TO_READ = -200096;
constexpr auto DAQMX_ERROR_CANNOT_WRITE_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING = -200846;
constexpr auto SAMPLES_NOT_YET_AVAILABLE_ERROR = -200284;
constexpr auto SPECIFIED_ATTRIBUTE_NOT_VALID_ERROR = -200233;
constexpr auto INVALID_AO_DATA_WRITE_ERROR = -200561;
constexpr auto DONE_EVENT_ALREADY_REGISTERED_ERROR = -200950;
constexpr auto WAIT_FOR_VALID_TIMESTAMP_NOT_SUPPORTED_ERROR = -209833;
constexpr auto INVALID_ATTRIBUTE_VALUE_ERROR = -200077;
constexpr auto RETRIEVING_NETWORK_DEVICE_PROPERTIES_ERROR = -201401;
constexpr auto TEDS_SENSOR_NOT_DETECTED_ERROR = -200709;
constexpr auto INVALID_TERM_ROUTING_ERROR = -89129;
constexpr auto DEVICE_DOES_NOT_SUPPORT_CDAQ_SYNC_CONNECTIONS_ERROR = -201450;
constexpr auto EVERY_N_SAMPLES_EVENT_NOT_SUPPORTED_FOR_NON_BUFFERED_TASKS = -200848;
constexpr auto EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE_ERROR = -200980;
constexpr auto CANNOT_UNREGISTER_DAQMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING_ERROR = -200986;
constexpr auto STRAIN_SHUNT_CAL_NOT_SUPPORTED_ERROR = -201203;
constexpr auto BRIDGE_SHUNT_CAL_NOT_SUPPORTED_ERROR = -201204;
constexpr auto THRMCPL_LEAD_OFFSET_NULLING_CAL_NOT_SUPPORTED_ERROR = -201375;
constexpr auto BRIDGE_OFFSET_NULLING_CAL_NOT_SUPPORTED_ERROR = -200696;

// Creates a static TResponse instance that can be used as a default/in-line value (because it's not a temporary).
template <typename TResponse>
struct ThrowawayResponse {
  static TResponse& response()
  {
    static TResponse response_instance;
    return response_instance;
  }
};

class NiDAQmxDriverApiTests : public Test {
 protected:
  const std::string DEVICE_NAME{"gRPCSystemTestDAQ"};
  const std::string ANY_DEVICE_MODEL{"[[ANY_DEVICE_MODEL]]"};
  const std::string AI_CHANNEL{"gRPCSystemTestDAQ/ai0"};
  const std::string AI_CHANNEL_1{"gRPCSystemTestDAQ/ai1"};
  const std::string AO_CHANNEL{"gRPCSystemTestDAQ/ao0"};

  NiDAQmxDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nidaqmx_stub_(NiDAQmx::NewStub(device_server_->InProcessChannel()))
  {
  }
  virtual ~NiDAQmxDriverApiTests() {}

  void SetUp() override
  {
    // In MAX, this can be set up by importing grpc-device-daq-tests.nce.
    // Allow ANY_DEVICE_MODEL so we can run on any hardware with DEVICE_NAME configured.
    // Tests are written for a simulated "NI PXIe-6341".
    std::unordered_map<std::string, std::string> required_devices{
        {DEVICE_NAME, ANY_DEVICE_MODEL}};

    if (!are_all_devices_present(required_devices)) {
      GTEST_SKIP() << "Required Device(s) not found";
    }

    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  bool are_all_devices_present(std::unordered_map<std::string, std::string> required_devices)
  {
    for (const auto& device : EnumerateDevices()) {
      auto matched_required_device = required_devices.find(device.name());
      if (matched_required_device != required_devices.cend()) {
        if (matched_required_device->second == device.model() || matched_required_device->second == ANY_DEVICE_MODEL)
          required_devices.erase(matched_required_device);
      }
    }

    return required_devices.empty();
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    CreateTaskResponse response;
    auto status = create_task(response);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.task());

    EXPECT_SUCCESS(status, response);
  }

  void close_driver_session()
  {
    if (!driver_session_) return;

    auto response = clear_task();

    EXPECT_SUCCESS(response);
  }

  ::grpc::Status create_task(CreateTaskResponse& response)
  {
    ::grpc::ClientContext context;
    CreateTaskRequest request;
    auto status = stub()->CreateTask(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ClearTaskResponse clear_task(const nidevice_grpc::Session& task)
  {
    return client::clear_task(stub(), task);
  }

  ClearTaskResponse clear_task()
  {
    return clear_task(task());
  }

  CreateAIVoltageChanRequest create_ai_voltage_request(double min_val, double max_val, const std::string& custom_scale_name = "", const std::string& physical_channel = "gRPCSystemTestDAQ/ai0", const std::string& channel_name = "ai0")
  {
    CreateAIVoltageChanRequest request;
    set_request_session_name(request);
    request.set_physical_channel(physical_channel);
    request.set_name_to_assign_to_channel(channel_name);
    request.set_terminal_config(InputTermCfgWithDefault::INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT);
    request.set_min_val(min_val);
    request.set_max_val(max_val);
    if (custom_scale_name.empty()) {
      request.set_units(VoltageUnits2::VOLTAGE_UNITS2_VOLTS);
    }
    else {
      request.set_custom_scale_name(custom_scale_name);
      request.set_units(VoltageUnits2::VOLTAGE_UNITS2_FROM_CUSTOM_SCALE);
    }
    return request;
  }

  ::grpc::Status create_ai_voltage_chan(const CreateAIVoltageChanRequest& request, CreateAIVoltageChanResponse& response = ThrowawayResponse<CreateAIVoltageChanResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CreateAIVoltageChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_ai_voltage_chan(double min_val, double max_val, CreateAIVoltageChanResponse& response = ThrowawayResponse<CreateAIVoltageChanResponse>::response())
  {
    auto request = create_ai_voltage_request(min_val, max_val);
    return create_ai_voltage_chan(request, response);
  }

  ::grpc::Status create_ai_voltage_chan(const std::string& physical_channel, const std::string& channel_name, double min_val, double max_val, CreateAIVoltageChanResponse& response = ThrowawayResponse<CreateAIVoltageChanResponse>::response())
  {
    auto request = create_ai_voltage_request(min_val, max_val, "", physical_channel, channel_name);
    return create_ai_voltage_chan(request, response);
  }

  CreateAIBridgeChanRequest create_ai_bridge_request(double min_val, double max_val, const std::string& custom_scale_name = "")
  {
    CreateAIBridgeChanRequest request;
    set_request_session_name(request);
    request.set_physical_channel("gRPCSystemTestDAQ/ai0");
    request.set_name_to_assign_to_channel("ai0");
    request.set_min_val(min_val);
    request.set_max_val(max_val);
    if (custom_scale_name.empty()) {
      request.set_units(BridgeUnits::BRIDGE_UNITS_VOLTS_PER_VOLT);
    }
    else {
      request.set_custom_scale_name(custom_scale_name);
      request.set_units(BridgeUnits::BRIDGE_UNITS_FROM_CUSTOM_SCALE);
    }
    request.set_bridge_config(BridgeConfiguration1::BRIDGE_CONFIGURATION1_FULL_BRIDGE);
    request.set_voltage_excit_source(ExcitationSource::EXCITATION_SOURCE_INTERNAL);
    request.set_voltage_excit_val(2.50);
    request.set_nominal_bridge_resistance(350.00);
    return request;
  }

  ::grpc::Status create_ai_bridge_chan(const CreateAIBridgeChanRequest& request, CreateAIBridgeChanResponse& response = ThrowawayResponse<CreateAIBridgeChanResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CreateAIBridgeChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_ai_bridge_chan(double min_val, double max_val, CreateAIBridgeChanResponse& response = ThrowawayResponse<CreateAIBridgeChanResponse>::response())
  {
    auto request = create_ai_bridge_request(min_val, max_val);
    return create_ai_bridge_chan(request, response);
  }

  CreateAIStrainGageChanRequest create_ai_strain_gage_request(double min_val, double max_val, const std::string& custom_scale_name = "")
  {
    CreateAIStrainGageChanRequest request;
    set_request_session_name(request);
    request.set_physical_channel("gRPCSystemTestDAQ/ai0");
    request.set_name_to_assign_to_channel("ai0");
    request.set_min_val(min_val);
    request.set_max_val(max_val);
    if (custom_scale_name.empty()) {
      request.set_units(StrainUnits1::STRAIN_UNITS1_STRAIN);
    }
    else {
      request.set_custom_scale_name(custom_scale_name);
      request.set_units(StrainUnits1::STRAIN_UNITS1_FROM_CUSTOM_SCALE);
    }
    request.set_strain_config(StrainGageBridgeType1::STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_I);
    request.set_initial_bridge_voltage(0.00);
    request.set_lead_wire_resistance(0.00);
    request.set_voltage_excit_source(ExcitationSource::EXCITATION_SOURCE_EXTERNAL);
    request.set_voltage_excit_val(2.50);
    request.set_gage_factor(2.00);
    request.set_poisson_ratio(0.30);
    request.set_nominal_gage_resistance(350.00);
    return request;
  }

  ::grpc::Status create_ai_strain_gage_chan(const CreateAIStrainGageChanRequest& request, CreateAIStrainGageChanResponse& response = ThrowawayResponse<CreateAIStrainGageChanResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CreateAIStrainGageChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_ai_strain_gage_chan(double min_val, double max_val, CreateAIStrainGageChanResponse& response = ThrowawayResponse<CreateAIStrainGageChanResponse>::response())
  {
    auto request = create_ai_strain_gage_request(min_val, max_val);
    return create_ai_strain_gage_chan(request, response);
  }

  CreateAIThrmcplChanRequest create_ai_thrmcpl_request(double min_val, double max_val, const std::string& custom_scale_name = "")
  {
    CreateAIThrmcplChanRequest request;
    set_request_session_name(request);
    request.set_physical_channel("gRPCSystemTestDAQ/ai0");
    request.set_name_to_assign_to_channel("ai0");
    request.set_min_val(min_val);
    request.set_max_val(max_val);
    request.set_units(TemperatureUnits::TEMPERATURE_UNITS_DEG_C);
    request.set_thermocouple_type(ThermocoupleType1::THERMOCOUPLE_TYPE1_J_TYPE_TC);
    request.set_cjc_val(25.0);
    request.set_cjc_channel("");
    request.set_cjc_source(CJCSource1::CJC_SOURCE1_CONST_VAL);
    return request;
  }

  ::grpc::Status create_ai_thrmcpl_chan(const CreateAIThrmcplChanRequest& request, CreateAIThrmcplChanResponse& response = ThrowawayResponse<CreateAIThrmcplChanResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CreateAIThrmcplChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_ai_thrmcpl_chan(double min_val, double max_val, CreateAIThrmcplChanResponse& response = ThrowawayResponse<CreateAIThrmcplChanResponse>::response())
  {
    auto request = create_ai_thrmcpl_request(min_val, max_val);
    return create_ai_thrmcpl_chan(request, response);
  }

  CreateAOVoltageChanRequest create_ao_voltage_chan_request(double min_val, double max_val, const std::string& name = "ao0")
  {
    CreateAOVoltageChanRequest request;
    set_request_session_name(request);

    request.set_physical_channel("gRPCSystemTestDAQ/ao0");
    request.set_name_to_assign_to_channel(name);

    request.set_min_val(min_val);
    request.set_max_val(max_val);
    request.set_units(VoltageUnits2::VOLTAGE_UNITS2_VOLTS);
    return request;
  }

  ::grpc::Status create_ao_voltage_chan(const CreateAOVoltageChanRequest& request, CreateAOVoltageChanResponse& response = ThrowawayResponse<CreateAOVoltageChanResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CreateAOVoltageChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_ao_voltage_chan(double min_val, double max_val, CreateAOVoltageChanResponse& response = ThrowawayResponse<CreateAOVoltageChanResponse>::response())
  {
    auto request = create_ao_voltage_chan_request(min_val, max_val);
    return create_ao_voltage_chan(request, response);
  }

  ::grpc::Status create_ao_voltage_chan(const std::string& physical_channel, const std::string& channel_name, double min_val, double max_val, CreateAOVoltageChanResponse& response = ThrowawayResponse<CreateAOVoltageChanResponse>::response())
  {
    CreateAOVoltageChanRequest request;
    set_request_session_name(request);
    request.set_physical_channel(physical_channel);
    request.set_name_to_assign_to_channel(channel_name);
    request.set_min_val(min_val);
    request.set_max_val(max_val);
    request.set_units(VoltageUnits2::VOLTAGE_UNITS2_VOLTS);
    return create_ao_voltage_chan(request, response);
  }

  ::grpc::Status create_di_chan(
    CreateDIChanResponse& response = ThrowawayResponse<CreateDIChanResponse>::response(),
    const std::string& lines = "gRPCSystemTestDAQ/port0/line0",
    const std::string& name = "di",
    LineGrouping line_grouping = LineGrouping::LINE_GROUPING_CHAN_PER_LINE)
  {
    ::grpc::ClientContext context;
    CreateDIChanRequest request;
    set_request_session_name(request);
    request.set_lines(lines);
    request.set_name_to_assign_to_lines(name);
    request.set_line_grouping(line_grouping);
    auto status = stub()->CreateDIChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  CreateDOChanResponse create_do_chan(CreateDOChanResponse& response = ThrowawayResponse<CreateDOChanResponse>::response())
  {
    return client::create_do_chan(stub(), task(), "gRPCSystemTestDAQ/port1/line0", "do", LineGrouping::LINE_GROUPING_CHAN_PER_LINE);
  }

  ::grpc::Status create_do_chan(
      CreateDOChanResponse& response,
      const std::string& lines,
      const std::string& name_to_assign_to_channel,
      LineGrouping line_grouping)
  {
    response = client::create_do_chan(stub(), task(), lines, name_to_assign_to_channel, line_grouping);
    return ::grpc::Status::OK;
  }

  ::grpc::Status create_ci_freq_chan(CreateCIFreqChanResponse& response)
  {
    ::grpc::ClientContext context;
    CreateCIFreqChanRequest request;
    set_request_session_name(request);
    request.set_counter("gRPCSystemTestDAQ/ctr0");
    request.set_name_to_assign_to_channel("ctr");
    request.set_min_val(1.19209);
    request.set_max_val(1e+2);
    request.set_units(FrequencyUnits3::FREQUENCY_UNITS3_HZ);
    request.set_edge(Edge1::EDGE1_RISING);
    request.set_meas_method(CounterFrequencyMethod::COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR);
    request.set_meas_time(0.001);
    request.set_divisor(4);
    auto status = stub()->CreateCIFreqChan(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status get_error_string(int32 error_code, GetErrorStringResponse& response)
  {
    ::grpc::ClientContext context;
    GetErrorStringRequest request;
    request.set_error_code(error_code);
    auto status = stub()->GetErrorString(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status start_task(const ::nidevice_grpc::Session& session, StartTaskResponse& response)
  {
    ::grpc::ClientContext context;
    StartTaskRequest request;
    set_request_session_name(request, session);
    auto status = stub()->StartTask(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status start_task(StartTaskResponse& response = ThrowawayResponse<StartTaskResponse>::response())
  {
    return start_task(*driver_session_, response);
  }

  ::grpc::Status stop_task(StopTaskResponse& response = ThrowawayResponse<StopTaskResponse>::response())
  {
    ::grpc::ClientContext context;
    StopTaskRequest request;
    set_request_session_name(request);
    auto status = stub()->StopTask(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status read_analog_f64(
      int32 samps_per_chan,
      uint32 array_size_in_samps,
      double timeout = 10.0,
      ReadAnalogF64Response& response = ThrowawayResponse<ReadAnalogF64Response>::response())
  {
    ::grpc::ClientContext context;
    ReadAnalogF64Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(samps_per_chan);
    request.set_array_size_in_samps(array_size_in_samps);
    request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    request.set_timeout(timeout);
    auto status = stub()->ReadAnalogF64(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  auto async_read_analog_f64(
    ::grpc::ClientContext& context,
    ::grpc::CompletionQueue& completion_queue,
    void* tag,
    int32 samps_per_chan,
    uint32 array_size_in_samps,
    ReadAnalogF64Response& response,
    ::grpc::Status& status)
  {
    ReadAnalogF64Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(samps_per_chan);
    request.set_array_size_in_samps(array_size_in_samps);
    request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    request.set_timeout(10.0);
    auto reader = stub()->AsyncReadAnalogF64(&context, request, &completion_queue);
    reader->Finish(&response, &status, tag);
    return reader;
  }

  ::grpc::Status read_analog_waveforms(
      ::grpc::ClientContext& context,
      int32 num_samps_per_chan,
      double timeout = 10.0,
      WaveformAttributeMode waveform_attribute_mode = WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE,
      ReadAnalogWaveformsResponse& response = ThrowawayResponse<ReadAnalogWaveformsResponse>::response())
  {
    ReadAnalogWaveformsRequest request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(num_samps_per_chan);
    request.set_timeout(timeout);
    request.set_waveform_attribute_mode(waveform_attribute_mode);
    auto status = stub()->ReadAnalogWaveforms(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status read_digital_waveforms(
      ::grpc::ClientContext& context,
      int32 number_of_samples_per_channel,
      double timeout = 10.0,
      WaveformAttributeMode waveform_attribute_mode = WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE,
      ReadDigitalWaveformsResponse& response = ThrowawayResponse<ReadDigitalWaveformsResponse>::response())
  {
    ReadDigitalWaveformsRequest request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(number_of_samples_per_channel);
    request.set_timeout(timeout);
    request.set_waveform_attribute_mode(waveform_attribute_mode);
    auto status = stub()->ReadDigitalWaveforms(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_analog_waveforms(
      ::grpc::ClientContext& context,
      const std::vector<std::vector<double>>& waveform_data,
      bool auto_start = false,
      double timeout = 10.0,
      WriteAnalogWaveformsResponse& response = ThrowawayResponse<WriteAnalogWaveformsResponse>::response())
  {
    WriteAnalogWaveformsRequest request;
    set_request_session_name(request);
    
    if (waveform_data.empty()) {
      return ::grpc::Status(::grpc::INVALID_ARGUMENT, "No waveform data provided");
    }
    
    request.set_auto_start(auto_start);
    request.set_timeout(timeout);
    
    for (const auto& channel_data : waveform_data) {
      auto* waveform = request.add_waveforms();
      auto* y_data = waveform->mutable_y_data();
      y_data->Add(channel_data.begin(), channel_data.end());
    }
    
    auto status = stub()->WriteAnalogWaveforms(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_digital_waveforms(
      ::grpc::ClientContext& context,
      int32 number_of_samples_per_channel,
      const std::vector<ni::protobuf::types::DigitalWaveform>& waveforms,
      bool auto_start = false,
      double timeout = 10.0,
      WriteDigitalWaveformsResponse& response = ThrowawayResponse<WriteDigitalWaveformsResponse>::response())
  {
    WriteDigitalWaveformsRequest request;
    set_request_session_name(request);
    request.set_auto_start(auto_start);
    request.set_timeout(timeout);
    for (const auto& waveform : waveforms) {
      *request.add_waveforms() = waveform;
    }
    auto status = stub()->WriteDigitalWaveforms(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_analog_f64(
      const std::vector<double>& data,
      WriteAnalogF64Response& response)
  {
    ::grpc::ClientContext context;
    WriteAnalogF64Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(static_cast<int32_t>(data.size()));
    request.set_auto_start(false);
    request.mutable_write_array()->Add(data.cbegin(), data.cend());
    request.set_data_layout(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    auto status = stub()->WriteAnalogF64(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_u32_digital_data(WriteDigitalU32Response& response)
  {
    ::grpc::ClientContext context;
    WriteDigitalU32Request request;
    set_request_session_name(request);
    request.set_data_layout(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    request.set_num_samps_per_chan(4);
    request.add_write_array(1000000);
    request.add_write_array(10000);
    request.add_write_array(1);
    request.add_write_array(0);
    auto status = stub()->WriteDigitalU32(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status read_u32_digital_data(ReadDigitalU32Response& response)
  {
    ::grpc::ClientContext context;
    ReadDigitalU32Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(4);
    request.set_array_size_in_samps(4);
    request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    auto status = stub()->ReadDigitalU32(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_u16_digital_data(WriteDigitalU16Response& response)
  {
    ::grpc::ClientContext context;
    WriteDigitalU16Request request;
    set_request_session_name(request);
    request.set_data_layout(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    request.set_num_samps_per_chan(4);
    request.add_write_array(65535);
    request.add_write_array(10);
    request.add_write_array(1);
    request.add_write_array(0);
    auto status = stub()->WriteDigitalU16(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status read_u16_digital_data(ReadDigitalU16Response& response)
  {
    ::grpc::ClientContext context;
    ReadDigitalU16Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(4);
    request.set_array_size_in_samps(4);
    request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    auto status = stub()->ReadDigitalU16(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_u8_digital_data(WriteDigitalU8Response& response)
  {
    ::grpc::ClientContext context;
    WriteDigitalU8Request request;
    set_request_session_name(request);
    request.set_data_layout(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    request.set_num_samps_per_chan(4);
    uint8_t data[4] = {255, 10, 1, 0};
    request.set_write_array(data, sizeof(data));
    auto status = stub()->WriteDigitalU8(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status read_u8_digital_data(ReadDigitalU8Response& response)
  {
    ::grpc::ClientContext context;
    ReadDigitalU8Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(4);
    request.set_array_size_in_samps(4);
    request.set_fill_mode(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    auto status = stub()->ReadDigitalU8(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status write_binary_i16(const std::vector<int16>& data, WriteBinaryI16Response& response)
  {
    ::grpc::ClientContext context;
    WriteBinaryI16Request request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(static_cast<uint32>(data.size()));
    request.mutable_write_array()->CopyFrom({data.cbegin(), data.cend()});
    request.set_data_layout(GroupBy::GROUP_BY_GROUP_BY_CHANNEL);
    auto status = stub()->WriteBinaryI16(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status get_nth_task_device(uint32_t index, GetNthTaskDeviceResponse& response)
  {
    ::grpc::ClientContext context;
    GetNthTaskDeviceRequest request;
    set_request_session_name(request);
    request.set_index(index);

    auto status = stub()->GetNthTaskDevice(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  bool is_task_done()
  {
    ::grpc::ClientContext context;
    IsTaskDoneRequest request;
    set_request_session_name(request);
    IsTaskDoneResponse response;
    auto status = stub()->IsTaskDone(&context, request, &response);
    client::raise_if_error(status, context);
    return response.is_task_done();
  }

  ::grpc::Status task_control(TaskControlAction action, TaskControlResponse& response)
  {
    ::grpc::ClientContext context;
    TaskControlRequest request;
    set_request_session_name(request);
    request.set_action(action);
    auto status = stub()->TaskControl(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  auto register_done_event(::grpc::ClientContext& context)
  {
    RegisterDoneEventRequest request;
    set_request_session_name(request);
    return stub()->RegisterDoneEvent(&context, request);
  }

  auto async_register_done_event(::grpc::ClientContext& context, ::grpc::CompletionQueue& completion_queue, void* tag)
  {
    RegisterDoneEventRequest request;
    set_request_session_name(request);
    return stub()->AsyncRegisterDoneEvent(&context, request, &completion_queue, tag);
  }

  auto register_every_n_samples_event(
    ::grpc::ClientContext& context,
    uint32 n_samples,
    EveryNSamplesEventType every_n_samples_event_type = EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER)
  {
    RegisterEveryNSamplesEventRequest request;
    set_request_session_name(request);
    request.set_n_samples(n_samples);
    request.set_every_n_samples_event_type(every_n_samples_event_type);
    return stub()->RegisterEveryNSamplesEvent(&context, request);
  }

  auto async_register_every_n_samples_event(
    ::grpc::ClientContext& context,
    ::grpc::CompletionQueue& completion_queue,
    void* tag,
    uint32 n_samples,
    EveryNSamplesEventType every_n_samples_event_type = EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER)
  {
    RegisterEveryNSamplesEventRequest request;
    set_request_session_name(request);
    request.set_n_samples(n_samples);
    request.set_every_n_samples_event_type(every_n_samples_event_type);
    return stub()->AsyncRegisterEveryNSamplesEvent(&context, request, &completion_queue, tag);
  }

  auto register_signal_event(::grpc::ClientContext& context, Signal2 signal_id)
  {
    RegisterSignalEventRequest request;
    set_request_session_name(request);
    request.set_signal_id(signal_id);
    return stub()->RegisterSignalEvent(&context, request);
  }

  auto async_register_signal_event(
    ::grpc::ClientContext& context,
    ::grpc::CompletionQueue& completion_queue,
    void* tag,
    Signal2 signal_id)
  {
    RegisterSignalEventRequest request;
    set_request_session_name(request);
    request.set_signal_id(signal_id);
    return stub()->AsyncRegisterSignalEvent(&context, request, &completion_queue, tag);
  }

  template <typename TResponse>
  void read_stream(
    ::grpc::ClientContext& context,
    ::grpc::ClientReader<TResponse>& reader,
    TResponse& response)
  {
    if (!reader.Read(&response)) {
      auto status = reader.Finish();
      client::raise_if_error(status, context);
      throw std::runtime_error("Stream unexpectedly closed");
    }
  }

  template <typename TResponse>
  void read_stream(
    ::grpc::ClientContext& context,
    ::grpc::ClientReader<TResponse>& reader,
    size_t count,
    std::vector<TResponse>& responses)
  {
    TResponse response;
    for (size_t i = 0; i < count; ++i) {
      read_stream(context, reader, response);
      responses.push_back(response);
    }
  }

  template <typename TResponse>
  void async_wait_for_initial_metadata(
    ::grpc::ClientContext& context,
    ::grpc::ClientAsyncReader<TResponse>& reader,
    ::grpc::CompletionQueue& completion_queue,
    void* start_call_tag,
    void* read_initial_metadata_tag)
  {
    // Assume start_call_tag was initiated by async_register_x_event().
    reader.ReadInitialMetadata(read_initial_metadata_tag);
    ASSERT_EQ(Completion(start_call_tag, true), get_next_completion(completion_queue));
    ASSERT_EQ(Completion(read_initial_metadata_tag, true), get_next_completion(completion_queue));
  }

  // Wait for the stream to finish and throw an exception if it has an error. If the stream is not
  // closed/canceled, this function waits forever.
  template <typename TResponse>
  void async_finish_stream(
    ::grpc::ClientContext& context,
    ::grpc::ClientAsyncReader<TResponse>& reader,
    ::grpc::CompletionQueue& completion_queue,
    void* finish_tag)
  {
    ::grpc::Status status;
    reader.Finish(&status, finish_tag);

    while (true) {
      auto completion = get_next_completion(completion_queue);
      if (get_completion_tag(completion) == finish_tag) {
        ASSERT_TRUE(is_completion_ok(completion));
        client::raise_if_error(status, context);
        break;
      }
      // Discard other completions.
    }
  }

  // Cancel the stream and wait for it to finish with ::grpc::CANCELLED.
  template <typename TResponse>
  void async_cancel_stream(
    ::grpc::ClientContext& context,
    ::grpc::ClientAsyncReader<TResponse>& reader,
    ::grpc::CompletionQueue& completion_queue,
    void* finish_tag)
  {
    context.TryCancel();
    EXPECT_THROW_GRPC_CANCELLED(async_finish_stream(context, reader, completion_queue, finish_tag));
  }

  // Begin an async read. If the read immediately completes with an error, finish the stream and
  // throw an exception. This function assumes there are no other pending tags.
  template <typename TResponse>
  void async_begin_read_stream(
    ::grpc::ClientContext& context,
    ::grpc::ClientAsyncReader<TResponse>& reader,
    ::grpc::CompletionQueue& completion_queue,
    void* read_tag,
    void* finish_tag,
    TResponse& response)
  {
    reader.Read(&response, read_tag);

    Completion completion;
    bool completed = try_get_next_completion_without_blocking(completion_queue, completion);

    if (completed) {
      ASSERT_EQ(read_tag, get_completion_tag(completion)) << "There should be no other pending tags";
      if (!is_completion_ok(completion)) {
        async_finish_stream(context, reader, completion_queue, finish_tag);
        throw std::runtime_error("Stream unexpectedly closed");
      }
    }
  }

  ::grpc::Status unregister_done_event(UnregisterDoneEventResponse& response = ThrowawayResponse<UnregisterDoneEventResponse>::response())
  {
    ::grpc::ClientContext context;
    UnregisterDoneEventRequest request;
    set_request_session_name(request);
    auto status = stub()->UnregisterDoneEvent(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status unregister_every_n_samples_event(
    EveryNSamplesEventType every_n_samples_event_type = EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER,
    UnregisterEveryNSamplesEventResponse& response = ThrowawayResponse<UnregisterEveryNSamplesEventResponse>::response())
  {
    ::grpc::ClientContext context;
    UnregisterEveryNSamplesEventRequest request;
    set_request_session_name(request);
    request.set_every_n_samples_event_type(every_n_samples_event_type);
    auto status = stub()->UnregisterEveryNSamplesEvent(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status unregister_signal_event(
    Signal2 signal_id,
    UnregisterSignalEventResponse& response = ThrowawayResponse<UnregisterSignalEventResponse>::response())
  {
    ::grpc::ClientContext context;
    UnregisterSignalEventRequest request;
    set_request_session_name(request);
    request.set_signal_id(signal_id);
    auto status = stub()->UnregisterSignalEvent(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  CfgSampClkTimingRequest create_cfg_samp_clk_timing_request(double rate, Edge1 active_edge, AcquisitionType sample_mode, uInt64 samples_per_chan)
  {
    CfgSampClkTimingRequest request;
    set_request_session_name(request);
    request.set_rate(rate);
    request.set_active_edge(active_edge);
    request.set_sample_mode(sample_mode);
    request.set_samps_per_chan(samples_per_chan);
    return request;
  }

  ::grpc::Status cfg_samp_clk_timing(CfgSampClkTimingResponse& response = ThrowawayResponse<CfgSampClkTimingResponse>::response())
  {
    auto request = create_cfg_samp_clk_timing_request(100.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_CONT_SAMPS, 1000UL);
    return cfg_samp_clk_timing(request, response);
  }

  ::grpc::Status cfg_samp_clk_timing(const CfgSampClkTimingRequest& request, CfgSampClkTimingResponse& response = ThrowawayResponse<CfgSampClkTimingResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CfgSampClkTiming(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  CfgChangeDetectionTimingRequest create_cfg_change_detection_timing(const std::string& channel)
  {
    CfgChangeDetectionTimingRequest request;
    set_request_session_name(request);
    request.set_falling_edge_chan(channel);
    request.set_rising_edge_chan(channel);
    request.set_sample_mode(AcquisitionType::ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT);
    return request;
  }

  ::grpc::Status cfg_change_detection_timing(const CfgChangeDetectionTimingRequest& request, CfgChangeDetectionTimingResponse& response = ThrowawayResponse<CfgChangeDetectionTimingResponse>::response())
  {
    ::grpc::ClientContext context;
    auto status = stub()->CfgChangeDetectionTiming(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status cfg_input_buffer(CfgInputBufferResponse& response)
  {
    ::grpc::ClientContext context;
    CfgInputBufferRequest request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(1024U);
    auto status = stub()->CfgInputBuffer(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status cfg_output_buffer(CfgOutputBufferResponse& response)
  {
    ::grpc::ClientContext context;
    CfgOutputBufferRequest request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(1024U);
    auto status = stub()->CfgOutputBuffer(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status self_test_device(SelfTestDeviceResponse& response)
  {
    ::grpc::ClientContext context;
    SelfTestDeviceRequest request;
    request.set_device_name(DEVICE_NAME);
    auto status = stub()->SelfTestDevice(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_lin_scale(const std::string& name, double slope, CreateLinScaleResponse& response = ThrowawayResponse<CreateLinScaleResponse>::response())
  {
    ::grpc::ClientContext context;
    CreateLinScaleRequest request;
    request.set_name(name);
    request.set_slope(slope);
    request.set_pre_scaled_units(UnitsPreScaled::UNITS_PRE_SCALED_VOLTS);
    auto status = stub()->CreateLinScale(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_polynomial_scale(const std::string& name, const std::vector<double>& forward_coeffs, const std::vector<double>& reverse_coeffs, CreatePolynomialScaleResponse& response = ThrowawayResponse<CreatePolynomialScaleResponse>::response())
  {
    ::grpc::ClientContext context;
    CreatePolynomialScaleRequest request;
    request.set_name(name);

    request.mutable_forward_coeffs()->CopyFrom({forward_coeffs.cbegin(), forward_coeffs.cend()});

    request.mutable_reverse_coeffs()->CopyFrom({reverse_coeffs.cbegin(), reverse_coeffs.cend()});

    request.set_pre_scaled_units(UnitsPreScaled::UNITS_PRE_SCALED_VOLTS);
    auto status = stub()->CreatePolynomialScale(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  CalculateReversePolyCoeffRequest create_calculate_reverse_poly_coeff_request(
      const std::vector<double> forward_coeffs,
      double min_val_x,
      double max_val_x,
      int32_t num_points_to_compute,
      int32_t reverse_poly_order)
  {
    CalculateReversePolyCoeffRequest request;
    request.mutable_forward_coeffs()->CopyFrom({forward_coeffs.cbegin(), forward_coeffs.cend()});
    request.set_min_val_x(min_val_x);
    request.set_max_val_x(max_val_x);
    request.set_num_points_to_compute(num_points_to_compute);
    request.set_reverse_poly_order(reverse_poly_order);
    return request;
  }

  ::grpc::Status calculate_reverse_poly_coeff(const CalculateReversePolyCoeffRequest& request, CalculateReversePolyCoeffResponse& response)
  {
    ::grpc::ClientContext context;
    auto status = stub()->CalculateReversePolyCoeff(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  template <typename TRaw>
  ::grpc::Status read_raw(int32 samples_to_read, ReadRawResponse& response)
  {
    ::grpc::ClientContext context;
    ReadRawRequest request;
    set_request_session_name(request);
    request.set_num_samps_per_chan(samples_to_read);
    request.set_array_size_in_bytes(samples_to_read * sizeof(TRaw));
    request.set_timeout(10.0);
    auto status = stub()->ReadRaw(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  template <typename TRaw>
  ::grpc::Status write_raw(const std::vector<TRaw>& data, WriteRawResponse& response)
  {
    ::grpc::ClientContext context;
    WriteRawRequest request;
    set_request_session_name(request);
    auto byte_data = reinterpret_cast<const char*>(data.data());
    auto write_data = request.mutable_write_array();
    write_data->insert(write_data->cbegin(), byte_data, byte_data + data.size() * sizeof(TRaw));
    request.set_num_samps(static_cast<uint32>(data.size()));
    request.set_timeout(10.0);
    auto status = stub()->WriteRaw(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status wait_for_valid_timestamp(WaitForValidTimestampResponse& response)
  {
    ::grpc::ClientContext context;
    WaitForValidTimestampRequest request;
    set_request_session_name(request);
    request.set_timestamp_event(TimestampEvent::TIMESTAMP_EVENT_FIRST_SAMPLE_TIMESTAMP);
    request.set_timeout(1.000);
    auto status = stub()->WaitForValidTimestamp(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status cfg_time_start_trig(CfgTimeStartTrigResponse& response)
  {
    ::grpc::ClientContext context;
    CfgTimeStartTrigRequest request;
    set_request_session_name(request);

    // Ensure GetCurrentTime macro in WinBase.h does not interfere with the GetCurrentTime function from protobuf.
#ifdef _WIN32
     #pragma push_macro("GetCurrentTime")
     #undef GetCurrentTime
#endif
    auto time = google::protobuf::util::TimeUtil::GetCurrentTime();
#ifdef _WIN32
     #pragma pop_macro("GetCurrentTime")
#endif


    auto duration = google::protobuf::Duration{};
    duration.set_seconds(10);
    time += duration;
    request.mutable_when()->CopyFrom(time);
    request.set_timescale(Timescale2::TIMESCALE2_IO_DEVICE_TIME);
    auto status = stub()->CfgTimeStartTrig(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status cfg_digital_edge_start_trigger_that_never_arrives(CfgDigEdgeStartTrigResponse& response)
  {
    ::grpc::ClientContext context;
    CfgDigEdgeStartTrigRequest request;
    set_request_session_name(request);
    request.set_trigger_source("PFI0");
    request.set_trigger_edge(Edge1::EDGE1_RISING);
    auto status = stub()->CfgDigEdgeStartTrig(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status save_task(SaveTaskResponse& response)
  {
    ::grpc::ClientContext context;
    SaveTaskRequest request;
    set_request_session_name(request);
    request.set_author("grpc.tester@ni.com");
    request.set_options_raw(SaveOptions::SAVE_OPTIONS_OVERWRITE | SaveOptions::SAVE_OPTIONS_ALLOW_INTERACTIVE_DELETION);
    request.set_save_as("saved_task");
    auto status = stub()->SaveTask(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status load_task(LoadTaskResponse& response)
  {
    ::grpc::ClientContext context;
    LoadTaskRequest request;
    request.set_session_name("saved_task");
    auto status = stub()->LoadTask(&context, request, &response);
    if (status.ok()) {
      EXPECT_NE(driver_session_->name(), response.task().name());
      driver_session_ = std::make_unique<nidevice_grpc::Session>(response.task());
    }
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status perform_bridge_offset_nulling_cal_ex(std::string channel, bool skipUnsupportedChannels, PerformBridgeOffsetNullingCalExResponse& response)
  {
    ::grpc::ClientContext context;
    PerformBridgeOffsetNullingCalExRequest request;
    set_request_session_name(request);
    request.set_channel(channel);
    request.set_skip_unsupported_channels(skipUnsupportedChannels);
    auto status = stub()->PerformBridgeOffsetNullingCalEx(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status perform_bridge_shunt_cal_ex(PerformBridgeShuntCalExResponse & response)
  {
    ::grpc::ClientContext context;
    PerformBridgeShuntCalExRequest request;
    set_request_session_name(request);
    request.set_channel("");
    request.set_shunt_resistor_value(100000);
    request.set_shunt_resistor_location(ShuntElementLocation::SHUNT_ELEMENT_LOCATION_R3);
    request.set_shunt_resistor_select(ShuntCalSelect::SHUNT_CAL_SELECT_A);
    request.set_shunt_resistor_source(ShuntCalSource::SHUNT_CAL_SOURCE_DEFAULT);
    request.set_bridge_resistance(120);
    request.set_skip_unsupported_channels(false);
    auto status = stub()->PerformBridgeShuntCalEx(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status perform_strain_shunt_cal_ex(PerformStrainShuntCalExResponse& response)
  {
    ::grpc::ClientContext context;
    PerformStrainShuntCalExRequest request;
    set_request_session_name(request);
    request.set_channel("");
    request.set_shunt_resistor_value(100000);
    request.set_shunt_resistor_location(ShuntElementLocation::SHUNT_ELEMENT_LOCATION_R3);
    request.set_shunt_resistor_select(ShuntCalSelect::SHUNT_CAL_SELECT_A);
    request.set_shunt_resistor_source(ShuntCalSource::SHUNT_CAL_SOURCE_DEFAULT);
    request.set_skip_unsupported_channels(false);
    auto status = stub()->PerformStrainShuntCalEx(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status perform_thrmcpl_lead_offset_nulling_cal(std::string channel, bool skipUnsupportedChannels, PerformThrmcplLeadOffsetNullingCalResponse& response)
  {
    ::grpc::ClientContext context;
    PerformThrmcplLeadOffsetNullingCalRequest request;
    set_request_session_name(request);
    request.set_channel(channel);
    request.set_skip_unsupported_channels(skipUnsupportedChannels);
    auto status = stub()->PerformThrmcplLeadOffsetNullingCal(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status self_cal(SelfCalResponse& response)
  {
    ::grpc::ClientContext context;
    SelfCalRequest request;
    request.set_device_name(DEVICE_NAME);
    auto status = stub()->SelfCal(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status add_network_device(const std::string& ip_address, AddNetworkDeviceResponse& response)
  {
    ::grpc::ClientContext context;
    AddNetworkDeviceRequest request;
    request.set_ip_address(ip_address);
    auto status = stub()->AddNetworkDevice(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status wait_for_next_sample_clock(WaitForNextSampleClockResponse& response)
  {
    ::grpc::ClientContext context;
    WaitForNextSampleClockRequest request;
    set_request_session_name(request);
    request.set_timeout(10.0);
    auto status = stub()->WaitForNextSampleClock(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status connect_terms(const std::string& source, const std::string& destination, ConnectTermsResponse& response)
  {
    ::grpc::ClientContext context;
    ConnectTermsRequest request;
    request.set_source_terminal(source);
    request.set_destination_terminal(destination);
    request.set_signal_modifiers(InvertPolarity::INVERT_POLARITY_DO_NOT_INVERT_POLARITY);
    auto status = stub()->ConnectTerms(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status create_watchdog_timer_task_ex(double timeout, CreateWatchdogTimerTaskExResponse& response)
  {
    ::grpc::ClientContext context;
    CreateWatchdogTimerTaskExRequest request;

    request.set_device_name(DEVICE_NAME);
    request.set_timeout(timeout);
    auto status = stub()->CreateWatchdogTimerTaskEx(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status cfg_watchdog_do_expir_states(const nidevice_grpc::Session& watchdog_session, CfgWatchdogDOExpirStatesResponse& response)
  {
    ::grpc::ClientContext context;
    CfgWatchdogDOExpirStatesRequest request;

    set_request_session_name(request, watchdog_session);
    request.set_channel_names("gRPCSystemTestDAQ/port1/line0:1");
    auto expir_states = std::vector<DigitalLineState>{
        DigitalLineState::DIGITAL_LINE_STATE_HIGH,
        DigitalLineState::DIGITAL_LINE_STATE_HIGH};
    request.mutable_expir_state_array()->CopyFrom({expir_states.cbegin(), expir_states.cend()});
    auto status = stub()->CfgWatchdogDOExpirStates(&context, request, &response);
    client::raise_if_error(status, context);
    return status;
  }

  std::unique_ptr<NiDAQmx::Stub>& stub()
  {
    return nidaqmx_stub_;
  }

  const nidevice_grpc::Session& task()
  {
    return *driver_session_;
  }

  template <typename TRequest>
  void set_request_session_name(TRequest& request)
  {
    set_request_session_name(request, *driver_session_);
  }

  template <typename TRequest>
  void set_request_session_name(TRequest& request, const nidevice_grpc::Session& session)
  {
    request.mutable_task()->set_name(session.name());
  }

  template <typename TResponse>
  void EXPECT_SUCCESS(const TResponse& response)
  {
    EXPECT_EQ(DAQMX_SUCCESS, response.status());
    if (response.status() != DAQMX_SUCCESS) {
      auto error_response = client::get_error_string(stub(), response.status());
      EXPECT_EQ("", error_response.error_string());
    }
  }

  template <typename TResponse>
  void EXPECT_SUCCESS(const ::grpc::Status& status, const TResponse& response)
  {
    EXPECT_SUCCESS(response);
    EXPECT_EQ(::grpc::Status::OK.error_code(), status.error_code());
  }

  template <typename T>
  void EXPECT_DATA_IN_RANGE(const ::google::protobuf::RepeatedField<T>& data, T min_val, T max_val)
  {
    EXPECT_THAT(data, Each(Not(Lt(min_val))));
    EXPECT_THAT(data, Each(Not(Gt(max_val))));
  }

  std::string get_from_trailing_metadata(const ::grpc::ClientContext& context, const std::string& key) const
  {
    auto trailing_metadata = context.GetServerTrailingMetadata();
    auto metadata_iter = trailing_metadata.find(key);
    EXPECT_NE(metadata_iter, trailing_metadata.end()) << "Trailing metadata key '" << key << "' not found";
    return metadata_iter != trailing_metadata.end() ? std::string(metadata_iter->second.data(), metadata_iter->second.size()) : "";
  }

  // Get number of seconds since 1904 epoch (CVI/BTF epoch) for comparison with waveform timestamps
  int64_t get_seconds_since_1904() const
  {    
    auto now = std::chrono::duration_cast<std::chrono::seconds>(
        std::chrono::system_clock::now().time_since_epoch()).count();    
    return now + SecondsFromCVI1904EpochTo1970Epoch;
  }

  std::vector<uint8_t> get_expected_data_for_line(int32 num_samples, int32 line_number) const
  {
    std::vector<uint8_t> data;
    // Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    // Each line represents a bit in the binary representation of the sample number.
    // - line 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1,0,1...
    // - line 1 represents bit 1 - alternates every 2 samples:    0,0,1,1,0,0,1,1...
    // - line 2 represents bit 2 - alternates every 4 samples:    0,0,0,0,1,1,1,1...
    line_number %= 8;
    for (int32 sample_num = 0; sample_num < num_samples; ++sample_num) {
      uint8_t bit_value = (sample_num >> line_number) & 1;
      data.push_back(bit_value);
    }
    return data;
  }

  void verify_digital_waveform_data(
      const std::string& y_data,
      int32 num_samples,
      int32 signals_per_sample,
      int32 line_offset) const
  {
    for (int32 sample = 0; sample < num_samples; ++sample) {
      for (int32 line = 0; line < signals_per_sample; ++line) {
        int32 line_number = line + line_offset;
        auto expected_data = get_expected_data_for_line(num_samples, line_number);
        uint8_t actual_value = static_cast<uint8_t>(y_data[sample * signals_per_sample + line]);
        uint8_t expected_value = expected_data[sample];
        EXPECT_EQ(actual_value, expected_value) 
          << "Mismatch at sample " << sample << ", line " << line_number
          << ": expected " << static_cast<int>(expected_value) 
          << ", got " << static_cast<int>(actual_value);
      }
    }
  }

  ni::protobuf::types::DigitalWaveform create_test_digital_waveform(
      int32 num_samples,
      int32 signal_count,
      int32 line_offset = 0) const
  {
    ni::protobuf::types::DigitalWaveform waveform;
    waveform.set_signal_count(signal_count);
    
    auto* y_data = waveform.mutable_y_data();
    y_data->reserve(num_samples * signal_count);
    
    for (int32 sample = 0; sample < num_samples; ++sample) {
      for (int32 line = 0; line < signal_count; ++line) {
        int32 line_number = line + line_offset;
        auto expected_data = get_expected_data_for_line(num_samples, line_number);
        y_data->push_back(expected_data[sample]);
      }
    }
    
    return waveform;
  }

  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<NiDAQmx::Stub> nidaqmx_stub_;
};

template <typename T>
std::function<T()> random_generator(T begin, T end)
{
  std::random_device device;
  std::default_random_engine engine(device());
  std::uniform_real_distribution<T> distribution(begin, end);
  return [=]() mutable { return distribution(engine); };
}

template <typename T>
std::vector<T> generate_random_data(T min, T max, size_t size)
{
  std::vector<T> data(size);
  auto generate_value_in_range = random_generator<T>(min, max);
  std::generate(data.begin(), data.end(), generate_value_in_range);
  return data;
}

TEST_F(NiDAQmxDriverApiTests, CreateAIVoltageChannel_Succeeds)
{
  CreateAIVoltageChanResponse response;
  auto status = create_ai_voltage_chan(-1.0, 1.0, response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, CreateDIChannel_Succeeds)
{
  CreateDIChanResponse response;
  auto status = create_di_chan(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, CreateDOChannel_Succeeds)
{
  auto response = create_do_chan();

  EXPECT_SUCCESS(response);
}

TEST_F(NiDAQmxDriverApiTests, WriteU32DigitalData_Succeeds)
{
  create_do_chan();
  start_task();

  WriteDigitalU32Response response;
  auto status = write_u32_digital_data(response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_written());
}

TEST_F(NiDAQmxDriverApiTests, ReadU32DigitalData_Succeeds)
{
  create_di_chan();
  start_task();

  ReadDigitalU32Response response;
  auto status = read_u32_digital_data(response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, WriteU16DigitalData_Succeeds)
{
  create_do_chan();
  start_task();

  WriteDigitalU16Response response;
  auto status = write_u16_digital_data(response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_written());
}

TEST_F(NiDAQmxDriverApiTests, ReadU16DigitalData_Succeeds)
{
  create_di_chan();
  start_task();

  ReadDigitalU16Response response;
  auto status = read_u16_digital_data(response);
  stop_task();

  EXPECT_EQ(0, status.error_code());
  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, WriteU8DigitalData_Succeeds)
{
  create_do_chan();
  start_task();

  WriteDigitalU8Response response;
  auto status = write_u8_digital_data(response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_written());
}

TEST_F(NiDAQmxDriverApiTests, WriteDigitalWaveforms_Succeeds)
{
  const auto NUM_SAMPLES = 50;
  const auto TIMEOUT = 10.0;
  CreateDOChanResponse create_channel_response;
  auto create_channel_status = create_do_chan(create_channel_response, "gRPCSystemTestDAQ/port1/line0:2", "do_port1", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_do_chan(create_channel_response, "gRPCSystemTestDAQ/port1/line4:5", "do_port1_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  std::vector<ni::protobuf::types::DigitalWaveform> waveforms;
  waveforms.push_back(create_test_digital_waveform(NUM_SAMPLES, 3, 0)); // 3 lines starting at line 0
  waveforms.push_back(create_test_digital_waveform(NUM_SAMPLES, 2, 4)); // 2 lines starting at line 4

  start_task();
  ::grpc::ClientContext context;
  WriteDigitalWaveformsResponse write_response;
  auto write_status = write_digital_waveforms(context, NUM_SAMPLES, waveforms, false, TIMEOUT, write_response);
  stop_task();

  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(write_response.samps_per_chan_written(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(NUM_SAMPLES));
}

TEST_F(NiDAQmxDriverApiTests, WriteDigitalWaveforms_WithAutoStart_Succeeds)
{
  const auto NUM_SAMPLES = 25;
  const auto TIMEOUT = 10.0;
  CreateDOChanResponse create_channel_response;
  auto create_channel_status = create_do_chan(create_channel_response, "gRPCSystemTestDAQ/port1/line0", "do_line0", LineGrouping::LINE_GROUPING_CHAN_PER_LINE);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  std::vector<ni::protobuf::types::DigitalWaveform> waveforms;
  waveforms.push_back(create_test_digital_waveform(NUM_SAMPLES, 1, 0)); // 1 line starting at line 0

  ::grpc::ClientContext context;
  WriteDigitalWaveformsResponse write_response;
  auto write_status = write_digital_waveforms(context, NUM_SAMPLES, waveforms, true, TIMEOUT, write_response);

  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(write_response.samps_per_chan_written(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(NUM_SAMPLES));
}

TEST_F(NiDAQmxDriverApiTests, WriteDigitalWaveforms_EmptyWaveforms_Fails)
{
  const auto NUM_SAMPLES = 10;
  CreateDOChanResponse create_channel_response;
  auto create_channel_status = create_do_chan(create_channel_response, "gRPCSystemTestDAQ/port1/line0", "do_line0", LineGrouping::LINE_GROUPING_CHAN_PER_LINE);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  std::vector<ni::protobuf::types::DigitalWaveform> waveforms; // Empty waveforms

  // Use direct stub call without raise_if_error to check for gRPC errors
  ::grpc::ClientContext context;
  WriteDigitalWaveformsRequest request;
  WriteDigitalWaveformsResponse response;
  set_request_session_name(request);
  request.set_auto_start(false);
  request.set_timeout(10.0);
  auto write_status = stub()->WriteDigitalWaveforms(&context, request, &response);

  EXPECT_FALSE(write_status.ok());
  EXPECT_EQ(write_status.error_code(), ::grpc::StatusCode::INVALID_ARGUMENT);
  EXPECT_THAT(write_status.error_message(), HasSubstr("No waveforms provided"));
}

TEST_F(NiDAQmxDriverApiTests, ReadU8DigitalData_Succeeds)
{
  create_di_chan();
  start_task();

  ReadDigitalU8Response response;
  auto status = read_u8_digital_data(response);
  stop_task();

  EXPECT_EQ(0, status.error_code());
  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(4, response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_ReadAIData_ReturnsDataInExpectedRange)
{
  const auto AI_MIN = 1.0;
  const auto AI_MAX = 10.0;
  const auto NUM_SAMPS = 100;
  const auto TIMEOUT = 10.0;
  create_ai_voltage_chan(AI_MIN, AI_MAX);

  StartTaskResponse start_response;
  auto start_status = start_task(start_response);
  ReadAnalogF64Response read_response;
  auto read_status = read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);
  StopTaskResponse stop_response;
  auto stop_status = stop_task(stop_response);

  EXPECT_EQ(read_response.read_array_size(), NUM_SAMPS);
  EXPECT_DATA_IN_RANGE(read_response.read_array(), AI_MIN, AI_MAX);
  EXPECT_SUCCESS(start_status, start_response);
  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_SUCCESS(stop_status, stop_response);
}

TEST_F(NiDAQmxDriverApiTests, AIDeviceTempChan_ReadAIData_ReturnsData)
{
  const auto NUM_SAMPS = 100;
  const auto MIN_TEMPERATURE = 0.0;
  const auto MAX_TEMPERATURE = 100.0;
  const auto TIMEOUT = 10.0;
  CreateAIThrmcplChanResponse create_response;
  auto create_status = create_ai_thrmcpl_chan(MIN_TEMPERATURE, MAX_TEMPERATURE, create_response);
  EXPECT_SUCCESS(create_status, create_response);

  start_task();
  ReadAnalogF64Response read_response;
  auto read_status = read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.read_array_size(), NUM_SAMPS);
  EXPECT_DATA_IN_RANGE(read_response.read_array(), MIN_TEMPERATURE, MAX_TEMPERATURE);
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannelWithLinearScale_ReadAIData_ReturnsDataInExpectedRange)
{
  const auto SCALE_NAME = std::string("TestScale");
  const auto AI_MIN = 1.0;
  const auto AI_MAX = 2.0;
  const auto NUM_SAMPS = 1000;
  const auto TIMEOUT = 10.0;
  CreateLinScaleResponse scale_response;
  auto scale_status = create_lin_scale(SCALE_NAME, 0.5, scale_response);
  EXPECT_SUCCESS(scale_status, scale_response);
  auto request = create_ai_voltage_request(AI_MIN, AI_MAX, SCALE_NAME);
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan(request, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  ReadAnalogF64Response read_response;
  auto read_status = read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.read_array_size(), NUM_SAMPS);
  // NOTE: linear scaling on simulated channels isn't really observable.
  // Either way you get a sine wave filling the min/max range.
  EXPECT_DATA_IN_RANGE(read_response.read_array(), AI_MIN, AI_MAX);
}

TEST_F(NiDAQmxDriverApiTests, LinearScale_GetSlopeAttribute_ReturnsInitialSlopeValue)
{
  const auto SCALE_NAME = std::string("TestScale");
  const auto SLOPE = 0.5;
  auto scale_status = create_lin_scale(SCALE_NAME, SLOPE);

  auto response = client::get_scale_attribute_double(
      stub(),
      SCALE_NAME,
      ScaleDoubleAttribute::SCALE_ATTRIBUTE_LIN_SLOPE);

  EXPECT_SUCCESS(response);
  EXPECT_NEAR(SLOPE, response.value(), .0001);
}

TEST_F(NiDAQmxDriverApiTests, SetYInterceptAttribute_GetYInterceptAttribute_ReturnsAttribute)
{
  const auto SCALE_NAME = std::string("TestScale");
  const auto Y_INTERCEPT = -3.0;
  auto scale_status = create_lin_scale(SCALE_NAME, 0.5);
  auto set_response = client::set_scale_attribute_double(
      stub(),
      SCALE_NAME,
      ScaleDoubleAttribute::SCALE_ATTRIBUTE_LIN_Y_INTERCEPT,
      Y_INTERCEPT);

  auto response = client::get_scale_attribute_double(
      stub(),
      SCALE_NAME,
      ScaleDoubleAttribute::SCALE_ATTRIBUTE_LIN_Y_INTERCEPT);

  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(response);
  EXPECT_NEAR(Y_INTERCEPT, response.value(), .0001);
}

TEST_F(NiDAQmxDriverApiTests, SetPreScaledUnits_GetPreScaledUnits_ReturnsAttribute)
{
  const auto SCALE_NAME = std::string("TestScale");
  auto scale_status = create_lin_scale(SCALE_NAME, 0.5);
  auto set_response = client::set_scale_attribute_int32(
      stub(),
      SCALE_NAME,
      ScaleInt32Attribute::SCALE_ATTRIBUTE_PRE_SCALED_UNITS,
      ScaleInt32AttributeValues::SCALE_INT32_UNITS_PRE_SCALED_RPM);

  auto response = client::get_scale_attribute_int32(
      stub(),
      SCALE_NAME,
      ScaleInt32Attribute::SCALE_ATTRIBUTE_PRE_SCALED_UNITS);

  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(response);
  EXPECT_EQ(ScaleInt32AttributeValues::SCALE_INT32_UNITS_PRE_SCALED_RPM, response.value());
  EXPECT_EQ(ScaleInt32AttributeValues::SCALE_INT32_UNITS_PRE_SCALED_RPM, response.value_raw());
}

TEST_F(NiDAQmxDriverApiTests, GetScaledUnitsAsDouble_Fails)
{
  const auto SCALE_NAME = std::string("TestScale");
  const auto UNITS = std::string("Digits");
  auto scale_status = create_lin_scale(SCALE_NAME, 0.5);
  auto set_response = client::set_scale_attribute_string(
      stub(),
      SCALE_NAME,
      ScaleStringAttribute::SCALE_ATTRIBUTE_SCALED_UNITS,
      UNITS);

  EXPECT_THROW_DRIVER_ERROR({
    client::get_scale_attribute_double(
      stub(),
      SCALE_NAME,
      (ScaleDoubleAttribute)ScaleStringAttribute::SCALE_ATTRIBUTE_SCALED_UNITS);
  }, SPECIFIED_ATTRIBUTE_NOT_VALID_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, SetScaledUnits_GetScaledUnits_ReturnsAttribute)
{
  const auto SCALE_NAME = std::string("TestScale");
  const auto UNITS = std::string("Battalions");
  auto scale_status = create_lin_scale(SCALE_NAME, 0.5);
  auto set_response = client::set_scale_attribute_string(
      stub(),
      SCALE_NAME,
      ScaleStringAttribute::SCALE_ATTRIBUTE_SCALED_UNITS,
      UNITS);

  auto response = client::get_scale_attribute_string(
      stub(),
      SCALE_NAME,
      ScaleStringAttribute::SCALE_ATTRIBUTE_SCALED_UNITS);

  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(response);
  EXPECT_EQ(UNITS, response.value());
}

TEST_F(NiDAQmxDriverApiTests, SetPolynomialForwardCoefficients_GetPolynomialForwardCoefficients_ReturnsAttribute)
{
  const auto SCALE_NAME = std::string("TestPolynomialScale");
  const auto INITIAL_COEFFICIENTS = std::vector<double>{1.0, 2.0, 3.0};
  const auto COEFFICIENTS = std::vector<double>{1.0, 3.0, 8.0};
  auto scale_status = create_polynomial_scale(SCALE_NAME, INITIAL_COEFFICIENTS, INITIAL_COEFFICIENTS);
  auto set_response = client::set_scale_attribute_double_array(
      stub(),
      SCALE_NAME,
      ScaleDoubleArrayAttribute::SCALE_ATTRIBUTE_POLY_FORWARD_COEFF,
      COEFFICIENTS);

  auto response = client::get_scale_attribute_double_array(
      stub(),
      SCALE_NAME,
      ScaleDoubleArrayAttribute::SCALE_ATTRIBUTE_POLY_FORWARD_COEFF);

  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(response);
  auto actual = std::vector<double>{response.value().cbegin(), response.value().cend()};
  EXPECT_THAT(actual, ContainerEq(COEFFICIENTS));
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_WithNoAttributeMode_ReturnsWaveformData)
{
  const auto NUM_SAMPLES = 1000;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -1.0, 1.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai1", "ai1", -1.0, 1.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  ::grpc::ClientContext context;
  ReadAnalogWaveformsResponse read_response;
  auto read_status = read_analog_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2);
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    EXPECT_EQ(waveform.y_data_size(), NUM_SAMPLES);    
    EXPECT_FALSE(waveform.has_t0());
    EXPECT_EQ(waveform.dt(), 0.0);    
    EXPECT_EQ(waveform.attributes_size(), 0);
    
    for (const auto& sample : waveform.y_data()) {
      EXPECT_GE(sample, -1.0);
      EXPECT_LE(sample, 1.0);
    }
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_WithTimingMode_ReturnsWaveformDataWithTimingInfo)
{
  const auto NUM_SAMPLES = 100;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -5.0, 5.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai1", "ai1", -5.0, 5.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, NUM_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  start_task();
  ::grpc::ClientContext context;
  ReadAnalogWaveformsResponse read_response;
  auto read_status = read_analog_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2);
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    EXPECT_EQ(waveform.y_data_size(), NUM_SAMPLES);
    EXPECT_TRUE(waveform.has_t0());
    EXPECT_NEAR(waveform.t0().seconds(), get_seconds_since_1904(), 1);    
    EXPECT_GT(waveform.dt(), 0.0);
    
    for (const auto& sample : waveform.y_data()) {
      EXPECT_GE(sample, -5.0);
      EXPECT_LE(sample, 5.0);
    }
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_WithExtendedPropertiesMode_ReturnsWaveformDataWithAttributes)
{
  const auto NUM_SAMPLES = 50;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -2.0, 2.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai1", "ai1", -2.0, 2.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  ::grpc::ClientContext context;
  ReadAnalogWaveformsResponse read_response;
  auto read_status = read_analog_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2);
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    EXPECT_EQ(waveform.y_data_size(), NUM_SAMPLES);
    EXPECT_GT(waveform.attributes_size(), 0);
    
    bool has_channel_name = false;
    bool has_units = false;
    std::string expected_channel_name = (i == 0) ? "ai0" : "ai1";
    
    for (const auto& attr_pair : waveform.attributes()) {
      const auto& attr_name = attr_pair.first;
      const auto& attr_value = attr_pair.second;
      
      if (attr_name == "NI_ChannelName" && attr_value.has_string_value()) {
        if (attr_value.string_value() == expected_channel_name) {
          has_channel_name = true;
        }
      }
      if (attr_name == "NI_UnitDescription" && attr_value.has_string_value()) {
        if (attr_value.string_value() == "Volts") {
          has_units = true;
        }
      }
    }
    EXPECT_TRUE(has_channel_name);
    EXPECT_TRUE(has_units);
    
    for (const auto& sample : waveform.y_data()) {
      EXPECT_GE(sample, -2.0);
      EXPECT_LE(sample, 2.0);
    }
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_WithTimingAndExtendedPropertiesMode_ReturnsWaveformDataWithTimingAndAttributes)
{
  const auto NUM_SAMPLES = 75;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -3.0, 3.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai1", "ai1", -3.0, 3.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(2000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, NUM_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  start_task();
  ::grpc::ClientContext context;
  ReadAnalogWaveformsResponse read_response;
  const auto combined_mode = static_cast<WaveformAttributeMode>(
    static_cast<int32>(WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING) | 
    static_cast<int32>(WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES)
  );
  auto read_status = read_analog_waveforms(context, NUM_SAMPLES, TIMEOUT, combined_mode, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2);
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    EXPECT_EQ(waveform.y_data_size(), NUM_SAMPLES);
    EXPECT_TRUE(waveform.has_t0());
    EXPECT_NEAR(waveform.t0().seconds(), get_seconds_since_1904(), 1);
    EXPECT_GT(waveform.dt(), 0.0);
    EXPECT_GT(waveform.attributes_size(), 0);
    
    bool has_channel_name = false;
    bool has_units = false;
    std::string expected_channel_name = (i == 0) ? "ai0" : "ai1";
    
    for (const auto& attr_pair : waveform.attributes()) {
      const auto& attr_name = attr_pair.first;
      const auto& attr_value = attr_pair.second;
      
      if (attr_name == "NI_ChannelName" && attr_value.has_string_value()) {
        if (attr_value.string_value() == expected_channel_name) {
          has_channel_name = true;
        }
      }
      if (attr_name == "NI_UnitDescription" && attr_value.has_string_value()) {
        if (attr_value.string_value() == "Volts") {
          has_units = true;
        }
      }
    }
    EXPECT_TRUE(has_channel_name);
    EXPECT_TRUE(has_units);
    
    for (const auto& sample : waveform.y_data()) {
      EXPECT_GE(sample, -3.0);
      EXPECT_LE(sample, 3.0);
    }
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_ReadAllAvailable_ReturnsAvailableSamples)
{
  const auto FINITE_SAMPLES = 100;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -1.0, 1.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai1", "ai1", -1.0, 1.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  start_task();
  ::grpc::ClientContext context;
  ReadAnalogWaveformsResponse read_response;
  auto read_status = read_analog_waveforms(context, READ_ALL_AVAILABLE, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2);
  EXPECT_EQ(read_response.samps_per_chan_read(), FINITE_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(FINITE_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    EXPECT_EQ(waveform.y_data_size(), FINITE_SAMPLES);    
    EXPECT_FALSE(waveform.has_t0());
    EXPECT_EQ(waveform.dt(), 0.0);    
    EXPECT_EQ(waveform.attributes_size(), 0);
    
    for (const auto& sample : waveform.y_data()) {
      EXPECT_GE(sample, -1.0);
      EXPECT_LE(sample, 1.0);
    }
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_WithNoAttributeMode_ReturnsWaveformData)
{
  const auto NUM_SAMPLES = 100;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0:2", "di_port0", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line4:5", "di_port0_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  ::grpc::ClientContext context;
  ReadDigitalWaveformsResponse read_response;
  auto read_status = read_digital_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2); // Two channels: di_port0 and di_port0_lines45
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  const auto& waveform0 = read_response.waveforms(0);
  EXPECT_EQ(waveform0.signal_count(), 3); // 3 lines in port0 (line0:2 means 0,1,2)
  EXPECT_EQ(static_cast<int32>(waveform0.y_data().size()), NUM_SAMPLES * 3); // 3 bytes per sample
  verify_digital_waveform_data(waveform0.y_data(), NUM_SAMPLES, 3, 0);
  
  const auto& waveform1 = read_response.waveforms(1);
  EXPECT_EQ(waveform1.signal_count(), 2); // 2 lines in port0 (line4:5 means 4,5)
  EXPECT_EQ(static_cast<int32>(waveform1.y_data().size()), NUM_SAMPLES * 2); // 2 bytes per sample
  verify_digital_waveform_data(waveform1.y_data(), NUM_SAMPLES, 2, 4);
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_WithTimingMode_ReturnsWaveformDataWithTimingInfo)
{
  const auto NUM_SAMPLES = 50;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0:2", "di_port0", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line4:5", "di_port0_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, NUM_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  start_task();
  ::grpc::ClientContext context;
  ReadDigitalWaveformsResponse read_response;
  auto read_status = read_digital_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2); // Two channels: di_port0 and di_port0_lines45
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
    
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    
    int expected_signal_count = (i == 0) ? 3 : 2; // port0 lines 0:2 has 3 lines, lines 4:5 has 2 lines
    EXPECT_EQ(waveform.signal_count(), expected_signal_count);
    EXPECT_EQ(static_cast<int32>(waveform.y_data().size()), NUM_SAMPLES * expected_signal_count);
    
    EXPECT_TRUE(waveform.has_t0());
    const auto& timestamp = waveform.t0();
    EXPECT_NEAR(timestamp.seconds(), get_seconds_since_1904(), 1);
    EXPECT_GT(waveform.dt(), 0.0);
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_WithExtendedPropertiesMode_ReturnsWaveformDataWithAttributes)
{
  const auto NUM_SAMPLES = 50;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0:2", "di_port0", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line4:5", "di_port0_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  ::grpc::ClientContext context;
  ReadDigitalWaveformsResponse read_response;
  auto read_status = read_digital_waveforms(context, NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2); // Two channels: di_port0 and di_port0_lines45
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    
    int expected_signal_count = (i == 0) ? 3 : 2; // port0 lines 0:2 has 3 lines, lines 4:5 has 2 lines
    EXPECT_EQ(waveform.signal_count(), expected_signal_count);
    EXPECT_EQ(static_cast<int32>(waveform.y_data().size()), NUM_SAMPLES * expected_signal_count);
    EXPECT_GT(waveform.attributes_size(), 0);
    
    std::string expected_channel_name = (i == 0) ? "di_port0" : "di_port0_lines45";
    bool has_channel_name = false;
    for (const auto& attr_pair : waveform.attributes()) {
      const auto& attr_name = attr_pair.first;
      const auto& attr_value = attr_pair.second;
      
      if (attr_name == "NI_ChannelName" && attr_value.has_string_value()) {
        if (attr_value.string_value() == expected_channel_name) {
          has_channel_name = true;
        }
      }
    }
    EXPECT_TRUE(has_channel_name);
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_WithTimingAndExtendedPropertiesMode_ReturnsWaveformDataWithTimingAndAttributes)
{
  const auto NUM_SAMPLES = 50;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0:2", "di_port0", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line4:5", "di_port0_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, NUM_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  const auto combined_mode = static_cast<WaveformAttributeMode>(
    WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_TIMING | 
    WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES);

  start_task();
  ::grpc::ClientContext context;
  ReadDigitalWaveformsResponse read_response;
  auto read_status = read_digital_waveforms(context, NUM_SAMPLES, TIMEOUT, combined_mode, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2); // Two channels: di_port0 and di_port0_lines45
  EXPECT_EQ(read_response.samps_per_chan_read(), NUM_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(NUM_SAMPLES));
  
  for (int i = 0; i < read_response.waveforms_size(); ++i) {
    const auto& waveform = read_response.waveforms(i);
    
    int expected_signal_count = (i == 0) ? 3 : 2; // port0 lines 0:2 has 3 lines, lines 4:5 has 2 lines
    EXPECT_EQ(waveform.signal_count(), expected_signal_count);
    EXPECT_EQ(static_cast<int32>(waveform.y_data().size()), NUM_SAMPLES * expected_signal_count);
    
    EXPECT_TRUE(waveform.has_t0());
    EXPECT_GT(waveform.dt(), 0.0);
    
    EXPECT_GT(waveform.attributes_size(), 0);
    
    std::string expected_channel_name = (i == 0) ? "di_port0" : "di_port0_lines45";
    bool has_channel_name = false;
    for (const auto& attr_pair : waveform.attributes()) {
      const auto& attr_name = attr_pair.first;
      const auto& attr_value = attr_pair.second;
      
      if (attr_name == "NI_ChannelName" && attr_value.has_string_value()) {
        if (attr_value.string_value() == expected_channel_name) {
          has_channel_name = true;
        }
      }
    }
    EXPECT_TRUE(has_channel_name);
  }
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_ReadAllAvailable_ReturnsAvailableSamples)
{
  const auto FINITE_SAMPLES = 75;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0:2", "di_port0", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line4:5", "di_port0_lines45", LineGrouping::LINE_GROUPING_CHAN_FOR_ALL_LINES);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  auto timing_request = create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLES);
  CfgSampClkTimingResponse timing_response;
  auto timing_status = cfg_samp_clk_timing(timing_request, timing_response);
  EXPECT_SUCCESS(timing_status, timing_response);

  start_task();
  ::grpc::ClientContext context;
  ReadDigitalWaveformsResponse read_response;
  auto read_status = read_digital_waveforms(context, READ_ALL_AVAILABLE, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  stop_task();

  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(read_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(read_response.waveforms_size(), 2); // Two channels: di_port0 and di_port0_lines45
  EXPECT_EQ(read_response.samps_per_chan_read(), FINITE_SAMPLES);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), std::to_string(FINITE_SAMPLES));
  
  const auto& waveform0 = read_response.waveforms(0);
  EXPECT_EQ(waveform0.signal_count(), 3); // 3 lines in port0 (line0:2 means 0,1,2)
  EXPECT_EQ(static_cast<int32>(waveform0.y_data().size()), FINITE_SAMPLES * 3); // 3 bytes per sample
  verify_digital_waveform_data(waveform0.y_data(), FINITE_SAMPLES, 3, 0);
  
  const auto& waveform1 = read_response.waveforms(1);
  EXPECT_EQ(waveform1.signal_count(), 2); // 2 lines in port0 (line4:5 means 4,5)
  EXPECT_EQ(static_cast<int32>(waveform1.y_data().size()), FINITE_SAMPLES * 2); // 2 bytes per sample
  verify_digital_waveform_data(waveform1.y_data(), FINITE_SAMPLES, 2, 4);
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_SingleChannel_Succeeds)
{
  const double AO_MIN = -5.0;
  const double AO_MAX = 5.0;
  const auto NUM_SAMPLES = 1000;
  const auto TIMEOUT = 10.0;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan(AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  std::vector<std::vector<double>> waveform_data(1);
  waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  
  ::grpc::ClientContext context;
  WriteAnalogWaveformsResponse write_response;
  auto write_status = write_analog_waveforms(context, waveform_data, false, TIMEOUT, write_response);
  stop_task();

  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(write_response.samps_per_chan_written(), NUM_SAMPLES);
  EXPECT_GT(write_response.samps_per_chan_written(), 0);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(NUM_SAMPLES));
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_MultipleChannels_Succeeds)
{
  const double AO_MIN = -3.0;
  const double AO_MAX = 3.0;
  const auto NUM_SAMPLES = 500;
  const auto TIMEOUT = 10.0;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao0", "ao0", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao1", "ao1", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  std::vector<std::vector<double>> waveform_data(2);
  waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  waveform_data[1] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  
  ::grpc::ClientContext context;
  WriteAnalogWaveformsResponse write_response;
  auto write_status = write_analog_waveforms(context, waveform_data, false, TIMEOUT, write_response);
  stop_task();

  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(write_response.samps_per_chan_written(), NUM_SAMPLES);
  EXPECT_GT(write_response.samps_per_chan_written(), 0);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(NUM_SAMPLES));
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_WithAutoStart_Succeeds)
{
  const double AO_MIN = -2.0;
  const double AO_MAX = 2.0;
  const auto NUM_SAMPLES = 100;
  const auto TIMEOUT = 10.0;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan(AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  // Don't start task manually since we're using auto_start
  std::vector<std::vector<double>> waveform_data(1);
  waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  
  ::grpc::ClientContext context;
  WriteAnalogWaveformsResponse write_response;
  auto write_status = write_analog_waveforms(context, waveform_data, true, TIMEOUT, write_response);
  stop_task();

  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.status(), DAQMX_SUCCESS);
  EXPECT_EQ(write_response.samps_per_chan_written(), NUM_SAMPLES);
  EXPECT_GT(write_response.samps_per_chan_written(), 0);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(NUM_SAMPLES));
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_WithOutOfRangeValue_ReturnsInvalidAODataError)
{
  const double AO_MIN = 0.0;
  const double AO_MAX = 5.0;
  const auto NUM_SAMPLES = 100;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan(AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  EXPECT_THROW_DRIVER_ERROR({
    std::vector<std::vector<double>> waveform_data(1);
    waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
    waveform_data[0][50] = AO_MAX + 10.0;  // Out of range value
    
    ::grpc::ClientContext context;
    WriteAnalogWaveformsResponse write_response;
    write_analog_waveforms(context, waveform_data, false, 10.0, write_response);
  }, INVALID_AO_DATA_WRITE_ERROR);
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_MismatchedNumberOfWaveforms_ReturnsError)
{
  const double AO_MIN = -1.0;
  const double AO_MAX = 1.0;
  const auto NUM_SAMPLES = 100;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan(AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  // Provide waveforms for 2 channels but task only has 1 channel
  std::vector<std::vector<double>> waveform_data(2);
  waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  waveform_data[1] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  
  EXPECT_THROW({
    try {
      ::grpc::ClientContext context;
      WriteAnalogWaveformsResponse write_response;
      write_analog_waveforms(context, waveform_data, false, 10.0, write_response);
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_EQ(::grpc::StatusCode::UNKNOWN, ex.StatusCode());
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_MismatchedSampleCounts_ReturnsError)
{
  const double AO_MIN = -1.0;
  const double AO_MAX = 1.0;
  const auto NUM_SAMPLES = 100;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao0", "ao0", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);
  create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao1", "ao1", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  // Provide waveforms with different sample counts
  std::vector<std::vector<double>> waveform_data(2);
  waveform_data[0] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES);
  waveform_data[1] = generate_random_data(AO_MIN, AO_MAX, NUM_SAMPLES / 2);  // Different count
  
  EXPECT_THROW_GRPC_INVALID_ARGUMENT({
    ::grpc::ClientContext context;
    WriteAnalogWaveformsResponse write_response;
    write_analog_waveforms(context, waveform_data, false, 10.0, write_response);
  });
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_ZeroSamples_Succeeds)
{
  const double AO_MIN = -1.0;
  const double AO_MAX = 1.0;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao0", "ao0", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  // Provide waveforms with zero samples
  std::vector<std::vector<double>> waveform_data(1);
  waveform_data[0] = {};  // Empty waveform
  
  ::grpc::ClientContext context;
  WriteAnalogWaveformsResponse write_response;
  auto write_status = write_analog_waveforms(context, waveform_data, false, 10.0, write_response);
  
  EXPECT_SUCCESS(write_status, write_response);
  EXPECT_EQ(write_response.samps_per_chan_written(), 0);
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), std::to_string(0));
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, ReadAnalogWaveforms_InvalidNumSampsPerChan_ReturnsErrorAndZeroMetadata)
{
  const auto INVALID_NUM_SAMPLES = -2;
  const auto TIMEOUT = 10.0;
  CreateAIVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ai_voltage_chan("gRPCSystemTestDAQ/ai0", "ai0", -1.0, 1.0, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  ::grpc::ClientContext context;
  EXPECT_THROW_DRIVER_ERROR({
    ReadAnalogWaveformsResponse read_response;
    auto read_status = read_analog_waveforms(context, INVALID_NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  }, DAQMX_ERROR_INVALID_NUMBER_SAMPLES_TO_READ);
  
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), "0");
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, ReadDigitalWaveforms_InvalidNumSampsPerChan_ReturnsErrorAndZeroMetadata)
{
  const auto INVALID_NUM_SAMPLES = -2;
  const auto TIMEOUT = 10.0;
  CreateDIChanResponse create_channel_response;
  auto create_channel_status = create_di_chan(create_channel_response, "gRPCSystemTestDAQ/port0/line0", "di_line0", LineGrouping::LINE_GROUPING_CHAN_PER_LINE);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  start_task();
  
  ::grpc::ClientContext context;
  EXPECT_THROW_DRIVER_ERROR({
    ReadDigitalWaveformsResponse read_response;
    auto read_status = read_digital_waveforms(context, INVALID_NUM_SAMPLES, TIMEOUT, WaveformAttributeMode::WAVEFORM_ATTRIBUTE_MODE_NONE, read_response);
  }, DAQMX_ERROR_INVALID_NUMBER_SAMPLES_TO_READ);
  
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-read"), "0");
  
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, WriteAnalogWaveforms_TaskNotRunning_ReturnsErrorAndZeroMetadata)
{
  const double AO_MIN = -1.0;
  const double AO_MAX = 1.0;
  const auto NUM_SAMPLES = 10;
  const auto TIMEOUT = 1.0;
  
  CreateAOVoltageChanResponse create_channel_response;
  auto create_channel_status = create_ao_voltage_chan("gRPCSystemTestDAQ/ao0", "ao0", AO_MIN, AO_MAX, create_channel_response);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  std::vector<std::vector<double>> waveform_data(1, std::vector<double>(NUM_SAMPLES, 1.0));

  ::grpc::ClientContext context;
  EXPECT_THROW_DRIVER_ERROR({
    WriteAnalogWaveformsResponse write_response;
    auto write_status = write_analog_waveforms(context, waveform_data, false, TIMEOUT, write_response);
  }, DAQMX_ERROR_CANNOT_WRITE_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING);
  
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), "0");
}

TEST_F(NiDAQmxDriverApiTests, WriteDigitalWaveforms_TaskNotRunning_ReturnsErrorAndZeroMetadata)
{
  const auto NUM_SAMPLES = 10;
  const auto TIMEOUT = 1.0;
  CreateDOChanResponse create_channel_response;
  auto create_channel_status = create_do_chan(create_channel_response, "gRPCSystemTestDAQ/port1/line0", "do_line0", LineGrouping::LINE_GROUPING_CHAN_PER_LINE);
  EXPECT_SUCCESS(create_channel_status, create_channel_response);

  std::vector<ni::protobuf::types::DigitalWaveform> waveforms;
  waveforms.push_back(create_test_digital_waveform(NUM_SAMPLES, 1, 0));

  ::grpc::ClientContext context;
  EXPECT_THROW_DRIVER_ERROR({
    WriteDigitalWaveformsResponse write_response;
    auto write_status = write_digital_waveforms(context, NUM_SAMPLES, waveforms, false, TIMEOUT, write_response);
  }, DAQMX_ERROR_CANNOT_WRITE_WHEN_AUTO_START_FALSE_AND_TASK_NOT_RUNNING);
  
  EXPECT_EQ(get_from_trailing_metadata(context, "ni-samps-per-chan-written"), "0");
}

TEST_F(NiDAQmxDriverApiTests, AOVoltageChannel_WriteAOData_Succeeds)
{
  const double AO_MIN = 1.0;
  const double AO_MAX = 10.0;
  CreateAOVoltageChanResponse create_channel_response;
  create_ao_voltage_chan(AO_MIN, AO_MAX, create_channel_response);

  start_task();
  auto write_data = generate_random_data(AO_MIN, AO_MAX, 100);
  WriteAnalogF64Response write_response;
  auto write_status = write_analog_f64(write_data, write_response);
  stop_task();

  EXPECT_SUCCESS(write_status, write_response);
}

TEST_F(NiDAQmxDriverApiTests, AOVoltageChannel_WriteAODataWithOutOfRangeValue_ReturnsInvalidAODataError)
{
  const double AO_MIN = 1.0;
  const double AO_MAX = 10.0;
  create_ao_voltage_chan(AO_MIN, AO_MAX);

  start_task();
  EXPECT_THROW_DRIVER_ERROR({
    auto write_data = generate_random_data(AO_MIN, AO_MAX, 100);
    write_data[80] += AO_MAX;
    WriteAnalogF64Response write_response;
    write_analog_f64(write_data, write_response);
  }, INVALID_AO_DATA_WRITE_ERROR);
  stop_task();
}

TEST_F(NiDAQmxDriverApiTests, TaskWithAOChannel_GetNthTaskDevice_ReturnsDeviceForChannel)
{
  const double AO_MIN = 1.0;
  const double AO_MAX = 10.0;
  create_ao_voltage_chan(AO_MIN, AO_MAX);

  GetNthTaskDeviceResponse nth_device_response;
  auto status = get_nth_task_device(1, nth_device_response);

  EXPECT_SUCCESS(status, nth_device_response);
  EXPECT_EQ(DEVICE_NAME, nth_device_response.buffer());
}

TEST_F(NiDAQmxDriverApiTests, RunningTask_StopWithTaskControl_TaskIsDone)
{
  create_ao_voltage_chan(0.0, 1.0);
  start_task();
  EXPECT_FALSE(is_task_done());

  TaskControlResponse response;
  auto status = task_control(TaskControlAction::TASK_CONTROL_ACTION_TASK_STOP, response);

  EXPECT_SUCCESS(status, response);
  EXPECT_TRUE(is_task_done());
}

TEST_F(NiDAQmxDriverApiTests, CreateCIFreqChannel_Succeeds)
{
  CreateCIFreqChanResponse response;
  auto status = create_ci_freq_chan(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, GetErrorString_ReturnsErrorMessage)
{
  GetErrorStringResponse response;
  auto status = get_error_string(INVALID_ATTRIBUTE_VALUE_ERROR, response);

  EXPECT_SUCCESS(status, response);
  const auto& error_string = response.error_string();
  EXPECT_THAT(
      error_string,
      StrEq("Requested value is not a supported value for this property. The property value may be invalid because it conflicts with another property."));
  // If we don't get the correct ivi-dance size we can get a string padded out with extra nulls.
  // Comparing to the length of the null-terminated c_str will catch this.
  EXPECT_EQ(error_string.length(), std::strlen(error_string.c_str()));
}

TEST_F(NiDAQmxDriverApiTests, ReadBinaryI32_Succeeds)
{
  create_ai_voltage_chan(-5.0, 5.0);
  start_task();

  const auto NUM_SAMPS = 4;
  auto response = client::read_binary_i32(
      stub(),
      task(),
      NUM_SAMPS,
      10.0,
      GroupBy::GROUP_BY_GROUP_BY_CHANNEL,
      NUM_SAMPS);
  stop_task();

  EXPECT_EQ(NUM_SAMPS, response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, AOVoltageChannel_WriteBinaryI16_Succeeds)
{
  create_ao_voltage_chan(-5.0, 5.0);

  start_task();
  WriteBinaryI16Response response;
  auto status = write_binary_i16({12, -13, 32767, 15, -32768}, response);
  stop_task();

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_ReadBinaryI16_Succeeds)
{
  create_ai_voltage_chan(-5.0, 5.0);

  start_task();
  const auto NUM_SAMPS = 10;
  auto response = client::read_binary_i16(
      stub(),
      task(),
      NUM_SAMPS,
      10.0,
      GroupBy::GROUP_BY_GROUP_BY_CHANNEL,
      NUM_SAMPS);
  stop_task();

  EXPECT_EQ(NUM_SAMPS, response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_ReadRaw_Succeeds)
{
  using TRaw = uint16_t;
  create_ai_voltage_chan(-5.0, 5.0);

  start_task();
  ReadRawResponse response;
  const auto NUM_SAMPS = 10;
  auto status = read_raw<TRaw>(NUM_SAMPS, response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(NUM_SAMPS, response.samps_read());
  EXPECT_EQ(NUM_SAMPS * sizeof(TRaw), response.read_array().size());
  auto data_ptr = reinterpret_cast<const TRaw*>(response.read_array().data());
  auto data_vector = std::vector<TRaw>(data_ptr, data_ptr + NUM_SAMPS);
  EXPECT_THAT(data_vector, Each(Not(Eq(0))));
}

TEST_F(NiDAQmxDriverApiTests, AOVoltageChannel_WriteRaw_Succeeds)
{
  using TRaw = uint16_t;
  const auto RAW_DATA = std::vector<TRaw>{65046, 262, 97, 902, 882, 978, 1050, 1786, 1914, 2038};
  create_ao_voltage_chan(-5.0, 5.0);

  start_task();
  WriteRawResponse response;
  const auto NUM_SAMPS = 10;
  auto status = write_raw<TRaw>(RAW_DATA, response);
  stop_task();

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(NUM_SAMPS, response.samps_per_chan_written());
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_CfgSampClkTimingAndAcquireData_Succeeds)
{
  create_ai_voltage_chan(0.0, 1.0);
  const auto TIMEOUT = 10.0;

  CfgSampClkTimingResponse response;
  auto config_status = cfg_samp_clk_timing(response);
  start_task();
  ReadAnalogF64Response read_response;
  const auto NUM_SAMPS = 10;
  auto read_status = read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);
  stop_task();

  EXPECT_SUCCESS(config_status, response);
  EXPECT_SUCCESS(read_status, read_response);
  EXPECT_EQ(NUM_SAMPS, read_response.samps_per_chan_read());
}

TEST_F(NiDAQmxDriverApiTests, AIFiniteAcquisition_ReadWithTimeoutTooSmall_SamplesNotYetAvailableStatusReturned)
{
  create_ai_voltage_chan(0.0, 1.0);
  const auto TIMEOUT = 100e-3;
  const auto SAMPLE_RATE = 1000.0;
  const auto SAMPLES_PER_CHAN = 60000UL;
  const auto NUM_SAMPS = 60000;
  cfg_samp_clk_timing(
      create_cfg_samp_clk_timing_request(SAMPLE_RATE, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS , SAMPLES_PER_CHAN));
  
  start_task();
  ReadAnalogF64Response read_response;
  read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);

  EXPECT_EQ(SAMPLES_NOT_YET_AVAILABLE_ERROR, read_response.status());
}

TEST_F(NiDAQmxDriverApiTests, ChannelWithDoneEventRegistered_RunCompleteFiniteAcquisition_DoneEventResponseIsReceived)
{
  const auto FINITE_SAMPLE_COUNT = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
    create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext reader_context;
  auto reader = register_done_event(reader_context);
  reader->WaitForInitialMetadata();

  start_task();
  read_analog_f64(FINITE_SAMPLE_COUNT, FINITE_SAMPLE_COUNT);
  RegisterDoneEventResponse response;
  read_stream(reader_context, *reader, response);

  EXPECT_EQ(DAQMX_SUCCESS, response.status());
}

TEST_F(NiDAQmxDriverApiTests, ChannelWithDoneEventRegistered_RunMultipleFiniteAcquisitions_DoneEventResponsesAreReceived)
{
  const auto ACQUISITION_COUNT = 3UL;
  const auto FINITE_SAMPLE_COUNT = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
    create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext reader_context;
  auto reader = register_done_event(reader_context);
  reader->WaitForInitialMetadata();

  std::vector<RegisterDoneEventResponse> responses;
  for (auto acquisition = 0UL; acquisition < ACQUISITION_COUNT; ++acquisition) {
    start_task();
    read_analog_f64(FINITE_SAMPLE_COUNT, FINITE_SAMPLE_COUNT);
    read_stream(reader_context, *reader, 1, responses);
    stop_task();
  }

  EXPECT_THAT(responses, SizeIs(ACQUISITION_COUNT));
  EXPECT_THAT(responses, Each(Property(&RegisterDoneEventResponse::status, Eq(DAQMX_SUCCESS))));
}

TEST_F(NiDAQmxDriverApiTests, ChannelWithEveryNSamplesEventRegistered_WaitForSamplesMultipleTimes_EveryNSamplesEventResponsesAreReceived)
{
  const auto FINITE_SAMPLE_COUNT = 100UL;
  const auto N_SAMPLES = 10UL;
  const auto N_READS = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
      create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES);
  reader->WaitForInitialMetadata();

  start_task();
  std::vector<RegisterEveryNSamplesEventResponse> responses;
  for (auto i = 0UL; i < N_READS; ++i) {
    read_stream(reader_context, *reader, 1, responses);
    read_analog_f64(N_SAMPLES, N_SAMPLES);
  }

  EXPECT_THAT(responses, SizeIs(N_READS));
  EXPECT_THAT(responses, Each(Property(&RegisterEveryNSamplesEventResponse::n_samples, Eq(N_SAMPLES))));
  EXPECT_THAT(responses, Each(Property(&RegisterEveryNSamplesEventResponse::status, Eq(DAQMX_SUCCESS))));
}

TEST_F(NiDAQmxDriverApiTests, ChannelWithEveryNSamplesEventRegistered_RunMultipleFiniteAcquisitions_EveryNSamplesEventResponsesAreReceived)
{
  const auto ACQUISITION_COUNT = 3UL;
  const auto FINITE_SAMPLE_COUNT = 100UL;
  const auto N_SAMPLES = 10UL;
  const auto N_READS = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
      create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES);
  reader->WaitForInitialMetadata();

  std::vector<RegisterEveryNSamplesEventResponse> responses;
  for (auto acquisition = 0UL; acquisition < ACQUISITION_COUNT; ++acquisition) {
    start_task();
    for (auto i = 0UL; i < N_READS; ++i) {
      read_stream(reader_context, *reader, 1, responses);
      read_analog_f64(N_SAMPLES, N_SAMPLES);
    }
    stop_task();
  }

  EXPECT_THAT(responses, SizeIs(ACQUISITION_COUNT * N_READS));
  EXPECT_THAT(responses, Each(Property(&RegisterEveryNSamplesEventResponse::n_samples, Eq(N_SAMPLES))));
  EXPECT_THAT(responses, Each(Property(&RegisterEveryNSamplesEventResponse::status, Eq(DAQMX_SUCCESS))));
}

TEST_F(NiDAQmxDriverApiTests, Channel_RunMultipleFiniteAcquisitionsWithVaryingEveryNSamplesEventInterval_EveryNSamplesEventResponsesAreReceived)
{
  const auto ACQUISITION_COUNT = 3UL;
  const auto FINITE_SAMPLE_COUNT = 100UL;
  const uint32_t N_SAMPLES[ACQUISITION_COUNT] = {10, 20, 25};
  const size_t N_READS[ACQUISITION_COUNT] = {10, 5, 4};
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
    create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));

  std::vector<RegisterEveryNSamplesEventResponse> responses[ACQUISITION_COUNT];
  for (auto acquisition = 0UL; acquisition < ACQUISITION_COUNT; ++acquisition) {
    ASSERT_EQ(FINITE_SAMPLE_COUNT, N_SAMPLES[acquisition] * N_READS[acquisition]);
    ::grpc::ClientContext reader_context;
    auto reader = register_every_n_samples_event(reader_context, N_SAMPLES[acquisition]);
    reader->WaitForInitialMetadata();
    start_task();
    for (auto i = 0UL; i < N_READS[acquisition]; ++i) {
      read_stream(reader_context, *reader, 1, responses[acquisition]);
      read_analog_f64(N_SAMPLES[acquisition], N_SAMPLES[acquisition]);
    }
    stop_task();
    unregister_every_n_samples_event();
  }

  for (auto acquisition = 0UL; acquisition < ACQUISITION_COUNT; ++acquisition) {
    SCOPED_TRACE(Message() << "acquisition=" << acquisition);
    EXPECT_THAT(responses[acquisition], SizeIs(N_READS[acquisition]));
    EXPECT_THAT(responses[acquisition], Each(Property(&RegisterEveryNSamplesEventResponse::n_samples, Eq(N_SAMPLES[acquisition]))));
    EXPECT_THAT(responses[acquisition], Each(Property(&RegisterEveryNSamplesEventResponse::status, Eq(DAQMX_SUCCESS))));
  }
}

TEST_F(NiDAQmxDriverApiTests, ChannelWithDoneEventRegisteredTwice_RunCompleteFiniteAcquisition_DoneEventResponseAndAlreadyRegisteredErrorReceived)
{
  const auto FINITE_SAMPLE_COUNT = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
      create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext reader_context1, reader_context2;
  auto reader1 = register_done_event(reader_context1);
  reader1->WaitForInitialMetadata();
  auto reader2 = register_done_event(reader_context2);
  reader2->WaitForInitialMetadata();

  start_task();
  read_analog_f64(FINITE_SAMPLE_COUNT, FINITE_SAMPLE_COUNT);
  RegisterDoneEventResponse response1, response2;
  read_stream(reader_context1, *reader1, response1);

  EXPECT_EQ(DAQMX_SUCCESS, response1.status());
  EXPECT_THROW_DRIVER_ERROR({
    read_stream(reader_context2, *reader2, response2);
  }, DONE_EVENT_ALREADY_REGISTERED_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventRegisteredWithNonBufferedTask_StartTask_NotSupportedForNonBufferedTaskErrorReceived)
{
  const auto N_SAMPLES = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES);
  reader->WaitForInitialMetadata();

  EXPECT_THROW_DRIVER_ERROR({
    start_task();
  }, EVERY_N_SAMPLES_EVENT_NOT_SUPPORTED_FOR_NON_BUFFERED_TASKS);
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventRegisteredWithWrongEventType_ReadStream_NotSupportedByDeviceErrorReceived)
{
  const auto N_SAMPLES = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES, EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER);
  reader->WaitForInitialMetadata();

  RegisterEveryNSamplesEventResponse response;
  EXPECT_THROW_DRIVER_ERROR({
    read_stream(reader_context, *reader, response);
  }, EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventRegisteredWithWrongEventType_Finish_NotSupportedByDeviceErrorReceived)
{
  const auto N_SAMPLES = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES, EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER);
  reader->WaitForInitialMetadata();

  EXPECT_THROW_DRIVER_ERROR({
    auto status = reader->Finish();
    client::raise_if_error(status, reader_context);
  }, EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventRegisteredWithWrongEventType_Cancel_NoErrors)
{
  const auto N_SAMPLES = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES, EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER);
  reader->WaitForInitialMetadata();

  reader_context.TryCancel();
}

TEST_F(NiDAQmxDriverApiTests, AsyncEveryNSamplesEventRegistered_OnEventReadAnalogF64_EventAndReadResponsesAreReceived)
{
  const auto FINITE_SAMPLE_COUNT = 100UL;
  const auto N_SAMPLES = 10UL;
  const auto N_READS = 10UL;
  const auto EVENT_START_CALL_TAG = (void*)1;
  const auto EVENT_READ_INITIAL_METADATA_TAG = (void*)2;
  const auto EVENT_READ_TAG = (void*)3;
  const auto READ_ANALOG_F64_TAG = (void*)4;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(
      create_cfg_samp_clk_timing_request(1000.0, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_FINITE_SAMPS, FINITE_SAMPLE_COUNT));
  ::grpc::ClientContext event_context;
  ::grpc::CompletionQueue completion_queue;
  auto shut_down_on_exit = make_scope_exit([&]{ shut_down_completion_queue(completion_queue); });
  auto event_reader = async_register_every_n_samples_event(event_context, completion_queue, EVENT_START_CALL_TAG, N_SAMPLES);
  async_wait_for_initial_metadata(event_context, *event_reader, completion_queue, EVENT_START_CALL_TAG, EVENT_READ_INITIAL_METADATA_TAG);

  start_task();
  RegisterEveryNSamplesEventResponse event_response;
  event_reader->Read(&event_response, EVENT_READ_TAG);
  std::vector<RegisterEveryNSamplesEventResponse> event_responses;
  std::vector<ReadAnalogF64Response> read_responses;
  std::unique_ptr<::grpc::ClientContext> read_context;
  std::unique_ptr<::grpc::ClientAsyncResponseReader<ReadAnalogF64Response>> read_reader;
  ReadAnalogF64Response read_response;
  ::grpc::Status read_status;
  while (read_responses.size() < N_READS) {
    auto completion = get_next_completion(completion_queue);
    if (get_completion_tag(completion) == EVENT_READ_TAG) {
      ASSERT_TRUE(is_completion_ok(completion));
      event_responses.push_back(event_response);
      if (event_responses.size() < N_READS) {
        event_reader->Read(&event_response, EVENT_READ_TAG);
      }
      // Start a new read, unless the previous read hasn't completed yet.
      if (read_responses.size() < N_READS && !read_context) {
        read_context = std::make_unique<::grpc::ClientContext>();
        read_reader = async_read_analog_f64(
          *read_context, completion_queue, READ_ANALOG_F64_TAG, N_SAMPLES, N_SAMPLES,
          read_response, read_status);
      }
    }
    else if (get_completion_tag(completion) == READ_ANALOG_F64_TAG) {
      ASSERT_TRUE(is_completion_ok(completion));
      client::raise_if_error(read_status, *read_context);
      read_responses.push_back(read_response);
      read_reader.reset();
      read_context.reset();
      // If reads can't keep up with events, do back-to-back reads.
      if (read_responses.size() < N_READS && read_responses.size() < event_responses.size()) {
        read_context = std::make_unique<::grpc::ClientContext>();
        read_reader = async_read_analog_f64(
          *read_context, completion_queue, READ_ANALOG_F64_TAG, N_SAMPLES, N_SAMPLES,
          read_response, read_status);
      }
    }
    else {
      FAIL() << "Unexpected completion: " << PrintToString(completion);
    }
  }

  EXPECT_THAT(event_responses, SizeIs(N_READS));
  EXPECT_THAT(event_responses, Each(Property(&RegisterEveryNSamplesEventResponse::n_samples, Eq(N_SAMPLES))));
  EXPECT_THAT(event_responses, Each(Property(&RegisterEveryNSamplesEventResponse::status, Eq(DAQMX_SUCCESS))));
  EXPECT_THAT(read_responses, SizeIs(N_READS));
  EXPECT_THAT(read_responses, Each(Property(&ReadAnalogF64Response::read_array, SizeIs(N_SAMPLES))));
  EXPECT_THAT(read_responses, Each(Property(&ReadAnalogF64Response::samps_per_chan_read, Eq(N_SAMPLES))));
  EXPECT_THAT(read_responses, Each(Property(&ReadAnalogF64Response::status, Eq(DAQMX_SUCCESS))));
}

// This test uses the async API in order to check whether the event stream is closed without blocking.
TEST_F(NiDAQmxDriverApiTests, AsyncEveryNSamplesEventRegisteredWithWrongEventTypeAndWaitForMetadata_ReadStreamWithoutBlocking_ReadCompletesImmediatelyWithError)
{
  const auto N_SAMPLES = 10UL;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_INITIAL_METADATA_TAG = (void*)2;
  const auto READ_TAG = (void*)3;
  const auto FINISH_TAG = (void*)4;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)
  ::grpc::ClientContext reader_context;
  ::grpc::CompletionQueue completion_queue;
  auto shut_down_on_exit = make_scope_exit([&]{ shut_down_completion_queue(completion_queue); });
  auto reader = async_register_every_n_samples_event(
    reader_context, completion_queue, START_CALL_TAG, N_SAMPLES,
    EveryNSamplesEventType::EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER);
  async_wait_for_initial_metadata(reader_context, *reader, completion_queue, START_CALL_TAG, READ_INITIAL_METADATA_TAG);

  RegisterEveryNSamplesEventResponse response;
  reader->Read(&response, READ_TAG);
  Completion read_completion;
  bool read_completed = try_get_next_completion_without_blocking(completion_queue, read_completion);

  EXPECT_TRUE(read_completed);
  EXPECT_EQ(Completion(READ_TAG, false), read_completion);  // read_completion should NOT be OK
  ::grpc::Status status;
  reader->Finish(&status, FINISH_TAG);
  Completion finish_completion;
  bool finish_completed = try_get_next_completion_without_blocking(completion_queue, finish_completion);
  EXPECT_TRUE(finish_completed);
  ASSERT_EQ(Completion(FINISH_TAG, true), finish_completion);
  EXPECT_THROW_DRIVER_ERROR({
    client::raise_if_error(status, reader_context);
  }, EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, Channel_AsyncRegisterUnregisterDoneEventMultipleTimes_NoErrors)
{
  const auto N_ITERATIONS = 10UL;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_INITIAL_METADATA_TAG = (void*)2;
  const auto READ_TAG = (void*)3;
  const auto FINISH_TAG = (void*)4;
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::CompletionQueue completion_queue;
  auto shut_down_on_exit = make_scope_exit([&]{ shut_down_completion_queue(completion_queue); });

  for (auto i = 0UL; i < N_ITERATIONS; ++i) {
    ::grpc::ClientContext reader_context;
    auto reader = async_register_done_event(reader_context, completion_queue, START_CALL_TAG);
    auto cancel_on_exit = make_scope_exit([&]{ async_cancel_stream(reader_context, *reader, completion_queue, FINISH_TAG); });
    async_wait_for_initial_metadata(reader_context, *reader, completion_queue, START_CALL_TAG, READ_INITIAL_METADATA_TAG);
    RegisterDoneEventResponse response;
    async_begin_read_stream(reader_context, *reader, completion_queue, READ_TAG, FINISH_TAG, response); // check for errors
    unregister_done_event(); // does not close/cancel stream
  }
}

TEST_F(NiDAQmxDriverApiTests, Channel_AsyncRegisterUnregisterEveryNSamplesEventMultipleTimes_NoErrors)
{
  const auto N_ITERATIONS = 10UL;
  const auto N_SAMPLES = 10UL;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_INITIAL_METADATA_TAG = (void*)2;
  const auto READ_TAG = (void*)3;
  const auto FINISH_TAG = (void*)4;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)
  ::grpc::CompletionQueue completion_queue;
  auto shut_down_on_exit = make_scope_exit([&]{ shut_down_completion_queue(completion_queue); });

  for (auto i = 0UL; i < N_ITERATIONS; ++i) {
    ::grpc::ClientContext reader_context;
    auto reader = async_register_every_n_samples_event(reader_context, completion_queue, START_CALL_TAG, N_SAMPLES);
    auto cancel_on_exit = make_scope_exit([&]{ async_cancel_stream(reader_context, *reader, completion_queue, FINISH_TAG); });
    async_wait_for_initial_metadata(reader_context, *reader, completion_queue, START_CALL_TAG, READ_INITIAL_METADATA_TAG);
    RegisterEveryNSamplesEventResponse response;
    async_begin_read_stream(reader_context, *reader, completion_queue, READ_TAG, FINISH_TAG, response); // check for errors
    unregister_every_n_samples_event(); // does not close/cancel stream
  }
}

TEST_F(NiDAQmxDriverApiTests, Channel_AsyncRegisterUnregisterSignalEventMultipleTimes_NoErrors)
{
  const auto N_ITERATIONS = 10UL;
  const auto START_CALL_TAG = (void*)1;
  const auto READ_INITIAL_METADATA_TAG = (void*)2;
  const auto READ_TAG = (void*)3;
  const auto FINISH_TAG = (void*)4;
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::CompletionQueue completion_queue;
  auto shut_down_on_exit = make_scope_exit([&]{ shut_down_completion_queue(completion_queue); });

  for (auto i = 0UL; i < N_ITERATIONS; ++i) {
    ::grpc::ClientContext reader_context;
    auto reader = async_register_signal_event(reader_context, completion_queue, START_CALL_TAG, Signal2::SIGNAL2_SAMPLE_COMPLETE_EVENT);
    auto cancel_on_exit = make_scope_exit([&]{ async_cancel_stream(reader_context, *reader, completion_queue, FINISH_TAG); });
    async_wait_for_initial_metadata(reader_context, *reader, completion_queue, START_CALL_TAG, READ_INITIAL_METADATA_TAG);
    RegisterSignalEventResponse response;
    async_begin_read_stream(reader_context, *reader, completion_queue, READ_TAG, FINISH_TAG, response); // check for errors
    unregister_signal_event(Signal2::SIGNAL2_SAMPLE_COMPLETE_EVENT); // does not close/cancel stream
  }
}

TEST_F(NiDAQmxDriverApiTests, DoneEventRegisteredAndTaskRunning_UnregisterDoneEvent_CannotUnregisterErrorReceived)
{
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::ClientContext reader_context;
  auto reader = register_done_event(reader_context);
  reader->WaitForInitialMetadata();
  start_task();

  EXPECT_THROW_DRIVER_ERROR({
    unregister_done_event();
  }, CANNOT_UNREGISTER_DAQMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventRegisteredAndTaskRunning_UnregisterEveryNSamplesEvent_CannotUnregisterErrorReceived)
{
  auto N_SAMPLES = 10UL;
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)
  ::grpc::ClientContext reader_context;
  auto reader = register_every_n_samples_event(reader_context, N_SAMPLES);
  reader->WaitForInitialMetadata();
  start_task();

  EXPECT_THROW_DRIVER_ERROR({
    unregister_every_n_samples_event();
  }, CANNOT_UNREGISTER_DAQMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, SignalEventRegisteredAndTaskRunning_UnregisterSignalEvent_CannotUnregisterErrorReceived)
{
  create_ai_voltage_chan(0.0, 1.0);
  ::grpc::ClientContext reader_context;
  auto reader = register_signal_event(reader_context, Signal2::SIGNAL2_SAMPLE_COMPLETE_EVENT);
  reader->WaitForInitialMetadata();
  start_task();

  EXPECT_THROW_DRIVER_ERROR({
    unregister_signal_event(Signal2::SIGNAL2_SAMPLE_COMPLETE_EVENT);
  }, CANNOT_UNREGISTER_DAQMX_SOFTWARE_EVENT_WHILE_TASK_IS_RUNNING_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, DoneEventNotRegistered_UnregisterDoneEvent_NoError)
{
  create_ai_voltage_chan(0.0, 1.0);

  unregister_done_event();
}

TEST_F(NiDAQmxDriverApiTests, EveryNSamplesEventNotRegistered_UnregisterEveryNSamplesEvent_NoError)
{
  create_ai_voltage_chan(0.0, 1.0);
  cfg_samp_clk_timing(); // Every N Samples requires a buffered task (validated in start_task)

  unregister_every_n_samples_event();
}

TEST_F(NiDAQmxDriverApiTests, SignalEventNotRegistered_UnregisterSignalEvent_NoError)
{
  create_ai_voltage_chan(0.0, 1.0);

  unregister_signal_event(Signal2::SIGNAL2_SAMPLE_COMPLETE_EVENT);
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_ConfigureInputBuffer_Succeeds)
{
  create_ai_voltage_chan(0.0, 1.0);

  CfgInputBufferResponse response;
  auto status = cfg_input_buffer(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, AOVoltageChannel_ConfigureOutputBuffer_Succeeds)
{
  create_ao_voltage_chan(0.0, 1.0);

  CfgOutputBufferResponse response;
  auto status = cfg_output_buffer(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, SelfTestDevice_Succeeds)
{
  SelfTestDeviceResponse response;
  auto status = self_test_device(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, CalculateReversePolyCoefficientsWithNegativeOneReverseOrder_ReturnsCoefficientsSizedToForwardCoefficients)
{
  auto const FORWARD_COEFFICIENTS = std::vector<double>{1.0, 3.0, 8.0};
  auto const REVERSE_ORDER = -1;
  auto request = create_calculate_reverse_poly_coeff_request(
      FORWARD_COEFFICIENTS,
      0.0,
      10.0,
      100,
      REVERSE_ORDER);
  auto response = CalculateReversePolyCoeffResponse{};
  auto status = calculate_reverse_poly_coeff(request, response);

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(FORWARD_COEFFICIENTS.size(), response.reverse_coeffs().size());
}

TEST_F(NiDAQmxDriverApiTests, CalculateReversePolyCoefficientsWithPositiveReverseOrder_ReturnsCoefficientsSizedToReverseOrderPlusOne)
{
  auto const REVERSE_ORDER = 10;
  auto request = create_calculate_reverse_poly_coeff_request(
      {1.0, 3.0, 8.0},
      0.0,
      10.0,
      100,
      REVERSE_ORDER);
  auto response = CalculateReversePolyCoeffResponse{};
  auto status = calculate_reverse_poly_coeff(request, response);

  EXPECT_SUCCESS(status, response);
  EXPECT_EQ(REVERSE_ORDER + 1, response.reverse_coeffs().size());
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_WaitForValidTimestamp_ReturnsError)
{
  create_ai_voltage_chan(0.0, 1.0);

  EXPECT_THROW_DRIVER_ERROR({
    auto response = WaitForValidTimestampResponse{};
    auto status = wait_for_valid_timestamp(response);
  }, WAIT_FOR_VALID_TIMESTAMP_NOT_SUPPORTED_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, AIVoltageChannel_CfgTimeStartTrig_ReturnsError)
{
  create_ai_voltage_chan(0.0, 1.0);

  EXPECT_THROW_DRIVER_ERROR({
    auto response = CfgTimeStartTrigResponse{};
    cfg_time_start_trig(response);
  }, INVALID_ATTRIBUTE_VALUE_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, LoadedVoltageTask_ReadAIData_ReturnsDataInExpectedRange)
{
  const auto AI_MIN = 0.0;
  const auto AI_MAX = 1.0;
  const auto NUM_SAMPS = 10;
  const auto TIMEOUT = 10.0;
  create_ai_voltage_chan(AI_MIN, AI_MAX);
  auto save_response = SaveTaskResponse{};
  auto status = save_task(save_response);
  EXPECT_SUCCESS(status, save_response);
  clear_task();
  auto load_response = LoadTaskResponse{};
  status = load_task(load_response); // cleaned up by test fixture
  EXPECT_SUCCESS(status, load_response);

  auto read_response = ReadAnalogF64Response{};
  status = read_analog_f64(NUM_SAMPS, NUM_SAMPS, TIMEOUT, read_response);

  EXPECT_SUCCESS(status, read_response);
  EXPECT_DATA_IN_RANGE(read_response.read_array(), AI_MIN, AI_MAX);
}

TEST_F(NiDAQmxDriverApiTests, UnsupportedChannelType_BridgeOffsetNullingCal_ReturnsError)
{
  const auto AI_MIN = 0.0;
  const auto AI_MAX = 1.0;
  create_ai_voltage_chan(AI_MIN, AI_MAX);

  std::string channel = "";
  bool skip_unsupported_channels = false;
  EXPECT_THROW_DRIVER_ERROR({
    auto response = PerformBridgeOffsetNullingCalExResponse{};
    auto status = perform_bridge_offset_nulling_cal_ex(channel, skip_unsupported_channels, response);
  }, BRIDGE_OFFSET_NULLING_CAL_NOT_SUPPORTED_ERROR);
}

// AI Voltage Channel doesn't support Bridge Shunt Calibration
TEST_F(NiDAQmxDriverApiTests, UnsupportedChannelType_PerformBridgeShuntCalEx_ReturnsError)
{
  const auto AI_MIN = -5;
  const auto AI_MAX = 5;
  create_ai_voltage_chan(AI_MIN, AI_MAX);

  EXPECT_THROW_DRIVER_ERROR({
    auto response = PerformBridgeShuntCalExResponse{};
    auto status = perform_bridge_shunt_cal_ex(response);
  }, BRIDGE_SHUNT_CAL_NOT_SUPPORTED_ERROR);
}

// X Series doesn't support Strain Shunt Calibration
TEST_F(NiDAQmxDriverApiTests, UnsupportedDevice_PerformStrainShuntCalEx_ReturnsError)
{
  const auto AI_MIN = -0.001;
  const auto AI_MAX = 0.001;
  create_ai_strain_gage_chan(AI_MIN, AI_MAX);

  EXPECT_THROW_DRIVER_ERROR({
    auto response = PerformStrainShuntCalExResponse{};
    auto status = perform_strain_shunt_cal_ex(response);
  }, STRAIN_SHUNT_CAL_NOT_SUPPORTED_ERROR);
}

// X Series doesn't support thermocouple offset nulling
TEST_F(NiDAQmxDriverApiTests, UnsupportedDevice_ThrmcplLeadOffsetNullingCal_ReturnsError)
{
  const auto AI_MIN = 0.0;
  const auto AI_MAX = 100.0;
  create_ai_thrmcpl_chan(AI_MIN, AI_MAX);

  std::string channel = "";
  bool skip_unsupported_channels = false;
  EXPECT_THROW_DRIVER_ERROR({
    auto response = PerformThrmcplLeadOffsetNullingCalResponse{};
    auto status = perform_thrmcpl_lead_offset_nulling_cal(channel, skip_unsupported_channels, response);
  }, THRMCPL_LEAD_OFFSET_NULLING_CAL_NOT_SUPPORTED_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, SelfCal_Succeeds)
{
  auto response = SelfCalResponse{};
  auto status = self_cal(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, AddNetworkDeviceWithInvalidIP_ErrorRetrievingNetworkDeviceProperties)
{
  EXPECT_THROW_DRIVER_ERROR({
    auto response = AddNetworkDeviceResponse{};
    add_network_device("0.0.0.0", response);
  }, RETRIEVING_NETWORK_DEVICE_PROPERTIES_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, ConfigureTEDSOnNonTEDSChannel_ErrorTEDSSensorNotDetected)
{
  EXPECT_THROW_DRIVER_ERROR({
    client::configure_teds(stub(), AI_CHANNEL, "");
  }, TEDS_SENSOR_NOT_DETECTED_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, HardwareTimedTask_WaitForNextSampleClock_Succeeds)
{
  create_ao_voltage_chan(0.0, 10.0);
  auto cfg_response = client::cfg_samp_clk_timing(
      stub(),
      task(),
      "",
      100.0,
      Edge1::EDGE1_RISING,
      AcquisitionType::ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT,
      1);
  EXPECT_SUCCESS(cfg_response);

  start_task();
  auto response = WaitForNextSampleClockResponse{};
  auto status = wait_for_next_sample_clock(response);

  EXPECT_SUCCESS(status, response);
}

TEST_F(NiDAQmxDriverApiTests, ConnectBogusTerms_FailsWithInvalidRoutingError)
{
  EXPECT_THROW_DRIVER_ERROR({
    auto response = ConnectTermsResponse{};
    connect_terms("ABC", "123", response);
  }, INVALID_TERM_ROUTING_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, DOWatchdogTask_StartTaskAndWatchdogTask_Succeeds)
{
  // Note: the DO chan will be the default task in this test.
  // The watchdog task is a separate task passed around through create_watchdog_response.
  create_do_chan();
  auto create_watchdog_response = CreateWatchdogTimerTaskExResponse{};
  auto create_status = create_watchdog_timer_task_ex(.001, create_watchdog_response);
  auto watchdog_task = create_watchdog_response.task();
  auto clear_watchdog_task_on_exit = make_scope_exit([&]{ clear_task(watchdog_task); });
  auto cfg_watchdog_response = CfgWatchdogDOExpirStatesResponse{};
  auto cfg_status = cfg_watchdog_do_expir_states(
      watchdog_task,
      cfg_watchdog_response);
  EXPECT_SUCCESS(create_status, create_watchdog_response);
  EXPECT_SUCCESS(cfg_status, cfg_watchdog_response);

  start_task();
  auto start_watchdog_response = StartTaskResponse{};
  auto start_watchdog_status = start_task(
      watchdog_task,
      start_watchdog_response);

  EXPECT_SUCCESS(start_watchdog_status, start_watchdog_response);
}

TEST_F(NiDAQmxDriverApiTests, AutoConfigureCDAQSyncConnections_ReturnsNotSupportedError)
{
  EXPECT_THROW_DRIVER_ERROR({
    client::auto_configure_cdaq_sync_connections(stub(), DEVICE_NAME, 1.0);
  }, DEVICE_DOES_NOT_SUPPORT_CDAQ_SYNC_CONNECTIONS_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, DIChannel_GetSetResetInputBufferSize_UpdatesBufferSize)
{
  create_di_chan();
  auto ATTRIBUTE = BufferUInt32Attribute::BUFFER_ATTRIBUTE_INPUT_BUF_SIZE;

  auto get_response = client::get_buffer_attribute_uint32(
      stub(),
      task(),
      ATTRIBUTE);
  auto initial_value = get_response.value();
  auto set_response = client::set_buffer_attribute_uint32(
      stub(),
      task(),
      ATTRIBUTE,
      initial_value * 2);
  auto readback_response = client::get_buffer_attribute_uint32(
      stub(),
      task(),
      ATTRIBUTE);
  auto reset_response = client::reset_buffer_attribute(
      stub(),
      task(),
      BufferResetAttribute::BUFFER_RESET_ATTRIBUTE_INPUT_BUF_SIZE);
  auto read_after_reset_response = client::get_buffer_attribute_uint32(
      stub(),
      task(),
      ATTRIBUTE);

  EXPECT_SUCCESS(get_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(readback_response);
  EXPECT_SUCCESS(reset_response);
  EXPECT_SUCCESS(read_after_reset_response);
  EXPECT_EQ(initial_value, read_after_reset_response.value());
  EXPECT_EQ(initial_value * 2, readback_response.value());
}

TEST_F(NiDAQmxDriverApiTests, GetAISupportMeasurementTypes_ResultIncludesCurrentAndVoltage)
{
  const auto ATTRIBUTE = DeviceInt32ArrayAttribute::DEVICE_ATTRIBUTE_AI_SUPPORTED_MEAS_TYPES;
  auto response = client::get_device_attribute_int32_array(stub(), DEVICE_NAME, ATTRIBUTE);

  EXPECT_SUCCESS(response);
  EXPECT_THAT(response.value(), Contains(DeviceInt32AttributeValues::DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT));
  EXPECT_THAT(response.value(), Contains(DeviceInt32AttributeValues::DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE));
  EXPECT_THAT(response.value_raw(), Contains(DeviceInt32AttributeValues::DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT));
  EXPECT_THAT(response.value_raw(), Contains(DeviceInt32AttributeValues::DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE));
}

TEST_F(NiDAQmxDriverApiTests, AOChannel_GetAOMax_ReturnsAOMax)
{
  const auto A0_MIN = -10.0;
  const auto AO_MAX = 10.0;
  const auto CHANNEL_NAME = "AO Channel";
  create_ao_voltage_chan(
      create_ao_voltage_chan_request(A0_MIN, AO_MAX, CHANNEL_NAME));

  auto response = client::get_chan_attribute_double(
      stub(),
      task(),
      CHANNEL_NAME,
      ChannelDoubleAttribute::CHANNEL_ATTRIBUTE_AO_MAX);

  EXPECT_SUCCESS(response);
  EXPECT_NEAR(AO_MAX, response.value(), 0.0001);
}

TEST_F(NiDAQmxDriverApiTests, AOChannel_SetAndGetAllowConnToGround_SucceedsAndReturnsSetValue)
{
  const auto CHANNEL_NAME = "AO Channel";
  create_ao_voltage_chan(
      create_ao_voltage_chan_request(-1.0, 1.0, CHANNEL_NAME));

  auto initial_get_response = client::get_chan_attribute_bool(
      stub(),
      task(),
      CHANNEL_NAME,
      ChannelBoolAttribute::CHANNEL_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND);
  auto set_response = client::set_chan_attribute_bool(
      stub(),
      task(),
      CHANNEL_NAME,
      ChannelBoolAttribute::CHANNEL_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND,
      true);
  auto get_response = client::get_chan_attribute_bool(
      stub(),
      task(),
      CHANNEL_NAME,
      ChannelBoolAttribute::CHANNEL_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND);

  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(get_response);
  EXPECT_FALSE(initial_get_response.value());
  EXPECT_TRUE(get_response.value());
}

TEST_F(NiDAQmxDriverApiTests, AOChannel_GetAOOutputType_SucceedsAndReturnsVoltage)
{
  const auto CHANNEL_NAME = "AO Channel";
  create_ao_voltage_chan(
      create_ao_voltage_chan_request(-1.0, 1.0, CHANNEL_NAME));

  auto response = client::get_chan_attribute_int32(
      stub(),
      task(),
      CHANNEL_NAME,
      ChannelInt32Attribute::CHANNEL_ATTRIBUTE_AO_OUTPUT_TYPE);

  EXPECT_SUCCESS(response);
  EXPECT_EQ(
      ChannelInt32AttributeValues::CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE,
      response.value());
}

TEST_F(NiDAQmxDriverApiTests, TaskWithChannel_GetTaskAttributes_ReturnsCorrectResults)
{
  const auto CHANNEL_NAME = "AO Channel";
  create_ao_voltage_chan(
      create_ao_voltage_chan_request(-1.0, 1.0, CHANNEL_NAME));
  start_task();

  auto num_chans_response = client::get_task_attribute_uint32(stub(), task(), TaskUInt32Attribute::TASK_ATTRIBUTE_NUM_CHANS);
  auto channels_response = client::get_task_attribute_string(stub(), task(), TaskStringAttribute::TASK_ATTRIBUTE_CHANNELS);
  auto complete_response = client::get_task_attribute_bool(stub(), task(), TaskBoolAttribute::TASK_ATTRIBUTE_COMPLETE);

  EXPECT_SUCCESS(num_chans_response);
  EXPECT_SUCCESS(channels_response);
  EXPECT_SUCCESS(complete_response);
  EXPECT_EQ(1, num_chans_response.value());
  EXPECT_EQ(CHANNEL_NAME, channels_response.value());
  EXPECT_FALSE(complete_response.value());
}

TEST_F(NiDAQmxDriverApiTests, AIChannelWithSampleClock_ReconfigureRate_UpdatesRateSuccessfully)
{
  const auto INITIAL_RATE = 100.0;
  const auto RECONFIGURED_RATE = 200.0;
  create_ai_voltage_chan(0.0, 10.0);
  auto cfg_request = create_cfg_samp_clk_timing_request(INITIAL_RATE, Edge1::EDGE1_RISING, AcquisitionType::ACQUISITION_TYPE_CONT_SAMPS, 1U);
  cfg_samp_clk_timing(cfg_request);

  auto initial_response = client::get_timing_attribute_double(stub(), task(), TimingDoubleAttribute::TIMING_ATTRIBUTE_SAMP_CLK_RATE);
  auto set_response = client::set_timing_attribute_double(stub(), task(), TimingDoubleAttribute::TIMING_ATTRIBUTE_SAMP_CLK_RATE, RECONFIGURED_RATE);
  auto get_response = client::get_timing_attribute_double(stub(), task(), TimingDoubleAttribute::TIMING_ATTRIBUTE_SAMP_CLK_RATE);

  EXPECT_SUCCESS(initial_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(get_response);
  EXPECT_NEAR(INITIAL_RATE, initial_response.value(), .0001);
  EXPECT_NEAR(RECONFIGURED_RATE, get_response.value(), .0001);
}

TEST_F(NiDAQmxDriverApiTests, AIChannel_ReconfigureOverwrite_UpdatesOverwriteSuccessfully)
{
  const auto NEW_VALUE = ReadInt32AttributeValues::READ_INT32_OVERWRITE_MODE1_OVERWRITE_UNREAD_SAMPS;
  create_ai_voltage_chan(-5.0, 5.0);

  auto initial_response = client::get_read_attribute_int32(stub(), task(), ReadInt32Attribute::READ_ATTRIBUTE_OVERWRITE);
  auto set_response = client::set_read_attribute_int32(stub(), task(), ReadInt32Attribute::READ_ATTRIBUTE_OVERWRITE, NEW_VALUE);
  auto get_response = client::get_read_attribute_int32(stub(), task(), ReadInt32Attribute::READ_ATTRIBUTE_OVERWRITE);

  EXPECT_SUCCESS(initial_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(get_response);
  EXPECT_EQ(NEW_VALUE, get_response.value());
  EXPECT_NE(get_response.value(), initial_response.value());
}

TEST_F(NiDAQmxDriverApiTests, AOChannel_ReconfigureSleepTime_UpdatesSleepTimeSuccessfully)
{
  const auto NEW_VALUE = 100.0;
  create_ao_voltage_chan(-10.0, 10.0);

  auto initial_response = client::get_write_attribute_double(stub(), task(), WriteDoubleAttribute::WRITE_ATTRIBUTE_SLEEP_TIME);
  auto set_response = client::set_write_attribute_double(stub(), task(), WriteDoubleAttribute::WRITE_ATTRIBUTE_SLEEP_TIME, NEW_VALUE);
  auto get_response = client::get_write_attribute_double(stub(), task(), WriteDoubleAttribute::WRITE_ATTRIBUTE_SLEEP_TIME);

  EXPECT_SUCCESS(initial_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(get_response);
  EXPECT_NEAR(NEW_VALUE, get_response.value(), .0001);
  EXPECT_NE(get_response.value(), initial_response.value());
}

TEST_F(NiDAQmxDriverApiTests, AIChannel_ReconfigureSampQuantSampsPerChan_UpdatesSampQuantSampsPerChanSuccessfully)
{
  const auto SAMPS_PER_CHAN_ATTRIBUTE = TimingUInt64Attribute::TIMING_ATTRIBUTE_SAMP_QUANT_SAMP_PER_CHAN;
  const auto RECONFIGURED_SAMPS_PER_CHAN = 2000ULL;
  create_ai_voltage_chan(-10.0, 10.0);

  auto initial_response = client::get_timing_attribute_uint64(
      stub(),
      task(),
      SAMPS_PER_CHAN_ATTRIBUTE);
  auto set_response = client::set_timing_attribute_uint64(
      stub(),
      task(),
      SAMPS_PER_CHAN_ATTRIBUTE,
      RECONFIGURED_SAMPS_PER_CHAN);
  auto get_response = client::get_timing_attribute_uint64(
      stub(),
      task(),
      SAMPS_PER_CHAN_ATTRIBUTE);

  EXPECT_SUCCESS(initial_response);
  EXPECT_SUCCESS(set_response);
  EXPECT_SUCCESS(get_response);
  EXPECT_EQ(1000ULL, initial_response.value());
  EXPECT_EQ(RECONFIGURED_SAMPS_PER_CHAN, get_response.value());
}

TEST_F(NiDAQmxDriverApiTests, SetWrongCategoryAttribute_ReturnsNotValidError)
{
  EXPECT_THROW_DRIVER_ERROR({
    client::get_device_attribute_bool(stub(), DEVICE_NAME, ScaleDoubleAttribute::SCALE_ATTRIBUTE_LIN_SLOPE);
  }, SPECIFIED_ATTRIBUTE_NOT_VALID_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, SetWrongDataTypeAttribute_ReturnsNotValidError)
{
  EXPECT_THROW_DRIVER_ERROR({
    client::get_device_attribute_bool(stub(), DEVICE_NAME, DeviceStringAttribute::DEVICE_ATTRIBUTE_AO_PHYSICAL_CHANS);
  }, SPECIFIED_ATTRIBUTE_NOT_VALID_ERROR);
}

TEST_F(NiDAQmxDriverApiTests, GetReadAttributeUInt32_DAQmxDefaultNumberOfSamplesToRead_RawAttribute_Succeeds)
{
  CreateAIVoltageChanResponse channel_response;
  auto channel_status = create_ai_voltage_chan(-10.0, 10.0, channel_response);
  
  auto response = client::get_read_attribute_uint32(stub(), task(), DAQmx_DefaultNumberOfSamplesToRead);
  
  EXPECT_SUCCESS(channel_status, channel_response);  
  EXPECT_SUCCESS(response);
  EXPECT_EQ(response.value(), 1);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidaqmx_session_tests.cpp sha256=7aa35dd0ab6e31aad5d92341e773cfbabdb9b122b540f44d06673fde0be90c5c bytes=1857 -->
## FILE: source/tests/system/nidaqmx_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidaqmx_session_tests.cpp`
- sha256: `7aa35dd0ab6e31aad5d92341e773cfbabdb9b122b540f44d06673fde0be90c5c`
- bytes: 1857

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nidaqmx/nidaqmx_client.h"

using namespace nidaqmx_grpc;

namespace ni {
namespace tests {
namespace system {

constexpr auto DAQMX_SUCCESS = 0;

class NiDAQmxSessionTests : public ::testing::Test {
 protected:
  NiDAQmxSessionTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nidaqmx_stub_(NiDAQmx::NewStub(device_server_->InProcessChannel()))
  {
  }
  virtual ~NiDAQmxSessionTests() {}

  ::grpc::Status create_task(const std::string& name, CreateTaskResponse& response)
  {
    ::grpc::ClientContext context;
    CreateTaskRequest request;
    request.set_session_name(name);
    return stub()->CreateTask(&context, request, &response);
  }

  ::grpc::Status clear_task(const std::string& name, ClearTaskResponse& response)
  {
    ::grpc::ClientContext context;
    ClearTaskRequest request;
    if (!name.empty()) {
      request.mutable_task()->set_name(name);
    }
    return stub()->ClearTask(&context, request, &response);
  }

  std::unique_ptr<NiDAQmx::Stub>& stub()
  {
    return nidaqmx_stub_;
  }
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiDAQmx::Stub> nidaqmx_stub_;
};

TEST_F(NiDAQmxSessionTests, CreateTask_ClearTask_Succeeds)
{
  CreateTaskResponse create_response;
  auto create_status = create_task("", create_response);
  auto task_name = create_response.task().name();

  ClearTaskResponse clear_response;
  auto clear_status = clear_task(task_name, clear_response);

  EXPECT_TRUE(create_status.ok());
  EXPECT_TRUE(clear_status.ok());
  EXPECT_EQ(DAQMX_SUCCESS, create_response.status());
  EXPECT_EQ(DAQMX_SUCCESS, clear_response.status());
  EXPECT_NE("", create_response.task().name());
}
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidcpower_driver_api_tests.cpp sha256=fef5f6687f1555685963dcbfd9866d5d1faf7eb32db3e6a206da2789a56491c0 bytes=23166 -->
## FILE: source/tests/system/nidcpower_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidcpower_driver_api_tests.cpp`
- sha256: `fef5f6687f1555685963dcbfd9866d5d1faf7eb32db3e6a206da2789a56491c0`
- bytes: 23166

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nidcpower/nidcpower_client.h"

namespace ni {
namespace tests {
namespace system {

namespace dcpower = nidcpower_grpc;
namespace client = nidcpower_grpc::experimental::client;
namespace pb = ::google::protobuf;

typedef pb::int32 int32;
typedef pb::int64 int64;
typedef pb::uint32 uint32;
typedef pb::uint16 uint16;

const int kdcpowerDriverApiSuccess = 0;

class NiDCPowerDriverApiTest : public ::testing::Test {
 protected:
  NiDCPowerDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidcpower_stub_(dcpower::NiDCPower::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDCPowerDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<dcpower::NiDCPower::Stub>& GetStub()
  {
    return nidcpower_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  void initialize_driver_session()
  {
    const auto DEVICE = "FakeDevice";
    const auto OPTIONS = "Simulate=1, DriverSetup=Model:4147; BoardType:PXIe";
    try {
      auto independent_response = client::initialize_with_independent_channels(
          GetStub(),
          DEVICE,
          false,
          OPTIONS,
          nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW);

      ASSERT_EQ(kdcpowerDriverApiSuccess, independent_response.status());
      driver_session_ = std::make_unique<nidevice_grpc::Session>(independent_response.vi());
    }
    catch (std::runtime_error&) {
      auto legacy_response = client::initialize_with_channels(
          GetStub(),
          DEVICE,
          "0",
          false,
          OPTIONS,
          nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_INITIALIZE_NEW);

      ASSERT_EQ(kdcpowerDriverApiSuccess, legacy_response.status());
      driver_session_ = std::make_unique<nidevice_grpc::Session>(legacy_response.vi());
      is_legacy_session_ = true;
    }
  }

  bool is_legacy_session()
  {
    return is_legacy_session_;
  }

  void initiate()
  {
    dcpower::InitiateRequest request;
    dcpower::InitiateResponse response;
    ::grpc::ClientContext context;
    request.mutable_vi()->set_name(GetSessionName());

    ::grpc::Status status = GetStub()->Initiate(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void close_driver_session()
  {
    ::grpc::ClientContext context;
    dcpower::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    dcpower::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void measure_multiple(const char* channel_name, nidcpower_grpc::MeasureMultipleResponse* response)
  {
    ::grpc::ClientContext context;
    dcpower::MeasureMultipleRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);

    ::grpc::Status status = GetStub()->MeasureMultiple(&context, request, response);

    EXPECT_TRUE(status.ok());
  }

  bool get_bool_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dcpower::GetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    dcpower::GetAttributeViBooleanResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViBoolean(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response.attribute_value();
  }

  int32 get_int32_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dcpower::GetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    dcpower::GetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt32(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response.attribute_value();
  }

  int64 get_int64_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dcpower::GetAttributeViInt64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    dcpower::GetAttributeViInt64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response.attribute_value();
  }

  double get_real64_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dcpower::GetAttributeViReal64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    dcpower::GetAttributeViReal64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response.attribute_value();
  }

  std::string get_string_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dcpower::GetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    dcpower::GetAttributeViStringResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViString(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response.attribute_value();
  }

  void set_int32_attribute(const char* channel_list, dcpower::NiDCPowerAttribute attribute_id, dcpower::NiDCPowerInt32AttributeValues attribute_value)
  {
    ::grpc::ClientContext context;
    const dcpower::NiDCPowerAttribute attribute_to_set = attribute_id;
    dcpower::SetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_to_set);
    request.set_attribute_value(attribute_value);
    dcpower::SetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void configure_output_function(const char* channel_name, dcpower::OutputFunction function)
  {
    ::grpc::ClientContext context;
    dcpower::ConfigureOutputFunctionRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_function(function);
    dcpower::ConfigureOutputFunctionResponse response;

    ::grpc::Status status = GetStub()->ConfigureOutputFunction(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void configure_voltage_level(const char* channel_name, double level)
  {
    ::grpc::ClientContext context;
    dcpower::ConfigureVoltageLevelRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_level(level);
    dcpower::ConfigureVoltageLevelResponse response;

    ::grpc::Status status = GetStub()->ConfigureVoltageLevel(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void configure_current_level(const char* channel_name, double level)
  {
    ::grpc::ClientContext context;
    dcpower::ConfigureCurrentLevelRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_level(level);
    dcpower::ConfigureCurrentLevelResponse response;

    ::grpc::Status status = GetStub()->ConfigureCurrentLevel(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  dcpower::ExportAttributeConfigurationBufferResponse export_attribute_configuration_buffer()
  {
    ::grpc::ClientContext context;
    dcpower::ExportAttributeConfigurationBufferRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    dcpower::ExportAttributeConfigurationBufferResponse response;

    ::grpc::Status status = GetStub()->ExportAttributeConfigurationBuffer(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
    return response;
  }

  void reset_with_channels(const char* channel_name)
  {
    ::grpc::ClientContext context;
    dcpower::ResetWithChannelsRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    dcpower::ResetWithChannelsResponse response;

    ::grpc::Status status = GetStub()->ResetWithChannels(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  }

  void fetch_multiple(const char* channel_name, nidcpower_grpc::FetchMultipleResponse* response)
  {
    ::grpc::ClientContext context;
    dcpower::FetchMultipleRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_timeout(5);
    request.set_count(20);

    ::grpc::Status status = GetStub()->FetchMultiple(&context, request, response);

    EXPECT_TRUE(status.ok());
  }

  void import_attribute_configuration_buffer(dcpower::ExportAttributeConfigurationBufferResponse export_buffer_response)
  {
    ::grpc::ClientContext context;
    dcpower::ImportAttributeConfigurationBufferRequest import_request;
    import_request.mutable_vi()->set_name(GetSessionName());
    auto exported_configuration = export_buffer_response.configuration();
    import_request.mutable_configuration()->append(exported_configuration.begin(), exported_configuration.end());
    dcpower::ImportAttributeConfigurationBufferResponse import_response;

    ::grpc::Status status = GetStub()->ImportAttributeConfigurationBuffer(&context, import_request, &import_response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kdcpowerDriverApiSuccess, import_response.status());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<dcpower::NiDCPower::Stub> nidcpower_stub_;
  bool is_legacy_session_{false};
};

// Some tests don't work with the legacy InitializeWithChannels API
// because of differences in how channels are configured OR because they
// test features of the independent channel API.
#define GTEST_SKIP_IF_LEGACY() \
  if (is_legacy_session()) GTEST_SKIP() << "Test not supported with legacy session API.";

TEST_F(NiDCPowerDriverApiTest, PerformSelfTest_CompletesSuccessfuly)
{
  ::grpc::ClientContext context;
  dcpower::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  dcpower::SelfTestResponse response;
  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_LT(0, response.self_test_message().size());
}

TEST_F(NiDCPowerDriverApiTest, PerformReset_CompletesSuccessfuly)
{
  ::grpc::ClientContext context;
  dcpower::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  dcpower::ResetResponse response;
  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
}

TEST_F(NiDCPowerDriverApiTest, SetAttributeViInt32_GetAttributeViInt32ReturnsSameValue)
{
  const char* channel_name = "";
  const dcpower::NiDCPowerAttribute attribute_to_set = dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_WHEN;
  const auto expected_value = dcpower::NiDCPowerInt32AttributeValues::NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE;
  ::grpc::ClientContext context;
  dcpower::SetAttributeViInt32Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value(expected_value);
  dcpower::SetAttributeViInt32Response response;
  ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  int32 get_attribute_value = get_int32_attribute(channel_name, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDCPowerDriverApiTest, SetAttributeViReal64_GetAttributeViReal64ReturnsSameValue)
{
  GTEST_SKIP_IF_LEGACY();
  const char* channel_name = "0";
  // Attribute 'NIDCPOWER_ATTRIBUTE_MEASURE_WHEN' must be set to 'MEASURE_WHEN_NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE'
  // before setting attribute 'NIDCPOWER_ATTRIBUTE_SOURCE_DELAY'.
  set_int32_attribute(
      channel_name,
      dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_WHEN,
      dcpower::NiDCPowerInt32AttributeValues::NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE);
  const dcpower::NiDCPowerAttribute attribute_to_set = dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_SOURCE_DELAY;
  const double expected_value = 2.516;
  ::grpc::ClientContext context;
  dcpower::SetAttributeViReal64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  dcpower::SetAttributeViReal64Response response;
  ::grpc::Status status = GetStub()->SetAttributeViReal64(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  double get_attribute_value_sourcedelay = get_real64_attribute(channel_name, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value_sourcedelay);
}

TEST_F(NiDCPowerDriverApiTest, SetAttributeViBoolean_GetAttributeViBooleanReturnsSameValue)
{
  GTEST_SKIP_IF_LEGACY();
  const char* channel_name = "0";
  // Attribute 'NIDCPOWER_ATTRIBUTE_MEASURE_WHEN' must be set to 'MEASURE_WHEN_NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE'
  // before setting attribute 'NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE'.
  set_int32_attribute(
      channel_name,
      dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_WHEN,
      dcpower::NiDCPowerInt32AttributeValues::NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE);
  const dcpower::NiDCPowerAttribute attribute_to_set = dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE;
  const bool expected_value = true;
  ::grpc::ClientContext context;
  dcpower::SetAttributeViBooleanRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value(expected_value);
  dcpower::SetAttributeViBooleanResponse response;
  ::grpc::Status status = GetStub()->SetAttributeViBoolean(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  bool get_attribute_value = get_bool_attribute(channel_name, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDCPowerDriverApiTest, SetAttributeViString_GetAttributeViStringReturnsSameValue)
{
  GTEST_SKIP_IF_LEGACY();
  const char* channel_name = "0";
  const dcpower::NiDCPowerAttribute attribute_to_set = dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL;
  const char* expected_value = "/Dev1/PXI_Trig0";
  ::grpc::ClientContext context;
  dcpower::SetAttributeViStringRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  dcpower::SetAttributeViStringResponse response;
  ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  std::string get_attribute_value = get_string_attribute(channel_name, attribute_to_set);
  EXPECT_STREQ(expected_value, get_attribute_value.c_str());
}

TEST_F(NiDCPowerDriverApiTest, SetAttributeViInt64_GetAttributeViInt64ReturnsSameValue)
{
  const char* channel_name = "";
  const dcpower::NiDCPowerAttribute attribute_to_set = dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE_STEP;
  const int64 expected_value = 1;
  ::grpc::ClientContext context;
  dcpower::SetAttributeViInt64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  dcpower::SetAttributeViInt64Response response;
  ::grpc::Status status = GetStub()->SetAttributeViInt64(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
  int64 get_attribute_value = get_int64_attribute(channel_name, attribute_to_set);
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDCPowerDriverApiTest, ConfigureOutputFunctionAndVoltageLevel_ConfiguresSuccessfully)
{
  const char* channel_name = "0";
  double expected_voltage_level = 3.0;
  auto expected_output_function_value = dcpower::OutputFunction::OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_VOLTAGE;
  configure_output_function(channel_name, expected_output_function_value);
  configure_voltage_level(channel_name, expected_voltage_level);

  double actual_voltage_level = get_real64_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL);
  int32 actual_output_function_value = get_int32_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION);
  EXPECT_EQ(expected_voltage_level, actual_voltage_level);
  EXPECT_EQ(expected_output_function_value, actual_output_function_value);
}

TEST_F(NiDCPowerDriverApiTest, ConfigureOutputFunctionAndCurrentLevel_ConfiguresSuccessfully)
{
  const char* channel_name = "0";
  double expected_current_level = 3.0;
  auto expected_output_function_value = dcpower::OutputFunction::OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_CURRENT;
  configure_output_function(channel_name, expected_output_function_value);
  configure_current_level(channel_name, expected_current_level);

  double actual_current_level = get_real64_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL);
  int32 actual_output_function_value = get_int32_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION);
  EXPECT_EQ(expected_current_level, actual_current_level);
  EXPECT_EQ(expected_output_function_value, actual_output_function_value);
}

TEST_F(NiDCPowerDriverApiTest, SetMeasureWhenAndInitiate_MeasureMultiple_ReturnsSuccess)
{
  const char* channel_name = "";  // all channels in session
  // Attribute 'NIDCPOWER_ATTRIBUTE_MEASURE_WHEN' must be set to On Demand before calling MeasureMultiple
  set_int32_attribute(
      channel_name,
      dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_WHEN,
      dcpower::NiDCPowerInt32AttributeValues::NIDCPOWER_INT32_MEASURE_WHEN_VAL_ON_DEMAND);
  initiate();

  dcpower::MeasureMultipleResponse response;
  measure_multiple(channel_name, &response);

  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
}

TEST_F(NiDCPowerDriverApiTest, SetMeasureWhenAndInitiate_FetchMultiple_FetchesSuccessfully)
{
  GTEST_SKIP_IF_LEGACY();
  const char* channel_name = "0";
  // Attribute 'NIDCPOWER_ATTRIBUTE_MEASURE_WHEN' must be set before calling FetchMultiple
  set_int32_attribute(
      channel_name,
      dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_MEASURE_WHEN,
      dcpower::NiDCPowerInt32AttributeValues::NIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE);
  initiate();

  dcpower::FetchMultipleResponse response;
  fetch_multiple(channel_name, &response);

  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
}

TEST_F(NiDCPowerDriverApiTest, VoltageLevelConfiguredAndExportedToBuffer_ResetAndImportConfigurationFromBuffer_ConfigurationIsImportedSuccessfully)
{
  GTEST_SKIP_IF_LEGACY();
  const char* channel_name = "0";
  auto expected_output_function = dcpower::OutputFunction::OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_VOLTAGE;
  auto expected_voltage_level = 3.0;
  configure_output_function(channel_name, expected_output_function);
  configure_voltage_level(channel_name, expected_voltage_level);
  auto export_buffer_response = export_attribute_configuration_buffer();

  reset_with_channels(channel_name);
  import_attribute_configuration_buffer(export_buffer_response);

  auto actual_voltage_level = get_real64_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL);
  auto actual_output_function = get_int32_attribute(channel_name, dcpower::NiDCPowerAttribute::NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION);
  EXPECT_EQ(expected_voltage_level, actual_voltage_level);
  EXPECT_EQ(expected_output_function, actual_output_function);
}

TEST_F(NiDCPowerDriverApiTest, CalSelfCalibrate_CompletesSuccessfully)
{
  const char* channel_name = "";
  ::grpc::ClientContext context;
  dcpower::CalSelfCalibrateRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  dcpower::CalSelfCalibrateResponse response;
  ::grpc::Status status = GetStub()->CalSelfCalibrate(&context, request, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(kdcpowerDriverApiSuccess, response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidcpower_session_tests.cpp sha256=0866b76d18a4434104ebb2d96d84bc43d8c219f27b206ef5cd15f64e3e52a637 bytes=6486 -->
## FILE: source/tests/system/nidcpower_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidcpower_session_tests.cpp`
- sha256: `0866b76d18a4434104ebb2d96d84bc43d8c219f27b206ef5cd15f64e3e52a637`
- bytes: 6486

````cpp
#include <gmock/gmock.h>

#include "device_server.h"
#include "nidcpower/nidcpower_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace dcpower = nidcpower_grpc;
using namespace ::testing;

const int kInvalidRsrc = -1074118656;
const int kInvalidDCPowerSession = -1074130544;
const char* kViErrorResourceNotFoundMessage = "Device was not recognized. The device is not supported with this driver or version.\n\nInvalid Identifier: ";
const char* kInvalidDCPowerSessionMessage = "The session handle is not valid.";
const char* kTestRsrc = "FakeDevice";
const char* kOptionsString = "Simulate=1, DriverSetup=Model:4147; BoardType:PXIe";
const char* kTestSession = "SessionName";
const char* kTestInvalidRsrc = "";

class NiDCPowerSessionTest : public ::testing::Test {
 protected:
  NiDCPowerSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidcpower_stub_(dcpower::NiDCPower::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDCPowerSessionTest() {}

  std::unique_ptr<dcpower::NiDCPower::Stub>& GetStub()
  {
    return nidcpower_stub_;
  }

  ::grpc::Status call_initialize_with_independent_channels(const char* resource_name, const char* option_string, const char* session_name, dcpower::InitializeWithIndependentChannelsResponse* response)
  {
    ::grpc::ClientContext context;
    dcpower::InitializeWithIndependentChannelsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset(false);

    ::grpc::Status status = GetStub()->InitializeWithIndependentChannels(&context, request, response);
    return status;
  }

  ::grpc::Status call_initialize_with_channels(const char* resource_name, const char* option_string, const char* session_name, dcpower::InitializeWithChannelsResponse* response)
  {
    ::grpc::ClientContext context;
    dcpower::InitializeWithChannelsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset(false);
    request.set_channels("");

    auto status = GetStub()->InitializeWithChannels(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  std::string get_error_message(int error_status)
  {
    dcpower::InitializeWithIndependentChannelsResponse init_response;
    call_initialize_with_independent_channels(kTestRsrc, kOptionsString, kTestSession, &init_response);
    nidevice_grpc::Session session = init_response.vi();

    ::grpc::ClientContext context;
    dcpower::ErrorMessageRequest request;
    request.mutable_vi()->set_name(session.name());
    request.set_error_code(error_status);
    dcpower::ErrorMessageResponse error_response;

    ::grpc::Status status = GetStub()->ErrorMessage(&context, request, &error_response);
    EXPECT_TRUE(status.ok());
    return error_response.error_message();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<dcpower::NiDCPower::Stub> nidcpower_stub_;
};

// InitializeWithIndependentChannels was added in dcpower 20.7.
// To support testing with older versions: skip tests for InitializeWithIndependentChannels if
// it returns an unsupported status.
#define GTEST_SKIP_IF_UNSUPPORTED(status) \
  if (status.error_code() == ::grpc::NOT_FOUND) GTEST_SKIP() << "Function not supported.";

TEST_F(NiDCPowerSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  dcpower::InitializeWithIndependentChannelsResponse response;
  auto status = call_initialize_with_independent_channels(kTestRsrc, kOptionsString, kTestSession, &response);

  GTEST_SKIP_IF_UNSUPPORTED(status);
  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDCPowerSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  dcpower::InitializeWithIndependentChannelsResponse response;
  ::grpc::Status status = call_initialize_with_independent_channels(kTestRsrc, kOptionsString, "", &response);

  GTEST_SKIP_IF_UNSUPPORTED(status);
  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDCPowerSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    dcpower::InitializeWithChannelsResponse response;
    call_initialize_with_channels(kTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiDCPowerSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  dcpower::InitializeWithIndependentChannelsResponse initialize_response;
  auto status = call_initialize_with_independent_channels(kTestRsrc, kOptionsString, kTestSession, &initialize_response);
  GTEST_SKIP_IF_UNSUPPORTED(status);
  EXPECT_TRUE(status.ok());
  nidevice_grpc::Session session = initialize_response.vi();

  ::grpc::ClientContext context;
  dcpower::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  dcpower::CloseResponse close_response;
  status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiDCPowerSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    ::grpc::ClientContext context;
    dcpower::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    dcpower::CloseResponse response;
    auto status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidDCPowerSession, kInvalidDCPowerSessionMessage);
}

TEST_F(NiDCPowerSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    dcpower::InitializeWithChannelsResponse initialize_response;
    call_initialize_with_channels(kTestInvalidRsrc, "", "", &initialize_response);
  }, kInvalidRsrc, kViErrorResourceNotFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidigital_driver_api_tests.cpp sha256=827cf163a50642ffeccdf134c3d1f006e7e8b44a380b4389ef7bdc29416abda2 bytes=27086 -->
## FILE: source/tests/system/nidigital_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidigital_driver_api_tests.cpp`
- sha256: `827cf163a50642ffeccdf134c3d1f006e7e8b44a380b4389ef7bdc29416abda2`
- bytes: 27086

````cpp
#include <gtest/gtest.h>

#ifdef FS_EXPERIMENTAL
  #include <experimental/filesystem>
#else
  #include <filesystem>
#endif

#include "device_server.h"
#include "nidigitalpattern/nidigitalpattern_client.h"
#include "tests/utilities/test_helpers.h"

#define EXPECT_SUCCESS(status)               \
  EXPECT_TRUE((status).ok());                \
  if (!(status).ok()) {                      \
    EXPECT_EQ(0, (status).error_code());     \
    EXPECT_EQ("", (status).error_message()); \
  }

namespace ni {
namespace tests {
namespace system {

namespace digital = nidigitalpattern_grpc;
namespace pb = ::google::protobuf;
#ifdef FS_EXPERIMENTAL
namespace fs = std::experimental::filesystem;
#else
namespace fs = std::filesystem;
#endif

typedef pb::int32 int32;
typedef pb::int64 int64;

const int kDigitalDriverApiSuccess = 0;

class NiDigitalDriverApiTest : public ::testing::Test {
 protected:
  NiDigitalDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidigital_stub_(digital::NiDigital::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDigitalDriverApiTest() {}

  void SetUp() override
  {
#ifndef WIN32
    GTEST_SKIP() << "Digital pattern is not supported on Linux.";
#endif
    initialize_driver_session();
    initialize_multi_instrument_driver_session();
  }

  void TearDown() override
  {
    close_multi_instrument_driver_session();
    close_driver_session();
  }

  std::unique_ptr<digital::NiDigital::Stub>& GetStub()
  {
    return nidigital_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  std::string GetMultiInstrumentSessionName()
  {
    return multi_instrument_driver_session_->name();
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    digital::InitWithOptionsRequest request;
    request.set_resource_name("FakeDevice");
    request.set_option_string("Simulate=1, DriverSetup=Model:6570; BoardType:PXIe");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_id_query(false);
    digital::InitWithOptionsResponse response;

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void initialize_multi_instrument_driver_session()
  {
    ::grpc::ClientContext context;
    digital::InitWithOptionsRequest request;
    request.set_resource_name("PXI1Slot2,PXI1Slot5");
    request.set_option_string("Simulate=1, DriverSetup=Model:6570; BoardType:PXIe");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_id_query(false);
    digital::InitWithOptionsResponse response;

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    multi_instrument_driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void close_driver_session()
  {
    if (!driver_session_) {
      return;
    }
    ::grpc::ClientContext context;
    digital::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    digital::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void close_multi_instrument_driver_session()
  {
    if (!multi_instrument_driver_session_) {
      return;
    }
    ::grpc::ClientContext context;
    digital::CloseRequest request;
    request.mutable_vi()->set_name(multi_instrument_driver_session_->name());
    digital::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void expect_api_success(int error_status)
  {
    EXPECT_EQ(kDigitalDriverApiSuccess, error_status) << get_error_message(error_status);
  }

  std::string get_error_message(int error_status)
  {
    ::grpc::ClientContext context;
    digital::ErrorMessageRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_error_code(error_status);
    digital::ErrorMessageResponse response;

    ::grpc::Status status = GetStub()->ErrorMessage(&context, request, &response);
    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
    return response.error_message();
  }

  void load_pin_map(const std::string& session_name, const fs::path& file_path)
  {
    ::grpc::ClientContext context;
    digital::LoadPinMapRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_file_path(file_path.string());
    digital::LoadPinMapResponse response;

    ::grpc::Status status = GetStub()->LoadPinMap(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void load_specifications(const std::string& session_name, const fs::path& file_path)
  {
    ::grpc::ClientContext context;
    digital::LoadSpecificationsRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_file_path(file_path.string());
    digital::LoadSpecificationsResponse response;

    ::grpc::Status status = GetStub()->LoadSpecifications(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void load_levels(const std::string & session_name, const fs::path& file_path)
  {
    ::grpc::ClientContext context;
    digital::LoadLevelsRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_file_path(file_path.string());
    digital::LoadLevelsResponse response;

    ::grpc::Status status = GetStub()->LoadLevels(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void load_timing(const std::string& session_name, const fs::path& file_path)
  {
    ::grpc::ClientContext context;
    digital::LoadTimingRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_file_path(file_path.string());
    digital::LoadTimingResponse response;

    ::grpc::Status status = GetStub()->LoadTiming(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void apply_levels_and_timing(const std::string & session_name, const char* levels_sheet, const char* timing_sheet)
  {
    ::grpc::ClientContext context;
    digital::ApplyLevelsAndTimingRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_levels_sheet(levels_sheet);
    request.set_timing_sheet(timing_sheet);
    digital::ApplyLevelsAndTimingResponse response;

    ::grpc::Status status = GetStub()->ApplyLevelsAndTiming(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void configure_session(const std::string & session_name)
  {
    load_pin_map(session_name, fs::absolute("test_create_capture_waveform_serial/pin_map.pinmap"));
    load_specifications(session_name, fs::absolute("test_create_capture_waveform_serial/specifications.specs"));
    load_levels(session_name, fs::absolute("test_create_capture_waveform_serial/pin_levels.digilevels"));
    load_timing(session_name, fs::absolute("test_create_capture_waveform_serial/timing.digitiming"));
    apply_levels_and_timing(session_name, "pin_levels", "timing");
  }

  void load_pattern(const std::string & session_name, const fs::path& file_path)
  {
    ::grpc::ClientContext context;
    digital::LoadPatternRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_file_path(file_path.string());
    digital::LoadPatternResponse response;

    ::grpc::Status status = GetStub()->LoadPattern(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void create_capture_waveform_serial(
      const std::string & session_name,
      const char* pin_list,
      const char* waveform_name,
      int sample_width,
      digital::BitOrder bit_order)
  {
    ::grpc::ClientContext context;
    digital::CreateCaptureWaveformSerialRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_pin_list(pin_list);
    request.set_waveform_name(waveform_name);
    request.set_sample_width(sample_width);
    request.set_bit_order(bit_order);
    digital::CreateCaptureWaveformSerialResponse response;

    ::grpc::Status status = GetStub()->CreateCaptureWaveformSerial(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void create_source_waveform_serial(
      const std::string & session_name,
      const char* pin_list,
      const char* waveform_name,
      digital::SourceDataMapping data_mapping,
      int sample_width,
      digital::BitOrder bit_order)
  {
    ::grpc::ClientContext context;
    digital::CreateSourceWaveformSerialRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_pin_list(pin_list);
    request.set_waveform_name(waveform_name);
    request.set_data_mapping(data_mapping);
    request.set_sample_width(sample_width);
    request.set_bit_order(bit_order);
    digital::CreateSourceWaveformSerialResponse response;

    ::grpc::Status status = GetStub()->CreateSourceWaveformSerial(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void write_source_waveform_broadcast_u32(const std::string & session_name, const char* waveform_name, unsigned int* waveform_data, int num_samples)
  {
    ::grpc::ClientContext context;
    digital::WriteSourceWaveformBroadcastU32Request request;
    request.mutable_vi()->set_name(session_name);
    request.set_waveform_name(waveform_name);
    for (int i = 0; i < num_samples; ++i) {
      request.add_waveform_data(waveform_data[i]);
    }
    digital::WriteSourceWaveformBroadcastU32Response response;

    ::grpc::Status status = GetStub()->WriteSourceWaveformBroadcastU32(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void burst_pattern(const std::string & session_name, const char* start_label)
  {
    ::grpc::ClientContext context;
    digital::BurstPatternRequest request;
    request.mutable_vi()->set_name(session_name);
    request.set_start_label(start_label);
    digital::BurstPatternResponse response;

    ::grpc::Status status = GetStub()->BurstPattern(&context, request, &response);

    EXPECT_SUCCESS(status);
    EXPECT_EQ(kDigitalDriverApiSuccess, response.status());
  }

  void fetch_capture_waveform(
      const std::string & session_name,
      const char* site_list,
      const char* waveform_name,
      int samples_to_read,
      digital::FetchCaptureWaveformU32Response* response)
  {
    ::grpc::ClientContext context;
    digital::FetchCaptureWaveformU32Request request;
    request.mutable_vi()->set_name(session_name);
    request.set_site_list(site_list);
    request.set_waveform_name(waveform_name);
    request.set_samples_to_read(samples_to_read);
    request.set_timeout(2.0);

    ::grpc::Status status = GetStub()->FetchCaptureWaveformU32(&context, request, response);

    EXPECT_SUCCESS(status);
  }

  void set_bool_attribute(const char* channel_name, digital::NiDigitalAttribute attribute, bool value)
  {
    ::grpc::ClientContext context;
    digital::SetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    request.set_value(value);
    digital::SetAttributeViBooleanResponse response;

    ::grpc::Status status = GetStub()->SetAttributeViBoolean(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void set_int32_attribute(const char* channel_name, digital::NiDigitalAttribute attribute, digital::NiDigitalInt32AttributeValues value)
  {
    ::grpc::ClientContext context;
    digital::SetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    request.set_value(value);
    digital::SetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void set_int64_attribute(const char* channel_name, digital::NiDigitalAttribute attribute, int64 value)
  {
    ::grpc::ClientContext context;
    digital::SetAttributeViInt64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    request.set_value_raw(value);
    digital::SetAttributeViInt64Response response;

    ::grpc::Status status = GetStub()->SetAttributeViInt64(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void set_string_attribute(const char* channel_name, digital::NiDigitalAttribute attribute, const std::string& value)
  {
    ::grpc::ClientContext context;
    digital::SetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    request.set_value_raw(value);
    digital::SetAttributeViStringResponse response;

    ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  bool get_bool_attribute(const char* channel_name, digital::NiDigitalAttribute attribute)
  {
    ::grpc::ClientContext context;
    digital::GetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    digital::GetAttributeViBooleanResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViBoolean(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
    return response.value();
  }

  int32 get_int32_attribute(const char* channel_name, digital::NiDigitalAttribute attribute)
  {
    ::grpc::ClientContext context;
    digital::GetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    digital::GetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt32(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
    return response.value();
  }

  int64 get_int64_attribute(const char* channel_name, digital::NiDigitalAttribute attribute)
  {
    ::grpc::ClientContext context;
    digital::GetAttributeViInt64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    digital::GetAttributeViInt64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt64(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
    return response.value();
  }

  std::string get_string_attribute(const char* channel_name, digital::NiDigitalAttribute attribute)
  {
    ::grpc::ClientContext context;
    digital::GetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute(attribute);
    digital::GetAttributeViStringResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViString(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
    return response.value();
  }

  void configure_frequency_counter_measurement_time(const char* channel_list, double value)
  {
    ::grpc::ClientContext context;
    digital::FrequencyCounterConfigureMeasurementTimeRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_measurement_time(value);
    digital::FrequencyCounterConfigureMeasurementTimeResponse response;

    ::grpc::Status status = GetStub()->FrequencyCounterConfigureMeasurementTime(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

  void select_function(const char* channel_list, digital::SelectedFunction function_type)
  {
    ::grpc::ClientContext context;
    digital::SelectFunctionRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_list(channel_list);
    request.set_function(function_type);
    digital::SelectFunctionResponse response;

    ::grpc::Status status = GetStub()->SelectFunction(&context, request, &response);

    EXPECT_SUCCESS(status);
    expect_api_success(response.status());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<::nidevice_grpc::Session> multi_instrument_driver_session_;
  std::unique_ptr<digital::NiDigital::Stub> nidigital_stub_;
};

TEST_F(NiDigitalDriverApiTest, PerformReadStatic_CompletesSuccessfully)
{
  const char* channel_name = "";
  ::grpc::ClientContext context;
  select_function(channel_name, digital::SelectedFunction::SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL);
  digital::ReadStaticRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_name);
  digital::ReadStaticResponse response;
  ::grpc::Status status = GetStub()->ReadStatic(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
}

TEST_F(NiDigitalDriverApiTest, PerformWriteStatic_CompletesSuccessfully)
{
  const char* channel_name = "";
  ::grpc::ClientContext context;
  select_function(channel_name, digital::SelectedFunction::SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL);
  digital::WriteStaticRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_name);
  request.set_state(digital::WriteStaticPinState::WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_0);
  digital::WriteStaticResponse response;
  ::grpc::Status status = GetStub()->WriteStatic(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
}

TEST_F(NiDigitalDriverApiTest, PerformFrequencyCounterMeasureFrequency_CompletesSuccessfully)
{
  const char* channel_name = "";
  double measurement_time = 5.0;
  ::grpc::ClientContext context;
  select_function(channel_name, digital::SelectedFunction::SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL);
  configure_frequency_counter_measurement_time(channel_name, measurement_time);
  digital::FrequencyCounterMeasureFrequencyRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_name);
  digital::FrequencyCounterMeasureFrequencyResponse response;
  ::grpc::Status status = GetStub()->FrequencyCounterMeasureFrequency(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
}

TEST_F(NiDigitalDriverApiTest, CreateCaptureWaveformSerial_FetchCaptureWaveform_ReturnsReasonableData)
{
  const std::string& session_name = GetMultiInstrumentSessionName();
  configure_session(session_name);
  load_pattern(session_name, fs::absolute("test_create_capture_waveform_serial/pattern.digipat"));
  auto bit_order = digital::BitOrder::BIT_ORDER_NIDIGITAL_VAL_LSB_FIRST;
  create_capture_waveform_serial(session_name, "HI0", "capt_wfm", 2, bit_order);
  // The pattern references a wfm "src_wfm", so we have to load it before we can burst
  auto source_data_mapping = digital::SourceDataMapping::SOURCE_DATA_MAPPING_NIDIGITAL_VAL_BROADCAST;
  create_source_waveform_serial(session_name, "LO0", "src_wfm", source_data_mapping, 2, bit_order);
  unsigned int waveform_data[] = {1, 2};
  write_source_waveform_broadcast_u32(session_name, "src_wfm", waveform_data, sizeof(waveform_data) / sizeof(unsigned int));
  burst_pattern(session_name, "new_pattern");

  int num_samples = 2;
  digital::FetchCaptureWaveformU32Response response;
  fetch_capture_waveform(session_name, "site0,site1", "capt_wfm", num_samples, &response);

  int num_sites = 2;
  expect_api_success(response.status());
  EXPECT_EQ(num_sites * num_samples, response.data_size());
}

TEST_F(NiDigitalDriverApiTest, SelfTest_SelfTestCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  digital::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  digital::SelfTestResponse response;
  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
  EXPECT_EQ(0, response.test_result());
  EXPECT_LT(0, strlen(response.test_message().c_str()));
}

TEST_F(NiDigitalDriverApiTest, Reset_ResetCompletesSuccessfully)
{
  ::grpc::ClientContext context;
  digital::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  digital::ResetResponse response;
  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
}

TEST_F(NiDigitalDriverApiTest, SetViInt32Attribute_GetViInt32Attribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const digital::NiDigitalAttribute attribute_to_set = digital::NiDigitalAttribute::NIDIGITAL_ATTRIBUTE_SELECTED_FUNCTION;
  auto expected_value = digital::NiDigitalInt32AttributeValues::NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_PPMU;
  set_int32_attribute(channel_name, attribute_to_set, expected_value);

  int32 get_attribute_value = get_int32_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDigitalDriverApiTest, SetViInt64Attribute_GetViInt64Attribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const digital::NiDigitalAttribute attribute_to_set = digital::NiDigitalAttribute::NIDIGITAL_ATTRIBUTE_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER;
  const int64 expected_value = 4;
  set_int64_attribute(channel_name, attribute_to_set, expected_value);

  int64 get_attribute_value = get_int64_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDigitalDriverApiTest, SetViStringAttribute_GetViStringAttribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const digital::NiDigitalAttribute attribute_to_set = digital::NiDigitalAttribute::NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE;
  const std::string expected_value = "Hello world!";
  set_string_attribute(channel_name, attribute_to_set, expected_value);

  std::string get_attribute_value = get_string_attribute(channel_name, attribute_to_set);

  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

TEST_F(NiDigitalDriverApiTest, SetBoolAttribute_GetBoolAttribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const digital::NiDigitalAttribute attribute_to_set = digital::NiDigitalAttribute::NIDIGITAL_ATTRIBUTE_CACHE;
  const bool expected_value = true;
  set_bool_attribute(channel_name, attribute_to_set, expected_value);

  bool get_attribute_value = get_bool_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDigitalDriverApiTest, SelfCalibrate_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  digital::SelfCalibrateRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  digital::SelfCalibrateResponse response;
  ::grpc::Status status = GetStub()->SelfCalibrate(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
}

TEST_F(NiDigitalDriverApiTest, ClockGeneratorInitiate_ClockGenerationInitiated)
{
  std::string channel_list = "0";
  ::grpc::ClientContext context;
  digital::ClockGeneratorInitiateRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_list(channel_list);
  digital::ClockGeneratorInitiateResponse response;
  ::grpc::Status status = GetStub()->ClockGeneratorInitiate(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
  EXPECT_TRUE(get_bool_attribute("0", digital::NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_IS_RUNNING));
}

TEST_F(NiDigitalDriverApiTest, ConfigureSoftwareEdgeStartTrigger_StartTriggerTypeAttributeIsSoftware)
{
  ::grpc::ClientContext context;
  digital::ConfigureSoftwareEdgeStartTriggerRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  digital::ConfigureSoftwareEdgeStartTriggerResponse response;
  ::grpc::Status status = GetStub()->ConfigureSoftwareEdgeStartTrigger(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
  int start_trigger_type = get_int32_attribute("", digital::NIDIGITAL_ATTRIBUTE_START_TRIGGER_TYPE);
  EXPECT_EQ(digital::NiDigitalInt32AttributeValues::NIDIGITAL_INT32_TRIGGER_TYPE_VAL_SOFTWARE, start_trigger_type);
}

TEST_F(NiDigitalDriverApiTest, ConfigureStartLabel_StartLabelConfigured)
{
  const char* start_label = "abcde";
  ::grpc::ClientContext context;
  digital::ConfigureStartLabelRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_label(start_label);
  digital::ConfigureStartLabelResponse response;
  ::grpc::Status status = GetStub()->ConfigureStartLabel(&context, request, &response);

  EXPECT_SUCCESS(status);
  expect_api_success(response.status());
  std::string actual_start_label = get_string_attribute("", digital::NIDIGITAL_ATTRIBUTE_START_LABEL);
  EXPECT_EQ(start_label, actual_start_label);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidigital_session_tests.cpp sha256=22968ac30b55b0102b7a02ccd176c6362074dd893169c1b90d1a3a1315457a0b bytes=3759 -->
## FILE: source/tests/system/nidigital_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidigital_session_tests.cpp`
- sha256: `22968ac30b55b0102b7a02ccd176c6362074dd893169c1b90d1a3a1315457a0b`
- bytes: 3759

````cpp
#include "device_server.h"
#include "nidigitalpattern/nidigitalpattern_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace digital = nidigitalpattern_grpc;

const int kDigitalRsrcNotFound = -1074098043;
const char* kDigitalRsrcNotFoundMessage = "Specified string is not valid, because it is empty.";
const char* kDigitalResourceName = "FakeDevice";
const char* kDigitalOptionsString = "Simulate=1, DriverSetup=Model:6570; BoardType:PXIe";
const char* kDigitalSessionName = "SessionName";
const char* kDigitalInvalidResourceName = "";

class NiDigitalSessionTest : public ::testing::Test {
 protected:
  NiDigitalSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidigital_stub_(digital::NiDigital::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDigitalSessionTest() {}

  void SetUp() override
  {
#ifndef WIN32
    GTEST_SKIP() << "Digital pattern is not supported on Linux.";
#endif
  }

  std::unique_ptr<digital::NiDigital::Stub>& GetStub()
  {
    return nidigital_stub_;
  }

  ::grpc::Status call_init_with_options(const char* resource_name, const char* option_string, const char* session_name, digital::InitWithOptionsResponse* response)
  {
    ::grpc::ClientContext context;
    digital::InitWithOptionsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset_device(false);
    request.set_id_query(false);

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<digital::NiDigital::Stub> nidigital_stub_;
};

TEST_F(NiDigitalSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  digital::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kDigitalResourceName, kDigitalOptionsString, kDigitalSessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDigitalSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  digital::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kDigitalResourceName, kDigitalOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDigitalSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  digital::InitWithOptionsResponse init_response;
  call_init_with_options(kDigitalResourceName, kDigitalOptionsString, kDigitalSessionName, &init_response);

  nidevice_grpc::Session session = init_response.vi();
  ::grpc::ClientContext context;
  digital::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  digital::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiDigitalSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    digital::InitWithOptionsResponse init_response;
    auto status = call_init_with_options(kDigitalInvalidResourceName, "", "", &init_response);
  }, kDigitalRsrcNotFound, kDigitalRsrcNotFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidmm_driver_api_tests.cpp sha256=e40555a5b3baba3f8b9f9fce0c126b3fad472a904b43b41b2068cae69d58d358 bytes=13307 -->
## FILE: source/tests/system/nidmm_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidmm_driver_api_tests.cpp`
- sha256: `e40555a5b3baba3f8b9f9fce0c126b3fad472a904b43b41b2068cae69d58d358`
- bytes: 13307

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nidmm/nidmm_client.h"
#include "nidmm/nidmm_library.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace dmm = nidmm_grpc;

const int kDMMDriverApiSuccess = 0;

class NiDmmDriverApiTest : public ::testing::Test {
 protected:
  NiDmmDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidmm_stub_(dmm::NiDmm::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDmmDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<dmm::NiDmm::Stub>& GetStub()
  {
    return nidmm_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  void expect_api_success(int error_status)
  {
    EXPECT_EQ(kDMMDriverApiSuccess, error_status) << get_error_message(error_status);
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    dmm::InitWithOptionsRequest request;
    request.set_resource_name("SimulatedDMM");
    request.set_option_string("Simulate=1, DriverSetup=Model:4080; BoardType:PXIe");
    request.set_session_name("");
    request.set_reset_device(false);
    request.set_id_query(false);
    dmm::InitWithOptionsResponse response;

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void close_driver_session()
  {
    ::grpc::ClientContext context;
    dmm::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    dmm::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  std::string get_error_message(int error_status)
  {
    ::grpc::ClientContext context;
    dmm::GetErrorMessageRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_error_code(error_status);
    dmm::GetErrorMessageResponse response;
    ::grpc::Status status = GetStub()->GetErrorMessage(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kDMMDriverApiSuccess, response.status());

    return response.error_message();
  }

  ViBoolean get_bool_attribute(const char* channel_name, dmm::NiDmmAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dmm::GetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    dmm::GetAttributeViBooleanResponse response;
    ::grpc::Status status = GetStub()->GetAttributeViBoolean(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());

    return response.attribute_value();
  }

  ViInt32 get_int32_attribute(const char* channel_name, dmm::NiDmmAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dmm::GetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    dmm::GetAttributeViInt32Response response;
    ::grpc::Status status = GetStub()->GetAttributeViInt32(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());

    return response.attribute_value();
  }

  ViReal64 get_real64_attribute(const char* channel_name, dmm::NiDmmAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    dmm::GetAttributeViReal64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute_id);
    dmm::GetAttributeViReal64Response response;
    ::grpc::Status status = GetStub()->GetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());

    return response.attribute_value();
  }

  void configure_current_source(double value)
  {
    ::grpc::ClientContext context;
    dmm::ConfigureCurrentSourceRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_current_source(value);
    dmm::ConfigureCurrentSourceResponse response;
    ::grpc::Status status = GetStub()->ConfigureCurrentSource(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  dmm::ExportAttributeConfigurationBufferResponse export_attribute_configuration_buffer()
  {
    ::grpc::ClientContext context;
    dmm::ExportAttributeConfigurationBufferRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    dmm::ExportAttributeConfigurationBufferResponse response;
    ::grpc::Status status = GetStub()->ExportAttributeConfigurationBuffer(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());

    return response;
  }

  void reset()
  {
    ::grpc::ClientContext context;
    dmm::ResetRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    dmm::ResetResponse response;
    ::grpc::Status status = GetStub()->Reset(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void import_attribute_configuration_buffer(dmm::ExportAttributeConfigurationBufferResponse exported_configuration_response)
  {
    ::grpc::ClientContext context;
    dmm::ImportAttributeConfigurationBufferRequest import_request;
    import_request.mutable_vi()->set_name(GetSessionName());
    auto exported_configuration = exported_configuration_response.configuration();
    import_request.mutable_configuration()->append(exported_configuration.begin(), exported_configuration.end());
    dmm::ImportAttributeConfigurationBufferResponse import_response;
    ::grpc::Status status = GetStub()->ImportAttributeConfigurationBuffer(&context, import_request, &import_response);

    EXPECT_TRUE(status.ok());
    expect_api_success(import_response.status());
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<dmm::NiDmm::Stub> nidmm_stub_;
};

TEST_F(NiDmmDriverApiTest, SelfTest_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  dmm::SelfTestResponse response;
  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_LT(0, strlen(response.self_test_message().c_str()));
}

TEST_F(NiDmmDriverApiTest, Reset_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  dmm::ResetResponse response;
  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiDmmDriverApiTest, SetViReal64Attribute_GetViReal64Attribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const dmm::NiDmmAttribute attribute_to_set = dmm::NiDmmAttribute::NIDMM_ATTRIBUTE_TRIGGER_DELAY;
  const ViReal64 expected_value = 42.24;
  ::grpc::ClientContext context;
  dmm::SetAttributeViReal64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  dmm::SetAttributeViReal64Response response;
  ::grpc::Status status = GetStub()->SetAttributeViReal64(&context, request, &response);
  ViReal64 get_attribute_value = get_real64_attribute(channel_name, attribute_to_set);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDmmDriverApiTest, SetViInt32Attribute_GetViInt32Attribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const dmm::NiDmmAttribute attribute_to_set = dmm::NiDmmAttribute::NIDMM_ATTRIBUTE_SAMPLE_COUNT;
  const ViInt32 expected_value = 4;
  ::grpc::ClientContext context;
  dmm::SetAttributeViInt32Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  dmm::SetAttributeViInt32Response response;
  ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);
  ViInt32 get_attribute_value = get_int32_attribute(channel_name, attribute_to_set);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDmmDriverApiTest, SetViBooleanAttribute_GetViBooleanAttribute_ValueMatchesSetValue)
{
  const char* channel_name = "";
  const dmm::NiDmmAttribute attribute_to_set = dmm::NiDmmAttribute::NIDMM_ATTRIBUTE_SIMULATE;
  const ViBoolean expected_value = true;
  ::grpc::ClientContext context;
  dmm::SetAttributeViBooleanRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value(expected_value);
  dmm::SetAttributeViBooleanResponse response;
  ::grpc::Status status = GetStub()->SetAttributeViBoolean(&context, request, &response);
  ViBoolean get_attribute_value = get_bool_attribute(channel_name, attribute_to_set);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiDmmDriverApiTest, ConfigureMeasurementAbsolute_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::ConfigureMeasurementAbsoluteRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_measurement_function(dmm::Function::FUNCTION_NIDMM_VAL_DC_VOLTS);
  request.set_range(10);
  request.set_resolution_absolute(5.5);
  dmm::ConfigureMeasurementAbsoluteResponse response;
  ::grpc::Status status = GetStub()->ConfigureMeasurementAbsolute(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiDmmDriverApiTest, ConfigureCurrentSourse_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::ConfigureCurrentSourceRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_current_source(0.0001);
  dmm::ConfigureCurrentSourceResponse response;
  ::grpc::Status status = GetStub()->ConfigureCurrentSource(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiDmmDriverApiTest, ExportConfiguredCurrentSource_ResetAndImportConfiguration_CurrentSourceConfigurationIsImported)
{
  double expected_value = 0.0001;
  configure_current_source(expected_value);
  auto exported_configuration_response = export_attribute_configuration_buffer();

  reset();
  import_attribute_configuration_buffer(exported_configuration_response);

  double set_value = get_real64_attribute("", dmm::NiDmmAttribute::NIDMM_ATTRIBUTE_CURRENT_SOURCE);
  EXPECT_EQ(expected_value, set_value);
}

TEST_F(NiDmmDriverApiTest, ConfiguredTrigger_ConfiguresSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::ConfigureTriggerRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_trigger_source(dmm::TriggerSource::TRIGGER_SOURCE_NIDMM_VAL_SOFTWARE_TRIG);
  request.set_trigger_delay(dmm::TriggerDelays::TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_ON);
  dmm::ConfigureTriggerResponse response;
  ::grpc::Status status = GetStub()->ConfigureTrigger(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiDmmDriverApiTest, AcquireMeasurement_CompletesSuccesfully)
{
  ::grpc::ClientContext context;
  dmm::ReadRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_maximum_time_raw(1000);
  dmm::ReadResponse response;
  ::grpc::Status status = GetStub()->Read(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_NE(0, response.reading());
}

TEST_F(NiDmmDriverApiTest, SelfCalibrate_CompletesSuccessfully)
{
  ::grpc::ClientContext context;
  dmm::SelfCalRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  dmm::SelfCalResponse response;
  ::grpc::Status status = GetStub()->SelfCal(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nidmm_session_tests.cpp sha256=8d181727c3faeb651255f283ef948d47381230b543e4e3e47a726f152155a249 bytes=4357 -->
## FILE: source/tests/system/nidmm_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nidmm_session_tests.cpp`
- sha256: `8d181727c3faeb651255f283ef948d47381230b543e4e3e47a726f152155a249`
- bytes: 4357

````cpp
#include <gmock/gmock.h>

#include "device_server.h"
#include "nidmm/nidmm_client.h"
#include "nidmm/nidmm_library.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace dmm = nidmm_grpc;
using namespace ::testing;

const int kViErrorDmmRsrcNFound = -1074118656;
const int kInvalidDmmSession = -1074130544;
const char* kViErrorDmmRsrcNFoundMessage = "Device was not recognized. The device is not supported with this driver or version.\n\nInvalid Identifier: ";
const char* kInvalidDmmSessionMessage = "The session handle is not valid.";
const char* kResourceName = "FakeDevice";
const char* kDmmOptionsString = "Simulate=1, DriverSetup=Model:4080; BoardType:PXIe";
const char* kSessionName = "SessionName";
const char* kInvalidRsrc = "";

class NiDmmSessionTest : public ::testing::Test {
 protected:
  NiDmmSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nidmm_stub_(dmm::NiDmm::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiDmmSessionTest() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  std::unique_ptr<dmm::NiDmm::Stub>& GetStub()
  {
    return nidmm_stub_;
  }

  ::grpc::Status call_init_with_options(const char* resource_name, const char* option_string, const char* session_name, dmm::InitWithOptionsResponse* response)
  {
    ::grpc::ClientContext context;
    dmm::InitWithOptionsRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);
    request.set_reset_device(false);
    request.set_id_query(false);

    ::grpc::Status status = GetStub()->InitWithOptions(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<dmm::NiDmm::Stub> nidmm_stub_;
};

TEST_F(NiDmmSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  dmm::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kResourceName, kDmmOptionsString, kSessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDmmSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  dmm::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kResourceName, kDmmOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiDmmSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  dmm::InitWithOptionsResponse init_response;
  call_init_with_options(kResourceName, kDmmOptionsString, kSessionName, &init_response);
  nidevice_grpc::Session session = init_response.vi();

  ::grpc::ClientContext context;
  dmm::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  dmm::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiDmmSessionTest, InvalidSession_CloseSession_ReturnsInvalidSesssionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    ::grpc::ClientContext context;
    dmm::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    dmm::CloseResponse response;
    ::grpc::Status status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidDmmSession, kInvalidDmmSessionMessage);
}

TEST_F(NiDmmSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    dmm::InitWithOptionsResponse init_response;
    call_init_with_options(kInvalidRsrc, "", "", &init_response);
  }, kViErrorDmmRsrcNFound, kViErrorDmmRsrcNFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nifgen_driver_api_tests.cpp sha256=0cb0cecef1f332176847f403e2ded8ed8a8df0c30386d6b684459326417faf1e bytes=24204 -->
## FILE: source/tests/system/nifgen_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nifgen_driver_api_tests.cpp`
- sha256: `0cb0cecef1f332176847f403e2ded8ed8a8df0c30386d6b684459326417faf1e`
- bytes: 24204

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nifgen/nifgen_client.h"
#include "tests/utilities/test_helpers.h"
#include "waveform_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace fgen = nifgen_grpc;

typedef ::google::protobuf::int16 int16;
typedef ::google::protobuf::int32 int32;
typedef ::google::protobuf::int64 int64;
typedef ::google::protobuf::uint32 uint32;
typedef ::google::protobuf::uint16 uint16;

const int kFgenDriverApiSuccess = 0;

class NiFgenDriverApiTest : public ::testing::Test {
 protected:
  NiFgenDriverApiTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nifgen_stub_(fgen::NiFgen::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiFgenDriverApiTest() {}

  void SetUp() override
  {
    initialize_driver_session();
  }

  void TearDown() override
  {
    close_driver_session();
  }

  std::unique_ptr<fgen::NiFgen::Stub>& GetStub()
  {
    return nifgen_stub_;
  }

  std::string GetSessionName()
  {
    return driver_session_->name();
  }

  void expect_api_success(int error_status)
  {
    EXPECT_EQ(kFgenDriverApiSuccess, error_status) << get_error_message(error_status);
  }

  void initialize_driver_session()
  {
    ::grpc::ClientContext context;
    fgen::InitializeWithChannelsRequest request;
    request.set_channel_name("");
    request.set_resource_name("FakeDevice");
    request.set_option_string("Simulate=1, DriverSetup=Model:5441;BoardType:PXI");
    request.set_reset_device(false);
    fgen::InitializeWithChannelsResponse response;

    ::grpc::Status status = GetStub()->InitializeWithChannels(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    driver_session_ = std::make_unique<nidevice_grpc::Session>(response.vi());

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void initiate()
  {
    fgen::InitiateGenerationRequest request;
    fgen::InitiateGenerationResponse response;
    ::grpc::ClientContext context;
    request.mutable_vi()->set_name(GetSessionName());

    ::grpc::Status status = GetStub()->InitiateGeneration(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void close_driver_session()
  {
    if (!driver_session_) {
      return;
    }

    ::grpc::ClientContext context;
    fgen::CloseRequest request;
    request.mutable_vi()->set_name(driver_session_->name());
    fgen::CloseResponse response;

    ::grpc::Status status = GetStub()->Close(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  std::string get_error_message(int error_status)
  {
    ::grpc::ClientContext context;
    fgen::ErrorHandlerRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_error_code(error_status);
    fgen::ErrorHandlerResponse response;
    ::grpc::Status status = GetStub()->ErrorHandler(&context, request, &response);

    EXPECT_TRUE(status.ok());
    EXPECT_EQ(kFgenDriverApiSuccess, response.status());

    return response.error_message();
  }

  bool get_bool_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    fgen::GetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    fgen::GetAttributeViBooleanResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViBoolean(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  int32 get_int32_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    fgen::GetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    fgen::GetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt32(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  int64 get_int64_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    fgen::GetAttributeViInt64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    fgen::GetAttributeViInt64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViInt64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  double get_real64_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    fgen::GetAttributeViReal64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    fgen::GetAttributeViReal64Response response;

    ::grpc::Status status = GetStub()->GetAttributeViReal64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  std::string get_string_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id)
  {
    ::grpc::ClientContext context;
    fgen::GetAttributeViStringRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    fgen::GetAttributeViStringResponse response;

    ::grpc::Status status = GetStub()->GetAttributeViString(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.attribute_value();
  }

  void set_int32_attribute(const char* channel_list, fgen::NiFgenAttribute attribute_id, fgen::NiFgenInt32AttributeValues attribute_value)
  {
    ::grpc::ClientContext context;
    fgen::SetAttributeViInt32Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_list);
    request.set_attribute_id(attribute_id);
    request.set_attribute_value(attribute_value);
    fgen::SetAttributeViInt32Response response;

    ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void set_bool_attribute(const char* channel_name, fgen::NiFgenAttribute attribute, bool value)
  {
    ::grpc::ClientContext context;
    fgen::SetAttributeViBooleanRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_attribute_id(attribute);
    request.set_attribute_value(value);
    fgen::SetAttributeViBooleanResponse response;

    ::grpc::Status status = GetStub()->SetAttributeViBoolean(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void configure_trigger_mode(const char* channel_name, fgen::TriggerMode trigger_mode)
  {
    ::grpc::ClientContext context;
    fgen::ConfigureTriggerModeRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_trigger_mode(trigger_mode);
    fgen::ConfigureTriggerModeResponse response;

    ::grpc::Status status = GetStub()->ConfigureTriggerMode(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  fgen::ExportAttributeConfigurationBufferResponse export_attribute_configuration_buffer()
  {
    ::grpc::ClientContext context;
    fgen::ExportAttributeConfigurationBufferRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    fgen::ExportAttributeConfigurationBufferResponse response;

    ::grpc::Status status = GetStub()->ExportAttributeConfigurationBuffer(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response;
  }

  void import_attribute_configuration_buffer(fgen::ExportAttributeConfigurationBufferResponse export_buffer_response)
  {
    ::grpc::ClientContext context;
    fgen::ImportAttributeConfigurationBufferRequest import_request;
    import_request.mutable_vi()->set_name(GetSessionName());
    auto exported_configuration = export_buffer_response.configuration();
    import_request.mutable_configuration()->append(exported_configuration.begin(), exported_configuration.end());
    fgen::ImportAttributeConfigurationBufferResponse import_response;

    ::grpc::Status status = GetStub()->ImportAttributeConfigurationBuffer(&context, import_request, &import_response);

    EXPECT_TRUE(status.ok());
    expect_api_success(import_response.status());
  }

  void reset()
  {
    ::grpc::ClientContext context;
    fgen::ResetRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    fgen::ResetResponse response;

    ::grpc::Status status = GetStub()->Reset(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  void configure_output_mode(const char* channel_name, fgen::OutputMode output_mode)
  {
    ::grpc::ClientContext context;
    fgen::ConfigureOutputModeRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_output_mode(output_mode);
    fgen::ConfigureOutputModeResponse response;

    ::grpc::Status status = GetStub()->ConfigureOutputMode(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  int32 create_arb_waveform(const char* channel_name)
  {
    ::grpc::ClientContext context;
    fgen::CreateWaveformF64Request request;
    const double waveform_data_array[] = {1, 0, 0, 1};
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    for (double waveform_data : waveform_data_array) {
      request.add_waveform_data_array(waveform_data);
    }
    fgen::CreateWaveformF64Response response;

    ::grpc::Status status = GetStub()->CreateWaveformF64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.waveform_handle();
  }

  int create_advanced_arb_sequence(int32 sequence_length, int32* waveform_handles_array, int32* loop_counts_array, int32* marker_location_array)
  {
    ::grpc::ClientContext context;
    fgen::CreateAdvancedArbSequenceRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.mutable_waveform_handles_array()->Add(waveform_handles_array, waveform_handles_array + sequence_length);
    request.mutable_loop_counts_array()->Add(loop_counts_array, loop_counts_array + sequence_length);
    request.mutable_marker_location_array()->Add(marker_location_array, marker_location_array + sequence_length);
    fgen::CreateAdvancedArbSequenceResponse response;

    ::grpc::Status status = GetStub()->CreateAdvancedArbSequence(&context, request, &response);

    EXPECT_TRUE(status.ok());
    return response.status();
  }

  void allocate_named_waveform(std::string channel_name, std::string waveform_name, int waveform_size)
  {
    ::grpc::ClientContext context;
    fgen::AllocateNamedWaveformRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_waveform_name(waveform_name);
    request.set_waveform_size(waveform_size);
    fgen::AllocateNamedWaveformResponse response;

    ::grpc::Status status = GetStub()->AllocateNamedWaveform(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
  }

  int32 write_named_waveform_f64(std::string channel_name, std::string waveform_name, int waveform_size, double waveform[])
  {
    ::grpc::ClientContext context;
    fgen::WriteNamedWaveformF64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_waveform_name(waveform_name);
    request.mutable_data()->CopyFrom(google::protobuf::RepeatedField<double>(waveform, waveform + waveform_size));
    fgen::WriteNamedWaveformF64Response response;

    ::grpc::Status status = GetStub()->WriteNamedWaveformF64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    return response.status();
  }

  int32 allocate_waveform(std::string channel_name, int waveform_size)
  {
    ::grpc::ClientContext context;
    fgen::AllocateWaveformRequest request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_waveform_size(waveform_size);
    fgen::AllocateWaveformResponse response;

    ::grpc::Status status = GetStub()->AllocateWaveform(&context, request, &response);

    EXPECT_TRUE(status.ok());
    expect_api_success(response.status());
    return response.waveform_handle();
  }

  int32 write_waveform_complexf64(std::string channel_name, int waveform_size, int waveform_handle, std::vector<nidevice_grpc::NIComplexNumber> waveform)
  {
    ::grpc::ClientContext context;
    fgen::WriteWaveformComplexF64Request request;
    request.mutable_vi()->set_name(GetSessionName());
    request.set_channel_name(channel_name);
    request.set_waveform_handle(waveform_handle);
    for (int i = 0; i < waveform_size; i++) {
      request.mutable_data()->Add();
      request.mutable_data(i)->set_imaginary(waveform[i].imaginary());
      request.mutable_data(i)->set_real(waveform[i].real());
    }
    fgen::WriteWaveformComplexF64Response response;

    ::grpc::Status status = GetStub()->WriteWaveformComplexF64(&context, request, &response);

    EXPECT_TRUE(status.ok());
    return response.status();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<::nidevice_grpc::Session> driver_session_;
  std::unique_ptr<fgen::NiFgen::Stub> nifgen_stub_;
};

std::vector<nidevice_grpc::NIComplexNumber> complex_number_array(
    std::vector<double> reals,
    std::vector<double> imaginaries)
{
  return complex_array<double, nidevice_grpc::NIComplexNumber>(reals, imaginaries);
}

TEST_F(NiFgenDriverApiTest, PerformSelfTest_CompletesSuccessfuly)
{
  ::grpc::ClientContext context;
  fgen::SelfTestRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  fgen::SelfTestResponse response;
  ::grpc::Status status = GetStub()->SelfTest(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
  EXPECT_EQ(0, response.self_test_result());
  EXPECT_EQ("", response.self_test_message());
}

TEST_F(NiFgenDriverApiTest, PerformReset_CompletesSuccessfuly)
{
  ::grpc::ClientContext context;
  fgen::ResetRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  fgen::ResetResponse response;
  ::grpc::Status status = GetStub()->Reset(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiFgenDriverApiTest, SetAttributeViInt32_GetAttributeViInt32_ValueMatches)
{
  const char* channel_name = "";
  const fgen::NiFgenAttribute attribute_to_set = fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_OUTPUT_MODE;
  const auto expected_value = fgen::NiFgenInt32AttributeValues::NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_ARB;
  ::grpc::ClientContext context;
  fgen::SetAttributeViInt32Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value(expected_value);
  fgen::SetAttributeViInt32Response response;
  ::grpc::Status status = GetStub()->SetAttributeViInt32(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  int32 get_attribute_value = get_int32_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiFgenDriverApiTest, SetAttributeViReal64_GetAttributeViReal64_ValueMatches)
{
  const char* channel_name = "";
  const fgen::NiFgenAttribute attribute_to_set = fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_DIGITAL_GAIN;
  const double expected_value = -1.0;
  ::grpc::ClientContext context;
  fgen::SetAttributeViReal64Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  fgen::SetAttributeViReal64Response response;
  ::grpc::Status status = GetStub()->SetAttributeViReal64(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  double get_attribute_value_sourcedelay = get_real64_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value_sourcedelay);
}

TEST_F(NiFgenDriverApiTest, SetAttributeViBoolean_GetAttributeViBoolean_ValueMatches)
{
  const char* channel_name = "0";
  const fgen::NiFgenAttribute attribute_to_set = fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_OUTPUT_ENABLED;
  const bool expected_value = true;
  set_bool_attribute(channel_name, attribute_to_set, expected_value);

  bool get_attribute_value = get_bool_attribute(channel_name, attribute_to_set);

  EXPECT_EQ(expected_value, get_attribute_value);
}

TEST_F(NiFgenDriverApiTest, SetAttributeViString_GetAttributeViString_ValueMatches)
{
  const char* channel_name = "";
  const fgen::NiFgenAttribute attribute_to_set = fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_TERMINAL;
  const std::string expected_value = "sample";
  ::grpc::ClientContext context;
  fgen::SetAttributeViStringRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  request.set_attribute_id(attribute_to_set);
  request.set_attribute_value_raw(expected_value);
  fgen::SetAttributeViStringResponse response;
  ::grpc::Status status = GetStub()->SetAttributeViString(&context, request, &response);
  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());

  std::string get_attribute_value = get_string_attribute(channel_name, attribute_to_set);

  EXPECT_STREQ(expected_value.c_str(), get_attribute_value.c_str());
}

TEST_F(NiFgenDriverApiTest, ConfigureTriggerMode_ConfiguresSuccessfully)
{
  const char* channel_name = "0";
  int32 expected_value = 2;  // NIFGEN_VAL_CONTINUOUS
  configure_trigger_mode(channel_name, fgen::TriggerMode::TRIGGER_MODE_NIFGEN_VAL_CONTINUOUS);

  int32 actual_trigger_mode = get_int32_attribute(channel_name, fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_TRIGGER_MODE);
  EXPECT_EQ(expected_value, actual_trigger_mode);
}

TEST_F(NiFgenDriverApiTest, ResetInterchangeCheck_ResetsSuccessfully)
{
  const char* channel_name = "0";
  double expected_current_level = 3.0;
  ::grpc::ClientContext context;
  fgen::ResetInterchangeCheckRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  fgen::ResetInterchangeCheckResponse response;
  ::grpc::Status status = GetStub()->ResetInterchangeCheck(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiFgenDriverApiTest, SendSoftwareEdgeTrigger_TriggersSuccessfully)
{
  ::grpc::ClientContext context;
  fgen::SendSoftwareEdgeTriggerRequest request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_trigger(fgen::Trigger::TRIGGER_NIFGEN_VAL_SCRIPT_TRIGGER);
  request.set_trigger_id("ScriptTrigger0");
  fgen::SendSoftwareEdgeTriggerResponse response;
  ::grpc::Status status = GetStub()->SendSoftwareEdgeTrigger(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

TEST_F(NiFgenDriverApiTest, AllocateNamedWaveform_WriteNamedWaveformF64_WaveformWrittenSuccessfully)
{
  std::string channel_name = "0";
  std::string waveform_name = "TestWaveform";
  int waveform_size = 5;
  configure_output_mode(channel_name.c_str(), fgen::OutputMode::OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SCRIPT);
  allocate_named_waveform(channel_name, waveform_name, waveform_size);

  double waveform[] = {1.55, 40.4, 21.6, 0.7, 15.89};
  int32 status = write_named_waveform_f64(channel_name, waveform_name, waveform_size, waveform);

  expect_api_success(status);
}

TEST_F(NiFgenDriverApiTest, ExportTriggerMode_ResetAndImportConfiguration_TriggerModeConfigurationIsImported)
{
  const char* channel_name = "0";
  int32 expected_trigger_mode = 1;  // NIFGEN_VAL_SINGLE
  configure_trigger_mode(channel_name, fgen::TriggerMode::TRIGGER_MODE_NIFGEN_VAL_SINGLE);
  auto exported_configuration_response = export_attribute_configuration_buffer();

  reset();
  import_attribute_configuration_buffer(exported_configuration_response);

  double set_trigger_mode = get_int32_attribute(channel_name, fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_TRIGGER_MODE);
  EXPECT_EQ(expected_trigger_mode, set_trigger_mode);
}

TEST_F(NiFgenDriverApiTest, AllocateWaveform_WriteWaveformComplexF64_WaveformWrittenSuccessfully)
{
#ifndef WIN32
  GTEST_SKIP() << "The Onboard Signal Processing (OSP) functionality of the PXI-5441 is not supported on Linux.";
#endif
  std::string channel_name = "0";
  int waveform_size = 5;
  configure_output_mode(channel_name.c_str(), fgen::OutputMode::OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB);
  int waveform_handle = allocate_waveform(channel_name, waveform_size);

  set_bool_attribute(channel_name.c_str(), fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_OSP_ENABLED, true);
  set_int32_attribute(channel_name.c_str(), fgen::NiFgenAttribute::NIFGEN_ATTRIBUTE_OSP_DATA_PROCESSING_MODE, fgen::NiFgenInt32AttributeValues::NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_COMPLEX);
  int32 status = write_waveform_complexf64(channel_name, waveform_size, waveform_handle, complex_number_array({1.55, 40.4, 21.6, 0.7, 15.89}, {2.3, -20.4, 112.4, -100.3, 0.0}));

  expect_api_success(status);
}

TEST_F(NiFgenDriverApiTest, OutputModeConfiguredToSeq_CreateAdvancedArbSequenceForArbitraryWaveform_CreatesSuccessfully)
{
  const char* channel_name = "0";
  int32 sequence_length = 1;
  int32 waveform_handles_array[1];
  int32 loop_counts_array[] = {1};
  int32 marker_location_array[] = {-1};
  configure_output_mode(channel_name, fgen::OutputMode::OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SEQ);

  waveform_handles_array[0] = create_arb_waveform(channel_name);
  int status = create_advanced_arb_sequence(sequence_length, waveform_handles_array, loop_counts_array, marker_location_array);

  expect_api_success(status);
}

TEST_F(NiFgenDriverApiTest, OutputModeConfiguredToArb_CreateWaveformI16_CreatesSuccessfully)
{
  const char* channel_name = "0";
  const int16 waveform_data_array[] = {0, 1, 0, 1};
  configure_output_mode(channel_name, fgen::OutputMode::OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB);

  ::grpc::ClientContext context;
  fgen::CreateWaveformI16Request request;
  request.mutable_vi()->set_name(GetSessionName());
  request.set_channel_name(channel_name);
  for (auto waveform_data : waveform_data_array) {
    request.add_waveform_data_array(waveform_data);
  }
  fgen::CreateWaveformI16Response response;
  ::grpc::Status status = GetStub()->CreateWaveformI16(&context, request, &response);

  EXPECT_TRUE(status.ok());
  expect_api_success(response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nifgen_session_tests.cpp sha256=d548575d3251f6c620e7c6ebf47b1ae9b11fa2a80d158718a48d3419f8334ba2 bytes=4955 -->
## FILE: source/tests/system/nifgen_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nifgen_session_tests.cpp`
- sha256: `d548575d3251f6c620e7c6ebf47b1ae9b11fa2a80d158718a48d3419f8334ba2`
- bytes: 4955

````cpp
#include <gmock/gmock.h>

#include "device_server.h"
#include "nifgen/nifgen_client.h"
#include "tests/utilities/test_helpers.h"

using namespace ::testing;

namespace ni {
namespace tests {
namespace system {

namespace fgen = nifgen_grpc;

const int kInvalidFgenRsrc = -1074134964;
const int kInvalidFgenSession = -1074130544;
const char* kViErrorFgenResourceNotFoundMessage = "IVI: (Hex 0xBFFA004C) The option string parameter contains an entry with an unknown option value.\n\nInvalid Identifier: ";
const char* kInvalidFgenSessionMessage = "The session handle is not valid.";
const char* kTestFgenRsrc = "FakeDevice";
const char* kFgenOptionsString = "Simulate=1, DriverSetup=Model:5433 (2CH); BoardType:PXIe";
const char* kFgenTestSession = "SessionName";
const char* kTestInvalidFgenRsrc = "";

class NiFgenSessionTest : public ::testing::Test {
 protected:
  NiFgenSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nifgen_stub_(fgen::NiFgen::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiFgenSessionTest() {}

  std::unique_ptr<fgen::NiFgen::Stub>& GetStub()
  {
    return nifgen_stub_;
  }

  ::grpc::Status call_init_with_options(const char* resource_name, const char* option_string, const char* session_name, fgen::InitWithOptionsResponse* response)
  {
    ::grpc::ClientContext context;
    fgen::InitWithOptionsRequest request;
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
    fgen::InitWithOptionsResponse init_response;
    call_init_with_options(kTestFgenRsrc, kFgenOptionsString, kFgenTestSession, &init_response);
    nidevice_grpc::Session session = init_response.vi();

    ::grpc::ClientContext context;
    fgen::ErrorMessageRequest request;
    request.mutable_vi()->set_name(session.name());
    request.set_error_code(error_status);
    fgen::ErrorMessageResponse error_response;

    ::grpc::Status status = GetStub()->ErrorMessage(&context, request, &error_response);
    EXPECT_TRUE(status.ok());
    return error_response.error_message();
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<fgen::NiFgen::Stub> nifgen_stub_;
};

TEST_F(NiFgenSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  fgen::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kTestFgenRsrc, kFgenOptionsString, kFgenTestSession, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiFgenSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  fgen::InitWithOptionsResponse response;
  ::grpc::Status status = call_init_with_options(kTestFgenRsrc, kFgenOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.vi().name());
}

TEST_F(NiFgenSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  fgen::InitWithOptionsResponse initialize_response;
  call_init_with_options(kTestFgenRsrc, kFgenOptionsString, kFgenTestSession, &initialize_response);
  nidevice_grpc::Session session = initialize_response.vi();

  ::grpc::ClientContext context;
  fgen::CloseRequest close_request;
  close_request.mutable_vi()->set_name(session.name());
  fgen::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiFgenSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    ::grpc::ClientContext context;
    fgen::CloseRequest request;
    request.mutable_vi()->set_name(session.name());
    fgen::CloseResponse response;
    auto status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidFgenSession, kInvalidFgenSessionMessage);
}

TEST_F(NiFgenSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    fgen::InitWithOptionsResponse initialize_response;
    call_init_with_options(kTestInvalidFgenRsrc, "", "", &initialize_response);
  }, kInvalidFgenRsrc, kViErrorFgenResourceNotFoundMessage);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nifpga_session_tests.cpp sha256=1466d67cf2f7279dedf6166a75a304dd99a9300b6effb083a97c20602734f733 bytes=3656 -->
## FILE: source/tests/system/nifpga_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nifpga_session_tests.cpp`
- sha256: `1466d67cf2f7279dedf6166a75a304dd99a9300b6effb083a97c20602734f733`
- bytes: 3656

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "enumerate_devices.h"
#include "nifpga/nifpga_client.h"

namespace ni {
namespace tests {
namespace system {

namespace nifpga = nifpga_grpc;

constexpr auto NIFPGA_ERROR_DEVICE_NOT_FOUND_MESSAGE = "Error";
static const char* kTestSessionName = "TestSession";
static const char* kEmptySessionName = "";
static const char* kInvalidRsrcName = "InvalidName";

inline static void EXPECT_FPGA_ERROR(const std::string& error_message, const ::grpc::Status& status)
{
  EXPECT_EQ(::grpc::StatusCode::UNKNOWN, status.error_code());
  EXPECT_EQ(error_message, status.error_message());
}

class NiFpgaSessionTest : public ::testing::Test {
 protected:
  std::string test_resource_name;

  NiFpgaSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nifpga_stub_(nifpga::NiFpga::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  void SetUp() override
  {
    for (const auto& device : EnumerateDevices()) {
      if ((device.model() == "NI PXIe-7976R")) {
        test_resource_name = device.name();
        break;
      }
    }

    if (test_resource_name.empty()) {
      GTEST_SKIP() << "No device found";
    }
  }

  virtual ~NiFpgaSessionTest() {}

  std::unique_ptr<nifpga::NiFpga::Stub>& GetStub()
  {
    return nifpga_stub_;
  }

  ::grpc::Status call_open(const char* resource_name, const char* session_name, nifpga::OpenResponse* response)
  {
    ::grpc::ClientContext context;
    nifpga::OpenRequest request;
    request.set_session_name(session_name);
    request.set_bitfile("C:\\DemoExample.lvbitx");
    request.set_signature("9A28199F1CEAD0E4DD35AF2730C072A6");
    request.set_resource(resource_name);
    request.set_attribute_raw(0);

    ::grpc::Status status = GetStub()->Open(&context, request, response);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<nifpga::NiFpga::Stub> nifpga_stub_;
};

TEST_F(NiFpgaSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  nifpga::OpenResponse response;
  ::grpc::Status status = call_open(test_resource_name.c_str(), kTestSessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
}

TEST_F(NiFpgaSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  nifpga::OpenResponse response;
  ::grpc::Status status = call_open(test_resource_name.c_str(), kEmptySessionName, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
}

TEST_F(NiFpgaSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  nifpga::OpenResponse response;
  ::grpc::Status status = call_open(kInvalidRsrcName, kTestSessionName, &response);

  EXPECT_FPGA_ERROR(NIFPGA_ERROR_DEVICE_NOT_FOUND_MESSAGE, status);
}

TEST_F(NiFpgaSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  nifpga::OpenResponse response;
  call_open(test_resource_name.c_str(), kTestSessionName, &response);
  nidevice_grpc::Session session = response.session();
  EXPECT_EQ(0, response.status());

  ::grpc::ClientContext context;
  nifpga::CloseRequest close_request;
  close_request.mutable_session()->set_name(session.name());
  close_request.set_attribute_raw(0);
  nifpga::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nimxlcterminaladaptor_restricted_driver_api_tests.cpp sha256=f28588917db42a3e54a1bf4c1808506a4f1d28f29db0be2f9eb03195a60ce042 bytes=2283 -->
## FILE: source/tests/system/nimxlcterminaladaptor_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nimxlcterminaladaptor_restricted_driver_api_tests.cpp`
- sha256: `f28588917db42a3e54a1bf4c1808506a4f1d28f29db0be2f9eb03195a60ce042`
- bytes: 2283

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nimxlcterminaladaptor_restricted/nimxlcterminaladaptor_restricted_client.h"

using namespace ::testing;
using namespace nimxlcterminaladaptor_restricted_grpc;
namespace client = nimxlcterminaladaptor_restricted_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

class NiMxLcTerminalAdaptorRestrictedDriverApiTests : public Test {
 protected:
  NiMxLcTerminalAdaptorRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nimxlcterminaladaptor_stub_(NimxlcTerminalAdaptorRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiMxLcTerminalAdaptorRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NimxlcTerminalAdaptorRestricted::Stub>& stub()
  {
    return nimxlcterminaladaptor_stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NimxlcTerminalAdaptorRestricted::Stub> nimxlcterminaladaptor_stub_;
};

nidevice_grpc::Session init_session(const client::StubPtr& stub)
{
  auto response = client::create_session(stub, "");
  EXPECT_EQ(0, response.status());
  EXPECT_EQ(0, response.c_status().code());
  auto session = response.handle();
  return session;
}

TEST_F(NiMxLcTerminalAdaptorRestrictedDriverApiTests, RefreshedTerminalCache_GetDeviceContainer_StatusOK)
{
  const auto session = init_session(stub());
  auto refresh_terminal_cache_response = client::refresh_terminal_cache(stub(), session);
  EXPECT_EQ(0, refresh_terminal_cache_response.status());
  EXPECT_EQ(0, refresh_terminal_cache_response.c_status().code());
  
  auto get_device_container_response = client::get_device_container(stub(), session);

  EXPECT_EQ(0, get_device_container_response.status());
  EXPECT_EQ(0, get_device_container_response.c_status().code());
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxbluetooth_driver_api_tests.cpp sha256=23882abd843ba18cc704bc4f97be78b08ee38b69a3db4f8c60ff352270b737df bytes=17867 -->
## FILE: source/tests/system/nirfmxbluetooth_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxbluetooth_driver_api_tests.cpp`
- sha256: `23882abd843ba18cc704bc4f97be78b08ee38b69a3db4f8c60ff352270b737df`
- bytes: 17867

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxbluetooth/nirfmxbluetooth_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"
#include "waveform_helpers.h"

using namespace ::testing;
using namespace nirfmxbluetooth_grpc;
namespace client = nirfmxbluetooth_grpc::experimental::client;
namespace nirfsa_client = nirfsa_grpc::experimental::client;

namespace nidevice_grpc {
// Needs to be in the nidevice_grpc namespace for googletest to find this
// because of argument-dependent lookup - see
// https://stackoverflow.com/questions/33371088/how-to-get-a-custom-operator-to-work-with-google-test
bool operator==(const NIComplexNumberF32& first, const NIComplexNumber& second)
{
  return first.real() == second.real() && first.imaginary() == second.imaginary();
}
}  // namespace nidevice_grpc

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5663E = "5663E";
constexpr auto PREAMBLE_BURST_SYNC_WARNING = 686280;
constexpr auto PREAMBLE_BURST_SYNC_WARNING_STR = "The Preamble Sync failed to detect start of the packet";
constexpr auto TYPE_MISMATCH_ERROR = -380251;
constexpr auto TYPE_MISMATCH_ERROR_STR = "Incorrect data type specified";

class NiRFmxBluetoothDriverApiTests : public Test {
 protected:
  NiRFmxBluetoothDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxBluetooth::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxBluetoothDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxBluetooth::Stub>& stub() const
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
  std::unique_ptr<NiRFmxBluetooth::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

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

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
}

nirfsa_grpc::InitWithOptionsResponse init_rfsa(const nirfsa_client::StubPtr& stub, const std::string& resource_name)
{
  return nirfsa_client::init_with_options(stub, resource_name, false, false, "Simulate=1, DriverSetup=Model:5663E");
}

nidevice_grpc::NIComplexNumber complex_number(
    const double real,
    const double imaginary)
{
  return complex<double, nidevice_grpc::NIComplexNumber>(real, imaginary);
}

TEST_F(NiRFmxBluetoothDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_RESPONSE_SUCCESS(init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxBluetoothDriverApiTests, Init_InitAgain_NewSessionInitializedValuesDiffer)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_RESPONSE_SUCCESS(init_response);
  EXPECT_TRUE(init_response.is_new_session());
  EXPECT_TRUE(init_response.new_session_initialized());

  auto init_response_2 = init(stub(), PXI_5663E);
  EXPECT_RESPONSE_SUCCESS(init_response_2);

  // 'is_new_session' comes from the driver and we expect that to be false since the same resource string and options were used.
  // 'new_session_initialized' should be true here, though, since a new grpc-device session name is used. This indicates when the
  // server calls the driver init method and a new mapping is created between the grpc-device session name and the session handle
  // returned from the driver.
  EXPECT_FALSE(init_response_2.is_new_session());
  EXPECT_TRUE(init_response_2.new_session_initialized());
}

TEST_F(NiRFmxBluetoothDriverApiTests, InitializeFromNIRFSA_Close_Succeeds)
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

TEST_F(NiRFmxBluetoothDriverApiTests, AcpBasicFromExample_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQPowerEdgeTriggerSlope::IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TriggerMinimumQuietTimeMode::TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQPowerEdgeTriggerLevelType::IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_packet_type(stub(), session, "", PacketType::PACKET_TYPE_DH1));
  EXPECT_SUCCESS(session, client::cfg_data_rate(stub(), session, "", 1000000));
  EXPECT_SUCCESS(session, client::cfg_payload_length(stub(), session, "", PayloadLengthMode::PAYLOAD_LENGTH_MODE_AUTO, 10));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_burst_synchronization_type(stub(), session, "", AcpBurstSynchronizationType::ACP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", AcpAveragingEnabled::ACP_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::acp_cfg_offset_channel_mode(stub(), session, "", AcpOffsetChannelMode::ACP_OFFSET_CHANNEL_MODE_SYMMETRIC));
  EXPECT_SUCCESS(session, client::acp_cfg_number_of_offsets(stub(), session, "", 5));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto reference_channel_power = client::acp_fetch_reference_channel_power(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, reference_channel_power);
  const auto measurement_response = client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, measurement_response);
  const auto mask_trace = client::acp_fetch_mask_trace(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, mask_trace);
  const auto absolute_power_trace = client::acp_fetch_absolute_power_trace(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, absolute_power_trace);
  const auto fetched_spectrum = client::acp_fetch_spectrum(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, fetched_spectrum);

  EXPECT_GT(reference_channel_power.reference_channel_power(), 0.0);
  EXPECT_THAT(measurement_response.lower_absolute_power(), Each(Ne(0.0)));
  EXPECT_THAT(measurement_response.upper_absolute_power(), Each(Ne(0.0)));
  EXPECT_THAT(measurement_response.lower_relative_power(), Each(Ne(0.0)));
  EXPECT_THAT(measurement_response.upper_relative_power(), Each(Ne(0.0)));
  EXPECT_GT(measurement_response.actual_array_size(), 0);
  EXPECT_EQ(mask_trace.x0(), 0.0);
  EXPECT_EQ(mask_trace.dx(), 0.0);
  EXPECT_THAT(mask_trace.limit_with_exception_mask(), Each(Ne(0.0)));
  EXPECT_THAT(mask_trace.limit_without_exception_mask(), Each(Ne(0.0)));
  EXPECT_EQ(mask_trace.actual_array_size(), 0);
  EXPECT_GT(absolute_power_trace.x0(), 0.0);
  EXPECT_GT(absolute_power_trace.dx(), 0.0);
  EXPECT_THAT(absolute_power_trace.absolute_power(), Each(Ne(0.0)));
  EXPECT_GT(absolute_power_trace.actual_array_size(), 0);
  EXPECT_GT(fetched_spectrum.x0(), 0.0);
  EXPECT_GT(fetched_spectrum.dx(), 0.0);
  EXPECT_THAT(fetched_spectrum.spectrum(), Each(Ne(0.0)));
  EXPECT_GT(fetched_spectrum.actual_array_size(), 0);
}

TEST_F(NiRFmxBluetoothDriverApiTests, TxpBasicFromExample_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 2.402000e9));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQPowerEdgeTriggerSlope::IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TriggerMinimumQuietTimeMode::TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQPowerEdgeTriggerLevelType::IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_packet_type(stub(), session, "", PacketType::PACKET_TYPE_DH1));
  EXPECT_SUCCESS(session, client::cfg_data_rate(stub(), session, "", 1000000));
  EXPECT_SUCCESS(session, client::cfg_payload_length(stub(), session, "", PayloadLengthMode::PAYLOAD_LENGTH_MODE_AUTO, 10));
  EXPECT_SUCCESS(session, client::cfg_le_direction_finding(stub(), session, "", DirectionFindingMode::DIRECTION_FINDING_MODE_DISABLED, 160e-6, 1e-6));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 10e-3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_TXP, true));
  EXPECT_SUCCESS(session, client::txp_cfg_burst_synchronization_type(stub(), session, "", TxpBurstSynchronizationType::TXP_BURST_SYNCHRONIZATION_TYPE_PREAMBLE));
  EXPECT_SUCCESS(session, client::txp_cfg_averaging(stub(), session, "", TxpAveragingEnabled::TXP_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  // We expect these actions to produce PREAMBLE_BURST_SYNC_WARNING since the test uses simulated hardware.
  const auto fetched_powers_response = client::txp_fetch_powers(stub(), session, "", 10.0);
  EXPECT_WARNING(PREAMBLE_BURST_SYNC_WARNING, PREAMBLE_BURST_SYNC_WARNING_STR, session, fetched_powers_response);
  const auto fetched_edr_powers_response = client::txp_fetch_edr_powers(stub(), session, "", 10.0);
  EXPECT_WARNING(PREAMBLE_BURST_SYNC_WARNING, PREAMBLE_BURST_SYNC_WARNING_STR, session, fetched_edr_powers_response);
  const auto fetched_lecte_reference_period_powers_response = client::txp_fetch_lecte_reference_period_powers(stub(), session, "", 10.0);
  EXPECT_WARNING(PREAMBLE_BURST_SYNC_WARNING, PREAMBLE_BURST_SYNC_WARNING_STR, session, fetched_lecte_reference_period_powers_response);

  EXPECT_GT(fetched_powers_response.average_power_mean(), 0.0);
  EXPECT_GT(fetched_powers_response.average_power_maximum(), 0.0);
  EXPECT_GT(fetched_powers_response.average_power_minimum(), 0.0);
  EXPECT_GT(fetched_powers_response.peak_to_average_power_ratio_maximum(), 0.0);
}

TEST_F(NiRFmxBluetoothDriverApiTests, ModAccMeasurement_FetchConstellationTrace_ComplexNumberLooksReasonable)
{
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 2.402000e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQPowerEdgeTriggerSlope::IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TriggerMinimumQuietTimeMode::TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQPowerEdgeTriggerLevelType::IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_packet_type(stub(), session, "", PacketType::PACKET_TYPE_2_DH1));
  EXPECT_SUCCESS(session, client::cfg_payload_length(stub(), session, "", PayloadLengthMode::PAYLOAD_LENGTH_MODE_AUTO, 10));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_burst_synchronization_type(stub(), session, "", ModAccBurstSynchronizationType::MODACC_BURST_SYNCHRONIZATION_TYPE_PREAMBLE));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", ModAccAveragingEnabled::MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  // We expect this action to produce PREAMBLE_BURST_SYNC_WARNING since the test uses simulated hardware.
  const auto constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.0);
  EXPECT_WARNING(PREAMBLE_BURST_SYNC_WARNING, PREAMBLE_BURST_SYNC_WARNING_STR, session, constellation_trace_response);

  // We expect the results to be empty since the measurement did not complete successfully.
  EXPECT_THAT(constellation_trace_response.constellation(), Each(Eq(complex_number(0.0, 0.0))));
  EXPECT_GT(constellation_trace_response.actual_array_size(), 0);
}

// Note: there aren't any i8 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxBluetoothDriverApiTests, SetAttributeInt8_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i8(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, 1));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u8(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, 1));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i8_array(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, {1, 0, -1, 0}));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u8_array(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, {1, 0, 1, 0}));
}

// Note: there aren't any i16 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxBluetoothDriverApiTests, SetAttributeInt16_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i16(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, -400));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u16(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, 400));
}

TEST_F(NiRFmxBluetoothDriverApiTests, SetAndGetAttributeInt32_Succeeds)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_TXP, true));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED, NiRFmxBluetoothInt32AttributeValues::NIRFMXBLUETOOTH_INT32_TXP_AVERAGING_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto txp_averaging_enabled = GET_ATTR_I32(session, "", NiRFmxBluetoothAttribute::NIRFMXBLUETOOTH_ATTRIBUTE_TXP_AVERAGING_ENABLED);

  EXPECT_EQ(NiRFmxBluetoothInt32AttributeValues::NIRFMXBLUETOOTH_INT32_TXP_AVERAGING_ENABLED_TRUE, txp_averaging_enabled);
}

TEST_F(NiRFmxBluetoothDriverApiTests, ConfigureTwentydBBandwidth_FetchMeasurements_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_TWENTY_DB_BANDWIDTH, true));
  EXPECT_SUCCESS(session, client::twentyd_b_bandwidth_cfg_averaging(stub(), session, "", TwentydBBandwidthAveragingEnabled::TWENTY_DB_BANDWIDTH_AVERAGING_ENABLED_FALSE, 10));

  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  const auto fetch_measurement_response = EXPECT_SUCCESS(session, client::twentyd_b_bandwidth_fetch_measurement(stub(), session, "", 10.0));
  const auto fetch_spectrum_response = EXPECT_SUCCESS(session, client::twentyd_b_bandwidth_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_NE(0.0, fetch_measurement_response.low_frequency());
  EXPECT_NE(0.0, fetch_measurement_response.peak_power());
  EXPECT_THAT(fetch_spectrum_response.spectrum(), Not(IsEmpty()));
  EXPECT_THAT(fetch_spectrum_response.spectrum(), Each(Ne(0.0)));
}

TEST_F(NiRFmxBluetoothDriverApiTests, BuildSlotString_ReturnsSlotString)
{
  const auto slot_string_response = client::build_slot_string(stub(), "", 25);

  EXPECT_EQ(slot_string_response.selector_string_out(), "slot25");
  EXPECT_RESPONSE_SUCCESS(slot_string_response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxbluetooth_session_tests.cpp sha256=c7e1f4a6b51d140ed9d6f34370ecb80dc93454ca26fab797672f54a431ea2580 bytes=7143 -->
## FILE: source/tests/system/nirfmxbluetooth_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxbluetooth_session_tests.cpp`
- sha256: `c7e1f4a6b51d140ed9d6f34370ecb80dc93454ca26fab797672f54a431ea2580`
- bytes: 7143

````cpp
#include "device_server.h"
#include "nirfmxbluetooth/nirfmxbluetooth_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxbluetooth = nirfmxbluetooth_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxBTSession = -380598;
const char* kRFmxBTTestRsrc = "FakeDevice";
const char* kRFmxBTOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxBTTestSessionOne = "SessionOneName";
const char* kRFmxBTTestSessionTwo = "SessionTwoName";
const char* kRFmxBTTestInvalidRsrc = "";

class NiRFmxBluetoothSessionTest : public ::testing::Test {
 protected:
  NiRFmxBluetoothSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxbluetooth_stub_(rfmxbluetooth::NiRFmxBluetooth::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxBluetoothSessionTest() {}

  std::unique_ptr<rfmxbluetooth::NiRFmxBluetooth::Stub>& GetStub()
  {
    return nirfmxbluetooth_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxbluetooth::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxbluetooth::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxbluetooth::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxbluetooth::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxbluetooth::NiRFmxBluetooth::Stub> nirfmxbluetooth_stub_;
};

TEST_F(NiRFmxBluetoothSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxbluetooth::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxBluetoothSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxbluetooth::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxBluetoothSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxbluetooth::InitializeResponse response;
    auto status = call_initialize(kRFmxBTTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxBluetoothSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxbluetooth::InitializeResponse init_response;
  call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxbluetooth::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxbluetooth::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxBluetoothSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxbluetooth::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxbluetooth::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxBluetoothSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxbluetooth::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxBTTestRsrc, kRFmxBTOptionsString, kRFmxBTTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxbluetooth::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxBTSession);
}

TEST_F(NiRFmxBluetoothSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxbluetooth::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxBTSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxcdma2k_driver_api_tests.cpp sha256=f3eb892c38320b20bfc87ddf7d1e0c22238bd9dcc3bf827526d461605a99826f bytes=26863 -->
## FILE: source/tests/system/nirfmxcdma2k_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxcdma2k_driver_api_tests.cpp`
- sha256: `f3eb892c38320b20bfc87ddf7d1e0c22238bd9dcc3bf827526d461605a99826f`
- bytes: 26863

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxcdma2k/nirfmxcdma2k_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxcdma2k_grpc;
namespace client = nirfmxcdma2k_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxCDMA2kDriverApiTests : public Test {
 protected:
  NiRFmxCDMA2kDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxCDMA2k::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxCDMA2kDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxCDMA2k::Stub>& stub() const
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
  std::unique_ptr<NiRFmxCDMA2k::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxCDMA2kDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxCDMA2kDriverApiTests, AcpFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_OFFSETS = 2;
  int32 autoLevel = 1;

  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.00));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 833.490e+6 ));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "", RF_ATTENUATION_AUTO_TRUE, 10.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,  DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  if(autoLevel)
  {
    EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", .02));
  }
  else
  {
    EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.00));
  }
  EXPECT_SUCCESS(session, client::cfg_band_class(stub(), session, "", 0 ));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_number_of_offsets(stub(), session, "", NUMBER_OF_OFFSETS ));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE ));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL ));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 1.67e-3 ));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS ));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto acp_fetch_offset_measurement_array_response = client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0);
  const auto acp_fetch_carrier_absolute_power_response = client::acp_fetch_carrier_absolute_power(stub(), session, "", 10.0);
  const auto acp_fetch_spectrum_response = client::acp_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, acp_fetch_offset_measurement_array_response);
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, acp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, acp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, acp_fetch_spectrum_response);
  EXPECT_NE(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(6719, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(6719, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, CdaFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,  DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_radio_configuration(stub(), session, "", RADIO_CONFIGURATION_RC3));
  EXPECT_SUCCESS(session, client::cfg_uplink_spreading(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CDA, true));
  EXPECT_SUCCESS(session, client::cda_cfg_synchronization_mode_and_interval(stub(), session, "", CDA_SYNCHRONIZATION_MODE_SLOT, 0 , 1));
  EXPECT_SUCCESS(session, client::cda_cfg_measurement_channel(stub(), session, "", 64, 0, CDA_MEASUREMENT_CHANNEL_BRANCH_I));
  EXPECT_SUCCESS(session, client::cda_cfg_power_unit(stub(), session, "", CDA_POWER_UNIT_DB));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto cda_fetch_code_domain_power_response = client::cda_fetch_code_domain_power(stub(), session, "", 10.0);
  const auto cda_fetch_code_domain_i_and_q_power_response = client::cda_fetch_code_domain_i_and_q_power(stub(), session, "", 10.0);
  const auto cda_fetch_symbol_evm_response = client::cda_fetch_symbol_evm(stub(), session, "", 10.0);
  const auto cda_fetch_iq_impairments_response = client::cda_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto cda_fetch_code_domain_i_and_q_power_trace_response = client::cda_fetch_code_domain_i_and_q_power_trace(stub(), session, "", 10.0);
  const auto cda_fetch_symbol_evm_trace_response = client::cda_fetch_symbol_evm_trace(stub(), session, "", 10.0);
  const auto cda_fetch_symbol_constellation_trace_response = client::cda_fetch_symbol_constellation_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, cda_fetch_code_domain_power_response);
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.total_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.total_active_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.mean_active_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.peak_active_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.mean_inactive_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.peak_inactive_power()));
  EXPECT_SUCCESS(session, cda_fetch_code_domain_i_and_q_power_response);
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.i_mean_active_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.q_mean_active_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.i_peak_inactive_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.q_peak_inactive_power()));
  EXPECT_SUCCESS(session, cda_fetch_symbol_evm_response);
  EXPECT_TRUE(isnan(cda_fetch_symbol_evm_response.rms_symbol_evm()));
  EXPECT_EQ(0.0, cda_fetch_symbol_evm_response.peak_symbol_evm());
  EXPECT_TRUE(isnan(cda_fetch_symbol_evm_response.rms_symbol_magnitude_error()));
  EXPECT_TRUE(isnan(cda_fetch_symbol_evm_response.rms_symbol_phase_error()));
  EXPECT_TRUE(isnan(cda_fetch_symbol_evm_response.mean_symbol_power()));
  EXPECT_NEAR(0.0, cda_fetch_symbol_evm_response.frequency_error(), 8000);
  EXPECT_NEAR(0, cda_fetch_symbol_evm_response.chip_rate_error(), 200);
  EXPECT_SUCCESS(session, cda_fetch_iq_impairments_response);
  EXPECT_TRUE(isnan(cda_fetch_iq_impairments_response.iq_origin_offset()));
  EXPECT_TRUE(isnan(cda_fetch_iq_impairments_response.iq_gain_imbalance()));
  EXPECT_TRUE(isnan(cda_fetch_iq_impairments_response.iq_quadrature_error()));
  EXPECT_SUCCESS(session, cda_fetch_code_domain_i_and_q_power_trace_response);
  EXPECT_EQ(64, cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers_size());
  EXPECT_EQ(64, cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers().size());
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers(0)));
  EXPECT_EQ(64, cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers_size());
  EXPECT_EQ(64, cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers().size());
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers(0)));
  EXPECT_SUCCESS(session, cda_fetch_symbol_evm_trace_response);
  EXPECT_EQ(24, cda_fetch_symbol_evm_trace_response.symbol_evm_size());
  EXPECT_EQ(24, cda_fetch_symbol_evm_trace_response.symbol_evm().size());
  EXPECT_TRUE(isnan(cda_fetch_symbol_evm_trace_response.symbol_evm(0)));
  EXPECT_SUCCESS(session, cda_fetch_symbol_constellation_trace_response);
  EXPECT_TRUE(isnan(cda_fetch_symbol_constellation_trace_response.symbol_constellation(0).real()));
  EXPECT_TRUE(isnan(cda_fetch_symbol_constellation_trace_response.symbol_constellation(0).imaginary()));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, ChpFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00 ));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.00, false ));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP, true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 1.670e-3 ));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS ));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_carrier_absolute_power_response = client::chp_fetch_carrier_absolute_power(stub(), session, "", 10.0);
  const auto chp_fetch_spectrum_response = client::chp_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, chp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, chp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, chp_fetch_spectrum_response);
  EXPECT_NE(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_EQ(3347, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(3347, chp_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, chp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, ModAccFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.00, false));
  EXPECT_SUCCESS(session, client::cfg_radio_configuration(stub(), session, "", RADIO_CONFIGURATION_RC3));
  EXPECT_SUCCESS(session, client::cfg_uplink_spreading(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_evm_response = client::mod_acc_fetch_evm(stub(), session, "", 10.0);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto mod_acc_fetch_peak_cde_response = client::mod_acc_fetch_peak_cde(stub(), session, "", 10.0);
  const auto mod_acc_fetch_peak_active_cde_response = client::mod_acc_fetch_peak_active_cde(stub(), session, "", 10.0);
  const auto mod_acc_fetch_constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.0);
  const auto mod_acc_fetch_evm_trace_response = client::mod_acc_fetch_evm_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, mod_acc_fetch_evm_response);
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_response.rms_evm()));
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_response.peak_evm()));
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_response.rho()));
  EXPECT_NEAR(0.0, mod_acc_fetch_evm_response.frequency_error(), 8000);
  EXPECT_NEAR(0, mod_acc_fetch_evm_response.chip_rate_error(), 200);  
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_response.rms_magnitude_error()));
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_response.rms_phase_error()));
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_TRUE(isnan(mod_acc_fetch_iq_impairments_response.iq_origin_offset()));
  EXPECT_TRUE(isnan(mod_acc_fetch_iq_impairments_response.iq_gain_imbalance()));
  EXPECT_TRUE(isnan(mod_acc_fetch_iq_impairments_response.iq_quadrature_error()));
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_cde_response);
  EXPECT_NE(0.0, mod_acc_fetch_peak_cde_response.peak_cde());
  EXPECT_EQ(31, mod_acc_fetch_peak_cde_response.peak_cde_walsh_code_number());
  EXPECT_EQ(1, mod_acc_fetch_peak_cde_response.peak_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_active_cde_response);
  EXPECT_TRUE(isinf(mod_acc_fetch_peak_active_cde_response.peak_active_cde()));
  EXPECT_EQ(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_walsh_code_length());
  EXPECT_EQ(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_walsh_code_number());
  EXPECT_EQ(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_TRUE(isnan(mod_acc_fetch_constellation_trace_response.constellation(0).real()));
  EXPECT_TRUE(isnan(mod_acc_fetch_constellation_trace_response.constellation(0).imaginary()));
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_EQ(1536, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_EQ(1536, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_trace_response.evm(0)));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, ObwFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00 ));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,  DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.00, false ));        
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 1.670e-3));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_measurement_response = client::obw_fetch_measurement(stub(), session, "", 10.0);
  const auto obw_fetch_spectrum_response = client::obw_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, obw_fetch_measurement_response);
  EXPECT_NEAR(72567.0, obw_fetch_measurement_response.occupied_bandwidth(), 100);
  EXPECT_NE(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_NEAR(833454000.0, obw_fetch_measurement_response.start_frequency(), 500);
  EXPECT_NEAR(833526000.0, obw_fetch_measurement_response.stop_frequency(), 500);
  EXPECT_SUCCESS(session, obw_fetch_spectrum_response);
  EXPECT_NE(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_EQ(5013, obw_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(5013, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, obw_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, QevmFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6 ));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00 ));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.00, false));
  EXPECT_SUCCESS(session, client::cfg_radio_configuration(stub(), session, "", RADIO_CONFIGURATION_RC3));
  EXPECT_SUCCESS(session, client::cfg_uplink_spreading(stub(), session, "", 0 ));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_QEVM, true));
  EXPECT_SUCCESS(session, client::qevm_cfg_averaging(stub(), session, "", QEVM_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::qevm_cfg_measurement_length(stub(), session, "", 1536));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto qevm_fetch_evm_response = client::qevm_fetch_evm(stub(), session, "", 10.0);
  const auto qevm_fetch_iq_impairments_response = client::qevm_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto qevm_fetch_evm_trace_response = client::qevm_fetch_evm_trace(stub(), session, "", 10.0);
  const auto qevm_fetch_constellation_trace_response = client::qevm_fetch_constellation_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, qevm_fetch_evm_response);
  EXPECT_TRUE(isnan(qevm_fetch_evm_response.mean_rms_evm()));
  EXPECT_EQ(0.0, qevm_fetch_evm_response.maximum_peak_evm());
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_frequency_error());
  EXPECT_TRUE(isnan(qevm_fetch_evm_response.mean_magnitude_error()));
  EXPECT_TRUE(isnan(qevm_fetch_evm_response.mean_phase_error()));
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_chip_rate_error());
  EXPECT_SUCCESS(session, qevm_fetch_iq_impairments_response);
  EXPECT_NE(0.0, qevm_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.mean_iq_gain_imbalance()));
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.mean_iq_quadrature_error()));
  EXPECT_NE(0.0, qevm_fetch_iq_impairments_response.maximum_iq_origin_offset());
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.maximum_iq_gain_imbalance()));
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.maximum_iq_quadrature_error()));
  EXPECT_SUCCESS(session, qevm_fetch_evm_trace_response);
  EXPECT_EQ(0.0, qevm_fetch_evm_trace_response.x0());
  EXPECT_NE(0.0, qevm_fetch_evm_trace_response.dx());
  EXPECT_NEAR(1503, qevm_fetch_evm_trace_response.evm_size(), 10);
  EXPECT_NEAR(1503, qevm_fetch_evm_trace_response.evm().size(), 10);
  EXPECT_TRUE(isnan(qevm_fetch_evm_trace_response.evm(0)));
  EXPECT_SUCCESS(session, qevm_fetch_constellation_trace_response);
  EXPECT_TRUE(isnan(qevm_fetch_constellation_trace_response.constellation(0).real()));
  EXPECT_TRUE(isnan(qevm_fetch_constellation_trace_response.constellation(0).imaginary()));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, SlotPhaseFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_SLOTS = 16;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,  DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_radio_configuration(stub(), session, "", RADIO_CONFIGURATION_RC3));
  EXPECT_SUCCESS(session, client::cfg_uplink_spreading(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPHASE, true));
  EXPECT_SUCCESS(session, client::slot_phase_cfg_synchronization_mode_and_interval(stub(), session, "", SLOT_PHASE_SYNCHRONIZATION_MODE_SLOT, 0 , NUMBER_OF_SLOTS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto slot_phase_fetch_maximum_phase_discontinuity_response = client::slot_phase_fetch_maximum_phase_discontinuity(stub(), session, "", 10.0);
  const auto slot_phase_fetch_phase_discontinuities_response = client::slot_phase_fetch_phase_discontinuities(stub(), session, "", 10.0);
  const auto slot_phase_fetch_chip_phase_error_trace_response = client::slot_phase_fetch_chip_phase_error_trace(stub(), session, "", 10.0);
  const auto slot_phase_fetch_chip_phase_error_linear_fit_trace_response = client::slot_phase_fetch_chip_phase_error_linear_fit_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, slot_phase_fetch_maximum_phase_discontinuity_response);
  EXPECT_EQ(0.0, slot_phase_fetch_maximum_phase_discontinuity_response.maximum_phase_discontinuity());
  EXPECT_SUCCESS(session, slot_phase_fetch_phase_discontinuities_response);
  EXPECT_EQ(16, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity_size());
  EXPECT_EQ(16, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity().size());
  EXPECT_TRUE(isnan(slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity(0)));
  EXPECT_SUCCESS(session, slot_phase_fetch_chip_phase_error_trace_response);
  EXPECT_EQ(0.0, slot_phase_fetch_chip_phase_error_trace_response.x0());
  EXPECT_NE(0.0, slot_phase_fetch_chip_phase_error_trace_response.dx());
  EXPECT_EQ(24576, slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error_size());
  EXPECT_EQ(24576, slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error().size());
  EXPECT_TRUE(isnan(slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error(0)));
  EXPECT_SUCCESS(session, slot_phase_fetch_chip_phase_error_linear_fit_trace_response);
  EXPECT_EQ(0.0, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.x0());
  EXPECT_NE(0.0, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.dx());
  EXPECT_EQ(24576, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit_size());
  EXPECT_EQ(24576, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit().size());
  EXPECT_EQ(0.0, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit(0));
}

TEST_F(NiRFmxCDMA2kDriverApiTests, SlotPowerFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_SLOTS = 16;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 833.490e+6, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0,  DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_radio_configuration(stub(), session, "", RADIO_CONFIGURATION_RC3));
  EXPECT_SUCCESS(session, client::cfg_uplink_spreading(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPOWER, true));
  EXPECT_SUCCESS(session, client::slot_power_cfg_synchronization_mode_and_interval(stub(), session, "", SLOT_POWER_SYNCHRONIZATION_MODE_SLOT, 0 , NUMBER_OF_SLOTS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto slot_power_fetch_powers_response = client::slot_power_fetch_powers(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, slot_power_fetch_powers_response);
  EXPECT_EQ(16, slot_power_fetch_powers_response.slot_power_size());
  EXPECT_EQ(16, slot_power_fetch_powers_response.slot_power().size());
  EXPECT_NE(0.0, slot_power_fetch_powers_response.slot_power(0));
  EXPECT_EQ(16, slot_power_fetch_powers_response.slot_power_delta_size());
  EXPECT_EQ(16, slot_power_fetch_powers_response.slot_power_delta().size());
  EXPECT_TRUE(isnan(slot_power_fetch_powers_response.slot_power_delta(0)));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxcdma2k_session_tests.cpp sha256=06b460fd338aea23911b72e4f3272471cdfa01c6b2df6d2f8df63e19c04d5fda bytes=7133 -->
## FILE: source/tests/system/nirfmxcdma2k_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxcdma2k_session_tests.cpp`
- sha256: `06b460fd338aea23911b72e4f3272471cdfa01c6b2df6d2f8df63e19c04d5fda`
- bytes: 7133

````cpp
#include "device_server.h"
#include "nirfmxcdma2k/nirfmxcdma2k_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxcdma2k = nirfmxcdma2k_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxCDMA2kSession = -380598;
const char* kRFmxCDMA2kTestRsrc = "FakeDevice";
const char* kRFmxCDMA2kOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxCDMA2kTestSessionOne = "SessionOneName";
const char* kRFmxCDMA2kTestSessionTwo = "SessionTwoName";
const char* kRFmxCDMA2kTestInvalidRsrc = "";

class NiRFmxCDMA2kSessionTest : public ::testing::Test {
 protected:
  NiRFmxCDMA2kSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxcdma2k_stub_(rfmxcdma2k::NiRFmxCDMA2k::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxCDMA2kSessionTest() {}

  std::unique_ptr<rfmxcdma2k::NiRFmxCDMA2k::Stub>& GetStub()
  {
    return nirfmxcdma2k_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxcdma2k::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxcdma2k::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxcdma2k::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxcdma2k::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxcdma2k::NiRFmxCDMA2k::Stub> nirfmxcdma2k_stub_;
};

TEST_F(NiRFmxCDMA2kSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxcdma2k::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxCDMA2kSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxcdma2k::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxCDMA2kSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxcdma2k::InitializeResponse response;
    call_initialize(kRFmxCDMA2kTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxCDMA2kSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxcdma2k::InitializeResponse init_response;
  call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxcdma2k::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxcdma2k::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxCDMA2kSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxcdma2k::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxcdma2k::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxCDMA2kSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxcdma2k::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxCDMA2kTestRsrc, kRFmxCDMA2kOptionsString, kRFmxCDMA2kTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxcdma2k::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxCDMA2kSession);

}

TEST_F(NiRFmxCDMA2kSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxcdma2k::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxCDMA2kSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxdemod_driver_api_tests.cpp sha256=6e945a25e469e04cd1222f1d3d9520d9dcbcc65982c054ce99f0b7319930ecd2 bytes=14062 -->
## FILE: source/tests/system/nirfmxdemod_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxdemod_driver_api_tests.cpp`
- sha256: `6e945a25e469e04cd1222f1d3d9520d9dcbcc65982c054ce99f0b7319930ecd2`
- bytes: 14062

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxdemod/nirfmxdemod_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxdemod_grpc;
namespace client = nirfmxdemod_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxDemodDriverApiTests : public Test {
 protected:
  NiRFmxDemodDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxDemod::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxDemodDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxDemod::Stub>& stub() const
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
  std::unique_ptr<NiRFmxDemod::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxDemodDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

// ADemod
TEST_F(NiRFmxDemodDriverApiTests, ADemodAMBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::a_demod_cfg_rbw_filter(stub(), session, "", 100.00e+3, A_DEMOD_RBW_FILTER_TYPE_FLAT, 0.1));
  EXPECT_SUCCESS(session, client::a_demod_cfg_measurement_interval(stub(), session, "", 10.00e-3 ));
  EXPECT_SUCCESS(session, client::a_demod_cfg_am_carrier_suppressed(stub(), session, "", A_DEMOD_AM_CARRIER_SUPPRESSED_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::a_demod_cfg_averaging(stub(), session, "", A_DEMOD_AVERAGING_ENABLED_FALSE, 10, A_DEMOD_AVERAGING_TYPE_LINEAR));

  const auto a_demod_read_am_response = client::a_demod_read_am(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, a_demod_read_am_response);
  NEAR(2.55532, a_demod_read_am_response.mean_carrier_power(), 0.5);
  NEAR(68.8951, a_demod_read_am_response.mean_modulation_depth(), 0.5);
}

TEST_F(NiRFmxDemodDriverApiTests, ADemodFMBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::a_demod_cfg_rbw_filter(stub(), session, "", 100.00e+3, A_DEMOD_RBW_FILTER_TYPE_FLAT, 0.1));
  EXPECT_SUCCESS(session, client::a_demod_cfg_measurement_interval(stub(), session, "", 10.00e-3 ));
  EXPECT_SUCCESS(session, client::a_demod_cfg_fm_de_emphasis(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::a_demod_cfg_averaging(stub(), session, "", A_DEMOD_AVERAGING_ENABLED_FALSE, 10, A_DEMOD_AVERAGING_TYPE_LINEAR));

  const auto a_demod_read_fm_response = client::a_demod_read_fm(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, a_demod_read_fm_response);
  NEAR(-487.5, a_demod_read_fm_response.mean_carrier_frequency_error(), 0.5);
  NEAR(7880.26, a_demod_read_fm_response.mean_deviation(), 0.5);
}

TEST_F(NiRFmxDemodDriverApiTests, ADemodPMBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::a_demod_cfg_rbw_filter(stub(), session, "", 100.00e+3, A_DEMOD_RBW_FILTER_TYPE_FLAT, 0.1));
  EXPECT_SUCCESS(session, client::a_demod_cfg_measurement_interval(stub(), session, "", 10.00e-3));
  EXPECT_SUCCESS(session, client::a_demod_cfg_carrier_correction(stub(), session, "", A_DEMOD_CARRIER_FREQUENCY_CORRECTION_ENABLED_TRUE, A_DEMOD_CARRIER_PHASE_CORRECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::a_demod_cfg_averaging(stub(), session, "", A_DEMOD_AVERAGING_ENABLED_FALSE, 10, A_DEMOD_AVERAGING_TYPE_LINEAR));

  const auto a_demod_read_pm_response = client::a_demod_read_pm(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, a_demod_read_pm_response);
  NEAR(-461.135, a_demod_read_pm_response.mean_carrier_frequency_error(), 0.5);
  NEAR(386.444, a_demod_read_pm_response.mean_deviation(), 0.5);
}

// DDemod
TEST_F(NiRFmxDemodDriverApiTests, DDemodASKBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::d_demod_cfg_modulation_type(stub(), session, "", D_DEMOD_MODULATION_TYPE_ASK, D_DEMOD_M_4, D_DEMOD_DIFFERENTIAL_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_symbol_rate(stub(), session, "", 100.000e+3));
  EXPECT_SUCCESS(session, client::d_demod_cfg_number_of_symbols(stub(), session, "", 1000));
  std::vector<float> empty_float_vec;  
  EXPECT_SUCCESS(session, client::d_demod_cfg_pulse_shaping_filter(stub(), session, "", D_DEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE, 0.50, 0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_measurement_filter(stub(), session, "", D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO, 0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_averaging(stub(), session, "", D_DEMOD_AVERAGING_ENABLED_FALSE, 10));

  const auto d_demod_read_response = client::d_demod_read(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, d_demod_read_response);
  NEAR(0, d_demod_read_response.mean_modulation_error_ratio(), 20);
  NEAR(135, d_demod_read_response.maximum_peak_evm(), 50);
  NEAR(60, d_demod_read_response.mean_rms_evm(), 20);
  NEAR(0, d_demod_read_response.mean_frequency_offset(), 2000);
}

TEST_F(NiRFmxDemodDriverApiTests, DDemodFSKBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK , 10.0e+6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_DDEMOD, true));
  EXPECT_SUCCESS(session, client::d_demod_cfg_modulation_type(stub(), session, "", D_DEMOD_MODULATION_TYPE_FSK, D_DEMOD_M_2, D_DEMOD_DIFFERENTIAL_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_fsk_deviation(stub(), session, "", 15.000e+3, D_DEMOD_FSK_REFERENCE_COMPENSATION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_symbol_rate(stub(), session, "", 100.000e+3));
  EXPECT_SUCCESS(session, client::d_demod_cfg_number_of_symbols(stub(), session, "", 1000));
  std::vector<float> empty_float_vec;
  EXPECT_SUCCESS(session, client::d_demod_cfg_pulse_shaping_filter(stub(), session, "", D_DEMOD_PULSE_SHAPING_FILTER_TYPE_GAUSSIAN, 0.50, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_measurement_filter(stub(), session, "", D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_averaging(stub(), session, "", D_DEMOD_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto d_demod_fetch_fsk_results_response = client::d_demod_fetch_fsk_results(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, d_demod_fetch_fsk_results_response);
  NEAR(17000, d_demod_fetch_fsk_results_response.mean_fsk_deviation(), 2000);
  NEAR(33000, d_demod_fetch_fsk_results_response.mean_rms_fsk_error(), 2000);
  NEAR(400000, d_demod_fetch_fsk_results_response.maximum_peak_fsk_error(), 100000);
}

TEST_F(NiRFmxDemodDriverApiTests, DDemodMSKBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::d_demod_cfg_modulation_type(stub(), session, "", D_DEMOD_MODULATION_TYPE_MSK, D_DEMOD_M_4, D_DEMOD_DIFFERENTIAL_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_symbol_rate(stub(), session, "", 100.000e+3));
  EXPECT_SUCCESS(session, client::d_demod_cfg_number_of_symbols(stub(), session, "", 1000));
  std::vector<float> empty_float_vec;
  EXPECT_SUCCESS(session, client::d_demod_cfg_pulse_shaping_filter(stub(), session, "", D_DEMOD_PULSE_SHAPING_FILTER_TYPE_GAUSSIAN, 0.50, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_measurement_filter(stub(), session, "", D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_averaging(stub(), session, "", D_DEMOD_AVERAGING_ENABLED_FALSE, 10));

  const auto d_demod_read_response = client::d_demod_read(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, d_demod_read_response);
  NEAR(0, d_demod_read_response.mean_modulation_error_ratio(), 50);
  NEAR(250, d_demod_read_response.maximum_peak_evm(), 50);
  NEAR(150, d_demod_read_response.mean_rms_evm(), 50);
  NEAR(0,  d_demod_read_response.mean_frequency_offset(), 50000);
}

TEST_F(NiRFmxDemodDriverApiTests, DDemodPSKBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::d_demod_cfg_modulation_type(stub(), session, "", D_DEMOD_MODULATION_TYPE_PSK, D_DEMOD_M_4, D_DEMOD_DIFFERENTIAL_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_psk_format(stub(), session, "", D_DEMOD_PSK_FORMAT_NORMAL));
  EXPECT_SUCCESS(session, client::d_demod_cfg_symbol_rate(stub(), session, "", 100.000e+3));
  EXPECT_SUCCESS(session, client::d_demod_cfg_number_of_symbols(stub(), session, "", 1000));
  std::vector<float> empty_float_vec;
  EXPECT_SUCCESS(session, client::d_demod_cfg_pulse_shaping_filter(stub(), session, "", D_DEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE, 0.50, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_measurement_filter(stub(), session, "", D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_averaging(stub(), session, "", D_DEMOD_AVERAGING_ENABLED_FALSE, 10));

  const auto d_demod_read_response = client::d_demod_read(stub(), session, "", 10.0);
  EXPECT_SUCCESS(session, d_demod_read_response);
  NEAR(0, d_demod_read_response.mean_modulation_error_ratio(), 100);
  NEAR(102, d_demod_read_response.maximum_peak_evm(), 50);
  NEAR(45, d_demod_read_response.mean_rms_evm(), 20);
  NEAR(0, d_demod_read_response.mean_frequency_offset(), 20);
}

TEST_F(NiRFmxDemodDriverApiTests, DDemodQAMBasicFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXDEMOD_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::d_demod_cfg_modulation_type(stub(), session, "", D_DEMOD_MODULATION_TYPE_QAM, D_DEMOD_M_16, D_DEMOD_DIFFERENTIAL_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::d_demod_cfg_symbol_rate(stub(), session, "", 100.000e+3));
  EXPECT_SUCCESS(session, client::d_demod_cfg_number_of_symbols(stub(), session, "", 1000));
  std::vector<float> empty_float_vec;
  EXPECT_SUCCESS(session, client::d_demod_cfg_pulse_shaping_filter(stub(), session, "", D_DEMOD_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE, 0.50, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_measurement_filter(stub(), session, "", D_DEMOD_MEASUREMENT_FILTER_TYPE_AUTO, 0.0, 1.0, empty_float_vec));
  EXPECT_SUCCESS(session, client::d_demod_cfg_averaging(stub(), session, "", D_DEMOD_AVERAGING_ENABLED_FALSE, 10));

  const auto d_demod_read_response = client::d_demod_read(stub(), session, "", 10.0);
  EXPECT_RESPONSE_WARNING(377702, d_demod_read_response);
  NEAR(0, d_demod_read_response.mean_modulation_error_ratio(), 100);
  NEAR(36, d_demod_read_response.maximum_peak_evm(), 20);
  NEAR(16, d_demod_read_response.mean_rms_evm(), 20);
  NEAR(0, d_demod_read_response.mean_frequency_offset(), 2000);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxdemod_session_tests.cpp sha256=eb1fac5763e5e618feb778fa96d6d7bbbd37cfdea4b16ec17168d5af5538fa06 bytes=7064 -->
## FILE: source/tests/system/nirfmxdemod_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxdemod_session_tests.cpp`
- sha256: `eb1fac5763e5e618feb778fa96d6d7bbbd37cfdea4b16ec17168d5af5538fa06`
- bytes: 7064

````cpp
#include "device_server.h"
#include "nirfmxdemod/nirfmxdemod_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxdemod = nirfmxdemod_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxDemodSession = -380598;
const char* kRFmxDemodTestRsrc = "FakeDevice";
const char* kRFmxDemodOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxDemodTestSessionOne = "SessionOneName";
const char* kRFmxDemodTestSessionTwo = "SessionTwoName";
const char* kRFmxDemodTestInvalidRsrc = "";

class NiRFmxDemodSessionTest : public ::testing::Test {
 protected:
  NiRFmxDemodSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxdemod_stub_(rfmxdemod::NiRFmxDemod::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxDemodSessionTest() {}

  std::unique_ptr<rfmxdemod::NiRFmxDemod::Stub>& GetStub()
  {
    return nirfmxdemod_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxdemod::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxdemod::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxdemod::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxdemod::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxdemod::NiRFmxDemod::Stub> nirfmxdemod_stub_;
};

TEST_F(NiRFmxDemodSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxdemod::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxDemodSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxdemod::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxDemodSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxdemod::InitializeResponse response;
    call_initialize(kRFmxDemodTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxDemodSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxdemod::InitializeResponse init_response;
  call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxdemod::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxdemod::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxDemodSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxdemod::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxdemod::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxDemodSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxdemod::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxDemodTestRsrc, kRFmxDemodOptionsString, kRFmxDemodTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxdemod::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxDemodSession);
}

TEST_F(NiRFmxDemodSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxdemod::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxDemodSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxgsm_driver_api_tests.cpp sha256=50431a683a4956d3df34089048e3287eb85400148c77bffe2976afcb07723683 bytes=35971 -->
## FILE: source/tests/system/nirfmxgsm_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxgsm_driver_api_tests.cpp`
- sha256: `50431a683a4956d3df34089048e3287eb85400148c77bffe2976afcb07723683`
- bytes: 35971

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxgsm/nirfmxgsm_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxgsm_grpc;
namespace client = nirfmxgsm_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxGSMDriverApiTests : public Test {
 protected:
  NiRFmxGSMDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxGSM::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxGSMDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxGSM::Stub>& stub() const
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
  std::unique_ptr<NiRFmxGSM::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxGSMDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxGSMDriverApiTests, EvmFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_TIMESLOTS = 1;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 890.2e6, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", NUMBER_OF_TIMESLOTS));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, "slot::all", MODULATION_TYPE_8PSK, BURST_TYPE_NB, HB_FILTER_WIDTH_NARROW));
  EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, "slot::all", TSC_TSC0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_evm_response = client::mod_acc_fetch_evm(stub(), session, "", 10.0);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto mod_acc_fetch_detected_tsc_array_response = client::mod_acc_fetch_detected_tsc_array(stub(), session, "", 10.0);
  const auto mod_acc_fetch_evm_trace_response = client::mod_acc_fetch_evm_trace(stub(), session, "", 10.0);
  const auto mod_acc_fetch_constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, mod_acc_fetch_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_rms_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.maximum_rms_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_peak_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.maximum_peak_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.ninety_fifth_percentile_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_frequency_error());
  EXPECT_NE(0, mod_acc_fetch_evm_response.peak_evm_symbol());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_origin_offset());
  EXPECT_SUCCESS(session, mod_acc_fetch_detected_tsc_array_response);
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc_size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc().size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.evm(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation_trace(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation_trace(0).imaginary());
}

TEST_F(NiRFmxGSMDriverApiTests, ModAccOrfsPvtCompositeFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_TIMESLOTS = 1;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 890.2e6, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", BAND_PGSM));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC | MEASUREMENT_TYPES_ORFS | MEASUREMENT_TYPES_PVT, true));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", NUMBER_OF_TIMESLOTS));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::orfs_cfg_averaging(stub(), session, "", ORFS_AVERAGING_ENABLED_FALSE, 10, ORFS_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::pvt_cfg_averaging(stub(), session, "", PVT_AVERAGING_ENABLED_FALSE, 10, PVT_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::orfs_cfg_measurement_type(stub(), session, "", ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING));
  EXPECT_SUCCESS(session, client::orfs_cfg_offset_frequency_mode(stub(), session, "", ORFS_OFFSET_FREQUENCY_MODE_STANDARD));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, "slot::all", MODULATION_TYPE_8PSK, BURST_TYPE_NB, HB_FILTER_WIDTH_NARROW));
  EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, "slot::all", TSC_TSC0));
  EXPECT_SUCCESS(session, client::cfg_power_control_level(stub(), session, "slot::all", 0));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_evm_response = client::mod_acc_fetch_evm(stub(), session, "", 10.0);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto mod_acc_fetch_detected_tsc_array_response = client::mod_acc_fetch_detected_tsc_array(stub(), session, "", 10.0);
  const auto mod_acc_fetch_pfer_response = client::mod_acc_fetch_pfer(stub(), session, "", 10.0);
  const auto orfs_fetch_modulation_results_array_response = client::orfs_fetch_modulation_results_array(stub(), session, "", 10.0);
  const auto orfs_fetch_switching_results_array_response = client::orfs_fetch_switching_results_array(stub(), session, "", 10.0);
  const auto pvt_fetch_slot_measurement_array_response = client::pvt_fetch_slot_measurement_array(stub(), session, "", 10.0);
  const auto pvt_fetch_measurement_status_response = client::pvt_fetch_measurement_status(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, mod_acc_fetch_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_rms_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.maximum_rms_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_peak_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.maximum_peak_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.ninety_fifth_percentile_evm());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.mean_frequency_error());
  EXPECT_NE(0, mod_acc_fetch_evm_response.peak_evm_symbol());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_origin_offset());
  EXPECT_SUCCESS(session, mod_acc_fetch_detected_tsc_array_response);
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc_size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc().size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_pfer_response);
  EXPECT_TRUE(isnan(mod_acc_fetch_pfer_response.mean_rms_phase_error()));
  EXPECT_TRUE(isnan(mod_acc_fetch_pfer_response.maximum_rms_phase_error()));
  EXPECT_TRUE(isnan(mod_acc_fetch_pfer_response.mean_peak_phase_error()));
  EXPECT_TRUE(isnan(mod_acc_fetch_pfer_response.maximum_peak_phase_error()));
  EXPECT_TRUE(isnan(mod_acc_fetch_pfer_response.mean_frequency_error()));
  EXPECT_EQ(-1, mod_acc_fetch_pfer_response.peak_symbol());
  EXPECT_SUCCESS(session, orfs_fetch_modulation_results_array_response);
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.modulation_carrier_power());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_relative_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.lower_relative_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_relative_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.upper_relative_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.lower_absolute_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, orfs_fetch_switching_results_array_response);
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.switching_carrier_power());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_relative_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.lower_relative_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_relative_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.upper_relative_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.lower_absolute_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, pvt_fetch_slot_measurement_array_response);
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_average_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_width(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status().size());
  EXPECT_EQ(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_maximum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_minimum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold(0));
  EXPECT_SUCCESS(session, pvt_fetch_measurement_status_response);
  EXPECT_EQ(0, pvt_fetch_measurement_status_response.measurement_status());
}

TEST_F(NiRFmxGSMDriverApiTests, MultiSlotPvtFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_SLOTS = 1;
  std::vector<int> slotConfigurationModulationType(NUMBER_OF_SLOTS);
  std::vector<int> slotConfigurationBurstType(NUMBER_OF_SLOTS);
  std::vector<int> slotConfigurationHBFilterWidth(NUMBER_OF_SLOTS);
  std::vector<int> slotConfigurationTSC(NUMBER_OF_SLOTS);
  std::vector<int> slotConfigurationPowerControlLevel(NUMBER_OF_SLOTS);
  for (int i = 0 ; i < NUMBER_OF_SLOTS; i++)
  {
    slotConfigurationModulationType[i] = NIRFMXGSM_INT32_MODULATION_TYPE_8PSK;
    slotConfigurationBurstType[i] = NIRFMXGSM_INT32_BURST_TYPE_NB;
    slotConfigurationHBFilterWidth[i] = NIRFMXGSM_INT32_HB_FILTER_WIDTH_NARROW;
    slotConfigurationTSC[i] = TSC_TSC0;
    slotConfigurationPowerControlLevel[i] = 0;
  }
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 890.2e6, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", BAND_PGSM));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", NUMBER_OF_SLOTS));
  for (int i = 0; i < NUMBER_OF_SLOTS; i++)
  {
    auto slot_string_response = client::build_slot_string(stub(), "", i);
    EXPECT_SUCCESS(session, slot_string_response);
    EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, slot_string_response.selector_string_out(), slotConfigurationModulationType[i], slotConfigurationBurstType[i], slotConfigurationHBFilterWidth[i]));
    EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, slot_string_response.selector_string_out(), slotConfigurationTSC[i]));
    EXPECT_SUCCESS(session, client::cfg_power_control_level(stub(), session, slot_string_response.selector_string_out(), slotConfigurationPowerControlLevel[i]));
  }
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_PVT, true));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXGSM_ATTRIBUTE_PVT_RBW_FILTER_BANDWIDTH, 500000.0));
  EXPECT_SUCCESS(session, client::pvt_cfg_averaging(stub(), session, "", PVT_AVERAGING_ENABLED_FALSE, 10, PVT_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto pvt_fetch_measurement_status_response = client::pvt_fetch_measurement_status(stub(), session, "", 10.0);
  const auto pvt_fetch_slot_measurement_array_response = client::pvt_fetch_slot_measurement_array(stub(), session, "", 10.0);
  const auto pvt_fetch_power_trace_response = client::pvt_fetch_power_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, pvt_fetch_measurement_status_response);
  EXPECT_EQ(0, pvt_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, pvt_fetch_slot_measurement_array_response);
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_average_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_width(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status().size());
  EXPECT_EQ(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_maximum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_minimum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold(0));
  EXPECT_SUCCESS(session, pvt_fetch_power_trace_response);
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.x0());
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.dx());
  EXPECT_NE(0, pvt_fetch_power_trace_response.upper_mask_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.upper_mask().size());
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.upper_mask(0));
  EXPECT_NE(0, pvt_fetch_power_trace_response.signal_power_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.signal_power().size());
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.signal_power(0));
  EXPECT_NE(0, pvt_fetch_power_trace_response.lower_mask_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.lower_mask().size());
  EXPECT_TRUE(isinf(pvt_fetch_power_trace_response.lower_mask(0)));
}

TEST_F(NiRFmxGSMDriverApiTests, OrfsFromExample_FetchData_DataLooksReasonable)
{
  const auto AUTO_LEVEL_ON = 1;
  int32 autoLevel = AUTO_LEVEL_ON;
  // TODO: Conversion process ignored auto_level_response.reference_level
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 890.2e6));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", 1));
  EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, "slot::all", MODULATION_TYPE_8PSK, BURST_TYPE_NB, HB_FILTER_WIDTH_NARROW));
  if(autoLevel)
  {
    EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 0.0046));
  }
  else
    EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, "slot::all", TSC_TSC0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ORFS, true));
  EXPECT_SUCCESS(session, client::orfs_cfg_noise_compensation_enabled(stub(), session, "", ORFS_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::orfs_cfg_measurement_type(stub(), session, "", ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING));
  EXPECT_SUCCESS(session, client::orfs_cfg_offset_frequency_mode(stub(), session, "", ORFS_OFFSET_FREQUENCY_MODE_STANDARD));
  EXPECT_SUCCESS(session, client::orfs_cfg_evaluation_symbols(stub(), session, "", 50.0, 0, 90.0));
  EXPECT_SUCCESS(session, client::orfs_cfg_averaging(stub(), session, "", ORFS_AVERAGING_ENABLED_FALSE, 10, ORFS_AVERAGING_TYPE_LOG));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto orfs_fetch_modulation_results_array_response = client::orfs_fetch_modulation_results_array(stub(), session, "", 10.0);
  const auto orfs_fetch_switching_results_array_response = client::orfs_fetch_switching_results_array(stub(), session, "", 10.0);
  const auto orfs_fetch_modulation_power_trace_response = client::orfs_fetch_modulation_power_trace(stub(), session, "", 10.0);
  const auto orfs_fetch_switching_power_trace_response = client::orfs_fetch_switching_power_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, orfs_fetch_modulation_results_array_response);
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.modulation_carrier_power());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_relative_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.lower_relative_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_relative_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.upper_relative_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.lower_absolute_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_results_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_results_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, orfs_fetch_switching_results_array_response);
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.switching_carrier_power());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_relative_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.lower_relative_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_relative_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.upper_relative_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.lower_absolute_power(0));
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_absolute_power_size());
  EXPECT_NE(0, orfs_fetch_switching_results_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_results_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, orfs_fetch_modulation_power_trace_response);
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.offset_frequency_size());
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.offset_frequency().size());
  EXPECT_EQ(0.0, orfs_fetch_modulation_power_trace_response.offset_frequency(0));
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.absolute_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_modulation_power_trace_response.absolute_power(0));
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.relative_power_size());
  EXPECT_NE(0, orfs_fetch_modulation_power_trace_response.relative_power().size());
  EXPECT_EQ(0.0, orfs_fetch_modulation_power_trace_response.relative_power(0));
  EXPECT_SUCCESS(session, orfs_fetch_switching_power_trace_response);
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.offset_frequency_size());
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.offset_frequency().size());
  EXPECT_EQ(0.0, orfs_fetch_switching_power_trace_response.offset_frequency(0));
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.absolute_power_size());
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.absolute_power().size());
  EXPECT_NE(0.0, orfs_fetch_switching_power_trace_response.absolute_power(0));
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.relative_power_size());
  EXPECT_NE(0, orfs_fetch_switching_power_trace_response.relative_power().size());
  EXPECT_EQ(0.0, orfs_fetch_switching_power_trace_response.relative_power(0));
}

TEST_F(NiRFmxGSMDriverApiTests, PferFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_TIMESLOTS = 1;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 890.2e6, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", NUMBER_OF_TIMESLOTS));
  EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, "slot::all", MODULATION_TYPE_GMSK, BURST_TYPE_NB, HB_FILTER_WIDTH_NARROW));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, "slot::all", TSC_TSC0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto mod_acc_fetch_pfer_response = client::mod_acc_fetch_pfer(stub(), session, "", 10.0);
  const auto mod_acc_fetch_detected_tsc_array_response = client::mod_acc_fetch_detected_tsc_array(stub(), session, "", 10.0);
  const auto mod_acc_fetch_phase_error_trace_response = client::mod_acc_fetch_phase_error_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.maximum_iq_origin_offset());
  EXPECT_SUCCESS(session, mod_acc_fetch_pfer_response);
  EXPECT_NE(0.0, mod_acc_fetch_pfer_response.mean_rms_phase_error());
  EXPECT_NE(0.0, mod_acc_fetch_pfer_response.maximum_rms_phase_error());
  EXPECT_NE(0.0, mod_acc_fetch_pfer_response.mean_peak_phase_error());
  EXPECT_NE(0.0, mod_acc_fetch_pfer_response.maximum_peak_phase_error());
  EXPECT_NE(0.0, mod_acc_fetch_pfer_response.mean_frequency_error());
  EXPECT_NE(0, mod_acc_fetch_pfer_response.peak_symbol());
  EXPECT_SUCCESS(session, mod_acc_fetch_detected_tsc_array_response);
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc_size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc().size());
  EXPECT_NE(0, mod_acc_fetch_detected_tsc_array_response.detected_tsc(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_phase_error_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_phase_error_trace_response.x0());
  EXPECT_NE(0.0, mod_acc_fetch_phase_error_trace_response.dx());
  EXPECT_NE(0, mod_acc_fetch_phase_error_trace_response.phase_error_size());
  EXPECT_NE(0, mod_acc_fetch_phase_error_trace_response.phase_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_phase_error_trace_response.phase_error(0));
}

TEST_F(NiRFmxGSMDriverApiTests, PvtFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_TIME_SLOTS = 1;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 890.2e6, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", BAND_PGSM));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 582e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_number_of_timeslots(stub(), session, "", NUMBER_OF_TIME_SLOTS));
  EXPECT_SUCCESS(session, client::cfg_auto_tsc_detection_enabled(stub(), session, "", AUTO_TSC_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::cfg_signal_type(stub(), session, "slot::all", MODULATION_TYPE_8PSK, BURST_TYPE_NB, HB_FILTER_WIDTH_NARROW));
  EXPECT_SUCCESS(session, client::cfg_tsc(stub(), session, "slot::all", TSC_TSC0));
  EXPECT_SUCCESS(session, client::cfg_power_control_level(stub(), session, "slot::all", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_PVT, true));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXGSM_ATTRIBUTE_PVT_RBW_FILTER_BANDWIDTH, 500000.0));
  EXPECT_SUCCESS(session, client::pvt_cfg_averaging(stub(), session, "", PVT_AVERAGING_ENABLED_FALSE, 10, PVT_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto pvt_fetch_measurement_status_response = client::pvt_fetch_measurement_status(stub(), session, "", 10.0);
  const auto pvt_fetch_slot_measurement_array_response = client::pvt_fetch_slot_measurement_array(stub(), session, "", 10.0);
  const auto pvt_fetch_power_trace_response = client::pvt_fetch_power_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, pvt_fetch_measurement_status_response);
  EXPECT_EQ(0, pvt_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, pvt_fetch_slot_measurement_array_response);
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_average_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_average_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_width().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_width(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status().size());
  EXPECT_EQ(0, pvt_fetch_slot_measurement_array_response.slot_measurement_status(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_maximum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_maximum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_minimum_power().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_minimum_power(0));
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold_size());
  EXPECT_NE(0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold().size());
  EXPECT_NE(0.0, pvt_fetch_slot_measurement_array_response.slot_burst_threshold(0));
  EXPECT_SUCCESS(session, pvt_fetch_power_trace_response);
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.x0());
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.dx());
  EXPECT_NE(0, pvt_fetch_power_trace_response.upper_mask_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.upper_mask().size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.upper_mask(0));
  EXPECT_NE(0, pvt_fetch_power_trace_response.signal_power_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.signal_power().size());
  EXPECT_NE(0.0, pvt_fetch_power_trace_response.signal_power(0));
  EXPECT_NE(0, pvt_fetch_power_trace_response.lower_mask_size());
  EXPECT_NE(0, pvt_fetch_power_trace_response.lower_mask().size());
  EXPECT_TRUE(isinf(pvt_fetch_power_trace_response.lower_mask(0)));
}
}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxgsm_session_tests.cpp sha256=2a38e312584ec742d1f7e24a7a4554a006eeeda826e0c44625937db7dc34ae34 bytes=6930 -->
## FILE: source/tests/system/nirfmxgsm_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxgsm_session_tests.cpp`
- sha256: `2a38e312584ec742d1f7e24a7a4554a006eeeda826e0c44625937db7dc34ae34`
- bytes: 6930

````cpp
#include "device_server.h"
#include "nirfmxgsm/nirfmxgsm_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxgsm = nirfmxgsm_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxGSMSession = -380598;
const char* kRFmxGSMTestRsrc = "FakeDevice";
const char* kRFmxGSMOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxGSMTestSessionOne = "SessionOneName";
const char* kRFmxGSMTestSessionTwo = "SessionTwoName";
const char* kRFmxGSMTestInvalidRsrc = "";

class NiRFmxGSMSessionTest : public ::testing::Test {
 protected:
  NiRFmxGSMSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxgsm_stub_(rfmxgsm::NiRFmxGSM::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxGSMSessionTest() {}

  std::unique_ptr<rfmxgsm::NiRFmxGSM::Stub>& GetStub()
  {
    return nirfmxgsm_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxgsm::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxgsm::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxgsm::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxgsm::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxgsm::NiRFmxGSM::Stub> nirfmxgsm_stub_;
};

TEST_F(NiRFmxGSMSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxgsm::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxGSMSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxgsm::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxGSMSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxgsm::InitializeResponse response;
    call_initialize(kRFmxGSMTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxGSMSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxgsm::InitializeResponse init_response;
  call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxgsm::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxgsm::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxGSMSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxgsm::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxgsm::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxGSMSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxgsm::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxGSMTestRsrc, kRFmxGSMOptionsString, kRFmxGSMTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxgsm::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxGSMSession);
}

TEST_F(NiRFmxGSMSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxgsm::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxGSMSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxinstr_driver_api_tests.cpp sha256=047f9e366d661f60a97fec6795b974cc55e88fdf7cdfa3f497a34a8d4683d211 bytes=17253 -->
## FILE: source/tests/system/nirfmxinstr_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxinstr_driver_api_tests.cpp`
- sha256: `047f9e366d661f60a97fec6795b974cc55e88fdf7cdfa3f497a34a8d4683d211`
- bytes: 17253

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxspecan/nirfmxspecan_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxinstr_grpc;
namespace client = nirfmxinstr_grpc::experimental::client;
namespace nirfsa_client = nirfsa_grpc::experimental::client;
namespace specan_client = nirfmxspecan_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5663 = "5663";
constexpr auto PXI_5663E = "5663E";

class NiRFmxInstrDriverApiTests : public Test {
 protected:
  NiRFmxInstrDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxInstr::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxInstrDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxInstr::Stub>& stub() const
  {
    return stub_;
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  // Some APIs (GetAttribute) require you Initate/Commit the session. Use an arbitrary SpecAn measurement type
  // to enter this state.
  void initiate_to_enter_committed_state(const nidevice_grpc::Session& session)
  {
    auto specan_stub = create_stub<nirfmxspecan_grpc::NiRFmxSpecAn>();
    EXPECT_SUCCESS(session, specan_client::select_measurements(specan_stub, session, "", nirfmxspecan_grpc::MeasurementTypes::MEASUREMENT_TYPES_CHP, true));
    EXPECT_SUCCESS(session, specan_client::initiate(specan_stub, session, "", ""));
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxInstr::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nirfsa_grpc::InitWithOptionsResponse init_rfsa(const nirfsa_client::StubPtr& stub, const std::string& resource_name)
{
  return nirfsa_client::init_with_options(stub, resource_name, false, false, "Simulate=1, DriverSetup=Model:5663E");
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

::grpc::Status get_rfsa_session_array(const client::StubPtr& stub, const nidevice_grpc::Session& session, const std::vector<std::string>& session_names, GetNIRFSASessionArrayResponse& response)
{
  auto request = GetNIRFSASessionArrayRequest{};

  for (const auto& name : session_names) {
    request.add_session_names(name);
  }
  request.mutable_instrument()->CopyFrom(session);
  ::grpc::ClientContext context;
  // Note: this can't use the experimental::client APIs, because those omit the session name
  // for simplicity (for most cases that we test).
  return stub->GetNIRFSASessionArray(&context, request, &response);
}

void EXPECT_GET_RFSA_ARRAY_WRONG_NUMBER_OF_SESSIONS_ERROR(const ::grpc::Status& actual_status, size_t expected_number_of_sessions)
{
  EXPECT_EQ(::grpc::INVALID_ARGUMENT, actual_status.error_code());
  std::stringstream stream;
  stream << "Number of session_names must be zero or match actual array size (" << expected_number_of_sessions << ").";
  EXPECT_EQ(stream.str(), actual_status.error_message());
}

nidevice_grpc::Session init_from_rfsa_session_array(const client::StubPtr& stub, const nirfsa_client::StubPtr& rfsa_stub, const std::vector<std::string>& rfsa_resource_names)
{
  auto rfsa_sessions = std::vector<nidevice_grpc::Session>{};
  for (const auto& resource_name : rfsa_resource_names) {
    auto init_rfsa_response = init_rfsa(rfsa_stub, resource_name);
    EXPECT_RESPONSE_SUCCESS(init_rfsa_response);
    rfsa_sessions.push_back(init_rfsa_response.vi());
  }

  auto init_response = client::initialize_from_nirfsa_session_array(stub, rfsa_sessions);
  auto session = init_response.instrument();
  EXPECT_RESPONSE_SUCCESS(init_response);
  return session;
}

TEST_F(NiRFmxInstrDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  // Don't use EXPECT_STATUS because that checks the error text, which can report stale errors from
  // previous tests.
  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxInstrDriverApiTests, GetNIRFSASession_SelfTest_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  const auto rfsa_response = EXPECT_SUCCESS(session, client::get_nirfsa_session(stub(), session));

  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  EXPECT_RESPONSE_SUCCESS(nirfsa_client::self_test(rfsa_stub, rfsa_response.nirfsa_session()));
}

TEST_F(NiRFmxInstrDriverApiTests, GetNIRFSASessionArrayAnonymous_SelfTest_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  const auto get_rfsa_response = EXPECT_SUCCESS(session, client::get_nirfsa_session_array(stub(), session));

  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  EXPECT_RESPONSE_SUCCESS(nirfsa_client::self_test(rfsa_stub, get_rfsa_response.nirfsa_sessions()[0]));
}

TEST_F(NiRFmxInstrDriverApiTests, GetNIRFSASessionArrayNamed_SelfTest_Succeeds)
{
  constexpr auto RFSA_SESSION_NAME = "test_rfsa_session";
  auto session = init_session(stub(), PXI_5663E);

  auto get_rfsa_response = GetNIRFSASessionArrayResponse{};
  const auto status = get_rfsa_session_array(stub(), session, {RFSA_SESSION_NAME}, get_rfsa_response);
  EXPECT_SUCCESS(session, get_rfsa_response);

  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  auto rfsa_named_session = nidevice_grpc::Session{};
  rfsa_named_session.set_name(RFSA_SESSION_NAME);
  EXPECT_RESPONSE_SUCCESS(nirfsa_client::self_test(rfsa_stub, rfsa_named_session));
}

TEST_F(NiRFmxInstrDriverApiTests, GetNIRFSASessionArrayWithTooManyNames_ReturnsBadStatus)
{
  auto session = init_session(stub(), PXI_5663E);

  auto get_rfsa_response = GetNIRFSASessionArrayResponse{};
  const auto status = get_rfsa_session_array(stub(), session, {"rfsa_1", "one_too_many"}, get_rfsa_response);

  EXPECT_GET_RFSA_ARRAY_WRONG_NUMBER_OF_SESSIONS_ERROR(status, 1);
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromNIRFSA_SelfCalibrate_Succeeds)
{
  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  auto init_rfsa_response = init_rfsa(rfsa_stub, "Sim");
  EXPECT_RESPONSE_SUCCESS(init_rfsa_response);
  auto init_response = client::initialize_from_nirfsa_session(stub(), init_rfsa_response.vi());
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  EXPECT_SUCCESS(session, client::self_calibrate(stub(), session, "", 0));
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromNIRFSAArray_SelfCalibrate_Succeeds)
{
  const auto session = init_from_rfsa_session_array(stub(), create_stub<nirfsa_grpc::NiRFSA>(), {"Sim1", "Sim2"});

  EXPECT_SUCCESS(session, client::self_calibrate(stub(), session, "", 0));
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromTwoRFSASessions_GetNIRFSASessionArrayAnonymous_SelfTestEachSessionSucceeds)
{
  const auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  const auto session = init_from_rfsa_session_array(stub(), rfsa_stub, {"Sim1", "Sim2"});

  const auto get_rfsa_response = client::get_nirfsa_session_array(stub(), session);
  EXPECT_SUCCESS(session, get_rfsa_response);

  EXPECT_EQ(2, get_rfsa_response.nirfsa_sessions_size());
  for (const auto& session : get_rfsa_response.nirfsa_sessions()) {
    EXPECT_RESPONSE_SUCCESS(nirfsa_client::self_test(rfsa_stub, session));
  }
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromTwoRFSASessions_GetNIRFSASessionArrayWithTooFewNames_ReturnsBadStatus)
{
  const auto session = init_from_rfsa_session_array(stub(), create_stub<nirfsa_grpc::NiRFSA>(), {"Sim1", "Sim2"});

  auto get_rfsa_response = GetNIRFSASessionArrayResponse{};
  const auto status = get_rfsa_session_array(stub(), session, {"rfsa_1"}, get_rfsa_response);

  EXPECT_GET_RFSA_ARRAY_WRONG_NUMBER_OF_SESSIONS_ERROR(status, 2);
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromTwoRFSASessions_GetNIRFSASessionArrayWithTooManyNames_ReturnsBadStatus)
{
  const auto session = init_from_rfsa_session_array(stub(), create_stub<nirfsa_grpc::NiRFSA>(), {"Sim1", "Sim2"});

  auto get_rfsa_response = GetNIRFSASessionArrayResponse{};
  const auto status = get_rfsa_session_array(stub(), session, {"rfsa_1", "rfsa_2", "rfsa_one_too_many"}, get_rfsa_response);

  EXPECT_GET_RFSA_ARRAY_WRONG_NUMBER_OF_SESSIONS_ERROR(status, 2);
}

TEST_F(NiRFmxInstrDriverApiTests, InitializeFromTwoRFSASessions_GetNIRFSASessionArrayNamed_ReturnsTwoSessions)
{
  const auto RFSA_SESSION_NAMES = std::vector<std::string>{"rfsa_1", "rfsa_2"};
  const auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  const auto session = init_from_rfsa_session_array(stub(), rfsa_stub, {"Sim1", "Sim2"});

  auto get_rfsa_response = GetNIRFSASessionArrayResponse{};
  const auto status = get_rfsa_session_array(stub(), session, RFSA_SESSION_NAMES, get_rfsa_response);

  EXPECT_EQ(::grpc::OK, status.error_code());
  EXPECT_EQ(2, get_rfsa_response.nirfsa_sessions_size());
  for (const auto& session_name : RFSA_SESSION_NAMES) {
    auto session = nidevice_grpc::Session{};
    session.set_name(session_name);
    EXPECT_RESPONSE_SUCCESS(nirfsa_client::self_test(rfsa_stub, session));
  }
}

TEST_F(NiRFmxInstrDriverApiTests, NoActiveList_GetListNames_ReturnsEmptyLists)
{
  const auto session = init_session(stub(), PXI_5663E);

  const auto response = EXPECT_SUCCESS(session, client::get_list_names(stub(), session, "", 0));

  EXPECT_THAT(response.list_names(), IsEmpty());
  EXPECT_THAT(response.personality(), IsEmpty());
}

TEST_F(NiRFmxInstrDriverApiTests, SetAndGetTuningSpeed_ReturnsTuningSpeed)
{
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED, NiRFmxInstrInt32AttributeValues::NIRFMXINSTR_INT32_TUNING_SPEED_FAST));
  initiate_to_enter_committed_state(session);
  const auto tuning_speed = GET_ATTR_I32(session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED);

  EXPECT_EQ(tuning_speed, NiRFmxInstrInt32AttributeValues::NIRFMXINSTR_INT32_TUNING_SPEED_FAST);
}

TEST_F(NiRFmxInstrDriverApiTests, SetAndGetFrequencyReferenceSource_ReturnsFrequencyReferenceSource)
{
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_FREQUENCY_REFERENCE_SOURCE, NiRFmxInstrStringAttributeValuesMapped::NIRFMXINSTR_STRING_FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK));
  initiate_to_enter_committed_state(session);
  const auto frequency_reference_source = GET_ATTR_STR(session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_FREQUENCY_REFERENCE_SOURCE);

  EXPECT_EQ(frequency_reference_source, "OnboardClock");
}

TEST_F(NiRFmxInstrDriverApiTests, CallCfgMethods_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_mechanical_attenuation(stub(), session, "", MechanicalAttenuationAuto::MECHANICAL_ATTENUATION_AUTO_TRUE, 10.0));
}

TEST_F(NiRFmxInstrDriverApiTests, CallCheckMethods_SucceedsWithReasonableResponseValues)
{
  const auto session = init_session(stub(), PXI_5663E);
  const auto status_response = client::check_acquisition_status(stub(), session);
  EXPECT_SUCCESS(session, status_response);
  const auto list_exists_response = client::check_if_list_exists(stub(), session, "NOTALIST");
  EXPECT_SUCCESS(session, list_exists_response);
  const auto self_cal_response = client::is_self_calibrate_valid(stub(), session, "");
  EXPECT_SUCCESS(session, self_cal_response);

  EXPECT_EQ(status_response.acquisition_done(), true);
  EXPECT_EQ(list_exists_response.list_exists(), false);
  EXPECT_EQ(list_exists_response.personality(), Personality::PERSONALITY_NONE);
  EXPECT_EQ(self_cal_response.self_calibrate_valid(), true);
  EXPECT_THAT(self_cal_response.valid_steps_array(), ElementsAreArray(std::vector<SelfCalStep>{SelfCalStep::SELF_CAL_STEP_DIGITIZER_SELF_CAL}));
}

// Use a mix of RFmxSpecAn and RFmxInstr APIs in an RFmxInstr session.
TEST_F(NiRFmxInstrDriverApiTests, SpectrumBasicWithRFmxInstr_DataLooksReasonable)
{
  auto specan_stub = create_stub<nirfmxspecan_grpc::NiRFmxSpecAn>();
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, specan_client::cfg_rf(specan_stub, session, "", 1e9, 0, 0));
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, specan_client::spectrum_cfg_span(specan_stub, session, "", 1e6));
  EXPECT_SUCCESS(session, specan_client::spectrum_cfg_rbw_filter(specan_stub, session, "", true, 100e3, nirfmxspecan_grpc::SpectrumRbwFilterType::SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN));
  EXPECT_SUCCESS(session, specan_client::spectrum_cfg_averaging(specan_stub, session, "", false, 10, nirfmxspecan_grpc::SpectrumAveragingType::SPECTRUM_AVERAGING_TYPE_RMS));

  auto read_response = EXPECT_SUCCESS(session, specan_client::spectrum_read(specan_stub, session, "", 10.0));

  constexpr auto EXPECTED_SPECTRUM_SIZE = 1005;
  EXPECT_EQ(EXPECTED_SPECTRUM_SIZE, read_response.spectrum().size());
  constexpr auto MIDPOINT_X = EXPECTED_SPECTRUM_SIZE / 2;
  EXPECT_LT(read_response.spectrum(0), read_response.spectrum(MIDPOINT_X));
  EXPECT_LT(read_response.spectrum(EXPECTED_SPECTRUM_SIZE - 1), read_response.spectrum(MIDPOINT_X));
}

TEST_F(NiRFmxInstrDriverApiTests, GetModelName_ReturnsModelName)
{
  const auto session = init_session(stub(), PXI_5663E);
  const auto instrument_model = GET_ATTR_STR(session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_INSTRUMENT_MODEL);

  EXPECT_EQ(instrument_model, "NI PXIe-5663E");
}

TEST_F(NiRFmxInstrDriverApiTests, TimestampFromValuesRoundTrip_SucceedsWithOriginalValues)
{
  constexpr auto UNIX_TIMESTAMP = 10000;
  constexpr auto FRACTIONAL_SECONDS = .75;
  const auto timestamp_response = client::timestamp_from_values(stub(), UNIX_TIMESTAMP, FRACTIONAL_SECONDS);
  const auto values_response = client::values_from_timestamp(stub(), timestamp_response.timestamp());

  EXPECT_RESPONSE_SUCCESS(timestamp_response);
  EXPECT_RESPONSE_SUCCESS(values_response);
  EXPECT_EQ(UNIX_TIMESTAMP, values_response.seconds_since_1970());
  EXPECT_NEAR(FRACTIONAL_SECONDS, values_response.fractional_seconds(), .001);
}

TEST_F(NiRFmxInstrDriverApiTests, BuildPortString_SucceedsWithExpectedValue)
{
  constexpr auto EXPECTED_PORT_STRING = "port::RFSA1/10";
  const auto build_port_string_response = client::build_port_string(stub(), "", "", "RFSA1", 10);

  EXPECT_RESPONSE_SUCCESS(build_port_string_response);
  EXPECT_EQ(EXPECTED_PORT_STRING, build_port_string_response.selector_string_out());
}

TEST_F(NiRFmxInstrDriverApiTests, ExportSignal_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663E);
  auto response = client::export_signal(stub(), session, ExportSignalSource::EXPORT_SIGNAL_SOURCE_ADVANCE_TRIGGER, OutputTerminal::OUTPUT_TERMINAL_PFI0);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFmxInstrDriverApiTests, SetReadyForStartEventOutputTerminal_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663);
  auto response = client::set_attribute_string(
      stub(),
      session,
      "",
      NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL,
      NiRFmxInstrStringAttributeValuesMapped::NIRFMXINSTR_STRING_OUTPUT_TERMINAL_PXI_TRIG0);

  EXPECT_SUCCESS(session, response);
}

TEST_F(NiRFmxInstrDriverApiTests, SetRStartTriggerDigitalEdgeSource_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663);
  auto response = client::set_attribute_string(
      stub(),
      session,
      "",
      NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_START_TRIGGER_DIGITAL_EDGE_SOURCE,
      NiRFmxInstrStringAttributeValuesMapped::NIRFMXINSTR_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_TIMER_EVENT);

  EXPECT_SUCCESS(session, response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxinstr_restricted_driver_api_tests.cpp sha256=35345b5325889ace2ea3807dd2f585b3a858a0126f0622fc34a728f490be1e1d bytes=7155 -->
## FILE: source/tests/system/nirfmxinstr_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxinstr_restricted_driver_api_tests.cpp`
- sha256: `35345b5325889ace2ea3807dd2f585b3a858a0126f0622fc34a728f490be1e1d`
- bytes: 7155

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxinstr_restricted/nirfmxinstr_restricted_client.h"
#include "nirfmxspecan/nirfmxspecan_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxinstr_grpc;
using namespace nirfmxinstr_restricted_grpc;
namespace client = nirfmxinstr_grpc::experimental::client;
namespace restricted_client = nirfmxinstr_restricted_grpc::experimental::client;
namespace nirfsa_client = nirfsa_grpc::experimental::client;
namespace specan_client = nirfmxspecan_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5663 = "5663";
constexpr auto PXI_5663E = "5663E";
constexpr auto DEFAULT_RESOURCE_NAME = "FakeDevice";

class NiRFmxInstrRestrictedDriverApiTests : public Test {
 protected:
  NiRFmxInstrRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxinstr_stub_(NiRFmxInstr::NewStub(device_server_->InProcessChannel())),
        nirfmxinstr_restricted_stub_(NiRFmxInstrRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxInstrRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiRFmxInstr::Stub>& stub()
  {
    return nirfmxinstr_stub_;
  }

  std::unique_ptr<NiRFmxInstrRestricted::Stub>& restricted_stub()
  {
    return nirfmxinstr_restricted_stub_;
  }

  // Some APIs (GetAttribute) require you Initiate/Commit the session. Use an arbitrary SpecAn measurement type
  // to enter this state.
  void initiate_to_enter_committed_state(const nidevice_grpc::Session& session)
  {
    auto specan_stub = create_stub<nirfmxspecan_grpc::NiRFmxSpecAn>();
    EXPECT_SUCCESS(session, specan_client::select_measurements(specan_stub, session, "", nirfmxspecan_grpc::MeasurementTypes::MEASUREMENT_TYPES_CHP, true));
    EXPECT_SUCCESS(session, specan_client::initiate(specan_stub, session, "", ""));
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxInstr::Stub> nirfmxinstr_stub_;
  std::unique_ptr<NiRFmxInstrRestricted::Stub> nirfmxinstr_restricted_stub_;
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

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, DEFAULT_RESOURCE_NAME);
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, GetRFmxVersion)
{
  const auto session = init_session(stub(), PXI_5663);
  auto get_version_response = restricted_client::get_r_fmx_version(restricted_stub(), session);
  EXPECT_RESPONSE_SUCCESS(get_version_response);
  EXPECT_GT(get_version_response.version().length(), 0);
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, SetForceAllTracesEnabled_GetForceAllTracesEnabled_AttributeIsAsSet)
{
  const auto session = init_session(stub(), PXI_5663E);
  auto initial_enabled_response = restricted_client::get_force_all_traces_enabled(restricted_stub(), session, "");
  auto new_enabled_value = initial_enabled_response.attr_val() == 0 ? 1 : 0;
  EXPECT_SUCCESS(session, restricted_client::set_force_all_traces_enabled(restricted_stub(), session, "", new_enabled_value));

  auto get_enabled_response = restricted_client::get_force_all_traces_enabled(restricted_stub(), session, "");
  EXPECT_RESPONSE_SUCCESS(get_enabled_response);
  EXPECT_EQ(new_enabled_value, get_enabled_response.attr_val());
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, SetAttributeOutOfRange_GetAttributeDesiredF64_DesiredAttributeReturned)
{
  const double attenuation = 150.0;
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_MECHANICAL_ATTENUATION_VALUE, attenuation));
  initiate_to_enter_committed_state(session);

  auto get_desired_attr_response = restricted_client::get_attribute_desired_f64(restricted_stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_MECHANICAL_ATTENUATION_VALUE);
  EXPECT_RESPONSE_SUCCESS(get_desired_attr_response);
  EXPECT_EQ(get_desired_attr_response.attr_val(), attenuation);

  auto get_attr_response = client::get_attribute_f64(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_MECHANICAL_ATTENUATION_VALUE);
  EXPECT_LT(get_attr_response.attr_val(), get_desired_attr_response.attr_val());
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, SetAttributeOutOfRange_GetAttributeDesiredI32_DesiredAttributeReturned)
{
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED, INT_MAX));
  initiate_to_enter_committed_state(session);

  auto get_desired_attr_response = restricted_client::get_attribute_desired_i32(restricted_stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED);
  EXPECT_RESPONSE_SUCCESS(get_desired_attr_response);
  EXPECT_EQ(get_desired_attr_response.attr_val(), INT_MAX);

  auto get_attr_response = client::get_attribute_i32(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED);
  EXPECT_LT(get_attr_response.attr_val(), get_desired_attr_response.attr_val());
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, GetAttributeAuthor)
{
  const auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED, 2));
  initiate_to_enter_committed_state(session);

  auto get_attribute_author_response = restricted_client::get_attribute_author(restricted_stub(), session, "", NIRFMXINSTR_ATTRIBUTE_TUNING_SPEED);
  EXPECT_RESPONSE_SUCCESS(get_attribute_author_response);
  EXPECT_EQ(get_attribute_author_response.attr_val(), 1);  // RfsgAttributeAuthor.User
}

TEST_F(NiRFmxInstrRestrictedDriverApiTests, SetIOTraceStatus)
{
  const auto session = init_session(stub(), PXI_5663);
  auto set_io_trace_status_response = restricted_client::set_io_trace_status(restricted_stub(), session, 1);
  EXPECT_RESPONSE_SUCCESS(set_io_trace_status_response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxlte_driver_api_tests.cpp sha256=3e12bf1d3183f2ac7eebe05f0b67ccecad193bf92b5c92d24490d40d102a9c22 bytes=105073 -->
## FILE: source/tests/system/nirfmxlte_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxlte_driver_api_tests.cpp`
- sha256: `3e12bf1d3183f2ac7eebe05f0b67ccecad193bf92b5c92d24490d40d102a9c22`
- bytes: 105073

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxlte/nirfmxlte_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxlte_grpc;
namespace client = nirfmxlte_grpc::experimental::client;
namespace nirfsa_client = nirfsa_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

typedef ::google::protobuf::int32 int32;
typedef ::google::protobuf::int64 int64;
typedef double float64;

constexpr auto PXI_5663E = "5663E";
constexpr auto SYNC_FAILURE_WARNING = 374603;
constexpr auto SYNC_FAILURE_WARNING_STR = "Unable to synchronize";
constexpr auto MODACC_NB_IOT_AUTODETECT_CHECK = -376649;
constexpr auto MODACC_NB_IOT_AUTODETECT_CHECK_STR = "Autodetected NPUSCH channel parameters are not ";

class NiRFmxLTEDriverApiTests : public Test {
 protected:
  NiRFmxLTEDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxLTE::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxLTEDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxLTE::Stub>& stub() const
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
  std::unique_ptr<NiRFmxLTE::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nirfsa_grpc::InitWithOptionsResponse init_rfsa(const nirfsa_client::StubPtr& stub, const std::string& resource_name)
{
  return nirfsa_client::init_with_options(stub, resource_name, false, false, "Simulate=1, DriverSetup=Model:5663E");
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxLTEDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxLTEDriverApiTests, InitializeFromNIRFSA_Close_Succeeds)
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

TEST_F(NiRFmxLTEDriverApiTests, AcpContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  const std::vector<int> empty_int_vec;
  std::vector<float64> componentCarrierBandwidth{20e6, 20e6};
  std::vector<float64> componentCarrierFrequency{-9.9e6, 9.9e6};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 1.95e9));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "", RF_ATTENUATION_AUTO_TRUE, 10.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, "", componentCarrierBandwidth, componentCarrierFrequency, empty_int_vec));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 0.01));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto NUMBER_OF_OFFSETS = 3;
  std::vector<ACPFetchAbsolutePowersTraceResponse> acp_fetch_absolute_powers_trace_response_vec;
  std::vector<ACPFetchRelativePowersTraceResponse> acp_fetch_relative_powers_trace_response_vec;
  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::acp_fetch_total_aggregated_power(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_OFFSETS; i++) {
    acp_fetch_absolute_powers_trace_response_vec.push_back(EXPECT_SUCCESS(session, client::acp_fetch_absolute_powers_trace(stub(), session, "", 10.0, i)));
    acp_fetch_relative_powers_trace_response_vec.push_back(EXPECT_SUCCESS(session, client::acp_fetch_relative_powers_trace(stub(), session, "", 10.0, i)));
  }
  const auto acp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::acp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_LT(0.0, acp_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_LT(0.0, acp_fetch_absolute_powers_trace_response_vec[0].x0());
  EXPECT_LT(0.0, acp_fetch_absolute_powers_trace_response_vec[0].dx());
  EXPECT_EQ(2, acp_fetch_absolute_powers_trace_response_vec[0].absolute_powers_trace_size());
  EXPECT_EQ(2, acp_fetch_absolute_powers_trace_response_vec[0].absolute_powers_trace().size());
  EXPECT_GT(0.0, acp_fetch_absolute_powers_trace_response_vec[0].absolute_powers_trace(0));
  EXPECT_LT(0.0, acp_fetch_relative_powers_trace_response_vec[0].x0());
  EXPECT_LT(0.0, acp_fetch_relative_powers_trace_response_vec[0].dx());
  EXPECT_EQ(2, acp_fetch_relative_powers_trace_response_vec[0].relative_powers_trace_size());
  EXPECT_EQ(2, acp_fetch_relative_powers_trace_response_vec[0].relative_powers_trace().size());
  EXPECT_GT(0.0, acp_fetch_relative_powers_trace_response_vec[0].relative_powers_trace(0));
  EXPECT_LT(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(117479, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(117479, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxLTEDriverApiTests, ChpSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP, true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::chp_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto chp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::chp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_LT(0.0, chp_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_EQ(0.0, chp_fetch_component_carrier_measurement_response.relative_power());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_EQ(217, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(217, chp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, chp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxLTEDriverApiTests, DLModAccContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  const std::vector<int> empty_int_vec;
  std::vector<float64> componentCarrierBandwidth{20e6, 20e6};
  std::vector<float64> componentCarrierFrequency{-9.9e6, 9.9e6};
  std::vector<int> downlinkTestModel{DOWNLINK_TEST_MODEL_TM1_1, DOWNLINK_TEST_MODEL_TM1_1};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 2.14e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", 1));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_DOWNLINK));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, "", componentCarrierBandwidth, componentCarrierFrequency, empty_int_vec));
  EXPECT_SUCCESS(session, client::cfg_downlink_test_model_array(stub(), session, "", downlinkTestModel));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_FRAME, 0, 1));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_evm_unit(stub(), session, "", MODACC_EVM_UNIT_PERCENTAGE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  ModAccFetchPDSCHQPSKConstellationResponse mod_acc_fetch_pdschqpsk_constellation_response;
  ModAccFetchEVMPerSubcarrierTraceResponse mod_acc_fetch_evm_per_subcarrier_trace_response;
  const auto mod_acc_fetch_composite_evm_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_composite_evm_array(stub(), session, "", 10.0));
  const auto mod_acc_fetch_iq_impairments_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments_array(stub(), session, "", 10.0));
  const auto mod_acc_fetch_pdschevm_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_pdschevm_array(stub(), session, "", 10.0));
  const auto mod_acc_fetch_pdsch1024q_amevm_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_pdsch1024q_amevm_array(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), "", i));
    mod_acc_fetch_pdschqpsk_constellation_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_pdschqpsk_constellation(stub(), session, carrier_string_response.selector_string_out(), 10.0));
    mod_acc_fetch_evm_per_subcarrier_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_per_subcarrier_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0));
  }

  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_frequency_error_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_frequency_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_array_response.mean_frequency_error(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index().size());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index().size());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index().size());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset().size());
  EXPECT_EQ(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance().size());
  // Sometimes nan: EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error().size());
  // Sometimes nan: EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error(0));
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_pdschevm_array_response.mean_rms_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_qpsk_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_qpsk_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_pdschevm_array_response.mean_rms_qpsk_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_16qam_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_16qam_evm().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_pdschevm_array_response.mean_rms_16qam_evm(0)));
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_64qam_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_64qam_evm().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_pdschevm_array_response.mean_rms_64qam_evm(0)));
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_256qam_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdschevm_array_response.mean_rms_256qam_evm().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_pdschevm_array_response.mean_rms_256qam_evm(0)));
  EXPECT_EQ(2, mod_acc_fetch_pdsch1024q_amevm_array_response.mean_rms_1024qam_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_pdsch1024q_amevm_array_response.mean_rms_1024qam_evm().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_pdsch1024q_amevm_array_response.mean_rms_1024qam_evm(0)));
  EXPECT_NE(0.0, mod_acc_fetch_pdschqpsk_constellation_response.qpsk_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pdschqpsk_constellation_response.qpsk_constellation(0).imaginary());
  EXPECT_EQ(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response.x0());
  EXPECT_EQ(1.0, mod_acc_fetch_evm_per_subcarrier_trace_response.dx());
  EXPECT_EQ(1201, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier_size());
  EXPECT_EQ(1201, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier(0));
}

TEST_F(NiRFmxLTEDriverApiTests, NBIotAcpFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
  EXPECT_SUCCESS(session, client::cfg_nb_io_t_component_carrier(stub(), session, "", 0, NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto NUMBER_OF_OFFSETS = 2;
  ACPFetchAbsolutePowersTraceResponse acp_fetch_absolute_powers_trace_response;
  ACPFetchRelativePowersTraceResponse acp_fetch_relative_powers_trace_response;
  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::acp_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_OFFSETS; i++) {
    acp_fetch_absolute_powers_trace_response = EXPECT_SUCCESS(session, client::acp_fetch_absolute_powers_trace(stub(), session, "", 10.0, i));
    acp_fetch_relative_powers_trace_response = EXPECT_SUCCESS(session, client::acp_fetch_relative_powers_trace(stub(), session, "", 10.0, i));
  }
  const auto acp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::acp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_LT(0.0, acp_fetch_component_carrier_measurement_response.absolute_power());
  // There have been intermittent instances where the relative_power returned
  // isn't absolutely 0.0 from the driver. When this happens it doesn't appear to affect
  // any of the other tests.
  EXPECT_NEAR(0.0, acp_fetch_component_carrier_measurement_response.relative_power(), 0.001);
  EXPECT_LT(0.0, acp_fetch_absolute_powers_trace_response.x0());
  EXPECT_LT(0.0, acp_fetch_absolute_powers_trace_response.dx());
  EXPECT_EQ(2, acp_fetch_absolute_powers_trace_response.absolute_powers_trace_size());
  EXPECT_EQ(2, acp_fetch_absolute_powers_trace_response.absolute_powers_trace().size());
  EXPECT_GT(0.0, acp_fetch_absolute_powers_trace_response.absolute_powers_trace(0));
  EXPECT_LT(0.0, acp_fetch_relative_powers_trace_response.x0());
  EXPECT_LT(0.0, acp_fetch_relative_powers_trace_response.dx());
  EXPECT_EQ(2, acp_fetch_relative_powers_trace_response.relative_powers_trace_size());
  EXPECT_EQ(2, acp_fetch_relative_powers_trace_response.relative_powers_trace().size());
  EXPECT_GT(0.0, acp_fetch_relative_powers_trace_response.relative_powers_trace(0));
  EXPECT_LT(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(9901, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(9901, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxLTEDriverApiTests, NBIoTModAccFromExample_FetchData_DataLooksReasonable)
{
  nidevice_grpc::Session session;
  ModAccFetchCompositeEVMResponse mod_acc_fetch_composite_evm_response;
  int actualStatus = -1, attempts = 1;
  while (1) {
    session = init_session(stub(), PXI_5663E);
    EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
    EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
    EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
    EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
    EXPECT_SUCCESS(session, client::cfg_nb_io_t_component_carrier(stub(), session, "", 0, NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ));
    EXPECT_SUCCESS(session, client::cfg_npusch_format(stub(), session, "", 1));
    EXPECT_SUCCESS(session, client::cfg_auto_npusch_channel_detection_enabled(stub(), session, "", AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_TRUE));
    EXPECT_SUCCESS(session, client::cfg_npusch_starting_slot(stub(), session, "", 0));
    EXPECT_SUCCESS(session, client::cfg_npuschdmrs(stub(), session, "", NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO, 0, 0, NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE, 0));
    EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_evm_unit(stub(), session, "", MODACC_EVM_UNIT_PERCENTAGE));
    EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

    // Intermittently fails with: "Autodetected NPUSCH channel parameters are not 3GPP spec compliant."
    try {
      mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.0);
      actualStatus = mod_acc_fetch_composite_evm_response.status();
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      const auto& error = ex.Trailers().find("ni-error")->second;
      actualStatus = std::stoi(error);
    }
    if (actualStatus == MODACC_NB_IOT_AUTODETECT_CHECK && attempts < 5) {
      TearDown();
      SetUp();
      ++attempts;
    }
    else {
      break;
    }
  }
  // If this fails, we want the test to be over now.
  ASSERT_GE(actualStatus, 0);

  const auto mod_acc_fetch_iq_impairments_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0));
  const auto mod_acc_fetch_in_band_emission_margin_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_in_band_emission_margin(stub(), session, "", 10.0));
  const auto mod_acc_fetch_npusch_constellation_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_npusch_constellation_trace(stub(), session, "", 10.0));
  const auto mod_acc_fetch_evm_per_symbol_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_per_symbol_trace(stub(), session, "", 10.0));

  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_response.mean_rms_composite_evm());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_response.maximum_peak_composite_evm());
  EXPECT_GT(0.0, mod_acc_fetch_composite_evm_response.mean_frequency_error());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_symbol_index());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_subcarrier_index());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_slot_index());
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_quadrature_error());
  EXPECT_EQ(0.0, mod_acc_fetch_in_band_emission_margin_response.in_band_emission_margin());
  EXPECT_EQ(72, mod_acc_fetch_npusch_constellation_trace_response.data_constellation_size());
  EXPECT_EQ(72, mod_acc_fetch_npusch_constellation_trace_response.data_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_npusch_constellation_trace_response.data_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_npusch_constellation_trace_response.data_constellation(0).imaginary());
  EXPECT_EQ(12, mod_acc_fetch_npusch_constellation_trace_response.dmrs_constellation_size());
  EXPECT_EQ(12, mod_acc_fetch_npusch_constellation_trace_response.dmrs_constellation().size());
  EXPECT_LT(0.0, mod_acc_fetch_npusch_constellation_trace_response.dmrs_constellation(0).real());
  EXPECT_GT(0.0, mod_acc_fetch_npusch_constellation_trace_response.dmrs_constellation(0).imaginary());
  EXPECT_EQ(0.0, mod_acc_fetch_evm_per_symbol_trace_response.x0());
  EXPECT_EQ(1.0, mod_acc_fetch_evm_per_symbol_trace_response.dx());
  EXPECT_EQ(7, mod_acc_fetch_evm_per_symbol_trace_response.rms_evm_per_symbol_size());
  EXPECT_EQ(7, mod_acc_fetch_evm_per_symbol_trace_response.rms_evm_per_symbol().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_per_symbol_trace_response.rms_evm_per_symbol(0));
}

TEST_F(NiRFmxLTEDriverApiTests, NBIoTModAccAcpChpObwSemCompositeSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  nidevice_grpc::Session session;
  ModAccFetchCompositeEVMResponse mod_acc_fetch_composite_evm_response;
  int actualStatus = -1, attempts = 1;
  while (1) {
    session = init_session(stub(), PXI_5663E);
    EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
    EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
    EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
    EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
    EXPECT_SUCCESS(session, client::cfg_nb_io_t_component_carrier(stub(), session, "", 0, NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ));
    EXPECT_SUCCESS(session, client::cfg_npusch_format(stub(), session, "", 1));
    EXPECT_SUCCESS(session, client::cfg_auto_npusch_channel_detection_enabled(stub(), session, "", AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_TRUE));
    EXPECT_SUCCESS(session, client::cfg_npusch_starting_slot(stub(), session, "", 0));
    EXPECT_SUCCESS(session, client::cfg_npuschdmrs(stub(), session, "", NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO, 0, 0, NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE, 0));
    EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP | MEASUREMENT_TYPES_CHP | MEASUREMENT_TYPES_MODACC | MEASUREMENT_TYPES_OBW | MEASUREMENT_TYPES_SEM, true));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
    EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
    EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
    EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
    EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
    EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
    EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.001));
    EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.001));
    EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.001));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
    EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

    // Intermittently fails with: "Autodetected NPUSCH channel parameters are not 3GPP spec compliant."
    try {
      mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.0);
      actualStatus = mod_acc_fetch_composite_evm_response.status();
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      const auto& error = ex.Trailers().find("ni-error")->second;
      actualStatus = std::stoi(error);
    }
    if (actualStatus == MODACC_NB_IOT_AUTODETECT_CHECK && attempts < 5) {
      TearDown();
      SetUp();
      ++attempts;
    }
    else {
      break;
    }
  }
  // If this fails, we want the test to be over now.
  ASSERT_GE(actualStatus, 0);

  const auto mod_acc_fetch_iq_impairments_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0));
  const auto mod_acc_fetch_in_band_emission_margin_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_in_band_emission_margin(stub(), session, "", 10.0));
  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::acp_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto obw_fetch_measurement_response = EXPECT_SUCCESS(session, client::obw_fetch_measurement(stub(), session, "", 10.0));
  const auto chp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::chp_fetch_component_carrier_measurement(stub(), session, "", 10.0));

  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_response.mean_rms_composite_evm());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_response.maximum_peak_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.mean_frequency_error());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_symbol_index());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_subcarrier_index());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_slot_index());
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_quadrature_error());
  EXPECT_EQ(0.0, mod_acc_fetch_in_band_emission_margin_response.in_band_emission_margin());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_LT(0.0, acp_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_LE(0.0, acp_fetch_component_carrier_measurement_response.relative_power());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_LT(0.0, sem_fetch_component_carrier_measurement_response.absolute_integrated_power());
  EXPECT_EQ(0.0, sem_fetch_component_carrier_measurement_response.relative_integrated_power());
  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
  EXPECT_LT(0.0, chp_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_EQ(0.0, chp_fetch_component_carrier_measurement_response.relative_power());
}

TEST_F(NiRFmxLTEDriverApiTests, NBIoTSemFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 100e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
  EXPECT_SUCCESS(session, client::cfg_nb_io_t_component_carrier(stub(), session, "", 0, NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(5, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_EQ(1, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_LT(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_EQ(5, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_GT(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_LT(0.0, sem_fetch_component_carrier_measurement_response.absolute_integrated_power());
  EXPECT_EQ(0.0, sem_fetch_component_carrier_measurement_response.relative_integrated_power());
  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_EQ(1000.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(3571, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(3571, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(3571, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(3571, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxLTEDriverApiTests, ObwSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.00, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 200e3, 0.0, 0));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_spectrum_response = EXPECT_SUCCESS(session, client::obw_fetch_spectrum(stub(), session, "", 10.0));
  const auto obw_fetch_measurement_response = EXPECT_SUCCESS(session, client::obw_fetch_measurement(stub(), session, "", 10.0));

  EXPECT_LT(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_EQ(403, obw_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(403, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, obw_fetch_spectrum_response.spectrum(0));
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
}

TEST_F(NiRFmxLTEDriverApiTests, SEMContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  const std::vector<int> empty_int_vec;
  std::vector<float64> componentCarrierBandwidth{20e6, 20e6};
  std::vector<float64> componentCarrierFrequency{-9.9e6, 9.9e6};
  std::vector<float64> componentCarrierMaximumOutputPower{0.0, 0.0};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, "", componentCarrierBandwidth, componentCarrierFrequency, empty_int_vec));
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_uplink_mask_type(stub(), session, "", SEM_UPLINK_MASK_TYPE_GENERAL_NS01));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::sem_fetch_total_aggregated_power(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

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
  EXPECT_LT(0.0, sem_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(128429, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(128429, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(128429, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(128429, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxLTEDriverApiTests, SemAdvancedNonContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  constexpr auto NUMBER_OF_COMPONENT_CARRIERS = 1;
  constexpr auto NUMBER_OF_SUBBLOCKS = 2;
  constexpr auto NUMBER_OF_OFFSET_SEGMENT = 4;
  std::vector<float64> subblocks_center_frequency{1.95e+9, 30e+6};
  std::vector<int32> subblocks_sideband(4, SEM_OFFSET_SIDEBAND_BOTH);
  std::vector<int32> subblocks_rbw_filter_type(4, SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN);
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_number_of_subblocks(stub(), session, "", NUMBER_OF_SUBBLOCKS));
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    auto subblock_string_response = client::build_subblock_string(stub(), "", i);
    EXPECT_SUCCESS(session, subblock_string_response);
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, subblock_string_response.selector_string_out(), subblocks_center_frequency[i]));
    EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, subblock_string_response.selector_string_out(), COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
    EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, subblock_string_response.selector_string_out(), NUMBER_OF_COMPONENT_CARRIERS));
    EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, subblock_string_response.selector_string_out(), {20e+6}, {0.0}, std::vector<int32>()));
    EXPECT_SUCCESS(session, client::sem_cfg_number_of_offsets(stub(), session, subblock_string_response.selector_string_out(), NUMBER_OF_OFFSET_SEGMENT));
    EXPECT_SUCCESS(session, client::sem_cfg_offset_frequency_array(stub(), session, subblock_string_response.selector_string_out(), {15e+3, 1.5e+6, 5.5e+6, 20.5e+6}, {985e+3, 4.5e+6, 19.5e+6, 24.5e+6}, subblocks_sideband));
    EXPECT_SUCCESS(session, client::sem_cfg_offset_rbw_filter_array(stub(), session, subblock_string_response.selector_string_out(), {10e+3, 250e+3, 250e+3, 250e+3}, subblocks_rbw_filter_type));
    EXPECT_SUCCESS(session, client::sem_cfg_offset_bandwidth_integral_array(stub(), session, subblock_string_response.selector_string_out(), {3, 4, 4, 4}));
    EXPECT_SUCCESS(session, client::sem_cfg_offset_absolute_limit_array(stub(), session, subblock_string_response.selector_string_out(), {-19.5, -8.5, -11.5, -23.5}, {-19.5, -8.5, -11.5, -23.5}));
  }
  EXPECT_SUCCESS(session, client::cfg_link_direction(stub(), session, "", LINK_DIRECTION_DOWNLINK));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::cfge_node_b_category(stub(), session, "", ENODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A));
  EXPECT_SUCCESS(session, client::sem_cfg_downlink_mask(stub(), session, "", SEM_DOWNLINK_MASK_TYPE_ENODEB_CATEGORY_BASED, 15.00e6, 0.00));
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    auto subblock_string_response = client::build_subblock_string(stub(), "", i);
    EXPECT_SUCCESS(session, subblock_string_response);
    EXPECT_SUCCESS(session, client::sem_cfg_component_carrier_maximum_output_power_array(stub(), session, subblock_string_response.selector_string_out(), {0.0}));
  }
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  SEMFetchSubblockMeasurementResponse sem_fetch_subblock_measurement_response;
  SEMFetchUpperOffsetMarginArrayResponse sem_fetch_upper_offset_margin_array_response;
  SEMFetchLowerOffsetMarginArrayResponse sem_fetch_lower_offset_margin_array_response;
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", i));
    sem_fetch_subblock_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_subblock_measurement(stub(), session, "", 10.0));
    for (int j = 0; j < NUMBER_OF_OFFSET_SEGMENT; j++) {
      sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, subblock_string_response.selector_string_out(), 10.0));
      sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, subblock_string_response.selector_string_out(), 10.0));
    }
  }
  const auto sem_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::sem_fetch_total_aggregated_power(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_LT(0.0, sem_fetch_subblock_measurement_response.subblock_power());
  EXPECT_LT(0.0, sem_fetch_subblock_measurement_response.integration_bandwidth());
  EXPECT_LT(0.0, sem_fetch_subblock_measurement_response.frequency());
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
  EXPECT_LT(0.0, sem_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(32411, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(32411, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(32411, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(32411, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxLTEDriverApiTests, ULLAAModAccMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  std::vector<float64> componentCarrierFrequency{-9.9e6, 9.9e6};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 50.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", 46));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_LAA, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), "", i));
    EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, carrier_string_response.selector_string_out(), 20e6, componentCarrierFrequency[i], 0));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrier_string_response.selector_string_out(), NIRFMXLTE_ATTRIBUTE_LAA_STARTING_SUBFRAME, 0));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrier_string_response.selector_string_out(), NIRFMXLTE_ATTRIBUTE_LAA_NUMBER_OF_SUBFRAMES, 1));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrier_string_response.selector_string_out(), NIRFMXLTE_ATTRIBUTE_LAA_UPLINK_START_POSITION, NIRFMXLTE_INT32_LAA_UPLINK_START_POSITION_00));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrier_string_response.selector_string_out(), NIRFMXLTE_ATTRIBUTE_LAA_UPLINK_ENDING_SYMBOL, NIRFMXLTE_INT32_LAA_UPLINK_ENDING_SYMBOL_13));
  }
  EXPECT_SUCCESS(session, client::cfg_auto_dmrs_detection_enabled(stub(), session, "", AUTO_DMRS_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_evm_unit(stub(), session, "", MODACC_EVM_UNIT_PERCENTAGE));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  std::vector<ModAccFetchPUSCHConstellationTraceResponse> mod_acc_fetch_pusch_constellation_trace_response_vec;
  std::vector<ModAccFetchEVMPerSubcarrierTraceResponse> mod_acc_fetch_evm_per_subcarrier_trace_response_vec;
  const auto mod_acc_fetch_composite_evm_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_composite_evm_array(stub(), session, "", 10.0));
  const auto mod_acc_fetch_iq_impairments_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments_array(stub(), session, "", 10.0));
  const auto mod_acc_fetch_in_band_emission_margin_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_in_band_emission_margin_array(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), "", i));
    mod_acc_fetch_pusch_constellation_trace_response_vec.push_back(EXPECT_SUCCESS(session, client::mod_acc_fetch_pusch_constellation_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0)));
    mod_acc_fetch_evm_per_subcarrier_trace_response_vec.push_back(EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_per_subcarrier_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0)));
  }

  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_frequency_error_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.mean_frequency_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_array_response.mean_frequency_error(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index().size());
  EXPECT_EQ(3, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index().size());
  EXPECT_LT(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index(0));
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index_size());
  EXPECT_EQ(2, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index().size());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset().size());
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance().size());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance(0));
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error_size());
  EXPECT_EQ(2, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error(0));
  EXPECT_EQ(2, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin_size());
  EXPECT_EQ(2, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin().size());
  EXPECT_EQ(0.0, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin(0));
  EXPECT_EQ(7200, mod_acc_fetch_pusch_constellation_trace_response_vec[0].data_constellation_size());
  EXPECT_EQ(7200, mod_acc_fetch_pusch_constellation_trace_response_vec[0].data_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response_vec[0].data_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response_vec[0].data_constellation(0).imaginary());
  EXPECT_EQ(1200, mod_acc_fetch_pusch_constellation_trace_response_vec[0].dmrs_constellation_size());
  EXPECT_EQ(1200, mod_acc_fetch_pusch_constellation_trace_response_vec[0].dmrs_constellation().size());
  EXPECT_LT(0.0, mod_acc_fetch_pusch_constellation_trace_response_vec[0].dmrs_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response_vec[0].dmrs_constellation(0).imaginary());
  EXPECT_EQ(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response_vec[0].x0());
  EXPECT_EQ(1.0, mod_acc_fetch_evm_per_subcarrier_trace_response_vec[0].dx());
  EXPECT_EQ(1200, mod_acc_fetch_evm_per_subcarrier_trace_response_vec[0].mean_rms_evm_per_subcarrier_size());
  EXPECT_EQ(1200, mod_acc_fetch_evm_per_subcarrier_trace_response_vec[0].mean_rms_evm_per_subcarrier().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response_vec[0].mean_rms_evm_per_subcarrier(0));
}

TEST_F(NiRFmxLTEDriverApiTests, ULModAccAcpChpObwSemCompositeContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  std::vector<float64> componentCarrierBandwidth{5e6, 10e6};
  std::vector<float64> componentCarrierFrequency{-9.225e6, 2.475e6};
  std::vector<int> cellID{0, 0};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", 1));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, "", componentCarrierBandwidth, componentCarrierFrequency, cellID));
  EXPECT_SUCCESS(session, client::cfg_auto_dmrs_detection_enabled(stub(), session, "", AUTO_DMRS_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP | MEASUREMENT_TYPES_CHP | MEASUREMENT_TYPES_MODACC | MEASUREMENT_TYPES_OBW | MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::sem_cfg_uplink_mask_type(stub(), session, "", SEM_UPLINK_MASK_TYPE_GENERAL_NS01));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_component_carrier_measurement_array_response = EXPECT_SUCCESS(session, client::sem_fetch_component_carrier_measurement_array(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::sem_fetch_total_aggregated_power(stub(), session, "", 10.0));
  const auto obw_fetch_measurement_response = EXPECT_SUCCESS(session, client::obw_fetch_measurement(stub(), session, "", 10.0));
  const auto chp_fetch_component_carrier_measurement_array_response = EXPECT_SUCCESS(session, client::chp_fetch_component_carrier_measurement_array(stub(), session, "", 10.0));
  const auto chp_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::chp_fetch_total_aggregated_power(stub(), session, "", 10.0));
  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_component_carrier_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_component_carrier_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::acp_fetch_total_aggregated_power(stub(), session, "", 10.0));

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
  EXPECT_EQ(2, sem_fetch_component_carrier_measurement_array_response.absolute_integrated_power_size());
  EXPECT_EQ(2, sem_fetch_component_carrier_measurement_array_response.absolute_integrated_power().size());
  EXPECT_GT(0.0, sem_fetch_component_carrier_measurement_array_response.absolute_integrated_power(0));
  EXPECT_EQ(2, sem_fetch_component_carrier_measurement_array_response.relative_integrated_power_size());
  EXPECT_EQ(2, sem_fetch_component_carrier_measurement_array_response.relative_integrated_power().size());
  EXPECT_GT(0.0, sem_fetch_component_carrier_measurement_array_response.relative_integrated_power(0));
  EXPECT_EQ(1, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
  EXPECT_EQ(2, chp_fetch_component_carrier_measurement_array_response.absolute_power_size());
  EXPECT_EQ(2, chp_fetch_component_carrier_measurement_array_response.absolute_power().size());
  EXPECT_GT(0.0, chp_fetch_component_carrier_measurement_array_response.absolute_power(0));
  EXPECT_EQ(2, chp_fetch_component_carrier_measurement_array_response.relative_power_size());
  EXPECT_EQ(2, chp_fetch_component_carrier_measurement_array_response.relative_power().size());
  EXPECT_GT(0.0, chp_fetch_component_carrier_measurement_array_response.relative_power(0));
  EXPECT_LT(0.0, chp_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_component_carrier_measurement_array_response.absolute_power_size());
  EXPECT_EQ(2, acp_fetch_component_carrier_measurement_array_response.absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_component_carrier_measurement_array_response.absolute_power(0));
  EXPECT_EQ(2, acp_fetch_component_carrier_measurement_array_response.relative_power_size());
  EXPECT_EQ(2, acp_fetch_component_carrier_measurement_array_response.relative_power().size());
  EXPECT_GT(0.0, acp_fetch_component_carrier_measurement_array_response.relative_power(0));
  EXPECT_LT(0.0, acp_fetch_total_aggregated_power_response.total_aggregated_power());
}

TEST_F(NiRFmxLTEDriverApiTests, ULModAccMIMOFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_SELECTOR_STRING = 256;
  const auto NUMBER_OF_SUBBLOCKS = 2;
  const auto NUMBER_OF_COMPONENT_CARRIERS = 1;
  std::vector<std::string> subblock_string_vec;
  const std::vector<float64> center_frequency_vec{1.95e9, 30e6};
  ModAccFetchPUSCHConstellationTraceResponse mod_acc_fetch_pusch_constellation_trace_response;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, NIRFMXLTE_INT32_DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_number_of_dut_antennas(stub(), session, "", 2));
  EXPECT_SUCCESS(session, client::cfg_transmit_antenna_to_analyze(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::cfg_number_of_subblocks(stub(), session, "", NUMBER_OF_SUBBLOCKS));
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    auto subblock_string_response = client::build_subblock_string(stub(), "", i);
    subblock_string_vec.push_back(subblock_string_response.selector_string_out());
    EXPECT_SUCCESS(session, subblock_string_response);
    EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, subblock_string_vec[i], center_frequency_vec[i]));
    EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, subblock_string_vec[i], COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
    EXPECT_SUCCESS(session, client::cfg_band(stub(), session, subblock_string_vec[i], 1));
    EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, subblock_string_vec[i], NUMBER_OF_COMPONENT_CARRIERS));
    EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, subblock_string_vec[i], {20e6}, {0.0}, {0}));
  }
  EXPECT_SUCCESS(session, client::cfg_auto_dmrs_detection_enabled(stub(), session, "", AUTO_DMRS_DETECTION_ENABLED_TRUE));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_evm_unit(stub(), session, "", MODACC_EVM_UNIT_PERCENTAGE));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_in_band_emission_mask_type(stub(), session, "", MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  ModAccFetchCompositeEVMArrayResponse mod_acc_fetch_composite_evm_array_response;
  ModAccFetchIQImpairmentsArrayResponse mod_acc_fetch_iq_impairments_array_response;
  ModAccFetchInBandEmissionMarginArrayResponse mod_acc_fetch_in_band_emission_margin_array_response;
  ModAccFetchEVMPerSubcarrierTraceResponse mod_acc_fetch_evm_per_subcarrier_trace_response;
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    mod_acc_fetch_composite_evm_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_composite_evm_array(stub(), session, subblock_string_vec[i], 10.0));
    mod_acc_fetch_iq_impairments_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments_array(stub(), session, subblock_string_vec[i], 10.0));
    mod_acc_fetch_in_band_emission_margin_array_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_in_band_emission_margin_array(stub(), session, subblock_string_vec[i], 10.0));
    for (int j = 0; j < NUMBER_OF_COMPONENT_CARRIERS; j++) {
      auto carrier_string_response = client::build_carrier_string(stub(), subblock_string_vec[i], j);
      EXPECT_SUCCESS(session, carrier_string_response);
      mod_acc_fetch_evm_per_subcarrier_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_per_subcarrier_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0));
    }
  }
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    auto carrier_string_response = client::build_carrier_string(stub(), subblock_string_vec[i], 0);
    EXPECT_SUCCESS(session, carrier_string_response);
    mod_acc_fetch_pusch_constellation_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_pusch_constellation_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0));
  }

  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.mean_rms_composite_evm(0));
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_composite_evm_array_response.maximum_peak_composite_evm(0));
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.mean_frequency_error_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.mean_frequency_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_array_response.mean_frequency_error(0));
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index().size());
  EXPECT_EQ(3, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_symbol_index(0));
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index().size());
  EXPECT_LT(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_subcarrier_index(0));
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index_size());
  EXPECT_EQ(1, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index().size());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_array_response.peak_composite_evm_slot_index(0));
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset_size());
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset().size());
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_origin_offset(0));
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance_size());
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance().size());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_gain_imbalance(0));
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error_size());
  EXPECT_EQ(1, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error().size());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_array_response.mean_iq_quadrature_error(0));
  EXPECT_EQ(1, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin_size());
  EXPECT_EQ(1, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin().size());
  EXPECT_EQ(0.0, mod_acc_fetch_in_band_emission_margin_array_response.in_band_emission_margin(0));
  EXPECT_EQ(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response.x0());
  EXPECT_EQ(1.0, mod_acc_fetch_evm_per_subcarrier_trace_response.dx());
  EXPECT_EQ(1200, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier_size());
  EXPECT_EQ(1200, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier(0));
  EXPECT_EQ(7200, mod_acc_fetch_pusch_constellation_trace_response.data_constellation_size());
  EXPECT_EQ(7200, mod_acc_fetch_pusch_constellation_trace_response.data_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.data_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.data_constellation(0).imaginary());
  EXPECT_EQ(1200, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation_size());
  EXPECT_EQ(1200, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation(0).imaginary());
}

TEST_F(NiRFmxLTEDriverApiTests, ULModAccSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  nidevice_grpc::Session session;
  ModAccFetchCompositeEVMResponse mod_acc_fetch_composite_evm_response;
  int attempts = 1;
  while (1) {
    session = init_session(stub(), PXI_5663E);
    EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
    EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
    EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
    EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 10e6, 0.0, 0));
    EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", 1));
    EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
    EXPECT_SUCCESS(session, client::cfg_auto_dmrs_detection_enabled(stub(), session, "", AUTO_DMRS_DETECTION_ENABLED_TRUE));
    EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_evm_unit(stub(), session, "", MODACC_EVM_UNIT_PERCENTAGE));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_in_band_emission_mask_type(stub(), session, "", MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS));
    EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
    EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

    // Intermittently gives "374603: Unable to synchronize." and outputs nan values
    mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.0);
    if (mod_acc_fetch_composite_evm_response.status() == SYNC_FAILURE_WARNING && attempts < 5) {
      TearDown();
      SetUp();
      ++attempts;
    }
    else {
      break;
    }
  }
  EXPECT_SUCCESS(session, mod_acc_fetch_composite_evm_response);
  if (mod_acc_fetch_composite_evm_response.status() != 0) {
    return;
  }
  const auto mod_acc_fetch_iq_impairments_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0));
  const auto mod_acc_fetch_in_band_emission_margin_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_in_band_emission_margin(stub(), session, "", 10.0));
  const auto mod_acc_fetch_pusch_constellation_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_pusch_constellation_trace(stub(), session, "", 10.0));
  const auto mod_acc_fetch_evm_per_subcarrier_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_per_subcarrier_trace(stub(), session, "", 10.0));

  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_symbol_index());
  EXPECT_LE(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_subcarrier_index());
  EXPECT_EQ(0, mod_acc_fetch_composite_evm_response.peak_composite_evm_slot_index());
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.mean_iq_quadrature_error());
  EXPECT_GT(0.0, mod_acc_fetch_in_band_emission_margin_response.in_band_emission_margin());
  EXPECT_EQ(144, mod_acc_fetch_pusch_constellation_trace_response.data_constellation_size());
  EXPECT_EQ(144, mod_acc_fetch_pusch_constellation_trace_response.data_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.data_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.data_constellation(0).imaginary());
  EXPECT_EQ(24, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation_size());
  EXPECT_EQ(24, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_pusch_constellation_trace_response.dmrs_constellation(0).imaginary());
  EXPECT_EQ(0.0, mod_acc_fetch_evm_per_subcarrier_trace_response.x0());
  EXPECT_EQ(1.0, mod_acc_fetch_evm_per_subcarrier_trace_response.dx());
  EXPECT_EQ(600, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier_size());
  EXPECT_EQ(600, mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier().size());
  EXPECT_TRUE(isnan(mod_acc_fetch_evm_per_subcarrier_trace_response.mean_rms_evm_per_subcarrier(0)));
}

TEST_F(NiRFmxLTEDriverApiTests, ULPvtSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 50.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, "", 10.0e6, 0.0, 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_PVT, true));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_TDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::pvt_cfg_measurement_method(stub(), session, "", PVT_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::pvt_cfg_off_power_exclusion_periods(stub(), session, "", 0.0, 0.0));
  EXPECT_SUCCESS(session, client::pvt_cfg_averaging(stub(), session, "", PVT_AVERAGING_ENABLED_FALSE, 10, PVT_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto pvt_fetch_signal_power_trace_response = EXPECT_SUCCESS(session, client::pvt_fetch_signal_power_trace(stub(), session, "", 10.0));
  const auto pvt_fetch_measurement_response = EXPECT_SUCCESS(session, client::pvt_fetch_measurement(stub(), session, "", 10.0));

  EXPECT_GT(0.0, pvt_fetch_signal_power_trace_response.x0());
  EXPECT_LT(0.0, pvt_fetch_signal_power_trace_response.dx());
  const auto signal_power_size = pvt_fetch_signal_power_trace_response.signal_power_size();
  EXPECT_LT(25000, signal_power_size);
  EXPECT_EQ(signal_power_size, pvt_fetch_signal_power_trace_response.signal_power().size());
  EXPECT_GT(0.0, pvt_fetch_signal_power_trace_response.signal_power(0));
  EXPECT_EQ(signal_power_size, pvt_fetch_signal_power_trace_response.absolute_limit_size());
  EXPECT_EQ(signal_power_size, pvt_fetch_signal_power_trace_response.absolute_limit().size());
  EXPECT_GT(0.0, pvt_fetch_signal_power_trace_response.absolute_limit(0));
  EXPECT_EQ(0, pvt_fetch_measurement_response.measurement_status());
  EXPECT_LT(0.0, pvt_fetch_measurement_response.mean_absolute_off_power_before());
  EXPECT_LT(0.0, pvt_fetch_measurement_response.mean_absolute_off_power_after());
  // Sometimes nan: EXPECT_LT(0.0, pvt_fetch_measurement_response.mean_absolute_on_power());
  EXPECT_LT(0.0, pvt_fetch_measurement_response.burst_width());
}

TEST_F(NiRFmxLTEDriverApiTests, ULSlotPhaseContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  const auto NUMBER_OF_SLOTS = 20;
  std::vector<float64> componentCarrierBandwidth{20e6, 20e6};
  std::vector<float64> componentCarrierFrequency{-9.9e6, 9.9e6};
  std::vector<int> cellID{0, 1};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_spacing(stub(), session, "", COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, -1));
  EXPECT_SUCCESS(session, client::cfg_number_of_component_carriers(stub(), session, "", NUMBER_OF_COMPONENT_CARRIERS));
  EXPECT_SUCCESS(session, client::cfg_component_carrier_array(stub(), session, "", componentCarrierBandwidth, componentCarrierFrequency, cellID));
  EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, UPLINK_DOWNLINK_CONFIGURATION_0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPHASE, true));
  EXPECT_SUCCESS(session, client::slot_phase_cfg_synchronization_mode_and_interval(stub(), session, "", SLOT_PHASE_SYNCHRONIZATION_MODE_SLOT, 0, NUMBER_OF_SLOTS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  SlotPhaseFetchPhaseDiscontinuitiesResponse slot_phase_fetch_phase_discontinuities_response;
  SlotPhaseFetchSamplePhaseErrorResponse slot_phase_fetch_sample_phase_error_response;
  SlotPhaseFetchSamplePhaseErrorLinearFitTraceResponse slot_phase_fetch_sample_phase_error_linear_fit_trace_response;
  const auto slot_phase_fetch_maximum_phase_discontinuity_array_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_maximum_phase_discontinuity_array(stub(), session, "", 10.0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), "", i));
    slot_phase_fetch_phase_discontinuities_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_phase_discontinuities(stub(), session, carrier_string_response.selector_string_out(), 10.0));
    slot_phase_fetch_sample_phase_error_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_sample_phase_error(stub(), session, carrier_string_response.selector_string_out(), 10.0));
    slot_phase_fetch_sample_phase_error_linear_fit_trace_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_sample_phase_error_linear_fit_trace(stub(), session, carrier_string_response.selector_string_out(), 10.0));
  }

  EXPECT_EQ(2, slot_phase_fetch_maximum_phase_discontinuity_array_response.maximum_phase_discontinuity_size());
  EXPECT_EQ(2, slot_phase_fetch_maximum_phase_discontinuity_array_response.maximum_phase_discontinuity().size());
  EXPECT_NE(0.0, slot_phase_fetch_maximum_phase_discontinuity_array_response.maximum_phase_discontinuity(0));
  EXPECT_EQ(20, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity_size());
  EXPECT_EQ(20, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity().size());
  EXPECT_TRUE(isnan(slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity(0)));
  EXPECT_EQ(0.0, slot_phase_fetch_sample_phase_error_response.x0());
  EXPECT_LT(0.0, slot_phase_fetch_sample_phase_error_response.dx());
  EXPECT_EQ(307200, slot_phase_fetch_sample_phase_error_response.sample_phase_error_size());
  EXPECT_EQ(307200, slot_phase_fetch_sample_phase_error_response.sample_phase_error().size());
  EXPECT_NE(0.0, slot_phase_fetch_sample_phase_error_response.sample_phase_error(0));
  EXPECT_EQ(0.0, slot_phase_fetch_sample_phase_error_linear_fit_trace_response.x0());
  EXPECT_LT(0.0, slot_phase_fetch_sample_phase_error_linear_fit_trace_response.dx());
  EXPECT_EQ(307200, slot_phase_fetch_sample_phase_error_linear_fit_trace_response.sample_phase_error_linear_fit_size());
  EXPECT_EQ(307200, slot_phase_fetch_sample_phase_error_linear_fit_trace_response.sample_phase_error_linear_fit().size());
  EXPECT_NE(0.0, slot_phase_fetch_sample_phase_error_linear_fit_trace_response.sample_phase_error_linear_fit(0));
}

TEST_F(NiRFmxLTEDriverApiTests, ULSlotPowerSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  nidevice_grpc::Session session;
  BuildSubblockStringResponse subblock_string_response;
  BuildCarrierStringResponse carrier_string_response;
  SlotPowerFetchPowersResponse slot_power_fetch_powers_response;
  int attempts = 1;
  while (1) {
    session = init_session(stub(), PXI_5663E);
    EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
    EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
    EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
    subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", 0));
    carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), 0));
    EXPECT_SUCCESS(session, client::cfg_component_carrier(stub(), session, carrier_string_response.selector_string_out(), 10e+6, 0.0, 0));
    EXPECT_SUCCESS(session, client::cfg_duplex_scheme(stub(), session, "", DUPLEX_SCHEME_FDD, 0));
    EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPOWER, true));
    EXPECT_SUCCESS(session, client::slot_power_cfg_measurement_interval(stub(), session, "", 0, 10));
    EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

    // Intermittently gives "374603: Unable to synchronize." and outputs nan values
    slot_power_fetch_powers_response = client::slot_power_fetch_powers(stub(), session, "", 10.0);
    if (slot_power_fetch_powers_response.status() == SYNC_FAILURE_WARNING && attempts < 5) {
      TearDown();
      SetUp();
      ++attempts;
    }
    else {
      break;
    }
  }
  EXPECT_SUCCESS(session, slot_power_fetch_powers_response);
  if (slot_power_fetch_powers_response.status() != 0) {
    return;
  }

  EXPECT_EQ(10, slot_power_fetch_powers_response.subframe_power_size());
  EXPECT_EQ(10, slot_power_fetch_powers_response.subframe_power().size());
  EXPECT_LT(0.0, slot_power_fetch_powers_response.subframe_power(0));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxlte_session_tests.cpp sha256=63e9d8072ee982064ba9cfe5e4aeea5dd648c1710940371184f3549bdbaebda0 bytes=6930 -->
## FILE: source/tests/system/nirfmxlte_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxlte_session_tests.cpp`
- sha256: `63e9d8072ee982064ba9cfe5e4aeea5dd648c1710940371184f3549bdbaebda0`
- bytes: 6930

````cpp
#include "device_server.h"
#include "nirfmxlte/nirfmxlte_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxlte = nirfmxlte_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxLTESession = -380598;
const char* kRFmxLTETestRsrc = "FakeDevice";
const char* kRFmxLTEOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxLTETestSessionOne = "SessionOneName";
const char* kRFmxLTETestSessionTwo = "SessionTwoName";
const char* kRFmxLTETestInvalidRsrc = "";

class NiRFmxLTESessionTest : public ::testing::Test {
 protected:
  NiRFmxLTESessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxlte_stub_(rfmxlte::NiRFmxLTE::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxLTESessionTest() {}

  std::unique_ptr<rfmxlte::NiRFmxLTE::Stub>& GetStub()
  {
    return nirfmxlte_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxlte::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxlte::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxlte::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxlte::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxlte::NiRFmxLTE::Stub> nirfmxlte_stub_;
};

TEST_F(NiRFmxLTESessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxlte::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxLTESessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxlte::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxLTESessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxlte::InitializeResponse response;
    call_initialize(kRFmxLTETestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxLTESessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxlte::InitializeResponse init_response;
  call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxlte::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxlte::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxLTESessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxlte::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxlte::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxLTESessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxlte::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxLTETestRsrc, kRFmxLTEOptionsString, kRFmxLTETestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxlte::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxLTESession);
}

TEST_F(NiRFmxLTESessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxlte::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxLTESession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxnr_driver_api_tests.cpp sha256=1d9513dbf2a06389e6f0033fd206f4bec256b6282b5e1beb36c31449a7311205 bytes=61916 -->
## FILE: source/tests/system/nirfmxnr_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxnr_driver_api_tests.cpp`
- sha256: `1d9513dbf2a06389e6f0033fd206f4bec256b6282b5e1beb36c31449a7311205`
- bytes: 61916

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxnr/nirfmxnr_client.h"
#include "nirfsa/nirfsa_client.h"
#include "rfmx_macros.h"
#include "waveform_helpers.h"

using namespace ::testing;
using namespace nirfmxnr_grpc;
namespace client = nirfmxnr_grpc::experimental::client;
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
constexpr auto NR_SYNC_FAILURE_WARNING1 = 684300;
constexpr auto NR_SYNC_FAILURE_WARNING1_STR = "Failed to synchronize to the signal";
constexpr auto NR_SYNC_FAILURE_WARNING2 = 684004;
constexpr auto NR_SYNC_FAILURE_WARNING2_STR = "Failed to synchronize to at-least one of the CC's";
constexpr auto IVI_INVALID_VALUE_ERROR = -1074135024;
constexpr auto IVI_INVALID_VALUE_ERROR_STR = "Invalid value for parameter or property";
constexpr auto TYPE_MISMATCH_ERROR = -380251;
constexpr auto TYPE_MISMATCH_ERROR_STR = "Incorrect data type specified";

#define EXPECT_NR_SYNC_FAILURE_WARNING(session, response)                                      \
  if ((response).status() == NR_SYNC_FAILURE_WARNING1) {                                       \
    EXPECT_WARNING(NR_SYNC_FAILURE_WARNING1, NR_SYNC_FAILURE_WARNING1_STR, session, response); \
  }                                                                                            \
  else {                                                                                       \
    EXPECT_WARNING(NR_SYNC_FAILURE_WARNING2, NR_SYNC_FAILURE_WARNING2_STR, session, response); \
  }

class NiRFmxNRDriverApiTests : public Test {
 protected:
  NiRFmxNRDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxNR::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxNRDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxNR::Stub>& stub() const
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
  std::unique_ptr<NiRFmxNR::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

nirfsa_grpc::InitWithOptionsResponse init_rfsa(const nirfsa_client::StubPtr& stub, const std::string& resource_name)
{
  return nirfsa_client::init_with_options(stub, resource_name, false, false, "Simulate=1, DriverSetup=Model:5663E");
}

std::vector<nidevice_grpc::NIComplexNumber> complex_number_array(
    std::vector<double> reals,
    std::vector<double> imaginaries)
{
  return complex_array<double, nidevice_grpc::NIComplexNumber>(reals, imaginaries);
}

TEST_F(NiRFmxNRDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_RESPONSE_SUCCESS(init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxNRDriverApiTests, InitializeFromNIRFSA_Close_Succeeds)
{
  auto rfsa_stub = create_stub<nirfsa_grpc::NiRFSA>();
  auto init_rfsa_response = init_rfsa(rfsa_stub, "Sim");
  EXPECT_RESPONSE_SUCCESS(init_rfsa_response);
  auto init_response = client::initialize_from_nirfsa_session(stub(), init_rfsa_response.vi());
  auto session = init_response.instrument();
  EXPECT_RESPONSE_SUCCESS(init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxNRDriverApiTests, AcpNonContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_SUBBLOCKS = 2;
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  float64 centerFrequency[NUMBER_OF_SUBBLOCKS] = {3.5e9, 200.0e6};
  float64 componentCarrierFrequency[NUMBER_OF_SUBBLOCKS][NUMBER_OF_COMPONENT_CARRIERS] = {{-49.98e6, 50.01e6}, {-49.98e6, 50.01e6}};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "", RF_ATTENUATION_AUTO_TRUE, 10.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_NUMBER_OF_SUBBLOCKS, NUMBER_OF_SUBBLOCKS));
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", i));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_CENTER_FREQUENCY, centerFrequency[i]));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE, NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER, 15e3));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY, -1));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, subblock_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS, NUMBER_OF_COMPONENT_CARRIERS));
    const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), -1));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
    for (int j = 0; j < NUMBER_OF_COMPONENT_CARRIERS; j++) {
      const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), j));
      EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
      EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY, componentCarrierFrequency[i][j]));
    }
  }
  EXPECT_ERROR(IVI_INVALID_VALUE_ERROR, IVI_INVALID_VALUE_ERROR_STR, session, client::auto_level(stub(), session, "", 10.0e-3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  ACPFetchSubblockMeasurementResponse fetch_subblock_responses[NUMBER_OF_SUBBLOCKS];
  ACPFetchOffsetMeasurementResponse fetch_measurement_responses[NUMBER_OF_SUBBLOCKS];
  for (int i = 0; i < NUMBER_OF_SUBBLOCKS; i++) {
    const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", i));
    fetch_subblock_responses[i] = EXPECT_SUCCESS(session, client::acp_fetch_subblock_measurement(stub(), session, subblock_string_response.selector_string_out(), 10.0));
    fetch_measurement_responses[i] = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement(stub(), session, subblock_string_response.selector_string_out(), 10.0));
  }

  EXPECT_LT(0.0, fetch_subblock_responses[0].subblock_power());
  EXPECT_LT(0.0, fetch_subblock_responses[0].integration_bandwidth());
  EXPECT_LT(0.0, fetch_subblock_responses[0].frequency());
  EXPECT_LT(0.0, fetch_subblock_responses[1].subblock_power());
  EXPECT_LT(0.0, fetch_subblock_responses[1].integration_bandwidth());
  EXPECT_LT(0.0, fetch_subblock_responses[1].frequency());
  EXPECT_GT(0.0, fetch_measurement_responses[0].lower_relative_power());
  EXPECT_GT(0.0, fetch_measurement_responses[0].upper_relative_power());
  EXPECT_GT(0.0, fetch_measurement_responses[0].lower_absolute_power());
  EXPECT_GT(0.0, fetch_measurement_responses[0].upper_absolute_power());
  EXPECT_GT(0.0, fetch_measurement_responses[1].lower_relative_power());
  EXPECT_GT(0.0, fetch_measurement_responses[1].upper_relative_power());
  EXPECT_GT(0.0, fetch_measurement_responses[1].lower_absolute_power());
  EXPECT_GT(0.0, fetch_measurement_responses[1].upper_absolute_power());
}

TEST_F(NiRFmxNRDriverApiTests, ACPSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 3.5e9));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "", RF_ATTENUATION_AUTO_TRUE, 10.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 8.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  auto auto_level_response = EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 10.0e-3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  int32 arraySize = acp_fetch_offset_measurement_array_response.lower_relative_power_size();
  const auto acp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::acp_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  std::vector<ACPFetchRelativePowersTraceResponse> acp_fetch_relative_powers_trace_responses;
  for (int i = 0; i < arraySize; i++) {
    acp_fetch_relative_powers_trace_responses.push_back(client::acp_fetch_relative_powers_trace(stub(), session, "", 10.0, i));
    EXPECT_SUCCESS(session, acp_fetch_relative_powers_trace_responses.back());
  }
  const auto acp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::acp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_LT(0.0, auto_level_response.reference_level());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_LT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_LT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_LT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(3, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_LT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_GT(0.0, acp_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_EQ(0.0, acp_fetch_component_carrier_measurement_response.relative_power());
  for (int i = 0; i < arraySize; i++) {
    EXPECT_LT(0.0, acp_fetch_relative_powers_trace_responses[i].x0());
    EXPECT_LT(0.0, acp_fetch_relative_powers_trace_responses[i].dx());
    EXPECT_EQ(2, acp_fetch_relative_powers_trace_responses[i].relative_powers_trace_size());
    EXPECT_EQ(2, acp_fetch_relative_powers_trace_responses[i].relative_powers_trace().size());
    EXPECT_LE(0.0, acp_fetch_relative_powers_trace_responses[i].relative_powers_trace(0));
  }
  EXPECT_LT(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(59096, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(59096, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxNRDriverApiTests, ChpSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 8.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP, true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::chp_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto chp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::chp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_LT(0.0, chp_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_EQ(0.0, chp_fetch_component_carrier_measurement_response.relative_power());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_EQ(22933, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(22933, chp_fetch_spectrum_response.spectrum().size());
  int midpoint_x = 22933 / 2;
  EXPECT_LT(chp_fetch_spectrum_response.spectrum(0), chp_fetch_spectrum_response.spectrum(midpoint_x));
  EXPECT_LT(chp_fetch_spectrum_response.spectrum(22932), chp_fetch_spectrum_response.spectrum(midpoint_x));
}

TEST_F(NiRFmxNRDriverApiTests, DLModAccContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_SELECTOR_STRING = 256;
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  char carrierString[MAX_SELECTOR_STRING];
  std::vector<float64> componentCarrierFrequency{-49.98e6, 50.01e6};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_DOWNLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER, 15e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE, NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY, -1));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS, NUMBER_OF_COMPONENT_CARRIERS));
  const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", 0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), i));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY, componentCarrierFrequency[i]));
  }
  strcpy_s(carrierString, sizeof("carrier::all"), "carrier::all");
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrierString, NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrierString, NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME, NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME_FDD));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, carrierString, NIRFMXNR_ATTRIBUTE_DOWNLINK_TEST_MODEL, NIRFMXNR_INT32_DOWNLINK_TEST_MODEL_TM1_1));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_SYNCHRONIZATION_MODE, NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_SLOT));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_ENABLED, NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_COUNT, 10));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT, NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET, 0.0));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH, 1));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  std::vector<float64> compositeRMSEVMMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<float64> compositePeakEVMMaximum(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<int> compositePeakEVMSlotIndex(NUMBER_OF_COMPONENT_CARRIERS, 0);
  std::vector<int> compositePeakEVMSymbolIndex(NUMBER_OF_COMPONENT_CARRIERS, 0);
  std::vector<int> compositePeakEVMSubcarrierIndex(NUMBER_OF_COMPONENT_CARRIERS, 0);
  std::vector<float64> pdschRMSEVMMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<float64> componentCarrierFrequencyErrorMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<float64> componentCarrierIQOriginOffsetMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<float64> componentCarrierIQGainImbalanceMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  std::vector<float64> componentCarrierQuadratureErrorMean(NUMBER_OF_COMPONENT_CARRIERS, 0.0);
  ModAccFetchRMSEVMPerSubcarrierMeanTraceResponse mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[2];
  ModAccFetchRMSEVMPerSymbolMeanTraceResponse mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[2];
  ModAccFetchTransientPeriodLocationsTraceResponse mod_acc_fetch_transient_period_locations_trace_response[2];
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), i));
    auto modacc_results_composite_rms_evm_mean_response = client::get_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN);
    if (i == 0) {
      EXPECT_NR_SYNC_FAILURE_WARNING(session, modacc_results_composite_rms_evm_mean_response);
    }
    else {
      EXPECT_SUCCESS(session, modacc_results_composite_rms_evm_mean_response);
    }
    compositeRMSEVMMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN);
    compositePeakEVMMaximum[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_MAXIMUM);
    compositePeakEVMSlotIndex[i] = GET_ATTR_I32(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX);
    compositePeakEVMSymbolIndex[i] = GET_ATTR_I32(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX);
    compositePeakEVMSubcarrierIndex[i] = GET_ATTR_I32(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SUBCARRIER_INDEX);
    componentCarrierFrequencyErrorMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_FREQUENCY_ERROR_MEAN);
    componentCarrierIQOriginOffsetMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_ORIGIN_OFFSET_MEAN);
    componentCarrierIQGainImbalanceMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_IQ_GAIN_IMBALANCE_MEAN);
    componentCarrierQuadratureErrorMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN);
    pdschRMSEVMMean[i] = GET_ATTR_F64(session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN);
    mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[i] = client::mod_acc_fetch_rmsevm_per_subcarrier_mean_trace(stub(), session, carrier_string_response.selector_string_out(), 10.000000);
    EXPECT_NR_SYNC_FAILURE_WARNING(session, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[i]);
    mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[i] = client::mod_acc_fetch_rmsevm_per_symbol_mean_trace(stub(), session, carrier_string_response.selector_string_out(), 10.000000);
    EXPECT_NR_SYNC_FAILURE_WARNING(session, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[i]);
    mod_acc_fetch_transient_period_locations_trace_response[i] = client::mod_acc_fetch_transient_period_locations_trace(stub(), session, carrier_string_response.selector_string_out(), 10.000000);
    EXPECT_NR_SYNC_FAILURE_WARNING(session, mod_acc_fetch_transient_period_locations_trace_response[i]);
  }

  EXPECT_TRUE(isnan(compositeRMSEVMMean[0]));
  EXPECT_TRUE(isnan(compositeRMSEVMMean[1]));
  EXPECT_TRUE(isnan(compositePeakEVMMaximum[0]));
  EXPECT_TRUE(isnan(compositePeakEVMMaximum[1]));
  EXPECT_EQ(0, compositePeakEVMSlotIndex[0]);
  EXPECT_EQ(0, compositePeakEVMSlotIndex[1]);
  EXPECT_EQ(0, compositePeakEVMSymbolIndex[0]);
  EXPECT_EQ(0, compositePeakEVMSymbolIndex[1]);
  EXPECT_EQ(0, compositePeakEVMSubcarrierIndex[0]);
  EXPECT_EQ(0, compositePeakEVMSubcarrierIndex[1]);
  EXPECT_TRUE(isnan(componentCarrierFrequencyErrorMean[0]));
  EXPECT_TRUE(isnan(componentCarrierFrequencyErrorMean[1]));
  EXPECT_TRUE(isnan(componentCarrierIQOriginOffsetMean[0]));
  EXPECT_TRUE(isnan(componentCarrierIQOriginOffsetMean[1]));
  EXPECT_TRUE(isnan(componentCarrierIQGainImbalanceMean[0]));
  EXPECT_TRUE(isnan(componentCarrierIQGainImbalanceMean[1]));
  EXPECT_TRUE(isnan(componentCarrierQuadratureErrorMean[0]));
  EXPECT_TRUE(isnan(componentCarrierQuadratureErrorMean[1]));
  EXPECT_TRUE(isnan(pdschRMSEVMMean[0]));
  EXPECT_TRUE(isnan(pdschRMSEVMMean[1]));
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[0].x0());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[0].dx());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[0].rms_evm_per_subcarrier_mean_size());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[0].rms_evm_per_subcarrier_mean().size());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[1].x0());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[1].dx());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[1].rms_evm_per_subcarrier_mean_size());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response[1].rms_evm_per_subcarrier_mean().size());
  // EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_subcarrier_mean_trace_response.rms_evm_per_subcarrier_mean(0));
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[0].x0());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[0].dx());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[0].rms_evm_per_symbol_mean_size());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[0].rms_evm_per_symbol_mean().size());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[1].x0());
  EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[1].dx());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[1].rms_evm_per_symbol_mean_size());
  EXPECT_EQ(0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response[1].rms_evm_per_symbol_mean().size());
  // EXPECT_EQ(0.0, mod_acc_fetch_rmsevm_per_symbol_mean_trace_response.rms_evm_per_symbol_mean(0));
}

TEST_F(NiRFmxNRDriverApiTests, ObwSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 8.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_OBW_SPAN_AUTO, NIRFMXNR_INT32_OBW_SPAN_AUTO_TRUE));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "subblock0", NIRFMXNR_ATTRIBUTE_OBW_SPAN, 200e6));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_spectrum_response = EXPECT_SUCCESS(session, client::obw_fetch_spectrum(stub(), session, "", 10.0));
  const auto obw_fetch_measurement_response = EXPECT_SUCCESS(session, client::obw_fetch_measurement(stub(), session, "", 10.0));

  EXPECT_LT(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_EQ(40115, obw_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(40115, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, obw_fetch_spectrum_response.spectrum(0));
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
}

TEST_F(NiRFmxNRDriverApiTests, SemContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_SELECTOR_STRING = 256;
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  const auto NUMBER_OF_OFFSETS = 4;
  char carrierString[MAX_SELECTOR_STRING];
  std::vector<float64> componentCarrierFrequency{-49.98e6, 50.01e6};
  std::vector<float64> componentCarrierRatedOutputPower{0.0, 0.0};
  std::vector<float64> offsetStartFrequency{15.0e3, 1.5e6, 5.5e6, 40.3e6};
  std::vector<float64> offsetStopFrequency{985.0e3, 4.5e6, 39.3e6, 44.3e6};
  std::vector<int> offsetSideband{SEM_OFFSET_SIDEBAND_BOTH, SEM_OFFSET_SIDEBAND_BOTH, SEM_OFFSET_SIDEBAND_BOTH, SEM_OFFSET_SIDEBAND_BOTH};
  std::vector<float64> offsetRBW{10.0e3, 250.0e3, 1.0e6, 1.0e6};
  std::vector<int> offsetRBWFilterType{SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN, SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN, SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN, SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN};
  std::vector<int> bandwidthIntegral{3, 4, 1, 1};
  std::vector<int> limitFailMask{SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE, SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE, SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE, SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE};
  std::vector<float64> absoluteLimitStart{-22.5, -8.5, -11.5, -23.5};
  std::vector<float64> absoluteLimitStop{-22.5, -8.5, -11.5, -23.5};
  std::vector<float64> relativeLimitStart{-53.0, -53.0, -53.0, -53.0};
  std::vector<float64> relativeLimitStop{-60.0, -60.0, -60.0, -60.0};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER, 15e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE, NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY, -1));
  strcpy_s(carrierString, sizeof("carrier::all"), "carrier::all");
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrierString, NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS, NUMBER_OF_COMPONENT_CARRIERS));
  const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", 0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), i));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY, componentCarrierFrequency[i]));
  }
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_number_of_offsets(stub(), session, "", NUMBER_OF_OFFSETS));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_frequency_array(stub(), session, "", offsetStartFrequency, offsetStopFrequency, offsetSideband));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_rbw_filter_array(stub(), session, "", offsetRBW, offsetRBWFilterType));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_bandwidth_integral_array(stub(), session, "", bandwidthIntegral));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_limit_fail_mask_array(stub(), session, "", limitFailMask));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_absolute_limit_array(stub(), session, "", absoluteLimitStart, absoluteLimitStop));
  EXPECT_SUCCESS(session, client::sem_cfg_offset_relative_limit_array(stub(), session, "", relativeLimitStart, relativeLimitStop));
  EXPECT_SUCCESS(session, client::sem_cfg_uplink_mask_type(stub(), session, "", SEM_UPLINK_MASK_TYPE_GENERAL));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  int32 arraySize = sem_fetch_upper_offset_margin_array_response.measurement_status_size();
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_total_aggregated_power_response = EXPECT_SUCCESS(session, client::sem_fetch_total_aggregated_power(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

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
  EXPECT_LT(0.0, sem_fetch_total_aggregated_power_response.total_aggregated_power());
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(47906, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(47906, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(47906, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(47906, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxNRDriverApiTests, SemSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.0, 0.0, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 8.0e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_uplink_mask_type(stub(), session, "", SEM_UPLINK_MASK_TYPE_GENERAL));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 1.0e-3));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  int32 arraySize = sem_fetch_upper_offset_margin_array_response.measurement_status_size();
  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_component_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_component_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

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
  EXPECT_GT(0.0, sem_fetch_component_carrier_measurement_response.absolute_power());
  EXPECT_GT(0.0, sem_fetch_component_carrier_measurement_response.peak_absolute_power());
  EXPECT_LT(0.0, sem_fetch_component_carrier_measurement_response.peak_frequency());
  EXPECT_EQ(0.0, sem_fetch_component_carrier_measurement_response.relative_power());
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(25685, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(25685, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_EQ(25685, sem_fetch_spectrum_response.composite_mask_size());
  EXPECT_EQ(25685, sem_fetch_spectrum_response.composite_mask().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.composite_mask(0));
}

TEST_F(NiRFmxNRDriverApiTests, TxpContiguousMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_SELECTOR_STRING = 256;
  const auto NUMBER_OF_COMPONENT_CARRIERS = 2;
  char carrierString[MAX_SELECTOR_STRING];
  std::vector<float64> componentCarrierFrequency{-49.98e6, 50.01e6};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_LINK_DIRECTION, NIRFMXNR_INT32_LINK_DIRECTION_UPLINK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_CHANNEL_RASTER, 15e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_SPACING_TYPE, NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_AT_CENTER_FREQUENCY, -1));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_NUMBER_OF_COMPONENT_CARRIERS, NUMBER_OF_COMPONENT_CARRIERS));
  const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", 0));
  for (int i = 0; i < NUMBER_OF_COMPONENT_CARRIERS; i++) {
    const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), i));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 20e6));
    EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrier_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_FREQUENCY, componentCarrierFrequency[i]));
  }
  strcpy_s(carrierString, sizeof("carrier::all"), "carrier::all");
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, carrierString, NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 30e3));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_TXP, true));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_INTERVAL, 1.0e-3));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_TXP_MEASUREMENT_OFFSET, 0.0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_ENABLED, NIRFMXNR_INT32_TXP_AVERAGING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_TXP_AVERAGING_COUNT, 10));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto txp_fetch_measurement_response = EXPECT_SUCCESS(session, client::txp_fetch_measurement(stub(), session, "", 10.0));
  const auto txp_fetch_power_trace_response = EXPECT_SUCCESS(session, client::txp_fetch_power_trace(stub(), session, "", 10.0));

  EXPECT_LT(0.0, txp_fetch_measurement_response.average_power_mean());
  EXPECT_LT(0.0, txp_fetch_measurement_response.peak_power_maximum());
  EXPECT_EQ(0.0, txp_fetch_power_trace_response.x0());
  EXPECT_LT(0.0, txp_fetch_power_trace_response.dx());
  EXPECT_EQ(47925, txp_fetch_power_trace_response.power_size());
  EXPECT_EQ(47925, txp_fetch_power_trace_response.power().size());
  EXPECT_NE(0.0, txp_fetch_power_trace_response.power(0));
}

// Note: there aren't any complex attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxNRDriverApiTests, SetAttributeComplex_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663E);

  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_ni_complex_double_array(stub(), session, "", NIRFMXNR_ATTRIBUTE_SEM_OFFSET_START_FREQUENCY, complex_number_array({1.2, 2.2}, {1e6, 1.01e6})));
}

TEST_F(NiRFmxNRDriverApiTests, ULModAccSpeedOptimizedFromExample_FetchData_DataLooksReasonable)
{
  auto instr_stub = create_stub<nirfmxinstr_grpc::NiRFmxInstr>();
  const auto NUMBER_OF_RESOURCE_BLOCK_CLUSTERS = 1;
  std::vector<int> pusch_resource_block_offset(NUMBER_OF_RESOURCE_BLOCK_CLUSTERS, 0);
  std::vector<int> pusch_number_of_resource_blocks{-1};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e6));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_SELECTED_PORTS, std::string()));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 3.5e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, true));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_FREQUENCY_RANGE, NIRFMXNR_INT32_FREQUENCY_RANGE_RANGE2_1));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_COMPONENT_CARRIER_BANDWIDTH, 50e6));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_CELL_ID, 0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_BAND, 78));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_BANDWIDTH_PART_SUBCARRIER_SPACING, 120e3));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED, NIRFMXNR_INT32_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_TRANSFORM_PRECODING_ENABLED, NIRFMXNR_INT32_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_SLOT_ALLOCATION, std::string("0-Last")));
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_SYMBOL_ALLOCATION, std::string("0-Last")));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_MODULATION_TYPE, NIRFMXNR_INT32_PUSCH_MODULATION_TYPE_QPSK));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS, NUMBER_OF_RESOURCE_BLOCK_CLUSTERS));
  const auto subblock_string_response = EXPECT_SUCCESS(session, client::build_subblock_string(stub(), "", 0));
  const auto carrier_string_response = EXPECT_SUCCESS(session, client::build_carrier_string(stub(), subblock_string_response.selector_string_out(), 0));
  const auto bandwidth_part_string_response = EXPECT_SUCCESS(session, client::build_bandwidth_part_string(stub(), carrier_string_response.selector_string_out(), 0));
  const auto user_string_response = EXPECT_SUCCESS(session, client::build_user_string(stub(), bandwidth_part_string_response.selector_string_out(), 0));
  const auto pusch_string_response = EXPECT_SUCCESS(session, client::build_pusch_string(stub(), user_string_response.selector_string_out(), 0));
  for (int i = 0; i < NUMBER_OF_RESOURCE_BLOCK_CLUSTERS; i++) {
    const auto pusch_cluster_string_response = EXPECT_SUCCESS(session, client::build_pusch_cluster_string(stub(), pusch_string_response.selector_string_out(), i));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, pusch_cluster_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_PUSCH_RESOURCE_BLOCK_OFFSET, pusch_resource_block_offset[i]));
    EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, pusch_cluster_string_response.selector_string_out(), NIRFMXNR_ATTRIBUTE_PUSCH_NUMBER_OF_RESOURCE_BLOCKS, pusch_number_of_resource_blocks[i]));
  }
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER_MODE, NIRFMXNR_INT32_PUSCH_DMRS_POWER_MODE_CDM_GROUPS));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_POWER, 0.0));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_CONFIGURATION_TYPE, NIRFMXNR_INT32_PUSCH_DMRS_CONFIGURATION_TYPE_1));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_MAPPING_TYPE, NIRFMXNR_INT32_PUSCH_MAPPING_TYPE_A));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_TYPE_A_POSITION, 2));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_DURATION, NIRFMXNR_INT32_PUSCH_DMRS_DURATION_SINGLE_SYMBOL));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_PUSCH_DMRS_ADDITIONAL_POSITIONS, 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, false));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_SYNCHRONIZATION_MODE, NIRFMXNR_INT32_MODACC_SYNCHRONIZATION_MODE_FRAME));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_ENABLED, NIRFMXNR_INT32_MODACC_AVERAGING_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_AVERAGING_COUNT, 10));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH_UNIT, NIRFMXNR_INT32_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET, 0.0));
  EXPECT_SUCCESS(session, client::set_attribute_f64(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH, 1));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED, NIRFMXNR_INT32_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED, NIRFMXNR_INT32_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_FREQUENCY_ERROR_ESTIMATION, NIRFMXNR_INT32_MODACC_FREQUENCY_ERROR_ESTIMATION_DISABLED));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED, NIRFMXNR_INT32_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_PHASE_TRACKING_MODE, NIRFMXNR_INT32_MODACC_PHASE_TRACKING_MODE_DISABLED));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_TIMING_TRACKING_MODE, NIRFMXNR_INT32_MODACC_TIMING_TRACKING_MODE_DISABLED));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED, NIRFMXNR_INT32_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::set_attribute_i32(stub(), session, "", NIRFMXNR_ATTRIBUTE_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE, NIRFMXNR_INT32_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM));

  // READ TDMS File
  auto waveform = load_test_waveform_data<float, nidevice_grpc::NIComplexNumberF32>("NR_FR2_UL_SISO_CC-1_BW-50MHz_SCS-120kHz.json");
  EXPECT_SUCCESS(session, client::mod_acc_cfg_reference_waveform(stub(), session, "", waveform.t0, waveform.dt, waveform.data));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  float64 composite_rms_evm_mean = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN);
  float64 composite_peak_evm_maximum = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_COMPOSITE_PEAK_EVM_MAXIMUM);
  float64 pusch_data_rms_evm_mean = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN);
  float64 pusch_data_peak_evm_maximum = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM);
  float64 pusch_dmrs_rms_evm_mean = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN);
  float64 pusch_dmrs_peak_evm_maximum = GET_ATTR_F64(session, "", NIRFMXNR_ATTRIBUTE_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM);

  EXPECT_LT(0.0, composite_rms_evm_mean);
  EXPECT_LT(0.0, composite_peak_evm_maximum);
  EXPECT_LT(0.0, pusch_data_rms_evm_mean);
  EXPECT_LT(0.0, pusch_data_peak_evm_maximum);
  EXPECT_LT(0.0, pusch_dmrs_rms_evm_mean);
  EXPECT_LT(0.0, pusch_dmrs_peak_evm_maximum);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxnr_session_tests.cpp sha256=f42ce21c9de9b5a946caa90cdeab85d768b006ba6f139a89b1a2042255d9e41f bytes=6855 -->
## FILE: source/tests/system/nirfmxnr_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxnr_session_tests.cpp`
- sha256: `f42ce21c9de9b5a946caa90cdeab85d768b006ba6f139a89b1a2042255d9e41f`
- bytes: 6855

````cpp
#include "device_server.h"
#include "nirfmxnr/nirfmxnr_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxnr = nirfmxnr_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxNRSession = -380598;
const char* kRFmxNRTestRsrc = "FakeDevice";
const char* kRFmxNROptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxNRTestSessionOne = "SessionOne";
const char* kRFmxNRTestSessionTwo = "SessionTwo";
const char* kRFmxNRTestInvalidRsrc = "";

class NiRFmxNRSessionTest : public ::testing::Test {
 protected:
  NiRFmxNRSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxnr_stub_(rfmxnr::NiRFmxNR::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxNRSessionTest() {}

  std::unique_ptr<rfmxnr::NiRFmxNR::Stub>& GetStub()
  {
    return nirfmxnr_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxnr::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxnr::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxnr::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxnr::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxnr::NiRFmxNR::Stub> nirfmxnr_stub_;
};

TEST_F(NiRFmxNRSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxnr::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxNRSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxnr::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxNRSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxnr::InitializeResponse response;
    call_initialize(kRFmxNRTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxNRSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxnr::InitializeResponse init_response;
  call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxnr::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxnr::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxNRSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxnr::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxnr::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxNRSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxnr::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxNRTestRsrc, kRFmxNROptionsString, kRFmxNRTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxnr::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxNRSession);
}

TEST_F(NiRFmxNRSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxnr::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxNRSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxpulse_driver_api_tests.cpp sha256=1186ee75f58ca171ec0edd3628a7de4d06516132c829746ff47f0880525e3da0 bytes=1967 -->
## FILE: source/tests/system/nirfmxpulse_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxpulse_driver_api_tests.cpp`
- sha256: `1186ee75f58ca171ec0edd3628a7de4d06516132c829746ff47f0880525e3da0`
- bytes: 1967

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxpulse/nirfmxpulse_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxpulse_grpc;
namespace client = nirfmxpulse_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxPulseDriverApiTests : public Test {
 protected:
  NiRFmxPulseDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxPulse::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxPulseDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxPulse::Stub>& stub() const
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
  std::unique_ptr<NiRFmxPulse::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxPulseDriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxpulse_session_tests.cpp sha256=39a7a07a982a99b992b2b32d850c81250915e19ac6a6629138c551b5bb4f2865 bytes=7066 -->
## FILE: source/tests/system/nirfmxpulse_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxpulse_session_tests.cpp`
- sha256: `39a7a07a982a99b992b2b32d850c81250915e19ac6a6629138c551b5bb4f2865`
- bytes: 7066

````cpp
#include "device_server.h"
#include "nirfmxpulse/nirfmxpulse_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxpulse = nirfmxpulse_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxPulseSession = -380598;
const char* kRFmxPulseTestRsrc = "FakeDevice";
const char* kRFmxPulseOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxPulseTestSessionOne = "SessionOneName";
const char* kRFmxPulseTestSessionTwo = "SessionTwoName";
const char* kRFmxPulseTestInvalidRsrc = "";

class NiRFmxPulseSessionTest : public ::testing::Test {
 protected:
  NiRFmxPulseSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxpulse_stub_(rfmxpulse::NiRFmxPulse::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxPulseSessionTest() {}

  std::unique_ptr<rfmxpulse::NiRFmxPulse::Stub>& GetStub()
  {
    return nirfmxpulse_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxpulse::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxpulse::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxpulse::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxpulse::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxpulse::NiRFmxPulse::Stub> nirfmxpulse_stub_;
};

TEST_F(NiRFmxPulseSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxpulse::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxPulseSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxpulse::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxPulseSessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxpulse::InitializeResponse response;
    call_initialize(kRFmxPulseTestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxPulseSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxpulse::InitializeResponse init_response;
  call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxpulse::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxpulse::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxPulseSessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxpulse::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxpulse::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxPulseSessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxpulse::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxPulseTestRsrc, kRFmxPulseOptionsString, kRFmxPulseTestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxpulse::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxPulseSession);

}

TEST_F(NiRFmxPulseSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxpulse::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxPulseSession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxspecan_driver_api_tests.cpp sha256=751858a424795a1b3dd700e0ec94c4d38cb64c4ea8afe84bff536766c8816ae4 bytes=32189 -->
## FILE: source/tests/system/nirfmxspecan_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxspecan_driver_api_tests.cpp`
- sha256: `751858a424795a1b3dd700e0ec94c4d38cb64c4ea8afe84bff536766c8816ae4`
- bytes: 32189

````cpp
#include <gmock/gmock.h>

#include <nlohmann/json.hpp>
#include <thread>
#include <tuple>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxspecan/nirfmxspecan_client.h"
#include "rfmx_macros.h"
#include "tests/utilities/test_helpers.h"
#include "waveform_helpers.h"

using namespace nirfmxspecan_grpc;
namespace client = nirfmxspecan_grpc::experimental::client;
namespace instr_client = nirfmxinstr_grpc::experimental::client;
using namespace ::testing;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5663 = "5663";
constexpr auto INVALID_SESSION_HANDLE_ERROR = -380598;
constexpr auto DEVICE_IN_USE_ERROR = -380489;
constexpr auto IQ_FETCH_DELETED_RECORD_ERROR = -379451;
constexpr auto IQ_FETCH_DELETED_RECORD_ERROR_STR = "The requested record number is invalid";
constexpr auto READ_ONLY_ATTRIBUTE_ERROR = -380231;
constexpr auto READ_ONLY_ATTRIBUTE_ERROR_STR = "This attribute is read-only and cannot be written";
constexpr auto SYNCHRONIZATION_WARNING = 377652;
constexpr auto SYNCHRONIZATION_WARNING_STR = "Synchronization not found";
constexpr auto TYPE_MISMATCH_ERROR = -380251;
constexpr auto TYPE_MISMATCH_ERROR_STR = "Incorrect data type specified";

class NiRFmxSpecAnDriverApiTests : public ::testing::Test {
 protected:
  NiRFmxSpecAnDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxspecan_stub_(NiRFmxSpecAn::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiRFmxSpecAnDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiRFmxSpecAn::Stub>& stub()
  {
    return nirfmxspecan_stub_;
  }

  bool is_driver_session_valid(const instr_client::StubPtr& stub, const nidevice_grpc::Session& session)
  {
    try {
      auto response = instr_client::get_attribute_string(stub, session, "", nirfmxinstr_grpc::NiRFmxInstrAttribute::NIRFMXINSTR_ATTRIBUTE_INSTRUMENT_MODEL);
      EXPECT_EQ(0, response.status());
      return true;
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      const auto& error = ex.Trailers().find("ni-error")->second;
      return std::stoi(error) != INVALID_SESSION_HANDLE_ERROR;
    }
  }

  void config_dpd_reference_waveform(const nidevice_grpc::Session& session)
  {
    EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_DPD, true));
    auto waveform = load_test_waveform_data<float, nidevice_grpc::NIComplexNumberF32>("LTE20MHz Waveform (Two Subframes).json");
    EXPECT_SUCCESS(session, client::dpd_cfg_reference_waveform(stub(), session, "", waveform.t0, waveform.dt, waveform.data, false, DpdSignalType::DPD_SIGNAL_TYPE_MODULATED));
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxSpecAn::Stub> nirfmxspecan_stub_;
};

#define EXPECT_VALID_DRIVER_SESSION(session) \
  EXPECT_TRUE(is_driver_session_valid(create_stub<nirfmxinstr_grpc::NiRFmxInstr>(), session));

#define EXPECT_INVALID_DRIVER_SESSION(session) \
  EXPECT_FALSE(is_driver_session_valid(create_stub<nirfmxinstr_grpc::NiRFmxInstr>(), session));

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

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
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

TEST_F(NiRFmxSpecAnDriverApiTests, SpectrumBasicFromExample_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0, 0));
  EXPECT_SUCCESS(session, client::spectrum_cfg_span(stub(), session, "", 1e6));
  EXPECT_SUCCESS(session, client::spectrum_cfg_rbw_filter(stub(), session, "", true, 100e3, SpectrumRbwFilterType::SPECTRUM_RBW_FILTER_TYPE_GAUSSIAN));
  EXPECT_SUCCESS(session, client::spectrum_cfg_averaging(stub(), session, "", false, 10, SpectrumAveragingType::SPECTRUM_AVERAGING_TYPE_RMS));

  auto read_response = EXPECT_SUCCESS(session, client::spectrum_read(stub(), session, "", 10.0));

  EXPECT_EQ(1005, read_response.actual_array_size());
  EXPECT_EQ(1005, read_response.spectrum_size());
  EXPECT_EQ(1005, read_response.spectrum().size());
  int midpoint_x = 1005 / 2;
  EXPECT_LT(read_response.spectrum(0), read_response.spectrum(midpoint_x));
  EXPECT_LT(read_response.spectrum(1004), read_response.spectrum(midpoint_x));
}

TEST_F(NiRFmxSpecAnDriverApiTests, AcpBasicFromExample_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::set_attribute_string(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_SELECTED_PORTS, std::string("")));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", false, 10, AcpAveragingType::ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_carrier_and_offsets(stub(), session, "", 1e6, 2, 1e6));
  EXPECT_SUCCESS(session, client::acp_cfg_offset_array(stub(), session, "", {1.0e6, 2.0e6}, {}, {}));

  const auto read_response = EXPECT_SUCCESS(session, client::acp_read(stub(), session, "", 10.0));

  EXPECT_GT(read_response.carrier_absolute_power(), 0.0);
  EXPECT_LT(read_response.offset_ch0_lower_relative_power(), 0.0);
  EXPECT_LT(read_response.offset_ch0_upper_relative_power(), 0.0);
  EXPECT_LT(read_response.offset_ch1_lower_relative_power(), 0.0);
  EXPECT_LT(read_response.offset_ch1_upper_relative_power(), 0.0);
}

TEST_F(NiRFmxSpecAnDriverApiTests, FcntBasicFromExample_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::f_cnt_cfg_measurement_interval(stub(), session, "", 1e-3));
  EXPECT_SUCCESS(session, client::f_cnt_cfg_averaging(stub(), session, "", false, 10, FcntAveragingType::FCNT_AVERAGING_TYPE_MEAN));
  EXPECT_SUCCESS(session, client::f_cnt_cfg_rbw_filter(stub(), session, "", 100e3, FcntRbwFilterType::FCNT_RBW_FILTER_TYPE_NONE, 0.1));

  const auto read_response = EXPECT_SUCCESS(session, client::f_cnt_read(stub(), session, "", 10.0));

  EXPECT_GT(read_response.average_relative_frequency(), 0.0);
  EXPECT_GT(read_response.average_absolute_frequency(), read_response.average_relative_frequency());
  EXPECT_GT(read_response.mean_phase(), 0.0);
}

TEST_F(NiRFmxSpecAnDriverApiTests, SpurBasicFromExample_ReturnsMeasurementStatusFail)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_SPUR, true));
  EXPECT_SUCCESS(session, client::spur_cfg_number_of_ranges(stub(), session, "", 1));
  EXPECT_SUCCESS(session, client::spur_cfg_range_frequency_array(stub(), session, "", {1e9}, {1.5e9}, {true}));
  EXPECT_SUCCESS(session, client::spur_cfg_range_rbw_array(stub(), session, "", {false}, {30e3}, {SpurRbwFilterType::SPUR_RBW_FILTER_TYPE_GAUSSIAN}));
  EXPECT_SUCCESS(session, client::spur_cfg_range_absolute_limit_array(stub(), session, "", {}, {-10.0}, {}));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = EXPECT_SUCCESS(session, client::spur_fetch_measurement_status(stub(), session, "", 10.0));
  EXPECT_EQ(SpurMeasurementStatus::SPUR_MEASUREMENT_STATUS_FAIL, fetch_response.measurement_status());
}

TEST_F(NiRFmxSpecAnDriverApiTests, HarmFromExample_NoError)
{
  constexpr auto NUMBER_OF_HARMONICS = 3;
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_HARMONICS, true));
  EXPECT_SUCCESS(session, client::harm_cfg_fundamental_rbw(stub(), session, "", 100e3, HarmRbwFilterType::HARM_RBW_FILTER_TYPE_GAUSSIAN, 0.010));
  EXPECT_SUCCESS(session, client::harm_cfg_fundamental_measurement_interval(stub(), session, "", 1e-3));
  EXPECT_SUCCESS(session, client::harm_cfg_auto_harmonics(stub(), session, "", true));
  EXPECT_SUCCESS(session, client::harm_cfg_number_of_harmonics(stub(), session, "", NUMBER_OF_HARMONICS));
  EXPECT_SUCCESS(session, client::harm_cfg_averaging(stub(), session, "", false, 10, HarmAveragingType::HARM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_thd_response = EXPECT_SUCCESS(session, client::harm_fetch_thd(stub(), session, "", 10.0));
  const auto fetch_measurement_response = EXPECT_SUCCESS(session, client::harm_fetch_harmonic_measurement_array(stub(), session, "", 10.0));
  for (auto i = 0; i < NUMBER_OF_HARMONICS; ++i) {
    const auto harmonic_string_response = EXPECT_SUCCESS(session, client::build_harmonic_string(stub(), "", i));
    const auto power_trace_response = EXPECT_SUCCESS(session, client::harm_fetch_harmonic_power_trace(stub(), session, harmonic_string_response.selector_string_out(), 10.0));
  }
}

TEST_F(NiRFmxSpecAnDriverApiTests, AMPMFromExample_NoError)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(
      session,
      client::cfg_digital_edge_trigger(stub(), session, "", DigitalEdgeTriggerSource::DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DigitalEdgeTriggerEdge::DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, true));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_AMPM, true));
  EXPECT_SUCCESS(session, client::dpd_cfg_dut_average_input_power(stub(), session, "", -20.0));
  EXPECT_SUCCESS(
      session,
      client::ampm_cfg_reference_waveform(
          stub(),
          session,
          "",
          0.0,
          0.1,
          // Note: this is random data.
          complex_f32_array({0.7f, 0.5f, 0.0f, -0.5f, -0.7f}, {-1.5f, -1.7f, -2.0f, -2.3f, -2.5f}),
          false,
          AmpmSignalType::AMPM_SIGNAL_TYPE_MODULATED));
  EXPECT_SUCCESS(session, client::ampm_cfg_measurement_sample_rate(stub(), session, "", AmpmMeasurementSampleRateMode::AMPM_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM, 120e6));
  EXPECT_SUCCESS(session, client::ampm_cfg_measurement_interval(stub(), session, "", 100e-6));
  EXPECT_SUCCESS(session, client::ampm_cfg_threshold(stub(), session, "", true, -20.0, AmpmThresholdType::AMPM_THRESHOLD_TYPE_RELATIVE));
  EXPECT_SUCCESS(session, client::ampm_cfg_reference_power_type(stub(), session, "", AmpmReferencePowerType::AMPM_REFERENCE_POWER_TYPE_INPUT));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 20e6, 100e-6));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto dut_char_response = EXPECT_SUCCESS(session, client::ampm_fetch_dut_characteristics(stub(), session, "", 10.0));
  const auto error_response = EXPECT_SUCCESS(session, client::ampm_fetch_error(stub(), session, "", 10.0));
  const auto curve_fit_response = EXPECT_SUCCESS(session, client::ampm_fetch_curve_fit_residual(stub(), session, "", 10.0));
  const auto am_to_am_response = EXPECT_SUCCESS(session, client::ampm_fetch_am_to_am_trace(stub(), session, "", 10.0));
}

TEST_F(NiRFmxSpecAnDriverApiTests, LutDpdFromExample_ReturnsSynchronizationNotFoundWarningWithData)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FrequencyReferenceSource::FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DigitalEdgeTriggerSource::DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0, DigitalEdgeTriggerEdge::DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, true));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_DPD, true));
  auto waveform = load_test_waveform_data<float, nidevice_grpc::NIComplexNumberF32>("LTE20MHz Waveform (Two Subframes).json");
  EXPECT_SUCCESS(session, client::dpd_cfg_reference_waveform(stub(), session, "", waveform.t0, waveform.dt, waveform.data, false, DpdSignalType::DPD_SIGNAL_TYPE_MODULATED));
  EXPECT_SUCCESS(session, client::dpd_cfg_dut_average_input_power(stub(), session, "", 1e9));
  EXPECT_SUCCESS(session, client::dpd_cfg_dpd_model(stub(), session, "", DpdModel::DPD_MODEL_LOOKUP_TABLE));
  EXPECT_SUCCESS(session, client::dpd_cfg_lookup_table_threshold(stub(), session, "", true, -20.0, DpdLookupTableThresholdType::DPD_LOOKUP_TABLE_THRESHOLD_TYPE_RELATIVE));
  EXPECT_SUCCESS(session, client::dpd_cfg_lookup_table_step_size(stub(), session, "", 0.1));
  EXPECT_SUCCESS(session, client::dpd_cfg_measurement_interval(stub(), session, "", 100e-6));
  EXPECT_SUCCESS(session, client::dpd_cfg_measurement_sample_rate(stub(), session, "", DpdMeasurementSampleRateMode::DPD_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM, 120e6));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", -14.00));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  EXPECT_SUCCESS(session, client::dpd_cfg_apply_dpd_lookup_table_correction_type(stub(), session, "", DpdApplyDpdLookupTableCorrectionType::DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_AND_PHASE));

  const auto apply_response = client::dpd_apply_digital_predistortion(stub(), session, "", waveform.t0, waveform.dt, waveform.data, false, 10.0);
  EXPECT_WARNING(SYNCHRONIZATION_WARNING, SYNCHRONIZATION_WARNING_STR, session, apply_response);
  EXPECT_THAT(apply_response.waveform_out(), Not(IsEmpty()));
}

// Note: there aren't any complex attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxSpecAnDriverApiTests, SetAttributeComplex_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663);

  EXPECT_ERROR(
      READ_ONLY_ATTRIBUTE_ERROR, READ_ONLY_ATTRIBUTE_ERROR_STR, session,
      client::set_attribute_ni_complex_double_array(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_SEM_RESULTS_CARRIER_FREQUENCY, complex_number_array({1.2, 2.2}, {1e6, 1.01e6})));
}

// Note: there aren't any i8 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxSpecAnDriverApiTests, SetAttributeInt8_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663);

  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i8(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, 1));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u8(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, 1));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i8_array(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, {1, 0, -1, 0}));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u8_array(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, {1, 0, 1, 0}));
}

// Note: there aren't any i16 attributes in attributes.py, but this at least exercises the code.
TEST_F(NiRFmxSpecAnDriverApiTests, SetAttributeInt16_ExpectedError)
{
  const auto session = init_session(stub(), PXI_5663);

  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_i16(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, -400));
  EXPECT_ERROR(
      TYPE_MISMATCH_ERROR, TYPE_MISMATCH_ERROR_STR, session,
      client::set_attribute_u16(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, 400));
}

TEST_F(NiRFmxSpecAnDriverApiTests, SetAndGetAttributeInt32_Succeeds)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(
      session,
      client::set_attribute_i32(stub(), session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT, NiRFmxSpecAnInt32AttributeValues::NIRFMXSPECAN_INT32_NF_EXTERNAL_PREAMP_PRESENT_TRUE));
  // This is one way to get the driver in a state where we can get attributes
  EXPECT_SUCCESS(session, client::spectrum_read(stub(), session, "", 10.0));

  const auto nf_external_preamp_present = GET_ATTR_I32(session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_NF_EXTERNAL_PREAMP_PRESENT);

  EXPECT_EQ(NiRFmxSpecAnInt32AttributeValues::NIRFMXSPECAN_INT32_NF_EXTERNAL_PREAMP_PRESENT_TRUE, nf_external_preamp_present);
}

TEST_F(NiRFmxSpecAnDriverApiTests, SetAndGetAttributeString_Succeeds)
{
  auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(
      session,
      client::set_attribute_string(
          stub(),
          session,
          "",
          NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_SOURCE,
          NiRFmxSpecAnStringAttributeValuesMapped::NIRFMXSPECAN_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PFI0));
  // This is one way to get the driver in a state where we can get attributes
  EXPECT_SUCCESS(session, client::spectrum_read(stub(), session, "", 10.0));

  const auto digital_edge_trigger_source = GET_ATTR_STR(session, "", NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_SOURCE);

  EXPECT_EQ("PFI0", digital_edge_trigger_source);
}

TEST_F(NiRFmxSpecAnDriverApiTests, BuildSpurString_ReturnsSpurString)
{
  auto session = init_session(stub(), PXI_5663);
  const auto spur_string_response = EXPECT_SUCCESS(session, client::build_spur_string(stub(), "", 0));

  EXPECT_EQ(spur_string_response.selector_string_out(), "spur0");
}

TEST_F(NiRFmxSpecAnDriverApiTests, BuildIntermodString_ReturnsIntermodString)
{
  auto session = init_session(stub(), PXI_5663);

  const auto intermod_string_response = client::build_intermod_string(stub(), "channel", 10);
  EXPECT_SUCCESS(session, intermod_string_response);

  EXPECT_EQ(intermod_string_response.selector_string_out(), "channel/intermod10");
}

TEST_F(NiRFmxSpecAnDriverApiTests, DefaultConfiguration_IQFetchData_RecordIsDeleted)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_IQ, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000);
  EXPECT_SUCCESS(session, fetch_response);
  EXPECT_THAT(fetch_response.data(), Not(IsEmpty()));

  EXPECT_ERROR(
      IQ_FETCH_DELETED_RECORD_ERROR, IQ_FETCH_DELETED_RECORD_ERROR_STR, session,
      client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000));
}

TEST_F(NiRFmxSpecAnDriverApiTests, DefaultConfiguration_IQFetchDataFetchAllAvailable_DataIsFetched)
{
  constexpr auto FETCH_ALL_AVAILABLE = -1;
  constexpr auto EXPECTED_RECORD_COUNT = 50000;
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_IQ, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = client::iq_fetch_data(stub(), session, "", 10.0, 0, FETCH_ALL_AVAILABLE);
  EXPECT_SUCCESS(session, fetch_response);

  EXPECT_THAT(fetch_response.data(), Not(IsEmpty()));
  EXPECT_EQ(EXPECTED_RECORD_COUNT, fetch_response.data().size());
}

TEST_F(NiRFmxSpecAnDriverApiTests, DisableDeleteRecordOnFetch_IQFetchData_RecordIsStillAvailable)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_IQ, true));
  EXPECT_SUCCESS(
      session,
      client::set_attribute_i32(
          stub(),
          session,
          "",
          NiRFmxSpecAnAttribute::NIRFMXSPECAN_ATTRIBUTE_IQ_DELETE_RECORD_ON_FETCH,
          NiRFmxSpecAnInt32AttributeValues::NIRFMXSPECAN_INT32_IQ_DELETE_RECORD_ON_FETCH_FALSE));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000);
  EXPECT_SUCCESS(session, fetch_response);
  EXPECT_THAT(fetch_response.data(), Not(IsEmpty()));
  const auto fetch_response_2 = client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000);
  EXPECT_SUCCESS(session, fetch_response_2);

  EXPECT_THAT(fetch_response_2.data(), Not(IsEmpty()));
}

TEST_F(NiRFmxSpecAnDriverApiTests, ConfigureDPDLookupTableWithNoComplexGains_Initiate_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663);
  config_dpd_reference_waveform(session);
  EXPECT_SUCCESS(session, client::dpd_cfg_apply_dpd_user_lookup_table(stub(), session, "", {1.23f, 4.56f, 7.89f}, {}));

  const auto initiate_response = client::initiate(stub(), session, "", "");

  EXPECT_SUCCESS(session, initiate_response);
}

TEST_F(NiRFmxSpecAnDriverApiTests, ConfigureDPDLookupTableWithNoInputPowers_Initiate_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663);
  config_dpd_reference_waveform(session);
  EXPECT_SUCCESS(
      session,
      client::dpd_cfg_apply_dpd_user_lookup_table(
          stub(),
          session,
          "",
          {},
          complex_f32_array({0.7f, 0.5f, 0.0f, -0.5f, -0.7f}, {-1.5f, -1.7f, -2.0f, -2.3f, -2.5f})));

  const auto initiate_response = client::initiate(stub(), session, "", "");

  EXPECT_SUCCESS(session, initiate_response);
}

TEST_F(NiRFmxSpecAnDriverApiTests, ConfigureDPDLookupTableWithBothInputs_Initiate_Succeeds)
{
  const auto session = init_session(stub(), PXI_5663);
  config_dpd_reference_waveform(session);
  EXPECT_SUCCESS(
      session,
      client::dpd_cfg_apply_dpd_user_lookup_table(
          stub(),
          session,
          "",
          {1.23f, 4.56f, 7.89f},
          complex_f32_array({0.7f, 0.5f, 0.0f}, {-1.5f, -1.7f, -2.0f})));

  const auto initiate_response = client::initiate(stub(), session, "", "");

  EXPECT_SUCCESS(session, initiate_response);
}

void close_session(const client::StubPtr& stub, const nidevice_grpc::Session& session)
{
  EXPECT_RESPONSE_SUCCESS(client::close(stub, session, false));
}

void force_close_session(const client::StubPtr& stub, const nidevice_grpc::Session& session)
{
  EXPECT_RESPONSE_SUCCESS(client::close(stub, session, true));
}

class NiRFmxSpecAnDriverApiResourceInitTests : public NiRFmxSpecAnDriverApiTests,
                                               public ::testing::WithParamInterface<std::tuple<std::string, std::string>> {
};

// Implements a function object that can be used as the name generator
// for parameterized test suites instantiated from NiRFmxSpecAnDriverApiResourceInitTests.
class ResourceTuplePrinter {
 public:
  using ParamType = NiRFmxSpecAnDriverApiResourceInitTests::ParamType;
  std::string operator()(const TestParamInfo<ParamType>& info)
  {
    return sanitize_param<0>(info.param) + "__" + sanitize_param<1>(info.param);
  }

 private:
  // The parameterized test string can only have alphanumeric characters
  // and "_". Replace ","" with "_".
  template <size_t I>
  static std::string sanitize_param(const ParamType& param)
  {
    auto param_value = std::get<I>(param);
    auto pos = std::size_t{};
    while ((pos = param_value.find(",", pos)) != std::string::npos) {
      param_value.replace(pos, 1, "_");
    }

    if (param_value.empty()) {
      param_value = "NONAME";
    }

    return param_value;
  }
};

using ResourcePair = std::tuple<std::string, std::string>;

template <typename T>
inline std::vector<T> vector_concat(const std::vector<T>& first, const std::vector<T>& second)
{
  auto result = std::vector<T>(first);
  result.insert(result.end(), second.cbegin(), second.cend());
  return result;
}

// These will initialize as separate driver resource handles.
const auto INDEPENDENT_RESOURCES = std::vector<ResourcePair>{
    {"specan1", "specan2"},
    {"specan1,specan2", "specan3,specan4"},
    {"", ""},
    {"specan1", ""},
};

// These will initialize as the same driver resource handle, the second
// session will increment that resource's ref count.
const auto DUPLICATE_RESOURCES = std::vector<ResourcePair>{
    {"specan1", "specan1"},
    {"specan1,specan2", "specan2,specan1"},
    {"specan1,specan2", "specan1,specan2"},
    {"specan1,specan2,specan3", "specan3,specan1,specan2"},
};

// All of these are valid to initialize as separate grpc-device sessions at the same time.
// Internally, they may or may not be separate driver handles, but they will each have their
// own ref count.
const auto COMPATIBLE_RESOURCES = vector_concat(INDEPENDENT_RESOURCES, DUPLICATE_RESOURCES);

// These are conflicting because the second set overlaps the first set but IS NOT IDENTICAL.
const auto CONFLICTING_RESOURCES = std::vector<ResourcePair>{
    {"specan1", "specan1,specan2"},
    {"specan1,specan2", "specan1"},
    {"specan1,specan2", "specan1,specan2,specan3"},
};

using NiRFmxSpecAnDriverApiCompatibleResourceInitTests = NiRFmxSpecAnDriverApiResourceInitTests;
INSTANTIATE_TEST_SUITE_P(
    CompatibleResourceInitTestCases,
    NiRFmxSpecAnDriverApiCompatibleResourceInitTests,
    ValuesIn(COMPATIBLE_RESOURCES),
    ResourceTuplePrinter{});

TEST_P(NiRFmxSpecAnDriverApiCompatibleResourceInitTests, InitializeTwoCompatibleResourcesAsSeparateSessions_CloseEachSession_EachIsClosedIndependently)
{
  const auto session1 = init_session(stub(), PXI_5663, std::get<0>(GetParam()));
  const auto session2 = init_session(stub(), PXI_5663, std::get<1>(GetParam()));
  EXPECT_NE(session1.name(), session2.name());
  EXPECT_VALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);

  close_session(stub(), session1);
  EXPECT_INVALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);
  close_session(stub(), session2);
  EXPECT_INVALID_DRIVER_SESSION(session2);
}

// Same as NiRFmxSpecAnDriverApiSuccessfulResourceInitTests, but with 3 sessions instead of the standard 2.
TEST_F(NiRFmxSpecAnDriverApiTests, InitializeThreeIdenticalResourcesAsSeparateSessions_CloseEachSession_EachIsClosedIndependently)
{
  const auto session1 = init_session(stub(), PXI_5663, "specan1,specan2");
  const auto session2 = init_session(stub(), PXI_5663, "specan2,specan1");
  const auto session3 = init_session(stub(), PXI_5663, "specan1,specan2");
  EXPECT_NE(session1.name(), session2.name());
  EXPECT_NE(session1.name(), session3.name());
  EXPECT_NE(session2.name(), session3.name());
  EXPECT_VALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);
  EXPECT_VALID_DRIVER_SESSION(session3);

  close_session(stub(), session1);
  EXPECT_INVALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);
  EXPECT_VALID_DRIVER_SESSION(session3);
  close_session(stub(), session2);
  EXPECT_INVALID_DRIVER_SESSION(session2);
  EXPECT_VALID_DRIVER_SESSION(session3);
  close_session(stub(), session3);
  EXPECT_INVALID_DRIVER_SESSION(session3);
}

using NiRFmxSpecAnDriverApiIndependentResourceInitTests = NiRFmxSpecAnDriverApiResourceInitTests;
INSTANTIATE_TEST_SUITE_P(
    IndependentResourceInitTestCases,
    NiRFmxSpecAnDriverApiIndependentResourceInitTests,
    ValuesIn(INDEPENDENT_RESOURCES),
    ResourceTuplePrinter{});

TEST_P(NiRFmxSpecAnDriverApiIndependentResourceInitTests, InitializeTwoSessionsWithDifferentResources_ForceCloseOne_OtherIsStillValid)
{
  const auto session1 = init_session(stub(), PXI_5663, std::get<0>(GetParam()));
  const auto session2 = init_session(stub(), PXI_5663, std::get<1>(GetParam()));
  EXPECT_NE(session1.name(), session2.name());
  EXPECT_VALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);

  force_close_session(stub(), session1);

  EXPECT_INVALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);
}

using NiRFmxSpecAnDriverApiSameUnderlyingResourceInitTests = NiRFmxSpecAnDriverApiResourceInitTests;
INSTANTIATE_TEST_SUITE_P(
    SameUnderlyingResourceInitTestCases,
    NiRFmxSpecAnDriverApiSameUnderlyingResourceInitTests,
    ValuesIn(DUPLICATE_RESOURCES),
    ResourceTuplePrinter{});

TEST_P(NiRFmxSpecAnDriverApiSameUnderlyingResourceInitTests, InitializeTwoSessionsWithSameUnderlyingResource_ForceCloseOne_BothAreInvalid)
{
  const auto session1 = init_session(stub(), PXI_5663, std::get<0>(GetParam()));
  const auto session2 = init_session(stub(), PXI_5663, std::get<1>(GetParam()));
  EXPECT_NE(session1.name(), session2.name());
  EXPECT_VALID_DRIVER_SESSION(session1);
  EXPECT_VALID_DRIVER_SESSION(session2);

  force_close_session(stub(), session1);

  EXPECT_INVALID_DRIVER_SESSION(session1);
  EXPECT_INVALID_DRIVER_SESSION(session2);
}

using NiRFmxSpecAnDriverApiConflictingResourceInitTests = NiRFmxSpecAnDriverApiResourceInitTests;
INSTANTIATE_TEST_SUITE_P(
    ConflictingTestCases,
    NiRFmxSpecAnDriverApiConflictingResourceInitTests,
    ValuesIn(CONFLICTING_RESOURCES),
    ResourceTuplePrinter{});

TEST_P(NiRFmxSpecAnDriverApiConflictingResourceInitTests, InitializeResource_InitializeConflictingResourceSet_FailsWithDeviceInUseError)
{
  const auto session1 = init_session(stub(), PXI_5663, std::get<0>(GetParam()));
  EXPECT_VALID_DRIVER_SESSION(session1);

  EXPECT_THROW_DRIVER_ERROR({
    init(stub(), PXI_5663, std::get<1>(GetParam()));
  }, DEVICE_IN_USE_ERROR);
}

TEST_P(NiRFmxSpecAnDriverApiConflictingResourceInitTests, InitializeAndCloseResource_InitializeResourceThatWouldHaveConflicted_Succeeds)
{
  const auto session1 = init_session(stub(), PXI_5663, std::get<0>(GetParam()));
  EXPECT_VALID_DRIVER_SESSION(session1);
  close_session(stub(), session1);

  const auto second_init_response = init(stub(), PXI_5663, std::get<1>(GetParam()));

  EXPECT_SUCCESS(second_init_response.instrument(), second_init_response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxspecan_restricted_driver_api_tests.cpp sha256=08bfb622f11fb0dc72537040df8f5c9e6ee6965ebb404e52277fe4f08fe7c13b bytes=5046 -->
## FILE: source/tests/system/nirfmxspecan_restricted_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxspecan_restricted_driver_api_tests.cpp`
- sha256: `08bfb622f11fb0dc72537040df8f5c9e6ee6965ebb404e52277fe4f08fe7c13b`
- bytes: 5046

````cpp
#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include <thread>
#include <tuple>

#include "device_server.h"
#include "nirfmxinstr/nirfmxinstr_client.h"
#include "nirfmxspecan/nirfmxspecan_client.h"
#include "nirfmxspecan_restricted/nirfmxspecan_restricted_client.h"
#include "rfmx_macros.h"
#include "waveform_helpers.h"

using namespace nirfmxspecan_grpc;
using namespace nirfmxspecan_restricted_grpc;
namespace client = nirfmxspecan_grpc::experimental::client;
namespace instr_client = nirfmxinstr_grpc::experimental::client;
namespace restricted_client = nirfmxspecan_restricted_grpc::experimental::client;
using namespace ::testing;

namespace ni {
namespace tests {
namespace system {
namespace {

constexpr auto PXI_5663 = "5663";
constexpr auto IQ_FETCH_DELETED_RECORD_ERROR = -379451;
constexpr auto IQ_FETCH_DELETED_RECORD_ERROR_STR = "The requested record number is invalid";

class NiRFmxSpecAnRestrictedDriverApiTests : public ::testing::Test {
 protected:
  NiRFmxSpecAnRestrictedDriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxspecan_stub_(NiRFmxSpecAn::NewStub(device_server_->InProcessChannel())),
        nirfmxspecan_restricted_stub_(NiRFmxSpecAnRestricted::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }
  virtual ~NiRFmxSpecAnRestrictedDriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  template <typename TService>
  std::unique_ptr<typename TService::Stub> create_stub()
  {
    return TService::NewStub(device_server_->InProcessChannel());
  }

  std::unique_ptr<NiRFmxSpecAn::Stub>& stub()
  {
    return nirfmxspecan_stub_;
  }

  std::unique_ptr<NiRFmxSpecAnRestricted::Stub>& restricted_stub()
  {
    return nirfmxspecan_restricted_stub_;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<NiRFmxSpecAn::Stub> nirfmxspecan_stub_;
  std::unique_ptr<NiRFmxSpecAnRestricted::Stub> nirfmxspecan_restricted_stub_;
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

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  return init_session(stub, model, "FakeDevice");
}

TEST_F(NiRFmxSpecAnRestrictedDriverApiTests, IQFetchDataOverrideBehavior_DeleteOnFetch_RecordIsDeleted)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_IQ, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = restricted_client::iq_fetch_data_override_behavior(restricted_stub(), session, "", 10.0, 0, 1000, 1);
  EXPECT_SUCCESS(session, fetch_response);
  EXPECT_THAT(fetch_response.data(), Not(IsEmpty()));

  EXPECT_ERROR(
      IQ_FETCH_DELETED_RECORD_ERROR, IQ_FETCH_DELETED_RECORD_ERROR_STR, session,
      client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000));
}

TEST_F(NiRFmxSpecAnRestrictedDriverApiTests, IQFetchDataOverrideBehavior_NoDeleteOnFetch_RecordIsNotDeleted)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_IQ, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto fetch_response = restricted_client::iq_fetch_data_override_behavior(restricted_stub(), session, "", 10.0, 0, 1000, 2);
  EXPECT_SUCCESS(session, fetch_response);
  EXPECT_THAT(fetch_response.data(), Not(IsEmpty()));
  const auto fetch_response_2 = client::iq_fetch_data(stub(), session, "", 10.0, 0, 1000);
  EXPECT_SUCCESS(session, fetch_response_2);

  EXPECT_THAT(fetch_response_2.data(), Not(IsEmpty()));
}

TEST_F(NiRFmxSpecAnRestrictedDriverApiTests, CacheResult_ReturnsNonEmptyResult)
{
  const auto session = init_session(stub(), PXI_5663);
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MeasurementTypes::MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  auto read_response = EXPECT_SUCCESS(session, client::spectrum_read(stub(), session, "", 10.0));

  const auto response = restricted_client::cache_result(restricted_stub(), session, "", 512);
  EXPECT_SUCCESS(session, response);

  EXPECT_THAT(response.selector_string_out(), Not(IsEmpty()));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxspecan_session_tests.cpp sha256=357e1841f5c6bad48cf8dfc837528adaefb47078efedb4b92b2a09b12e31642c bytes=5391 -->
## FILE: source/tests/system/nirfmxspecan_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxspecan_session_tests.cpp`
- sha256: `357e1841f5c6bad48cf8dfc837528adaefb47078efedb4b92b2a09b12e31642c`
- bytes: 5391

````cpp
#include <gmock/gmock.h>

#include "device_server.h"
#include "nirfmxspecan/nirfmxspecan_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {

namespace rfmxspecan = nirfmxspecan_grpc;
using ::testing::IsEmpty;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxSpecAnSession = -380598;
const char* kRFmxSpecAnErrorResourceNotFoundMessage = "-200220: Device identifier is invalid.";
const char* kRFmxSpecAnTestRsrc = "FakeDevice";
const char* kRFmxSpecAnOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxSpecAnTestSession = "SessionName";
const char* kRFmxSpecAnTestInvalidRsrc = "";

class NiRFmxSpecAnSessionTest : public ::testing::Test {
 protected:
  NiRFmxSpecAnSessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxspecan_stub_(rfmxspecan::NiRFmxSpecAn::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxSpecAnSessionTest() {}

  std::unique_ptr<rfmxspecan::NiRFmxSpecAn::Stub>& GetStub()
  {
    return nirfmxspecan_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxspecan::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxspecan::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxspecan::NiRFmxSpecAn::Stub> nirfmxspecan_stub_;
};

TEST_F(NiRFmxSpecAnSessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxspecan::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxSpecAnTestRsrc, kRFmxSpecAnOptionsString, kRFmxSpecAnTestSession, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxSpecAnSessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxspecan::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxSpecAnTestRsrc, kRFmxSpecAnOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxSpecAnSessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxspecan::InitializeResponse init_response;
  call_initialize(kRFmxSpecAnTestRsrc, kRFmxSpecAnOptionsString, kRFmxSpecAnTestSession, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxspecan::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxspecan::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

// Note: the error_message is included in the Init response because querying for errors
// afterwards will fail to get the error_message if the request is handled on a different thread.
TEST_F(NiRFmxSpecAnSessionTest, InitWithErrorFromDriver_ReturnsDriverErrorWithUserErrorMessage)
{
  EXPECT_THROW_DRIVER_ERROR_WITH_SUBSTR({
    rfmxspecan::InitializeResponse init_response;
    call_initialize(kRFmxSpecAnTestInvalidRsrc, "", "", &init_response);
  }, kInvalidRsrc, kRFmxSpecAnErrorResourceNotFoundMessage);
}

TEST_F(NiRFmxSpecAnSessionTest, InitWithErrorFromDriver_ReinitSuccessfully_ErrorMessageIsEmpty)
{
  EXPECT_THROW({
    try {
      rfmxspecan::InitializeResponse failed_init_response;
      call_initialize(kRFmxSpecAnTestInvalidRsrc, "", "", &failed_init_response);
    }
    catch (const nidevice_grpc::experimental::client::grpc_driver_error& ex) {
      EXPECT_EQ(::grpc::StatusCode::UNKNOWN, ex.StatusCode());
      EXPECT_STREQ(kRFmxSpecAnErrorResourceNotFoundMessage, ex.what());
      throw;
    }
  }, nidevice_grpc::experimental::client::grpc_driver_error);

  rfmxspecan::InitializeResponse successful_init_response;
  auto status_two = call_initialize(kRFmxSpecAnTestRsrc, kRFmxSpecAnOptionsString, kRFmxSpecAnTestSession, &successful_init_response);

  EXPECT_EQ(::grpc::StatusCode::OK, status_two.error_code());
  EXPECT_THAT(status_two.error_message(), IsEmpty());
}

TEST_F(NiRFmxSpecAnSessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    ::grpc::ClientContext context;
    rfmxspecan::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(false);
    rfmxspecan::CloseResponse response;
    ::grpc::Status status = GetStub()->Close(&context, request, &response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
  }, kInvalidRFmxSpecAnSession);
}

}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxtdscdma_driver_api_tests.cpp sha256=c7f27d78e485ec76a5201dd40b61d7b5757fb0eb24fe0c2e236d864d7edda8f9 bytes=48008 -->
## FILE: source/tests/system/nirfmxtdscdma_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxtdscdma_driver_api_tests.cpp`
- sha256: `c7f27d78e485ec76a5201dd40b61d7b5757fb0eb24fe0c2e236d864d7edda8f9`
- bytes: 48008

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxtdscdma/nirfmxtdscdma_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxtdscdma_grpc;
namespace client = nirfmxtdscdma_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxTDSCDMADriverApiTests : public Test {
 protected:
  NiRFmxTDSCDMADriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxTDSCDMA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxTDSCDMADriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxTDSCDMA::Stub>& stub() const
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
  std::unique_ptr<NiRFmxTDSCDMA::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxTDSCDMADriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxTDSCDMADriverApiTests, AcpFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_OFFSETS = 2;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e+6));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.00));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 1.91e+9));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_reference_level(stub(), session, "", 0.00));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.000660));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::acp_cfg_number_of_offsets(stub(), session, "", NUMBER_OF_OFFSETS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto acp_fetch_offset_measurement_array_response = client::acp_fetch_offset_measurement_array(stub(), session, "", 10.00);
  const auto acp_fetch_carrier_absolute_power_response = client::acp_fetch_carrier_absolute_power(stub(), session, "", 10.00);
  const auto acp_fetch_spectrum_response = client::acp_fetch_spectrum(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, acp_fetch_offset_measurement_array_response);
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, acp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, acp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, acp_fetch_spectrum_response);
  EXPECT_NE(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_NE(0, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_NE(0, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, CdaFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_NUMBER_OF_USERS = 16;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10E+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91E+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CDA, true));
  EXPECT_SUCCESS(session, client::cda_cfg_averaging(stub(), session, "", CDA_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::cda_cfg_synchronization_mode_and_offset(stub(), session, "", CDA_SYNCHRONIZATION_MODE_SLOT, 0));
  EXPECT_SUCCESS(session, client::cda_cfg_measurement_channel(stub(), session, "", 16, 1));
  EXPECT_SUCCESS(session, client::cda_cfg_power_unit(stub(), session, "", CDA_POWER_UNIT_DB));
  EXPECT_SUCCESS(session, client::cfg_midamble_shift(stub(), session, "", MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT, MAX_NUMBER_OF_USERS, 8));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling_code(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto cda_fetch_iq_impairments_response = client::cda_fetch_iq_impairments(stub(), session, "", 10.00);
  const auto cda_fetch_code_domain_power_response = client::cda_fetch_code_domain_power(stub(), session, "", 10.00);
  const auto cda_fetch_symbol_evm_response = client::cda_fetch_symbol_evm(stub(), session, "", 10.00);
  const auto cda_fetch_mean_code_domain_power_trace_response = client::cda_fetch_mean_code_domain_power_trace(stub(), session, "", 10.00);
  const auto cda_fetch_mean_symbol_evm_trace_response = client::cda_fetch_mean_symbol_evm_trace(stub(), session, "", 10.00);
  const auto cda_fetch_symbol_constellation_trace_response = client::cda_fetch_symbol_constellation_trace(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, cda_fetch_iq_impairments_response);
  EXPECT_NE(0.0, cda_fetch_iq_impairments_response.iq_origin_offset());
  EXPECT_NE(0.0, cda_fetch_iq_impairments_response.iq_gain_imbalance());
  EXPECT_NE(0.0, cda_fetch_iq_impairments_response.iq_quadrature_error());
  EXPECT_SUCCESS(session, cda_fetch_code_domain_power_response);
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.mean_total_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.mean_total_active_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.mean_active_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.maximum_peak_active_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.mean_inactive_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_power_response.maximum_peak_inactive_power());
  EXPECT_SUCCESS(session, cda_fetch_symbol_evm_response);
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.mean_rms_symbol_evm());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.maximum_peak_symbol_evm());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.frequency_error());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.chip_rate_error());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.mean_rms_symbol_magnitude_error());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.mean_rms_symbol_phase_error());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.mean_symbol_power());
  EXPECT_SUCCESS(session, cda_fetch_mean_code_domain_power_trace_response);
  EXPECT_EQ(0, cda_fetch_mean_code_domain_power_trace_response.mean_code_domain_powers_size());
  EXPECT_EQ(0, cda_fetch_mean_code_domain_power_trace_response.mean_code_domain_powers().size());
  EXPECT_SUCCESS(session, cda_fetch_mean_symbol_evm_trace_response);
  EXPECT_EQ(0, cda_fetch_mean_symbol_evm_trace_response.mean_symbol_evm_size());
  EXPECT_EQ(0, cda_fetch_mean_symbol_evm_trace_response.mean_symbol_evm().size());
  EXPECT_SUCCESS(session, cda_fetch_symbol_constellation_trace_response);
}

TEST_F(NiRFmxTDSCDMADriverApiTests, ChpFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP , true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 660E-6));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_carrier_absolute_power_response = client::chp_fetch_carrier_absolute_power(stub(), session, "", 10.00);
  const auto chp_fetch_spectrum_response = client::chp_fetch_spectrum(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, chp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, chp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, chp_fetch_spectrum_response);
  EXPECT_NE(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_NE(0, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_NE(0, chp_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, chp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, ModAccFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_NUMBER_OF_USERS = 16;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10E+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91E+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 80E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC , true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling_code(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::cfg_midamble_shift(stub(), session, "", MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT, MAX_NUMBER_OF_USERS, 8));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.00);
  const auto mod_acc_fetch_data_evm_response = client::mod_acc_fetch_data_evm(stub(), session, "", 10.00);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "" , 10.00);
  const auto mod_acc_fetch_constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.00);
  const auto mod_acc_fetch_midamble_evm_response = client::mod_acc_fetch_midamble_evm(stub(), session, "", 10.00);
  const auto mod_acc_fetch_midamble_and_data_power_response = client::mod_acc_fetch_midamble_and_data_power(stub(), session, "", 10.00);
  const auto mod_acc_fetch_evm_trace_response = client::mod_acc_fetch_evm_trace(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, mod_acc_fetch_composite_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.peak_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.composite_rho());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.frequency_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.chip_rate_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_data_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_data_evm_response.rms_data_evm());
  EXPECT_NE(0.0, mod_acc_fetch_data_evm_response.peak_data_evm());
  EXPECT_NE(0.0, mod_acc_fetch_data_evm_response.data_rho());
  EXPECT_NE(0.0, mod_acc_fetch_data_evm_response.rms_data_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_data_evm_response.rms_data_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_quadrature_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).imaginary());
  EXPECT_SUCCESS(session, mod_acc_fetch_midamble_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_midamble_evm_response.rms_midamble_evm());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_evm_response.peak_midamble_evm());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_evm_response.midamble_rho());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_evm_response.rms_midamble_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_evm_response.rms_midamble_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_midamble_and_data_power_response);
  EXPECT_NE(0.0, mod_acc_fetch_midamble_and_data_power_response.midamble_power());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_and_data_power_response.data_field1_power());
  EXPECT_NE(0.0, mod_acc_fetch_midamble_and_data_power_response.data_field2_power());
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.evm(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, ModAccAcpChpObwSemCompositeFromExample_FetchData_DataLooksReasonable)
{
  const auto MAX_NUMBER_OF_USERS = 16;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 80E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC | MEASUREMENT_TYPES_SEM| MEASUREMENT_TYPES_ACP | MEASUREMENT_TYPES_CHP | MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::cfg_midamble_shift(stub(), session, "", MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT, MAX_NUMBER_OF_USERS, 8));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling_code(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.000660));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.000660));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.000660));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.000660));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.00);
  const auto acp_fetch_offset_measurement_array_response = client::acp_fetch_offset_measurement_array(stub(), session, "", 10.00);
  const auto acp_fetch_carrier_absolute_power_response = client::acp_fetch_carrier_absolute_power(stub(), session, "", 10.00);
  const auto chp_fetch_carrier_absolute_power_response = client::chp_fetch_carrier_absolute_power(stub(), session, "", 10.00);
  const auto obw_fetch_measurement_response = client::obw_fetch_measurement(stub(), session, "", 10.00);
  const auto sem_fetch_lower_offset_margin_array_response = client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.00);
  const auto sem_fetch_upper_offset_margin_array_response = client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.00);
  const auto sem_fetch_measurement_status_response = client::sem_fetch_measurement_status(stub(), session, "", 10.00);
  const auto sem_fetch_carrier_absolute_integrated_power_response = client::sem_fetch_carrier_absolute_integrated_power(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, mod_acc_fetch_composite_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.peak_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.composite_rho());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.frequency_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.chip_rate_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_phase_error());
  EXPECT_SUCCESS(session, acp_fetch_offset_measurement_array_response);
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_NE(0, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_NE(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, acp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, acp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, chp_fetch_carrier_absolute_power_response);
  EXPECT_NE(0.0, chp_fetch_carrier_absolute_power_response.carrier_absolute_power());
  EXPECT_SUCCESS(session, obw_fetch_measurement_response);
  EXPECT_NE(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_NE(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_NE(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_NE(0.0, obw_fetch_measurement_response.stop_frequency());
  EXPECT_SUCCESS(session, sem_fetch_lower_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_lower_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_upper_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_upper_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_measurement_status_response);
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, sem_fetch_carrier_absolute_integrated_power_response);
  EXPECT_NE(0.0, sem_fetch_carrier_absolute_integrated_power_response.carrier_absolute_integrated_power());
}

TEST_F(NiRFmxTDSCDMADriverApiTests, ModAccPilotFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10E+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91E+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 50E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::cfg_pilot(stub(), session, "", 0));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC , true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_averaging(stub(), session, "", MODACC_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_slot_type(stub(), session, "", MODACC_MEASUREMENT_SLOT_TYPE_PILOT));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_pilot_evm_response = client::mod_acc_fetch_pilot_evm(stub(), session, "", 10.00);
  const auto mod_acc_fetch_composite_evm_response = client::mod_acc_fetch_composite_evm(stub(), session, "", 10.00);
  const auto mod_acc_fetch_constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.00);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "" , 10.00);
  const auto mod_acc_fetch_evm_trace_response = client::mod_acc_fetch_evm_trace(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, mod_acc_fetch_pilot_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_pilot_evm_response.rms_pilot_evm());
  EXPECT_NE(0.0, mod_acc_fetch_pilot_evm_response.peak_pilot_evm());
  EXPECT_NE(0.0, mod_acc_fetch_pilot_evm_response.pilot_rho());
  EXPECT_NE(0.0, mod_acc_fetch_pilot_evm_response.rms_pilot_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_pilot_evm_response.rms_pilot_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_composite_evm_response);
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.peak_composite_evm());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.composite_rho());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.frequency_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.chip_rate_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_magnitude_error());
  EXPECT_NE(0.0, mod_acc_fetch_composite_evm_response.rms_composite_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).imaginary());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_quadrature_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_NE(0, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_NE(0.0, mod_acc_fetch_evm_trace_response.evm(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, ObwFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16e-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 660e-6));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_measurement_response = client::obw_fetch_measurement(stub(), session, "", 10.00);
  const auto obw_fetch_spectrum_response = client::obw_fetch_spectrum(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, obw_fetch_measurement_response);
  EXPECT_NE(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_NE(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_NE(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_NE(0.0, obw_fetch_measurement_response.stop_frequency());
  EXPECT_SUCCESS(session, obw_fetch_spectrum_response);
  EXPECT_NE(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_NE(0, obw_fetch_spectrum_response.spectrum_size());
  EXPECT_NE(0, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, obw_fetch_spectrum_response.spectrum(0));
}

// The following test is disabled because the simulated device session always returns an error:
// '-357830: Burst Timing Detection Failed. 0 midamble(s) found.'
TEST_F(NiRFmxTDSCDMADriverApiTests, DISABLED_PvtFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10E+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91E+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_PVT , true));
  EXPECT_SUCCESS(session, client::cfg_midamble_shift(stub(), session, "", MIDAMBLE_AUTO_DETECTION_MODE_MIDAMBLE_SHIFT, 16, 8));
  EXPECT_SUCCESS(session, client::pvt_cfg_measurement_method(stub(), session, "", PVT_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::pvt_cfg_averaging(stub(), session, "", PVT_AVERAGING_ENABLED_FALSE, 10, PVT_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto pvt_fetch_measurement_status_response = client::pvt_fetch_measurement_status(stub(), session, "", 10.00);
  const auto pvt_fetch_powers_response = client::pvt_fetch_powers(stub(), session, "", 10.00);
  const auto pvt_fetch_segment_measurement_array_response = client::pvt_fetch_segment_measurement_array(stub(), session, "", 10.00);
  const auto pvt_fetch_signal_power_trace_response = client::pvt_fetch_signal_power_trace(stub(), session, "", 10.00);

  EXPECT_SUCCESS(session, pvt_fetch_measurement_status_response);
  EXPECT_EQ(0, pvt_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, pvt_fetch_powers_response);
  EXPECT_NE(0.0, pvt_fetch_powers_response.mean_absolute_on_power());
  EXPECT_NE(0.0, pvt_fetch_powers_response.mean_absolute_off_power());
  EXPECT_SUCCESS(session, pvt_fetch_segment_measurement_array_response);
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_status_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_status().size());
  EXPECT_EQ(0, pvt_fetch_segment_measurement_array_response.segment_status(0));
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_margin_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_margin().size());
  EXPECT_NE(0.0, pvt_fetch_segment_measurement_array_response.segment_margin(0));
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_margin_time_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_margin_time().size());
  EXPECT_NE(0.0, pvt_fetch_segment_measurement_array_response.segment_margin_time(0));
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_mean_absolute_power_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_mean_absolute_power().size());
  EXPECT_NE(0.0, pvt_fetch_segment_measurement_array_response.segment_mean_absolute_power(0));
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_maximum_absolute_power_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_maximum_absolute_power().size());
  EXPECT_NE(0.0, pvt_fetch_segment_measurement_array_response.segment_maximum_absolute_power(0));
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_minimum_absolute_power_size());
  EXPECT_NE(0, pvt_fetch_segment_measurement_array_response.segment_minimum_absolute_power().size());
  EXPECT_NE(0.0, pvt_fetch_segment_measurement_array_response.segment_minimum_absolute_power(0));
  EXPECT_SUCCESS(session, pvt_fetch_signal_power_trace_response);
  EXPECT_NE(0.0, pvt_fetch_signal_power_trace_response.x0());
  EXPECT_NE(0.0, pvt_fetch_signal_power_trace_response.dx());
  EXPECT_NE(0, pvt_fetch_signal_power_trace_response.signal_power_size());
  EXPECT_NE(0, pvt_fetch_signal_power_trace_response.signal_power().size());
  EXPECT_NE(0.0, pvt_fetch_signal_power_trace_response.signal_power(0));
  EXPECT_NE(0, pvt_fetch_signal_power_trace_response.absolute_limit_size());
  EXPECT_NE(0, pvt_fetch_signal_power_trace_response.absolute_limit().size());
  EXPECT_NE(0.0, pvt_fetch_signal_power_trace_response.absolute_limit(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, SemFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10E+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91e+9, 0.000000, 0.000000));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.000000, 0.000000, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 660E-6));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto sem_fetch_lower_offset_margin_array_response = client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.000000);
  const auto sem_fetch_upper_offset_margin_array_response = client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.000000);
  const auto sem_fetch_measurement_status_response = client::sem_fetch_measurement_status(stub(), session, "", 10.000000);
  const auto sem_fetch_carrier_absolute_integrated_power_response = client::sem_fetch_carrier_absolute_integrated_power(stub(), session, "", 10.000000);
  const auto sem_fetch_spectrum_response = client::sem_fetch_spectrum(stub(), session, "", 10.000000);

  EXPECT_SUCCESS(session, sem_fetch_lower_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_lower_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_lower_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_lower_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_upper_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_upper_offset_margin_array_response);
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status().size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.measurement_status(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_frequency().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_frequency(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_absolute_power(0));
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power_size());
  EXPECT_NE(0, sem_fetch_upper_offset_margin_array_response.margin_relative_power().size());
  EXPECT_NE(0.0, sem_fetch_upper_offset_margin_array_response.margin_relative_power(0));
  EXPECT_SUCCESS(session, sem_fetch_measurement_status_response);
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, sem_fetch_carrier_absolute_integrated_power_response);
  EXPECT_NE(0.0, sem_fetch_carrier_absolute_integrated_power_response.carrier_absolute_integrated_power());
  EXPECT_SUCCESS(session, sem_fetch_spectrum_response);
  EXPECT_NE(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_NE(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_NE(0, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_NE(0, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, sem_fetch_spectrum_response.spectrum(0));
  EXPECT_NE(0, sem_fetch_spectrum_response.relative_mask_size());
  EXPECT_NE(0, sem_fetch_spectrum_response.relative_mask().size());
  EXPECT_NE(0.0, sem_fetch_spectrum_response.relative_mask(0));
  EXPECT_NE(0, sem_fetch_spectrum_response.absolute_mask_size());
  EXPECT_NE(0, sem_fetch_spectrum_response.absolute_mask().size());
  EXPECT_NE(0.0, sem_fetch_spectrum_response.absolute_mask(0));
}

TEST_F(NiRFmxTDSCDMADriverApiTests, SlotPowerFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_SLOTS = 28;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10.0e+6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.91e+9, 0.00, 0.00));
  EXPECT_SUCCESS(session, client::cfg_iq_power_edge_trigger(stub(), session, "", "0", IQ_POWER_EDGE_TRIGGER_SLOPE_RISING, -20.00, 0.00, TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO, 16E-6, IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE, true));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPOWER, true));
  EXPECT_SUCCESS(session, client::slot_power_cfg_measurement_length(stub(), session, "", NUMBER_OF_SLOTS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto slot_power_fetch_powers_response = client::slot_power_fetch_powers(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, slot_power_fetch_powers_response);
  EXPECT_NE(0, slot_power_fetch_powers_response.slot_power_size());
  EXPECT_NE(0, slot_power_fetch_powers_response.slot_power().size());
  EXPECT_NE(0.0, slot_power_fetch_powers_response.slot_power(0));
  EXPECT_NE(0, slot_power_fetch_powers_response.slot_power_delta_size());
  EXPECT_NE(0, slot_power_fetch_powers_response.slot_power_delta().size());
  EXPECT_NE(0.0, slot_power_fetch_powers_response.slot_power_delta(0));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxtdscdma_session_tests.cpp sha256=2e8adeeaf9e6c457772f03e5933425ce176146a6c83710bcb7601f725f42bebb bytes=7198 -->
## FILE: source/tests/system/nirfmxtdscdma_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxtdscdma_session_tests.cpp`
- sha256: `2e8adeeaf9e6c457772f03e5933425ce176146a6c83710bcb7601f725f42bebb`
- bytes: 7198

````cpp
#include "device_server.h"
#include "nirfmxtdscdma/nirfmxtdscdma_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxtdscdma = nirfmxtdscdma_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxTDSCDMASession = -380598;
const char* kRFmxTDSCDMATestRsrc = "FakeDevice";
const char* kRFmxTDSCDMAOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxTDSCDMATestSessionOne = "SessionOneName";
const char* kRFmxTDSCDMATestSessionTwo = "SessionTwoName";
const char* kRFmxTDSCDMATestInvalidRsrc = "";

class NiRFmxTDSCDMASessionTest : public ::testing::Test {
 protected:
  NiRFmxTDSCDMASessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxtdscdma_stub_(rfmxtdscdma::NiRFmxTDSCDMA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxTDSCDMASessionTest() {}

  std::unique_ptr<rfmxtdscdma::NiRFmxTDSCDMA::Stub>& GetStub()
  {
    return nirfmxtdscdma_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxtdscdma::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxtdscdma::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxtdscdma::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxtdscdma::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxtdscdma::NiRFmxTDSCDMA::Stub> nirfmxtdscdma_stub_;
};

TEST_F(NiRFmxTDSCDMASessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxtdscdma::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxTDSCDMASessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxtdscdma::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxTDSCDMASessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxtdscdma::InitializeResponse response;
    call_initialize(kRFmxTDSCDMATestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxTDSCDMASessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxtdscdma::InitializeResponse init_response;
  call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxtdscdma::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxtdscdma::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxTDSCDMASessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxtdscdma::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxtdscdma::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxTDSCDMASessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxtdscdma::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxTDSCDMATestRsrc, kRFmxTDSCDMAOptionsString, kRFmxTDSCDMATestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxtdscdma::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxTDSCDMASession);
}

TEST_F(NiRFmxTDSCDMASessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxtdscdma::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxTDSCDMASession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxvna_driver_api_tests.cpp sha256=55b3a207fb8e12a8ca3f9011444721c7271bb5aea9c0d16d77263257e0e1cbf8 bytes=1945 -->
## FILE: source/tests/system/nirfmxvna_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxvna_driver_api_tests.cpp`
- sha256: `55b3a207fb8e12a8ca3f9011444721c7271bb5aea9c0d16d77263257e0e1cbf8`
- bytes: 1945

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxvna/nirfmxvna_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxvna_grpc;
namespace client = nirfmxvna_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxVNADriverApiTests : public Test {
 protected:
  NiRFmxVNADriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxVNA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxVNADriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxVNA::Stub>& stub() const
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
  std::unique_ptr<NiRFmxVNA::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxVNADriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxvna_session_tests.cpp sha256=524f453634e0f86868d2e08d6ae8b301832ca79f6f50752b25e7ba49cda63694 bytes=6932 -->
## FILE: source/tests/system/nirfmxvna_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxvna_session_tests.cpp`
- sha256: `524f453634e0f86868d2e08d6ae8b301832ca79f6f50752b25e7ba49cda63694`
- bytes: 6932

````cpp
#include "device_server.h"
#include "nirfmxvna/nirfmxvna_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxvna = nirfmxvna_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxVNASession = -380598;
const char* kRFmxVNATestRsrc = "FakeDevice";
const char* kRFmxVNAOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxVNATestSessionOne = "SessionOneName";
const char* kRFmxVNATestSessionTwo = "SessionTwoName";
const char* kRFmxVNATestInvalidRsrc = "";

class NiRFmxVNASessionTest : public ::testing::Test {
 protected:
  NiRFmxVNASessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxvna_stub_(rfmxvna::NiRFmxVNA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxVNASessionTest() {}

  std::unique_ptr<rfmxvna::NiRFmxVNA::Stub>& GetStub()
  {
    return nirfmxvna_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxvna::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxvna::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxvna::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxvna::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxvna::NiRFmxVNA::Stub> nirfmxvna_stub_;
};

TEST_F(NiRFmxVNASessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxvna::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxVNASessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxvna::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxVNASessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxvna::InitializeResponse response;
    call_initialize(kRFmxVNATestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxVNASessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxvna::InitializeResponse init_response;
  call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxvna::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxvna::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxVNASessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxvna::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxvna::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxVNASessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxvna::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxVNATestRsrc, kRFmxVNAOptionsString, kRFmxVNATestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxvna::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxVNASession);

}

TEST_F(NiRFmxVNASessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxvna::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxVNASession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxwcdma_driver_api_tests.cpp sha256=71797dd89e2e026884389b6f3e5212b233287f7327ef471b160ca92fd7b41355 bytes=46813 -->
## FILE: source/tests/system/nirfmxwcdma_driver_api_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxwcdma_driver_api_tests.cpp`
- sha256: `71797dd89e2e026884389b6f3e5212b233287f7327ef471b160ca92fd7b41355`
- bytes: 46813

````cpp
#include <gtest/gtest.h>

#include "device_server.h"
#include "nirfmxwcdma/nirfmxwcdma_client.h"
#include "rfmx_macros.h"

using namespace ::testing;
using namespace nirfmxwcdma_grpc;
namespace client = nirfmxwcdma_grpc::experimental::client;

namespace ni {
namespace tests {
namespace system {
namespace {

const auto PXI_5663E = "5663E";

class NiRFmxWCDMADriverApiTests : public Test {
 protected:
  NiRFmxWCDMADriverApiTests()
      : device_server_(DeviceServerInterface::Singleton()),
        stub_(NiRFmxWCDMA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxWCDMADriverApiTests() {}

  void TearDown() override
  {
    device_server_->ResetServer();
  }

  const std::unique_ptr<NiRFmxWCDMA::Stub>& stub() const
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
  std::unique_ptr<NiRFmxWCDMA::Stub> stub_;
};

InitializeResponse init(const client::StubPtr& stub, const std::string& model)
{
  auto options = std::string("Simulate=1, DriverSetup=Model:") + model;
  return client::initialize(stub, "FakeDevice", options);
}

nidevice_grpc::Session init_session(const client::StubPtr& stub, const std::string& model)
{
  auto response = init(stub, model);
  auto session = response.instrument();
  EXPECT_RESPONSE_SUCCESS(response);
  return session;
}

TEST_F(NiRFmxWCDMADriverApiTests, Init_Close_Succeeds)
{
  auto init_response = init(stub(), PXI_5663E);
  auto session = init_response.instrument();
  EXPECT_SUCCESS(session, init_response);

  auto close_response = client::close(stub(), session, 0);

  EXPECT_RESPONSE_SUCCESS(close_response);
}

TEST_F(NiRFmxWCDMADriverApiTests, AcpMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_CARRIERS = 2;
  const auto NUMBER_OF_OFFSETS = 2;
  const std::vector<int> empty_int_vec;

  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 1.95e9));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "", RF_ATTENUATION_AUTO_TRUE, 10.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_contiguous_carriers(stub(), session, "", NUMBER_OF_CARRIERS, -1));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 0.01));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.001));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::acp_cfg_number_of_offsets(stub(), session, "", 2));
  EXPECT_SUCCESS(session, client::acp_cfg_offset_power_reference(stub(), session, "", ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE, 0));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  std::vector<ACPFetchAbsolutePowersTraceResponse> acp_fetch_absolute_powers_trace_response_vec;
  std::vector<ACPFetchRelativePowersTraceResponse> acp_fetch_relative_powers_trace_response_vec;
  const auto acp_fetch_offset_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_carrier_measurement_array_response = EXPECT_SUCCESS(session, client::acp_fetch_carrier_measurement_array(stub(), session, "", 10.0));
  const auto acp_fetch_total_carrier_power_response = EXPECT_SUCCESS(session, client::acp_fetch_total_carrier_power(stub(), session, "", 10.0));
  const auto acp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::acp_fetch_spectrum(stub(), session, "", 10.0));

  EXPECT_SUCCESS(session, acp_fetch_carrier_measurement_array_response);
  EXPECT_EQ(2, acp_fetch_carrier_measurement_array_response.absolute_power_size());
  EXPECT_EQ(2, acp_fetch_carrier_measurement_array_response.absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_carrier_measurement_array_response.absolute_power(0));
  EXPECT_EQ(2, acp_fetch_carrier_measurement_array_response.relative_power_size());
  EXPECT_EQ(2, acp_fetch_carrier_measurement_array_response.relative_power().size());
  EXPECT_GT(0.0, acp_fetch_carrier_measurement_array_response.relative_power(0));
  EXPECT_SUCCESS(session, acp_fetch_offset_measurement_array_response);
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, acp_fetch_total_carrier_power_response);
  EXPECT_GT(0.0, acp_fetch_total_carrier_power_response.total_carrier_power());
  EXPECT_SUCCESS(session, acp_fetch_spectrum_response);
  EXPECT_LT(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(19801, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(19801, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, AcpSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_OFFSETS = 2;

  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_frequency(stub(), session, "", 1.95e9 ));
  EXPECT_SUCCESS(session, client::cfg_external_attenuation(stub(), session, "", 0.0));
  EXPECT_SUCCESS(session, client::cfg_rf_attenuation(stub(), session, "",  RF_ATTENUATION_AUTO_TRUE, 10.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::auto_level(stub(), session, "", 0.01));

  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_ACP, true));
  EXPECT_SUCCESS(session, client::acp_cfg_measurement_method(stub(), session, "", ACP_MEASUREMENT_METHOD_NORMAL));
  EXPECT_SUCCESS(session, client::acp_cfg_averaging(stub(), session, "", ACP_AVERAGING_ENABLED_FALSE, 10, ACP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::acp_cfg_sweep_time(stub(), session, "", ACP_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::acp_cfg_noise_compensation_enabled(stub(), session, "", ACP_NOISE_COMPENSATION_ENABLED_FALSE));
  EXPECT_SUCCESS(session, client::acp_cfg_number_of_offsets(stub(), session, "", NUMBER_OF_OFFSETS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto acp_fetch_offset_measurement_array_response = client::acp_fetch_offset_measurement_array(stub(), session, "", 10.0);
  const auto acp_fetch_carrier_measurement_response = client::acp_fetch_carrier_measurement(stub(), session, "", 10.0);
  const auto acp_fetch_spectrum_response = client::acp_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, acp_fetch_offset_measurement_array_response);
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_relative_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_relative_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.lower_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.lower_absolute_power(0));
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power_size());
  EXPECT_EQ(2, acp_fetch_offset_measurement_array_response.upper_absolute_power().size());
  EXPECT_GT(0.0, acp_fetch_offset_measurement_array_response.upper_absolute_power(0));
  EXPECT_SUCCESS(session, acp_fetch_carrier_measurement_response);
  EXPECT_LT(0.0, acp_fetch_carrier_measurement_response.absolute_power());
  EXPECT_EQ(0.0, acp_fetch_carrier_measurement_response.relative_power());
  EXPECT_SUCCESS(session, acp_fetch_spectrum_response);
  EXPECT_LT(0.0, acp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, acp_fetch_spectrum_response.dx());
  EXPECT_EQ(16465, acp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(16465, acp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, acp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, ChpMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_CARRIERS = 2;
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_contiguous_carriers(stub(), session, "", NUMBER_OF_CARRIERS, -1));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP, true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_carrier_measurement_array_response = client::chp_fetch_carrier_measurement_array(stub(), session, "", 10.0);
  const auto chp_fetch_total_carrier_power_response = client::chp_fetch_total_carrier_power(stub(), session, "", 10.0);
  const auto chp_fetch_spectrum_response = client::chp_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, chp_fetch_carrier_measurement_array_response);
  EXPECT_EQ(2, chp_fetch_carrier_measurement_array_response.absolute_power_size());
  EXPECT_EQ(2, chp_fetch_carrier_measurement_array_response.absolute_power().size());
  EXPECT_GT(0.0, chp_fetch_carrier_measurement_array_response.absolute_power(0));
  EXPECT_GT(0.0, chp_fetch_carrier_measurement_array_response.absolute_power(1));
  EXPECT_EQ(2, chp_fetch_carrier_measurement_array_response.relative_power_size());
  EXPECT_EQ(2, chp_fetch_carrier_measurement_array_response.relative_power().size());
  EXPECT_GT(0.0, chp_fetch_carrier_measurement_array_response.relative_power(0));
  EXPECT_GT(0.0, chp_fetch_carrier_measurement_array_response.relative_power(1));
  EXPECT_SUCCESS(session, chp_fetch_total_carrier_power_response);
  EXPECT_LT(0.0, chp_fetch_total_carrier_power_response.total_carrier_power());
  EXPECT_SUCCESS(session, chp_fetch_spectrum_response);
  EXPECT_LT(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_EQ(8401, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(8401, chp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, chp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, ChpSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CHP, true));
  EXPECT_SUCCESS(session, client::chp_cfg_sweep_time(stub(), session, "", CHP_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::chp_cfg_averaging(stub(), session, "", CHP_AVERAGING_ENABLED_FALSE, 10, CHP_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto chp_fetch_carrier_measurement_response = EXPECT_SUCCESS(session, client::chp_fetch_carrier_measurement(stub(), session, "", 10.0));
  const auto chp_fetch_spectrum_response = EXPECT_SUCCESS(session, client::chp_fetch_spectrum(stub(), session, "", 10.0));
  EXPECT_SUCCESS(session, chp_fetch_carrier_measurement_response);
  EXPECT_NEAR(0.0, chp_fetch_carrier_measurement_response.absolute_power(), 10);
  EXPECT_NEAR(0.0, chp_fetch_carrier_measurement_response.relative_power(), 10);
  EXPECT_SUCCESS(session, chp_fetch_spectrum_response);
  EXPECT_LT(0.0, chp_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, chp_fetch_spectrum_response.dx());
  EXPECT_EQ(4201, chp_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(4201, chp_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, chp_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, CdaFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling(stub(), session, "", 0, UPLINK_SCRAMBLING_TYPE_LONG));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_CDA, true));
  EXPECT_SUCCESS(session, client::cda_cfg_synchronization_mode_and_interval(stub(), session, "", CDA_SYNCHRONIZATION_MODE_SLOT, 0, 1));
  EXPECT_SUCCESS(session, client::cda_cfg_measurement_channel(stub(), session, "", 256, 0, CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_BPSK_QPSK, BRANCH_Q));
  EXPECT_SUCCESS(session, client::cda_cfg_power_unit(stub(), session, "", CDA_POWER_UNIT_DB));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto cda_fetch_symbol_evm_response = EXPECT_SUCCESS(session, client::cda_fetch_symbol_evm(stub(), session, "", 10.0));
  const auto cda_fetch_code_domain_power_response = EXPECT_SUCCESS(session, client::cda_fetch_code_domain_power(stub(), session, "", 10.0));
  const auto cda_fetch_code_domain_i_and_q_power_response = EXPECT_SUCCESS(session, client::cda_fetch_code_domain_i_and_q_power(stub(), session, "", 10.0));
  const auto cda_fetch_symbol_evm_trace_response = EXPECT_SUCCESS(session, client::cda_fetch_symbol_evm_trace(stub(), session, "", 10.0));
  const auto cda_fetch_code_domain_i_and_q_power_trace_response = EXPECT_SUCCESS(session, client::cda_fetch_code_domain_i_and_q_power_trace(stub(), session, "", 10.0));

  EXPECT_SUCCESS(session, cda_fetch_symbol_evm_response);
  EXPECT_LT(0.0, cda_fetch_symbol_evm_response.rms_symbol_evm());
  EXPECT_LT(0.0, cda_fetch_symbol_evm_response.peak_symbol_evm());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.rms_symbol_magnitude_error());
  EXPECT_LT(0.0, cda_fetch_symbol_evm_response.rms_symbol_phase_error());
  EXPECT_GT(0.0, cda_fetch_symbol_evm_response.mean_symbol_power());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_response.chip_rate_error());
  EXPECT_SUCCESS(session, cda_fetch_code_domain_power_response);
  EXPECT_LE(0.0, cda_fetch_code_domain_power_response.total_power());
  EXPECT_NEAR(0.0, cda_fetch_code_domain_power_response.total_active_power(), 10);
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.mean_inactive_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_power_response.peak_inactive_power()));
  EXPECT_SUCCESS(session, cda_fetch_code_domain_i_and_q_power_response);
  EXPECT_NE(0.0, cda_fetch_code_domain_i_and_q_power_response.i_mean_active_power());
  EXPECT_NE(0.0, cda_fetch_code_domain_i_and_q_power_response.q_mean_active_power());
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.i_peak_inactive_power()));
  EXPECT_TRUE(isnan(cda_fetch_code_domain_i_and_q_power_response.q_peak_inactive_power()));
  EXPECT_SUCCESS(session, cda_fetch_symbol_evm_trace_response);
  EXPECT_EQ(10, cda_fetch_symbol_evm_trace_response.symbol_evm_size());
  EXPECT_EQ(10, cda_fetch_symbol_evm_trace_response.symbol_evm().size());
  EXPECT_NE(0.0, cda_fetch_symbol_evm_trace_response.symbol_evm(0));
  EXPECT_SUCCESS(session, cda_fetch_code_domain_i_and_q_power_trace_response);
  EXPECT_EQ(256, cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers_size());
  EXPECT_EQ(256, cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers().size());
  EXPECT_NE(0.0, cda_fetch_code_domain_i_and_q_power_trace_response.i_code_domain_powers(0));
  EXPECT_EQ(256, cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers_size());
  EXPECT_EQ(256, cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers().size());
  EXPECT_NE(0.0, cda_fetch_code_domain_i_and_q_power_trace_response.q_code_domain_powers(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, ModAccMarkerModeFromExample_FetchData_DataLooksReasonable)
{
  const auto NUMBER_OF_USER_DEFINED_CHANNELS = 2;
  std::vector<int> spreadingFactor {256,64};
  std::vector<int> spreadingCode {0,16};
  std::vector<int> modulationType {MODULATION_TYPE_BPSK_QPSK, MODULATION_TYPE_BPSK_QPSK};
  std::vector<int> branch {BRANCH_Q, BRANCH_I};
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, true));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling(stub(), session, "", 0x0, UPLINK_SCRAMBLING_TYPE_LONG));
  EXPECT_SUCCESS(session, client::cfg_channel_configuration_mode(stub(), session, "", CHANNEL_CONFIGURATION_MODE_TEST_MODEL));
  EXPECT_SUCCESS(session, client::cfg_uplink_test_model(stub(), session, "", UPLINK_TEST_MODEL_R6C_2_1));  
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true));
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_MARKER, 0, 1));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_reference_waveform_response = client::mod_acc_fetch_reference_waveform(stub(), session, "", 10.0);  
  std::vector<nidevice_grpc::NIComplexNumberF32> reference_waveform;
  for( int i = 0; i< mod_acc_fetch_reference_waveform_response.reference_waveform_size(); i++)
  {
    reference_waveform.push_back( mod_acc_fetch_reference_waveform_response.reference_waveform(i));
  }

  EXPECT_SUCCESS(session, client::mod_acc_cfg_reference_waveform(stub(), session, "", mod_acc_fetch_reference_waveform_response.x0(), mod_acc_fetch_reference_waveform_response.dx(), reference_waveform));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  const auto mod_acc_fetch_evm_response = client::mod_acc_fetch_evm(stub(), session, "", 10.0);
  const auto mod_acc_fetch_iq_impairments_response = client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0);
  const auto mod_acc_fetch_peak_cde_response = client::mod_acc_fetch_peak_cde(stub(), session, "", 10.0);
  const auto mod_acc_fetch_peak_active_cde_response = client::mod_acc_fetch_peak_active_cde(stub(), session, "", 10.0);
  const auto mod_acc_fetch_rcde_response = client::mod_acc_fetch_rcde(stub(), session, "", 10.0);
  const auto mod_acc_fetch_evm_trace_response = client::mod_acc_fetch_evm_trace(stub(), session, "", 10.0);
  const auto mod_acc_fetch_constellation_trace_response = client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, mod_acc_fetch_reference_waveform_response);
  EXPECT_EQ(0.0, mod_acc_fetch_reference_waveform_response.x0());
  EXPECT_LT(0.0, mod_acc_fetch_reference_waveform_response.dx());
  EXPECT_LT(0.0, mod_acc_fetch_reference_waveform_response.reference_waveform(0).real());
  EXPECT_LT(0.0, mod_acc_fetch_reference_waveform_response.reference_waveform(0).imaginary());
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_response);
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_evm());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.peak_evm());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rho());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.frequency_error());
  EXPECT_EQ(0.0, mod_acc_fetch_evm_response.chip_rate_error());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_magnitude_error());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_response.iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_quadrature_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_cde_response);
  EXPECT_LT(0.0, mod_acc_fetch_peak_cde_response.peak_cde());
  EXPECT_LE(0, mod_acc_fetch_peak_cde_response.peak_cde_code());
  EXPECT_LE(0, mod_acc_fetch_peak_cde_response.peak_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_active_cde_response);
  EXPECT_LT(0.0, mod_acc_fetch_peak_active_cde_response.peak_active_cde());
  EXPECT_EQ(64, mod_acc_fetch_peak_active_cde_response.peak_active_cde_spreading_factor());
  EXPECT_EQ(16, mod_acc_fetch_peak_active_cde_response.peak_active_cde_code());
  EXPECT_EQ(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_rcde_response);
  EXPECT_LT(0.0, mod_acc_fetch_rcde_response.peak_rcde());
  EXPECT_LE(64, mod_acc_fetch_rcde_response.peak_rcde_spreading_factor());
  EXPECT_LE(0, mod_acc_fetch_rcde_response.peak_rcde_code());
  EXPECT_LE(0, mod_acc_fetch_rcde_response.peak_rcde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_LT(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_LT(2000, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_LT(2000, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_trace_response.evm(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).imaginary());
}

TEST_F(NiRFmxWCDMADriverApiTests, ModAccSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  nidevice_grpc::Session session;

  session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling(stub(), session, "", 0, UPLINK_SCRAMBLING_TYPE_LONG));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_MODACC, true)); 
  EXPECT_SUCCESS(session, client::mod_acc_cfg_synchronization_mode_and_interval(stub(), session, "", MODACC_SYNCHRONIZATION_MODE_SLOT, 0, 1));  
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto mod_acc_fetch_evm_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm(stub(), session, "", 10.0));
  const auto mod_acc_fetch_iq_impairments_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_iq_impairments(stub(), session, "", 10.0));
  const auto mod_acc_fetch_peak_cde_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_peak_cde(stub(), session, "", 10.0));
  const auto mod_acc_fetch_peak_active_cde_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_peak_active_cde(stub(), session, "", 10.0));
  const auto mod_acc_fetch_rcde_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_rcde(stub(), session, "", 10.0));
  const auto mod_acc_fetch_evm_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_evm_trace(stub(), session, "", 10.0));
  const auto mod_acc_fetch_constellation_trace_response = EXPECT_SUCCESS(session, client::mod_acc_fetch_constellation_trace(stub(), session, "", 10.0));
  
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_response);
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_evm());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.peak_evm());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rho());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.frequency_error());
  EXPECT_NE(0.0, mod_acc_fetch_evm_response.chip_rate_error());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_magnitude_error());
  EXPECT_LT(0.0, mod_acc_fetch_evm_response.rms_phase_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_iq_impairments_response);
  EXPECT_GT(0.0, mod_acc_fetch_iq_impairments_response.iq_origin_offset());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_gain_imbalance());
  EXPECT_NE(0.0, mod_acc_fetch_iq_impairments_response.iq_quadrature_error());
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_cde_response);
  EXPECT_GT(0.0, mod_acc_fetch_peak_cde_response.peak_cde());
  EXPECT_LE(0, mod_acc_fetch_peak_cde_response.peak_cde_code());
  EXPECT_LE(0, mod_acc_fetch_peak_cde_response.peak_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_peak_active_cde_response);
  EXPECT_GT(0.0, mod_acc_fetch_peak_active_cde_response.peak_active_cde());
  EXPECT_EQ(2, mod_acc_fetch_peak_active_cde_response.peak_active_cde_spreading_factor());
  EXPECT_LE(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_code());
  EXPECT_LE(0, mod_acc_fetch_peak_active_cde_response.peak_active_cde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_rcde_response);
  EXPECT_GT(0.0, mod_acc_fetch_rcde_response.peak_rcde());
  EXPECT_LE(0, mod_acc_fetch_rcde_response.peak_rcde_spreading_factor());
  EXPECT_LE(0, mod_acc_fetch_rcde_response.peak_rcde_code());
  EXPECT_LE(0, mod_acc_fetch_rcde_response.peak_rcde_branch());
  EXPECT_SUCCESS(session, mod_acc_fetch_evm_trace_response);
  EXPECT_EQ(0.0, mod_acc_fetch_evm_trace_response.x0());
  EXPECT_LT(0.0, mod_acc_fetch_evm_trace_response.dx());
  EXPECT_EQ(2560, mod_acc_fetch_evm_trace_response.evm_size());
  EXPECT_EQ(2560, mod_acc_fetch_evm_trace_response.evm().size());
  EXPECT_LT(0.0, mod_acc_fetch_evm_trace_response.evm(0));
  EXPECT_SUCCESS(session, mod_acc_fetch_constellation_trace_response);
  EXPECT_EQ(2560, mod_acc_fetch_constellation_trace_response.constellation().size());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).real());
  EXPECT_NE(0.0, mod_acc_fetch_constellation_trace_response.constellation(0).imaginary());
}

TEST_F(NiRFmxWCDMADriverApiTests, ObwMultiCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.00, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_contiguous_carriers(stub(), session, "", 2, -1));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_spectrum_response = EXPECT_SUCCESS(session, client::obw_fetch_spectrum(stub(), session, "", 10.0));
  const auto obw_fetch_measurement_response = EXPECT_SUCCESS(session, client::obw_fetch_measurement(stub(), session, "", 10.0));

  EXPECT_SUCCESS(session, obw_fetch_spectrum_response);
  EXPECT_LT(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_EQ(13337, obw_fetch_spectrum_response.actual_array_size());
  EXPECT_EQ(13337, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, obw_fetch_spectrum_response.spectrum(0));
  EXPECT_SUCCESS(session, obw_fetch_measurement_response);
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
}

TEST_F(NiRFmxWCDMADriverApiTests, ObwSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_OBW, true));
  EXPECT_SUCCESS(session, client::obw_cfg_sweep_time(stub(), session, "", OBW_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::obw_cfg_averaging(stub(), session, "", OBW_AVERAGING_ENABLED_FALSE, 10, OBW_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto obw_fetch_measurement_response = client::obw_fetch_measurement(stub(), session, "", 10.0);
  const auto obw_fetch_spectrum_response = client::obw_fetch_spectrum(stub(), session, "", 10.0);

  EXPECT_SUCCESS(session, obw_fetch_measurement_response);
  EXPECT_LT(0.0, obw_fetch_measurement_response.occupied_bandwidth());
  EXPECT_LT(0.0, obw_fetch_measurement_response.absolute_power());
  EXPECT_LT(0.0, obw_fetch_measurement_response.start_frequency());
  EXPECT_LT(0.0, obw_fetch_measurement_response.stop_frequency());
  EXPECT_SUCCESS(session, obw_fetch_spectrum_response);
  EXPECT_LT(0.0, obw_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, obw_fetch_spectrum_response.dx());
  EXPECT_EQ(6673, obw_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(6673, obw_fetch_spectrum_response.spectrum().size());
  EXPECT_NE(0.0, obw_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, QevmFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.0, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_QEVM, true));
  EXPECT_SUCCESS(session, client::qevm_cfg_averaging(stub(), session, "", QEVM_AVERAGING_ENABLED_FALSE, 10));
  EXPECT_SUCCESS(session, client::qevm_cfg_measurement_length(stub(), session, "", 2560));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  QEVMFetchEVMTraceResponse qevm_fetch_evm_trace_response;
  QEVMFetchConstellationTraceResponse qevm_fetch_constellation_trace_response;
  const auto qevm_fetch_evm_response = client::qevm_fetch_evm(stub(), session, "", 10.0);
  const auto qevm_fetch_iq_impairments_response = client::qevm_fetch_iq_impairments(stub(), session, "", 10.0);
   qevm_fetch_evm_trace_response = client::qevm_fetch_evm_trace(stub(), session, "", 10.0);
   qevm_fetch_constellation_trace_response = client::qevm_fetch_constellation_trace(stub(), session, "", 10.0);

  EXPECT_RESPONSE_WARNING(375920, qevm_fetch_evm_response);
  EXPECT_LT(0.0, qevm_fetch_evm_response.mean_rms_evm());
  EXPECT_LT(0.0, qevm_fetch_evm_response.maximum_peak_evm());
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_frequency_error());
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_magnitude_error());
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_phase_error());
  EXPECT_NE(0.0, qevm_fetch_evm_response.mean_chip_rate_error());
  EXPECT_RESPONSE_WARNING(375920, qevm_fetch_iq_impairments_response);
  EXPECT_GT(0.0, qevm_fetch_iq_impairments_response.mean_iq_origin_offset());
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.mean_iq_gain_imbalance()));
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.mean_iq_quadrature_error()));
  EXPECT_GT(0.0, qevm_fetch_iq_impairments_response.maximum_iq_origin_offset());
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.maximum_iq_gain_imbalance()));
  EXPECT_TRUE(isnan(qevm_fetch_iq_impairments_response.maximum_iq_quadrature_error()));
  EXPECT_RESPONSE_WARNING(375920, qevm_fetch_evm_trace_response);
  EXPECT_EQ(0.0, qevm_fetch_evm_trace_response.x0());
  EXPECT_LT(0.0, qevm_fetch_evm_trace_response.dx());
  EXPECT_EQ(2560, qevm_fetch_evm_trace_response.evm_size());
  EXPECT_EQ(2560, qevm_fetch_evm_trace_response.evm().size());
  EXPECT_LT(0.0, qevm_fetch_evm_trace_response.evm(0));
  EXPECT_RESPONSE_WARNING(375920, qevm_fetch_constellation_trace_response);
  EXPECT_NE(0.0, qevm_fetch_constellation_trace_response.constellation(0).real());
  EXPECT_NE(0.0, qevm_fetch_constellation_trace_response.constellation(0).imaginary());
}


TEST_F(NiRFmxWCDMADriverApiTests, SemSingleCarrierFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.00, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_band(stub(), session, "", 1));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SEM, true));
  EXPECT_SUCCESS(session, client::sem_cfg_sweep_time(stub(), session, "", SEM_SWEEP_TIME_AUTO_TRUE, 0.000667));
  EXPECT_SUCCESS(session, client::sem_cfg_averaging(stub(), session, "", SEM_AVERAGING_ENABLED_FALSE, 10, SEM_AVERAGING_TYPE_RMS));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));
  

  const auto sem_fetch_lower_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_lower_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_upper_offset_margin_array_response = EXPECT_SUCCESS(session, client::sem_fetch_upper_offset_margin_array(stub(), session, "", 10.0));
  const auto sem_fetch_carrier_measurement_response = EXPECT_SUCCESS(session, client::sem_fetch_carrier_measurement(stub(), session, "", 10.0));
  const auto sem_fetch_measurement_status_response = EXPECT_SUCCESS(session, client::sem_fetch_measurement_status(stub(), session, "", 10.0));
  const auto sem_fetch_spectrum_response = EXPECT_SUCCESS(session, client::sem_fetch_spectrum(stub(), session, "", 10.0));

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

  EXPECT_SUCCESS(session, sem_fetch_upper_offset_margin_array_response);
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
  EXPECT_SUCCESS(session, sem_fetch_carrier_measurement_response);
  EXPECT_LT(0.0, sem_fetch_carrier_measurement_response.absolute_integrated_power());
  EXPECT_SUCCESS(session, sem_fetch_measurement_status_response);
  EXPECT_EQ(0, sem_fetch_measurement_status_response.measurement_status());
  EXPECT_SUCCESS(session, sem_fetch_spectrum_response);
  EXPECT_LT(0.0, sem_fetch_spectrum_response.x0());
  EXPECT_LT(0.0, sem_fetch_spectrum_response.dx());
  EXPECT_EQ(16003, sem_fetch_spectrum_response.spectrum_size());
  EXPECT_EQ(16003, sem_fetch_spectrum_response.spectrum().size());
  EXPECT_GT(0.0, sem_fetch_spectrum_response.spectrum(0));
}

TEST_F(NiRFmxWCDMADriverApiTests, SlotPowerFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.00, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling(stub(), session, "", 0, UPLINK_SCRAMBLING_TYPE_LONG));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPOWER, true));
  EXPECT_SUCCESS(session, client::slot_power_cfg_synchronization_mode_and_interval(stub(), session, "", SLOT_POWER_SYNCHRONIZATION_MODE_SLOT, 0, 15));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto slot_power_fetch_powers_response = EXPECT_SUCCESS(session, client::slot_power_fetch_powers(stub(), session, "", 10.0));

  EXPECT_SUCCESS(session, slot_power_fetch_powers_response);
  EXPECT_EQ(15, slot_power_fetch_powers_response.slot_power_size());
  EXPECT_EQ(15, slot_power_fetch_powers_response.slot_power().size());
  EXPECT_LT(0.0, slot_power_fetch_powers_response.slot_power(0));
  EXPECT_EQ(15, slot_power_fetch_powers_response.slot_power_delta_size());
  EXPECT_EQ(15, slot_power_fetch_powers_response.slot_power_delta().size());
  EXPECT_TRUE(isnan(slot_power_fetch_powers_response.slot_power_delta(0)));
}

TEST_F(NiRFmxWCDMADriverApiTests, SlotPhaseFromExample_FetchData_DataLooksReasonable)
{
  auto session = init_session(stub(), PXI_5663E);
  EXPECT_SUCCESS(session, client::cfg_frequency_reference(stub(), session, "", FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK, 10e6));
  EXPECT_SUCCESS(session, client::cfg_rf(stub(), session, "", 1.95e9, 0.00, 0.0));
  EXPECT_SUCCESS(session, client::cfg_digital_edge_trigger(stub(), session, "", DIGITAL_EDGE_TRIGGER_SOURCE_PFI0, DIGITAL_EDGE_TRIGGER_EDGE_RISING, 0.0, false));
  EXPECT_SUCCESS(session, client::select_measurements(stub(), session, "", MEASUREMENT_TYPES_SLOTPHASE, true));
  EXPECT_SUCCESS(session, client::cfg_uplink_scrambling(stub(), session, "", 0, UPLINK_SCRAMBLING_TYPE_LONG));
  EXPECT_SUCCESS(session, client::slot_power_cfg_synchronization_mode_and_interval(stub(), session, "", SLOT_PHASE_SYNCHRONIZATION_MODE_SLOT, 0, 15));
  EXPECT_SUCCESS(session, client::initiate(stub(), session, "", ""));

  const auto slot_phase_fetch_measurement_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_measurement(stub(), session, "", 10.0));
  const auto slot_phase_fetch_phase_discontinuities_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_phase_discontinuities(stub(), session, "", 10.0));
  const auto slot_phase_fetch_chip_phase_error_linear_fit_trace_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_chip_phase_error_linear_fit_trace(stub(), session, "", 10.0));
  const auto slot_phase_fetch_chip_phase_error_trace_response = EXPECT_SUCCESS(session, client::slot_phase_fetch_chip_phase_error_trace(stub(), session, "", 10.0));

  EXPECT_SUCCESS(session, slot_phase_fetch_measurement_response);
  EXPECT_NEAR(0.0, slot_phase_fetch_measurement_response.maximum_phase_discontinuity(), 180);
  EXPECT_LE(0, slot_phase_fetch_measurement_response.discontinuity_count_greater_than_limit1());
  EXPECT_LE(0, slot_phase_fetch_measurement_response.discontinuity_count_greater_than_limit2());
  EXPECT_NE(0, slot_phase_fetch_measurement_response.discontinuity_minimum_distance());
  EXPECT_SUCCESS(session, slot_phase_fetch_phase_discontinuities_response);
  EXPECT_EQ(15, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity_size());
  EXPECT_EQ(15, slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity().size());
  EXPECT_TRUE(isnan(slot_phase_fetch_phase_discontinuities_response.slot_phase_discontinuity(0)));
  EXPECT_SUCCESS(session, slot_phase_fetch_chip_phase_error_linear_fit_trace_response);
  EXPECT_EQ(0.0, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.x0());
  EXPECT_LT(0.0, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.dx());
  EXPECT_EQ(38400, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit_size());
  EXPECT_EQ(38400, slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit().size());
  auto linear_fit_zero = slot_phase_fetch_chip_phase_error_linear_fit_trace_response.chip_phase_error_linear_fit(0);
  EXPECT_TRUE(isnan(linear_fit_zero) || 0.0 == linear_fit_zero);
  EXPECT_SUCCESS(session, slot_phase_fetch_chip_phase_error_trace_response);
  EXPECT_EQ(0.0, slot_phase_fetch_chip_phase_error_trace_response.x0());
  EXPECT_LT(0.0, slot_phase_fetch_chip_phase_error_trace_response.dx());
  EXPECT_EQ(38400, slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error_size());
  EXPECT_EQ(38400, slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error().size());
  EXPECT_NE(0.0, slot_phase_fetch_chip_phase_error_trace_response.chip_phase_error(0));
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/tests/system/nirfmxwcdma_session_tests.cpp sha256=238316669593a66bd40e4ebc15cc1a340910d156caf3d2660ec800452e839de5 bytes=7064 -->
## FILE: source/tests/system/nirfmxwcdma_session_tests.cpp

- repository: `ni/grpc-device`
- source_path: `source/tests/system/nirfmxwcdma_session_tests.cpp`
- sha256: `238316669593a66bd40e4ebc15cc1a340910d156caf3d2660ec800452e839de5`
- bytes: 7064

````cpp
#include "device_server.h"
#include "nirfmxwcdma/nirfmxwcdma_client.h"
#include "tests/utilities/test_helpers.h"

namespace ni {
namespace tests {
namespace system {
namespace {

namespace rfmxwcdma = nirfmxwcdma_grpc;

const int kInvalidRsrc = -200220;
const int kInvalidRFmxWCDMASession = -380598;
const char* kRFmxWCDMATestRsrc = "FakeDevice";
const char* kRFmxWCDMAOptionsString = "Simulate=1, DriverSetup=Model:5663E";
const char* kRFmxWCDMATestSessionOne = "SessionOneName";
const char* kRFmxWCDMATestSessionTwo = "SessionTwoName";
const char* kRFmxWCDMATestInvalidRsrc = "";

class NiRFmxWCDMASessionTest : public ::testing::Test {
 protected:
  NiRFmxWCDMASessionTest()
      : device_server_(DeviceServerInterface::Singleton()),
        nirfmxwcdma_stub_(rfmxwcdma::NiRFmxWCDMA::NewStub(device_server_->InProcessChannel()))
  {
    device_server_->ResetServer();
  }

  virtual ~NiRFmxWCDMASessionTest() {}

  std::unique_ptr<rfmxwcdma::NiRFmxWCDMA::Stub>& GetStub()
  {
    return nirfmxwcdma_stub_;
  }

  ::grpc::Status call_initialize(const char* resource_name, const char* option_string, const char* session_name, rfmxwcdma::InitializeResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxwcdma::InitializeRequest request;
    request.set_resource_name(resource_name);
    request.set_option_string(option_string);
    request.set_session_name(session_name);

    ::grpc::Status status = GetStub()->Initialize(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

  ::grpc::Status call_close(nidevice_grpc::Session session, bool force_destroy, rfmxwcdma::CloseResponse* response)
  {
    ::grpc::ClientContext context;
    rfmxwcdma::CloseRequest request;
    request.mutable_instrument()->set_name(session.name());
    request.set_force_destroy(force_destroy);

    ::grpc::Status status = GetStub()->Close(&context, request, response);
    nidevice_grpc::experimental::client::raise_if_error(status, context);
    return status;
  }

 private:
  DeviceServerInterface* device_server_;
  std::unique_ptr<rfmxwcdma::NiRFmxWCDMA::Stub> nirfmxwcdma_stub_;
};

TEST_F(NiRFmxWCDMASessionTest, InitializeSessionWithDeviceAndSessionName_CreatesDriverSession)
{
  rfmxwcdma::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionOne, &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxWCDMASessionTest, InitializeSessionWithDeviceAndNoSessionName_CreatesDriverSession)
{
  rfmxwcdma::InitializeResponse response;
  ::grpc::Status status = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, "", &response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, response.status());
  EXPECT_NE("", response.instrument().name());
}

TEST_F(NiRFmxWCDMASessionTest, InitializeSessionWithoutDevice_ReturnsDriverError)
{
  EXPECT_THROW_DRIVER_ERROR({
    rfmxwcdma::InitializeResponse response;
    call_initialize(kRFmxWCDMATestInvalidRsrc, "", "", &response);
  }, kInvalidRsrc);
}

TEST_F(NiRFmxWCDMASessionTest, InitializedSession_CloseSession_ClosesDriverSession)
{
  rfmxwcdma::InitializeResponse init_response;
  call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionOne, &init_response);

  nidevice_grpc::Session session = init_response.instrument();
  ::grpc::ClientContext context;
  rfmxwcdma::CloseRequest close_request;
  close_request.mutable_instrument()->set_name(session.name());
  close_request.set_force_destroy(false);
  rfmxwcdma::CloseResponse close_response;
  ::grpc::Status status = GetStub()->Close(&context, close_request, &close_response);

  EXPECT_TRUE(status.ok());
  EXPECT_EQ(0, close_response.status());
}

TEST_F(NiRFmxWCDMASessionTest, TwoInitializedSessionsOnSameDevice_CloseSessions_ClosesDriverSessions)
{
  rfmxwcdma::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionTwo, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_NE(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxwcdma::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  status_two = call_close(session_two, false, &close_response_two);

  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, close_response_two.status());
}

TEST_F(NiRFmxWCDMASessionTest, CallInitializeTwiceWithSameSessionNameOnSameDevice_CloseSessionTwice_SecondCloseReturnsInvalidSessionError)
{
  rfmxwcdma::InitializeResponse init_response_one, init_response_two;
  ::grpc::Status status_one = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionOne, &init_response_one);
  ::grpc::Status status_two = call_initialize(kRFmxWCDMATestRsrc, kRFmxWCDMAOptionsString, kRFmxWCDMATestSessionOne, &init_response_two);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, init_response_one.status());
  EXPECT_TRUE(status_two.ok());
  EXPECT_EQ(0, init_response_two.status());
  EXPECT_EQ(init_response_one.instrument().name(), init_response_two.instrument().name());

  nidevice_grpc::Session session_one = init_response_one.instrument();
  nidevice_grpc::Session session_two = init_response_two.instrument();
  rfmxwcdma::CloseResponse close_response_one, close_response_two;
  status_one = call_close(session_one, false, &close_response_one);
  EXPECT_TRUE(status_one.ok());
  EXPECT_EQ(0, close_response_one.status());

  EXPECT_THROW_DRIVER_ERROR({
    // Initialize was only called once in the driver since the second init call to the service found the Session by the same name and returned it.
    // Therefore if we try to close the session again the driver will respond that it's not a valid session (it's already been closed).
    call_close(session_two, false, &close_response_two);
  }, kInvalidRFmxWCDMASession);
}

TEST_F(NiRFmxWCDMASessionTest, InvalidSession_CloseSession_ReturnsInvalidSessionError)
{
  nidevice_grpc::Session session;
  session.set_name("");

  EXPECT_THROW_DRIVER_ERROR({
    rfmxwcdma::CloseResponse response;
    call_close(session, false, &response);
  }, kInvalidRFmxWCDMASession);
}

}  // namespace
}  // namespace system
}  // namespace tests
}  // namespace ni
````
