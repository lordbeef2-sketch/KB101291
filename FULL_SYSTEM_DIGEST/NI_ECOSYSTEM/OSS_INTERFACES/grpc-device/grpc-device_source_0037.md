# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxEVDO.h sha256=b099a31798d2874687f2b0ff8864c1e39a9830eac40680681f06d81cafaefdee bytes=134338 -->
## FILE: imports/include/niRFmxEVDO.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxEVDO.h`
- sha256: `b099a31798d2874687f2b0ff8864c1e39a9830eac40680681f06d81cafaefdee`
- bytes: 134338

````c

/****************************************************************************************************
*          National Instruments RFmx EVDO
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2021.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxEVDO.h
*
* Purpose:  National Instruments RFmx EVDO,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_EVDO_H__
#define __NI_RFMX_EVDO_H__

#include "niRFmxInstr.h"

#define RFMXEVDO_ATTR_MODACC_MEASUREMENT_ENABLED                                   0x00811000
#define RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE                                  0x00811002
#define RFMXEVDO_ATTR_MODACC_MEASUREMENT_OFFSET                                    0x00811004
#define RFMXEVDO_ATTR_MODACC_MEASUREMENT_LENGTH                                    0x00811005
#define RFMXEVDO_ATTR_MODACC_SPECTRUM_INVERTED                                     0x00811006
#define RFMXEVDO_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED                             0x00811007
#define RFMXEVDO_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                     0x008110a1
#define RFMXEVDO_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED                   0x008110a2
#define RFMXEVDO_ATTR_MODACC_RECEIVE_FILTER_ENABLED                                0x008110a3
#define RFMXEVDO_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED                          0x00811008
#define RFMXEVDO_ATTR_MODACC_ALL_TRACES_ENABLED                                    0x0081100c
#define RFMXEVDO_ATTR_MODACC_RESULTS_FREQUENCY_ERROR                               0x0081100f
#define RFMXEVDO_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR                               0x00811010
#define RFMXEVDO_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET                              0x00811011
#define RFMXEVDO_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE                             0x00811012
#define RFMXEVDO_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR                           0x00811013
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_EVM                                0x00811014
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_EVM                               0x00811015
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_MAGNITUDE_ERROR                    0x00811016
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RMS_PHASE_ERROR                        0x00811017
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_RHO                                    0x00811018
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE                               0x00811019
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE_WALSH_CODE_NUMBER             0x0081101b
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE_BRANCH                        0x0081104d
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE                        0x0081101c
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH      0x0081101d
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER      0x0081101e
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_BRANCH                 0x0081104e
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_DATA_MODULATION_TYPE          0x0081101f
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_NUMBER_OF_DETECTED_CHANNELS            0x00811020
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_WALSH_CODE_LENGTH             0x00811021
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_WALSH_CODE_NUMBER             0x00811022
#define RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_BRANCH                        0x00811023
#define RFMXEVDO_ATTR_ACP_MEASUREMENT_ENABLED                                      0x00801000
#define RFMXEVDO_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH                            0x00801005
#define RFMXEVDO_ATTR_ACP_NUMBER_OF_OFFSETS                                        0x00801008
#define RFMXEVDO_ATTR_ACP_OFFSET_FREQUENCY                                         0x0080100a
#define RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER                           0x0080100c
#define RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC                          0x0080100d
#define RFMXEVDO_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH                             0x0080100e
#define RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH                                0x0080101b
#define RFMXEVDO_ATTR_ACP_RBW_FILTER_BANDWIDTH                                     0x0080101c
#define RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE                                          0x0080101d
#define RFMXEVDO_ATTR_ACP_SWEEP_TIME_AUTO                                          0x0080101e
#define RFMXEVDO_ATTR_ACP_SWEEP_TIME_INTERVAL                                      0x0080101f
#define RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD                                       0x00801012
#define RFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLED                               0x00801020
#define RFMXEVDO_ATTR_ACP_AVERAGING_ENABLED                                        0x00801016
#define RFMXEVDO_ATTR_ACP_AVERAGING_COUNT                                          0x00801015
#define RFMXEVDO_ATTR_ACP_AVERAGING_TYPE                                           0x00801018
#define RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO                              0x00801034
#define RFMXEVDO_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET                              0x00801035
#define RFMXEVDO_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET                               0x00801036
#define RFMXEVDO_ATTR_ACP_ALL_TRACES_ENABLED                                       0x00801021
#define RFMXEVDO_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                               0x00801014
#define RFMXEVDO_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER                              0x00801022
#define RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER                           0x00801026
#define RFMXEVDO_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER                           0x00801027
#define RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                      0x0080102c
#define RFMXEVDO_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                      0x0080102d
#define RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                      0x00801032
#define RFMXEVDO_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                      0x00801033
#define RFMXEVDO_ATTR_ACP_SEQUENTIAL_FFT_SIZE                                      0x00801038
#define RFMXEVDO_ATTR_CHP_MEASUREMENT_ENABLED                                      0x00803000
#define RFMXEVDO_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH                            0x00803002
#define RFMXEVDO_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH                                0x0080300c
#define RFMXEVDO_ATTR_CHP_RBW_FILTER_BANDWIDTH                                     0x0080300d
#define RFMXEVDO_ATTR_CHP_RBW_FILTER_TYPE                                          0x0080300e
#define RFMXEVDO_ATTR_CHP_SWEEP_TIME_AUTO                                          0x00803011
#define RFMXEVDO_ATTR_CHP_SWEEP_TIME_INTERVAL                                      0x00803012
#define RFMXEVDO_ATTR_CHP_AVERAGING_ENABLED                                        0x00803007
#define RFMXEVDO_ATTR_CHP_AVERAGING_COUNT                                          0x00803006
#define RFMXEVDO_ATTR_CHP_AVERAGING_TYPE                                           0x00803009
#define RFMXEVDO_ATTR_CHP_ALL_TRACES_ENABLED                                       0x00803014
#define RFMXEVDO_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS                               0x00803003
#define RFMXEVDO_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER                              0x00803018
#define RFMXEVDO_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER                           0x00803015
#define RFMXEVDO_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER                           0x00803019
#define RFMXEVDO_ATTR_OBW_MEASUREMENT_ENABLED                                      0x00806000
#define RFMXEVDO_ATTR_OBW_SPAN                                                     0x00806004
#define RFMXEVDO_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH                                0x0080600c
#define RFMXEVDO_ATTR_OBW_RBW_FILTER_BANDWIDTH                                     0x0080600d
#define RFMXEVDO_ATTR_OBW_RBW_FILTER_TYPE                                          0x0080600e
#define RFMXEVDO_ATTR_OBW_SWEEP_TIME_AUTO                                          0x0080600f
#define RFMXEVDO_ATTR_OBW_SWEEP_TIME_INTERVAL                                      0x00806010
#define RFMXEVDO_ATTR_OBW_AVERAGING_ENABLED                                        0x00806007
#define RFMXEVDO_ATTR_OBW_AVERAGING_COUNT                                          0x00806006
#define RFMXEVDO_ATTR_OBW_AVERAGING_TYPE                                           0x00806009
#define RFMXEVDO_ATTR_OBW_ALL_TRACES_ENABLED                                       0x00806012
#define RFMXEVDO_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS                               0x00806003
#define RFMXEVDO_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH                               0x00806013
#define RFMXEVDO_ATTR_OBW_RESULTS_ABSOLUTE_POWER                                   0x00806014
#define RFMXEVDO_ATTR_OBW_RESULTS_START_FREQUENCY                                  0x00806015
#define RFMXEVDO_ATTR_OBW_RESULTS_STOP_FREQUENCY                                   0x00806016
#define RFMXEVDO_ATTR_SEM_MEASUREMENT_ENABLED                                      0x00808000
#define RFMXEVDO_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH                            0x00808005
#define RFMXEVDO_ATTR_SEM_NUMBER_OF_OFFSETS                                        0x0080800b
#define RFMXEVDO_ATTR_SEM_OFFSET_START_FREQUENCY                                   0x00808014
#define RFMXEVDO_ATTR_SEM_OFFSET_STOP_FREQUENCY                                    0x00808015
#define RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH                              0x00808017
#define RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_TYPE                                   0x00808018
#define RFMXEVDO_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL                                0x0080800c
#define RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO                                          0x00808025
#define RFMXEVDO_ATTR_SEM_SWEEP_TIME_INTERVAL                                      0x00808026
#define RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED                                        0x0080801f
#define RFMXEVDO_ATTR_SEM_AVERAGING_COUNT                                          0x0080801e
#define RFMXEVDO_ATTR_SEM_AVERAGING_TYPE                                           0x00808021
#define RFMXEVDO_ATTR_SEM_ALL_TRACES_ENABLED                                       0x00808027
#define RFMXEVDO_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                               0x0080801d
#define RFMXEVDO_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER                              0x00808028
#define RFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS                     0x00808029
#define RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER                0x0080802e
#define RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER                0x0080802d
#define RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER                      0x0080802f
#define RFMXEVDO_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY                           0x00808030
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS                  0x0080803d
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER           0x00808034
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER           0x00808035
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER                 0x00808036
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER                 0x00808037
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                      0x00808038
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                              0x00808039
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER               0x0080803a
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER               0x0080803b
#define RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY                    0x0080803c
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS                  0x0080804a
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER           0x00808041
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER           0x00808042
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER                 0x00808043
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER                 0x00808044
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                      0x00808045
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                              0x00808046
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER               0x00808047
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER               0x00808048
#define RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY                    0x00808049
#define RFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGE                                 0x0080d003
#define RFMXEVDO_ATTR_RESULT_FETCH_TIMEOUT                                         0x0080c000
#define RFMXEVDO_ATTR_CENTER_FREQUENCY                                             0x00800001
#define RFMXEVDO_ATTR_REFERENCE_LEVEL                                              0x00800002
#define RFMXEVDO_ATTR_EXTERNAL_ATTENUATION                                         0x00800003
#define RFMXEVDO_ATTR_TRIGGER_TYPE                                                 0x00800004
#define RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                  0x00800005
#define RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                    0x00800006
#define RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                 0x00800007
#define RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                  0x00800008
#define RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                             0x00800fff
#define RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                  0x00800009
#define RFMXEVDO_ATTR_TRIGGER_DELAY                                                0x0080000a
#define RFMXEVDO_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                              0x0080000b
#define RFMXEVDO_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                          0x0080000c
#define RFMXEVDO_ATTR_BAND_CLASS                                                   0x00800010
#define RFMXEVDO_ATTR_NUMBER_OF_CARRIERS                                           0x0080000e
#define RFMXEVDO_ATTR_CARRIER_FREQUENCY                                            0x0080000f
#define RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE                                       0x00800011
#define RFMXEVDO_ATTR_CHANNEL_CONFIGURATION_MODE                                   0x00800012
#define RFMXEVDO_ATTR_UPLINK_NUMBER_OF_CHANNELS                                    0x00800018
#define RFMXEVDO_ATTR_UPLINK_DATA_MODULATION_TYPE                                  0x00800019
#define RFMXEVDO_ATTR_UPLINK_WALSH_CODE_LENGTH                                     0x0080001a
#define RFMXEVDO_ATTR_UPLINK_WALSH_CODE_NUMBER                                     0x0080001b
#define RFMXEVDO_ATTR_UPLINK_BRANCH                                                0x0080001c
#define RFMXEVDO_ATTR_UPLINK_SPREADING_I_MASK                                      0x00800029
#define RFMXEVDO_ATTR_UPLINK_SPREADING_Q_MASK                                      0x0080002a
#define RFMXEVDO_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                           0x0080d000
#define RFMXEVDO_ATTR_CDA_MEASUREMENT_ENABLED                                      0x00813000
#define RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE                                     0x00813002
#define RFMXEVDO_ATTR_CDA_MEASUREMENT_OFFSET                                       0x00813003
#define RFMXEVDO_ATTR_CDA_MEASUREMENT_LENGTH                                       0x00813004
#define RFMXEVDO_ATTR_CDA_UPLINK_WALSH_CODE_LENGTH                                 0x00813005
#define RFMXEVDO_ATTR_CDA_UPLINK_WALSH_CODE_NUMBER                                 0x00813006
#define RFMXEVDO_ATTR_CDA_UPLINK_BRANCH                                            0x00813007
#define RFMXEVDO_ATTR_CDA_POWER_UNIT                                               0x00813008
#define RFMXEVDO_ATTR_CDA_SPECTRUM_INVERTED                                        0x00813009
#define RFMXEVDO_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED                                0x0081300a
#define RFMXEVDO_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                        0x0081300b
#define RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED                      0x0081300c
#define RFMXEVDO_ATTR_CDA_RECEIVE_FILTER_ENABLED                                   0x0081300d
#define RFMXEVDO_ATTR_CDA_ALL_TRACES_ENABLED                                       0x0081300e
#define RFMXEVDO_ATTR_CDA_RESULTS_FREQUENCY_ERROR                                  0x00813011
#define RFMXEVDO_ATTR_CDA_RESULTS_CHIP_RATE_ERROR                                  0x00813012
#define RFMXEVDO_ATTR_CDA_RESULTS_IQ_ORIGIN_OFFSET                                 0x00813013
#define RFMXEVDO_ATTR_CDA_RESULTS_IQ_GAIN_IMBALANCE                                0x00813014
#define RFMXEVDO_ATTR_CDA_RESULTS_IQ_QUADRATURE_ERROR                              0x00813015
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_EVM                            0x00813016
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_SYMBOL_EVM                           0x00813017
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_MAGNITUDE_ERROR                0x00813018
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_RMS_SYMBOL_PHASE_ERROR                    0x00813019
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_SYMBOL_POWER                         0x0081301a
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_POWER                               0x0081301b
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_TOTAL_ACTIVE_POWER                        0x0081301c
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_ACTIVE_POWER                         0x0081301d
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_ACTIVE_POWER                         0x0081301e
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_INACTIVE_POWER                       0x0081301f
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_PEAK_INACTIVE_POWER                       0x00813020
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_I_MEAN_ACTIVE_POWER                       0x00813021
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_I_PEAK_INACTIVE_POWER                     0x00813022
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_MEAN_ACTIVE_POWER                       0x00813023
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_Q_PEAK_INACTIVE_POWER                     0x00813024
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_PILOT_POWER                          0x00813025
#define RFMXEVDO_ATTR_CDA_RESULTS_UPLINK_MEAN_AUXILIARY_PILOT_POWER                0x00813026
#define RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_ENABLED                                0x00814000
#define RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE                               0x00814002
#define RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_OFFSET                                 0x00814003
#define RFMXEVDO_ATTR_SLOTPOWER_MEASUREMENT_LENGTH                                 0x00814004
#define RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED                                  0x00814005
#define RFMXEVDO_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED                             0x00814006
#define RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_ENABLED                                0x00815000
#define RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE                               0x00815002
#define RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_OFFSET                                 0x00815003
#define RFMXEVDO_ATTR_SLOTPHASE_MEASUREMENT_LENGTH                                 0x00815004
#define RFMXEVDO_ATTR_SLOTPHASE_SPECTRUM_INVERTED                                  0x00815005
#define RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED                             0x00815006
#define RFMXEVDO_ATTR_SLOTPHASE_TRANSIENT_DURATION                                 0x00815007
#define RFMXEVDO_ATTR_SLOTPHASE_ALL_TRACES_ENABLED                                 0x00815008
#define RFMXEVDO_ATTR_SLOTPHASE_RESULTS_MAXIMUM_HALF_SLOT_PHASE_DISCONTINUITY      0x0081500b
#define RFMXEVDO_ATTR_SELECTED_PORTS                                               0x00800ffd
#define RFMXEVDO_ATTR_REFERENCE_LEVEL_HEADROOM                                     0x00800ffc
#define RFMXEVDO_ATTR_ACP_FFT_OVERLAP_MODE                                         0x00801039
#define RFMXEVDO_ATTR_ACP_FFT_OVERLAP                                              0x0080103a

// Values for RFMXEVDO_ATTR_TRIGGER_TYPE
#define RFMXEVDO_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXEVDO_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXEVDO_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXEVDO_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXEVDO_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXEVDO_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXEVDO_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXEVDO_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXEVDO_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXEVDO_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXEVDO_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXEVDO_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXEVDO_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXEVDO_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXEVDO_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXEVDO_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXEVDO_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXEVDO_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXEVDO_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXEVDO_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXEVDO_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXEVDO_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXEVDO_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXEVDO_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXEVDO_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXEVDO_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXEVDO_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXEVDO_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXEVDO_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXEVDO_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXEVDO_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXEVDO_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXEVDO_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXEVDO_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXEVDO_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXEVDO_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXEVDO_ATTR_PHYSICAL_LAYER_SUBTYPE
#define RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_0_1                                                     0
#define RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_2                                                       1
#define RFMXEVDO_VAL_PHYSICAL_LAYER_SUBTYPE_3                                                       2

// Values for RFMXEVDO_ATTR_CHANNEL_CONFIGURATION_MODE
#define RFMXEVDO_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT                                         0
#define RFMXEVDO_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                                        1

// Values for RFMXEVDO_ATTR_UPLINK_DATA_MODULATION_TYPE
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_AUTO                                               0
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT                                1
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_B4                                                 2
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4                                                 3
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q2                                                 4
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_Q4Q2                                               5
#define RFMXEVDO_VAL_UPLINK_DATA_MODULATION_TYPE_E4E2                                               6

// Values for RFMXEVDO_ATTR_UPLINK_BRANCH
#define RFMXEVDO_VAL_UPLINK_BRANCH_I                                                                0
#define RFMXEVDO_VAL_UPLINK_BRANCH_Q                                                                1
#define RFMXEVDO_VAL_UPLINK_BRANCH_I_AND_Q                                                          2

// Values for RFMXEVDO_ATTR_MODACC_SYNCHRONIZATION_MODE
#define RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME                                              0
#define RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT                                               1
#define RFMXEVDO_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY                                          2

// Values for RFMXEVDO_ATTR_MODACC_SPECTRUM_INVERTED
#define RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXEVDO_VAL_MODACC_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXEVDO_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXEVDO_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                         0
#define RFMXEVDO_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                          1

// Values for RFMXEVDO_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXEVDO_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                 0
#define RFMXEVDO_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                  1

// Values for RFMXEVDO_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXEVDO_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                               0
#define RFMXEVDO_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                1

// Values for RFMXEVDO_ATTR_MODACC_RECEIVE_FILTER_ENABLED
#define RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_FALSE                                            0
#define RFMXEVDO_VAL_MODACC_RECEIVE_FILTER_ENABLED_TRUE                                             1

// Values for RFMXEVDO_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED
#define RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE                                      0
#define RFMXEVDO_VAL_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE                                       1

// Values for RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_CDE_BRANCH
#define RFMXEVDO_VAL_MODACC_UPLINK_PEAK_CDE_BRANCH_I                                                0
#define RFMXEVDO_VAL_MODACC_UPLINK_PEAK_CDE_BRANCH_Q                                                1

// Values for RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_PEAK_ACTIVE_CDE_BRANCH
#define RFMXEVDO_VAL_MODACC_UPLINK_PEAK_ACTIVE_CDE_BRANCH_I                                         0
#define RFMXEVDO_VAL_MODACC_UPLINK_PEAK_ACTIVE_CDE_BRANCH_Q                                         1
#define RFMXEVDO_VAL_MODACC_UPLINK_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q                                   2

// Values for RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_DATA_MODULATION_TYPE
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_DATA_CHANNEL_ABSENT                1
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_B4                                 2
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4                                 3
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q2                                 4
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_Q4Q2                               5
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_DATA_MODULATION_TYPE_E4E2                               6

// Values for RFMXEVDO_ATTR_MODACC_RESULTS_UPLINK_DETECTED_BRANCH
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I                                                0
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_Q                                                1
#define RFMXEVDO_VAL_MODACC_UPLINK_DETECTED_BRANCH_I_AND_Q                                          2

// Values for RFMXEVDO_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER
#define RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST                                     0
#define RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST                                     1
#define RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE                                   2
#define RFMXEVDO_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC                                    3

// Values for RFMXEVDO_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXEVDO_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXEVDO_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXEVDO_ATTR_ACP_RBW_FILTER_TYPE
#define RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXEVDO_VAL_ACP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXEVDO_ATTR_ACP_SWEEP_TIME_AUTO
#define RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXEVDO_VAL_ACP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXEVDO_ATTR_ACP_MEASUREMENT_METHOD
#define RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1
#define RFMXEVDO_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT                                          2

// Values for RFMXEVDO_ATTR_ACP_NOISE_COMPENSATION_ENABLED
#define RFMXEVDO_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXEVDO_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXEVDO_ATTR_ACP_AVERAGING_ENABLED
#define RFMXEVDO_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXEVDO_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXEVDO_ATTR_ACP_AVERAGING_TYPE
#define RFMXEVDO_VAL_ACP_AVERAGING_TYPE_RMS                                                         0
#define RFMXEVDO_VAL_ACP_AVERAGING_TYPE_LOG                                                         1
#define RFMXEVDO_VAL_ACP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXEVDO_VAL_ACP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXEVDO_VAL_ACP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXEVDO_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO
#define RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE                                          0
#define RFMXEVDO_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE                                           1

// Values for RFMXEVDO_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXEVDO_VAL_CHP_RBW_AUTO_FALSE                                                             0
#define RFMXEVDO_VAL_CHP_RBW_AUTO_TRUE                                                              1

// Values for RFMXEVDO_ATTR_CHP_RBW_FILTER_TYPE
#define RFMXEVDO_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXEVDO_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXEVDO_VAL_CHP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXEVDO_ATTR_CHP_SWEEP_TIME_AUTO
#define RFMXEVDO_VAL_CHP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXEVDO_VAL_CHP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXEVDO_ATTR_CHP_AVERAGING_ENABLED
#define RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXEVDO_VAL_CHP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXEVDO_ATTR_CHP_AVERAGING_TYPE
#define RFMXEVDO_VAL_CHP_AVERAGING_TYPE_RMS                                                         0
#define RFMXEVDO_VAL_CHP_AVERAGING_TYPE_LOG                                                         1
#define RFMXEVDO_VAL_CHP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXEVDO_VAL_CHP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXEVDO_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXEVDO_VAL_OBW_RBW_AUTO_FALSE                                                             0
#define RFMXEVDO_VAL_OBW_RBW_AUTO_TRUE                                                              1

// Values for RFMXEVDO_ATTR_OBW_RBW_FILTER_TYPE
#define RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXEVDO_VAL_OBW_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXEVDO_ATTR_OBW_SWEEP_TIME_AUTO
#define RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXEVDO_VAL_OBW_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXEVDO_ATTR_OBW_AVERAGING_ENABLED
#define RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXEVDO_VAL_OBW_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXEVDO_ATTR_OBW_AVERAGING_TYPE
#define RFMXEVDO_VAL_OBW_AVERAGING_TYPE_RMS                                                         0
#define RFMXEVDO_VAL_OBW_AVERAGING_TYPE_LOG                                                         1
#define RFMXEVDO_VAL_OBW_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXEVDO_VAL_OBW_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXEVDO_ATTR_SEM_OFFSET_RBW_FILTER_TYPE
#define RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED                                           0
#define RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN                                            1
#define RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT                                                2
#define RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4                                       3
#define RFMXEVDO_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5                                       4

// Values for RFMXEVDO_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXEVDO_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXEVDO_ATTR_SEM_AVERAGING_ENABLED
#define RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXEVDO_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXEVDO_ATTR_SEM_AVERAGING_TYPE
#define RFMXEVDO_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXEVDO_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXEVDO_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXEVDO_VAL_SEM_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXEVDO_ATTR_SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS
#define RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXEVDO_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXEVDO_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXEVDO_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for Boolean
#define RFMXEVDO_VAL_FALSE                                                                          0
#define RFMXEVDO_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXEVDO_VAL_MODACC                                                                         1 << 0
#define RFMXEVDO_VAL_ACP                                                                            1 << 1
#define RFMXEVDO_VAL_CHP                                                                            1 << 2
#define RFMXEVDO_VAL_OBW                                                                            1 << 3
#define RFMXEVDO_VAL_SEM                                                                            1 << 4
#define RFMXEVDO_VAL_CDA                                                                            1 << 5
#define RFMXEVDO_VAL_SLOTPHASE                                                                      1 << 6
#define RFMXEVDO_VAL_SLOTPOWER                                                                      1 << 7

// Values for FrequencyReferenceSource
#define RFMXEVDO_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXEVDO_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXEVDO_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXEVDO_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for RFMXEVDO_ATTR_LINK_DIRECTION
#define RFMXEVDO_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for RFAttenuationAuto
#define RFMXEVDO_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXEVDO_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for MechanicalAttenuationAuto
#define RFMXEVDO_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXEVDO_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

// Values for RFMXEVDO_ATTR_CDA_SYNCHRONIZATION_MODE
#define RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_FRAME                                                 0
#define RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_SLOT                                                  1
#define RFMXEVDO_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY                                             2

// Values for RFMXEVDO_ATTR_CDA_UPLINK_BRANCH
#define RFMXEVDO_VAL_CDA_UPLINK_BRANCH_I                                                            0
#define RFMXEVDO_VAL_CDA_UPLINK_BRANCH_Q                                                            1
#define RFMXEVDO_VAL_CDA_UPLINK_BRANCH_I_AND_Q                                                      2

// Values for RFMXEVDO_ATTR_CDA_POWER_UNIT
#define RFMXEVDO_VAL_CDA_POWER_UNIT_DB                                                              0
#define RFMXEVDO_VAL_CDA_POWER_UNIT_DBM                                                             1

// Values for RFMXEVDO_ATTR_CDA_SPECTRUM_INVERTED
#define RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_FALSE                                                    0
#define RFMXEVDO_VAL_CDA_SPECTRUM_INVERTED_TRUE                                                     1

// Values for RFMXEVDO_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                            0
#define RFMXEVDO_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                             1

// Values for RFMXEVDO_ATTR_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXEVDO_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                    0
#define RFMXEVDO_VAL_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                     1

// Values for RFMXEVDO_ATTR_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXEVDO_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                                  0
#define RFMXEVDO_VAL_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                   1

// Values for RFMXEVDO_ATTR_CDA_RECEIVE_FILTER_ENABLED
#define RFMXEVDO_VAL_CDA_RECEIVE_FILTER_ENABLED_FALSE                                               0
#define RFMXEVDO_VAL_CDA_RECEIVE_FILTER_ENABLED_TRUE                                                1

// Values for RFMXEVDO_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE
#define RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXEVDO_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXEVDO_ATTR_SLOTPOWER_SPECTRUM_INVERTED
#define RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXEVDO_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXEVDO_ATTR_SLOTPOWER_RECEIVE_FILTER_ENABLED
#define RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_FALSE                                         0
#define RFMXEVDO_VAL_SLOTPOWER_RECEIVE_FILTER_ENABLED_TRUE                                          1

// Values for RFMXEVDO_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE
#define RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXEVDO_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXEVDO_ATTR_SLOTPHASE_SPECTRUM_INVERTED
#define RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXEVDO_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXEVDO_ATTR_SLOTPHASE_RECEIVE_FILTER_ENABLED
#define RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_FALSE                                         0
#define RFMXEVDO_VAL_SLOTPHASE_RECEIVE_FILTER_ENABLED_TRUE                                          1

// Values for RFMXEVDO_ATTR_ACP_FFT_OVERLAP_MODE
#define RFMXEVDO_VAL_ACP_FFT_OVERLAP_MODE_DISABLED                                                  0
#define RFMXEVDO_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC                                                 1

/* ---------------- RFmxEVDO APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxEVDO_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxEVDO_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxEVDO_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxEVDO_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxEVDO_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxEVDO_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxEVDO_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxEVDO_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxEVDO_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxEVDO_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxEVDO_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_BuildChannelString(
   char selectorString[],
   int32 channelNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxEVDO_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxEVDO_BuildCarrierString(
   char selectorString[],
   int32 carrierNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxEVDO_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxEVDO_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxEVDO_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxEVDO_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxEVDO_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxEVDO_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* done
);

int32 __stdcall RFmxEVDO_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxEVDO_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxEVDO_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxEVDO_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxEVDO_AnalyzeSpectrum1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxEVDO_CfgContiguousCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfCarriers,
   int32 carrierAtCenterFrequency,
   int32 bandClass
);

int32 __stdcall RFmxEVDO_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxEVDO_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxEVDO_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxEVDO_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxEVDO_CfgFrequencyChannelNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection,
   int32 bandClass,
   int32 channelNumber
);

int32 __stdcall RFmxEVDO_CfgUplinkNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkNumberOfChannels
);

int32 __stdcall RFmxEVDO_CfgUplinkDataModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkDataModulationType
);

int32 __stdcall RFmxEVDO_CfgUplinkUserDefinedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkWalshCodeLength,
   int32 uplinkWalshCodeNumber,
   int32 uplinkBranch
);

int32 __stdcall RFmxEVDO_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxEVDO_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxEVDO_CfgUplinkSpreading(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 uplinkSpreadingIMask,
   int64 uplinkSpreadingQMask
);

int32 __stdcall RFmxEVDO_CfgBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 bandClass
);

int32 __stdcall RFmxEVDO_CfgCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 carrierFrequency
);

int32 __stdcall RFmxEVDO_CfgPhysicalLayerSubtype(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 physicalLayerSubtype
);

int32 __stdcall RFmxEVDO_CfgChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelConfigurationMode
);

int32 __stdcall RFmxEVDO_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxEVDO_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxEVDO_CfgNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfCarriers
);

int32 __stdcall RFmxEVDO_CfgUplinkUserDefinedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkWalshCodeLength[],
   int32 uplinkWalshCodeNumber[],
   int32 uplinkBranch[],
   int32 numberOfElements
);

int32 __stdcall RFmxEVDO_CfgCarrierFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 carrierFrequency[],
   int32 numberOfElements
);

int32 __stdcall RFmxEVDO_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxEVDO_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxEVDO_CHPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxEVDO_CHPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxEVDO_CHPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxEVDO_OBWCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxEVDO_OBWCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxEVDO_OBWCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxEVDO_ModAccCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxEVDO_ModAccCfgMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 multiCarrierFilterEnabled
);

int32 __stdcall RFmxEVDO_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxEVDO_ACPCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxEVDO_ACPCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxEVDO_ACPCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxEVDO_ACPCfgOffsetPowerReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetPowerReferenceCarrier,
   int32 offsetPowerReferenceSpecific
);

int32 __stdcall RFmxEVDO_ACPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxEVDO_ACPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxEVDO_CDACfgPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerUnit
);

int32 __stdcall RFmxEVDO_CDACfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxEVDO_CDACfgUplinkMeasurementChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 walshCodeLength,
   int32 walshCodeNumber,
   int32 branch
);

int32 __stdcall RFmxEVDO_SlotPhaseCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxEVDO_SlotPowerCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxEVDO_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxEVDO_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxEVDO_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxEVDO_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxEVDO_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxEVDO_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxEVDO_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxEVDO_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 minimumQuietTimeMode,
   float64 minimumQuietTime,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxEVDO_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ACPFetchRelativePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 relativePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ACPFetchAbsolutePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 absolutePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ACPFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxEVDO_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower
);

int32 __stdcall RFmxEVDO_ACPFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 uplinkDetectedWalshCodeLength[],
   int32 uplinkDetectedWalshCodeNumber[],
   int32 uplinkDetectedBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedDataModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* uplinkDetectedDataModulationType
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkDetectedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* uplinkDetectedWalshCodeLength,
   int32* uplinkDetectedWalshCodeNumber,
   int32* uplinkDetectedBranch
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* uplinkRMSEVM,
   float64* uplinkPeakEVM,
   float64* uplinkRho,
   float64* frequencyError,
   float64* chipRateError,
   float64* uplinkRMSMagnitudeError,
   float64* uplinkRMSPhaseError
);

int32 __stdcall RFmxEVDO_ModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffset,
   float64* IQGainImbalance,
   float64* IQQuadratureError
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* uplinkNumberOfDetectedChannels
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* uplinkPeakActiveCDE,
   int32* uplinkPeakActiveCDEWalshCodeLength,
   int32* uplinkPeakActiveCDEWalshCodeNumber,
   int32* uplinkPeakActiveCDEBranch
);

int32 __stdcall RFmxEVDO_ModAccFetchUplinkPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* uplinkPeakCDE,
   int32* uplinkPeakCDEWalshCodeNumber,
   int32* uplinkPeakCDEBranch
);

int32 __stdcall RFmxEVDO_OBWFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_OBWFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* occupiedBandwidth,
   float64* absolutePower,
   float64* startFrequency,
   float64* stopFrequency
);

int32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 carrierAbsolutePower[],
   float64 carrierRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CHPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CHPFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* carrierAbsolutePower,
   float64* carrierRelativePower
);

int32 __stdcall RFmxEVDO_CHPFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   float32 relativeMask[],
   float32 absoluteMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SEMFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower
);

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxEVDO_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxEVDO_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxEVDO_SEMFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxEVDO_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolMagnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 ICodeDomainPowers[],
   float32 QCodeDomainPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle symbolConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolConstellationI[],
   float32 symbolConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_CDAFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffset,
   float64* IQGainImbalance,
   float64* IQQuadratureError
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSSymbolEVM,
   float64* peakSymbolEVM,
   float64* RMSSymbolMagnitudeError,
   float64* RMSSymbolPhaseError,
   float64* meanSymbolPower,
   float64* frequencyError,
   float64* chipRateError
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalPower,
   float64* totalActivePower,
   float64* meanActivePower,
   float64* peakActivePower,
   float64* meanInactivePower,
   float64* peakInactivePower
);

int32 __stdcall RFmxEVDO_CDAFetchUplinkCodeDomainIAndQPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IMeanActivePower,
   float64* QMeanActivePower,
   float64* IPeakInactivePower,
   float64* QPeakInactivePower
);

int32 __stdcall RFmxEVDO_SlotPhaseFetchPhaseDiscontinuities(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 halfSlotPhaseDiscontinuity[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SlotPhaseFetchChipPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SlotPhaseFetchChipPhaseErrorLinearFitTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseErrorLinearFit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_SlotPhaseFetchMaximumHalfSlotPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumHalfSlotPhaseDiscontinuity
);

int32 __stdcall RFmxEVDO_SlotPowerFetchPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 halfSlotPower[],
   float64 halfSlotPowerDelta[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxEVDO_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkRMSMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkRMSPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkRho(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakCDEWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDEWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDEWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkPeakActiveCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkDetectedDataModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkDetectedWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkDetectedWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ModAccGetResultsUplinkDetectedBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetOffsetPowerReferenceCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetOffsetPowerReferenceCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetOffsetPowerReferenceSpecific(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetOffsetPowerReferenceSpecific(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_ACPGetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_ACPSetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_ACPGetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CHPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CHPGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CHPGetResultsCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_OBWSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_OBWGetResultsOccupiedBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWGetResultsAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWGetResultsStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_OBWGetResultsStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsCompositeMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsCarrierRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsCarrierAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsCarrierPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetBandClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetPhysicalLayerSubtype(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetPhysicalLayerSubtype(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkDataModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkDataModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkSpreadingImask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkSpreadingImask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 attrVal
);

int32 __stdcall RFmxEVDO_GetUplinkSpreadingQmask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 *attrVal
);

int32 __stdcall RFmxEVDO_SetUplinkSpreadingQmask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 attrVal
);

int32 __stdcall RFmxEVDO_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxEVDO_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxEVDO_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetUplinkWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetUplinkWalshCodeLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetUplinkWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetUplinkWalshCodeNumber(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetUplinkBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetUplinkBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_CDASetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkRMSSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkPeakSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkRMSSymbolMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkRMSSymbolPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkMeanSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkTotalPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkTotalActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkPeakActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkMeanInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkIMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkIPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkQMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkQPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkMeanPilotPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_CDAGetResultsUplinkMeanAuxiliaryPilotPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPowerSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetReceiveFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetTransientDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetTransientDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxEVDO_SlotPhaseGetResultsMaximumHalfSlotPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

// Values for RFMXEVDO_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FALSE                                      0
#define RFMXEVDO_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_TRUE                                       1

// Values for RFMXEVDO_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FALSE                                      0
#define RFMXEVDO_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_TRUE                                       1

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxEVDO_CalculateFrequencyFromChannelNumber(
   int32 linkDirection,
   int32 bandClass,
   int32 channelNumber,
   float64 *centerFrequency
);

int32 __stdcall RFmxEVDO_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxEVDO_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxEVDO_AnalyzeSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxGSM.h sha256=5e182e6b7009ed3a9b15b2d4f99fbd5312dea7491ca471c712e172f0454fcf37 bytes=75680 -->
## FILE: imports/include/niRFmxGSM.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxGSM.h`
- sha256: `5e182e6b7009ed3a9b15b2d4f99fbd5312dea7491ca471c712e172f0454fcf37`
- bytes: 75680

````c

/****************************************************************************************************
*          National Instruments RFmx GSM
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2021.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxGSM.h
*
* Purpose:  National Instruments RFmx GSM,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_GSM_H__
#define __NI_RFMX_GSM_H__

#include "niRFmxInstr.h"

#define RFMXGSM_ATTR_MODACC_MEASUREMENT_ENABLED                              0x00401000
#define RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED                                0x00401002
#define RFMXGSM_ATTR_MODACC_AVERAGING_COUNT                                  0x00401004
#define RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL                             0x0040102a
#define RFMXGSM_ATTR_MODACC_MEASUREMENT_OFFSET                               0x0040102b
#define RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED                       0x00401005
#define RFMXGSM_ATTR_MODACC_ALL_TRACES_ENABLED                               0x00401006
#define RFMXGSM_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS                       0x00401007
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_RMS_EVM                         0x00401008
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM                      0x00401009
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_EVM                        0x0040100a
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM                     0x0040100b
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM                  0x0040100c
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL                      0x0040100d
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR                 0x0040100e
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR              0x0040100f
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PHASE_ERROR                     0x00401010
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR                  0x00401011
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR                 0x00401012
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR              0x00401013
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP                 0x00401014
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP              0x00401015
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR                0x00401016
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR             0x00401017
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR               0x00401018
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR            0x00401019
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL             0x0040101a
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR                0x0040101b
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR             0x0040101c
#define RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE                   0x0040101d
#define RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE                0x0040101e
#define RFMXGSM_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET                    0x0040101f
#define RFMXGSM_ATTR_MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET                 0x00401020
#define RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC                             0x00401021
#define RFMXGSM_ATTR_ORFS_MEASUREMENT_ENABLED                                0x00402000
#define RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED                                  0x00402002
#define RFMXGSM_ATTR_ORFS_AVERAGING_TYPE                                     0x00402003
#define RFMXGSM_ATTR_ORFS_AVERAGING_COUNT                                    0x00402004
#define RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL                               0x00402025
#define RFMXGSM_ATTR_ORFS_MEASUREMENT_OFFSET                                 0x00402026
#define RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE                                   0x00402005
#define RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE                              0x00402007
#define RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_START                           0x00402011
#define RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC                     0x00402012
#define RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_STOP                            0x00402013
#define RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE                           0x00402024
#define RFMXGSM_ATTR_ORFS_MODULATION_CARRIER_RBW                             0x0040200b
#define RFMXGSM_ATTR_ORFS_MODULATION_NUMBER_OF_OFFSETS                       0x0040201d
#define RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_FREQUENCY                        0x0040201e
#define RFMXGSM_ATTR_ORFS_MODULATION_OFFSET_RBW                              0x0040201f
#define RFMXGSM_ATTR_ORFS_SWITCHING_CARRIER_RBW                              0x0040200e
#define RFMXGSM_ATTR_ORFS_SWITCHING_NUMBER_OF_OFFSETS                        0x00402020
#define RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_FREQUENCY                         0x00402021
#define RFMXGSM_ATTR_ORFS_SWITCHING_OFFSET_RBW                               0x00402022
#define RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED                         0x00402006
#define RFMXGSM_ATTR_ORFS_ALL_TRACES_ENABLED                                 0x00402014
#define RFMXGSM_ATTR_ORFS_NUMBER_OF_ANALYSIS_THREADS                         0x00402015
#define RFMXGSM_ATTR_PVT_MEASUREMENT_ENABLED                                 0x00403000
#define RFMXGSM_ATTR_PVT_AVERAGING_ENABLED                                   0x00403002
#define RFMXGSM_ATTR_PVT_AVERAGING_TYPE                                      0x00403004
#define RFMXGSM_ATTR_PVT_AVERAGING_COUNT                                     0x00403005
#define RFMXGSM_ATTR_PVT_RBW_FILTER_BANDWIDTH                                0x00403007
#define RFMXGSM_ATTR_PVT_ALL_TRACES_ENABLED                                  0x00403009
#define RFMXGSM_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS                          0x0040300a
#define RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS                          0x0040300b
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_AVERAGE_POWER                          0x0040300c
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_WIDTH                            0x0040300d
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_MAXIMUM_POWER                          0x0040300e
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_MINIMUM_POWER                          0x0040300f
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_BURST_THRESHOLD                        0x00403010
#define RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS                     0x00403011
#define RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE                            0x0040d003
#define RFMXGSM_ATTR_RESULT_FETCH_TIMEOUT                                    0x0040c000
#define RFMXGSM_ATTR_CENTER_FREQUENCY                                        0x00400001
#define RFMXGSM_ATTR_REFERENCE_LEVEL                                         0x00400002
#define RFMXGSM_ATTR_EXTERNAL_ATTENUATION                                    0x00400003
#define RFMXGSM_ATTR_TRIGGER_TYPE                                            0x00400004
#define RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                             0x00400005
#define RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                               0x00400006
#define RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                            0x00400007
#define RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                             0x00400008
#define RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                        0x00400fff
#define RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                             0x00400009
#define RFMXGSM_ATTR_TRIGGER_DELAY                                           0x0040000a
#define RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                         0x0040000b
#define RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                     0x0040000c
#define RFMXGSM_ATTR_LINK_DIRECTION                                          0x0040000d
#define RFMXGSM_ATTR_BAND                                                    0x0040000e
#define RFMXGSM_ATTR_SIGNAL_STRUCTURE                                        0x00400017
#define RFMXGSM_ATTR_NUMBER_OF_TIMESLOTS                                     0x0040000f
#define RFMXGSM_ATTR_MODULATION_TYPE                                         0x00400010
#define RFMXGSM_ATTR_BURST_TYPE                                              0x00400011
#define RFMXGSM_ATTR_HB_FILTER_WIDTH                                         0x00400012
#define RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED                              0x00400013
#define RFMXGSM_ATTR_TSC                                                     0x00400014
#define RFMXGSM_ATTR_POWER_CONTROL_LEVEL                                     0x00400015
#define RFMXGSM_ATTR_TIMING_ADVANCE                                          0x00400018
#define RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE                              0x00400016
#define RFMXGSM_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                      0x0040d000
#define RFMXGSM_ATTR_SELECTED_PORTS                                          0x00400ffd
#define RFMXGSM_ATTR_REFERENCE_LEVEL_HEADROOM                                0x00400ffc
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR            0x00401023
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR         0x00401024
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR      0x00401025
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR                0x00401026
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR             0x00401027
#define RFMXGSM_ATTR_MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR          0x00401028
#define RFMXGSM_ATTR_MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR         0x00401029

// Values for RFMXGSM_ATTR_TRIGGER_TYPE
#define RFMXGSM_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXGSM_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXGSM_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXGSM_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXGSM_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXGSM_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXGSM_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXGSM_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXGSM_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXGSM_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXGSM_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXGSM_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXGSM_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXGSM_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXGSM_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXGSM_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXGSM_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXGSM_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXGSM_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXGSM_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXGSM_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXGSM_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXGSM_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXGSM_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXGSM_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXGSM_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXGSM_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXGSM_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXGSM_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXGSM_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXGSM_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXGSM_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXGSM_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXGSM_ATTR_LINK_DIRECTION
#define RFMXGSM_VAL_LINK_DIRECTION_DOWNLINK                                                        0
#define RFMXGSM_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for RFMXGSM_ATTR_BAND
#define RFMXGSM_VAL_BAND_PGSM                                                                      0
#define RFMXGSM_VAL_BAND_EGSM                                                                      1
#define RFMXGSM_VAL_BAND_RGSM                                                                      2
#define RFMXGSM_VAL_BAND_DCS1800                                                                   3
#define RFMXGSM_VAL_BAND_PCS1900                                                                   4
#define RFMXGSM_VAL_BAND_GSM450                                                                    5
#define RFMXGSM_VAL_BAND_GSM480                                                                    6
#define RFMXGSM_VAL_BAND_GSM850                                                                    7
#define RFMXGSM_VAL_BAND_GSM750                                                                    8
#define RFMXGSM_VAL_BAND_TGSM810                                                                   9

// Values for RFMXGSM_ATTR_SIGNAL_STRUCTURE
#define RFMXGSM_VAL_SIGNAL_STRUCTURE_BURSTED                                                       0
#define RFMXGSM_VAL_SIGNAL_STRUCTURE_CONTINUOUS                                                    1

// Values for RFMXGSM_ATTR_MODULATION_TYPE
#define RFMXGSM_VAL_MODULATION_TYPE_GMSK                                                           0
#define RFMXGSM_VAL_MODULATION_TYPE_8PSK                                                           1
#define RFMXGSM_VAL_MODULATION_TYPE_QPSK                                                           2
#define RFMXGSM_VAL_MODULATION_TYPE_16QAM                                                          3
#define RFMXGSM_VAL_MODULATION_TYPE_32QAM                                                          4

// Values for RFMXGSM_ATTR_BURST_TYPE
#define RFMXGSM_VAL_BURST_TYPE_NB                                                                  0
#define RFMXGSM_VAL_BURST_TYPE_HB                                                                  1
#define RFMXGSM_VAL_BURST_TYPE_AB                                                                  2

// Values for RFMXGSM_ATTR_HB_FILTER_WIDTH
#define RFMXGSM_VAL_HB_FILTER_WIDTH_NARROW                                                         0
#define RFMXGSM_VAL_HB_FILTER_WIDTH_WIDE                                                           1

// Values for RFMXGSM_ATTR_AUTO_TSC_DETECTION_ENABLED
#define RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_FALSE                                               0
#define RFMXGSM_VAL_AUTO_TSC_DETECTION_ENABLED_TRUE                                                1

// Values for RFMXGSM_ATTR_TSC
#define RFMXGSM_VAL_TSC0                                                                           0
#define RFMXGSM_VAL_TSC1                                                                           1
#define RFMXGSM_VAL_TSC2                                                                           2
#define RFMXGSM_VAL_TSC3                                                                           3
#define RFMXGSM_VAL_TSC4                                                                           4
#define RFMXGSM_VAL_TSC5                                                                           5
#define RFMXGSM_VAL_TSC6                                                                           6
#define RFMXGSM_VAL_TSC7                                                                           7

// Values for RFMXGSM_ATTR_BURST_SYNCHRONIZATION_TYPE
#define RFMXGSM_VAL_BURST_SYNC_TYPE_TSC                                                            0
#define RFMXGSM_VAL_BURST_SYNC_TYPE_AMPLITUDE                                                      1
#define RFMXGSM_VAL_BURST_SYNC_TYPE_NONE                                                           2

// Values for RFMXGSM_ATTR_MODACC_AVERAGING_ENABLED
#define RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXGSM_VAL_MODACC_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXGSM_ATTR_MODACC_MEASUREMENT_INTERVAL
#define RFMXGSM_VAL_MODACC_MEASUREMENT_INTERVAL_NUMBER_OF_TIMESLOTS                                0
#define RFMXGSM_VAL_MODACC_MEASUREMENT_INTERVAL_TIMESLOT_AT_OFFSET                                 1

// Values for RFMXGSM_ATTR_MODACC_DROOP_COMPENSATION_ENABLED
#define RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_FALSE                                        0
#define RFMXGSM_VAL_MODACC_DROOP_COMPENSATION_ENABLED_TRUE                                         1

// Values for RFMXGSM_ATTR_MODACC_RESULTS_DETECTED_TSC
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_UNKNOWN                                                    -1
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC0                                                       0
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC1                                                       1
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC2                                                       2
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC3                                                       3
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC4                                                       4
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC5                                                       5
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC6                                                       6
#define RFMXGSM_VAL_MODACC_DETECTED_TSC_TSC7                                                       7

// Values for RFMXGSM_ATTR_ORFS_AVERAGING_ENABLED
#define RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_FALSE                                                   0
#define RFMXGSM_VAL_ORFS_AVERAGING_ENABLED_TRUE                                                    1

// Values for RFMXGSM_ATTR_ORFS_AVERAGING_TYPE
#define RFMXGSM_VAL_ORFS_AVERAGING_TYPE_RMS                                                        0
#define RFMXGSM_VAL_ORFS_AVERAGING_TYPE_LOG                                                        1

// Values for RFMXGSM_ATTR_ORFS_MEASUREMENT_INTERVAL
#define RFMXGSM_VAL_ORFS_MEASUREMENT_INTERVAL_NUMBER_OF_TIMESLOTS                                  0
#define RFMXGSM_VAL_ORFS_MEASUREMENT_INTERVAL_TIMESLOT_AT_OFFSET                                   1

// Values for RFMXGSM_ATTR_ORFS_MEASUREMENT_TYPE
#define RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION_AND_SWITCHING                                 0
#define RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_MODULATION                                               1
#define RFMXGSM_VAL_ORFS_MEASUREMENT_TYPE_SWITCHING                                                2

// Values for RFMXGSM_ATTR_ORFS_OFFSET_FREQUENCY_MODE
#define RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_STANDARD                                            0
#define RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_SHORT                                               1
#define RFMXGSM_VAL_ORFS_OFFSET_FREQUENCY_MODE_CUSTOM                                              2

// Values for RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC
#define RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_FALSE                                      0
#define RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC_TRUE                                       1

// Values for RFMXGSM_ATTR_ORFS_EVALUATION_SYMBOLS_SCOPE
#define RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_SCOPE_OFFSET                                           0
#define RFMXGSM_VAL_ORFS_EVALUATION_SYMBOLS_SCOPE_OFFSET_AND_CARRIER                               1

// Values for RFMXGSM_ATTR_ORFS_NOISE_COMPENSATION_ENABLED
#define RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_FALSE                                          0
#define RFMXGSM_VAL_ORFS_NOISE_COMPENSATION_ENABLED_TRUE                                           1

// Values for RFMXGSM_ATTR_PVT_AVERAGING_ENABLED
#define RFMXGSM_VAL_PVT_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXGSM_VAL_PVT_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXGSM_ATTR_PVT_AVERAGING_TYPE
#define RFMXGSM_VAL_PVT_AVERAGING_TYPE_RMS                                                         0
#define RFMXGSM_VAL_PVT_AVERAGING_TYPE_LOG                                                         1
#define RFMXGSM_VAL_PVT_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXGSM_VAL_PVT_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXGSM_ATTR_PVT_RESULTS_MEASUREMENT_STATUS
#define RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXGSM_VAL_PVT_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXGSM_ATTR_PVT_RESULTS_SLOT_MEASUREMENT_STATUS
#define RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_FAIL                                               0
#define RFMXGSM_VAL_PVT_SLOT_MEASUREMENT_STATUS_PASS                                               1

// Values for RFMXGSM_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXGSM_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for Boolean
#define RFMXGSM_VAL_FALSE                                                                          0
#define RFMXGSM_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXGSM_VAL_MODACC                                                                         1 << 0
#define RFMXGSM_VAL_ORFS                                                                           1 << 1
#define RFMXGSM_VAL_PVT                                                                            1 << 2

// Values for FrequencyReferenceSource
#define RFMXGSM_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXGSM_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXGSM_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXGSM_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for RFAttenuationAuto
#define RFMXGSM_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXGSM_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for MechanicalAttenuationAuto
#define RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXGSM_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

/* ---------------- RFmxGSM APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxGSM_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxGSM_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxGSM_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxGSM_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxGSM_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxGSM_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxGSM_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxGSM_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxGSM_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxGSM_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxGSM_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxGSM_BuildSlotString(
   char selectorString[],
   int32 slotNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxGSM_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxGSM_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxGSM_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxGSM_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxGSM_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxGSM_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* done
);

int32 __stdcall RFmxGSM_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxGSM_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxGSM_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxGSM_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxGSM_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxGSM_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxGSM_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxGSM_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxGSM_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxGSM_ORFSCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxGSM_ORFSCfgEvaluationSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 evaluationSymbolsStart,
   int32 evaluationSymbolsIncludeTSC,
   float64 evaluationSymbolsStop
);

int32 __stdcall RFmxGSM_ORFSCfgMeasurementType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementType
);

int32 __stdcall RFmxGSM_ORFSCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxGSM_ORFSCfgOffsetFrequencyMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetFrequencyMode
);

int32 __stdcall RFmxGSM_ModAccCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxGSM_ModAccCfgDroopCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 droopCompensationEnabled
);

int32 __stdcall RFmxGSM_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxGSM_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxGSM_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxGSM_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxGSM_CfgNumberOfTimeslots(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfTimeslots
);

int32 __stdcall RFmxGSM_CfgAutoTSCDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoTSCDetectionEnabled
);

int32 __stdcall RFmxGSM_CfgSignalType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modulationType,
   int32 burstType,
   int32 HBFilterWidth
);

int32 __stdcall RFmxGSM_CfgTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 TSC
);

int32 __stdcall RFmxGSM_CfgBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 band
);

int32 __stdcall RFmxGSM_CfgBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstSynchronizationType
);

int32 __stdcall RFmxGSM_CfgLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection
);

int32 __stdcall RFmxGSM_CfgPowerControlLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerControlLevel
);

int32 __stdcall RFmxGSM_PVTCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxGSM_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxGSM_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxGSM_ORFSCfgModulationCustomOffsetFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 modulationCustomOffsetFrequency[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_ORFSCfgSwitchingCustomOffsetFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 switchingCustomOffsetFrequency[],
   int32 arraySize
);

int32 __stdcall RFmxGSM_CfgFrequencyARFCN(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection,
   int32 band,
   int32 ARFCN
);

int32 __stdcall RFmxGSM_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxGSM_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxGSM_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxGSM_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 minimumQuietTimeMode,
   float64 minimumQuietTime,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxGSM_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxGSM_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxGSM_ModAccFetchDemodulatedBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 demodulatedBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSCArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 detectedTSC[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellationTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationTraceI[],
   float32 constellationTraceQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ModAccFetchDetectedTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* detectedTSC
);

int32 __stdcall RFmxGSM_ModAccFetchEVMAmplitudeDroop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanAmplitudeDroop,
   float64* maximumAmplitudeDroop
);

int32 __stdcall RFmxGSM_ModAccFetchEVMMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanMagnitudeError,
   float64* maximumMagnitudeError
);

int32 __stdcall RFmxGSM_ModAccFetchEVMPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanPhaseError,
   float64* maximumPhaseError
);

int32 __stdcall RFmxGSM_ModAccFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSEVM,
   float64* maximumRMSEVM,
   float64* meanPeakEVM,
   float64* maximumPeakEVM,
   float64* ninetyFifthPercentileEVM,
   float64* meanFrequencyError,
   int32* peakEVMSymbol
);

int32 __stdcall RFmxGSM_ModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanIQGainImbalance,
   float64* maximumIQGainImbalance,
   float64* meanIQOriginOffset,
   float64* maximumIQOriginOffset
);

int32 __stdcall RFmxGSM_ModAccFetchPFER(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSPhaseError,
   float64* maximumRMSPhaseError,
   float64* meanPeakPhaseError,
   float64* maximumPeakPhaseError,
   float64* meanFrequencyError,
   int32* peakSymbol
);

int32 __stdcall RFmxGSM_ORFSFetchModulationPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 offsetFrequency[],
   float32 absolutePower[],
   float32 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ORFSFetchModulationResultsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* modulationCarrierPower,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ORFSFetchSwitchingPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 offsetFrequency[],
   float32 absolutePower[],
   float32 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_ORFSFetchSwitchingResultsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* switchingCarrierPower,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotAveragePower[],
   float64 slotBurstWidth[],
   int32 slotMeasurementStatus[],
   float64 slotMaximumPower[],
   float64 slotMinimumPower[],
   float64 slotBurstThreshold[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_PVTFetchPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 upperMask[],
   float32 signalPower[],
   float32 lowerMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxGSM_PVTFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxGSM_PVTFetchSlotMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* slotAveragePower,
   float64* slotBurstWidth,
   int32* slotMeasurementStatus,
   float64* slotMaximumPower,
   float64* slotMinimumPower,
   float64* slotBurstThreshold
);

int32 __stdcall RFmxGSM_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetDroopCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetDroopCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVM95thpercentileEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMPeakEVMSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanAmplitudeDroop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumAmplitudeDroop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMeanRMSPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMaximumRMSPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMeanPeakPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMaximumPeakPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERPeakPhaseErrorSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFERMaximumFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsMeanIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsMaximumIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsMaximumIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsDetectedTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanPeakMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumPeakMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVM95thPercentileMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMeanPeakPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVMMaximumPeakPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsEVM95thPercentilePhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ModAccGetResultsPFER95thPercentilePhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetMeasurementType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetMeasurementType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetOffsetFrequencyMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetOffsetFrequencyMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetEvaluationSymbolsStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetEvaluationSymbolsStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetEvaluationSymbolsIncludeTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetEvaluationSymbolsIncludeTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetEvaluationSymbolsStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetEvaluationSymbolsStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetEvaluationSymbolsScope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetEvaluationSymbolsScope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetModulationCarrierRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetModulationCarrierRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetModulationNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetModulationNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetModulationOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetModulationOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetModulationOffsetRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSGetSwitchingCarrierRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetSwitchingCarrierRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetSwitchingNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetSwitchingNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetSwitchingOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetSwitchingOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetSwitchingOffsetRBW(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_ORFSGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_ORFSGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_ORFSSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_PVTGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotAveragePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotBurstWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotMaximumPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotMinimumPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotBurstThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_PVTGetResultsSlotMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetSignalStructure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetSignalStructure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetNumberOfTimeslots(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetNumberOfTimeslots(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetBurstType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetBurstType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetHBFilterWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetHBFilterWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetAutoTSCDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetAutoTSCDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetTSC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetPowerControlLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetPowerControlLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetTimingAdvance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetTimingAdvance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxGSM_SetBurstSynchronizationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxGSM_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxGSM_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxGSM_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxGSM_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxGSM_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

// Values for RFMXGSM_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXGSM_VAL_MINIMUM_QUIET_TIME_MODE_AUTO                                                   0
#define RFMXGSM_VAL_MINIMUM_QUIET_TIME_MODE_MANUAL                                                 1

// Values for RFMXGSM_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXGSM_VAL_IQ_POWER_EDGE_LEVEL_TYPE_RELATIVE                                              0
#define RFMXGSM_VAL_IQ_POWER_EDGE_LEVEL_TYPE_ABSOLUTE                                              1

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxGSM_CalculateFrequencyFromARFCN(
   int32 linkDirection,
   int32 band,
   int32 ARFCN,
   float64 *centerFrequency
);

int32 __stdcall RFmxGSM_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxGSM_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxInstr.h sha256=c8257a687facde81d4af8fdedb630a1bb17ac6011fc3081591ee1b510af46735 bytes=75753 -->
## FILE: imports/include/niRFmxInstr.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxInstr.h`
- sha256: `c8257a687facde81d4af8fdedb630a1bb17ac6011fc3081591ee1b510af46735`
- bytes: 75753

````c
/******************************************************************************
 *          National Instruments RFmx Instr
 *-----------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2014-2016.  All Rights Reserved.
 *-----------------------------------------------------------------------------
 *
 * Title:    niRFmxInstr.h
 * Purpose:  National Instruments RFmx Instr
 *           Attribute IDs,
 *           Attribute Values,
 *           Functions declarations.
 *
 *****************************************************************************/

#ifndef __NI_RFMX_INSTR_H__
#define __NI_RFMX_INSTR_H__


#ifndef _NI_int8_DEFINED_
#define _NI_int8_DEFINED_
typedef char               int8;
#endif
#ifndef _NI_uInt8_DEFINED_
#define _NI_uInt8_DEFINED_
typedef unsigned char      uInt8;
#endif
#ifndef _NI_int16_DEFINED_
#define _NI_int16_DEFINED_
typedef signed short       int16;
#endif
#ifndef _NI_uInt16_DEFINED_
#define _NI_uInt16_DEFINED_
typedef unsigned short     uInt16;
#endif
#ifndef _NI_int32_DEFINED_
#define _NI_int32_DEFINED_
typedef signed long        int32;
#endif
#ifndef _NI_uInt32_DEFINED_
#define _NI_uInt32_DEFINED_
typedef unsigned long      uInt32;
#endif
#ifndef _NI_float32_DEFINED_
#define _NI_float32_DEFINED_
typedef float              float32;
#endif
#ifndef _NI_float64_DEFINED_
#define _NI_float64_DEFINED_
typedef double             float64;
#endif
#ifndef _NI_int64_DEFINED_
#define _NI_int64_DEFINED_
#ifdef __linux__
typedef long long int      int64;
#else
typedef __int64            int64;
#endif
#endif
#ifndef _NI_uInt64_DEFINED_
#define _NI_uInt64_DEFINED_
#ifdef __linux__
typedef unsigned long long uInt64;
#else
typedef unsigned __int64   uInt64;
#endif
#endif

#ifndef _NI_RFMX_SESSION_DEFINED_
#define _NI_RFMX_SESSION_DEFINED_
typedef void*   niRFmxInstrHandle;
#endif

#if !defined(_NIComplexDoublePrecision)
#define _NIComplexDoublePrecision

#ifndef _WIN64
#pragma pack(push, 1)
#endif

typedef struct NIComplexDouble_struct {
   float64 real;
   float64 imaginary;
} NIComplexDouble;

#ifndef _WIN64
#pragma pack(pop)
#endif

#endif

#if !defined(_NIComplexSinglePrecision)
#define _NIComplexSinglePrecision

#ifndef _WIN64
#pragma pack(push, 1)
#endif

typedef struct NIComplexSingle_struct {
   float32 real;
   float32 imaginary;
} NIComplexSingle;

#ifndef _WIN64
#pragma pack(pop)
#endif

#endif

/*- Time Structures and Helpers ----------------------------------*/

// Please visit ni.com/info and enter the Info Code NI_BTF for more information
#ifndef CVITime_DECLARED
#define CVITime_DECLARED
typedef struct CVITime { unsigned __int64 lsb; __int64 msb; } CVITime;
#endif
#ifndef CVIAbsoluteTime_DECLARED
#define CVIAbsoluteTime_DECLARED
typedef union CVIAbsoluteTime { CVITime cviTime; unsigned int u32Data[4]; } CVIAbsoluteTime;
#endif

/* -- RFmxInstr Attribute IDs --*/

#define RFMXINSTR_ATTR_FREQUENCY_REFERENCE_SOURCE                          0x00000002
#define RFMXINSTR_ATTR_FREQUENCY_REFERENCE_FREQUENCY                       0x00000003
#define RFMXINSTR_ATTR_RF_ATTENUATION_AUTO                                 0x00000004
#define RFMXINSTR_ATTR_RF_ATTENUATION_VALUE                                0x00000005
#define RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_AUTO                         0x00000006
#define RFMXINSTR_ATTR_MECHANICAL_ATTENUATION_VALUE                        0x00000007
#define RFMXINSTR_ATTR_LO_EXPORT_ENABLED                                   0x00000021
#define RFMXINSTR_ATTR_FREQUENCY_REFERENCE_EXPORTED_TERMINAL               0x00000022
#define RFMXINSTR_ATTR_LO2_EXPORT_ENABLED                                  0x0000003A
#define RFMXINSTR_ATTR_TRIGGER_EXPORT_OUTPUT_TERMINAL                      0x00000023
#define RFMXINSTR_ATTR_TRIGGER_TERMINAL_NAME                               0x00000024
#define RFMXINSTR_ATTR_DEVICE_TEMPERATURE                                  0x00000018
#define RFMXINSTR_ATTR_DIGITIZER_TEMPERATURE                               0x00000019
#define RFMXINSTR_ATTR_LO_TEMPERATURE                                      0x0000001a
#define RFMXINSTR_ATTR_SERIAL_NUMBER                                       0x0000001e
#define RFMXINSTR_ATTR_INSTRUMENT_MODEL                                    0x0000001c
#define RFMXINSTR_ATTR_MODULE_REVISION                                     0x0000001d
#define RFMXINSTR_ATTR_INSTRUMENT_FIRMWARE_REVISION                        0x0000001b
#define RFMXINSTR_ATTR_PRESELECTOR_PRESENT                                 0x0000001f
#define RFMXINSTR_ATTR_RF_PREAMP_PRESENT                                   0x00000020
#define RFMXINSTR_ATTR_PREAMP_ENABLED                                      0x0000000e
#define RFMXINSTR_ATTR_CHANNEL_COUPLING                                    0x0000000b
#define RFMXINSTR_ATTR_TUNING_SPEED                                        0x00000008
#define RFMXINSTR_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED                   0x0000000c
#define RFMXINSTR_ATTR_MIXER_LEVEL                                         0x00000010
#define RFMXINSTR_ATTR_MIXER_LEVEL_OFFSET                                  0x0000000f
#define RFMXINSTR_ATTR_DOWNCONVERTER_CENTER_FREQUENCY                      0x0000000d
#define RFMXINSTR_ATTR_LO_SOURCE                                           0x0000003B
#define RFMXINSTR_ATTR_LO_FREQUENCY                                        0x0000003C
#define RFMXINSTR_ATTR_OSP_DELAY_ENABLED                                   0x00000017
#define RFMXINSTR_ATTR_PHASE_OFFSET                                        0x00000013
#define RFMXINSTR_ATTR_FFT_WIDTH                                           0x00000016
#define RFMXINSTR_ATTR_CLEANER_SPECTRUM                                    0x00000025
#define RFMXINSTR_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET                        0x00000011
#define RFMXINSTR_ATTR_DIGITIZER_DITHER_ENABLED                            0x00000015
#define RFMXINSTR_ATTR_IF_FILTER_BANDWIDTH                                 0x00000030
#define RFMXINSTR_ATTR_LO_INJECTION_SIDE                                   0x00000012
#define RFMXINSTR_ATTR_FREQUENCY_SETTLING_UNITS                            0x00000009
#define RFMXINSTR_ATTR_FREQUENCY_SETTLING                                  0x0000000a
#define RFMXINSTR_ATTR_SUBSPAN_OVERLAP                                     0x00000032
#define RFMXINSTR_ATTR_DOWNCONVERTER_GAIN                                  0x00000034
#define RFMXINSTR_ATTR_RECOMMENDED_ACQUISITION_TYPE                        0x00000027
#define RFMXINSTR_ATTR_RECOMMENDED_NUMBER_OF_RECORDS                       0x00000028
#define RFMXINSTR_ATTR_RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME              0x00000029
#define RFMXINSTR_ATTR_RECOMMENDED_IQ_ACQUISITION_TIME                     0x0000002a
#define RFMXINSTR_ATTR_RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE                  0x0000002b
#define RFMXINSTR_ATTR_RECOMMENDED_IQ_PRE_TRIGGER_TIME                     0x0000002c
#define RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_ACQUISITION_SPAN               0x0000002d
#define RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_FFT_WINDOW                     0x0000002e
#define RFMXINSTR_ATTR_RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH           0x0000002f
#define RFMXINSTR_ATTR_RECOMMENDED_CENTER_FREQUENCY                        0x00000039
#define RFMXINSTR_ATTR_COMMON_MODE_LEVEL                                   0x00000046
#define RFMXINSTR_ATTR_SMU_RESOURCE_NAME                                   0x00000047
#define RFMXINSTR_ATTR_SMU_CHANNEL                                         0x00000048
#define RFMXINSTR_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET                      0x00000035
#define RFMXINSTR_ATTR_RF_ATTENUATION_STEP_SIZE                            0x00000036
#define RFMXINSTR_ATTR_LO_LEAKAGE_AVOIDANCE_ENABLED                        0x00000037
#define RFMXINSTR_ATTR_AMPLITUDE_SETTLING                                  0x00000038
#define RFMXINSTR_ATTR_OVERFLOW_ERROR_REPORTING                            0x0000004d
#define RFMXINSTR_ATTR_LO_IN_POWER                                         0x0000004e
#define RFMXINSTR_ATTR_LO_OUT_POWER                                        0x0000004f
#define RFMXINSTR_ATTR_LO_PLL_FRACTIONAL_MODE                              0x0000005a
#define RFMXINSTR_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH                  0x0000005b
#define RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED                             0x0000005c
#define RFMXINSTR_ATTR_LO_VCO_FREQUENCY_STEP_SIZE                          0x00000050
#define RFMXINSTR_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE                   0x0000005e
#define RFMXINSTR_ATTR_LO_FREQUENCY_STEP_SIZE                              0x0000005f
#define RFMXINSTR_ATTR_RF_HIGHPASS_FILTER_FREQUENCY                        0x00000031
#define RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK                     0x00000075
#define RFMXINSTR_ATTR_SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL       0x00000076
#define RFMXINSTR_ATTR_START_TRIGGER_TYPE                                  0x00000062
#define RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE_SOURCE                   0x00000063
#define RFMXINSTR_ATTR_START_TRIGGER_DIGITAL_EDGE                          0x00000064
#define RFMXINSTR_ATTR_START_TRIGGER_EXPORT_OUTPUT_TERMINAL                0x00000065
#define RFMXINSTR_ATTR_START_TRIGGER_TERMINAL_NAME                         0x00000066
#define RFMXINSTR_ATTR_ADVANCE_TRIGGER_TYPE                                0x00000067
#define RFMXINSTR_ATTR_ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE                 0x00000068
#define RFMXINSTR_ATTR_ADVANCE_TRIGGER_EXPORT_OUTPUT_TERMINAL              0x00000069
#define RFMXINSTR_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME                       0x0000006a
#define RFMXINSTR_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL               0x0000006b
#define RFMXINSTR_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME                 0x0000006c
#define RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL             0x0000006d
#define RFMXINSTR_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME               0x0000006e
#define RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL           0x0000006f
#define RFMXINSTR_ATTR_READY_FOR_REFERENCE_EVENT_TERMINAL_NAME             0x00000070
#define RFMXINSTR_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL                 0x00000071
#define RFMXINSTR_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME                   0x00000072
#define RFMXINSTR_ATTR_DONE_EVENT_OUTPUT_TERMINAL                          0x00000073
#define RFMXINSTR_ATTR_DONE_EVENT_TERMINAL_NAME                            0x00000074
#define RFMXINSTR_ATTR_TEMPERATURE_READ_INTERVAL                           0x00000077
#define RFMXINSTR_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION           0x00000078
#define RFMXINSTR_ATTR_NUMBER_OF_RAW_IQ_RECORDS                            0x00000080
#define RFMXINSTR_ATTR_LO_SHARING_MODE                                     0x00000044
#define RFMXINSTR_ATTR_NUMBER_OF_LO_SHARING_GROUPS                         0x00000061
#define RFMXINSTR_ATTR_LOAD_OPTIONS                                        0x000000A3
#define RFMXINSTR_ATTR_DIGITAL_GAIN                                        0x00000054
#define RFMXINSTR_ATTR_LO_SPLITTER_LOSS_FREQUENCY                          0x000000b8
#define RFMXINSTR_ATTR_LO_SPLITTER_LOSS                                    0x000000b9
#define RFMXINSTR_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS                      0x000000bc


/* -- Values for binary attributes -- */
#define RFMXINSTR_VAL_FALSE                                                0
#define RFMXINSTR_VAL_TRUE                                                 1

/* -- Values for RF Attenuation Auto -- */

#define RFMXINSTR_VAL_RF_ATTENUATION_AUTO_FALSE                            0
#define RFMXINSTR_VAL_RF_ATTENUATION_AUTO_TRUE                             1

/* -- Values for RF Mechanical Attenuation Auto -- */

#define RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                    0
#define RFMXINSTR_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                     1

/* -- Values for LO2 Export Enabled -- */
#define RFMXINSTR_VAL_LO2_EXPORT_DISABLED                                  0
#define RFMXINSTR_VAL_LO2_EXPORT_ENABLED                                   1

/* -- Values for LO Source  -- */

#define RFMXINSTR_VAL_LO_SOURCE_NONE                                        "None"
#define RFMXINSTR_VAL_LO_SOURCE_ONBOARD                                     "Onboard"
#define RFMXINSTR_VAL_LO_SOURCE_LO_IN                                       "LO_In"
#define RFMXINSTR_VAL_LO_SOURCE_SECONDARY                                   "Secondary"
#define RFMXINSTR_VAL_LO_SOURCE_SG_SA_SHARED                                "SG_SA_Shared"
#define RFMXINSTR_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED                      "Automatic_SG_SA_Shared"

/* -- Values for Tuning Speed -- */

#define RFMXINSTR_VAL_TUNING_SPEED_NORMAL                                  0
#define RFMXINSTR_VAL_TUNING_SPEED_MEDIUM                                  1
#define RFMXINSTR_VAL_TUNING_SPEED_FAST                                    2

/* -- Values for Frequency Settling Units -- */

#define RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_PPM                         0
#define RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_LOCK          1
#define RFMXINSTR_VAL_FREQUENCY_SETTLING_UNITS_SECONDS_AFTER_IO            2

/* -- Values for Cleaner Spectrum -- */

#define RFMXINSTR_VAL_CLEANER_SPECTRUM_DISABLED                            0
#define RFMXINSTR_VAL_CLEANER_SPECTRUM_ENABLED                             1

/* -- Values for Channel Coupling -- */

#define RFMXINSTR_VAL_CHANNEL_COUPLING_AC_COUPLED                          0
#define RFMXINSTR_VAL_CHANNEL_COUPLING_DC_COUPLED                          1

/* -- Values for Downconverter Preselector Enabled -- */

#define RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_DISABLED                   0
#define RFMXINSTR_VAL_DOWNCONVERTER_PRESELECTOR_ENABLED                    1

/* -- Values for Preamp Enabled -- */

#define RFMXINSTR_VAL_PREAMP_DISABLED                                      0
#define RFMXINSTR_VAL_PREAMP_ENABLED                                       1
#define RFMXINSTR_VAL_PREAMP_AUTOMATIC                                     3

/* -- Values for LO Injection Side -- */

#define RFMXINSTR_VAL_LO_INJECTION_HIGH_SIDE                               0
#define RFMXINSTR_VAL_LO_INJECTION_LOW_SIDE                                1

/* -- Values for Digitizer Dither Enabled -- */

#define RFMXINSTR_VAL_DIGITIZER_DITHER_DISABLED                            0
#define RFMXINSTR_VAL_DIGITIZER_DITHER_ENABLED                             1

/* -- Values for OSP Delay Enabled -- */

#define RFMXINSTR_VAL_OSP_DELAY_DISABLED                                   0
#define RFMXINSTR_VAL_OSP_DELAY_ENABLED                                    1

/* -- Values for Export Signal Source -- */

#define RFMXINSTR_VAL_START_TRIGGER                                        0
#define RFMXINSTR_VAL_REFERENCE_TRIGGER                                    1
#define RFMXINSTR_VAL_ADVANCE_TRIGGER                                      2
#define RFMXINSTR_VAL_READY_FOR_START_EVENT                                3
#define RFMXINSTR_VAL_READY_FOR_REFERENCE_EVENT                            4
#define RFMXINSTR_VAL_READY_FOR_ADVANCE_EVENT                              5
#define RFMXINSTR_VAL_END_OF_RECORD_EVENT                                  6
#define RFMXINSTR_VAL_DONE_EVENT                                           7
#define RFMXINSTR_VAL_REFERENCE_CLOCK                                      8

/* -- Values for LO Export Enabled -- */

#define RFMXINSTR_VAL_LO_EXPORT_DISABLED                                   0
#define RFMXINSTR_VAL_LO_EXPORT_ENABLED                                    1

/* -- Values for Acquisition Type -- */

#define RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ                      0
#define RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_SPECTRAL                1
#define RFMXINSTR_VAL_RECOMMENDED_ACQUISITION_TYPE_IQ_OR_SPECTRAL          2

/* -- Values for FFT Window -- */

#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_NONE                 0
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_FLAT_TOP             1
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HANNING              2
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_HAMMING              3
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_GAUSSIAN             4
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN             5
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_BLACKMAN_HARRIS      6
#define RFMXINSTR_VAL_RECOMMENDED_SPECTRAL_FFT_WINDOW_KAISER_BESSEL        7

/* -- Values for Steps to Omit -- */
#define RFMXINSTR_VAL_SELF_CAL_STEP_NONE                                   0
#define RFMXINSTR_VAL_SELF_CAL_STEP_PRESELECTOR_ALIGNMENT                  1 << 0
#define RFMXINSTR_VAL_SELF_CAL_STEP_GAIN_REFERENCE                         1 << 1
#define RFMXINSTR_VAL_SELF_CAL_STEP_IF_FLATNESS                            1 << 2
#define RFMXINSTR_VAL_SELF_CAL_STEP_DIGITIZER_SELF_CAL                     1 << 3
#define RFMXINSTR_VAL_SELF_CAL_STEP_LO_SELF_CAL                            1 << 4
#define RFMXINSTR_VAL_SELF_CAL_STEP_AMPLITUDE_ACCURACY                     1 << 5
#define RFMXINSTR_VAL_SELF_CAL_STEP_RESIDUAL_LO_POWER                      1 << 6
#define RFMXINSTR_VAL_SELF_CAL_STEP_IMAGE_SUPPRESSION                      1 << 7
#define RFMXINSTR_VAL_SELF_CAL_STEP_SYNTHESIZER_ALIGNMENT                  1 << 8
#define RFMXINSTR_VAL_SELF_CAL_STEP_DC_OFFSET                              1 << 9
/* -- Values for Frequency Reference Source -- */

#define RFMXINSTR_VAL_ONBOARD_CLOCK_STR                                    "OnboardClock"
#define RFMXINSTR_VAL_REF_IN_STR                                           "RefIn"
#define RFMXINSTR_VAL_PXI_CLK_STR                                          "PXI_Clk"
#define RFMXINSTR_VAL_CLK_IN_STR                                           "ClkIn"
#define RFMXINSTR_VAL_REF_IN2_STR                                          "RefIn2"
#define RFMXINSTR_VAL_PXI_CLK_MASTER_STR                                   "PXI_ClkMaster"

/* -- Values for Frequency Reference Exported Terminal -- */

#define RFMXINSTR_VAL_NONE_STR                                             ""
#define RFMXINSTR_VAL_REF_OUT_STR                                          "RefOut"
#define RFMXINSTR_VAL_REF_OUT2_STR                                         "RefOut2"
#define RFMXINSTR_VAL_CLK_OUT_STR                                          "ClkOut"

/* -- Values for Trigger Export Output Terminal -- */

#define RFMXINSTR_VAL_DO_NOT_EXPORT_STR                                    ""
#define RFMXINSTR_VAL_PFI0_STR                                             "PFI0"
#define RFMXINSTR_VAL_PFI1_STR                                             "PFI1"
#define RFMXINSTR_VAL_PXI_TRIG0_STR                                        "PXI_Trig0"
#define RFMXINSTR_VAL_PXI_TRIG1_STR                                        "PXI_Trig1"
#define RFMXINSTR_VAL_PXI_TRIG2_STR                                        "PXI_Trig2"
#define RFMXINSTR_VAL_PXI_TRIG3_STR                                        "PXI_Trig3"
#define RFMXINSTR_VAL_PXI_TRIG4_STR                                        "PXI_Trig4"
#define RFMXINSTR_VAL_PXI_TRIG5_STR                                        "PXI_Trig5"
#define RFMXINSTR_VAL_PXI_TRIG6_STR                                        "PXI_Trig6"
#define RFMXINSTR_VAL_PXI_TRIG7_STR                                        "PXI_Trig7"
#define RFMXINSTR_VAL_PXI_STAR_STR                                         "PXI_STAR"
#define RFMXINSTR_VAL_PXIE_DSTARC_STR                                      "PXIe_DStarC"
#define RFMXINSTR_VAL_PXIE_DSTARB_STR                                      "PXIe_DStarB"
#define RFMXINSTR_VAL_TIMER_EVENT_STR                                      "TimerEvent"
#define RFMXINSTR_VAL_PULSE_IN_STR                                         "PulseIn"
#define RFMXINSTR_VAL_DIO_PFI0_STR                                         "DIO/PFI0"
#define RFMXINSTR_VAL_DIO_PFI1_STR                                         "DIO/PFI1"
#define RFMXINSTR_VAL_DIO_PFI2_STR                                         "DIO/PFI2"
#define RFMXINSTR_VAL_DIO_PFI3_STR                                         "DIO/PFI3"
#define RFMXINSTR_VAL_DIO_PFI4_STR                                         "DIO/PFI4"
#define RFMXINSTR_VAL_DIO_PFI5_STR                                         "DIO/PFI5"
#define RFMXINSTR_VAL_DIO_PFI6_STR                                         "DIO/PFI6"
#define RFMXINSTR_VAL_DIO_PFI7_STR                                         "DIO/PFI7"

/* -- Values for LO Leakage Avoidance Enabled -- */
#define RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_FALSE                   0
#define RFMXINSTR_VAL_LO_LEAKAGE_AVOIDANCE_ENABLED_TRUE                    1

//Enum PersonalityID
#define RFMXINSTR_VAL_PERSONALITY_NONE                                      0
#define RFMXINSTR_VAL_PERSONALITY_SPECAN                                   (1 << 0)
#define RFMXINSTR_VAL_PERSONALITY_DEMOD                                    (1 << 1)
#define RFMXINSTR_VAL_PERSONALITY_LTE                                      (1 << 2)
#define RFMXINSTR_VAL_PERSONALITY_GSM                                      (1 << 3)
#define RFMXINSTR_VAL_PERSONALITY_WCDMA                                    (1 << 4)
#define RFMXINSTR_VAL_PERSONALITY_CDMA2K                                   (1 << 5)
#define RFMXINSTR_VAL_PERSONALITY_TDSCDMA                                  (1 << 6)
#define RFMXINSTR_VAL_PERSONALITY_EVDO                                     (1 << 7)
#define RFMXINSTR_VAL_PERSONALITY_NR                                       (1 << 8)
#define RFMXINSTR_VAL_PERSONALITY_BT                                       (1 << 10)
#define RFMXINSTR_VAL_PERSONALITY_WLAN                                     (1 << 9)
#define RFMXINSTR_VAL_PERSONALITY_VNA                                      (1 << 12)
#define RFMXINSTR_VAL_PERSONALITY_PULSE                                    (1 << 11)
#define RFMXINSTR_VAL_PERSONALITY_UWB                                      (1 << 13)
#define RFMXINSTR_VAL_PERSONALITY_ALL                                      0x7FFFFFFF

/* -- Values for Overflow Error Reporting -- */
#define RFMXINSTR_VAL_OVERFLOW_ERROR_REPORTING_WARNING                     0
#define RFMXINSTR_VAL_OVERFLOW_ERROR_REPORTING_DISABLED                    1

/*- Values for S-parameters orientation passed to Create De-embedding S-parameter Table functions -*/
#define RFMXINSTR_VAL_PORT1_TOWARDS_DUT                                    0
#define RFMXINSTR_VAL_PORT2_TOWARDS_DUT                                    1

/*- Values for Linear Interpolation passed to Configure External Attenuation Interpolation Linear function -*/
#define RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY       0
#define RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE      1
#define RFMXINSTR_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE   2

/*  Values for LO PLL Fractional Mode */
#define RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_DISABLED                      0
#define RFMXINSTR_VAL_LO_PLL_FRACTIONAL_MODE_ENABLED                       1

/* Values for Optimize Path For Signal Bandwidth */
#define RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_DISABLED          0
#define RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_ENABLED           1
#define RFMXINSTR_VAL_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH_AUTOMATIC         2

/*  Values for Input Isolation Enabled */
#define RFMXINSTR_VAL_INPUT_ISOLATION_DISABLED                             0
#define RFMXINSTR_VAL_INPUT_ISOLATION_ENABLED                              1

/* Values for S-Parameter Type */
#define RFMXINSTR_VAL_SPARAMETER_TYPE_SCALAR                               1
#define RFMXINSTR_VAL_SPARAMETER_TYPE_VECTOR                               2
#define RFMXINSTR_VAL_SPARAMETER_TYPE_AMPLITUDE_FLATNESS                   3
#define RFMXINSTR_VAL_SPARAMETER_TYPE_AMPLITUDE_AND_PHASE_FLATNESS         4

/* Values for Self Calibration Validity Check */
#define RFMXINSTR_VAL_SELF_CALIBRATION_VALIDITY_CHECK_OFF                  0
#define RFMXINSTR_VAL_SELF_CALIBRATION_VALIDITY_CHECK_ENABLED              1

/* Values for Start Trigger Type */
#define RFMXINSTR_VAL_START_TRIGGER_TYPE_NONE                              0
#define RFMXINSTR_VAL_START_TRIGGER_TYPE_DIGITAL_EDGE                      1
#define RFMXINSTR_VAL_START_TRIGGER_TYPE_SOFTWARE                          3

/* Values for Start Trigger Digital Edge */
#define RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_RISING_EDGE               0
#define RFMXINSTR_VAL_START_TRIGGER_DIGITAL_EDGE_FALLING_EDGE              1

/* Values for Advance Trigger Type */
#define RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_NONE                            0
#define RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_DIGITAL_EDGE                    1
#define RFMXINSTR_VAL_ADVANCE_TRIGGER_TYPE_SOFTWARE                        3

/* Values for LO Sharing Mode */
#define RFMXINSTR_VAL_LO_SHARING_MODE_DISABLED                             0
#define RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_STAR                        3
#define RFMXINSTR_VAL_LO_SHARING_MODE_EXTERNAL_DAISY_CHAIN                 4
#define RFMXINSTR_VAL_LO_SHARING_MODE_SPLITTER_AND_DAISY_CHAIN             5

// Values for RFMXINSTR_ATTR_LOAD_OPTIONS
#define RFMXINSTR_VAL_LOAD_OPTIONS_SKIP_NONE                               0
#define RFMXINSTR_VAL_LOAD_OPTIONS_SKIP_RFINSTR                            1

/*****************************************************************************/
/*= Macros for checking for errors.                                 ======== */
/*= The RFmxcheckWarn macro preserve warnings.                      ======== */
/*****************************************************************************/
#ifndef RFmxCheckWarn
#define RFmxCheckWarn(fCall)     if (1) {int32 _code_; if (_code_ = (fCall), _code_ < 0)    \
                                    {error = _code_;goto Error;}        \
                                    else error = (error==0)?_code_:error;} else error = error
#endif

#ifndef RFmxCheckAlloc
#define RFmxCheckAlloc(fCall)    if ((fCall) == 0) \
                                 {error = -1; goto Error;}  else error = error
#endif


#ifdef __cplusplus
extern "C"
{
#endif

   /******************************************************************************
    *------------------- NI RFmxInstr Function Declarations ---------------------*
    *****************************************************************************/

   // Initializiation methods
   int32 __stdcall RFmxInstr_Initialize(
      char resourceName[],
      char optionString[],
      niRFmxInstrHandle *handleOut,
      int32 *isNewSession);

   int32 __stdcall RFmxInstr_InitializeFromNIRFSASession(
      uInt32 NIRFSASession,
      niRFmxInstrHandle *handleOut);

   int32 __stdcall RFmxInstr_InitializeFromNIRFSASessionArray(
       uInt32 NIRFSASessions[],
       int32 numberOfNIRFSASessions,
       niRFmxInstrHandle* handleOut
       );

   // Close method
   int32 __stdcall RFmxInstr_Close(
      niRFmxInstrHandle instrumentHandle,
      int32 forceDestroy);

   // Error methods
   int32 __stdcall RFmxInstr_GetError(
      niRFmxInstrHandle instrumentHandle,
      int32* errorCode,
      int32 errorDescriptionBufferSize,
      char errorDescription[]);

   int32 __stdcall RFmxInstr_GetErrorString(
      niRFmxInstrHandle instrumentHandle,
      int32 errorCode,
      int32 errorDescriptionBufferSize,
      char errorDescription[]);

   // Configuation methods
   int32 __stdcall RFmxInstr_CfgFrequencyReference(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char frequencyReferenceSource[],
      float64 frequencyReferenceFrequency);

   int32 __stdcall RFmxInstr_CfgMechanicalAttenuation(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 mechanicalAttenuationAuto,
      float64 mechanicalAttenuationValue);

   int32 __stdcall RFmxInstr_CfgRFAttenuation(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 RFAttenuationAuto,
      float64 RFAttenuationValue);

   int32 __stdcall RFmxInstr_CfgExternalAttenuationTable(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[],
      float64 frequency[],
      float64 externalAttenuation[],
      int32 arraySize
   );

   int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 sParameterType
   );

   int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationTable(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[],
      float64 frequency[],
      int32 frequencyArraySize,
      NIComplexDouble sParameters[],
      int32 sParameterTableSize,
      int32 numberOfPorts,
      int32 sParameterOrientation
   );

   int32 __stdcall RFmxInstr_CfgSParameterExternalAttenuationTableSplit(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[],
      float64 frequency[],
      int32 frequencyArraySize,
      float64 sParametersI[],
      float64 sParametersQ[],
      int32 sParameterTableSize,
      int32 numberOfPorts,
      int32 sParameterOrientation
   );

   int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationNearest
   (
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[]
   );

   int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationLinear
   (
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[],
      int32 format
   );

   int32 __stdcall RFmxInstr_CfgExternalAttenuationInterpolationSpline
   (
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[]
   );

   int32 __stdcall RFmxInstr_DeleteExternalAttenuationTable(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[]
   );

   int32 __stdcall RFmxInstr_DeleteAllExternalAttenuationTables(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[]
   );

   int32 __stdcall RFmxInstr_EnableCalibrationPlane(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[]
   );

   int32 __stdcall RFmxInstr_DisableCalibrationPlane(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[]
   );

   // Utility methods
   int32 __stdcall RFmxInstr_WaitForAcquisitionComplete(
      niRFmxInstrHandle instrumentHandle,
      float64 timeout);

   int32 __stdcall RFmxInstr_CheckAcquisitionStatus(
      niRFmxInstrHandle instrumentHandle,
      int32* acquisitionDone
   );

   int32 __stdcall RFmxInstr_ResetToDefault(
      niRFmxInstrHandle instrumentHandle);

   int32 __stdcall RFmxInstr_ResetDriver(
      niRFmxInstrHandle instrumentHandle);

   int32 __stdcall RFmxInstr_GetNIRFSASession(
      niRFmxInstrHandle instrumentHandle,
      uInt32 *niRfsaSession);

   int32 __stdcall RFmxInstr_GetNIRFSASessionArray(
       niRFmxInstrHandle instrumentHandle,
       uInt32 NIRFSASessions[],
       int32 arraySize,
       int32* actualArraySize
       );

   int32 __stdcall RFmxInstr_CheckIfSignalConfigurationExists(
      niRFmxInstrHandle instrumentHandle,
      char signalName[],
      int32* signalConfigurationExists,
      int32* personality
   );

   int32 __stdcall RFmxInstr_CheckIfListExists(
      niRFmxInstrHandle instrumentHandle,
      char listName[],
      int32* listExists,
      int32* personality
   );

   int32 __stdcall RFmxInstr_SaveAllConfigurations(
      niRFmxInstrHandle instrumentHandle,
      char filePath[]);

   int32 __stdcall RFmxInstr_LoadConfigurations(
      niRFmxInstrHandle instrumentHandle,
      char filePath[]);

   int32 __stdcall RFmxInstr_ResetEntireSession(
      niRFmxInstrHandle instrumentHandle);

   int32 __stdcall RFmxInstr_ResetAttribute(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID);

   int32 __stdcall RFmxInstr_GetSignalConfigurationNames(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 personalityFilter,
      char signalNames[],
      int32 signalNamesSize,
      int32* actualSignalNamesSize,
      int32 personality[],
      int32 personalityArraySize,
      int32* actualPersonalityArraySize
   );

   int32 __stdcall RFmxInstr_GetListNames(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       int32 personalityFilter,
       char listNames[],
       int32 listNamesSize,
       int32* actualListNamesSize,
       int32 personality[],
       int32 personalityArraySize,
       int32* actualPersonalityArraySize
   );


   int32 __stdcall RFmxInstr_GetAvailablePorts(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char availablePorts[]
   );

   int32 __stdcall RFmxInstr_ExportSignal(
      niRFmxInstrHandle instrumentHandle,
      int32 exportSignalSource,
      char exportSignalOutputTerminal[]);

   int32 __stdcall RFmxInstr_LoadSParameterExternalAttenuationTableFromS2PFile(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[],
      char S2PFilePath[],
      int32 sParameterOrientation
   );

   int32 __stdcall RFmxInstr_SelectActiveExternalAttenuationTable(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char tableName[]
   );

   int32 __stdcall RFmxInstr_GetExternalAttenuationTableActualValue(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64* externalAttenuation
   );

   int32 __stdcall RFmxInstr_SelfCalibrate(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 stepsToOmit
   );

   int32 __stdcall RFmxInstr_SelfCalibrateRange(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 stepsToOmit,
      float64 minimumFrequency,
      float64 maximumFrequency,
      float64 minimumReferenceLevel,
      float64 maximumReferenceLevel
   );

   int32 __stdcall RFmxInstr_IsSelfCalibrateValid(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32* selfCalibrateValid,
      int32* validSteps
   );

   int32 __stdcall RFmxInstr_GetSelfCalibrateLastDateAndTime(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int64 selfCalibrateStep,
      CVIAbsoluteTime* timestamp
   );

   int32 __stdcall RFmxInstr_GetSelfCalibrateLastTemperature(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int64 selfCalibrateStep,
      float64* temperature
   );

   int32 __stdcall RFmxInstr_ValuesFromTimestamp(
      CVIAbsoluteTime timestamp,
      int64* secondsSince1970,
      float64* fractionalSeconds);

   int32 __stdcall RFmxInstr_TimestampFromValues(
      int64 secondsSince1970,
      float64 fractionalSeconds,
      CVIAbsoluteTime* timestamp);

   int32 __stdcall RFmxInstr_SendSoftwareEdgeStartTrigger(
      niRFmxInstrHandle instrumentHandle
   );

   int32 __stdcall RFmxInstr_SendSoftwareEdgeAdvanceTrigger(
      niRFmxInstrHandle instrumentHandle
   );

   int32 __stdcall RFmxInstr_RegisterExternalRFSubsystemCallbacks(
      niRFmxInstrHandle instrumentHandle,
      void *externalRFSubsystemContext,
      void *callbacks[],
      int32 arraySize,
      int32 callbackVersion);

   int32 __stdcall RFmxInstr_UnregisterExternalRFSubsystemCallbacks(niRFmxInstrHandle instrumentHandle);

   int32 __stdcall RFmxInstr_GetAvailablePaths(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char availablePaths[]
   );

// Fetch methods 

int32 __stdcall RFmxInstr_FetchRawIQData(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       float64 timeout,
       int32 recordsToFetch,
       int64 samplesToRead,
       float64* x0,
       float64* dx,
       NIComplexSingle data[],
       int32 arraySize,
       int32* actualArraySize,
       void* reserved);

   int32 __stdcall RFmxInstr_FetchRawIQDataSplit(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       float64 timeout,
       int32 recordsToFetch,
       int64 samplesToRead,
       float64* x0,
       float64* dx,
       float32 I[],
       float32 Q[],
       int32 arraySize,
       int32* actualArraySize,
       void* reserved);


   // Build string methods
   int32 __stdcall RFmxInstr_BuildPortString2(
      char selectorString[],
      char portName[],
      char deviceName[],
      int32 channelNumber,
      int32 selectorStringOutLength,
      char selectorStringOut[]
   );

   int32 __stdcall RFmxInstr_BuildCalibrationPlaneString(
      char calibrationPlaneName[],
      int32 selectorStringLength,
      char selectorString[]
   );

   int32 __stdcall RFmxInstr_BuildLOString(
      char selectorString[],
      int32 LOIndex,
      int32 selectorStringOutLength,
      char selectorStringOut[]
   );

   int32 __stdcall RFmxInstr_BuildModuleString(
      char selectorString[],
      char moduleName[],
      int32 selectorStringOutLength,
      char selectorStringOut[]
   );

   int32 __stdcall RFmxInstr_BuildInstrumentString(
      char selectorString[],
      int32 instrumentNumber,
      int32 selectorStringOutLength,
      char selectorStringOut[]
   );

   // Generic Get/Set Methods
   int32 __stdcall RFmxInstr_SetAttributeString(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      char attrVal[]
   );
   int32 __stdcall RFmxInstr_GetAttributeString(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetAttributeI8(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int8 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeI8(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int8 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeU8(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt8 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeU8(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt8 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeI16(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int16 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeI16(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int16 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeU16(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt16 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeU16(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt16 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeI32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int32 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeI32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeU32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt32 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeU32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeI64(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int64 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeI64(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeF64(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float64 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeF64(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeF32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float32 attrVal
   );
   int32 __stdcall RFmxInstr_GetAttributeF32(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAttributeI8Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int8 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeI8Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int8 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeI32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int32 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeI32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int32 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeI64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int64 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeI64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      int64 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeU64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt64 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeU64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt64 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeU8Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt8 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeU8Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt8 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeU32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt32 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeU32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      uInt32 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeF32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float32 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeF32Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float32 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeF64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float64 attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeF64Array(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      float64 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeNIComplexSingleArray(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      NIComplexSingle attrVal[],
      int32 arraySize
   );
   int32 __stdcall RFmxInstr_GetAttributeNIComplexSingleArray(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      NIComplexSingle attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetAttributeNIComplexDoubleArray(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      NIComplexDouble attrVal[],
      int32 arraySize
   );

   int32 __stdcall RFmxInstr_GetAttributeNIComplexDoubleArray(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attributeID,
      NIComplexDouble attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   // Get/Set attribute methods
   int32 __stdcall RFmxInstr_SetFrequencyReferenceSource(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetFrequencyReferenceSource(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_SetFrequencyReferenceFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetFrequencyReferenceFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetRFAttenuationAuto(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetRFAttenuationAuto(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetRFAttenuationValue(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetRFAttenuationValue(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetMechanicalAttenuationAuto(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetMechanicalAttenuationAuto(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetMechanicalAttenuationValue(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetMechanicalAttenuationValue(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetTuningSpeed(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetTuningSpeed(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetFrequencySettlingUnits(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetFrequencySettlingUnits(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetFrequencySettling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetFrequencySettling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetChannelCoupling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetChannelCoupling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetDownconverterPreselectorEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetDownconverterPreselectorEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetDownconverterCenterFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetDownconverterCenterFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetLOSource(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetLOSource(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_SetLOFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetLOFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetPreampEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetPreampEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetMixerLevelOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetMixerLevelOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetMixerLevel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetMixerLevel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetIFOutputPowerLevelOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetIFOutputPowerLevelOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetLOInjectionSide(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetLOInjectionSide(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetPhaseOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetPhaseOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetDigitizerDitherEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetDigitizerDitherEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetFFTWidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetFFTWidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetOSPDelayEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetOSPDelayEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetDeviceTemperature(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetDigitizerTemperature(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetLOTemperature(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetInstrumentFirmwareRevision(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetInstrumentModel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetModuleRevision(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetSerialNumber(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetPreselectorPresent(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetRFPreampPresent(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetLOExportEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetLOExportEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetLO2ExportEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetLO2ExportEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetFrequencyReferenceExportedTerminal(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetFrequencyReferenceExportedTerminal(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_SetTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_GetTriggerTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]);

   int32 __stdcall RFmxInstr_SetCleanerSpectrum(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetCleanerSpectrum(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedAcquisitionType(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedNumberOfRecords(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedTriggerMinimumQuietTime(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedIQAcquisitionTime(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedIQMinimumSampleRate(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedIQPreTriggerTime(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedSpectralAcquisitionSpan(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedSpectralFFTWindow(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedSpectralResolutionBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetRecommendedCenterFrequency(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetIFFilterBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetIFFilterBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetSubSpanOverlap(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetSubSpanOverlap(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_GetDownconverterGain(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetDownconverterFrequencyOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetDownconverterFrequencyOffset(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetRFAttenuationStepSize(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetRFAttenuationStepSize(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAmplitudeSettling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetAmplitudeSettling(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetLOLeakageAvoidanceEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetLOLeakageAvoidanceEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetCommonModeLevel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetCommonModeLevel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetSMUResourceName(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetSMUResourceName(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetSMUChannel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetSMUChannel(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetSelfCalibrationValidityCheck(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetSelfCalibrationValidityCheck(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetSelfCalibrationValidityCheckTimeInterval(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetSelfCalibrationValidityCheckTimeInterval(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_SetOverflowErrorReporting(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetOverflowErrorReporting(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetLOInPower(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetLOInPower(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetLOOutPower(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 attrVal);

   int32 __stdcall RFmxInstr_GetLOOutPower(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal);

   int32 __stdcall RFmxInstr_SetLOPLLFractionalMode(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetLOPLLFractionalMode(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetOptimizePathForSignalBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetOptimizePathForSignalBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_SetInputIsolationEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 attrVal);

   int32 __stdcall RFmxInstr_GetInputIsolationEnabled(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      int32 *attrVal);

   int32 __stdcall RFmxInstr_GetLOVCOFrequencyStepSize(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetLOVCOFrequencyStepSize(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetThermalCorrectionHeadroomRange(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetThermalCorrectionHeadroomRange(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetLOFrequencyStepSize(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetLOFrequencyStepSize(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );
   int32 __stdcall RFmxInstr_GetRFHighpassFilterFrequency(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetRFHighpassFilterFrequency(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetStartTriggerType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetStartTriggerType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetStartTriggerDigitalEdgeSource(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetStartTriggerDigitalEdgeSource(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetStartTriggerDigitalEdge(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetStartTriggerDigitalEdge(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetStartTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetStartTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetStartTriggerTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetAdvanceTriggerType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetAdvanceTriggerType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetAdvanceTriggerDigitalEdgeSource(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetAdvanceTriggerDigitalEdgeSource(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetAdvanceTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetAdvanceTriggerExportOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetAdvanceTriggerTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForStartEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetReadyForStartEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForStartEventTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForAdvanceEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetReadyForAdvanceEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForAdvanceEventTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForReferenceEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetReadyForReferenceEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetReadyForReferenceEventTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetEndOfRecordEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetEndOfRecordEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetEndOfRecordEventTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetDoneEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetDoneEventOutputTerminal(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetDoneEventTerminalName(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_GetTemperatureReadInterval(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetTemperatureReadInterval(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetThermalCorrectionTemperatureResolution(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetThermalCorrectionTemperatureResolution(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetNumberOfRawIQRecords(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       int32* attrVal
   );
   int32 __stdcall RFmxInstr_GetSParameterExternalAttenuationType(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32* sParameterType
   );

   int32 __stdcall RFmxInstr_GetLOSharingMode(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetLOSharingMode(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetNumberOfLOSharingGroups(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 *attrVal
   );

   int32 __stdcall RFmxInstr_SetNumberOfLOSharingGroups(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 attrVal
   );

   int32 __stdcall RFmxInstr_GetLoadOptions(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       int32 attrVal[],
       int32 arraySize,
       int32* actualArraySize
   );

   int32 __stdcall RFmxInstr_SetLoadOptions(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       int32 attrVal[],
       int32 arraySize
   );

   int32 __stdcall RFmxInstr_GetDigitalGain(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_SetDigitalGain(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal
   );

   int32 __stdcall RFmxInstr_GetLOSplitterLossFrequency(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetLOSplitterLossFrequency(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal[],
      int32 arraySize
   );

   int32 __stdcall RFmxInstr_GetLOSplitterLoss(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal[],
      int32 arraySize,
      int32 *actualArraySize
   );

   int32 __stdcall RFmxInstr_SetLOSplitterLoss(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      float64 attrVal[],
      int32 arraySize
   );

   int32 __stdcall RFmxInstr_GetFixedGroupDelayAcrossPorts(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      int32 arraySize,
      char attrVal[]
   );

   int32 __stdcall RFmxInstr_SetFixedGroupDelayAcrossPorts(
      niRFmxInstrHandle instrumentHandle,
      char selectorString[],
      char attrVal[]
   );

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXINSTR_ATTR_RECOMMENDED_IQ_MEASUREMENT_BANDWIDTH                0x00000033
#define RFMXINSTR_ATTR_AUTOMATIC_SG_SA_SHARED_LO                           0x0000004a

/* -- Values for Automatic SG SA Shared LO -- */

#define RFMXINSTR_VAL_AUTOMATIC_SG_SA_SHARED_LO_DISABLED                   0
#define RFMXINSTR_VAL_AUTOMATIC_SG_SA_SHARED_LO_ENABLED                    1

/* -- Values for LO Sharing Mode -- */

#define RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_STAR   					         1
#define RFMXINSTR_VAL_LO_SHARING_MODE_ONBOARD_DAISY_CHAIN				      2

#ifdef __cplusplus
extern "C"
{
#endif

   int32 __stdcall RFmxInstr_GetRecommendedIQMeasurementBandwidth(
      niRFmxInstrHandle instrumentHandle,
      char channelName[],
      float64 *attrVal
   );

   int32 __stdcall RFmxInstr_BuildPortString(
      char selectorString[],
      char portName[],
      int32 selectorStringOutLength,
      char selectorStringOut[]
   );

   int32 __stdcall RFmxInstr_CfgAutomaticSGSASharedLO(
       niRFmxInstrHandle instrumentHandle,
       char selectorString[],
       int32 automaticSGSASharedLO
   );

   int32 __stdcall RFmxInstr_GetAutomaticSGSASharedLO(
       niRFmxInstrHandle instrumentHandle,
       char channelName[],
       int32* attrVal
   );

   int32 __stdcall RFmxInstr_SetAutomaticSGSASharedLO(
       niRFmxInstrHandle instrumentHandle,
       char channelName[],
       int32 attrVal
   );

   int32 __stdcall RFmxInstr_LoadAllConfigurations(
      niRFmxInstrHandle instrumentHandle,
      char filePath[],
      int32 loadRFInstrConfiguration
   );
  
#ifdef __cplusplus
}
#endif

#endif   /*__NI_RFMX_INSTR_H__*/
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxLTE.h sha256=66845897e1643c2f9918b8f44a052fe8dc89a5561bb6da805cb7d1ce5769704a bytes=265556 -->
## FILE: imports/include/niRFmxLTE.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxLTE.h`
- sha256: `66845897e1643c2f9918b8f44a052fe8dc89a5561bb6da805cb7d1ce5769704a`
- bytes: 265556

````c

/****************************************************************************************************
*          National Instruments RFmx LTE
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2024.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxLTE.h
*
* Purpose:  National Instruments RFmx LTE,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_LTE_H__
#define __NI_RFMX_LTE_H__

#include "niRFmxInstr.h"

#define RFMXLTE_ATTR_SELECTED_PORTS                                                         0x00300ffd
#define RFMXLTE_ATTR_CENTER_FREQUENCY                                                       0x00300001
#define RFMXLTE_ATTR_REFERENCE_LEVEL                                                        0x00300002
#define RFMXLTE_ATTR_EXTERNAL_ATTENUATION                                                   0x00300003
#define RFMXLTE_ATTR_REFERENCE_LEVEL_HEADROOM                                               0x00300ffc
#define RFMXLTE_ATTR_TRIGGER_TYPE                                                           0x00300004
#define RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                            0x00300005
#define RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                              0x00300006
#define RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                           0x00300007
#define RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                            0x00300008
#define RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                                       0x00300fff
#define RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                            0x00300009
#define RFMXLTE_ATTR_TRIGGER_DELAY                                                          0x0030000a
#define RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                        0x0030000b
#define RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                                    0x0030000c
#define RFMXLTE_ATTR_LINK_DIRECTION                                                         0x00300029
#define RFMXLTE_ATTR_DUPLEX_SCHEME                                                          0x0030000d
#define RFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATION                                          0x0030000e
#define RFMXLTE_ATTR_ENODEB_CATEGORY                                                        0x00300050
#define RFMXLTE_ATTR_SPECIAL_SUBFRAME_CONFIGURATION                                         0x0030002a
#define RFMXLTE_ATTR_NUMBER_OF_DUT_ANTENNAS                                                 0x0030002b
#define RFMXLTE_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE                                            0x0030002c
#define RFMXLTE_ATTR_NUMBER_OF_SUBBLOCKS                                                    0x00300023
#define RFMXLTE_ATTR_SUBBLOCK_FREQUENCY                                                     0x00300059
#define RFMXLTE_ATTR_BAND                                                                   0x00300017
#define RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE                                         0x00300013
#define RFMXLTE_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY                                  0x00300014
#define RFMXLTE_ATTR_NUMBER_OF_COMPONENT_CARRIERS                                           0x0030000f
#define RFMXLTE_ATTR_COMPONENT_CARRIER_BANDWIDTH                                            0x00300010
#define RFMXLTE_ATTR_COMPONENT_CARRIER_FREQUENCY                                            0x00300011
#define RFMXLTE_ATTR_CELL_ID                                                                0x00300012
#define RFMXLTE_ATTR_CYCLIC_PREFIX_MODE                                                     0x00300015
#define RFMXLTE_ATTR_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED                                0x0030003c
#define RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE                                    0x0030003d
#define RFMXLTE_ATTR_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED                                   0x00304054
#define RFMXLTE_ATTR_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED                           0x00304055
#define RFMXLTE_ATTR_AUTO_PCFICH_CFI_DETECTION_ENABLED                                      0x00304056
#define RFMXLTE_ATTR_MI_CONFIGURATION                                                       0x00300053
#define RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO                              0x0030003e
#define RFMXLTE_ATTR_PSS_POWER                                                              0x0030003f
#define RFMXLTE_ATTR_SSS_POWER                                                              0x00300040
#define RFMXLTE_ATTR_PBCH_POWER                                                             0x00300041
#define RFMXLTE_ATTR_PDCCH_POWER                                                            0x00300042
#define RFMXLTE_ATTR_DOWNLINK_NUMBER_OF_SUBFRAMES                                           0x00300043
#define RFMXLTE_ATTR_PCFICH_CFI                                                             0x00300044
#define RFMXLTE_ATTR_PCFICH_POWER                                                           0x00300045
#define RFMXLTE_ATTR_PHICH_RESOURCE                                                         0x00300046
#define RFMXLTE_ATTR_PHICH_DURATION                                                         0x00300047
#define RFMXLTE_ATTR_PHICH_POWER                                                            0x00300048
#define RFMXLTE_ATTR_NUMBER_OF_PDSCH_CHANNELS                                               0x00300049
#define RFMXLTE_ATTR_PDSCH_CW0_MODULATION_TYPE                                              0x0030004a
#define RFMXLTE_ATTR_PDSCH_RESOURCE_BLOCK_ALLOCATION                                        0x0030004b
#define RFMXLTE_ATTR_PDSCH_POWER                                                            0x0030004c
#define RFMXLTE_ATTR_DOWNLINK_TEST_MODEL                                                    0x0030004d
#define RFMXLTE_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED                                  0x00300026
#define RFMXLTE_ATTR_AUTO_DMRS_DETECTION_ENABLED                                            0x00300028
#define RFMXLTE_ATTR_UPLINK_GROUP_HOPPING_ENABLED                                           0x00300019
#define RFMXLTE_ATTR_UPLINK_SEQUENCE_HOPPING_ENABLED                                        0x0030001a
#define RFMXLTE_ATTR_DMRS_OCC_ENABLED                                                       0x00300051
#define RFMXLTE_ATTR_PUSCH_N_DMRS_1                                                         0x0030001f
#define RFMXLTE_ATTR_PUSCH_DELTA_SEQUENCE_SHIFT                                             0x00300021
#define RFMXLTE_ATTR_PUSCH_MODULATION_TYPE                                                  0x0030001b
#define RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS                                0x0030001c
#define RFMXLTE_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET                                            0x0030001e
#define RFMXLTE_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS                                        0x00300022
#define RFMXLTE_ATTR_PUSCH_N_DMRS_2                                                         0x00300020
#define RFMXLTE_ATTR_PUSCH_CYCLIC_SHIFT_FIELD                                               0x00300052
#define RFMXLTE_ATTR_PUSCH_POWER                                                            0x00300027
#define RFMXLTE_ATTR_SRS_ENABLED                                                            0x0030002d
#define RFMXLTE_ATTR_SRS_SUBFRAME_CONFIGURATION                                             0x0030002e
#define RFMXLTE_ATTR_SRS_C_SRS                                                              0x0030002f
#define RFMXLTE_ATTR_SRS_B_SRS                                                              0x00300030
#define RFMXLTE_ATTR_SRS_I_SRS                                                              0x00300031
#define RFMXLTE_ATTR_SRS_n_RRC                                                              0x00300032
#define RFMXLTE_ATTR_SRS_n_SRS_CS                                                           0x00300033
#define RFMXLTE_ATTR_SRS_b_HOP                                                              0x00300034
#define RFMXLTE_ATTR_SRS_k_TC                                                               0x00300035
#define RFMXLTE_ATTR_SRS_MAXIMUM_UpPTS_ENABLED                                              0x00300036
#define RFMXLTE_ATTR_SRS_SUBFRAME1_N_RA                                                     0x00300037
#define RFMXLTE_ATTR_SRS_SUBFRAME6_N_RA                                                     0x00300038
#define RFMXLTE_ATTR_SRS_POWER                                                              0x00300039
#define RFMXLTE_ATTR_PSSCH_MODULATION_TYPE                                                  0x00300055
#define RFMXLTE_ATTR_PSSCH_RESOURCE_BLOCK_OFFSET                                            0x00300056
#define RFMXLTE_ATTR_PSSCH_NUMBER_OF_RESOURCE_BLOCKS                                        0x00300057
#define RFMXLTE_ATTR_PSSCH_POWER                                                            0x00300058
#define RFMXLTE_ATTR_LAA_STARTING_SUBFRAME                                                  0x00304057
#define RFMXLTE_ATTR_LAA_NUMBER_OF_SUBFRAMES                                                0x00304058
#define RFMXLTE_ATTR_LAA_UPLINK_START_POSITION                                              0x00304059
#define RFMXLTE_ATTR_LAA_UPLINK_ENDING_SYMBOL                                               0x0030405a
#define RFMXLTE_ATTR_LAA_DOWNLINK_STARTING_SYMBOL                                           0x0030405b
#define RFMXLTE_ATTR_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS                                  0x0030405c
#define RFMXLTE_ATTR_NCELL_ID                                                               0x0030405e
#define RFMXLTE_ATTR_NB_IOT_UPLINK_SUBCARRIER_SPACING                                       0x0030405f
#define RFMXLTE_ATTR_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED                                  0x00304060
#define RFMXLTE_ATTR_NPUSCH_FORMAT                                                          0x00304061
#define RFMXLTE_ATTR_NPUSCH_STARTING_SLOT                                                   0x00304072
#define RFMXLTE_ATTR_NPUSCH_TONE_OFFSET                                                     0x00304062
#define RFMXLTE_ATTR_NPUSCH_NUMBER_OF_TONES                                                 0x00304063
#define RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE                                                 0x00304064
#define RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_MODE                                         0x00304065
#define RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_INDEX                                        0x00304066
#define RFMXLTE_ATTR_NPUSCH_DMRS_CYCLIC_SHIFT                                               0x00304067
#define RFMXLTE_ATTR_NPUSCH_DMRS_GROUP_HOPPING_ENABLED                                      0x00304069
#define RFMXLTE_ATTR_NPUSCH_DMRS_DELTA_SEQUENCE_SHIFT                                       0x00304068
#define RFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE                             0x00304084
#define RFMXLTE_ATTR_NPSS_POWER                                                             0x00304087
#define RFMXLTE_ATTR_NSSS_POWER                                                             0x00304089
#define RFMXLTE_ATTR_NPDSCH_POWER                                                           0x0030408a
#define RFMXLTE_ATTR_NPDSCH_ENABLED                                                         0x0030408b
#define RFMXLTE_ATTR_NPDSCH_MODULATION_TYPE                                                 0x0030408c
#define RFMXLTE_ATTR_EMTC_ANALYSIS_ENABLED                                                  0x00304070
#define RFMXLTE_ATTR_NUMBER_OF_STEPS                                                        0x00300ff8
#define RFMXLTE_ATTR_LIST_STEP_TIMER_UNIT                                                   0x00300ff6
#define RFMXLTE_ATTR_LIST_STEP_TIMER_DURATION                                               0x00300ff9
#define RFMXLTE_ATTR_LIST_STEP_TIMER_OFFSET                                                 0x00300ff7
#define RFMXLTE_ATTR_MODACC_MEASUREMENT_ENABLED                                             0x00304000
#define RFMXLTE_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED                                     0x00304002
#define RFMXLTE_ATTR_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE                          0x0030407e
#define RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE                                            0x00304003
#define RFMXLTE_ATTR_MODACC_MEASUREMENT_OFFSET                                              0x00304004
#define RFMXLTE_ATTR_MODACC_MEASUREMENT_LENGTH                                              0x00304005
#define RFMXLTE_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION                                      0x0030e00c
#define RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED                             0x00304079
#define RFMXLTE_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED                                  0x0030407a
#define RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED                            0x0030407b
#define RFMXLTE_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED                          0x0030407c
#define RFMXLTE_ATTR_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED                               0x0030407d
#define RFMXLTE_ATTR_MODACC_SPECTRUM_INVERTED                                               0x00304036
#define RFMXLTE_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE                                         0x00304037
#define RFMXLTE_ATTR_MODACC_EVM_UNIT                                                        0x00304006
#define RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE                                                 0x00304038
#define RFMXLTE_ATTR_MODACC_FFT_WINDOW_OFFSET                                               0x00304007
#define RFMXLTE_ATTR_MODACC_FFT_WINDOW_LENGTH                                               0x00304039
#define RFMXLTE_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED                                     0x00304009
#define RFMXLTE_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED                               0x00304032
#define RFMXLTE_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION                                     0x00304008
#define RFMXLTE_ATTR_MODACC_IN_BAND_EMISSION_MASK_TYPE                                      0x00304071
#define RFMXLTE_ATTR_MODACC_AVERAGING_ENABLED                                               0x0030400a
#define RFMXLTE_ATTR_MODACC_AVERAGING_COUNT                                                 0x0030400b
#define RFMXLTE_ATTR_MODACC_ALL_TRACES_ENABLED                                              0x0030400d
#define RFMXLTE_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS                                      0x0030400e
#define RFMXLTE_ATTR_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL                               0x0030407f
#define RFMXLTE_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED                           0x00304080
#define RFMXLTE_ATTR_MODACC_TIMING_TRACKING_ENABLED                                         0x00304081
#define RFMXLTE_ATTR_MODACC_PHASE_TRACKING_ENABLED                                          0x00304082
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_EVM                                  0x0030400f
#define RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM                              0x00304010
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_MAGNITUDE_ERROR                      0x0030403a
#define RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR                  0x0030403b
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_COMPOSITE_PHASE_ERROR                          0x0030403c
#define RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR                      0x0030403d
#define RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX                           0x00304013
#define RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SYMBOL_INDEX                         0x00304014
#define RFMXLTE_ATTR_MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX                     0x00304015
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_EVM                                      0x00304044
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_QPSK_EVM                                 0x00304045
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_16QAM_EVM                                0x00304046
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_64QAM_EVM                                0x00304047
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_256QAM_EVM                               0x00304048
#define RFMXLTE_ATTR_MODACC_RESULTS_PDSCH_MEAN_RMS_1024QAM_EVM                              0x0030405d
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_CSRS_EVM                                       0x00304049
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PSS_EVM                                        0x0030404a
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SSS_EVM                                        0x0030404b
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PBCH_EVM                                       0x0030404c
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PCFICH_EVM                                     0x0030404d
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PDCCH_EVM                                      0x0030404e
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_PHICH_EVM                                      0x0030404f
#define RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER                              0x00304051
#define RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER                     0x00304052
#define RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID                               0x00304053
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NPSS_EVM                                       0x0030408e
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NSSS_EVM                                       0x0030408f
#define RFMXLTE_ATTR_MODACC_RESULTS_NPDSCH_MEAN_RMS_EVM                                     0x00304090
#define RFMXLTE_ATTR_MODACC_RESULTS_NPDSCH_MEAN_RMS_QPSK_EVM                                0x00304091
#define RFMXLTE_ATTR_MODACC_RESULTS_NPDSCH_MEAN_RMS_16QAM_EVM                               0x00304092
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_NRS_EVM                                        0x00304093
#define RFMXLTE_ATTR_MODACC_RESULTS_DOWNLINK_NRS_TRANSMIT_POWER                             0x00304094
#define RFMXLTE_ATTR_MODACC_RESULTS_IN_BAND_EMISSION_MARGIN                                 0x0030402b
#define RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM      0x0030402c
#define RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM      0x0030402d
#define RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM      0x0030402e
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MEAN_RMS_DATA_EVM                                 0x00304016
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MAXIMUM_PEAK_DATA_EVM                             0x00304017
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MEAN_RMS_DMRS_EVM                                 0x00304018
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MAXIMUM_PEAK_DMRS_EVM                             0x00304019
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MEAN_DATA_POWER                                   0x0030401a
#define RFMXLTE_ATTR_MODACC_RESULTS_PUSCH_MEAN_DMRS_POWER                                   0x0030401b
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_RMS_SRS_EVM                                        0x00304042
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SRS_POWER                                          0x00304043
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_RMS_DATA_EVM                                0x0030406a
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DATA_EVM                            0x0030406b
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_RMS_DMRS_EVM                                0x0030406c
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DMRS_EVM                            0x0030406d
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_DATA_POWER                                  0x0030406e
#define RFMXLTE_ATTR_MODACC_RESULTS_NPUSCH_MEAN_DMRS_POWER                                  0x0030406f
#define RFMXLTE_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM      0x0030402f
#define RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN                        0x0030403e
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MEAN_RMS_DATA_EVM                                 0x00304073
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MAXIMUM_PEAK_DATA_EVM                             0x00304074
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MEAN_RMS_DMRS_EVM                                 0x00304075
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MAXIMUM_PEAK_DMRS_EVM                             0x00304076
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MEAN_DATA_POWER                                   0x00304077
#define RFMXLTE_ATTR_MODACC_RESULTS_PSSCH_MEAN_DMRS_POWER                                   0x00304078
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_FREQUENCY_ERROR                                    0x00304022
#define RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR                            0x00304083
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET                                   0x00304023
#define RFMXLTE_ATTR_MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET                           0x00304030
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE                                  0x00304024
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_QUADRATURE_ERROR                                   0x00304025
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_IQ_TIMING_SKEW                                     0x00304026
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_TIME_OFFSET                                        0x00304027
#define RFMXLTE_ATTR_MODACC_RESULTS_MEAN_SYMBOL_CLOCK_ERROR                                 0x00304028
#define RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_IQ_ORIGIN_OFFSET                          0x0030403f
#define RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_IQ_GAIN_IMBALANCE                         0x00304040
#define RFMXLTE_ATTR_MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR                          0x00304041
#define RFMXLTE_ATTR_ACP_MEASUREMENT_ENABLED                                                0x00301000
#define RFMXLTE_ATTR_ACP_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x0030103f
#define RFMXLTE_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00301005
#define RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED                             0x00301044
#define RFMXLTE_ATTR_ACP_NUMBER_OF_UTRA_OFFSETS                                             0x0030103a
#define RFMXLTE_ATTR_ACP_NUMBER_OF_EUTRA_OFFSETS                                            0x0030103b
#define RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION                                            0x00301043
#define RFMXLTE_ATTR_ACP_NUMBER_OF_GSM_OFFSETS                                              0x00301042
#define RFMXLTE_ATTR_ACP_NUMBER_OF_STANDALONE_NB_IOT_OFFSETS                                0x00301050
#define RFMXLTE_ATTR_ACP_OFFSET_FREQUENCY                                                   0x0030100a
#define RFMXLTE_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH                                       0x0030100e
#define RFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH                                          0x0030101b
#define RFMXLTE_ATTR_ACP_RBW_FILTER_BANDWIDTH                                               0x0030101c
#define RFMXLTE_ATTR_ACP_RBW_FILTER_TYPE                                                    0x0030101d
#define RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO                                                    0x0030101e
#define RFMXLTE_ATTR_ACP_SWEEP_TIME_INTERVAL                                                0x0030101f
#define RFMXLTE_ATTR_ACP_POWER_UNITS                                                        0x00301013
#define RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD                                                 0x00301012
#define RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODE                                             0x0030104b
#define RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO                                   0x0030104a
#define RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT                                  0x00301049
#define RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_ENABLED                                         0x00301020
#define RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_TYPE                                            0x00301048
#define RFMXLTE_ATTR_ACP_AVERAGING_ENABLED                                                  0x00301016
#define RFMXLTE_ATTR_ACP_AVERAGING_COUNT                                                    0x00301015
#define RFMXLTE_ATTR_ACP_AVERAGING_TYPE                                                     0x00301018
#define RFMXLTE_ATTR_ACP_MEASUREMENT_MODE                                                   0x00301047
#define RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE                                                   0x00301045
#define RFMXLTE_ATTR_ACP_FFT_OVERLAP                                                        0x00301046
#define RFMXLTE_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO                                        0x00301034
#define RFMXLTE_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET                                        0x00301035
#define RFMXLTE_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET                                         0x00301036
#define RFMXLTE_ATTR_ACP_SEQUENTIAL_FFT_SIZE                                                0x00301041
#define RFMXLTE_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE                                          0x00301040
#define RFMXLTE_ATTR_ACP_ALL_TRACES_ENABLED                                                 0x00301021
#define RFMXLTE_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                                         0x00301014
#define RFMXLTE_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER                                     0x00301022
#define RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY                                  0x00301039
#define RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH                             0x00301037
#define RFMXLTE_ATTR_ACP_RESULTS_SUBBLOCK_POWER                                             0x00301038
#define RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER                           0x00301026
#define RFMXLTE_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER                           0x00301027
#define RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                                0x0030102c
#define RFMXLTE_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                                0x0030102d
#define RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                                0x00301032
#define RFMXLTE_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                                0x00301033
#define RFMXLTE_ATTR_CHP_MEASUREMENT_ENABLED                                                0x00303000
#define RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE                                         0x00303018
#define RFMXLTE_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x00303022
#define RFMXLTE_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00303002
#define RFMXLTE_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH                                          0x0030300c
#define RFMXLTE_ATTR_CHP_RBW_FILTER_BANDWIDTH                                               0x0030300d
#define RFMXLTE_ATTR_CHP_RBW_FILTER_TYPE                                                    0x0030300e
#define RFMXLTE_ATTR_CHP_SWEEP_TIME_AUTO                                                    0x00303011
#define RFMXLTE_ATTR_CHP_SWEEP_TIME_INTERVAL                                                0x00303012
#define RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODE                                             0x00303029
#define RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO                                   0x00303028
#define RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT                                  0x00303027
#define RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_ENABLED                                         0x00303025
#define RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_TYPE                                            0x00303026
#define RFMXLTE_ATTR_CHP_AVERAGING_ENABLED                                                  0x00303007
#define RFMXLTE_ATTR_CHP_AVERAGING_COUNT                                                    0x00303006
#define RFMXLTE_ATTR_CHP_AVERAGING_TYPE                                                     0x00303009
#define RFMXLTE_ATTR_CHP_MEASUREMENT_MODE                                                   0x00303024
#define RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE                                          0x00303023
#define RFMXLTE_ATTR_CHP_ALL_TRACES_ENABLED                                                 0x00303014
#define RFMXLTE_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS                                         0x00303003
#define RFMXLTE_ATTR_CHP_RESULTS_TOTAL_AGGREGATED_POWER                                     0x00303019
#define RFMXLTE_ATTR_CHP_RESULTS_SUBBLOCK_FREQUENCY                                         0x0030301b
#define RFMXLTE_ATTR_CHP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH                             0x0030301c
#define RFMXLTE_ATTR_CHP_RESULTS_SUBBLOCK_POWER                                             0x0030301d
#define RFMXLTE_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER                           0x00303015
#define RFMXLTE_ATTR_CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER                           0x00303020
#define RFMXLTE_ATTR_OBW_MEASUREMENT_ENABLED                                                0x00306000
#define RFMXLTE_ATTR_OBW_SPAN                                                               0x00306004
#define RFMXLTE_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH                                          0x0030600c
#define RFMXLTE_ATTR_OBW_RBW_FILTER_BANDWIDTH                                               0x0030600d
#define RFMXLTE_ATTR_OBW_RBW_FILTER_TYPE                                                    0x0030600e
#define RFMXLTE_ATTR_OBW_SWEEP_TIME_AUTO                                                    0x0030600f
#define RFMXLTE_ATTR_OBW_SWEEP_TIME_INTERVAL                                                0x00306010
#define RFMXLTE_ATTR_OBW_AVERAGING_ENABLED                                                  0x00306007
#define RFMXLTE_ATTR_OBW_AVERAGING_COUNT                                                    0x00306006
#define RFMXLTE_ATTR_OBW_AVERAGING_TYPE                                                     0x00306009
#define RFMXLTE_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE                                          0x0030601b
#define RFMXLTE_ATTR_OBW_ALL_TRACES_ENABLED                                                 0x00306012
#define RFMXLTE_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS                                         0x00306003
#define RFMXLTE_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH                                         0x00306013
#define RFMXLTE_ATTR_OBW_RESULTS_ABSOLUTE_POWER                                             0x00306014
#define RFMXLTE_ATTR_OBW_RESULTS_START_FREQUENCY                                            0x00306015
#define RFMXLTE_ATTR_OBW_RESULTS_STOP_FREQUENCY                                             0x00306016
#define RFMXLTE_ATTR_SEM_MEASUREMENT_ENABLED                                                0x00308000
#define RFMXLTE_ATTR_SEM_UPLINK_MASK_TYPE                                                   0x0030804c
#define RFMXLTE_ATTR_SEM_DOWNLINK_MASK_TYPE                                                 0x00308053
#define RFMXLTE_ATTR_SEM_SIDELINK_MASK_TYPE                                                 0x00308058
#define RFMXLTE_ATTR_SEM_DELTA_F_MAXIMUM                                                    0x00308054
#define RFMXLTE_ATTR_SEM_AGGREGATED_MAXIMUM_POWER                                           0x00308055
#define RFMXLTE_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x00308051
#define RFMXLTE_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH                              0x00308052
#define RFMXLTE_ATTR_SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00308005
#define RFMXLTE_ATTR_SEM_COMPONENT_CARRIER_OUTPUT_POWER_TYPE                                0x00308059
#define RFMXLTE_ATTR_SEM_COMPONENT_CARRIER_MAXIMUM_OUTPUT_POWER                             0x00308056
#define RFMXLTE_ATTR_SEM_NUMBER_OF_OFFSETS                                                  0x0030800b
#define RFMXLTE_ATTR_SEM_OFFSET_START_FREQUENCY                                             0x00308014
#define RFMXLTE_ATTR_SEM_OFFSET_STOP_FREQUENCY                                              0x00308015
#define RFMXLTE_ATTR_SEM_OFFSET_SIDEBAND                                                    0x00308013
#define RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH                                        0x00308017
#define RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_TYPE                                             0x00308018
#define RFMXLTE_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL                                          0x0030800c
#define RFMXLTE_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK                                             0x0030800d
#define RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START                                        0x00308010
#define RFMXLTE_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP                                         0x00308011
#define RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START                                        0x0030801a
#define RFMXLTE_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP                                         0x0030801b
#define RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO                                                    0x00308025
#define RFMXLTE_ATTR_SEM_SWEEP_TIME_INTERVAL                                                0x00308026
#define RFMXLTE_ATTR_SEM_AVERAGING_ENABLED                                                  0x0030801f
#define RFMXLTE_ATTR_SEM_AVERAGING_COUNT                                                    0x0030801e
#define RFMXLTE_ATTR_SEM_AVERAGING_TYPE                                                     0x00308021
#define RFMXLTE_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE                                          0x00308057
#define RFMXLTE_ATTR_SEM_ALL_TRACES_ENABLED                                                 0x00308027
#define RFMXLTE_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                                         0x0030801d
#define RFMXLTE_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER                                     0x00308028
#define RFMXLTE_ATTR_SEM_RESULTS_MEASUREMENT_STATUS                                         0x00308029
#define RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_CENTER_FREQUENCY                                  0x0030804d
#define RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH                             0x0030804e
#define RFMXLTE_ATTR_SEM_RESULTS_SUBBLOCK_POWER                                             0x0030804f
#define RFMXLTE_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER                0x0030802d
#define RFMXLTE_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER                0x0030802e
#define RFMXLTE_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER                      0x0030802f
#define RFMXLTE_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY                           0x00308030
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS                            0x0030803d
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER                     0x00308034
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER                     0x00308035
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER                           0x00308036
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER                           0x00308037
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                                0x00308038
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                                        0x00308039
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER                         0x0030803a
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER                         0x0030803b
#define RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY                              0x0030803c
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS                            0x0030804a
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER                     0x00308041
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER                     0x00308042
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER                           0x00308043
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER                           0x00308044
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                                0x00308045
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                                        0x00308046
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER                         0x00308047
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER                         0x00308048
#define RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY                              0x00308049
#define RFMXLTE_ATTR_PVT_MEASUREMENT_ENABLED                                                0x00309000
#define RFMXLTE_ATTR_PVT_MEASUREMENT_METHOD                                                 0x00309002
#define RFMXLTE_ATTR_PVT_AVERAGING_ENABLED                                                  0x00309007
#define RFMXLTE_ATTR_PVT_AVERAGING_COUNT                                                    0x00309009
#define RFMXLTE_ATTR_PVT_AVERAGING_TYPE                                                     0x0030900a
#define RFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_BEFORE                                         0x00309015
#define RFMXLTE_ATTR_PVT_OFF_POWER_EXCLUSION_AFTER                                          0x00309016
#define RFMXLTE_ATTR_PVT_ALL_TRACES_ENABLED                                                 0x0030900b
#define RFMXLTE_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS                                         0x0030900c
#define RFMXLTE_ATTR_PVT_RESULTS_MEASUREMENT_STATUS                                         0x0030900e
#define RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORE                             0x00309010
#define RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_AFTER                              0x00309011
#define RFMXLTE_ATTR_PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER                                     0x00309012
#define RFMXLTE_ATTR_PVT_RESULTS_BURST_WIDTH                                                0x00309014
#define RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_ENABLED                                          0x0030a000
#define RFMXLTE_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE                                         0x0030a006
#define RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_OFFSET                                           0x0030a002
#define RFMXLTE_ATTR_SLOTPHASE_MEASUREMENT_LENGTH                                           0x0030a003
#define RFMXLTE_ATTR_SLOTPHASE_EXCLUSION_PERIOD_ENABLED                                     0x0030a007
#define RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED                                  0x0030a008
#define RFMXLTE_ATTR_SLOTPHASE_SPECTRUM_INVERTED                                            0x0030a009
#define RFMXLTE_ATTR_SLOTPHASE_ALL_TRACES_ENABLED                                           0x0030a00b
#define RFMXLTE_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY                          0x0030a014
#define RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_ENABLED                                          0x0030b000
#define RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_OFFSET                                           0x0030b002
#define RFMXLTE_ATTR_SLOTPOWER_MEASUREMENT_LENGTH                                           0x0030b003
#define RFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED                                  0x0030b005
#define RFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTED                                            0x0030b006
#define RFMXLTE_ATTR_SLOTPOWER_ALL_TRACES_ENABLED                                           0x0030b00a
#define RFMXLTE_ATTR_TXP_MEASUREMENT_ENABLED                                                0x0030e000
#define RFMXLTE_ATTR_TXP_MEASUREMENT_OFFSET                                                 0x0030e002
#define RFMXLTE_ATTR_TXP_MEASUREMENT_INTERVAL                                               0x0030e003
#define RFMXLTE_ATTR_TXP_AVERAGING_ENABLED                                                  0x0030e004
#define RFMXLTE_ATTR_TXP_AVERAGING_COUNT                                                    0x0030e005
#define RFMXLTE_ATTR_TXP_ALL_TRACES_ENABLED                                                 0x0030e007
#define RFMXLTE_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS                                         0x0030e008
#define RFMXLTE_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN                                         0x0030e00a
#define RFMXLTE_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM                                         0x0030e00b
#define RFMXLTE_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                                     0x0030d000
#define RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED                             0x0030d001
#define RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE                                               0x0030d002
#define RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE                                           0x0030d003
#define RFMXLTE_ATTR_CENTER_FREQUENCY_FOR_LIMITS                                            0x0030d004
#define RFMXLTE_ATTR_RESULT_FETCH_TIMEOUT                                                   0x0030c000

// Values for RFMXLTE_ATTR_TRIGGER_TYPE
#define RFMXLTE_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXLTE_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXLTE_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXLTE_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXLTE_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXLTE_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXLTE_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXLTE_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXLTE_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXLTE_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXLTE_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXLTE_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXLTE_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXLTE_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXLTE_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXLTE_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXLTE_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXLTE_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXLTE_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXLTE_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXLTE_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXLTE_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXLTE_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXLTE_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXLTE_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXLTE_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXLTE_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXLTE_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXLTE_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXLTE_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXLTE_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXLTE_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXLTE_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXLTE_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXLTE_ATTR_LINK_DIRECTION
#define RFMXLTE_VAL_LINK_DIRECTION_DOWNLINK                                                        0
#define RFMXLTE_VAL_LINK_DIRECTION_UPLINK                                                          1
#define RFMXLTE_VAL_LINK_DIRECTION_SIDELINK                                                        2

// Values for RFMXLTE_ATTR_DUPLEX_SCHEME
#define RFMXLTE_VAL_DUPLEX_SCHEME_FDD                                                              0
#define RFMXLTE_VAL_DUPLEX_SCHEME_TDD                                                              1
#define RFMXLTE_VAL_DUPLEX_SCHEME_LAA                                                              2

// Values for RFMXLTE_ATTR_UPLINK_DOWNLINK_CONFIGURATION
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_0                                                0
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_1                                                1
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_2                                                2
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_3                                                3
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_4                                                4
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_5                                                5
#define RFMXLTE_VAL_UPLINK_DOWNLINK_CONFIGURATION_6                                                6

// Values for RFMXLTE_ATTR_ENODEB_CATEGORY
#define RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_A                                       0
#define RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1                               1
#define RFMXLTE_VAL_ENODEB_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2                               2
#define RFMXLTE_VAL_ENODEB_LOCAL_AREA_BASE_STATION                                                 3
#define RFMXLTE_VAL_ENODEB_HOME_BASE_STATION                                                       4
#define RFMXLTE_VAL_ENODEB_MEDIUM_RANGE_BASE_STATION                                               5

// Values for RFMXLTE_ATTR_COMPONENT_CARRIER_SPACING_TYPE
#define RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL                                         0
#define RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_MINIMUM                                         1
#define RFMXLTE_VAL_COMPONENT_CARRIER_SPACING_TYPE_USER                                            2

// Values for RFMXLTE_ATTR_CYCLIC_PREFIX_MODE
#define RFMXLTE_VAL_CYCLIC_PREFIX_MODE_NORMAL                                                      0
#define RFMXLTE_VAL_CYCLIC_PREFIX_MODE_EXTENDED                                                    1

// Values for RFMXLTE_ATTR_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED
#define RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_FALSE                                  0
#define RFMXLTE_VAL_DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED_TRUE                                   1

// Values for RFMXLTE_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE
#define RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                               1
#define RFMXLTE_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL                                 2

// Values for RFMXLTE_ATTR_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_FALSE                                     0
#define RFMXLTE_VAL_AUTO_PDSCH_CHANNEL_DETECTION_ENABLED_TRUE                                      1

// Values for RFMXLTE_ATTR_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_FALSE                             0
#define RFMXLTE_VAL_AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED_TRUE                              1

// Values for RFMXLTE_ATTR_AUTO_PCFICH_CFI_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_FALSE                                        0
#define RFMXLTE_VAL_AUTO_PCFICH_CFI_DETECTION_ENABLED_TRUE                                         1

// Values for RFMXLTE_ATTR_MI_CONFIGURATION
#define RFMXLTE_VAL_MI_CONFIGURATION_TEST_MODEL                                                    0
#define RFMXLTE_VAL_MI_CONFIGURATION_STANDARD                                                      1

// Values for RFMXLTE_ATTR_DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B0                                               0
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B1                                               1
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B2                                               2
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_RATIO_P_B3                                               3

// Values for RFMXLTE_ATTR_PHICH_RESOURCE
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE_SIXTH                                 0
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_HALF                                      1
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_ONE                                       2
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_RESOURCE_TWO                                       3

// Values for RFMXLTE_ATTR_PHICH_DURATION
#define RFMXLTE_VAL_DOWNLINK_USER_DEFINED_PHICH_DURATION_NORMAL                                    0

// Values for RFMXLTE_ATTR_PDSCH_CW0_MODULATION_TYPE
#define RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QPSK                                    0
#define RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM16                                   1
#define RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM64                                   2
#define RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM256                                  3
#define RFMXLTE_VAL_USER_DEFINED_PDSCH_CW0_MODULATION_TYPE_QAM1024                                 4

// Values for RFMXLTE_ATTR_DOWNLINK_TEST_MODEL
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_1                                                      0
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM1_2                                                      1
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2                                                        2
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2A                                                       3
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1                                                      4
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_2                                                      5
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_3                                                      6
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1A                                                     7
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM2B                                                       8
#define RFMXLTE_VAL_DOWNLINK_TEST_MODEL_TM3_1B                                                     9

// Values for RFMXLTE_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_FALSE                                    0
#define RFMXLTE_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE                                     1

// Values for RFMXLTE_ATTR_AUTO_DMRS_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_DMRS_DETECTION_ENABLED_FALSE                                              0
#define RFMXLTE_VAL_AUTO_DMRS_DETECTION_ENABLED_TRUE                                               1

// Values for RFMXLTE_ATTR_UPLINK_GROUP_HOPPING_ENABLED
#define RFMXLTE_VAL_UPLINK_GROUP_HOPPING_ENABLED_FALSE                                             0
#define RFMXLTE_VAL_UPLINK_GROUP_HOPPING_ENABLED_TRUE                                              1

// Values for RFMXLTE_ATTR_UPLINK_SEQUENCE_HOPPING_ENABLED
#define RFMXLTE_VAL_UPLINK_SEQUENCE_HOPPING_ENABLED_FALSE                                          0
#define RFMXLTE_VAL_UPLINK_SEQUENCE_HOPPING_ENABLED_TRUE                                           1

// Values for RFMXLTE_ATTR_DMRS_OCC_ENABLED
#define RFMXLTE_VAL_DMRS_OCC_ENABLED_FALSE                                                         0
#define RFMXLTE_VAL_DMRS_OCC_ENABLED_TRUE                                                          1

// Values for RFMXLTE_ATTR_PUSCH_MODULATION_TYPE
#define RFMXLTE_VAL_PUSCH_MODULATION_TYPE_QPSK                                                     0
#define RFMXLTE_VAL_PUSCH_MODULATION_TYPE_16_QAM                                                   1
#define RFMXLTE_VAL_PUSCH_MODULATION_TYPE_64_QAM                                                   2
#define RFMXLTE_VAL_PUSCH_MODULATION_TYPE_256_QAM                                                  3
#define RFMXLTE_VAL_PUSCH_MODULATION_TYPE_1024_QAM                                                 4

// Values for RFMXLTE_ATTR_SRS_ENABLED
#define RFMXLTE_VAL_SRS_ENABLED_FALSE                                                              0
#define RFMXLTE_VAL_SRS_ENABLED_TRUE                                                               1

// Values for RFMXLTE_ATTR_SRS_MAXIMUM_UpPTS_ENABLED
#define RFMXLTE_VAL_SRS_MAXIMUM_UpPTS_ENABLED_FALSE                                                0
#define RFMXLTE_VAL_SRS_MAXIMUM_UpPTS_ENABLED_TRUE                                                 1

// Values for RFMXLTE_ATTR_PSSCH_MODULATION_TYPE
#define RFMXLTE_VAL_PSSCH_MODULATION_TYPE_QPSK                                                     0
#define RFMXLTE_VAL_PSSCH_MODULATION_TYPE_QAM16                                                    1
#define RFMXLTE_VAL_PSSCH_MODULATION_TYPE_QAM64                                                    2

// Values for RFMXLTE_ATTR_LAA_UPLINK_START_POSITION
#define RFMXLTE_VAL_LAA_UPLINK_START_POSITION_00                                                   0
#define RFMXLTE_VAL_LAA_UPLINK_START_POSITION_01                                                   1
#define RFMXLTE_VAL_LAA_UPLINK_START_POSITION_10                                                   2
#define RFMXLTE_VAL_LAA_UPLINK_START_POSITION_11                                                   3

// Values for RFMXLTE_ATTR_LAA_UPLINK_ENDING_SYMBOL
#define RFMXLTE_VAL_LAA_UPLINK_ENDING_SYMBOL_12                                                    12
#define RFMXLTE_VAL_LAA_UPLINK_ENDING_SYMBOL_13                                                    13

// Values for RFMXLTE_ATTR_LAA_DOWNLINK_STARTING_SYMBOL
#define RFMXLTE_VAL_LAA_DOWNLINK_STARTING_SYMBOL_0                                                 0
#define RFMXLTE_VAL_LAA_DOWNLINK_STARTING_SYMBOL_7                                                 7

// Values for RFMXLTE_ATTR_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_3                                        3
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_6                                        6
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_9                                        9
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_10                                       10
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_11                                       11
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_12                                       12
#define RFMXLTE_VAL_LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS_14                                       14

// Values for RFMXLTE_ATTR_NB_IOT_UPLINK_SUBCARRIER_SPACING
#define RFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_15KHZ                                         0
#define RFMXLTE_VAL_NB_IOT_UPLINK_SUBCARRIER_SPACING_3_75KHZ                                       1

// Values for RFMXLTE_ATTR_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED
#define RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_FALSE                                    0
#define RFMXLTE_VAL_AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED_TRUE                                     1

// Values for RFMXLTE_ATTR_NPUSCH_MODULATION_TYPE
#define RFMXLTE_VAL_NPUSCH_MODULATION_TYPE_BPSK                                                    0
#define RFMXLTE_VAL_NPUSCH_MODULATION_TYPE_QPSK                                                    1

// Values for RFMXLTE_ATTR_NPUSCH_DMRS_BASE_SEQUENCE_MODE
#define RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_MANUAL                                          0
#define RFMXLTE_VAL_NPUSCH_DMRS_BASE_SEQUENCE_MODE_AUTO                                            1

// Values for RFMXLTE_ATTR_NPUSCH_DMRS_GROUP_HOPPING_ENABLED
#define RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE                                        0
#define RFMXLTE_VAL_NPUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE                                         1

// Values for RFMXLTE_ATTR_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE
#define RFMXLTE_VAL_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                        1
#define RFMXLTE_VAL_NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL                          2

// Values for RFMXLTE_ATTR_NPDSCH_ENABLED
#define RFMXLTE_VAL_NPDSCH_ENABLED_FALSE                                                           0
#define RFMXLTE_VAL_NPDSCH_ENABLED_TRUE                                                            1

// Values for RFMXLTE_ATTR_NPDSCH_MODULATION_TYPE
#define RFMXLTE_VAL_NPDSCH_MODULATION_TYPE_QPSK                                                    0
#define RFMXLTE_VAL_NPDSCH_MODULATION_TYPE_QAM16                                                   1

// Values for RFMXLTE_ATTR_EMTC_ANALYSIS_ENABLED
#define RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_EMTC_ANALYSIS_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_LIST_STEP_TIMER_UNIT
#define RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_SLOT                                                      1
#define RFMXLTE_VAL_LIST_STEP_TIMER_UNIT_TIME                                                      6

// Values for RFMXLTE_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED
#define RFMXLTE_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE                                       0
#define RFMXLTE_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE                                        1

// Values for RFMXLTE_ATTR_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE
#define RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_COMMON                           0
#define RFMXLTE_VAL_MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE_PER_CARRIER                      1

// Values for RFMXLTE_ATTR_MODACC_SYNCHRONIZATION_MODE
#define RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME                                              0
#define RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT                                               1
#define RFMXLTE_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER                                             2

// Values for RFMXLTE_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION
#define RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL                                       1
#define RFMXLTE_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE                                         2

// Values for RFMXLTE_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED
#define RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE                               0
#define RFMXLTE_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE                                1

// Values for RFMXLTE_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED
#define RFMXLTE_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE                                    0
#define RFMXLTE_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE                                     1

// Values for RFMXLTE_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED
#define RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE                              0
#define RFMXLTE_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE                               1

// Values for RFMXLTE_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED
#define RFMXLTE_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE                            0
#define RFMXLTE_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE                             1

// Values for RFMXLTE_ATTR_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED
#define RFMXLTE_VAL_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_FALSE                                 0
#define RFMXLTE_VAL_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_TRUE                                  1

// Values for RFMXLTE_ATTR_MODACC_SPECTRUM_INVERTED
#define RFMXLTE_VAL_MODACC_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXLTE_VAL_MODACC_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXLTE_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE
#define RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE                                       0
#define RFMXLTE_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA                              1

// Values for RFMXLTE_ATTR_MODACC_EVM_UNIT
#define RFMXLTE_VAL_MODACC_EVM_UNIT_PERCENTAGE                                                     0
#define RFMXLTE_VAL_MODACC_EVM_UNIT_DB                                                             1

// Values for RFMXLTE_ATTR_MODACC_FFT_WINDOW_TYPE
#define RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_3GPP                                                    0
#define RFMXLTE_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM                                                  1

// Values for RFMXLTE_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED
#define RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE                                       0
#define RFMXLTE_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE                                        1

// Values for RFMXLTE_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED
#define RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_FALSE                                 0
#define RFMXLTE_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_TRUE                                  1

// Values for RFMXLTE_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION
#define RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL                                      0
#define RFMXLTE_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME                                     1

// Values for RFMXLTE_ATTR_MODACC_IN_BAND_EMISSION_MASK_TYPE
#define RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_8_10                                 0
#define RFMXLTE_VAL_MODACC_IN_BAND_EMISSION_MASK_TYPE_RELEASE_11_ONWARDS                           1

// Values for RFMXLTE_ATTR_MODACC_AVERAGING_ENABLED
#define RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXLTE_VAL_MODACC_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXLTE_ATTR_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL
#define RFMXLTE_VAL_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_SLOT                                  0
#define RFMXLTE_VAL_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_SUBFRAME                              1
#define RFMXLTE_VAL_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_MEASUREMENT_LENGTH                    2

// Values for RFMXLTE_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED
#define RFMXLTE_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_FALSE                             0
#define RFMXLTE_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_TRUE                              1

// Values for RFMXLTE_ATTR_MODACC_TIMING_TRACKING_ENABLED
#define RFMXLTE_VAL_MODACC_TIMING_TRACKING_ENABLED_FALSE                                           0
#define RFMXLTE_VAL_MODACC_TIMING_TRACKING_ENABLED_TRUE                                            1

// Values for RFMXLTE_ATTR_MODACC_PHASE_TRACKING_ENABLED
#define RFMXLTE_VAL_MODACC_PHASE_TRACKING_ENABLED_FALSE                                            0
#define RFMXLTE_VAL_MODACC_PHASE_TRACKING_ENABLED_TRUE                                             1

// Values for RFMXLTE_ATTR_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED
#define RFMXLTE_VAL_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED_FALSE                               0
#define RFMXLTE_VAL_ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED_TRUE                                1

// Values for RFMXLTE_ATTR_ACP_EUTRA_OFFSET_DEFINITION
#define RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_AUTO                                               0
#define RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_CLOSEST                                            1
#define RFMXLTE_VAL_ACP_EUTRA_OFFSET_DEFINITION_COMPOSITE                                          2

// Values for RFMXLTE_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXLTE_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXLTE_ATTR_ACP_RBW_FILTER_TYPE
#define RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXLTE_VAL_ACP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXLTE_ATTR_ACP_SWEEP_TIME_AUTO
#define RFMXLTE_VAL_ACP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXLTE_VAL_ACP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXLTE_ATTR_ACP_POWER_UNITS
#define RFMXLTE_VAL_ACP_POWER_UNITS_DBM                                                            0
#define RFMXLTE_VAL_ACP_POWER_UNITS_DBM_BY_HZ                                                      1

// Values for RFMXLTE_ATTR_ACP_MEASUREMENT_METHOD
#define RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1
#define RFMXLTE_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT                                          2

// Values for RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_MODE
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_MODE_MANUAL                                              0
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_MODE_AUTO                                                1

// Values for RFMXLTE_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE                                     0
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE                                      1

// Values for RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_ENABLED
#define RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXLTE_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXLTE_ATTR_ACP_NOISE_COMPENSATION_TYPE
#define RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION                           0
#define RFMXLTE_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY                                      1

// Values for RFMXLTE_ATTR_ACP_AVERAGING_ENABLED
#define RFMXLTE_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_ACP_AVERAGING_TYPE
#define RFMXLTE_VAL_ACP_AVERAGING_TYPE_RMS                                                         0
#define RFMXLTE_VAL_ACP_AVERAGING_TYPE_LOG                                                         1
#define RFMXLTE_VAL_ACP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXLTE_VAL_ACP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXLTE_VAL_ACP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXLTE_ATTR_ACP_MEASUREMENT_MODE
#define RFMXLTE_VAL_ACP_MEASUREMENT_MODE_MEASURE                                                   0
#define RFMXLTE_VAL_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                                     1

// Values for RFMXLTE_ATTR_ACP_FFT_OVERLAP_MODE
#define RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_DISABLED                                                  0
#define RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC                                                 1
#define RFMXLTE_VAL_ACP_FFT_OVERLAP_MODE_USER_DEFINED                                              2

// Values for RFMXLTE_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO
#define RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE                                          0
#define RFMXLTE_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE                                           1

// Values for RFMXLTE_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE
#define RFMXLTE_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXLTE_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXLTE_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE
#define RFMXLTE_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH                                0
#define RFMXLTE_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH                               1

// Values for RFMXLTE_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXLTE_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXLTE_ATTR_CHP_RBW_FILTER_TYPE
#define RFMXLTE_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXLTE_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXLTE_VAL_CHP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXLTE_ATTR_CHP_SWEEP_TIME_AUTO
#define RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXLTE_VAL_CHP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_MODE
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL                                              0
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO                                                1

// Values for RFMXLTE_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE                                     0
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE                                      1

// Values for RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_ENABLED
#define RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXLTE_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXLTE_ATTR_CHP_NOISE_COMPENSATION_TYPE
#define RFMXLTE_VAL_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION                           0
#define RFMXLTE_VAL_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY                                      1

// Values for RFMXLTE_ATTR_CHP_AVERAGING_ENABLED
#define RFMXLTE_VAL_CHP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_CHP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_CHP_AVERAGING_TYPE
#define RFMXLTE_VAL_CHP_AVERAGING_TYPE_RMS                                                         0
#define RFMXLTE_VAL_CHP_AVERAGING_TYPE_LOG                                                         1
#define RFMXLTE_VAL_CHP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXLTE_VAL_CHP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXLTE_VAL_CHP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXLTE_ATTR_CHP_MEASUREMENT_MODE
#define RFMXLTE_VAL_CHP_MEASUREMENT_MODE_MEASURE                                                   0
#define RFMXLTE_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                                     1

// Values for RFMXLTE_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE
#define RFMXLTE_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXLTE_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXLTE_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXLTE_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXLTE_ATTR_OBW_RBW_FILTER_TYPE
#define RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXLTE_VAL_OBW_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXLTE_ATTR_OBW_SWEEP_TIME_AUTO
#define RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXLTE_VAL_OBW_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXLTE_ATTR_OBW_AVERAGING_ENABLED
#define RFMXLTE_VAL_OBW_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_OBW_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_OBW_AVERAGING_TYPE
#define RFMXLTE_VAL_OBW_AVERAGING_TYPE_RMS                                                         0
#define RFMXLTE_VAL_OBW_AVERAGING_TYPE_LOG                                                         1
#define RFMXLTE_VAL_OBW_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXLTE_VAL_OBW_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXLTE_VAL_OBW_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXLTE_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE
#define RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXLTE_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXLTE_ATTR_SEM_UPLINK_MASK_TYPE
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_GENERAL_NS01                                              0
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS03_OR_NS11_OR_NS20_OR_NS21                              1
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS04                                                      2
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS06_OR_NS07                                              3
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_CANS04                                                    4
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_CUSTOM                                                    5
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_GENERAL_CACLASSB                                          6
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_CANCNS01                                                  7
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS27_OR_NS43                                              8
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS35                                                      9
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS28                                                      10
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_CANS09                                                    11
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_CANS10                                                    12

// Values for RFMXLTE_ATTR_SEM_DOWNLINK_MASK_TYPE
#define RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_ENODEB_CATEGORY_BASED                                   0
#define RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_BAND46                                                  1
#define RFMXLTE_VAL_SEM_DOWNLINK_MASK_TYPE_CUSTOM                                                  5

// Values for RFMXLTE_ATTR_SEM_SIDELINK_MASK_TYPE
#define RFMXLTE_VAL_SEM_SIDELINK_MASK_TYPE_GENERAL_NS01                                            0
#define RFMXLTE_VAL_SEM_SIDELINK_MASK_TYPE_NS33_OR_NS34                                            1
#define RFMXLTE_VAL_SEM_SIDELINK_MASK_TYPE_CUSTOM                                                  5

// Values for RFMXLTE_ATTR_SEM_COMPONENT_CARRIER_OUTPUT_POWER_TYPE
#define RFMXLTE_VAL_SEM_COMPONENT_CARRIER_OUTPUT_POWER_TYPE_MAXIMUM_OUTPUT_POWER                   0
#define RFMXLTE_VAL_SEM_COMPONENT_CARRIER_OUTPUT_POWER_TYPE_RATED_OUTPUT_POWER                     1

// Values for RFMXLTE_ATTR_SEM_OFFSET_SIDEBAND
#define RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE                                                   0
#define RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_POSITIVE                                                   1
#define RFMXLTE_VAL_SEM_OFFSET_SIDEBAND_BOTH                                                       2

// Values for RFMXLTE_ATTR_SEM_OFFSET_RBW_FILTER_TYPE
#define RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED                                           0
#define RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN                                            1
#define RFMXLTE_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT                                                2

// Values for RFMXLTE_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK
#define RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL                                         0
#define RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL                                          1
#define RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE                                            2
#define RFMXLTE_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE                                            3

// Values for RFMXLTE_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXLTE_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXLTE_ATTR_SEM_AVERAGING_ENABLED
#define RFMXLTE_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_SEM_AVERAGING_TYPE
#define RFMXLTE_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXLTE_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXLTE_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXLTE_VAL_SEM_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXLTE_VAL_SEM_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXLTE_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE
#define RFMXLTE_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXLTE_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXLTE_ATTR_SEM_RESULTS_MEASUREMENT_STATUS
#define RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXLTE_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXLTE_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXLTE_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXLTE_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXLTE_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXLTE_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXLTE_ATTR_PVT_MEASUREMENT_METHOD
#define RFMXLTE_VAL_PVT_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXLTE_VAL_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1

// Values for RFMXLTE_ATTR_PVT_AVERAGING_ENABLED
#define RFMXLTE_VAL_PVT_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_PVT_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_PVT_AVERAGING_TYPE
#define RFMXLTE_VAL_PVT_AVERAGING_TYPE_RMS                                                         0
#define RFMXLTE_VAL_PVT_AVERAGING_TYPE_LOG                                                         1

// Values for RFMXLTE_ATTR_PVT_RESULTS_MEASUREMENT_STATUS
#define RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_FAIL                                            0
#define RFMXLTE_VAL_PVT_RESULTS_MEASUREMENT_STATUS_PASS                                            1

// Values for RFMXLTE_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE
#define RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXLTE_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXLTE_ATTR_SLOTPHASE_EXCLUSION_PERIOD_ENABLED
#define RFMXLTE_VAL_SLOTPHASE_EXCLUSION_PERIOD_ENABLED_FALSE                                       0
#define RFMXLTE_VAL_SLOTPHASE_EXCLUSION_PERIOD_ENABLED_TRUE                                        1

// Values for RFMXLTE_ATTR_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED
#define RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_FALSE                                    0
#define RFMXLTE_VAL_SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED_TRUE                                     1

// Values for RFMXLTE_ATTR_SLOTPHASE_SPECTRUM_INVERTED
#define RFMXLTE_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXLTE_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXLTE_ATTR_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED
#define RFMXLTE_VAL_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED_FALSE                                    0
#define RFMXLTE_VAL_SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED_TRUE                                     1

// Values for RFMXLTE_ATTR_SLOTPOWER_SPECTRUM_INVERTED
#define RFMXLTE_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXLTE_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXLTE_ATTR_TXP_AVERAGING_ENABLED
#define RFMXLTE_VAL_TXP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXLTE_VAL_TXP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXLTE_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED
#define RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE                               0
#define RFMXLTE_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE                                1

// Values for RFMXLTE_ATTR_TRANSMITTER_ARCHITECTURE
#define RFMXLTE_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_COMPONENT_CARRIER                              0
#define RFMXLTE_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK                                       1

// Values for RFMXLTE_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXLTE_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for MechanicalAttenuationAuto
#define RFMXLTE_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXLTE_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

// Values for RFAttenuationAuto
#define RFMXLTE_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXLTE_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for FrequencyReferenceSource
#define RFMXLTE_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXLTE_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXLTE_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXLTE_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for Boolean
#define RFMXLTE_VAL_FALSE                                                                          0
#define RFMXLTE_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXLTE_VAL_ACP                                                                            1<<0
#define RFMXLTE_VAL_CHP                                                                            1<<1
#define RFMXLTE_VAL_MODACC                                                                         1<<2
#define RFMXLTE_VAL_OBW                                                                            1<<3
#define RFMXLTE_VAL_SEM                                                                            1<<4
#define RFMXLTE_VAL_PVT                                                                            1<<5
#define RFMXLTE_VAL_SLOTPHASE                                                                      1<<6
#define RFMXLTE_VAL_SLOTPOWER                                                                      1<<7
#define RFMXLTE_VAL_TXP                                                                            1<<8

// Values for AcpNoiseCalibrationDataValid
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_DATA_VALID_FALSE                                         0
#define RFMXLTE_VAL_ACP_NOISE_CALIBRATION_DATA_VALID_TRUE                                          1

// Values for ChpNoiseCalibrationDataValid
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_DATA_VALID_FALSE                                         0
#define RFMXLTE_VAL_CHP_NOISE_CALIBRATION_DATA_VALID_TRUE                                          1

/* ---------------- RFmxLTE APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxLTE_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxLTE_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxLTE_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxLTE_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxLTE_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxLTE_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxLTE_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxLTE_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxLTE_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxLTE_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxLTE_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxLTE_BuildListString(
   char listName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxLTE_BuildListStepString(
   char listName[],
   char resultName[],
   int32 stepNumber,
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxLTE_BuildCarrierString(
   char selectorString[],
   int32 carrierNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_BuildClusterString(
   char selectorString[],
   int32 clusterNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_BuildPDSCHString(
   char selectorString[],
   int32 PDSCHNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_BuildSubblockString(
   char selectorString[],
   int32 subblockNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_BuildSubframeString(
   char selectorString[],
   int32 subframeNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxLTE_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxLTE_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxLTE_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxLTE_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxLTE_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxLTE_ACPValidateNoiseCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* noiseCalibrationDataValid
);

int32 __stdcall RFmxLTE_CHPValidateNoiseCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* noiseCalibrationDataValid
);

int32 __stdcall RFmxLTE_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxLTE_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxLTE_AnalyzeSpectrum1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxLTE_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxLTE_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxLTE_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_ClearNoiseCalibrationDatabase(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxLTE_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_CfgFrequencyEARFCN(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection,
   int32 band,
   int32 EARFCN
);

int32 __stdcall RFmxLTE_CreateListStep(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* createdStepIndex
);

int32 __stdcall RFmxLTE_CreateList(
   niRFmxInstrHandle instrumentHandle,
   char listName[]
);

int32 __stdcall RFmxLTE_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxLTE_DeleteList(
   niRFmxInstrHandle instrumentHandle,
   char listName[]
);

int32 __stdcall RFmxLTE_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxLTE_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxLTE_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxLTE_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxLTE_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxLTE_SEMCfgComponentCarrierMaximumOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierMaximumOutputPower
);

int32 __stdcall RFmxLTE_SEMCfgDownlinkMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 downlinkMaskType,
   float64 deltaFMaximum,
   float64 aggregatedMaximumPower
);

int32 __stdcall RFmxLTE_SEMCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxLTE_SEMCfgOffsetAbsoluteLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetAbsoluteLimitStart,
   float64 offsetAbsoluteLimitStop
);

int32 __stdcall RFmxLTE_SEMCfgOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetBandwidthIntegral
);

int32 __stdcall RFmxLTE_SEMCfgOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetStartFrequency,
   float64 offsetStopFrequency,
   int32 offsetSideband
);

int32 __stdcall RFmxLTE_SEMCfgOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 limitFailMask
);

int32 __stdcall RFmxLTE_SEMCfgOffsetRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetRBW,
   int32 offsetRBWFilterType
);

int32 __stdcall RFmxLTE_SEMCfgOffsetRelativeLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 relativeLimitStart,
   float64 relativeLimitStop
);

int32 __stdcall RFmxLTE_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxLTE_SEMCfgUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkMaskType
);

int32 __stdcall RFmxLTE_SEMCfgComponentCarrierMaximumOutputPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierMaximumOutputPower[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetAbsoluteLimitArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetAbsoluteLimitStart[],
   float64 offsetAbsoluteLimitStop[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetBandwidthIntegralArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetBandwidthIntegral[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetStartFrequency[],
   float64 offsetStopFrequency[],
   int32 offsetSideband[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetLimitFailMaskArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 limitFailMask[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetRBWFilterArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetRBW[],
   int32 offsetRBWFilterType[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_SEMCfgOffsetRelativeLimitArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 relativeLimitStart[],
   float64 relativeLimitStop[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_CfgAutoDMRSDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoDMRSDetectionEnabled
);

int32 __stdcall RFmxLTE_CfgAutoNPUSCHChannelDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoNPUSCHChannelDetectionEnabled
);

int32 __stdcall RFmxLTE_CfgAutoResourceBlockDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoResourceBlockDetectionEnabled
);

int32 __stdcall RFmxLTE_CfgBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 band
);

int32 __stdcall RFmxLTE_CfgCellSpecificRatio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 cellSpecificRatio
);

int32 __stdcall RFmxLTE_CfgComponentCarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 componentCarrierSpacingType,
   int32 componentCarrierAtCenterFrequency
);

int32 __stdcall RFmxLTE_CfgComponentCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierBandwidth,
   float64 componentCarrierFrequency,
   int32 cellID
);

int32 __stdcall RFmxLTE_CfgDownlinkAutoCellIDDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoCellIDDetectionEnabled
);

int32 __stdcall RFmxLTE_CfgDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelConfigurationMode
);

int32 __stdcall RFmxLTE_CfgDownlinkNumberOfSubframes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfSubframes
);

int32 __stdcall RFmxLTE_CfgDownlinkSynchronizationSignal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 PSSPower,
   float64 SSSPower
);

int32 __stdcall RFmxLTE_CfgDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 downlinkTestModel
);

int32 __stdcall RFmxLTE_CfgDuplexScheme(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 duplexScheme,
   int32 uplinkDownlinkConfiguration
);

int32 __stdcall RFmxLTE_CfgEMTCAnalysisEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 EMTCAnalysisEnabled
);

int32 __stdcall RFmxLTE_CfgeNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 eNodeBCategory
);

int32 __stdcall RFmxLTE_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxLTE_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxLTE_CfgLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection
);

int32 __stdcall RFmxLTE_CfgNBIoTComponentCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 NCellID,
   int32 uplinkSubcarrierSpacing
);

int32 __stdcall RFmxLTE_CfgNPUSCHDMRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 NPUSCHDMRSBaseSequenceMode,
   int32 NPUSCHDMRSBaseSequenceIndex,
   int32 NPUSCHDMRSCyclicShift,
   int32 NPUSCHDMRSGroupHoppingEnabled,
   int32 NPUSCHDMRSDeltaSS
);

int32 __stdcall RFmxLTE_CfgNPUSCHFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 format
);

int32 __stdcall RFmxLTE_CfgNPUSCHStartingSlot(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 startingSlot
);

int32 __stdcall RFmxLTE_CfgNPUSCHTones(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 toneOffset,
   int32 numberOfTones,
   int32 modulationType
);

int32 __stdcall RFmxLTE_CfgNumberOfComponentCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfComponentCarriers
);

int32 __stdcall RFmxLTE_CfgNumberOfDUTAntennas(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfDUTAntennas
);

int32 __stdcall RFmxLTE_CfgNumberOfPDSCHChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfPDSCHChannels
);

int32 __stdcall RFmxLTE_CfgNumberOfPUSCHResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfResourceBlockClusters
);

int32 __stdcall RFmxLTE_CfgNumberOfSubblocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfSubblocks
);

int32 __stdcall RFmxLTE_CfgPBCH(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 PBCHPower
);

int32 __stdcall RFmxLTE_CfgPCFICH(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 CFI,
   float64 power
);

int32 __stdcall RFmxLTE_CfgPDCCH(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 PDCCHPower
);

int32 __stdcall RFmxLTE_CfgPDSCH(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 CW0ModulationType,
   char resourceBlockAllocation[],
   float64 power
);

int32 __stdcall RFmxLTE_CfgPHICH(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 resource,
   int32 duration,
   float64 power
);

int32 __stdcall RFmxLTE_CfgPSSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modulationType
);

int32 __stdcall RFmxLTE_CfgPSSCHResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 resourceBlockOffset,
   int32 numberOfResourceBlocks
);

int32 __stdcall RFmxLTE_CfgPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modulationType
);

int32 __stdcall RFmxLTE_CfgPUSCHResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 resourceBlockOffset,
   int32 numberOfResourceBlocks
);

int32 __stdcall RFmxLTE_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxLTE_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxLTE_CfgTransmitAntennaToAnalyze(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 transmitAntennaToAnalyze
);

int32 __stdcall RFmxLTE_CfgComponentCarrierArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierBandwidth[],
   float64 componentCarrierFrequency[],
   int32 cellID[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_CfgDownlinkTestModelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 downlinkTestModel[],
   int32 numberOfElements
);

int32 __stdcall RFmxLTE_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxLTE_ACPCfgConfigurableNumberOfOffsetsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 configurableNumberOfOffsetsEnabled
);

int32 __stdcall RFmxLTE_ACPCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxLTE_ACPCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxLTE_ACPCfgNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfEUTRAOffsets
);

int32 __stdcall RFmxLTE_ACPCfgNumberOfGSMOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfGSMOffsets
);

int32 __stdcall RFmxLTE_ACPCfgNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfUTRAOffsets
);

int32 __stdcall RFmxLTE_ACPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxLTE_ACPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxLTE_ACPCfgUTRAAndEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfUTRAOffsets,
   int32 numberOfEUTRAOffsets
);

int32 __stdcall RFmxLTE_ACPCfgPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerUnits
);

int32 __stdcall RFmxLTE_CHPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxLTE_CHPCfgIntegrationBandwidthType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 integrationBandwidthType
);

int32 __stdcall RFmxLTE_CHPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxLTE_CHPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxLTE_ModAccCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxLTE_ModAccCfgCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 commonClockSourceEnabled
);

int32 __stdcall RFmxLTE_ModAccCfgEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 EVMUnit
);

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 FFTWindowOffset
);

int32 __stdcall RFmxLTE_ModAccCfgFFTWindowPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 FFTWindowType,
   float64 FFTWindowOffset,
   float64 FFTWindowLength
);

int32 __stdcall RFmxLTE_ModAccCfgInBandEmissionMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 inBandEmissionMaskType
);

int32 __stdcall RFmxLTE_ModAccCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxLTE_OBWCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxLTE_OBWCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxLTE_OBWCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxLTE_PVTCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxLTE_PVTCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxLTE_PVTCfgOFFPowerExclusionPeriods(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 OFFPowerExclusionBefore,
   float64 OFFPowerExclusionAfter
);

int32 __stdcall RFmxLTE_SlotPhaseCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxLTE_SlotPowerCfgMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxLTE_TXPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxLTE_TXPCfgMeasurementOffsetAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementOffset,
   float64 measurementInterval
);

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle dataConstellation[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   NIComplexSingle DMRSConstellation[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 dataConstellationI[],
   float32 dataConstellationQ[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   float32 DMRSConstellationI[],
   float32 DMRSConstellationQ[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle dataConstellation[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   NIComplexSingle DMRSConstellation[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 dataConstellationI[],
   float32 dataConstellationQ[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   float32 DMRSConstellationI[],
   float32 DMRSConstellationQ[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle dataConstellation[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   NIComplexSingle DMRSConstellation[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 dataConstellationI[],
   float32 dataConstellationQ[],
   int32 dataConstellationArraySize,
   int32* dataConstellationActualArraySize,
   float32 DMRSConstellationI[],
   float32 DMRSConstellationQ[],
   int32 DMRSConstellationArraySize,
   int32* DMRSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSpectralFlatnessTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectralFlatness[],
   float32 spectralFlatnessLowerMask[],
   float32 spectralFlatnessUpperMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle SSSConstellation[],
   NIComplexSingle PSSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 SSSConstellationI[],
   float32 SSSConstellationQ[],
   float32 PSSConstellationI[],
   float32 PSSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle NSSSConstellation[],
   int32 NSSSConstellationArraySize,
   int32* NSSSConstellationActualArraySize,
   NIComplexSingle NPSSConstellation[],
   int32 NPSSConstellationArraySize,
   int32* NPSSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNBSynchronizationSignalConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 NSSSConstellationI[],
   float32 NSSSConstellationQ[],
   int32 NSSSConstellationArraySize,
   int32* NSSSConstellationActualArraySize,
   float32 NPSSConstellationI[],
   float32 NPSSConstellationQ[],
   int32 NPSSConstellationArraySize,
   int32* NPSSConstellationActualArraySize
);

int32 __stdcall RFmxLTE_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxLTE_CfgDownlinkAutoChannelDetection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoPDSCHChannelDetectionEnabled,
   int32 autoControlChannelPowerDetectionEnabled,
   int32 autoPCFICHCFIDetectionEnabled,
   int32 reserved
);

int32 __stdcall RFmxLTE_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 triggerMinQuietTimeMode,
   float64 triggerMinQuietTimeDuration,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxLTE_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxLTE_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxLTE_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxLTE_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxLTE_ACPFetchAbsolutePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 absolutePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ACPFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ACPFetchOffsetMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ACPFetchRelativePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 relativePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ACPFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxLTE_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower
);

int32 __stdcall RFmxLTE_ACPFetchSubblockMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower,
   float64* integrationBandwidth,
   float64* frequency
);

int32 __stdcall RFmxLTE_ACPFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxLTE_CHPFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_CHPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_CHPFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxLTE_CHPFetchSubblockMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower,
   float64* integrationBandwidth,
   float64* frequency
);

int32 __stdcall RFmxLTE_CHPFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxLTE_ModAccFetchCompositeEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSCompositeEVM[],
   float64 maximumPeakCompositeEVM[],
   float64 meanFrequencyError[],
   int32 peakCompositeEVMSymbolIndex[],
   int32 peakCompositeEVMSubcarrierIndex[],
   int32 peakCompositeEVMSlotIndex[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchCompositeMagnitudeAndPhaseErrorArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSCompositeMagnitudeError[],
   float64 maximumPeakCompositeMagnitudeError[],
   float64 meanRMSCompositePhaseError[],
   float64 maximumPeakCompositePhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchCSRSConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle CSRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchCSRSConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 CSRSConstellationI[],
   float32 CSRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchCSRSEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSCSRSEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellIDArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 detectedCellID[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PBCHConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPBCHConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PBCHConstellationI[],
   float32 PBCHConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PCFICHConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPCFICHConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PCFICHConstellationI[],
   float32 PCFICHConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPDCCHConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PDCCHConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPDCCHConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PDCCHConstellationI[],
   float32 PDCCHConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PHICHConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkPHICHConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PHICHConstellationI[],
   float32 PHICHConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 RSTransmitPower[],
   float64 OFDMSymbolTransmitPower[],
   float64 reserved1[],
   float64 reserved2[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchEVMPerSlotTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMPerSlot[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchEVMPerSubcarrierTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 meanRMSEVMPerSubcarrier[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchEVMHighPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVMHighPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMHighPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumEVMHighPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchEVMLowPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVMLowPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMLowPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumEVMLowPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchInBandEmissionMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 inBandEmissionMargin[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchInBandEmissionTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 inBandEmission[],
   float32 inBandEmissionMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchIQImpairmentsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanIQOriginOffset[],
   float64 meanIQGainImbalance[],
   float64 meanIQQuadratureError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSlotTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumEVMPerSlot[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSubcarrierTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumEVMPerSubcarrier[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumEVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumMagnitudeErrorPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumMagnitudeErrorPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumPhaseErrorPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumPhaseErrorPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM1024Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM1024ConstellationI[],
   float32 QAM1024ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMS1024QAMEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM16Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH16QAMConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM16ConstellationI[],
   float32 QAM16ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM256Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH256QAMConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM256ConstellationI[],
   float32 QAM256ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM64Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH64QAMConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM64ConstellationI[],
   float32 QAM64ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCHEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSEVM[],
   float64 meanRMSQPSKEVM[],
   float64 meanRMS16QAMEVM[],
   float64 meanRMS64QAMEVM[],
   float64 meanRMS256QAMEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCHQPSKConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QPSKConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCHQPSKConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QPSKConstellationI[],
   float32 QPSKConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHDataEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 PSSCHMeanRMSDataEVM[],
   float64 PSSCHMaximumPeakDataEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHDMRSEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 PSSCHMeanRMSDMRSEVM[],
   float64 PSSCHMaximumPeakDMRSEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 PSSCHMeanDataPower[],
   float64 PSSCHMeanDMRSPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDataEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSDataEVM[],
   float64 maximumPeakDataEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDemodulatedBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 bits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSDMRSEVM[],
   float64 maximumPeakDMRSEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHSymbolPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 PUSCHMeanDataPower[],
   float64 PUSCHMeanDMRSPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchRMSMagnitudeErrorPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSMagnitudeErrorPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchRMSPhaseErrorPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSPhaseErrorPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSpectralFlatnessArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 range1MaximumToRange1Minimum[],
   float64 range2MaximumToRange2Minimum[],
   float64 range1MaximumToRange2Minimum[],
   float64 range2MaximumToRange1Minimum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSRSConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle SRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSRSConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 SRSConstellationI[],
   float32 SRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSRSEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSSRSEVM[],
   float64 meanSRSPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSubblockInBandEmissionTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 subblockInBandEmission[],
   float64 subblockInBandEmissionMask[],
   float64 subblockInBandEmissionRBIndices[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 meanRMSPSSEVM[],
   float64 meanRMSSSSEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchMaximumFrequencyErrorPerSlotTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 maximumFrequencyErrorPerSlot[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QPSKConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNPDSCHQPSKConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QPSKConstellationI[],
   float32 QPSKConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNRSConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle NRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNRSConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 NRSConstellationI[],
   float32 NRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNPDSCH16QAMConstellation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM16Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchNPDSCH16QAMConstellationSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM16ConstellationI[],
   float32 QAM16ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_ModAccFetchCompositeEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSCompositeEVM,
   float64* maximumPeakCompositeEVM,
   float64* meanFrequencyError,
   int32* peakCompositeEVMSymbolIndex,
   int32* peakCompositeEVMSubcarrierIndex,
   int32* peakCompositeEVMSlotIndex
);

int32 __stdcall RFmxLTE_ModAccFetchCompositeMagnitudeAndPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSCompositeMagnitudeError,
   float64* maxPeakCompositeMagnitudeError,
   float64* meanRMSCompositePhaseError,
   float64* maxPeakCompositePhaseError
);

int32 __stdcall RFmxLTE_ModAccFetchCSRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSCSRSEVM
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkDetectedCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* detectedCellID
);

int32 __stdcall RFmxLTE_ModAccFetchDownlinkTransmitPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RSTransmitPower,
   float64* OFDMSymbolTransmitPower,
   float64* reserved1,
   float64* reserved2
);

int32 __stdcall RFmxLTE_ModAccFetchInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* inBandEmissionMargin
);

int32 __stdcall RFmxLTE_ModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanIQOriginOffset,
   float64* meanIQGainImbalance,
   float64* meanIQQuadratureError
);

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* NPUSCHMeanRMSDataEVM,
   float64* NPUSCHMaximumPeakDataEVM
);

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* NPUSCHMeanRMSDMRSEVM,
   float64* NPUSCHMaximumPeakDMRSEVM
);

int32 __stdcall RFmxLTE_ModAccFetchNPUSCHSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* NPUSCHMeanDataPower,
   float64* NPUSCHMeanDMRSPower
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCH1024QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMS1024QAMEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPDSCHEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSEVM,
   float64* meanRMSQPSKEVM,
   float64* meanRMS16QAMEVM,
   float64* meanRMS64QAMEVM,
   float64* meanRMS256QAMEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PSSCHMeanRMSDataEVM,
   float64* PSSCHMaximumPeakDataEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PSSCHMeanRMSDMRSEVM,
   float64* PSSCHMaximumPeakDMRSEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPSSCHSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PSSCHMeanDataPower,
   float64* PSSCHMeanDMRSPower
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSDataEVM,
   float64* maximumPeakDataEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSDMRSEVM,
   float64* maximumPeakDMRSEVM
);

int32 __stdcall RFmxLTE_ModAccFetchPUSCHSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PUSCHMeanDataPower,
   float64* PUSCHMeanDMRSPower
);

int32 __stdcall RFmxLTE_ModAccFetchSpectralFlatness(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* range1MaximumToRange1Minimum,
   float64* range2MaximumToRange2Minimum,
   float64* range1MaximumToRange2Minimum,
   float64* range2MaximumToRange1Minimum
);

int32 __stdcall RFmxLTE_ModAccFetchSRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSSRSEVM,
   float64* meanSRSPower
);

int32 __stdcall RFmxLTE_ModAccFetchSubblockInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockInBandEmissionMargin
);

int32 __stdcall RFmxLTE_ModAccFetchSubblockIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockMeanIQOriginOffset,
   float64* subblockMeanIQGainImbalance,
   float64* subblockMeanIQQuadratureError
);

int32 __stdcall RFmxLTE_ModAccFetchSynchronizationSignalEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSPSSEVM,
   float64* meanRMSSSSEVM
);

int32 __stdcall RFmxLTE_OBWFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_OBWFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* occupiedBandwidth,
   float64* absolutePower,
   float64* startFrequency,
   float64* stopFrequency
);

int32 __stdcall RFmxLTE_SEMFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   float32 compositeMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   float64 absolutePeakPower[],
   float64 peakFrequency[],
   float64 relativePeakPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SEMFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower
);

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxLTE_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxLTE_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxLTE_SEMFetchSubblockMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower,
   float64* integrationBandwidth,
   float64* frequency
);

int32 __stdcall RFmxLTE_SEMFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxLTE_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxLTE_PVTFetchMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 meanAbsoluteOFFPowerBefore[],
   float64 meanAbsoluteOFFPowerAfter[],
   float64 meanAbsoluteONPower[],
   float64 burstWidth[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_PVTFetchSignalPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 signalPower[],
   float32 absoluteLimit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_PVTFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* meanAbsoluteOFFPowerBefore,
   float64* meanAbsoluteOFFPowerAfter,
   float64* meanAbsoluteONPower,
   float64* burstWidth
);

int32 __stdcall RFmxLTE_SlotPhaseFetchMaximumPhaseDiscontinuityArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 maximumPhaseDiscontinuity[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SlotPhaseFetchPhaseDiscontinuities(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotPhaseDiscontinuity[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SlotPhaseFetchSamplePhaseErrorLinearFitTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 samplePhaseErrorLinearFit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SlotPhaseFetchSamplePhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 samplePhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_SlotPhaseFetchMaximumPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumPhaseDiscontinuity
);

int32 __stdcall RFmxLTE_SlotPowerFetchPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 subframePower[],
   float64 subframePowerDelta[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_TXPFetchPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 power[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxLTE_TXPFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averagePowerMean,
   float64* peakPowerMaximum
);

int32 __stdcall RFmxLTE_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxLTE_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxLTE_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxLTE_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxLTE_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxLTE_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxLTE_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDuplexScheme(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDuplexScheme(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetUplinkDownlinkConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetUplinkDownlinkConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GeteNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SeteNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSpecialSubframeConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSpecialSubframeConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNumberOfDUTAntennas(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNumberOfDUTAntennas(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetTransmitAntennaToAnalyze(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetTransmitAntennaToAnalyze(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNumberOfSubblocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNumberOfSubblocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSubblockFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetSubblockFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetComponentCarrierSpacingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetComponentCarrierSpacingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetComponentCarrierAtCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetComponentCarrierAtCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNumberOfComponentCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNumberOfComponentCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetComponentCarrierBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetComponentCarrierBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetComponentCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetComponentCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetCyclicPrefixMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetCyclicPrefixMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkAutoCellIDDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkAutoCellIDDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoPDSCHChannelDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoPDSCHChannelDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoControlChannelPowerDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoControlChannelPowerDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoPCFICHCFIDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoPCFICHCFIDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetMiConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetMiConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedCellSpecificRatio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedCellSpecificRatio(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinUserDefinedPBCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinUserDefinedPBCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetUserDefinedPDCCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetUserDefinedPDCCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedNumberOfSubframes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedNumberOfSubframes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPCFICHCFI(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPCFICHCFI(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPCFICHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPCFICHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPHICHResource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPHICHResource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPHICHDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPHICHDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkUserDefinedPhichPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkUserDefinedPhichPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetUserDefinedPDSCHNumberOfAllocations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetUserDefinedPDSCHNumberOfAllocations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetUserDefinedPDSCHCW0ModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetUserDefinedPDSCHCW0ModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetUserDefinedPDSCHResourceBlockAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxLTE_SetUserDefinedPDSCHResourceBlockAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxLTE_GetUserDefinedPDSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetUserDefinedPDSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoResourceBlockDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoResourceBlockDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoDMRSDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoDMRSDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetUplinkGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetUplinkGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetUplinkSequenceHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetUplinkSequenceHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetDMRSOCCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetDMRSOCCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHnDMRS1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHnDMRS1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHDeltaSequenceShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHDeltaSequenceShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHnDMRS2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHnDMRS2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHCyclicShiftField(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHCyclicShiftField(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPUSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetPUSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetSRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRSSubframeConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSSubframeConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_C_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_C_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_B_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_B_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_I_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_I_SRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_n_RRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_n_RRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_n_SRS_CS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_n_SRS_CS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_b_Hop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_b_Hop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRS_k_TC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRS_k_TC(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRSMaximumUpPTSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSMaximumUpPTSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRSSubframe1_N_RA(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSSubframe1_N_RA(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRSSubframe6_N_RA(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSSubframe6_N_RA(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetSRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetPSSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPSSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPSSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPSSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPSSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetPSSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetPSSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetPSSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetLAAStartingSubframe(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAAStartingSubframe(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLAANumberOfSubframes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAANumberOfSubframes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLAAUplinkStartPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAAUplinkStartPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLAAUplinkEndingSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAAUplinkEndingSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLAADownlinkStartingSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAADownlinkStartingSymbol(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLAADownlinkNumberOfEndingSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLAADownlinkNumberOfEndingSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNBIoTUplinkSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNBIoTUplinkSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetAutoNPUSCHChannelDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoNPUSCHChannelDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHStartingSlot(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHStartingSlot(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHToneOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHToneOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHNumberOfTones(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHNumberOfTones(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHDMRSBaseSequenceMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHDMRSBaseSequenceMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHDMRSBaseSequenceIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHDMRSBaseSequenceIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHDMRSCyclicShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHDMRSCyclicShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHDMRSGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHDMRSGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPUSCHDMRSDeltaSequenceShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPUSCHDMRSDeltaSequenceShift(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNBIoTDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNBIoTDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetNPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetNSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetNSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetNPDSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetNPDSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetNPDSCHEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPDSCHEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNPDSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNPDSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetEMTCAnalysisEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetEMTCAnalysisEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetNumberOfSteps(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetNumberOfSteps(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetListStepTimerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetListStepTimerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetListStepTimerDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetListStepTimerDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetListStepTimerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetListStepTimerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetAcquisitionBandwidthOptimizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetAcquisitionBandwidthOptimizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetCenterFrequencyForLimits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetCenterFrequencyForLimits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetMulticarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMulticarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetMulticarrierTimeSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMulticarrierTimeSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetFrequencyErrorEstimation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetFrequencyErrorEstimation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetIQOriginOffsetEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetIQOriginOffsetEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetIQMismatchEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetIQMismatchEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetFFTWindowType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetFFTWindowType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetFFTWindowOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetFFTWindowOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetFFTWindowLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetFFTWindowLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetEVMWithExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetEVMWithExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetSpectralFlatnessCondition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetSpectralFlatnessCondition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetInBandEmissionMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetInBandEmissionMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetPreFFTErrorEstimationInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetPreFFTErrorEstimationInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetSymbolClockErrorEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetSymbolClockErrorEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetTimingTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetTimingTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSCompositeEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMaximumPeakCompositeEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSCompositeMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMaximumPeakCompositeMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRmsCompositePhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMaximumPeakCompositePhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPeakCompositeEVMSlotIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPeakCompositeEVMSymbolIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPeakCompositeEVMSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMSQPSKEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMS16QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMS64QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMS256QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDSCHMeanRMS1024QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsRSDownlinkMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkPSSMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkSSSMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkPBCHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkPCFICHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPDCCHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkPHICHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkRSTransmitPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkOFDMSymbolTransmitPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkDetectedCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSNPSSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSNSSSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPDSCHMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPDSCHMeanRMSQPSKEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPDSCHMeanRMS16QAMEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSNRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsDownlinkNRSTransmitPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSpectralFlatnessRange1MaximumToRange1Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSpectralFlatnessRange2MaximumToRange2Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSpectralFlatnessRange1MaximumToRange2Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMeanRMSDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMaximumPeakDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMeanRMSDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMaximumPeakDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMeanDataPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPUSCHMeanDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanRMSSRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanSRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMeanRMSDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMaximumPeakDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMeanRMSDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMaximumPeakDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMeanDataPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsNPUSCHMeanDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSpectralFlatnessRange2MaximumToRange1Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSubblockInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMeanRMSDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMaximumPeakDataEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMeanRMSDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMaximumPeakDMRSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMeanDataPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsPSSCHMeanDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMaximumPeakFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMaximumPeakIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanIQTimingSkew(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanTimeOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsMeanSymbolClockError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSubblockMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSubblockMeanIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ModAccGetResultsSubblockMeanQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetConfigurableNumberOfOffsetsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetConfigurableNumberOfOffsetsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetEUTRAOffsetDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetEUTRAOffsetDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNumberOfGSMOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNumberOfGSMOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNumberOfStandaloneNBIoTOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNumberOfStandaloneNBIoTOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ACPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ACPGetPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ACPGetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ACPGetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_ACPGetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsSubblockCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsComponentCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsComponentCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetIntegrationBandwidthType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetIntegrationBandwidthType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_CHPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_CHPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsSubblockFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsComponentCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_CHPGetResultsComponentCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_OBWGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_OBWGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_OBWSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_OBWGetResultsOccupiedBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWGetResultsAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWGetResultsStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_OBWGetResultsStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetDownlinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetDownlinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetSidelinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetSidelinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetDeltaFMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetDeltaFMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAggregatedMaximumPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAggregatedMaximumPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetSubblockAggregatedChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetComponentCarrierOutputPowerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetComponentCarrierOutputPowerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetComponentCarrierMaximumOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetComponentCarrierMaximumOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetAbsoluteLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetAbsoluteLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetAbsoluteLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetAbsoluteLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsSubblockCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsComponentCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsComponentCarrierRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsComponentCarrierAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsComponentCarrierPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetOFFPowerExclusionBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetOFFPowerExclusionBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_PVTGetOFFPowerExclusionAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetOFFPowerExclusionAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_PVTGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_PVTGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_PVTGetResultsMeanAbsoluteOFFPowerBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTGetResultsMeanAbsoluteOFFPowerAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTGetResultsMeanAbsoluteONPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_PVTGetResultsBurstWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPhaseGetResultsMaximumPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SlotPowerGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SlotPowerSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_TXPGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxLTE_TXPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_TXPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_TXPGetResultsAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxLTE_TXPGetResultsPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXLTE_ATTR_SEM_STANDARD_MASK_TYPE                                                 0x0030804c
#define RFMXLTE_ATTR_MODACC_MULTI_CARRIER_FILTER_ENABLED                                    0x00304002
#define RFMXLTE_ATTR_SUBBLOCK_FREQUENCY_DEFINITION                                          0x00300024

// Values for RFMXLTE_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXLTE_VAL_IQ_POWER_EDGE_LEVEL_TYPE_RELATIVE                                              0
#define RFMXLTE_VAL_IQ_POWER_EDGE_LEVEL_TYPE_ABSOLUTE                                              1

// Values for RFMXLTE_ATTR_SEM_STANDARD_MASK_TYPE
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_GENERAL_NS01                                            0
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_NS03_OR_NS11_OR_NS20                                    1
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_NS04                                                    2
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_NS06_OR_NS07                                            3
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_CANS04                                                  4
#define RFMXLTE_VAL_SEM_STANDARD_MASK_TYPE_CUSTOM                                                  5

// Values for RFMXLTE_ATTR_SEM_UPLINK_MASK_TYPE
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS03_OR_NS11_OR_NS20                                      1
#define RFMXLTE_VAL_SEM_UPLINK_MASK_TYPE_NS27                                                      8

// Values for RFMXLTE_ATTR_SUBBLOCK_FREQUENCY_DEFINITION
#define RFMXLTE_VAL_SUBBLOCK_FREQUENCY_DEFINITION_RELATIVE                                         0
#define RFMXLTE_VAL_SUBBLOCK_FREQUENCY_DEFINITION_ABSOLUTE                                         1

// Values for RFMXLTE_ATTR_SRS_MAXIMUM_UpPTS_ENABLED
#define RRFMXLTE_VAL_SRS_MAXIMUM_UpPTS_ENABLED_FALSE                                               0
#define RRFMXLTE_VAL_SRS_MAXIMUM_UpPTS_ENABLED_TRUE                                                1

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxLTE_SEMGetStandardMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SEMSetStandardMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_SEMCfgStandardMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 standardMaskType
);

int32 __stdcall RFmxLTE_CalculateFrequencyFromEARFCN(
   int32 linkDirection,
   int32 band,
   int32 EARFCN,
   float64 *centerFrequency
);

int32 __stdcall RFmxLTE_ModAccGetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_ModAccSetMultiCarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_GetSubblockFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxLTE_SetSubblockFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxLTE_CfgSubblockFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 subblockFrequencyDefinition
);

int32 __stdcall RFmxLTE_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxLTE_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxLTE_AnalyzeSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxNR.h sha256=5e4a8703a26449d618d2da99a16921ea470caa6476696ee053c37ab1ad1e7a0b bytes=283660 -->
## FILE: imports/include/niRFmxNR.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxNR.h`
- sha256: `5e4a8703a26449d618d2da99a16921ea470caa6476696ee053c37ab1ad1e7a0b`
- bytes: 283660

````c

/****************************************************************************************************
*          National Instruments RFmx NR
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2021.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxNR.h
*
* Purpose:  National Instruments RFmx NR,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_NR_H__
#define __NI_RFMX_NR_H__

#include "niRFmxInstr.h"

#define RFMXNR_ATTR_SELECTED_PORTS                                                         0x00900ffd
#define RFMXNR_ATTR_CENTER_FREQUENCY                                                       0x00900001
#define RFMXNR_ATTR_REFERENCE_LEVEL                                                        0x00900002
#define RFMXNR_ATTR_EXTERNAL_ATTENUATION                                                   0x00900003
#define RFMXNR_ATTR_REFERENCE_LEVEL_HEADROOM                                               0x00900ffc
#define RFMXNR_ATTR_TRIGGER_TYPE                                                           0x00900004
#define RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                            0x00900005
#define RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                              0x00900006
#define RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                           0x00900007
#define RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                            0x00900008
#define RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                                       0x00900fff
#define RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                            0x00900009
#define RFMXNR_ATTR_TRIGGER_DELAY                                                          0x0090000a
#define RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                        0x0090000b
#define RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                                    0x0090000c
#define RFMXNR_ATTR_LINK_DIRECTION                                                         0x0090000e
#define RFMXNR_ATTR_GNODEB_CATEGORY                                                        0x0090005f
#define RFMXNR_ATTR_GNODEB_TYPE                                                            0x009000a0
#define RFMXNR_ATTR_SATELLITE_ACCESS_NODE_TYPE                                             0x009000a4
#define RFMXNR_ATTR_SATELLITE_ACCESS_NODE_CLASS                                            0x009000a3
#define RFMXNR_ATTR_TRANSMIT_ANTENNA_TO_ANALYZE                                            0x0090009b
#define RFMXNR_ATTR_NUMBER_OF_RECEIVE_CHAINS                                               0x0090d003
#define RFMXNR_ATTR_POWER_CLASS                                                            0x0090009c
#define RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED                                          0x0090009e
#define RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED                                  0x0090001f
#define RFMXNR_ATTR_AUTO_CELL_ID_DETECTION_ENABLED                                         0x0090008c
#define RFMXNR_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE                                    0x0090008e
#define RFMXNR_ATTR_AUTO_INCREMENT_CELL_ID_ENABLED                                         0x0090009f
#define RFMXNR_ATTR_DOWNLINK_TEST_MODEL_CELL_ID_MODE                                       0x0090011e
#define RFMXNR_ATTR_NUMBER_OF_SUBBLOCKS                                                    0x00900010
#define RFMXNR_ATTR_SUBBLOCK_FREQUENCY                                                     0x0090011f
#define RFMXNR_ATTR_SUBBLOCK_TRANSMIT_LO_FREQUENCY                                         0x00900060
#define RFMXNR_ATTR_PHASE_COMPENSATION_FREQUENCY                                           0x00900061
#define RFMXNR_ATTR_FREQUENCY_RANGE                                                        0x00900035
#define RFMXNR_ATTR_BAND                                                                   0x00900012
#define RFMXNR_ATTR_SUBBLOCK_ENDC_NOMINAL_SPACING_ADJUSTMENT                               0x00900103
#define RFMXNR_ATTR_CHANNEL_RASTER                                                         0x00900098
#define RFMXNR_ATTR_COMPONENT_CARRIER_SPACING_TYPE                                         0x00900013
#define RFMXNR_ATTR_COMPONENT_CARRIER_AT_CENTER_FREQUENCY                                  0x00900014
#define RFMXNR_ATTR_NUMBER_OF_COMPONENT_CARRIERS                                           0x00900015
#define RFMXNR_ATTR_DOWNLINK_TEST_MODEL                                                    0x00900100
#define RFMXNR_ATTR_DOWNLINK_TEST_MODEL_MODULATION_TYPE                                    0x0090011d
#define RFMXNR_ATTR_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME                                      0x00900101
#define RFMXNR_ATTR_RATED_TRP                                                              0x009000a1
#define RFMXNR_ATTR_RATED_EIRP                                                             0x009000a2
#define RFMXNR_ATTR_COMPONENT_CARRIER_BANDWIDTH                                            0x00900016
#define RFMXNR_ATTR_COMPONENT_CARRIER_FREQUENCY                                            0x00900017
#define RFMXNR_ATTR_COMPONENT_CARRIER_ALLOCATED                                            0x00900118
#define RFMXNR_ATTR_COMPONENT_CARRIER_RADIO_ACCESS_TYPE                                    0x00900102
#define RFMXNR_ATTR_CELL_ID                                                                0x00900019
#define RFMXNR_ATTR_REFERENCE_GRID_SUBCARRIER_SPACING                                      0x00900062
#define RFMXNR_ATTR_REFERENCE_GRID_START                                                   0x00900063
#define RFMXNR_ATTR_REFERENCE_GRID_SIZE                                                    0x00900119
#define RFMXNR_ATTR_SUB_BAND_ALLOCATION                                                    0x0090003c
#define RFMXNR_ATTR_NUMBER_OF_BANDWIDTH_PARTS                                              0x0090003d
#define RFMXNR_ATTR_BANDWIDTH_PART_SUBCARRIER_SPACING                                      0x0090001b
#define RFMXNR_ATTR_BANDWIDTH_PART_CYCLIC_PREFIX_MODE                                      0x0090001a
#define RFMXNR_ATTR_GRID_START                                                             0x00900096
#define RFMXNR_ATTR_GRID_SIZE                                                              0x0090009a
#define RFMXNR_ATTR_BANDWIDTH_PART_RESOURCE_BLOCK_OFFSET                                   0x0090003e
#define RFMXNR_ATTR_BANDWIDTH_PART_NUMBER_OF_RESOURCE_BLOCKS                               0x0090003f
#define RFMXNR_ATTR_BANDWIDTH_PART_DC_LOCATION_KNOWN                                       0x00900121
#define RFMXNR_ATTR_NUMBER_OF_USERS                                                        0x00900064
#define RFMXNR_ATTR_RNTI                                                                   0x00900065
#define RFMXNR_ATTR_NUMBER_OF_PUSCH_CONFIGURATIONS                                         0x0090004b
#define RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED                                      0x0090001e
#define RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS                                0x00900027
#define RFMXNR_ATTR_PUSCH_RESOURCE_BLOCK_OFFSET                                            0x00900028
#define RFMXNR_ATTR_PUSCH_NUMBER_OF_RESOURCE_BLOCKS                                        0x00900029
#define RFMXNR_ATTR_PUSCH_MODULATION_TYPE                                                  0x00900026
#define RFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSION                                             0x00900116
#define RFMXNR_ATTR_PUSCH_DMRS_ANTENNA_PORTS                                               0x00900041
#define RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE                                                  0x00900051
#define RFMXNR_ATTR_PUSCH_DMRS_POWER                                                       0x00900030
#define RFMXNR_ATTR_PUSCH_DMRS_NUMBER_OF_CDM_GROUPS                                        0x00900042
#define RFMXNR_ATTR_PUSCH_DMRS_SCRAMBLING_ID_MODE                                          0x00900044
#define RFMXNR_ATTR_PUSCH_DMRS_SCRAMBLING_ID                                               0x00900045
#define RFMXNR_ATTR_PUSCH_DMRS_NSCID                                                       0x00900046
#define RFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLED                                       0x00900021
#define RFMXNR_ATTR_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED                                    0x00900022
#define RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID_MODE                                               0x00900047
#define RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID                                                    0x00900048
#define RFMXNR_ATTR_PUSCH_DMRS_CONFIGURATION_TYPE                                          0x00900031
#define RFMXNR_ATTR_PUSCH_MAPPING_TYPE                                                     0x00900034
#define RFMXNR_ATTR_PUSCH_DMRS_TYPE_A_POSITION                                             0x0090004a
#define RFMXNR_ATTR_PUSCH_DMRS_DURATION                                                    0x00900033
#define RFMXNR_ATTR_PUSCH_DMRS_ADDITIONAL_POSITIONS                                        0x00900032
#define RFMXNR_ATTR_PUSCH_PTRS_ENABLED                                                     0x00900055
#define RFMXNR_ATTR_PUSCH_PTRS_ANTENNA_PORTS                                               0x00900056
#define RFMXNR_ATTR_PUSCH_PTRS_POWER_MODE                                                  0x00900057
#define RFMXNR_ATTR_PUSCH_PTRS_POWER                                                       0x00900058
#define RFMXNR_ATTR_NUMBER_OF_PTRS_GROUPS                                                  0x0090005a
#define RFMXNR_ATTR_SAMPLES_PER_PTRS_GROUP                                                 0x0090005b
#define RFMXNR_ATTR_PUSCH_PTRS_TIME_DENSITY                                                0x0090005c
#define RFMXNR_ATTR_PUSCH_PTRS_FREQUENCY_DENSITY                                           0x0090005d
#define RFMXNR_ATTR_PUSCH_PTRS_RE_OFFSET                                                   0x0090005e
#define RFMXNR_ATTR_PUSCH_SLOT_ALLOCATION                                                  0x0090004c
#define RFMXNR_ATTR_PUSCH_SYMBOL_ALLOCATION                                                0x0090004d
#define RFMXNR_ATTR_NUMBER_OF_PDSCH_CONFIGURATIONS                                         0x00900090
#define RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS                                0x00900067
#define RFMXNR_ATTR_PDSCH_RESOURCE_BLOCK_OFFSET                                            0x00900068
#define RFMXNR_ATTR_PDSCH_NUMBER_OF_RESOURCE_BLOCKS                                        0x00900069
#define RFMXNR_ATTR_PDSCH_MODULATION_TYPE                                                  0x0090006a
#define RFMXNR_ATTR_PDSCH_DMRS_RELEASE_VERSION                                             0x00900117
#define RFMXNR_ATTR_PDSCH_DMRS_ANTENNA_PORTS                                               0x0090006b
#define RFMXNR_ATTR_PDSCH_DMRS_POWER_MODE                                                  0x0090006c
#define RFMXNR_ATTR_PDSCH_DMRS_POWER                                                       0x0090006d
#define RFMXNR_ATTR_PDSCH_DMRS_NUMBER_OF_CDM_GROUPS                                        0x0090006e
#define RFMXNR_ATTR_PDSCH_DMRS_SCRAMBLING_ID_MODE                                          0x0090006f
#define RFMXNR_ATTR_PDSCH_DMRS_SCRAMBLING_ID                                               0x00900070
#define RFMXNR_ATTR_PDSCH_DMRS_NSCID                                                       0x00900071
#define RFMXNR_ATTR_PDSCH_DMRS_CONFIGURATION_TYPE                                          0x00900074
#define RFMXNR_ATTR_PDSCH_MAPPING_TYPE                                                     0x00900075
#define RFMXNR_ATTR_PDSCH_DMRS_TYPE_A_POSITION                                             0x00900076
#define RFMXNR_ATTR_PDSCH_DMRS_DURATION                                                    0x00900077
#define RFMXNR_ATTR_PDSCH_DMRS_ADDITIONAL_POSITIONS                                        0x00900078
#define RFMXNR_ATTR_PDSCH_PTRS_ENABLED                                                     0x00900079
#define RFMXNR_ATTR_PDSCH_PTRS_ANTENNA_PORTS                                               0x0090007a
#define RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE                                                  0x0090007b
#define RFMXNR_ATTR_EPRE_RATIO_PORT                                                        0x00900092
#define RFMXNR_ATTR_PDSCH_PTRS_POWER                                                       0x0090007c
#define RFMXNR_ATTR_PDSCH_PTRS_TIME_DENSITY                                                0x0090007d
#define RFMXNR_ATTR_PDSCH_PTRS_FREQUENCY_DENSITY                                           0x0090007e
#define RFMXNR_ATTR_PDSCH_PTRS_RE_OFFSET                                                   0x0090007f
#define RFMXNR_ATTR_PDSCH_SLOT_ALLOCATION                                                  0x00900080
#define RFMXNR_ATTR_PDSCH_SYMBOL_ALLOCATION                                                0x00900081
#define RFMXNR_ATTR_NUMBER_OF_CORESETS                                                     0x00900106
#define RFMXNR_ATTR_CORESET_SYMBOL_OFFSET                                                  0x00900107
#define RFMXNR_ATTR_CORESET_NUMBER_OF_SYMBOLS                                              0x00900108
#define RFMXNR_ATTR_CORESET_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS                              0x00900109
#define RFMXNR_ATTR_CORESET_RESOURCE_BLOCK_OFFSET                                          0x0090010a
#define RFMXNR_ATTR_CORESET_NUMBER_OF_RESOURCE_BLOCKS                                      0x0090010b
#define RFMXNR_ATTR_CORESET_PRECODING_GRANULARITY                                          0x0090010c
#define RFMXNR_ATTR_CORESET_CCE_TO_REG_MAPPING_TYPE                                        0x0090010d
#define RFMXNR_ATTR_CORESET_REG_BUNDLE_SIZE                                                0x0090010e
#define RFMXNR_ATTR_CORESET_INTERLEAVER_SIZE                                               0x0090010f
#define RFMXNR_ATTR_CORESET_SHIFT_INDEX                                                    0x00900110
#define RFMXNR_ATTR_NUMBER_OF_PDCCH_CONFIGURATIONS                                         0x00900112
#define RFMXNR_ATTR_PDCCH_CCE_AGGREGATION_LEVEL                                            0x00900113
#define RFMXNR_ATTR_PDCCH_CCE_OFFSET                                                       0x00900114
#define RFMXNR_ATTR_PDCCH_SLOT_ALLOCATION                                                  0x00900115
#define RFMXNR_ATTR_SSB_ENABLED                                                            0x00900082
#define RFMXNR_ATTR_SSB_GRID_START                                                         0x0090011a
#define RFMXNR_ATTR_SSB_GRID_SIZE                                                          0x0090011b
#define RFMXNR_ATTR_SSB_CRB_OFFSET                                                         0x00900083
#define RFMXNR_ATTR_SUBCARRIER_SPACING_COMMON                                              0x00900099
#define RFMXNR_ATTR_SSB_SUBCARRIER_OFFSET                                                  0x00900084
#define RFMXNR_ATTR_SSB_PERIODICITY                                                        0x00900094
#define RFMXNR_ATTR_SSB_PATTERN                                                            0x00900085
#define RFMXNR_ATTR_SSB_ACTIVE_BLOCKS                                                      0x00900095
#define RFMXNR_ATTR_PSS_POWER                                                              0x00900086
#define RFMXNR_ATTR_SSS_POWER                                                              0x00900087
#define RFMXNR_ATTR_PBCH_POWER                                                             0x00900088
#define RFMXNR_ATTR_PBCH_DMRS_POWER                                                        0x00900089
#define RFMXNR_ATTR_SSB_HRF_INDEX                                                          0x00900120
#define RFMXNR_ATTR_NUMBER_OF_STEPS                                                        0x00900ff8
#define RFMXNR_ATTR_LIST_STEP_TIMER_UNIT                                                   0x00900ff6
#define RFMXNR_ATTR_LIST_STEP_TIMER_DURATION                                               0x00900ff9
#define RFMXNR_ATTR_LIST_STEP_TIMER_OFFSET                                                 0x00900ff7
#define RFMXNR_ATTR_MODACC_MEASUREMENT_ENABLED                                             0x00904000
#define RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED                                     0x00904002
#define RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE                                            0x00904004
#define RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT                                         0x00904005
#define RFMXNR_ATTR_MODACC_MEASUREMENT_OFFSET                                              0x00904006
#define RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH                                              0x00904007
#define RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION                                      0x00904071
#define RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED                           0x00904075
#define RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_MODEL                                            0x00904082
#define RFMXNR_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED                             0x00904076
#define RFMXNR_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED                                  0x00904077
#define RFMXNR_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED                            0x00904083
#define RFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED                          0x00904084
#define RFMXNR_ATTR_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED                               0x00904085
#define RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED                           0x00904086
#define RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED                               0x00904078
#define RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE                                 0x00904081
#define RFMXNR_ATTR_MODACC_SPECTRUM_INVERTED                                               0x00904008
#define RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE                                         0x00904009
#define RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE                                             0x00904051
#define RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE                                            0x00904052
#define RFMXNR_ATTR_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL                               0x009040a0
#define RFMXNR_ATTR_MODACC_EVM_UNIT                                                        0x0090400a
#define RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE                                                 0x0090400b
#define RFMXNR_ATTR_MODACC_FFT_WINDOW_OFFSET                                               0x0090400c
#define RFMXNR_ATTR_MODACC_FFT_WINDOW_LENGTH                                               0x0090400d
#define RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED                                   0x0090002f
#define RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED                                     0x0090400e
#define RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION                                     0x00904010
#define RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED                                      0x00904092
#define RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED                    0x00904093
#define RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_REFERENCE_LEVEL_COERCION_LIMIT               0x00904094
#define RFMXNR_ATTR_MODACC_MEASUREMENT_MODE                                                0x00904095
#define RFMXNR_ATTR_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS                                  0x00900038
#define RFMXNR_ATTR_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS                                  0x00900039
#define RFMXNR_ATTR_MODACC_AVERAGING_ENABLED                                               0x00904011
#define RFMXNR_ATTR_MODACC_AVERAGING_COUNT                                                 0x00904012
#define RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW                                       0x00904097
#define RFMXNR_ATTR_MODACC_SHORT_FRAME_ENABLED                                             0x0090409d
#define RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH                                              0x0090409e
#define RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH_UNIT                                         0x0090409f
#define RFMXNR_ATTR_MODACC_TRANSIENT_PERIOD_EVM_MODE                                       0x009040a3
#define RFMXNR_ATTR_MODACC_TRANSIENT_PERIOD                                                0x009040a4
#define RFMXNR_ATTR_MODACC_TRANSIENT_POWER_CHANGE_THRESHOLD                                0x009040a5
#define RFMXNR_ATTR_MODACC_ALL_TRACES_ENABLED                                              0x00904013
#define RFMXNR_ATTR_MODACC_NUMBER_OF_ANALYSIS_THREADS                                      0x00904014
#define RFMXNR_ATTR_MODACC_RESULTS_DETECTED_CELL_ID                                        0x0090403a
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN                                  0x00904016
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_MAXIMUM                              0x00904017
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_BWP_INDEX                            0x00904054
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX                           0x0090401c
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX                         0x0090401d
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_EVM_SUBCARRIER_INDEX                     0x0090401e
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_RMS_MAGNITUDE_ERROR_MEAN                      0x00904018
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_MAGNITUDE_ERROR_MAXIMUM                  0x00904019
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_RMS_PHASE_ERROR_MEAN                          0x0090401a
#define RFMXNR_ATTR_MODACC_RESULTS_COMPOSITE_PEAK_PHASE_ERROR_MAXIMUM                      0x0090401b
#define RFMXNR_ATTR_MODACC_RESULTS_SCH_SYMBOL_POWER_MEAN                                   0x0090406f
#define RFMXNR_ATTR_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE                            0x00904070
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN                                 0x0090401f
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM                             0x00904020
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN                                 0x00904023
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM                             0x00904024
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RMS_EVM_MEAN                                 0x00904048
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_PEAK_EVM_MAXIMUM                             0x00904049
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN                                0x009040a9
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN                                0x009040aa
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN                                0x009040ab
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN                       0x009040a6
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM                         0x009040a7
#define RFMXNR_ATTR_MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX                      0x009040a8
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN                                 0x00904055
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_16QAM_RMS_EVM_MEAN                                0x00904056
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN                                0x00904057
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_256QAM_RMS_EVM_MEAN                               0x00904058
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_1024QAM_RMS_EVM_MEAN                              0x00904073
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN                              0x009040b2
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_8PSK_RMS_EVM_MEAN                                 0x00904091
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN                                 0x00904059
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_PEAK_EVM_MAXIMUM                             0x0090405a
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DMRS_RMS_EVM_MEAN                                 0x0090405b
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DMRS_PEAK_EVM_MAXIMUM                             0x0090405c
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_PTRS_RMS_EVM_MEAN                                 0x0090405d
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_PTRS_PEAK_EVM_MAXIMUM                             0x0090405e
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DATA_RE_POWER_MEAN                                0x009040ac
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_DMRS_RE_POWER_MEAN                                0x009040ad
#define RFMXNR_ATTR_MODACC_RESULTS_PDSCH_PTRS_RE_POWER_MEAN                                0x009040ae
#define RFMXNR_ATTR_MODACC_RESULTS_PSS_RMS_EVM_MEAN                                        0x00904079
#define RFMXNR_ATTR_MODACC_RESULTS_PSS_PEAK_EVM_MAXIMUM                                    0x0090407a
#define RFMXNR_ATTR_MODACC_RESULTS_SSS_RMS_EVM_MEAN                                        0x0090407b
#define RFMXNR_ATTR_MODACC_RESULTS_SSS_PEAK_EVM_MAXIMUM                                    0x0090407c
#define RFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_RMS_EVM_MEAN                                  0x0090407d
#define RFMXNR_ATTR_MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM                              0x0090407e
#define RFMXNR_ATTR_MODACC_RESULTS_PBCH_DMRS_RMS_EVM_MEAN                                  0x0090407f
#define RFMXNR_ATTR_MODACC_RESULTS_PBCH_DMRS_PEAK_EVM_MAXIMUM                              0x00904080
#define RFMXNR_ATTR_MODACC_RESULTS_IN_BAND_EMISSION_MARGIN                                 0x00904027
#define RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN                        0x0090402c
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX                     0x00904088
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM      0x00904028
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM      0x00904029
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM      0x0090402a
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM      0x0090402b
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM                        0x00904089
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM                        0x0090408a
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM                        0x0090408b
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM                        0x0090408c
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX       0x0090408d
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM_SUBCARRIER_INDEX       0x0090408e
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_SUBCARRIER_INDEX       0x0090408f
#define RFMXNR_ATTR_MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM_SUBCARRIER_INDEX       0x00904090
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN                      0x00904032
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_FREQUENCY_ERROR_MEAN                  0x0090402d
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_FREQUENCY_ERROR_MAXIMUM          0x009040a1
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN               0x00904033
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN             0x009040b0
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_IQ_ORIGIN_OFFSET_MEAN                 0x0090402e
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_SLOT_IQ_ORIGIN_OFFSET_MAXIMUM         0x009040a2
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_IQ_GAIN_IMBALANCE_MEAN                0x0090402f
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN                 0x00904030
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_IQ_TIMING_SKEW_MEAN                   0x00904031
#define RFMXNR_ATTR_MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN                      0x009040af
#define RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX                     0x00904062
#define RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX                            0x00904063
#define RFMXNR_ATTR_MODACC_RESULTS_SUBBLOCK_IQ_ORIGIN_OFFSET_MEAN                          0x00904036
#define RFMXNR_ATTR_MODACC_RESULTS_NOISE_COMPENSATION_APPLIED                              0x00904096
#define RFMXNR_ATTR_ACP_MEASUREMENT_ENABLED                                                0x00901000
#define RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE                                         0x0090104d
#define RFMXNR_ATTR_ACP_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x00901002
#define RFMXNR_ATTR_ACP_SUBBLOCK_OFFSET                                                    0x0090104e
#define RFMXNR_ATTR_ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00901006
#define RFMXNR_ATTR_ACP_NUMBER_OF_UTRA_OFFSETS                                             0x00901009
#define RFMXNR_ATTR_ACP_NUMBER_OF_EUTRA_OFFSETS                                            0x0090100a
#define RFMXNR_ATTR_ACP_NUMBER_OF_NR_OFFSETS                                               0x0090100b
#define RFMXNR_ATTR_ACP_NUMBER_OF_ENDC_OFFSETS                                             0x00901043
#define RFMXNR_ATTR_ACP_OFFSET_CHANNEL_SPACING_ADJUSTMENT                                  0x00901045
#define RFMXNR_ATTR_ACP_NUMBER_OF_OFFSETS                                                  0x0090100c
#define RFMXNR_ATTR_ACP_OFFSET_FREQUENCY                                                   0x0090100e
#define RFMXNR_ATTR_ACP_OFFSET_SIDEBAND                                                    0x0090100f
#define RFMXNR_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH                                       0x00901012
#define RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH                                          0x00901016
#define RFMXNR_ATTR_ACP_RBW_FILTER_BANDWIDTH                                               0x00901017
#define RFMXNR_ATTR_ACP_RBW_FILTER_TYPE                                                    0x00901018
#define RFMXNR_ATTR_ACP_SWEEP_TIME_AUTO                                                    0x00901019
#define RFMXNR_ATTR_ACP_SWEEP_TIME_INTERVAL                                                0x0090101a
#define RFMXNR_ATTR_ACP_POWER_UNITS                                                        0x0090101b
#define RFMXNR_ATTR_ACP_MEASUREMENT_METHOD                                                 0x0090101c
#define RFMXNR_ATTR_ACP_NOISE_CALIBRATION_MODE                                             0x0090104c
#define RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO                                   0x0090104b
#define RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT                                  0x0090104a
#define RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED                                         0x0090101d
#define RFMXNR_ATTR_ACP_NOISE_COMPENSATION_TYPE                                            0x00901049
#define RFMXNR_ATTR_ACP_AVERAGING_ENABLED                                                  0x0090101e
#define RFMXNR_ATTR_ACP_AVERAGING_COUNT                                                    0x0090101f
#define RFMXNR_ATTR_ACP_AVERAGING_TYPE                                                     0x00901021
#define RFMXNR_ATTR_ACP_MEASUREMENT_MODE                                                   0x00901048
#define RFMXNR_ATTR_ACP_FFT_WINDOW                                                         0x00901022
#define RFMXNR_ATTR_ACP_FFT_OVERLAP_MODE                                                   0x00901046
#define RFMXNR_ATTR_ACP_FFT_OVERLAP                                                        0x00901047
#define RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO                                        0x00901024
#define RFMXNR_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET                                        0x00901025
#define RFMXNR_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET                                         0x00901026
#define RFMXNR_ATTR_ACP_SEQUENTIAL_FFT_SIZE                                                0x00901027
#define RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE                                          0x00901028
#define RFMXNR_ATTR_ACP_ALL_TRACES_ENABLED                                                 0x00901029
#define RFMXNR_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                                         0x0090102a
#define RFMXNR_ATTR_ACP_RESULTS_TOTAL_AGGREGATED_POWER                                     0x0090102c
#define RFMXNR_ATTR_ACP_RESULTS_SUBBLOCK_POWER                                             0x00901030
#define RFMXNR_ATTR_ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER                           0x00901033
#define RFMXNR_ATTR_ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER                           0x00901034
#define RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                                0x0090103a
#define RFMXNR_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                                0x0090103b
#define RFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                                0x00901041
#define RFMXNR_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                                0x00901042
#define RFMXNR_ATTR_CHP_MEASUREMENT_ENABLED                                                0x00903000
#define RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO                                                    0x00903002
#define RFMXNR_ATTR_CHP_SWEEP_TIME_INTERVAL                                                0x00903003
#define RFMXNR_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE                                         0x00903004
#define RFMXNR_ATTR_CHP_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x00903005
#define RFMXNR_ATTR_CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00903006
#define RFMXNR_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH                                          0x00903009
#define RFMXNR_ATTR_CHP_RBW_FILTER_BANDWIDTH                                               0x0090300a
#define RFMXNR_ATTR_CHP_RBW_FILTER_TYPE                                                    0x0090300b
#define RFMXNR_ATTR_CHP_NOISE_CALIBRATION_MODE                                             0x00903026
#define RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO                                   0x00903025
#define RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_COUNT                                  0x00903024
#define RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED                                         0x00903022
#define RFMXNR_ATTR_CHP_NOISE_COMPENSATION_TYPE                                            0x00903023
#define RFMXNR_ATTR_CHP_AVERAGING_ENABLED                                                  0x0090300d
#define RFMXNR_ATTR_CHP_AVERAGING_COUNT                                                    0x0090300e
#define RFMXNR_ATTR_CHP_AVERAGING_TYPE                                                     0x00903010
#define RFMXNR_ATTR_CHP_MEASUREMENT_MODE                                                   0x00903021
#define RFMXNR_ATTR_CHP_FFT_WINDOW                                                         0x00903011
#define RFMXNR_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE                                          0x00903012
#define RFMXNR_ATTR_CHP_ALL_TRACES_ENABLED                                                 0x00903013
#define RFMXNR_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS                                         0x00903014
#define RFMXNR_ATTR_CHP_RESULTS_TOTAL_AGGREGATED_POWER                                     0x00903016
#define RFMXNR_ATTR_CHP_RESULTS_SUBBLOCK_POWER                                             0x0090301a
#define RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER                           0x0090301d
#define RFMXNR_ATTR_CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER                           0x0090301f
#define RFMXNR_ATTR_OBW_MEASUREMENT_ENABLED                                                0x00906000
#define RFMXNR_ATTR_OBW_POWER_INTEGRATION_METHOD                                           0x00906020
#define RFMXNR_ATTR_OBW_SPAN_AUTO                                                          0x0090601a
#define RFMXNR_ATTR_OBW_SPAN                                                               0x00906003
#define RFMXNR_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH                                          0x00906006
#define RFMXNR_ATTR_OBW_RBW_FILTER_BANDWIDTH                                               0x00906007
#define RFMXNR_ATTR_OBW_RBW_FILTER_TYPE                                                    0x00906008
#define RFMXNR_ATTR_OBW_SWEEP_TIME_AUTO                                                    0x00906009
#define RFMXNR_ATTR_OBW_SWEEP_TIME_INTERVAL                                                0x0090600a
#define RFMXNR_ATTR_OBW_AVERAGING_ENABLED                                                  0x0090600b
#define RFMXNR_ATTR_OBW_AVERAGING_COUNT                                                    0x0090600c
#define RFMXNR_ATTR_OBW_AVERAGING_TYPE                                                     0x0090600e
#define RFMXNR_ATTR_OBW_FFT_WINDOW                                                         0x0090600f
#define RFMXNR_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE                                          0x00906011
#define RFMXNR_ATTR_OBW_ALL_TRACES_ENABLED                                                 0x00906012
#define RFMXNR_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS                                         0x00906013
#define RFMXNR_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH                                         0x00906015
#define RFMXNR_ATTR_OBW_RESULTS_ABSOLUTE_POWER                                             0x00906016
#define RFMXNR_ATTR_OBW_RESULTS_START_FREQUENCY                                            0x00906017
#define RFMXNR_ATTR_OBW_RESULTS_STOP_FREQUENCY                                             0x00906018
#define RFMXNR_ATTR_SEM_MEASUREMENT_ENABLED                                                0x00908000
#define RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE                                                   0x00908002
#define RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE                                                 0x00908038
#define RFMXNR_ATTR_SEM_DELTA_F_MAXIMUM                                                    0x00908039
#define RFMXNR_ATTR_SEM_SUBBLOCK_INTEGRATION_BANDWIDTH                                     0x00908003
#define RFMXNR_ATTR_SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH                              0x00908004
#define RFMXNR_ATTR_SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH                            0x00908005
#define RFMXNR_ATTR_SEM_COMPONENT_CARRIER_RATED_OUTPUT_POWER                               0x0090803a
#define RFMXNR_ATTR_SEM_NUMBER_OF_OFFSETS                                                  0x00908006
#define RFMXNR_ATTR_SEM_OFFSET_START_FREQUENCY                                             0x00908007
#define RFMXNR_ATTR_SEM_OFFSET_STOP_FREQUENCY                                              0x00908008
#define RFMXNR_ATTR_SEM_OFFSET_SIDEBAND                                                    0x00908009
#define RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH                                        0x0090800a
#define RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_TYPE                                             0x0090800b
#define RFMXNR_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL                                          0x0090800c
#define RFMXNR_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK                                             0x0090800d
#define RFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION                                        0x00908042
#define RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_START                                        0x0090800e
#define RFMXNR_ATTR_SEM_OFFSET_ABSOLUTE_LIMIT_STOP                                         0x0090800f
#define RFMXNR_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START                                        0x00908010
#define RFMXNR_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP                                         0x00908011
#define RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO                                                    0x00908012
#define RFMXNR_ATTR_SEM_SWEEP_TIME_INTERVAL                                                0x00908013
#define RFMXNR_ATTR_SEM_AVERAGING_ENABLED                                                  0x00908014
#define RFMXNR_ATTR_SEM_AVERAGING_COUNT                                                    0x00908015
#define RFMXNR_ATTR_SEM_AVERAGING_TYPE                                                     0x00908016
#define RFMXNR_ATTR_SEM_FFT_WINDOW                                                         0x00908040
#define RFMXNR_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE                                          0x00908017
#define RFMXNR_ATTR_SEM_ALL_TRACES_ENABLED                                                 0x00908018
#define RFMXNR_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                                         0x00908019
#define RFMXNR_ATTR_SEM_RESULTS_TOTAL_AGGREGATED_POWER                                     0x0090801b
#define RFMXNR_ATTR_SEM_RESULTS_MEASUREMENT_STATUS                                         0x0090801c
#define RFMXNR_ATTR_SEM_RESULTS_SUBBLOCK_POWER                                             0x0090801f
#define RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER                0x00908020
#define RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER                0x00908021
#define RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER                      0x00908022
#define RFMXNR_ATTR_SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY                           0x00908023
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS                            0x00908024
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER                     0x00908025
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER                     0x00908026
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER                           0x00908027
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER                           0x00908028
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                                0x00908029
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                                        0x0090802a
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER                         0x0090802b
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER                         0x0090802c
#define RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY                              0x0090802d
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS                            0x0090802e
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER                     0x0090802f
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER                     0x00908030
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER                           0x00908031
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER                           0x00908032
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                                0x00908033
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                                        0x00908034
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER                         0x00908035
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER                         0x00908036
#define RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY                              0x00908037
#define RFMXNR_ATTR_TXP_MEASUREMENT_ENABLED                                                0x00907000
#define RFMXNR_ATTR_TXP_MEASUREMENT_OFFSET                                                 0x00907002
#define RFMXNR_ATTR_TXP_MEASUREMENT_INTERVAL                                               0x00907003
#define RFMXNR_ATTR_TXP_AVERAGING_ENABLED                                                  0x00907004
#define RFMXNR_ATTR_TXP_AVERAGING_COUNT                                                    0x00907005
#define RFMXNR_ATTR_TXP_ALL_TRACES_ENABLED                                                 0x00907007
#define RFMXNR_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS                                         0x00907008
#define RFMXNR_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN                                         0x0090700a
#define RFMXNR_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM                                         0x0090700b
#define RFMXNR_ATTR_PVT_MEASUREMENT_ENABLED                                                0x00909000
#define RFMXNR_ATTR_PVT_MEASUREMENT_INTERVAL_AUTO                                          0x00909014
#define RFMXNR_ATTR_PVT_MEASUREMENT_INTERVAL                                               0x00909015
#define RFMXNR_ATTR_PVT_MEASUREMENT_METHOD                                                 0x00909002
#define RFMXNR_ATTR_PVT_AVERAGING_ENABLED                                                  0x00909003
#define RFMXNR_ATTR_PVT_AVERAGING_COUNT                                                    0x00909004
#define RFMXNR_ATTR_PVT_AVERAGING_TYPE                                                     0x00909005
#define RFMXNR_ATTR_PVT_OFF_POWER_EXCLUSION_BEFORE                                         0x00909007
#define RFMXNR_ATTR_PVT_OFF_POWER_EXCLUSION_AFTER                                          0x00909008
#define RFMXNR_ATTR_PVT_ALL_TRACES_ENABLED                                                 0x00909009
#define RFMXNR_ATTR_PVT_NUMBER_OF_ANALYSIS_THREADS                                         0x0090900b
#define RFMXNR_ATTR_PVT_RESULTS_MEASUREMENT_STATUS                                         0x0090900c
#define RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_BEFORE                                  0x0090900d
#define RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_OFF_POWER_AFTER                                   0x0090900e
#define RFMXNR_ATTR_PVT_RESULTS_ABSOLUTE_ON_POWER                                          0x0090900f
#define RFMXNR_ATTR_PVT_RESULTS_BURST_WIDTH                                                0x00909010
#define RFMXNR_ATTR_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER                                    0x00909016
#define RFMXNR_ATTR_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_MARGIN                             0x00909017
#define RFMXNR_ATTR_PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_TIME                               0x00909018
#define RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED                             0x0090d001
#define RFMXNR_ATTR_TRANSMITTER_ARCHITECTURE                                               0x0090043b
#define RFMXNR_ATTR_PHASE_COMPENSATION                                                     0x0090043d
#define RFMXNR_ATTR_REFERENCE_GRID_ALIGNMENT_MODE                                          0x00900037
#define RFMXNR_ATTR_GRID_SIZE_MODE                                                         0x0090011c
#define RFMXNR_ATTR_LIMITED_CONFIGURATION_CHANGE                                           0x0090d002
#define RFMXNR_ATTR_RESULT_FETCH_TIMEOUT                                                   0x0090c000

// Values for RFMXNR_ATTR_TRIGGER_TYPE
#define RFMXNR_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXNR_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXNR_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXNR_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXNR_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXNR_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXNR_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXNR_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXNR_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXNR_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXNR_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXNR_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXNR_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXNR_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXNR_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXNR_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXNR_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXNR_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXNR_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXNR_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXNR_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXNR_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXNR_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXNR_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXNR_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXNR_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXNR_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXNR_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXNR_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXNR_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXNR_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXNR_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXNR_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXNR_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXNR_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXNR_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXNR_ATTR_LINK_DIRECTION
#define RFMXNR_VAL_LINK_DIRECTION_DOWNLINK                                                        0
#define RFMXNR_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for RFMXNR_ATTR_GNODEB_CATEGORY
#define RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_A                              0
#define RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1                      1
#define RFMXNR_VAL_GNODEB_CATEGORY_WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2                      2
#define RFMXNR_VAL_GNODEB_CATEGORY_LOCAL_AREA_BASE_STATION                                        3
#define RFMXNR_VAL_GNODEB_CATEGORY_MEDIUM_RANGE_BASE_STATION                                      5
#define RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_A                                                 6
#define RFMXNR_VAL_GNODEB_CATEGORY_FR2_CATEGORY_B                                                 7

// Values for RFMXNR_ATTR_GNODEB_TYPE
#define RFMXNR_VAL_GNODEB_TYPE_1C                                                                 0
#define RFMXNR_VAL_GNODEB_TYPE_1H                                                                 1
#define RFMXNR_VAL_GNODEB_TYPE_1O                                                                 2
#define RFMXNR_VAL_GNODEB_TYPE_2O                                                                 3

// Values for RFMXNR_ATTR_SATELLITE_ACCESS_NODE_TYPE
#define RFMXNR_VAL_SATELLITE_ACCESS_NODE_TYPE_1H                                                  0
#define RFMXNR_VAL_SATELLITE_ACCESS_NODE_TYPE_1O                                                  1
#define RFMXNR_VAL_SATELLITE_ACCESS_NODE_TYPE_2O                                                  2

// Values for RFMXNR_ATTR_SATELLITE_ACCESS_NODE_CLASS
#define RFMXNR_VAL_SATELLITE_ACCESS_NODE_CLASS_GEO                                                0
#define RFMXNR_VAL_SATELLITE_ACCESS_NODE_CLASS_LEO                                                1

// Values for RFMXNR_ATTR_PIBY2BPSK_POWER_BOOST_ENABLED
#define RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_FALSE                                            0
#define RFMXNR_VAL_PIBY2BPSK_POWER_BOOST_ENABLED_TRUE                                             1

// Values for RFMXNR_ATTR_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED
#define RFMXNR_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_FALSE                                    0
#define RFMXNR_VAL_AUTO_RESOURCE_BLOCK_DETECTION_ENABLED_TRUE                                     1

// Values for RFMXNR_ATTR_AUTO_CELL_ID_DETECTION_ENABLED
#define RFMXNR_VAL_AUTO_CELL_ID_DETECTION_ENABLED_FALSE                                           0
#define RFMXNR_VAL_AUTO_CELL_ID_DETECTION_ENABLED_TRUE                                            1

// Values for RFMXNR_ATTR_DOWNLINK_CHANNEL_CONFIGURATION_MODE
#define RFMXNR_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                               1
#define RFMXNR_VAL_DOWNLINK_CHANNEL_CONFIGURATION_MODE_TEST_MODEL                                 2

// Values for RFMXNR_ATTR_AUTO_INCREMENT_CELL_ID_ENABLED
#define RFMXNR_VAL_AUTO_INCREMENT_CELL_ID_ENABLED_FALSE                                           0
#define RFMXNR_VAL_AUTO_INCREMENT_CELL_ID_ENABLED_TRUE                                            1

// Values for RFMXNR_ATTR_DOWNLINK_TEST_MODEL_CELL_ID_MODE
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_CELL_ID_MODE_AUTO                                          0
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_CELL_ID_MODE_MANUAL                                        1

// Values for RFMXNR_ATTR_FREQUENCY_RANGE
#define RFMXNR_VAL_FREQUENCY_RANGE_RANGE1                                                         0
#define RFMXNR_VAL_FREQUENCY_RANGE_RANGE2_1                                                       1
#define RFMXNR_VAL_FREQUENCY_RANGE_RANGE2_2                                                       2

// Values for RFMXNR_ATTR_COMPONENT_CARRIER_SPACING_TYPE
#define RFMXNR_VAL_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL                                         0
#define RFMXNR_VAL_COMPONENT_CARRIER_SPACING_TYPE_USER                                            2

// Values for RFMXNR_ATTR_DOWNLINK_TEST_MODEL
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM1_1                                                      0
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM1_2                                                      1
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM2                                                        2
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM2A                                                       3
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM3_1                                                      4
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM3_1A                                                     5
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM3_2                                                      6
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM3_3                                                      7
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM2B                                                       8
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_TM3_1B                                                     9

// Values for RFMXNR_ATTR_DOWNLINK_TEST_MODEL_MODULATION_TYPE
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_MODULATION_TYPE_STANDARD                                   0
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QPSK                                       1
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QAM16                                      2
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_MODULATION_TYPE_QAM64                                      3

// Values for RFMXNR_ATTR_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME_FDD                                          0
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_DUPLEX_SCHEME_TDD                                          1

// Values for RFMXNR_ATTR_COMPONENT_CARRIER_ALLOCATED
#define RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_FALSE                                              0
#define RFMXNR_VAL_COMPONENT_CARRIER_ALLOCATED_TRUE                                               1

// Values for RFMXNR_ATTR_COMPONENT_CARRIER_RADIO_ACCESS_TYPE
#define RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_NR                                         0
#define RFMXNR_VAL_COMPONENT_CARRIER_RADIO_ACCESS_TYPE_EUTRA                                      1

// Values for RFMXNR_ATTR_BANDWIDTH_PART_CYCLIC_PREFIX_MODE
#define RFMXNR_VAL_BANDWIDTH_PART_CYCLIC_PREFIX_MODE_NORMAL                                       0
#define RFMXNR_VAL_BANDWIDTH_PART_CYCLIC_PREFIX_MODE_EXTENDED                                     1

// Values for RFMXNR_ATTR_BANDWIDTH_PART_DC_LOCATION_KNOWN
#define RFMXNR_VAL_BANDWIDTH_PART_DC_LOCATION_KNOWN_FALSE                                         0
#define RFMXNR_VAL_BANDWIDTH_PART_DC_LOCATION_KNOWN_TRUE                                          1

// Values for RFMXNR_ATTR_PUSCH_TRANSFORM_PRECODING_ENABLED
#define RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_FALSE                                        0
#define RFMXNR_VAL_PUSCH_TRANSFORM_PRECODING_ENABLED_TRUE                                         1

// Values for RFMXNR_ATTR_PUSCH_MODULATION_TYPE
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_PI_BY_2_BPSK                                             0
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QPSK                                                     1
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QAM16                                                    2
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QAM64                                                    3
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QAM256                                                   4
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QAM1024                                                  5
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_PSK8                                                     100
#define RFMXNR_VAL_PUSCH_MODULATION_TYPE_QAM4096                                                  6

// Values for RFMXNR_ATTR_PUSCH_DMRS_RELEASE_VERSION
#define RFMXNR_VAL_PUSCH_DMRS_RELEASE_VERSION_RELEASE15                                           0
#define RFMXNR_VAL_PUSCH_DMRS_RELEASE_VERSION_RELEASE16                                           1

// Values for RFMXNR_ATTR_PUSCH_DMRS_POWER_MODE
#define RFMXNR_VAL_PUSCH_DMRS_POWER_MODE_CDM_GROUPS                                               0
#define RFMXNR_VAL_PUSCH_DMRS_POWER_MODE_USER_DEFINED                                             1

// Values for RFMXNR_ATTR_PUSCH_DMRS_SCRAMBLING_ID_MODE
#define RFMXNR_VAL_PUSCH_DMRS_SCRAMBLING_ID_MODE_CELL_ID                                          0
#define RFMXNR_VAL_PUSCH_DMRS_SCRAMBLING_ID_MODE_USER_DEFINED                                     1

// Values for RFMXNR_ATTR_PUSCH_DMRS_GROUP_HOPPING_ENABLED
#define RFMXNR_VAL_PUSCH_DMRS_GROUP_HOPPING_ENABLED_FALSE                                         0
#define RFMXNR_VAL_PUSCH_DMRS_GROUP_HOPPING_ENABLED_TRUE                                          1

// Values for RFMXNR_ATTR_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED
#define RFMXNR_VAL_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED_FALSE                                      0
#define RFMXNR_VAL_PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED_TRUE                                       1

// Values for RFMXNR_ATTR_PUSCH_DMRS_PUSCH_ID_MODE
#define RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_CELL_ID                                               0
#define RFMXNR_VAL_PUSCH_DMRS_PUSCH_ID_MODE_USER_DEFINED                                          1

// Values for RFMXNR_ATTR_PUSCH_DMRS_CONFIGURATION_TYPE
#define RFMXNR_VAL_PUSCH_DMRS_CONFIGURATION_TYPE_TYPE1                                            0
#define RFMXNR_VAL_PUSCH_DMRS_CONFIGURATION_TYPE_TYPE2                                            1

// Values for RFMXNR_ATTR_PUSCH_MAPPING_TYPE
#define RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_A                                                      0
#define RFMXNR_VAL_PUSCH_MAPPING_TYPE_TYPE_B                                                      1

// Values for RFMXNR_ATTR_PUSCH_DMRS_DURATION
#define RFMXNR_VAL_PUSCH_DMRS_DURATION_SINGLE_SYMBOL                                              1
#define RFMXNR_VAL_PUSCH_DMRS_DURATION_DOUBLE_SYMBOL                                              2

// Values for RFMXNR_ATTR_PUSCH_PTRS_ENABLED
#define RFMXNR_VAL_PUSCH_PTRS_ENABLED_FALSE                                                       0
#define RFMXNR_VAL_PUSCH_PTRS_ENABLED_TRUE                                                        1

// Values for RFMXNR_ATTR_PUSCH_PTRS_POWER_MODE
#define RFMXNR_VAL_PUSCH_PTRS_POWER_MODE_STANDARD                                                 0
#define RFMXNR_VAL_PUSCH_PTRS_POWER_MODE_USER_DEFINED                                             1

// Values for RFMXNR_ATTR_PDSCH_MODULATION_TYPE
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QPSK                                                     1
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QAM16                                                    2
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QAM64                                                    3
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QAM256                                                   4
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QAM1024                                                  5
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_PSK8                                                     100
#define RFMXNR_VAL_PDSCH_MODULATION_TYPE_QAM4096                                                  6

// Values for RFMXNR_ATTR_PDSCH_DMRS_RELEASE_VERSION
#define RFMXNR_VAL_PDSCH_DMRS_RELEASE_VERSION_RELEASE15                                           0
#define RFMXNR_VAL_PDSCH_DMRS_RELEASE_VERSION_RELEASE16                                           1

// Values for RFMXNR_ATTR_PDSCH_DMRS_POWER_MODE
#define RFMXNR_VAL_PDSCH_DMRS_POWER_MODE_CDM_GROUPS                                               0
#define RFMXNR_VAL_PDSCH_DMRS_POWER_MODE_USER_DEFINED                                             1

// Values for RFMXNR_ATTR_PDSCH_DMRS_SCRAMBLING_ID_MODE
#define RFMXNR_VAL_PDSCH_DMRS_SCRAMBLING_ID_MODE_CELL_ID                                          0
#define RFMXNR_VAL_PDSCH_DMRS_SCRAMBLING_ID_MODE_USER_DEFINED                                     1

// Values for RFMXNR_ATTR_PDSCH_DMRS_CONFIGURATION_TYPE
#define RFMXNR_VAL_PDSCH_DMRS_CONFIGURATION_TYPE_TYPE1                                            0
#define RFMXNR_VAL_PDSCH_DMRS_CONFIGURATION_TYPE_TYPE2                                            1

// Values for RFMXNR_ATTR_PDSCH_MAPPING_TYPE
#define RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_A                                                      0
#define RFMXNR_VAL_PDSCH_MAPPING_TYPE_TYPE_B                                                      1

// Values for RFMXNR_ATTR_PDSCH_DMRS_DURATION
#define RFMXNR_VAL_PDSCH_DMRS_DURATION_SINGLE_SYMBOL                                              1
#define RFMXNR_VAL_PDSCH_DMRS_DURATION_DOUBLE_SYMBOL                                              2

// Values for RFMXNR_ATTR_PDSCH_PTRS_ENABLED
#define RFMXNR_VAL_PDSCH_PTRS_ENABLED_FALSE                                                       0
#define RFMXNR_VAL_PDSCH_PTRS_ENABLED_TRUE                                                        1

// Values for RFMXNR_ATTR_PDSCH_PTRS_POWER_MODE
#define RFMXNR_VAL_PDSCH_PTRS_POWER_MODE_STANDARD                                                 0
#define RFMXNR_VAL_PDSCH_PTRS_POWER_MODE_USER_DEFINED                                             1

// Values for RFMXNR_ATTR_CORESET_PRECODING_GRANULARITY
#define RFMXNR_VAL_CORESET_PRECODING_GRANULARITY_SAME_AS_REG_BUNDLE                               0
#define RFMXNR_VAL_CORESET_PRECODING_GRANULARITY_ALL_CONTIGUOUS_RESOURCE_BLOCKS                   1

// Values for RFMXNR_ATTR_CORESET_CCE_TO_REG_MAPPING_TYPE
#define RFMXNR_VAL_CORESET_CCE_TO_REG_MAPPING_TYPE_NON_INTERLEAVED                                0
#define RFMXNR_VAL_CORESET_CCE_TO_REG_MAPPING_TYPE_INTERLEAVED                                    1

// Values for RFMXNR_ATTR_SSB_ENABLED
#define RFMXNR_VAL_SSB_ENABLED_FALSE                                                              0
#define RFMXNR_VAL_SSB_ENABLED_TRUE                                                               1

// Values for RFMXNR_ATTR_SSB_PATTERN
#define RFMXNR_VAL_SSB_PATTERN_CASE_A_UP_TO_3GHZ                                                  0
#define RFMXNR_VAL_SSB_PATTERN_CASE_A_3GHZ_TO_6GHZ                                                1
#define RFMXNR_VAL_SSB_PATTERN_CASE_B_UP_TO_3GHZ                                                  2
#define RFMXNR_VAL_SSB_PATTERN_CASE_B_3GHZ_TO_6GHZ                                                3
#define RFMXNR_VAL_SSB_PATTERN_CASE_C_UP_TO_3GHZ                                                  4
#define RFMXNR_VAL_SSB_PATTERN_CASE_C_3GHZ_TO_6GHZ                                                5
#define RFMXNR_VAL_SSB_PATTERN_CASE_D                                                             6
#define RFMXNR_VAL_SSB_PATTERN_CASE_E                                                             7
#define RFMXNR_VAL_SSB_PATTERN_CASE_F                                                             8
#define RFMXNR_VAL_SSB_PATTERN_CASE_G                                                             9

// Values for RFMXNR_ATTR_LIST_STEP_TIMER_UNIT
#define RFMXNR_VAL_LIST_STEP_TIMER_UNIT_SLOT                                                      1
#define RFMXNR_VAL_LIST_STEP_TIMER_UNIT_TIME                                                      6

// Values for RFMXNR_ATTR_MODACC_MULTICARRIER_FILTER_ENABLED
#define RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_FALSE                                       0
#define RFMXNR_VAL_MODACC_MULTICARRIER_FILTER_ENABLED_TRUE                                        1

// Values for RFMXNR_ATTR_MODACC_SYNCHRONIZATION_MODE
#define RFMXNR_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT                                               1
#define RFMXNR_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME                                              5
#define RFMXNR_VAL_MODACC_SYNCHRONIZATION_MODE_SSB_START_FRAME                                    7

// Values for RFMXNR_ATTR_MODACC_MEASUREMENT_LENGTH_UNIT
#define RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SLOT                                            1
#define RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_SUBFRAME                                        3
#define RFMXNR_VAL_MODACC_MEASUREMENT_LENGTH_UNIT_TIME                                            6

// Values for RFMXNR_ATTR_MODACC_FREQUENCY_ERROR_ESTIMATION
#define RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_DISABLED                                     0
#define RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_NORMAL                                       1
#define RFMXNR_VAL_MODACC_FREQUENCY_ERROR_ESTIMATION_WIDE                                         2

// Values for RFMXNR_ATTR_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED
#define RFMXNR_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_FALSE                             0
#define RFMXNR_VAL_MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED_TRUE                              1

// Values for RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_MODEL
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_MODEL_TX                                                 0
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_MODEL_RX                                                 1

// Values for RFMXNR_ATTR_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_FALSE                               0
#define RFMXNR_VAL_MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED_TRUE                                1

// Values for RFMXNR_ATTR_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_FALSE                                    0
#define RFMXNR_VAL_MODACC_IQ_MISMATCH_ESTIMATION_ENABLED_TRUE                                     1

// Values for RFMXNR_ATTR_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE                              0
#define RFMXNR_VAL_MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE                               1

// Values for RFMXNR_ATTR_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE                            0
#define RFMXNR_VAL_MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE                             1

// Values for RFMXNR_ATTR_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_FALSE                                 0
#define RFMXNR_VAL_MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_TRUE                                  1

// Values for RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE                             0
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_TRUE                              1

// Values for RFMXNR_ATTR_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED
#define RFMXNR_VAL_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_FALSE                                 0
#define RFMXNR_VAL_MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED_TRUE                                  1

// Values for RFMXNR_ATTR_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE
#define RFMXNR_VAL_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_ACQUIRED_WAVEFORM                       0
#define RFMXNR_VAL_MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM                      1

// Values for RFMXNR_ATTR_MODACC_SPECTRUM_INVERTED
#define RFMXNR_VAL_MODACC_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXNR_VAL_MODACC_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXNR_ATTR_MODACC_CHANNEL_ESTIMATION_TYPE
#define RFMXNR_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE                                       0
#define RFMXNR_VAL_MODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA                              1

// Values for RFMXNR_ATTR_MODACC_PHASE_TRACKING_MODE
#define RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_DISABLED                                            0
#define RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_REFERENCE_AND_DATA                                  1
#define RFMXNR_VAL_MODACC_PHASE_TRACKING_MODE_PTRS                                                2

// Values for RFMXNR_ATTR_MODACC_TIMING_TRACKING_MODE
#define RFMXNR_VAL_MODACC_TIMING_TRACKING_MODE_DISABLED                                           0
#define RFMXNR_VAL_MODACC_TIMING_TRACKING_MODE_REFERENCE_AND_DATA                                 1

// Values for RFMXNR_ATTR_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL
#define RFMXNR_VAL_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_SLOT                                  0
#define RFMXNR_VAL_MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL_MEASUREMENT_LENGTH                    1

// Values for RFMXNR_ATTR_MODACC_EVM_UNIT
#define RFMXNR_VAL_MODACC_EVM_UNIT_PERCENTAGE                                                     0
#define RFMXNR_VAL_MODACC_EVM_UNIT_DB                                                             1

// Values for RFMXNR_ATTR_MODACC_FFT_WINDOW_TYPE
#define RFMXNR_VAL_MODACC_FFT_WINDOW_TYPE_3GPP                                                    0
#define RFMXNR_VAL_MODACC_FFT_WINDOW_TYPE_CUSTOM                                                  1

// Values for RFMXNR_ATTR_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED
#define RFMXNR_VAL_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_FALSE                                     0
#define RFMXNR_VAL_MODACC_DC_SUBCARRIER_REMOVAL_ENABLED_TRUE                                      1

// Values for RFMXNR_ATTR_MODACC_COMMON_CLOCK_SOURCE_ENABLED
#define RFMXNR_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE                                       0
#define RFMXNR_VAL_MODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE                                        1

// Values for RFMXNR_ATTR_MODACC_SPECTRAL_FLATNESS_CONDITION
#define RFMXNR_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_NORMAL                                      0
#define RFMXNR_VAL_MODACC_SPECTRAL_FLATNESS_CONDITION_EXTREME                                     1

// Values for RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_ENABLED
#define RFMXNR_VAL_MODACC_NOISE_COMPENSATION_ENABLED_FALSE                                        0
#define RFMXNR_VAL_MODACC_NOISE_COMPENSATION_ENABLED_TRUE                                         1

// Values for RFMXNR_ATTR_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED
#define RFMXNR_VAL_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_FALSE                      0
#define RFMXNR_VAL_MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_TRUE                       1

// Values for RFMXNR_ATTR_MODACC_MEASUREMENT_MODE
#define RFMXNR_VAL_MODACC_MEASUREMENT_MODE_MEASURE                                                0
#define RFMXNR_VAL_MODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                                  1

// Values for RFMXNR_ATTR_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS
#define RFMXNR_VAL_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS_FALSE                                    0
#define RFMXNR_VAL_MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS_TRUE                                     1

// Values for RFMXNR_ATTR_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS
#define RFMXNR_VAL_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS_FALSE                                    0
#define RFMXNR_VAL_MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS_TRUE                                     1

// Values for RFMXNR_ATTR_MODACC_AVERAGING_ENABLED
#define RFMXNR_VAL_MODACC_AVERAGING_ENABLED_FALSE                                                 0
#define RFMXNR_VAL_MODACC_AVERAGING_ENABLED_TRUE                                                  1

// Values for RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW
#define RFMXNR_VAL_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW_FALSE                                         0
#define RFMXNR_VAL_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW_TRUE                                          1

// Values for RFMXNR_ATTR_MODACC_SHORT_FRAME_ENABLED
#define RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_FALSE                                               0
#define RFMXNR_VAL_MODACC_SHORT_FRAME_ENABLED_TRUE                                                1

// Values for RFMXNR_ATTR_MODACC_SHORT_FRAME_LENGTH_UNIT
#define RFMXNR_VAL_MODACC_SHORT_FRAME_LENGTH_UNIT_SLOT                                            1
#define RFMXNR_VAL_MODACC_SHORT_FRAME_LENGTH_UNIT_SUBFRAME                                        3
#define RFMXNR_VAL_MODACC_SHORT_FRAME_LENGTH_UNIT_TIME                                            6

// Values for RFMXNR_ATTR_MODACC_TRANSIENT_PERIOD_EVM_MODE
#define RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_DISABLED                                      0
#define RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_EXCLUDE                                       1
#define RFMXNR_VAL_MODACC_TRANSIENT_PERIOD_EVM_MODE_INCLUDE                                       2

// Values for RFMXNR_ATTR_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_PI_BY_2_BPSK                       0
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QPSK                               1
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QAM16                              2
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QAM64                              3
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QAM256                             4
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QAM1024                            5
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_PSK8                               100
#define RFMXNR_VAL_MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE_QAM4096                            6

// Values for RFMXNR_ATTR_MODACC_RESULTS_NOISE_COMPENSATION_APPLIED
#define RFMXNR_VAL_MODACC_RESULTS_NOISE_COMPENSATION_APPLIED_FALSE                                0
#define RFMXNR_VAL_MODACC_RESULTS_NOISE_COMPENSATION_APPLIED_TRUE                                 1

// Values for RFMXNR_ATTR_ACP_CHANNEL_CONFIGURATION_TYPE
#define RFMXNR_VAL_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD                                        0
#define RFMXNR_VAL_ACP_CHANNEL_CONFIGURATION_TYPE_CUSTOM                                          1
#define RFMXNR_VAL_ACP_CHANNEL_CONFIGURATION_TYPE_NS_29                                           2
#define RFMXNR_VAL_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD_REL_16                                 3
#define RFMXNR_VAL_ACP_CHANNEL_CONFIGURATION_TYPE_STANDARD_REL_18                                 4

// Values for RFMXNR_ATTR_ACP_OFFSET_SIDEBAND
#define RFMXNR_VAL_ACP_OFFSET_SIDEBAND_NEGATIVE                                                   0
#define RFMXNR_VAL_ACP_OFFSET_SIDEBAND_POSITIVE                                                   1
#define RFMXNR_VAL_ACP_OFFSET_SIDEBAND_BOTH                                                       2

// Values for RFMXNR_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXNR_VAL_ACP_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXNR_ATTR_ACP_RBW_FILTER_TYPE
#define RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXNR_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXNR_VAL_ACP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXNR_ATTR_ACP_SWEEP_TIME_AUTO
#define RFMXNR_VAL_ACP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXNR_VAL_ACP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXNR_ATTR_ACP_POWER_UNITS
#define RFMXNR_VAL_ACP_POWER_UNITS_DBM                                                            0
#define RFMXNR_VAL_ACP_POWER_UNITS_DBM_BY_HZ                                                      1

// Values for RFMXNR_ATTR_ACP_MEASUREMENT_METHOD
#define RFMXNR_VAL_ACP_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXNR_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1
#define RFMXNR_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT                                          2

// Values for RFMXNR_ATTR_ACP_NOISE_CALIBRATION_MODE
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_MODE_MANUAL                                              0
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_MODE_AUTO                                                1

// Values for RFMXNR_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE                                     0
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE                                      1

// Values for RFMXNR_ATTR_ACP_NOISE_COMPENSATION_ENABLED
#define RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXNR_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXNR_ATTR_ACP_NOISE_COMPENSATION_TYPE
#define RFMXNR_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION                           0
#define RFMXNR_VAL_ACP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY                                      1

// Values for RFMXNR_ATTR_ACP_AVERAGING_ENABLED
#define RFMXNR_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_ACP_AVERAGING_TYPE
#define RFMXNR_VAL_ACP_AVERAGING_TYPE_RMS                                                         0
#define RFMXNR_VAL_ACP_AVERAGING_TYPE_LOG                                                         1
#define RFMXNR_VAL_ACP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXNR_VAL_ACP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXNR_VAL_ACP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXNR_ATTR_ACP_MEASUREMENT_MODE
#define RFMXNR_VAL_ACP_MEASUREMENT_MODE_MEASURE                                                   0
#define RFMXNR_VAL_ACP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                                     1

// Values for RFMXNR_ATTR_ACP_FFT_WINDOW
#define RFMXNR_VAL_ACP_FFT_WINDOW_NONE                                                            0
#define RFMXNR_VAL_ACP_FFT_WINDOW_FLAT_TOP                                                        1
#define RFMXNR_VAL_ACP_FFT_WINDOW_HANNING                                                         2
#define RFMXNR_VAL_ACP_FFT_WINDOW_HAMMING                                                         3
#define RFMXNR_VAL_ACP_FFT_WINDOW_GAUSSIAN                                                        4
#define RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN                                                        5
#define RFMXNR_VAL_ACP_FFT_WINDOW_BLACKMAN_HARRIS                                                 6
#define RFMXNR_VAL_ACP_FFT_WINDOW_KAISER_BESSEL                                                   7

// Values for RFMXNR_ATTR_ACP_FFT_OVERLAP_MODE
#define RFMXNR_VAL_ACP_FFT_OVERLAP_MODE_DISABLED                                                  0
#define RFMXNR_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC                                                 1
#define RFMXNR_VAL_ACP_FFT_OVERLAP_MODE_USER_DEFINED                                              2

// Values for RFMXNR_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO
#define RFMXNR_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE                                          0
#define RFMXNR_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE                                           1

// Values for RFMXNR_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE
#define RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXNR_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXNR_ATTR_CHP_SWEEP_TIME_AUTO
#define RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXNR_VAL_CHP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXNR_ATTR_CHP_INTEGRATION_BANDWIDTH_TYPE
#define RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_SIGNAL_BANDWIDTH                                0
#define RFMXNR_VAL_CHP_INTEGRATION_BANDWIDTH_TYPE_CHANNEL_BANDWIDTH                               1

// Values for RFMXNR_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXNR_VAL_CHP_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXNR_ATTR_CHP_RBW_FILTER_TYPE
#define RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXNR_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXNR_VAL_CHP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXNR_ATTR_CHP_NOISE_CALIBRATION_MODE
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL                                              0
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO                                                1

// Values for RFMXNR_ATTR_CHP_NOISE_CALIBRATION_AVERAGING_AUTO
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE                                     0
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE                                      1

// Values for RFMXNR_ATTR_CHP_NOISE_COMPENSATION_ENABLED
#define RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXNR_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXNR_ATTR_CHP_NOISE_COMPENSATION_TYPE
#define RFMXNR_VAL_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_AND_TERMINATION                           0
#define RFMXNR_VAL_CHP_NOISE_COMPENSATION_TYPE_ANALYZER_ONLY                                      1

// Values for RFMXNR_ATTR_CHP_AVERAGING_ENABLED
#define RFMXNR_VAL_CHP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_CHP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_CHP_AVERAGING_TYPE
#define RFMXNR_VAL_CHP_AVERAGING_TYPE_RMS                                                         0
#define RFMXNR_VAL_CHP_AVERAGING_TYPE_LOG                                                         1
#define RFMXNR_VAL_CHP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXNR_VAL_CHP_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXNR_VAL_CHP_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXNR_ATTR_CHP_MEASUREMENT_MODE
#define RFMXNR_VAL_CHP_MEASUREMENT_MODE_MEASURE                                                   0
#define RFMXNR_VAL_CHP_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                                     1

// Values for RFMXNR_ATTR_CHP_FFT_WINDOW
#define RFMXNR_VAL_CHP_FFT_WINDOW_NONE                                                            0
#define RFMXNR_VAL_CHP_FFT_WINDOW_FLAT_TOP                                                        1
#define RFMXNR_VAL_CHP_FFT_WINDOW_HANNING                                                         2
#define RFMXNR_VAL_CHP_FFT_WINDOW_HAMMING                                                         3
#define RFMXNR_VAL_CHP_FFT_WINDOW_GAUSSIAN                                                        4
#define RFMXNR_VAL_CHP_FFT_WINDOW_BLACKMAN                                                        5
#define RFMXNR_VAL_CHP_FFT_WINDOW_BLACKMAN_HARRIS                                                 6
#define RFMXNR_VAL_CHP_FFT_WINDOW_KAISER_BESSEL                                                   7

// Values for RFMXNR_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE
#define RFMXNR_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXNR_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXNR_ATTR_OBW_POWER_INTEGRATION_METHOD
#define RFMXNR_VAL_OBW_POWER_INTEGRATION_METHOD_NORMAL                                            0
#define RFMXNR_VAL_OBW_POWER_INTEGRATION_METHOD_FROM_CENTER                                       1

// Values for RFMXNR_ATTR_OBW_SPAN_AUTO
#define RFMXNR_VAL_OBW_SPAN_AUTO_FALSE                                                            0
#define RFMXNR_VAL_OBW_SPAN_AUTO_TRUE                                                             1

// Values for RFMXNR_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_FALSE                                            0
#define RFMXNR_VAL_OBW_RBW_FILTER_AUTO_BANDWIDTH_TRUE                                             1

// Values for RFMXNR_ATTR_OBW_RBW_FILTER_TYPE
#define RFMXNR_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXNR_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXNR_VAL_OBW_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXNR_ATTR_OBW_SWEEP_TIME_AUTO
#define RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXNR_VAL_OBW_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXNR_ATTR_OBW_AVERAGING_ENABLED
#define RFMXNR_VAL_OBW_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_OBW_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_OBW_AVERAGING_TYPE
#define RFMXNR_VAL_OBW_AVERAGING_TYPE_RMS                                                         0
#define RFMXNR_VAL_OBW_AVERAGING_TYPE_LOG                                                         1
#define RFMXNR_VAL_OBW_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXNR_VAL_OBW_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXNR_VAL_OBW_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXNR_ATTR_OBW_FFT_WINDOW
#define RFMXNR_VAL_OBW_FFT_WINDOW_NONE                                                            0
#define RFMXNR_VAL_OBW_FFT_WINDOW_FLAT_TOP                                                        1
#define RFMXNR_VAL_OBW_FFT_WINDOW_HANNING                                                         2
#define RFMXNR_VAL_OBW_FFT_WINDOW_HAMMING                                                         3
#define RFMXNR_VAL_OBW_FFT_WINDOW_GAUSSIAN                                                        4
#define RFMXNR_VAL_OBW_FFT_WINDOW_BLACKMAN                                                        5
#define RFMXNR_VAL_OBW_FFT_WINDOW_BLACKMAN_HARRIS                                                 6
#define RFMXNR_VAL_OBW_FFT_WINDOW_KAISER_BESSEL                                                   7

// Values for RFMXNR_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE
#define RFMXNR_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXNR_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXNR_ATTR_SEM_UPLINK_MASK_TYPE
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_GENERAL                                                   0
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS35                                                      1
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_CUSTOM                                                    2
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS03                                                      3
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS04                                                      4
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS06                                                      5
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS21                                                      6
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS27                                                      7
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS07                                                      8
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS03U                                                     9
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS21_REL_17_ONWARDS                                       10
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS04N                                                     11
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS05N                                                     12
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS09N                                                     13
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS10N                                                     14
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS11N                                                     15
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS12N                                                     16
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS203N                                                    17
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS204N                                                    18
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS207N                                                    19
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS208N                                                    20
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS02N                                                     21
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS03N                                                     22
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS06N                                                     23
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS07N                                                     24
#define RFMXNR_VAL_SEM_UPLINK_MASK_TYPE_NS08N                                                     25

// Values for RFMXNR_ATTR_SEM_DOWNLINK_MASK_TYPE
#define RFMXNR_VAL_SEM_DOWNLINK_MASK_TYPE_STANDARD                                                0
#define RFMXNR_VAL_SEM_DOWNLINK_MASK_TYPE_CUSTOM                                                  2

// Values for RFMXNR_ATTR_SEM_OFFSET_SIDEBAND
#define RFMXNR_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE                                                   0
#define RFMXNR_VAL_SEM_OFFSET_SIDEBAND_POSITIVE                                                   1
#define RFMXNR_VAL_SEM_OFFSET_SIDEBAND_BOTH                                                       2

// Values for RFMXNR_ATTR_SEM_OFFSET_RBW_FILTER_TYPE
#define RFMXNR_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED                                           0
#define RFMXNR_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN                                            1
#define RFMXNR_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT                                                2

// Values for RFMXNR_ATTR_SEM_OFFSET_LIMIT_FAIL_MASK
#define RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_AND_REL                                         0
#define RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABS_OR_REL                                          1
#define RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_ABSOLUTE                                            2
#define RFMXNR_VAL_SEM_OFFSET_LIMIT_FAIL_MASK_RELATIVE                                            3

// Values for RFMXNR_ATTR_SEM_OFFSET_FREQUENCY_DEFINITION
#define RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_CENTER_TO_MEAS_BW_CENTER               0
#define RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_CARRIER_EDGE_TO_MEAS_BW_CENTER                 2
#define RFMXNR_VAL_SEM_OFFSET_FREQUENCY_DEFINITION_SUBBLOCK_EDGE_TO_MEAS_BW_CENTER                6

// Values for RFMXNR_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXNR_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXNR_ATTR_SEM_AVERAGING_ENABLED
#define RFMXNR_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_SEM_AVERAGING_TYPE
#define RFMXNR_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXNR_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXNR_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXNR_VAL_SEM_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXNR_VAL_SEM_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXNR_ATTR_SEM_FFT_WINDOW
#define RFMXNR_VAL_SEM_FFT_WINDOW_NONE                                                            0
#define RFMXNR_VAL_SEM_FFT_WINDOW_FLAT_TOP                                                        1
#define RFMXNR_VAL_SEM_FFT_WINDOW_HANNING                                                         2
#define RFMXNR_VAL_SEM_FFT_WINDOW_HAMMING                                                         3
#define RFMXNR_VAL_SEM_FFT_WINDOW_GAUSSIAN                                                        4
#define RFMXNR_VAL_SEM_FFT_WINDOW_BLACKMAN                                                        5
#define RFMXNR_VAL_SEM_FFT_WINDOW_BLACKMAN_HARRIS                                                 6
#define RFMXNR_VAL_SEM_FFT_WINDOW_KAISER_BESSEL                                                   7

// Values for RFMXNR_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE
#define RFMXNR_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXNR_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXNR_ATTR_SEM_RESULTS_MEASUREMENT_STATUS
#define RFMXNR_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXNR_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXNR_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXNR_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXNR_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXNR_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXNR_ATTR_TXP_AVERAGING_ENABLED
#define RFMXNR_VAL_TXP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_TXP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_PVT_MEASUREMENT_INTERVAL_AUTO
#define RFMXNR_VAL_PVT_MEASUREMENT_INTERVAL_AUTO_FALSE                                            0
#define RFMXNR_VAL_PVT_MEASUREMENT_INTERVAL_AUTO_TRUE                                             1

// Values for RFMXNR_ATTR_PVT_MEASUREMENT_METHOD
#define RFMXNR_VAL_PVT_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXNR_VAL_PVT_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1

// Values for RFMXNR_ATTR_PVT_AVERAGING_ENABLED
#define RFMXNR_VAL_PVT_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXNR_VAL_PVT_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXNR_ATTR_PVT_AVERAGING_TYPE
#define RFMXNR_VAL_PVT_AVERAGING_TYPE_RMS                                                         0
#define RFMXNR_VAL_PVT_AVERAGING_TYPE_LOG                                                         1

// Values for RFMXNR_ATTR_PVT_RESULTS_MEASUREMENT_STATUS
#define RFMXNR_VAL_PVT_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXNR_VAL_PVT_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXNR_ATTR_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED
#define RFMXNR_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_FALSE                               0
#define RFMXNR_VAL_ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED_TRUE                                1

// Values for RFMXNR_ATTR_TRANSMITTER_ARCHITECTURE
#define RFMXNR_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_COMPONENT_CARRIER                              0
#define RFMXNR_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_SUBBLOCK                                       1

// Values for RFMXNR_ATTR_PHASE_COMPENSATION
#define RFMXNR_VAL_PHASE_COMPENSATION_DISABLED                                                    0
#define RFMXNR_VAL_PHASE_COMPENSATION_AUTO                                                        1
#define RFMXNR_VAL_PHASE_COMPENSATION_USER_DEFINED                                                2

// Values for RFMXNR_ATTR_REFERENCE_GRID_ALIGNMENT_MODE
#define RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_MANUAL                                           0
#define RFMXNR_VAL_REFERENCE_GRID_ALIGNMENT_MODE_AUTO                                             1

// Values for RFMXNR_ATTR_GRID_SIZE_MODE
#define RFMXNR_VAL_GRID_SIZE_MODE_MANUAL                                                          0
#define RFMXNR_VAL_GRID_SIZE_MODE_AUTO                                                            1

// Values for RFMXNR_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXNR_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for ChpNoiseCalibrationDataValid
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_DATA_VALID_FALSE                                         0
#define RFMXNR_VAL_CHP_NOISE_CALIBRATION_DATA_VALID_TRUE                                          1

// Values for AcpNoiseCalibrationDataValid
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_DATA_VALID_FALSE                                         0
#define RFMXNR_VAL_ACP_NOISE_CALIBRATION_DATA_VALID_TRUE                                          1

// Values for ModAccCalibrationDataValid
#define RFMXNR_VAL_MODACC_CALIBRATION_DATA_VALID_FALSE                                            0
#define RFMXNR_VAL_MODACC_CALIBRATION_DATA_VALID_TRUE                                             1

// Values for Boolean
#define RFMXNR_VAL_FALSE                                                                          0
#define RFMXNR_VAL_TRUE                                                                           1

// Values for FrequencyReferenceSource
#define RFMXNR_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXNR_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXNR_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXNR_VAL_CLK_IN_STR                                                                     "ClkIn"
#define RFMXNR_VAL_REF_IN2_STR                                                                    "RefIn2"
#define RFMXNR_VAL_PXI_CLK_MASTER_STR                                                             "PXI_Clk_Master"

// Values for RFAttenuationAuto
#define RFMXNR_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXNR_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for MeasurementTypes
#define RFMXNR_VAL_MODACC                                                                         1<<0
#define RFMXNR_VAL_SEM                                                                            1<<1
#define RFMXNR_VAL_ACP                                                                            1<<2
#define RFMXNR_VAL_CHP                                                                            1<<3
#define RFMXNR_VAL_OBW                                                                            1<<4
#define RFMXNR_VAL_PVT                                                                            1<<5
#define RFMXNR_VAL_TXP                                                                            1<<6

/* ---------------- RFmxNR APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxNR_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxNR_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxNR_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxNR_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxNR_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxNR_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxNR_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxNR_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxNR_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxNR_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxNR_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxNR_BuildListString(
   char listName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxNR_BuildListStepString(
   char listName[],
   char resultName[],
   int32 stepNumber,
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxNR_BuildBandwidthPartString(
   char selectorString[],
   int32 bandwidthPartNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildCarrierString(
   char selectorString[],
   int32 carrierNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildCORESETClusterString(
   char selectorString[],
   int32 CORESETClusterNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildCORESETString(
   char selectorString[],
   int32 CORESETNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildPDCCHString(
   char selectorString[],
   int32 PDCCHNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildPDSCHClusterString(
   char selectorString[],
   int32 PDSCHClusterNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildPDSCHString(
   char selectorString[],
   int32 PDSCHNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildPUSCHClusterString(
   char selectorString[],
   int32 PUSCHClusterNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildPUSCHString(
   char selectorString[],
   int32 PUSCHNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildSubblockString(
   char selectorString[],
   int32 subblockNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildUserString(
   char selectorString[],
   int32 userNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildLayerString(
   char selectorString[],
   int32 layerNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_BuildChainString(
   char selectorString[],
   int32 chainNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxNR_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxNR_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxNR_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxNR_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxNR_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxNR_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxNR_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxNR_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxNR_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxNR_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxNR_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxNR_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxNR_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxNR_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxNR_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxNR_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxNR_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxNR_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxNR_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxNR_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxNR_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxNR_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_ModAccCfgReferenceWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   NIComplexSingle referenceWaveform[],
   int32 arraySize
);

int32 __stdcall RFmxNR_ModAccCfgReferenceWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 arraySize
);

int32 __stdcall RFmxNR_ModAccAutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxNR_ModAccValidateCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* calibrationDataValid
);

int32 __stdcall RFmxNR_ModAccClearNoiseCalibrationDatabase(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxNR_ACPValidateNoiseCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* noiseCalibrationDataValid
);

int32 __stdcall RFmxNR_CHPValidateNoiseCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* noiseCalibrationDataValid
);

int32 __stdcall RFmxNR_AnalyzeIQ1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxNR_AnalyzeIQ1WaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxNR_AnalyzeSpectrum1Waveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int64 reserved
);

int32 __stdcall RFmxNR_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxNR_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxNR_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_ClearNoiseCalibrationDatabase(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxNR_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_CfgSelectedPortsMultiple(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char selectedPorts[]
);

int32 __stdcall RFmxNR_CreateList(
   niRFmxInstrHandle instrumentHandle,
   char listName[]
);

int32 __stdcall RFmxNR_CreateListStep(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* createdStepIndex
);

int32 __stdcall RFmxNR_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxNR_DeleteList(
   niRFmxInstrHandle instrumentHandle,
   char listName[]
);

int32 __stdcall RFmxNR_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxNR_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxNR_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxNR_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxNR_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierRatedOutputPower
);

int32 __stdcall RFmxNR_SEMCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxNR_SEMCfgOffsetAbsoluteLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 absoluteLimitStart,
   float64 absoluteLimitStop
);

int32 __stdcall RFmxNR_SEMCfgOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 bandwidthIntegral
);

int32 __stdcall RFmxNR_SEMCfgOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetStartFrequency,
   float64 offsetStopFrequency,
   int32 offsetSideband
);

int32 __stdcall RFmxNR_SEMCfgOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 limitFailMask
);

int32 __stdcall RFmxNR_SEMCfgOffsetRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetRBW,
   int32 offsetRBWFilterType
);

int32 __stdcall RFmxNR_SEMCfgOffsetRelativeLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 relativeLimitStart,
   float64 relativeLimitStop
);

int32 __stdcall RFmxNR_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxNR_SEMCfgUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkMaskType
);

int32 __stdcall RFmxNR_SEMCfgComponentCarrierRatedOutputPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 componentCarrierRatedOutputPower[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetAbsoluteLimitArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 absoluteLimitStart[],
   float64 absoluteLimitStop[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetBandwidthIntegralArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 bandwidthIntegral[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetStartFrequency[],
   float64 offsetStopFrequency[],
   int32 offsetSideband[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetLimitFailMaskArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 limitFailMask[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetRBWFilterArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetRBW[],
   int32 offsetRBWFilterType[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_SEMCfgOffsetRelativeLimitArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 relativeLimitStart[],
   float64 relativeLimitStop[],
   int32 numberOfElements
);

int32 __stdcall RFmxNR_ModAccCfgMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMode
);

int32 __stdcall RFmxNR_ModAccCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxNR_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxNR_ACPCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxNR_ACPCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxNR_ACPCfgNumberOfENDCOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfENDCOffsets
);

int32 __stdcall RFmxNR_ACPCfgNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfEUTRAOffsets
);

int32 __stdcall RFmxNR_ACPCfgNumberOfNROffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfNROffsets
);

int32 __stdcall RFmxNR_ACPCfgNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfUTRAOffsets
);

int32 __stdcall RFmxNR_ACPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxNR_ACPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxNR_ACPCfgPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerUnits
);

int32 __stdcall RFmxNR_PVTCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxNR_PVTCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxNR_PVTCfgOFFPowerExclusionPeriods(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 OFFPowerExclusionBefore,
   float64 OFFPowerExclusionAfter
);

int32 __stdcall RFmxNR_OBWCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxNR_OBWCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxNR_OBWCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxNR_CHPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxNR_CHPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxNR_CHPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxNR_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxNR_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxNR_CfggNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 gNodeBCategory
);

int32 __stdcall RFmxNR_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxNR_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxNR_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_AnalyzeNWaveformsIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0[],
   float64 dx[],
   NIComplexSingle IQ[],
   int32 IQSize[],
   int32 arraySize,
   int32 reset
);

int32 __stdcall RFmxNR_AnalyzeNWaveformsIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0[],
   float64 dx[],
   float32 IQI[],
   float32 IQQ[],
   int32 IQSize[],
   int32 arraySize,
   int32 reset
);

int32 __stdcall RFmxNR_AnalyzeNWaveformsSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0[],
   float64 dx[],
   float32 spectrum[],
   int32 spectrumSize[],
   int32 arraySize,
   int32 reset
);

int32 __stdcall RFmxNR_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxNR_CfgIQPowerEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char IQPowerEdgeSource[],
   int32 IQPowerEdgeSlope,
   float64 IQPowerEdgeLevel,
   float64 triggerDelay,
   int32 triggerMinQuietTimeMode,
   float64 triggerMinQuietTimeDuration,
   int32 IQPowerEdgeLevelType,
   int32 enableTrigger
);

int32 __stdcall RFmxNR_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxNR_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxNR_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxNR_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxNR_LoadFromGenerationConfigurationFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char filePath[],
   int32 configurationIndex
);

int32 __stdcall RFmxNR_ModAccFetchInBandEmissionTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 inBandEmission[],
   float32 inBandEmissionMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PBCHDataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PBCHDataConstellationI[],
   float32 PBCHDataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PBCHDataRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PBCHDataRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PBCHDMRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PBCHDMRSConstellationI[],
   float32 PBCHDMRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PBCHDMRSRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PBCHDMRSRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM4096Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH4096QAMConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM4096ConstellationI[],
   float32 QAM4096ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PSK8Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH8PSKConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PSK8ConstellationI[],
   float32 PSK8ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM1024Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH1024QAMConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM1024ConstellationI[],
   float32 QAM1024ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM16Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH16QAMConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM16ConstellationI[],
   float32 QAM16ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM256Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH256QAMConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM256ConstellationI[],
   float32 QAM256ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QAM64Constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCH64QAMConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QAM64ConstellationI[],
   float32 QAM64ConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PDSCHDataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PDSCHDataConstellationI[],
   float32 PDSCHDataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHDemodulatedBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 bits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PDSCHDMRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHDMRSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PDSCHDMRSConstellationI[],
   float32 PDSCHDMRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PDSCHPTRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHPTRSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PDSCHPTRSConstellationI[],
   float32 PDSCHPTRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle QPSKConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPDSCHQPSKConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 QPSKConstellationI[],
   float32 QPSKConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSlotMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 peakEVMPerSlotMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSubcarrierMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 peakEVMPerSubcarrierMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPeakEVMPerSymbolMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 peakEVMPerSymbolMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPSSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PSSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPSSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PSSConstellationI[],
   float32 PSSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PSSRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPSSRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PSSRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PUSCHDataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PUSCHDataConstellationI[],
   float32 PUSCHDataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHDemodulatedBits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int8 bits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PUSCHDMRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHDMRSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PUSCHDMRSConstellationI[],
   float32 PUSCHDMRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle PUSCHPTRSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHPTRSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 PUSCHPTRSConstellationI[],
   float32 PUSCHPTRSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSlotMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMPerSlotMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchRMSEVMHighPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMHighPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPeakEVMHighPerSymbolMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 peakEVMHighPerSymbolMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchRMSEVMLowPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 RMSEVMLowPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPeakEVMLowPerSymbolMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 peakEVMLowPerSymbolMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchTransientPeriodLocationsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 transientPeriodLocations[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchPUSCHPhaseOffsetTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 PUSCHPhaseOffset[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchFrequencyErrorPerSlotMaximumTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 frequencyErrorPerSlotMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSpectralFlatnessTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectralFlatness[],
   float32 spectralFlatnessLowerMask[],
   float32 spectralFlatnessUpperMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSSSConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle SSSConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSSSConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 SSSConstellationI[],
   float32 SSSConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 SSSRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSSSRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 SSSRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchSubblockInBandEmissionTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 subblockInBandEmission[],
   float64 subblockInBandEmissionMask[],
   float64 subblockInBandEmissionRBIndices[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchIQGainImbalancePerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 IQGainImbalancePerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 IQQuadratureErrorPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ModAccFetchCompositeEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* compositeRMSEVMMean,
   float64* compositePeakEVMMaximum
);

int32 __stdcall RFmxNR_ModAccFetchFrequencyErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* frequencyErrorMean
);

int32 __stdcall RFmxNR_ACPFetchAbsolutePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 absolutePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ACPFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ACPFetchOffsetMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 lowerRelativePower[],
   float64 upperRelativePower[],
   float64 lowerAbsolutePower[],
   float64 upperAbsolutePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ACPFetchRelativePowersTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 traceIndex,
   float64* x0,
   float64* dx,
   float32 relativePowersTrace[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_ACPFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxNR_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower
);

int32 __stdcall RFmxNR_ACPFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxNR_ACPFetchSubblockMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower,
   float64* integrationBandwidth,
   float64* frequency
);

int32 __stdcall RFmxNR_TXPFetchPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 power[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_TXPFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averagePowerMean,
   float64* peakPowerMaximum
);

int32 __stdcall RFmxNR_PVTFetchMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 absoluteOFFPowerBefore[],
   float64 absoluteOFFPowerAfter[],
   float64 absoluteONPower[],
   float64 burstWidth[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_PVTFetchSignalPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 signalPower[],
   float32 absoluteLimit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_PVTFetchWindowedSignalPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 windowedSignalPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_PVTFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* absoluteOFFPowerBefore,
   float64* absoluteOFFPowerAfter,
   float64* absoluteONPower,
   float64* burstWidth
);

int32 __stdcall RFmxNR_OBWFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_OBWFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* occupiedBandwidth,
   float64* absolutePower,
   float64* startFrequency,
   float64* stopFrequency
);

int32 __stdcall RFmxNR_SEMFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 peakAbsolutePower[],
   float64 peakFrequency[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchLowerOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchLowerOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 totalAbsolutePower[],
   float64 totalRelativePower[],
   float64 peakAbsolutePower[],
   float64 peakFrequency[],
   float64 peakRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   float32 compositeMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMarginArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 measurementStatus[],
   float64 margin[],
   float64 marginFrequency[],
   float64 marginAbsolutePower[],
   float64 marginRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchUpperOffsetPowerArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 totalAbsolutePower[],
   float64 totalRelativePower[],
   float64 peakAbsolutePower[],
   float64 peakFrequency[],
   float64 peakRelativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_SEMFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* peakAbsolutePower,
   float64* peakFrequency,
   float64* relativePower
);

int32 __stdcall RFmxNR_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxNR_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAbsolutePower,
   float64* totalRelativePower,
   float64* peakAbsolutePower,
   float64* peakFrequency,
   float64* peakRelativePower
);

int32 __stdcall RFmxNR_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxNR_SEMFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxNR_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxNR_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAbsolutePower,
   float64* totalRelativePower,
   float64* peakAbsolutePower,
   float64* peakFrequency,
   float64* peakRelativePower
);

int32 __stdcall RFmxNR_SEMFetchSubblockMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower,
   float64* integrationBandwidth,
   float64* frequency
);

int32 __stdcall RFmxNR_CHPFetchComponentCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_CHPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxNR_CHPFetchComponentCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxNR_CHPFetchSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower
);

int32 __stdcall RFmxNR_CHPFetchTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAggregatedPower
);

int32 __stdcall RFmxNR_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetgNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetgNodeBCategory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetgNodeBType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetgNodeBType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSatelliteAccessNodeType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSatelliteAccessNodeType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSatelliteAccessNodeClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSatelliteAccessNodeClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetTransmitAntennaToAnalyze(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetTransmitAntennaToAnalyze(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfReceiveChains(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfReceiveChains(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPowerClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPowerClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPiBy2BPSKPowerBoostEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPiBy2BPSKPowerBoostEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetAutoResourceBlockDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetAutoResourceBlockDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetAutoCellIDDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetAutoCellIDDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDownlinkChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetAutoIncrementCellIDEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetAutoIncrementCellIDEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDownlinkTestModelCellIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDownlinkTestModelCellIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfSubblocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfSubblocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSubblockFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSubblockFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetSubblockTransmitLOFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSubblockTransmitLOFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPhaseCompensationFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPhaseCompensationFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetFrequencyRange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetFrequencyRange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSubblockENDCNominalSpacingAdjustment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSubblockENDCNominalSpacingAdjustment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetChannelRaster(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetChannelRaster(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierSpacingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierSpacingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierAtCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierAtCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfComponentCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfComponentCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDownlinkTestModelModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDownlinkTestModelModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetDownlinkTestModelDuplexScheme(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetDownlinkTestModelDuplexScheme(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetRatedTRP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetRatedTRP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetRatedEIRP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetRatedEIRP(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierAllocated(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierAllocated(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetComponentCarrierRadioAccessType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetComponentCarrierRadioAccessType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetReferenceGridSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceGridSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetReferenceGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetReferenceGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSubBandAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetSubBandAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetNumberOfBandwidthParts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfBandwidthParts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetBandwidthPartSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetBandwidthPartSubcarrierSpacing(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetBandwidthPartCyclicPrefixMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetBandwidthPartCyclicPrefixMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetBandwidthPartResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetBandwidthPartResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetBandwidthPartNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetBandwidthPartNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetBandwidthPartDCLocationKnown(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetBandwidthPartDCLocationKnown(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetRNTI(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetRNTI(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfPUSCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfPUSCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHTransformPrecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHTransformPrecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSReleaseVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSReleaseVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPUSCHDMRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPUSCHDMRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSNumberOfCDMGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSNumberOfCDMGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSScramblingIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSScramblingIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSScramblingID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSScramblingID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSNSCID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSNSCID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSGroupHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSSequenceHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSSequenceHoppingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSPUSCHIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSPUSCHIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSPUSCHID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSPUSCHID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSTypeAPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSTypeAPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHDMRSAdditionalPositions(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHDMRSAdditionalPositions(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPUSCHPTRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPUSCHPTRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfPTRSGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfPTRSGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSamplesPerPTRSGroup(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSamplesPerPTRSGroup(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSTimeDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSTimeDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSFrequencyDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSFrequencyDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHPTRSREOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPUSCHPTRSREOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPUSCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPUSCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPUSCHSymbolAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPUSCHSymbolAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetNumberOfPDSCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfPDSCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSReleaseVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSReleaseVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPDSCHDMRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPDSCHDMRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSNumberOfCDMGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSNumberOfCDMGroups(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSScramblingIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSScramblingIDMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSScramblingID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSScramblingID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSnSCID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSnSCID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSTypeAPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSTypeAPosition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHDMRSAdditionalPositions(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHDMRSAdditionalPositions(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPDSCHPTRSAntennaPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPDSCHPTRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSPowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetEPRERatioPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetEPRERatioPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSTimeDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSTimeDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSFrequencyDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSFrequencyDensity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHPTRSREOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPTRSREOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDSCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPDSCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPDSCHSymbolAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPDSCHSymbolAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetNumberOfCORESETs(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfCORESETs(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETSymbolOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETSymbolOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETNumberOfSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETNumberOfSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETNumberOfResourceBlockClusters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETResourceBlockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETNumberOfResourceBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETPrecodingGranularity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETPrecodingGranularity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETCCEToREGMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETCCEToREGMappingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETREGBundleSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETREGBundleSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETInterleaverSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETInterleaverSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetCORESETShiftIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetCORESETShiftIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfPDCCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfPDCCHConfigurations(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDCCHCCEAggregationLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDCCHCCEAggregationLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDCCHCCEOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDCCHCCEOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPDCCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetPDCCHSlotAllocation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetSSBEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSSBGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBGridStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSSBGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBGridSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSSBCRBOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBCRBOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSubcarrierSpacingCommon(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSubcarrierSpacingCommon(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetSSBSubcarrierOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBSubcarrierOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSSBPeriodicity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSSBPeriodicity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetSSBPattern(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBPattern(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSSBActiveBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxNR_SetSSBActiveBlocks(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxNR_GetPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetSSSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPBCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPBCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetPBCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetPBCHDMRSPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetSSBHRFIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSSBHRFIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetNumberOfSteps(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetNumberOfSteps(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetListStepTimerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetListStepTimerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetListStepTimerDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetListStepTimerDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetListStepTimerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetListStepTimerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_GetAcquisitionBandwidthOptimizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetAcquisitionBandwidthOptimizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetPhaseCompensation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPhaseCompensation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetReferenceGridAlignmentMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetReferenceGridAlignmentMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetGridSizeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetGridSizeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMulticarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMulticarrierFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMeasurementLengthUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMeasurementLengthUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetFrequencyErrorEstimation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetFrequencyErrorEstimation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetSymbolClockErrorEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetSymbolClockErrorEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQImpairmentsModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQImpairmentsModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQOriginOffsetEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQOriginOffsetEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQMismatchEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQMismatchEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQImpairmentsPerSubcarrierEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQImpairmentsPerSubcarrierEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMagnitudeAndPhaseErrorEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMagnitudeAndPhaseErrorEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetEVMReferenceDataSymbolsMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetEVMReferenceDataSymbolsMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetPhaseTrackingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetPhaseTrackingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetTimingTrackingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetTimingTrackingMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetPreFFTErrorEstimationInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetPreFFTErrorEstimationInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetFFTWindowType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetFFTWindowType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetFFTWindowOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetFFTWindowOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetFFTWindowLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetFFTWindowLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetDCSubcarrierRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetDCSubcarrierRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetSpectralFlatnessCondition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetSpectralFlatnessCondition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetNoiseCompensationInputPowerCheckEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetNoiseCompensationInputPowerCheckEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetNoiseCompensationReferenceLevelCoercionLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetNoiseCompensationReferenceLevelCoercionLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetCompositeResultsIncludeDMRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetCompositeResultsIncludeDMRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetCompositeResultsIncludePTRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetCompositeResultsIncludePTRS(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetAutoLevelAllowOverflow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetAutoLevelAllowOverflow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetShortFrameEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetShortFrameEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetShortFrameLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetShortFrameLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetShortFrameLengthUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetShortFrameLengthUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetTransientPeriodEVMMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetTransientPeriodEVMMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetTransientPeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetTransientPeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetTransientPowerChangeThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetTransientPowerChangeThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsDetectedCellID(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositeRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakEVMBWPIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakEVMSlotIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakEVMSymbolIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakEVMSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositeRMSMagnitudeErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakMagnitudeErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositeRMSPhaseErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsCompositePeakPhaseErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSCHSymbolPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSCHDetectedModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDataPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDMRSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDMRSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHPTRSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHPTRSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDataREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDMRSREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHPTRSREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHDataTransientRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHPeakPhaseOffsetMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPUSCHPeakPhaseOffsetSlotIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHQPSKRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH16QAMRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH64QAMRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH256QAMRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH1024QAMRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH4096QAMRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCH8PSKRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDataPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDMRSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDMRSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHPTRSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHPTRSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDataREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHDMRSREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPDSCHPTRSREPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPSSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPSSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSSSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSSSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPBCHDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPBCHDataPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPBCHDMRSRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsPBCHDMRSPeakEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSubblockInBandEmissionMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessMarginSlotIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1MaximumToRange1Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2MaximumToRange2Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1MaximumToRange2Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2MaximumToRange1Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2Minimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1MaximumSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange1MinimumSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2MaximumSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSpectralFlatnessRange2MinimumSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierTimeOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierFrequencyErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierSlotFrequencyErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierSymbolClockErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierTimeAlignmentErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierSlotIQOriginOffsetMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierIQGainImbalanceMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierQuadratureErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierIQTimingSkewMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsComponentCarrierCrossPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSubblockLOComponentCarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSubblockLOSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsSubblockIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ModAccGetResultsNoiseCompensationApplied(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetChannelConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetChannelConfigurationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetSubblockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetSubblockOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfEUTRAOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfNROffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfNROffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfENDCOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfENDCOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetOffsetChannelSpacingAdjustment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetOffsetChannelSpacingAdjustment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetPowerUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPSetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_ACPGetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsComponentCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsComponentCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_CHPGetIntegrationBandwidthType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetIntegrationBandwidthType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_CHPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNoiseCalibrationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNoiseCalibrationAveragingAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNoiseCalibrationAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNoiseCompensationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_CHPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_CHPGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetResultsComponentCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_CHPGetResultsComponentCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetPowerIntegrationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetPowerIntegrationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetSpanAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetSpanAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWSetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_OBWGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_OBWGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_OBWGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_OBWSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_OBWGetResultsOccupiedBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWGetResultsAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWGetResultsStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_OBWGetResultsStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetUplinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetDownlinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetDownlinkMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetDeltaFMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetDeltaFMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetSubblockIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetSubblockAggregatedChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetComponentCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetComponentCarrierRatedOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetComponentCarrierRatedOutputPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetLimitFailMask(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetAbsoluteLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetAbsoluteLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetAbsoluteLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetAbsoluteLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetFFTWindow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsTotalAggregatedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsComponentCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsComponentCarrierRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsComponentCarrierAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsComponentCarrierPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_TXPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_TXPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_TXPGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_TXPSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_TXPGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_TXPSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_TXPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_TXPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_TXPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_TXPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_TXPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_TXPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_TXPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_TXPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_TXPGetResultsAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_TXPGetResultsPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetMeasurementIntervalAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetMeasurementIntervalAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTSetMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_PVTGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetOFFPowerExclusionBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTSetOFFPowerExclusionBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_PVTGetOFFPowerExclusionAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTSetOFFPowerExclusionAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxNR_PVTGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsAbsoluteOFFPowerBefore(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsAbsoluteOFFPowerAfter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsAbsoluteONPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsBurstWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsPeakWindowedOFFPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsPeakWindowedOFFPowerMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxNR_PVTGetResultsPeakWindowedOFFPowerTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXNR_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED                               0x0090400f
#define RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED                               0x00904077
#define RFMXNR_ATTR_PDSCH_PRESENT_IN_SSB_RESOURCE_BLOCK                                    0x00900097
#define RFMXNR_ATTR_SUBBLOCK_FREQUENCY_DEFINITION                                          0x00900011
#define RFMXNR_ATTR_MODACC_PHASE_TRACKING_ENABLED                                          0x00904051
#define RFMXNR_ATTR_MODACC_TIMING_TRACKING_ENABLED                                         0x00904052

// Values for RFMXNR_ATTR_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED
#define RFMXNR_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_FALSE                                 0
#define RFMXNR_VAL_MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED_TRUE                                  1

// Values for RFMXNR_ATTR_MODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED_FALSE                                 0
#define RFMXNR_VAL_MODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED_TRUE                                  1

// Values for RFMXNR_ATTR_PDSCH_PRESENT_IN_SSB_RESOURCE_BLOCK
#define RFMXNR_VAL_PDSCH_PRESENT_IN_SSB_RESOURCE_BLOCK_FALSE                                      0
#define RFMXNR_VAL_PDSCH_PRESENT_IN_SSB_RESOURCE_BLOCK_TRUE                                       1

// Values for RFMXNR_ATTR_SUBBLOCK_FREQUENCY_DEFINITION
#define RFMXNR_VAL_SUBBLOCK_FREQUENCY_DEFINITION_RELATIVE                                         0
#define RFMXNR_VAL_SUBBLOCK_FREQUENCY_DEFINITION_ABSOLUTE                                         1

// Values for RFMXNR_ATTR_MODACC_PHASE_TRACKING_ENABLED
#define RFMXNR_VAL_MODACC_PHASE_TRACKING_ENABLED_FALSE                                            0
#define RFMXNR_VAL_MODACC_PHASE_TRACKING_ENABLED_TRUE                                             1

// Values for RFMXNR_ATTR_MODACC_TIMING_TRACKING_ENABLED
#define RFMXNR_VAL_MODACC_TIMING_TRACKING_ENABLED_FALSE                                           0
#define RFMXNR_VAL_MODACC_TIMING_TRACKING_ENABLED_TRUE                                            1

// Values for RFMXNR_ATTR_FREQUENCY_RANGE
#define RFMXNR_VAL_FREQUENCY_RANGE_RANGE2                                                         1

// Values for RFMXNR_ATTR_MODACC_AUTO_LEVEL_ALLOW_OVERFLOW
#define RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_FALSE                                         0
#define RFMXNR_VAL_MODACC_ATUO_LEVEL_ALLOW_OVERFLOW_TRUE                                          1

// Values for RFMXNR_ATTR_DOWNLINK_TEST_MODEL_MODULATION_TYPE
#define RFMXNR_VAL_DOWNLINK_TEST_MODEL_MODULATION_TYPE_Standard                                   0

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxNR_AnalyzeIQ(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxNR_AnalyzeIQSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 I[],
   float32 Q[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxNR_AnalyzeSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[],
   float64 x0,
   float64 dx,
   float32 spectrum[],
   int32 arraySize,
   int32 reset,
   int32* averagingDone
);

int32 __stdcall RFmxNR_ModAccGetEVMWithExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetEVMWithExclusionPeriodEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetIQImpairmentsEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetIQImpairmentsEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ACPFetchSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower
);

int32 __stdcall RFmxNR_SEMFetchSubblockPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* subblockPower
);

int32 __stdcall RFmxNR_GetPDSCHPresentInSSBResourceBlock(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetPDSCHPresentInSSBResourceBlock(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_GetSubblockFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_SetSubblockFrequencyDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxNR_ModAccGetTimingTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxNR_ModAccSetTimingTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

#ifdef __cplusplus
}
#endif


#endif
````
