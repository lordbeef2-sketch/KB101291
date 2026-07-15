# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxVNA.h sha256=014880fb39a41bd17059d9932796ca27bcb2e09e47fe537452b78fb14f305bed bytes=125212 -->
## FILE: imports/include/niRFmxVNA.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxVNA.h`
- sha256: `014880fb39a41bd17059d9932796ca27bcb2e09e47fe537452b78fb14f305bed`
- bytes: 125212

````c

/****************************************************************************************************
*          National Instruments RFmx VNA
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2024.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxVNA.h
*
* Purpose:  National Instruments RFmx VNA,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_VNA_H__
#define __NI_RFMX_VNA_H__

#include "niRFmxInstr.h"

#define RFMXVNA_ATTR_TRIGGER_TYPE                                                0x00d00042
#define RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                 0x00d00043
#define RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                   0x00d00044
#define RFMXVNA_ATTR_TRIGGER_MODE                                                0x00d00045
#define RFMXVNA_ATTR_TRIGGER_DELAY                                               0x00d00070
#define RFMXVNA_ATTR_READY_FOR_TRIGGER_EVENT_OUTPUT_TERMINAL                     0x00d00063
#define RFMXVNA_ATTR_READY_FOR_TRIGGER_EVENT_TERMINAL_NAME                       0x00d00064
#define RFMXVNA_ATTR_READY_FOR_TRIGGER_EVENT_LEVEL                               0x00d00065
#define RFMXVNA_ATTR_INDEX_EVENT_OUTPUT_TERMINAL                                 0x00d00066
#define RFMXVNA_ATTR_INDEX_EVENT_TERMINAL_NAME                                   0x00d00067
#define RFMXVNA_ATTR_INDEX_EVENT_LEVEL                                           0x00d00068
#define RFMXVNA_ATTR_SWEEP_TYPE                                                  0x00d0002e
#define RFMXVNA_ATTR_FREQUENCY_LIST                                              0x00d00002
#define RFMXVNA_ATTR_START_FREQUENCY                                             0x00d00051
#define RFMXVNA_ATTR_STOP_FREQUENCY                                              0x00d00052
#define RFMXVNA_ATTR_CW_FREQUENCY                                                0x00d0006a
#define RFMXVNA_ATTR_NUMBER_OF_POINTS                                            0x00d00053
#define RFMXVNA_ATTR_POWER_LEVEL                                                 0x00d00003
#define RFMXVNA_ATTR_TEST_RECEIVER_ATTENUATION                                   0x00d0000a
#define RFMXVNA_ATTR_IF_BANDWIDTH                                                0x00d00004
#define RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED                           0x00d00046
#define RFMXVNA_ATTR_SWEEP_SEQUENCE                                              0x00d0002d
#define RFMXVNA_ATTR_SWEEP_DELAY                                                 0x00d00005
#define RFMXVNA_ATTR_DWELL_TIME                                                  0x00d00006
#define RFMXVNA_ATTR_NUMBER_OF_SEGMENTS                                          0x00d00001
#define RFMXVNA_ATTR_SEGMENT_ENABLED                                             0x00d0002f
#define RFMXVNA_ATTR_SEGMENT_START_FREQUENCY                                     0x00d00054
#define RFMXVNA_ATTR_SEGMENT_STOP_FREQUENCY                                      0x00d00055
#define RFMXVNA_ATTR_SEGMENT_NUMBER_OF_FREQUENCY_POINTS                          0x00d00056
#define RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED                                 0x00d00048
#define RFMXVNA_ATTR_SEGMENT_POWER_LEVEL                                         0x00d00049
#define RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH_ENABLED                                0x00d0004a
#define RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH                                        0x00d0004b
#define RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED                   0x00d0004c
#define RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION                           0x00d0004d
#define RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED                                  0x00d0004e
#define RFMXVNA_ATTR_SEGMENT_DWELL_TIME                                          0x00d0004f
#define RFMXVNA_ATTR_PULSE_MODE_ENABLED                                          0x00d00031
#define RFMXVNA_ATTR_PULSE_TRIGGER_TYPE                                          0x00d00033
#define RFMXVNA_ATTR_PULSE_DIGITAL_EDGE_TRIGGER_SOURCE                           0x00d00034
#define RFMXVNA_ATTR_PULSE_PERIOD                                                0x00d00035
#define RFMXVNA_ATTR_PULSE_MODULATOR_DELAY                                       0x00d00037
#define RFMXVNA_ATTR_PULSE_MODULATOR_WIDTH                                       0x00d00038
#define RFMXVNA_ATTR_PULSE_ACQUISITION_AUTO                                      0x00d00039
#define RFMXVNA_ATTR_PULSE_ACQUISITION_DELAY                                     0x00d0003a
#define RFMXVNA_ATTR_PULSE_ACQUISITION_WIDTH                                     0x00d0003b
#define RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED                                     0x00d0003e
#define RFMXVNA_ATTR_PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL                      0x00d0003f
#define RFMXVNA_ATTR_PULSE_GENERATOR_TERMINAL_NAME                               0x00d00050
#define RFMXVNA_ATTR_PULSE_GENERATOR_DELAY                                       0x00d00040
#define RFMXVNA_ATTR_PULSE_GENERATOR_WIDTH                                       0x00d00041
#define RFMXVNA_ATTR_X_AXIS_VALUES                                               0x00d00057
#define RFMXVNA_ATTR_AVERAGING_ENABLED                                           0x00d00007
#define RFMXVNA_ATTR_AVERAGING_COUNT                                             0x00d00008
#define RFMXVNA_ATTR_CORRECTION_ENABLED                                          0x00d0000b
#define RFMXVNA_ATTR_CORRECTION_INTERPOLATION_ENABLED                            0x00d00058
#define RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_ENABLED                              0x00d0000e
#define RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_FULL_PORTS                           0x00d0000f
#define RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_RESPONSE_PORTS                       0x00d00079
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED                           0x00d00026
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN                      0x00d0005f
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY                             0x00d00027
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE                          0x00d00060
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT                     0x00d00061
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_VELOCITY_FACTOR                   0x00d00062
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DC_LOSS_ENABLED                   0x00d00028
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DC_LOSS                           0x00d00029
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS1_ENABLED                     0x00d00059
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS1_FREQUENCY                   0x00d0005a
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS1                             0x00d0005b
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS2_ENABLED                     0x00d0005c
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS2_FREQUENCY                   0x00d0005d
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS2                             0x00d0005e
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_LOSS_ENABLED                 0x00d0007a
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_REGULARIZATION_ENABLED       0x00d0007b
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_FREQUENCY_MODE               0x00d0007c
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_START_FREQUENCY              0x00d0007d
#define RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_STOP_FREQUENCY               0x00d0007e
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_PORTS                                0x00d00010
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_CONNECTOR_TYPE                       0x00d00011
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_TYPE                          0x00d00012
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_RESOURCE_NAME      0x00d00013
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION        0x00d0001e
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_MECHANICAL_NAME               0x00d00014
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_METHOD                               0x00d00015
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_METHOD                          0x00d00017
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_COAX_DELAY                      0x00d00018
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_COUNT                           0x00d00019
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_STEP_DESCRIPTION                     0x00d0001a
#define RFMXVNA_ATTR_CORRECTION_CALIBRATION_ESTIMATED_THRU_DELAY                 0x00d00800
#define RFMXVNA_ATTR_CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION               0x00d00047
#define RFMXVNA_ATTR_SPARAMS_MEASUREMENT_ENABLED                                 0x00d01000
#define RFMXVNA_ATTR_SPARAMS_NUMBER_OF_SPARAMETERS                               0x00d01002
#define RFMXVNA_ATTR_SPARAMS_RECEIVER_PORT                                       0x00d01003
#define RFMXVNA_ATTR_SPARAMS_SOURCE_PORT                                         0x00d01004
#define RFMXVNA_ATTR_SPARAMS_FORMAT                                              0x00d01005
#define RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS                                     0x00d01006
#define RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE                                    0x00d01007
#define RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE                           0x00d0101c
#define RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_POINTS                         0x00d0101d
#define RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE                     0x00d0101e
#define RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_FREQUENCY_SPAN                 0x00d0101f
#define RFMXVNA_ATTR_SPARAMS_MATH_FUNCTION                                       0x00d0101a
#define RFMXVNA_ATTR_SPARAMS_MATH_ACTIVE_MEASUREMENT_MEMORY                      0x00d0101b
#define RFMXVNA_ATTR_SPARAMS_RESULTS_CORRECTION_STATE                            0x00d01018
#define RFMXVNA_ATTR_SPARAMS_RESULTS_CORRECTION_LEVEL                            0x00d01020
#define RFMXVNA_ATTR_SPARAMS_SNP_DATA_FORMAT                                     0x00d01013
#define RFMXVNA_ATTR_SPARAMS_SNP_USER_COMMENT                                    0x00d01014
#define RFMXVNA_ATTR_SPARAMS_SNP_PORTS                                           0x00d01015
#define RFMXVNA_ATTR_WAVES_MEASUREMENT_ENABLED                                   0x00d02000
#define RFMXVNA_ATTR_WAVES_NUMBER_OF_WAVES                                       0x00d02002
#define RFMXVNA_ATTR_WAVES_RECEIVER                                              0x00d02003
#define RFMXVNA_ATTR_WAVES_RECEIVER_PORT                                         0x00d02004
#define RFMXVNA_ATTR_WAVES_SOURCE_PORT                                           0x00d02005
#define RFMXVNA_ATTR_WAVES_FORMAT                                                0x00d02006
#define RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS                                       0x00d02007
#define RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE                                      0x00d02008
#define RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE                             0x00d02015
#define RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_POINTS                           0x00d02016
#define RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_PERCENTAGE                       0x00d02017
#define RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN                   0x00d02018
#define RFMXVNA_ATTR_WAVES_RESULTS_CORRECTION_STATE                              0x00d02013
#define RFMXVNA_ATTR_WAVES_RESULTS_CORRECTION_LEVEL                              0x00d02019
#define RFMXVNA_ATTR_IQ_MEASUREMENT_ENABLED                                      0x00d0100a
#define RFMXVNA_ATTR_IQ_ACQUISITION_TIME                                         0x00d0100d
#define RFMXVNA_ATTR_IQ_RECEIVER_PORT                                            0x00d0100f
#define RFMXVNA_ATTR_IQ_SOURCE_PORT                                              0x00d01010
#define RFMXVNA_ATTR_IQ_RESULTS_CORRECTION_STATE                                 0x00d01019
#define RFMXVNA_ATTR_LIMITED_CONFIGURATION_CHANGE                                0x00d0200b
#define RFMXVNA_ATTR_SOURCE_POWER_MODE                                           0x00d0200c
#define RFMXVNA_ATTR_GROUND_TERMINATED_PORTS                                     0x00d0200d
#define RFMXVNA_ATTR_RESULT_FETCH_TIMEOUT                                        0x00d0c000

// Values for RFMXVNA_ATTR_TRIGGER_TYPE
#define RFMXVNA_VAL_TRIGGER_TYPE_NONE                                                                             0
#define RFMXVNA_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                                     1
#define RFMXVNA_VAL_TRIGGER_TYPE_SOFTWARE                                                                         2

// Values for RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXVNA_VAL_PFI0_STR                                                                                      "PFI0"
#define RFMXVNA_VAL_PFI1_STR                                                                                      "PFI1"
#define RFMXVNA_VAL_PXI_TRIG0_STR                                                                                 "PXI_Trig0"
#define RFMXVNA_VAL_PXI_TRIG1_STR                                                                                 "PXI_Trig1"
#define RFMXVNA_VAL_PXI_TRIG2_STR                                                                                 "PXI_Trig2"
#define RFMXVNA_VAL_PXI_TRIG3_STR                                                                                 "PXI_Trig3"
#define RFMXVNA_VAL_PXI_TRIG4_STR                                                                                 "PXI_Trig4"
#define RFMXVNA_VAL_PXI_TRIG5_STR                                                                                 "PXI_Trig5"
#define RFMXVNA_VAL_PXI_TRIG6_STR                                                                                 "PXI_Trig6"
#define RFMXVNA_VAL_PXI_TRIG7_STR                                                                                 "PXI_Trig7"
#define RFMXVNA_VAL_PXI_STAR_STR                                                                                  "PXI_STAR"
#define RFMXVNA_VAL_PXIE_DSTARB_STR                                                                               "PXIe_DStarB"
#define RFMXVNA_VAL_TIMER_EVENT_STR                                                                               "TimerEvent"

// Values for RFMXVNA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXVNA_VAL_DIGITAL_EDGE_RISING_EDGE                                                                      0
#define RFMXVNA_VAL_DIGITAL_EDGE_FALLING_EDGE                                                                     1

// Values for RFMXVNA_ATTR_TRIGGER_MODE
#define RFMXVNA_VAL_TRIGGER_MODE_SIGNAL                                                                           0
#define RFMXVNA_VAL_TRIGGER_MODE_SWEEP                                                                            1
#define RFMXVNA_VAL_TRIGGER_MODE_POINT                                                                            2
#define RFMXVNA_VAL_TRIGGER_MODE_SEGMENT                                                                          3

// Values for RFMXVNA_ATTR_READY_FOR_TRIGGER_EVENT_LEVEL
#define RFMXVNA_VAL_READY_FOR_TRIGGER_EVENT_LEVEL_ACTIVE_HIGH                                                     0
#define RFMXVNA_VAL_READY_FOR_TRIGGER_EVENT_LEVEL_ACTIVE_LOW                                                      1

// Values for RFMXVNA_ATTR_INDEX_EVENT_LEVEL
#define RFMXVNA_VAL_INDEX_EVENT_LEVEL_ACTIVE_HIGH                                                                 0
#define RFMXVNA_VAL_INDEX_EVENT_LEVEL_ACTIVE_LOW                                                                  1

// Values for RFMXVNA_ATTR_SWEEP_TYPE
#define RFMXVNA_VAL_SWEEP_TYPE_LIST                                                                               0
#define RFMXVNA_VAL_SWEEP_TYPE_LINEAR                                                                             1
#define RFMXVNA_VAL_SWEEP_TYPE_SEGMENT                                                                            2
#define RFMXVNA_VAL_SWEEP_TYPE_CW_TIME                                                                            4

// Values for RFMXVNA_ATTR_AUTO_IF_BANDWIDTH_SCALING_ENABLED
#define RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_FALSE                                                       0
#define RFMXVNA_VAL_AUTO_IF_BANDWIDTH_SCALING_ENABLED_TRUE                                                        1

// Values for RFMXVNA_ATTR_SWEEP_SEQUENCE
#define RFMXVNA_VAL_SWEEP_SEQUENCE_STANDARD                                                                       0
#define RFMXVNA_VAL_SWEEP_SEQUENCE_POINT                                                                          1

// Values for RFMXVNA_ATTR_SEGMENT_ENABLED
#define RFMXVNA_VAL_SEGMENT_ENABLED_FALSE                                                                         0
#define RFMXVNA_VAL_SEGMENT_ENABLED_TRUE                                                                          1

// Values for RFMXVNA_ATTR_SEGMENT_POWER_LEVEL_ENABLED
#define RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_FALSE                                                             0
#define RFMXVNA_VAL_SEGMENT_POWER_LEVEL_ENABLED_TRUE                                                              1

// Values for RFMXVNA_ATTR_SEGMENT_IF_BANDWIDTH_ENABLED
#define RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_FALSE                                                            0
#define RFMXVNA_VAL_SEGMENT_IF_BANDWIDTH_ENABLED_TRUE                                                             1

// Values for RFMXVNA_ATTR_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED
#define RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_FALSE                                               0
#define RFMXVNA_VAL_SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED_TRUE                                                1

// Values for RFMXVNA_ATTR_SEGMENT_DWELL_TIME_ENABLED
#define RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_FALSE                                                              0
#define RFMXVNA_VAL_SEGMENT_DWELL_TIME_ENABLED_TRUE                                                               1

// Values for RFMXVNA_ATTR_PULSE_MODE_ENABLED
#define RFMXVNA_VAL_PULSE_MODE_ENABLED_FALSE                                                                      0
#define RFMXVNA_VAL_PULSE_MODE_ENABLED_TRUE                                                                       1

// Values for RFMXVNA_ATTR_PULSE_TRIGGER_TYPE
#define RFMXVNA_VAL_PULSE_TRIGGER_TYPE_NONE                                                                       0
#define RFMXVNA_VAL_PULSE_TRIGGER_TYPE_DIGITAL_EDGE                                                               1

// Values for RFMXVNA_ATTR_PULSE_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXVNA_VAL_PFI0_STR                                                                                      "PFI0"
#define RFMXVNA_VAL_PFI1_STR                                                                                      "PFI1"
#define RFMXVNA_VAL_PXI_TRIG0_STR                                                                                 "PXI_Trig0"
#define RFMXVNA_VAL_PXI_TRIG1_STR                                                                                 "PXI_Trig1"
#define RFMXVNA_VAL_PXI_TRIG2_STR                                                                                 "PXI_Trig2"
#define RFMXVNA_VAL_PXI_TRIG3_STR                                                                                 "PXI_Trig3"
#define RFMXVNA_VAL_PXI_TRIG4_STR                                                                                 "PXI_Trig4"
#define RFMXVNA_VAL_PXI_TRIG5_STR                                                                                 "PXI_Trig5"
#define RFMXVNA_VAL_PXI_TRIG6_STR                                                                                 "PXI_Trig6"
#define RFMXVNA_VAL_PXI_TRIG7_STR                                                                                 "PXI_Trig7"
#define RFMXVNA_VAL_PXI_STAR_STR                                                                                  "PXI_STAR"
#define RFMXVNA_VAL_PXIE_DSTARB_STR                                                                               "PXIe_DStarB"

// Values for RFMXVNA_ATTR_PULSE_ACQUISITION_AUTO
#define RFMXVNA_VAL_PULSE_ACQUISITION_AUTO_FALSE                                                                  0
#define RFMXVNA_VAL_PULSE_ACQUISITION_AUTO_TRUE                                                                   1

// Values for RFMXVNA_ATTR_PULSE_GENERATOR_ENABLED
#define RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_FALSE                                                                 0
#define RFMXVNA_VAL_PULSE_GENERATOR_ENABLED_TRUE                                                                  1

// Values for RFMXVNA_ATTR_AVERAGING_ENABLED
#define RFMXVNA_VAL_AVERAGING_ENABLED_FALSE                                                                       0
#define RFMXVNA_VAL_AVERAGING_ENABLED_TRUE                                                                        1

// Values for RFMXVNA_ATTR_CORRECTION_ENABLED
#define RFMXVNA_VAL_CORRECTION_ENABLED_FALSE                                                                      0
#define RFMXVNA_VAL_CORRECTION_ENABLED_TRUE                                                                       1

// Values for RFMXVNA_ATTR_CORRECTION_INTERPOLATION_ENABLED
#define RFMXVNA_VAL_CORRECTION_INTERPOLATION_ENABLED_FALSE                                                        0
#define RFMXVNA_VAL_CORRECTION_INTERPOLATION_ENABLED_TRUE                                                         1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_FALSE                                                          0
#define RFMXVNA_VAL_CORRECTION_PORT_SUBSET_ENABLED_TRUE                                                           1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_FALSE                                                       0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_ENABLED_TRUE                                                        1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN_DELAY                                                  0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DELAY_DOMAIN_DISTANCE                                               1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_METERS                                                0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_FEET                                                  1
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DISTANCE_UNIT_INCHES                                                2

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_DC_LOSS_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DC_LOSS_ENABLED_FALSE                                               0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_DC_LOSS_ENABLED_TRUE                                                1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS1_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_LOSS1_ENABLED_FALSE                                                 0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_LOSS1_ENABLED_TRUE                                                  1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_LOSS2_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_LOSS2_ENABLED_FALSE                                                 0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_LOSS2_ENABLED_TRUE                                                  1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_LOSS_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_LOSS_ENABLED_FALSE                                             0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_LOSS_ENABLED_TRUE                                              1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_REGULARIZATION_ENABLED
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_REGULARIZATION_ENABLED_FALSE                                   0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_REGULARIZATION_ENABLED_TRUE                                    1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_FREQUENCY_MODE
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_FREQUENCY_MODE_SWEEP                                           0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_FREQUENCY_MODE_USER                                            1

// Values for RFMXVNA_ATTR_CORRECTION_CALIBRATION_CALKIT_TYPE
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_CALKIT_TYPE_ELECTRONIC                                                 0
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_CALKIT_TYPE_MECHANICAL                                                 1

// Values for RFMXVNA_ATTR_CORRECTION_CALIBRATION_METHOD
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_METHOD_SOL                                                             0
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_METHOD_SOLT                                                            1
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_METHOD_TRL                                                             2

// Values for RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_METHOD
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_AUTO                                                       0
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_DEFINED_THRU                                               1
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_FLUSH_THRU                                                 2
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_UNDEFINED_THRU                                             3
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_VCAL_THRU_AS_UNKNOWN_THRU                                  5

// Values for RFMXVNA_ATTR_CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION
#define RFMXVNA_VAL_CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION_AUTO                                            0
#define RFMXVNA_VAL_CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION_DISABLED                                        1
#define RFMXVNA_VAL_CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION_ENABLED                                         2

// Values for RFMXVNA_ATTR_SPARAMS_FORMAT
#define RFMXVNA_VAL_SPARAMS_FORMAT_MAGNITUDE                                                                      0
#define RFMXVNA_VAL_SPARAMS_FORMAT_PHASE                                                                          1
#define RFMXVNA_VAL_SPARAMS_FORMAT_COMPLEX                                                                        2
#define RFMXVNA_VAL_SPARAMS_FORMAT_SWR                                                                            3
#define RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_IMPEDANCE                                                                4
#define RFMXVNA_VAL_SPARAMS_FORMAT_SMITH_ADMITTANCE                                                               5
#define RFMXVNA_VAL_SPARAMS_FORMAT_POLAR                                                                          6
#define RFMXVNA_VAL_SPARAMS_FORMAT_GROUP_DELAY                                                                    7

// Values for RFMXVNA_ATTR_SPARAMS_MAGNITUDE_UNITS
#define RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_DB                                                                    0
#define RFMXVNA_VAL_SPARAMS_MAGNITUDE_UNITS_LINEAR                                                                1

// Values for RFMXVNA_ATTR_SPARAMS_PHASE_TRACE_TYPE
#define RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_WRAPPED                                                              0
#define RFMXVNA_VAL_SPARAMS_PHASE_TRACE_TYPE_UNWRAPPED                                                            1

// Values for RFMXVNA_ATTR_SPARAMS_GROUP_DELAY_APERTURE_MODE
#define RFMXVNA_VAL_SPARAMS_GROUP_DELAY_APERTURE_MODE_POINTS                                                      0
#define RFMXVNA_VAL_SPARAMS_GROUP_DELAY_APERTURE_MODE_PERCENTAGE                                                  1
#define RFMXVNA_VAL_SPARAMS_GROUP_DELAY_APERTURE_MODE_FREQUENCY_SPAN                                              2

// Values for RFMXVNA_ATTR_SPARAMS_MATH_FUNCTION
#define RFMXVNA_VAL_SPARAMS_MATH_FUNCTION_OFF                                                                     0
#define RFMXVNA_VAL_SPARAMS_MATH_FUNCTION_ADD                                                                     1
#define RFMXVNA_VAL_SPARAMS_MATH_FUNCTION_SUBTRACT                                                                2
#define RFMXVNA_VAL_SPARAMS_MATH_FUNCTION_MULTIPLY                                                                3
#define RFMXVNA_VAL_SPARAMS_MATH_FUNCTION_DIVIDE                                                                  4

// Values for RFMXVNA_ATTR_SPARAMS_RESULTS_CORRECTION_STATE
#define RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_NONE                                                                 0
#define RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_CORRECTED                                                            1
#define RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_INTERPOLATED                                                         2
#define RFMXVNA_VAL_SPARAMS_CORRECTION_STATE_SETTINGS_MODIFIED                                                    3

// Values for RFMXVNA_ATTR_SPARAMS_SNP_DATA_FORMAT
#define RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_AUTO                                                                  0
#define RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LOG_MAGNITUDE_ANGLE                                                   1
#define RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_REAL_IMAGINARY                                                        2
#define RFMXVNA_VAL_SPARAMS_SNP_DATA_FORMAT_LINEAR_MAGNITUDE_ANGLE                                                3

// Values for RFMXVNA_ATTR_WAVES_RECEIVER
#define RFMXVNA_VAL_WAVES_RECEIVER_TEST                                                                           0
#define RFMXVNA_VAL_WAVES_RECEIVER_REFERENCE                                                                      1

// Values for RFMXVNA_ATTR_WAVES_FORMAT
#define RFMXVNA_VAL_WAVES_FORMAT_MAGNITUDE                                                                        0
#define RFMXVNA_VAL_WAVES_FORMAT_PHASE                                                                            1
#define RFMXVNA_VAL_WAVES_FORMAT_COMPLEX                                                                          2
#define RFMXVNA_VAL_WAVES_FORMAT_SWR                                                                              3
#define RFMXVNA_VAL_WAVES_FORMAT_SMITH_IMPEDANCE                                                                  4
#define RFMXVNA_VAL_WAVES_FORMAT_SMITH_ADMITTANCE                                                                 5
#define RFMXVNA_VAL_WAVES_FORMAT_POLAR                                                                            6
#define RFMXVNA_VAL_WAVES_FORMAT_GROUP_DELAY                                                                      7

// Values for RFMXVNA_ATTR_WAVES_MAGNITUDE_UNITS
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBM                                                                     0
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMV                                                                    1
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBUV                                                                    2
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_DBMA                                                                    3
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_W                                                                       4
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_V                                                                       5
#define RFMXVNA_VAL_WAVES_MAGNITUDE_UNITS_A                                                                       6

// Values for RFMXVNA_ATTR_WAVES_PHASE_TRACE_TYPE
#define RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_WRAPPED                                                                0
#define RFMXVNA_VAL_WAVES_PHASE_TRACE_TYPE_UNWRAPPED                                                              1

// Values for RFMXVNA_ATTR_WAVES_GROUP_DELAY_APERTURE_MODE
#define RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_POINTS                                                        0
#define RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_PERCENTAGE                                                    1
#define RFMXVNA_VAL_WAVES_GROUP_DELAY_APERTURE_MODE_FREQUENCY_SPAN                                                2

// Values for RFMXVNA_ATTR_WAVES_RESULTS_CORRECTION_STATE
#define RFMXVNA_VAL_WAVES_CORRECTION_STATE_NONE                                                                   0
#define RFMXVNA_VAL_WAVES_CORRECTION_STATE_CORRECTED                                                              1
#define RFMXVNA_VAL_WAVES_CORRECTION_STATE_INTERPOLATED                                                           2
#define RFMXVNA_VAL_WAVES_CORRECTION_STATE_SETTINGS_MODIFIED                                                      3

// Values for RFMXVNA_ATTR_IQ_RESULTS_CORRECTION_STATE
#define RFMXVNA_VAL_IQ_CORRECTION_STATE_NONE                                                                      0
#define RFMXVNA_VAL_IQ_CORRECTION_STATE_CORRECTED                                                                 1
#define RFMXVNA_VAL_IQ_CORRECTION_STATE_INTERPOLATED                                                              2
#define RFMXVNA_VAL_IQ_CORRECTION_STATE_SETTINGS_MODIFIED                                                         3

// Values for RFMXVNA_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                                         0
#define RFMXVNA_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                                        1

// Values for RFMXVNA_ATTR_SOURCE_POWER_MODE
#define RFMXVNA_VAL_SOURCE_POWER_MODE_AUTO                                                                        0
#define RFMXVNA_VAL_SOURCE_POWER_MODE_OFF                                                                         1

// Values for FrequencyReferenceSource
#define RFMXVNA_VAL_ONBOARD_CLOCK_STR                                                                             "OnboardClock"
#define RFMXVNA_VAL_REF_IN_STR                                                                                    "RefIn"
#define RFMXVNA_VAL_PXI_CLK_STR                                                                                   "PXI_Clk"
#define RFMXVNA_VAL_CLK_IN_STR                                                                                    "ClkIn"
#define RFMXVNA_VAL_REF_IN2_STR                                                                                   "RefIn2"
#define RFMXVNA_VAL_PXI_CLK_MASTER_STR                                                                            "PXI_Clk_Master"

// Values for Boolean
#define RFMXVNA_VAL_FALSE                                                                                         0
#define RFMXVNA_VAL_TRUE                                                                                          1

// Values for RestoreConfiguration
#define RFMXVNA_VAL_RESTORE_CONFIGURATION_NONE                                                                    0
#define RFMXVNA_VAL_RESTORE_CONFIGURATION_STIMULUS                                                                1

// Values for MeasurementTypes
#define RFMXVNA_VAL_SPARAMS                                                                                       1<<0
#define RFMXVNA_VAL_WAVES                                                                                         1<<1
#define RFMXVNA_VAL_IQ                                                                                            1<<2
#define RFMXVNA_VAL_INTEGRATEDPOWER                                                                               1<<3

// Values for CalFrequencyGrid
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_DIRECTIVITY                                                                0
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_SOURCE_MATCH                                                               1
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_REFLECTION_TRACKING                                                        2
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_TRANSMISSION_TRACKING                                                      3
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_LOAD_MATCH                                                                 4
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_K                                                                          5
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_ALPHA                                                                      6
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_BETA                                                                       7
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_GAMMA                                                                      8
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_DELTA                                                                      9
#define RFMXVNA_VAL_CAL_FREQUENCY_GRID_SWITCH_TERM                                                                10

// Values for CalErrorTerm
#define RFMXVNA_VAL_CAL_ERROR_TERM_DIRECTIVITY                                                                    0
#define RFMXVNA_VAL_CAL_ERROR_TERM_SOURCE_MATCH                                                                   1
#define RFMXVNA_VAL_CAL_ERROR_TERM_REFLECTION_TRACKING                                                            2
#define RFMXVNA_VAL_CAL_ERROR_TERM_TRANSMISSION_TRACKING                                                          3
#define RFMXVNA_VAL_CAL_ERROR_TERM_LOAD_MATCH                                                                     4
#define RFMXVNA_VAL_CAL_ERROR_TERM_K                                                                              5
#define RFMXVNA_VAL_CAL_ERROR_TERM_ALPHA                                                                          6
#define RFMXVNA_VAL_CAL_ERROR_TERM_BETA                                                                           7
#define RFMXVNA_VAL_CAL_ERROR_TERM_GAMMA                                                                          8
#define RFMXVNA_VAL_CAL_ERROR_TERM_DELTA                                                                          9
#define RFMXVNA_VAL_CAL_ERROR_TERM_SWITCH_TERM                                                                    10

// Values for SParameterOrientation
#define RFMXVNA_VAL_SPARAMETER_ORIENTATION_PORT1_TOWARDS_VNA                                                      0
#define RFMXVNA_VAL_SPARAMETER_ORIENTATION_PORT2_TOWARDS_VNA                                                      1

// Values for CalkitManagerCalkitConnectorGender
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CONNECTOR_GENDER_MALE                                                   0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CONNECTOR_GENDER_FEMALE                                                 1
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CONNECTOR_GENDER_NO_GENDER                                              2

// Values for CalkitManagerCalkitTrlReferencePlane
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_TRL_REFERENCE_PLANE_THRU                                                0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_TRL_REFERENCE_PLANE_REFLECT                                             1

// Values for CalkitManagerCalkitCalibrationElementType
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_LOAD                                           0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_OPEN                                           1
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_SHORT                                          2
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_THRU                                           3
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_LINE                                           4
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_REFLECT                                        5
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_TYPE_TERMINATION                                    6

// Values for CalkitManagerCalkitCalibrationElementSParameterDefinition
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_DEFINITION_REFLECT_MODEL                 0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_DEFINITION_SPARAMETER                    1
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_DEFINITION_DELAY_MODEL                   2
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_DEFINITION_UNKNOWN                       3

// Values for CalkitManagerCalkitCalibrationElementReflectModelType
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_REFLECT_MODEL_TYPE_REFLECT_OPEN                     0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_REFLECT_MODEL_TYPE_REFLECT_SHORT                    1
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_REFLECT_MODEL_TYPE_LOAD                             2

// Values for CalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_REFLECT_MODEL_SPARAMETER_AVAILABILITY_ESTIMATE      0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_REFLECT_MODEL_SPARAMETER_AVAILABILITY_KNOWN         1

// Values for CalkitManagerCalkitCalibrationElementSParameterAvailability
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_AVAILABILITY_ESTIMATE                    0
#define RFMXVNA_VAL_CALKIT_MANAGER_CALKIT_CALIBRATION_ELEMENT_SPARAMETER_AVAILABILITY_KNOWN                       1

// Values for MarkerSearchMode
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NONE                                                                       0
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_MAX                                                                        1
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_MIN                                                                        2
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_PEAK                                                                       3
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NEXT_PEAK                                                                  4
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NEXT_LEFT_PEAK                                                             5
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NEXT_RIGHT_PEAK                                                            6
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_TARGET                                                                     7
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NEXT_LEFT_TARGET                                                           8
#define RFMXVNA_VAL_MARKER_SEARCH_MODE_NEXT_RIGHT_TARGET                                                          9

// Values for MarkerType
#define RFMXVNA_VAL_MARKER_TYPE_OFF                                                                               0
#define RFMXVNA_VAL_MARKER_TYPE_NORMAL                                                                            1
#define RFMXVNA_VAL_MARKER_TYPE_DELTA                                                                             2
#define RFMXVNA_VAL_MARKER_TYPE_FIXED                                                                             3

// Values for MarkerPeakSearchThresholdEnabled
#define RFMXVNA_VAL_MARKER_PEAK_SEARCH_THRESHOLD_ENABLED_FALSE                                                    0
#define RFMXVNA_VAL_MARKER_PEAK_SEARCH_THRESHOLD_ENABLED_TRUE                                                     1

// Values for MarkerPeakSearchExcursionEnabled
#define RFMXVNA_VAL_MARKER_PEAK_SEARCH_EXCURSION_ENABLED_FALSE                                                    0
#define RFMXVNA_VAL_MARKER_PEAK_SEARCH_EXCURSION_ENABLED_TRUE                                                     1

// Values for MarkerMode
#define RFMXVNA_VAL_MARKER_MODE_CONTINUOUS                                                                        0
#define RFMXVNA_VAL_MARKER_MODE_DISCRETE                                                                          1

// Values for RFAttenuationAuto
#define RFMXVNA_VAL_RF_ATTENUATION_AUTO_FALSE                                                                     0
#define RFMXVNA_VAL_RF_ATTENUATION_AUTO_TRUE                                                                      1

// Values for MechanicalAttenuationAuto
#define RFMXVNA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                                             0
#define RFMXVNA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                                              1

// Values for RFMXVNA_ATTR_CORRECTION_PORT_EXTENSION_AUTO_STANDARD
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_STANDARD_OPEN                                                  0
#define RFMXVNA_VAL_CORRECTION_PORT_EXTENSION_AUTO_STANDARD_SHORT                                                 1

/* ---------------- RFmxVNA APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxVNA_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxVNA_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxVNA_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxVNA_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxVNA_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxVNA_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxVNA_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxVNA_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxVNA_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxVNA_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxVNA_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxVNA_BuildPortString(
   char selectorString[],
   char portString[],
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildSegmentString(
   char selectorString[],
   int32 segmentNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildSParameterString(
   char selectorString[],
   int32 sParameterNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildWaveString(
   char selectorString[],
   int32 waveNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildCalstepString(
   char selectorString[],
   int32 calstepNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildCalkitString(
   char selectorString[],
   char calkitID[],
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildConnectorString(
   char selectorString[],
   char connectorID[],
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildCalibrationElementString(
   char selectorString[],
   char calibrationElementID[],
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildPulseGeneratorString(
   char selectorString[],
   int32 pulseGeneratorNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildMarkerString(
   char selectorString[],
   int32 markerNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_BuildMeasurementMemoryString(
   char selectorString[],
   char measurementMemoryName[],
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxVNA_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxVNA_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxVNA_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsCfgSParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char sParameter[]
);

int32 __stdcall RFmxVNA_SParamsExportToSnPFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char snpFilePath[]
);

int32 __stdcall RFmxVNA_WavesCfgWave(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char wave[]
);

int32 __stdcall RFmxVNA_CalibrationInitiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CalibrationAcquire(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxVNA_CalibrationAbort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CalibrationSave(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[]
);

int32 __stdcall RFmxVNA_ClearCalset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[]
);

int32 __stdcall RFmxVNA_CalsetLoadFromFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   char calsetFilePath[]
);

int32 __stdcall RFmxVNA_CalsetSaveToFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   char calsetFilePath[]
);

int32 __stdcall RFmxVNA_AutoDetectvCalOrientation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxVNA_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CopyCalset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char sourceCalsetName[],
   char newCalsetName[]
);

int32 __stdcall RFmxVNA_SelectActiveCalset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   int32 restoreConfiguration
);

int32 __stdcall RFmxVNA_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxVNA_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxVNA_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxVNA_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxVNA_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxVNA_CalsetEmbedFixtureS2p(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   char fixtureS2pFilePath[],
   char vnaPort[],
   int32 sParameterOrientation,
   char newCalsetName[]
);

int32 __stdcall RFmxVNA_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxVNA_DeselectActiveCalset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_LoadDataToMeasurementMemoryFromFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char filePath[],
   char parameter[],
   char measurementMemoryName[]
);

int32 __stdcall RFmxVNA_CopyDataToMeasurementMemory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char measurementMemoryName[]
);

int32 __stdcall RFmxVNA_ClearMeasurementMemoryNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_AutoPortExtensionMeasure(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 standard,
   char port[]
);

int32 __stdcall RFmxVNA_AutoPortExtensionReset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_CalkitManagerImportCalkit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitFilePath[]
);

int32 __stdcall RFmxVNA_CalkitManagerExportCalkit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitID[],
   char calkitFilePath[]
);

int32 __stdcall RFmxVNA_CalkitManagerCreateCalkit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitID[]
);

int32 __stdcall RFmxVNA_CalkitManagerRemoveCalkit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitID[]
);

int32 __stdcall RFmxVNA_CalkitManagerValidateCalkit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitID[]
);

int32 __stdcall RFmxVNA_CalkitManagerGetCalkitIDs(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char calkitIDs[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitAddConnector(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char connectorID[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveConnector(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char connectorID[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetConnectorIDs(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char connectorIDs[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitAddCalibrationElement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calibrationElementID[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitRemoveCalibrationElement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calibrationElementID[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetCalibrationElementIDs(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char calibrationElementIDs[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitSetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitDescription[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char calkitDescription[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitSetVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calkitVersion[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetVersion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char calkitVersion[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitSetTRLReferencePlane(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 referencePlane
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitSetLRLLineAutoChar(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 autoCharacterizationEnabled
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char description[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char description[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetGender(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 connectorGender
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char connectorType[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char connectorType[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetImpedance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 impedance
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMinimumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 minimumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorSetMaximumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 maximumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char description[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char description[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetPortConnectors(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char connectorIDs[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetPortConnectors(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char connectorIDs[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetSParameterDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sParameterDefinition
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMinimumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 minimumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetMaximumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 maximumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetModelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 modelType
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sParameterAvailability
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC0(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 c0
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 c1
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 c2
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetC3(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 c3
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetDelay
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetLoss
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetZ0
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceImpedance
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementDelayModelSetDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 delay
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sParameterAvailability
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetFromFile(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char fileName[]
);

int32 __stdcall RFmxVNA_MarkerCfgNumberOfMarkers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfMarkers
);

int32 __stdcall RFmxVNA_MarkerCfgType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 markerType
);

int32 __stdcall RFmxVNA_MarkerCfgReferenceMarker(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 referenceMarker
);

int32 __stdcall RFmxVNA_MarkerCfgDataSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char dataSource[]
);

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchThreshold(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 thresholdEnabled,
   float64 threshold
);

int32 __stdcall RFmxVNA_MarkerCfgPeakSearchExcursion(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 peakExcursionEnabled,
   float64 peakExcursion
);

int32 __stdcall RFmxVNA_MarkerCfgMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 markerMode
);

int32 __stdcall RFmxVNA_MarkerCfgTargetValue(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 targetValue
);

int32 __stdcall RFmxVNA_MarkerCfgX(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 markerX
);

int32 __stdcall RFmxVNA_MarkerCfgY(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 markerY1,
   float64 markerY2
);

int32 __stdcall RFmxVNA_CalsetGetFrequencyGrid(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   int32 errorTermIdentifier,
   float64 frequencyGrid[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalsetGetErrorTerm(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   int32 errorTermIdentifier,
   char measurementPort[],
   char sourcePort[],
   NIComplexSingle errorTerm[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalsetGetErrorTermSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char calsetName[],
   int32 errorTermIdentifier,
   char measurementPort[],
   char sourcePort[],
   float32 errorTermI[],
   float32 errorTermQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetTypes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 calibrationElementTypes[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 frequency[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s11[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s11I[],
   float64 s11Q[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s12[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s12I[],
   float64 s12Q[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s21[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s21I[],
   float64 s21Q[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s22[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s22I[],
   float64 s22Q[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_MarkerSearch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 searchMode
);

int32 __stdcall RFmxVNA_MarkerFetchX(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* markerX
);

int32 __stdcall RFmxVNA_MarkerFetchY(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* markerY1,
   float64* markerY2
);

int32 __stdcall RFmxVNA_SParamsGetSParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char sParameter[]
);

int32 __stdcall RFmxVNA_WavesGetWave(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char wave[]
);

int32 __stdcall RFmxVNA_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxVNA_GetAllCalsetNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char calsetNames[]
);

int32 __stdcall RFmxVNA_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxVNA_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxVNA_GetMeasurementMemoryNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char measurementMemoryNames[]
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSetTypes(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 calibrationElementTypes[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 frequency[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS11(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s11[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS11Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s11I[],
   float64 s11Q[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS12(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s12[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS12Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s12I[],
   float64 s12Q[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS21(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s21[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS21Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s21I[],
   float64 s21Q[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS22(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   NIComplexDouble s22[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS22Split(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 s22I[],
   float64 s22Q[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_SParamsFetchXData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 X[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SParamsFetchYData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 Y1[],
   float32 Y2[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_WavesFetchXData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 X[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_WavesFetchYData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 Y1[],
   float32 Y2[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_IQFetchData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   NIComplexSingle data[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_IQFetchDataSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 dataI[],
   float32 dataQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_GetMeasurementMemoryXData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementMemoryX[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_GetMeasurementMemoryYData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float32 measurementMemoryY1[],
   float32 measurementMemoryY2[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetTRLReferencePlane(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* referencePlane
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitGetLRLLineAutoChar(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* autoCharacterizationEnabled
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetGender(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* connectorGender
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetImpedance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* impedance
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMinimumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* minimumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitConnectorGetMaximumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* maximumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetSParameterDefinition(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* sParameterDefinition
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetMinimumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* minimumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementGetMaximumFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* maximumFrequency
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetModelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* modelType
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetSParamAvailability(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* sParameterAvailability
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC0(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* c0
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* c1
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* c2
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetC3(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* c3
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetOffsetDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* offsetDelay
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* offsetLoss
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetOffsetZ0(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* offsetZ0
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* referenceImpedance
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementDelayModelGetDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64* delay
);

int32 __stdcall RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* sParameterAvailability
);

int32 __stdcall RFmxVNA_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetTriggerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetTriggerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetReadyForTriggerEventOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetReadyForTriggerEventOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetReadyForTriggerEventTerminalName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetReadyForTriggerEventLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetReadyForTriggerEventLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetIndexEventOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetIndexEventOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetIndexEventTerminalName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetIndexEventLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetIndexEventLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSweepType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSweepType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetFrequencyList(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal[],
   int32 arraySize,
   int32 *actualArraySize
);

int32 __stdcall RFmxVNA_SetFrequencyList(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxVNA_GetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCWFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCWFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetNumberOfPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetNumberOfPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetPowerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPowerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetTestReceiverAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetTestReceiverAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetIFBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetIFBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetAutoIFBandwidthScalingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetAutoIFBandwidthScalingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSweepSequence(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSweepSequence(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSweepDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSweepDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetDwellTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetDwellTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetNumberOfSegments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetNumberOfSegments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentNumberOfFrequencyPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentNumberOfFrequencyPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentPowerLevelEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentPowerLevelEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentPowerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentPowerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentIFBandwidthEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentIFBandwidthEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentIFBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentIFBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentTestReceiverAttenuationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentTestReceiverAttenuationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentTestReceiverAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentTestReceiverAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentDwellTimeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentDwellTimeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSegmentDwellTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetSegmentDwellTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetPulseTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetPulseDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetPulseDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetPulsePeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulsePeriod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseModulatorDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseModulatorDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseModulatorWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseModulatorWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseAcquisitionAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseAcquisitionAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetPulseAcquisitionDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseAcquisitionDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseAcquisitionWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseAcquisitionWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseGeneratorEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseGeneratorEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetPulseGeneratorExportOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetPulseGeneratorExportOutputTerminal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetPulseGeneratorTerminalName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetPulseGeneratorDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseGeneratorDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetPulseGeneratorWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetPulseGeneratorWidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetXAxisValues(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal[],
   int32 arraySize,
   int32 *actualArraySize
);

int32 __stdcall RFmxVNA_GetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionInterpolationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionInterpolationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortSubsetEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortSubsetEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortSubsetFullPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionPortSubsetFullPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionPortSubsetResponsePorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionPortSubsetResponsePorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDelayDomain(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDelayDomain(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDistance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDistance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDistanceUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDistanceUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionVelocityFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionVelocityFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDCLossEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDCLossEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionDCLoss(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionDCLoss(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss1Enabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss1Enabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss1Frequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss1Frequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss2Enabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss2Enabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss2Frequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss2Frequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionLoss2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionLoss2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionAutoLossEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionAutoLossEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionAutoRegularizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionAutoRegularizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionAutoFrequencyMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionAutoFrequencyMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionAutoStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionAutoStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortExtensionAutoStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionPortExtensionAutoStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationConnectorType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationConnectorType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationCalkitType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationCalkitType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationCalkitElectronicResourceName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationCalkitElectronicResourceName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationCalkitElectronicOrientation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationCalkitElectronicOrientation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationCalkitMechanicalName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationCalkitMechanicalName(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationThruMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationThruMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationThruCoaxDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationThruCoaxDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationStepCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionCalibrationStepCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationStepDescription(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetCorrectionCalibrationEstimatedThruDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionSwitchPortsMultipathCalibration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetCorrectionSwitchPortsMultipathCalibration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetSourcePowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetSourcePowerMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetGroundTerminatedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetGroundTerminatedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetNumberOfSParameters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetNumberOfSParameters(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsSetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsGetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsSetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsGetFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetMagnitudeUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetMagnitudeUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetPhaseTraceType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetPhaseTraceType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetGroupDelayApertureMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetGroupDelayApertureMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetGroupDelayAperturePoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetGroupDelayAperturePoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetGroupDelayAperturePercentage(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetGroupDelayAperturePercentage(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetGroupDelayApertureFrequencySpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetGroupDelayApertureFrequencySpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetMathFunction(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetMathFunction(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetMathActiveMeasurementMemory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsSetMathActiveMeasurementMemory(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsGetResultsCorrectionState(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsGetResultsCorrectionLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsGetSnPDataFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SParamsSetSnPDataFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_SParamsGetSnPUserComment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsSetSnPUserComment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsGetSnPPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SParamsSetSnPPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_WavesGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetNumberOfWaves(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetNumberOfWaves(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetReceiver(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetReceiver(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_WavesSetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_WavesGetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_WavesSetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_WavesGetFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetMagnitudeUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetMagnitudeUnits(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetPhaseTraceType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetPhaseTraceType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetGroupDelayApertureMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetGroupDelayApertureMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_WavesGetGroupDelayAperturePoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetGroupDelayAperturePoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_WavesGetGroupDelayAperturePercentage(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetGroupDelayAperturePercentage(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_WavesGetGroupDelayApertureFrequencySpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_WavesSetGroupDelayApertureFrequencySpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_WavesGetResultsCorrectionState(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_WavesGetResultsCorrectionLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_IQGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_IQSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_IQGetAcquisitionTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxVNA_IQSetAcquisitionTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxVNA_IQGetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_IQSetReceiverPort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_IQGetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_IQSetSourcePort(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_IQGetResultsCorrectionState(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXVNA_ATTR_CORRECTION_PORT_SUBSET_PORTS                                0x00d0000f
#define RFMXVNA_ATTR_NUMBER_OF_FREQUENCY_POINTS                                  0x00d00053
// Values for RFMXVNA_ATTR_CORRECTION_CALIBRATION_THRU_METHOD
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_UNDEFINED_THRU_USING_DEFINED_THRU                          4
#define RFMXVNA_VAL_CORRECTION_CALIBRATION_THRU_METHOD_DELAY_THRU_USING_DEFINED_THRU                              5

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxVNA_CfgFrequencyListStartStopPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 startFrequency,
   float64 stopFrequency,
   int32 numberOfPoints
);

int32 __stdcall RFmxVNA_SParamsFetchRealData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 realData[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SParamsFetchComplexData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle complexData[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_SParamsFetchComplexDataSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 complexDataI[],
   float32 complexDataQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_WavesFetchRealData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 realData[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_WavesFetchComplexData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle complexData[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_WavesFetchComplexDataSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 complexDataI[],
   float32 complexDataQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxVNA_GetNumberOfFrequencyPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxVNA_SetNumberOfFrequencyPoints(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxVNA_GetCorrectionPortSubsetPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxVNA_SetCorrectionPortSubsetPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxVNA_CfgCorrectionPortSubset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char portSubset[]
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxWCDMA.h sha256=7f581370939033c74866b9a9fcc8084d15e8413f82faa3dda99edc597614ca5c bytes=160388 -->
## FILE: imports/include/niRFmxWCDMA.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxWCDMA.h`
- sha256: `7f581370939033c74866b9a9fcc8084d15e8413f82faa3dda99edc597614ca5c`
- bytes: 160388

````c

/****************************************************************************************************
*          National Instruments RFmx WCDMA
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2021.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxWCDMA.h
*
* Purpose:  National Instruments RFmx WCDMA,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_WCDMA_H__
#define __NI_RFMX_WCDMA_H__

#include "niRFmxInstr.h"

#define RFMXWCDMA_ATTR_MODACC_MEASUREMENT_ENABLED                                     0x00511000
#define RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE                                    0x00511002
#define RFMXWCDMA_ATTR_MODACC_MEASUREMENT_OFFSET                                      0x00511003
#define RFMXWCDMA_ATTR_MODACC_MEASUREMENT_LENGTH                                      0x00511004
#define RFMXWCDMA_ATTR_MODACC_SPECTRUM_INVERTED                                       0x00511005
#define RFMXWCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED                               0x00511006
#define RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED                       0x0051103c
#define RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED                     0x0051103d
#define RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED                               0x00511007
#define RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED                                      0x0051103b
#define RFMXWCDMA_ATTR_MODACC_ALL_TRACES_ENABLED                                      0x00511008
#define RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR                0x00511009
#define RFMXWCDMA_ATTR_MODACC_DOWNLINK_TIMING_CHANNEL_CODE                            0x0051100a
#define RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_EVM                                         0x00511011
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_EVM                                        0x00511012
#define RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_MAGNITUDE_ERROR                             0x00511013
#define RFMXWCDMA_ATTR_MODACC_RESULTS_RMS_PHASE_ERROR                                 0x00511014
#define RFMXWCDMA_ATTR_MODACC_RESULTS_RHO                                             0x00511015
#define RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_ORIGIN_OFFSET                                0x00511016
#define RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_GAIN_IMBALANCE                               0x0051102d
#define RFMXWCDMA_ATTR_MODACC_RESULTS_IQ_QUADRATURE_ERROR                             0x0051102e
#define RFMXWCDMA_ATTR_MODACC_RESULTS_FREQUENCY_ERROR                                 0x00511017
#define RFMXWCDMA_ATTR_MODACC_RESULTS_CHIP_RATE_ERROR                                 0x00511018
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE                                        0x00511019
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_CODE                                   0x0051101b
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH                                 0x0051102a
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE                                 0x0051101c
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR                0x0051101d
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_CODE                            0x0051101e
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH                          0x0051102b
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PSCH_POWER                                      0x0051101f
#define RFMXWCDMA_ATTR_MODACC_RESULTS_SSCH_POWER                                      0x00511020
#define RFMXWCDMA_ATTR_MODACC_RESULTS_DPCH_TIMING_OFFSET                              0x00511021
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE                                       0x00511022
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR                      0x00511023
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_CODE                                  0x00511024
#define RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH                                0x0051102c
#define RFMXWCDMA_ATTR_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS                     0x00511025
#define RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_FACTOR                       0x00511026
#define RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_SPREADING_CODE                         0x00511027
#define RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE                        0x00511028
#define RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH                                 0x00511029
#define RFMXWCDMA_ATTR_ACP_MEASUREMENT_ENABLED                                        0x00501000
#define RFMXWCDMA_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH                              0x00501005
#define RFMXWCDMA_ATTR_ACP_NUMBER_OF_OFFSETS                                          0x00501008
#define RFMXWCDMA_ATTR_ACP_OFFSET_FREQUENCY                                           0x0050100a
#define RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER                             0x0050100c
#define RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_SPECIFIC                            0x0050100d
#define RFMXWCDMA_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH                               0x0050100e
#define RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH                                  0x0050101b
#define RFMXWCDMA_ATTR_ACP_RBW_FILTER_BANDWIDTH                                       0x0050101c
#define RFMXWCDMA_ATTR_ACP_RBW_FILTER_TYPE                                            0x0050101d
#define RFMXWCDMA_ATTR_ACP_SWEEP_TIME_AUTO                                            0x0050101e
#define RFMXWCDMA_ATTR_ACP_SWEEP_TIME_INTERVAL                                        0x0050101f
#define RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD                                         0x00501012
#define RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED                                 0x00501020
#define RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED                                          0x00501016
#define RFMXWCDMA_ATTR_ACP_AVERAGING_COUNT                                            0x00501015
#define RFMXWCDMA_ATTR_ACP_AVERAGING_TYPE                                             0x00501018
#define RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO                                0x00501034
#define RFMXWCDMA_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET                                0x00501035
#define RFMXWCDMA_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET                                 0x00501036
#define RFMXWCDMA_ATTR_ACP_ALL_TRACES_ENABLED                                         0x00501021
#define RFMXWCDMA_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS                                 0x00501014
#define RFMXWCDMA_ATTR_ACP_RESULTS_TOTAL_CARRIER_POWER                                0x00501022
#define RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_ABSOLUTE_POWER                             0x00501026
#define RFMXWCDMA_ATTR_ACP_RESULTS_CARRIER_RELATIVE_POWER                             0x00501027
#define RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER                        0x0050102c
#define RFMXWCDMA_ATTR_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER                        0x0050102d
#define RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER                        0x00501032
#define RFMXWCDMA_ATTR_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER                        0x00501033
#define RFMXWCDMA_ATTR_CHP_MEASUREMENT_ENABLED                                        0x00503000
#define RFMXWCDMA_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH                              0x00503002
#define RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH                                  0x0050300c
#define RFMXWCDMA_ATTR_CHP_RBW_FILTER_BANDWIDTH                                       0x0050300d
#define RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE                                            0x0050300e
#define RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO                                            0x00503011
#define RFMXWCDMA_ATTR_CHP_SWEEP_TIME_INTERVAL                                        0x00503012
#define RFMXWCDMA_ATTR_CHP_AVERAGING_ENABLED                                          0x00503007
#define RFMXWCDMA_ATTR_CHP_AVERAGING_COUNT                                            0x00503006
#define RFMXWCDMA_ATTR_CHP_AVERAGING_TYPE                                             0x00503009
#define RFMXWCDMA_ATTR_CHP_ALL_TRACES_ENABLED                                         0x00503014
#define RFMXWCDMA_ATTR_CHP_NUMBER_OF_ANALYSIS_THREADS                                 0x00503003
#define RFMXWCDMA_ATTR_CHP_RESULTS_TOTAL_CARRIER_POWER                                0x00503018
#define RFMXWCDMA_ATTR_CHP_RESULTS_CARRIER_ABSOLUTE_POWER                             0x00503015
#define RFMXWCDMA_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER                             0x00503019
#define RFMXWCDMA_ATTR_OBW_MEASUREMENT_ENABLED                                        0x00506000
#define RFMXWCDMA_ATTR_OBW_SPAN                                                       0x00506004
#define RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH                                  0x0050600c
#define RFMXWCDMA_ATTR_OBW_RBW_FILTER_BANDWIDTH                                       0x0050600d
#define RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE                                            0x0050600e
#define RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO                                            0x0050600f
#define RFMXWCDMA_ATTR_OBW_SWEEP_TIME_INTERVAL                                        0x00506010
#define RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED                                          0x00506007
#define RFMXWCDMA_ATTR_OBW_AVERAGING_COUNT                                            0x00506006
#define RFMXWCDMA_ATTR_OBW_AVERAGING_TYPE                                             0x00506009
#define RFMXWCDMA_ATTR_OBW_ALL_TRACES_ENABLED                                         0x00506012
#define RFMXWCDMA_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS                                 0x00506003
#define RFMXWCDMA_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH                                 0x00506013
#define RFMXWCDMA_ATTR_OBW_RESULTS_ABSOLUTE_POWER                                     0x00506014
#define RFMXWCDMA_ATTR_OBW_RESULTS_START_FREQUENCY                                    0x00506015
#define RFMXWCDMA_ATTR_OBW_RESULTS_STOP_FREQUENCY                                     0x00506016
#define RFMXWCDMA_ATTR_SEM_MEASUREMENT_ENABLED                                        0x00508000
#define RFMXWCDMA_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH                              0x00508005
#define RFMXWCDMA_ATTR_SEM_NUMBER_OF_OFFSETS                                          0x0050800b
#define RFMXWCDMA_ATTR_SEM_OFFSET_START_FREQUENCY                                     0x00508014
#define RFMXWCDMA_ATTR_SEM_OFFSET_STOP_FREQUENCY                                      0x00508015
#define RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_BANDWIDTH                                0x00508017
#define RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPE                                     0x00508018
#define RFMXWCDMA_ATTR_SEM_OFFSET_BANDWIDTH_INTEGRAL                                  0x0050800c
#define RFMXWCDMA_ATTR_SEM_SWEEP_TIME_AUTO                                            0x00508025
#define RFMXWCDMA_ATTR_SEM_SWEEP_TIME_INTERVAL                                        0x00508026
#define RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED                                          0x0050801f
#define RFMXWCDMA_ATTR_SEM_AVERAGING_COUNT                                            0x0050801e
#define RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE                                             0x00508021
#define RFMXWCDMA_ATTR_SEM_ALL_TRACES_ENABLED                                         0x00508027
#define RFMXWCDMA_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                                 0x0050801d
#define RFMXWCDMA_ATTR_SEM_RESULTS_TOTAL_CARRIER_POWER                                0x00508028
#define RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS                                 0x00508029
#define RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER                  0x0050802e
#define RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER                  0x0050802d
#define RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER                        0x0050802f
#define RFMXWCDMA_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY                             0x00508030
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS                    0x0050803d
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER             0x00508034
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER             0x00508035
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER                   0x00508036
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER                   0x00508037
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                        0x00508038
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                                0x00508039
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER                 0x0050803a
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER                 0x0050803b
#define RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY                      0x0050803c
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS                    0x0050804a
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER             0x00508041
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER             0x00508042
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER                   0x00508043
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER                   0x00508044
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                        0x00508045
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                                0x00508046
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER                 0x00508047
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER                 0x00508048
#define RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY                      0x00508049
#define RFMXWCDMA_ATTR_QEVM_MEASUREMENT_ENABLED                                       0x00512000
#define RFMXWCDMA_ATTR_QEVM_MEASUREMENT_LENGTH                                        0x00512003
#define RFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLED                                         0x00512005
#define RFMXWCDMA_ATTR_QEVM_AVERAGING_COUNT                                           0x00512006
#define RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED                                         0x00512007
#define RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED                                 0x00512008
#define RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED                                        0x0051200b
#define RFMXWCDMA_ATTR_QEVM_ALL_TRACES_ENABLED                                        0x0051200c
#define RFMXWCDMA_ATTR_QEVM_NUMBER_OF_ANALYSIS_THREADS                                0x0051200d
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_RMS_EVM                                      0x0051200e
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_RMS_EVM                                   0x0051200f
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_PEAK_EVM                                     0x00512010
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PEAK_EVM                                  0x00512011
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR                              0x00512012
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR                           0x00512013
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_PHASE_ERROR                                  0x00512014
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_PHASE_ERROR                               0x00512015
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_FREQUENCY_ERROR                              0x00512016
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR                           0x00512017
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET                             0x00512018
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET                          0x00512019
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR                              0x0051201a
#define RFMXWCDMA_ATTR_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR                           0x0051201b
#define RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_ENABLED                                  0x00514000
#define RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE                                 0x00514002
#define RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_OFFSET                                   0x00514003
#define RFMXWCDMA_ATTR_SLOTPHASE_MEASUREMENT_LENGTH                                   0x00514004
#define RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED                                    0x00514007
#define RFMXWCDMA_ATTR_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED                            0x00514008
#define RFMXWCDMA_ATTR_SLOTPHASE_RRC_FILTER_ENABLED                                   0x00514009
#define RFMXWCDMA_ATTR_SLOTPHASE_ALL_TRACES_ENABLED                                   0x0051400c
#define RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY                  0x0051400e
#define RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1      0x0051400f
#define RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT2      0x00514010
#define RFMXWCDMA_ATTR_SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE               0x00514011
#define RFMXWCDMA_ATTR_LIMITED_CONFIGURATION_CHANGE                                   0x0050d003
#define RFMXWCDMA_ATTR_RESULT_FETCH_TIMEOUT                                           0x0050c000
#define RFMXWCDMA_ATTR_CENTER_FREQUENCY                                               0x00500001
#define RFMXWCDMA_ATTR_REFERENCE_LEVEL                                                0x00500002
#define RFMXWCDMA_ATTR_EXTERNAL_ATTENUATION                                           0x00500003
#define RFMXWCDMA_ATTR_TRIGGER_TYPE                                                   0x00500004
#define RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                    0x00500005
#define RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                      0x00500006
#define RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                   0x00500007
#define RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                    0x00500008
#define RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                               0x00500fff
#define RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                    0x00500009
#define RFMXWCDMA_ATTR_TRIGGER_DELAY                                                  0x0050000a
#define RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                0x0050000b
#define RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                            0x0050000c
#define RFMXWCDMA_ATTR_LINK_DIRECTION                                                 0x0050000d
#define RFMXWCDMA_ATTR_BAND                                                           0x00500020
#define RFMXWCDMA_ATTR_NUMBER_OF_CARRIERS                                             0x0050000e
#define RFMXWCDMA_ATTR_CARRIER_FREQUENCY                                              0x0050000f
#define RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE                                     0x00500010
#define RFMXWCDMA_ATTR_NUMBER_OF_CHANNELS                                             0x00500014
#define RFMXWCDMA_ATTR_SPREADING_FACTOR                                               0x00500015
#define RFMXWCDMA_ATTR_SPREADING_CODE                                                 0x00500016
#define RFMXWCDMA_ATTR_MODULATION_TYPE                                                0x00500017
#define RFMXWCDMA_ATTR_BRANCH                                                         0x00500018
#define RFMXWCDMA_ATTR_UPLINK_TEST_MODEL                                              0x00500019
#define RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL                                            0x0050001a
#define RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_TYPE                                         0x0050001b
#define RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_CODE                                         0x0050001c
#define RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_TYPE                                       0x0050001d
#define RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_PRIMARY_CODE                               0x0050001e
#define RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_SECONDARY_CODE                             0x0050001f
#define RFMXWCDMA_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                             0x0050d000
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_ENABLED                                        0x00515000
#define RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE                                       0x00515002
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_OFFSET                                         0x00515003
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_LENGTH                                         0x00515004
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR                       0x00515009
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_SPREADING_CODE                         0x0051500a
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE                        0x0051500b
#define RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH                                 0x0051500c
#define RFMXWCDMA_ATTR_CDA_POWER_UNIT                                                 0x0051500d
#define RFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTED                                          0x00515005
#define RFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED                                  0x00515006
#define RFMXWCDMA_ATTR_CDA_RRC_FILTER_ENABLED                                         0x00515007
#define RFMXWCDMA_ATTR_CDA_ALL_TRACES_ENABLED                                         0x00515015
#define RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_EVM                                     0x00515017
#define RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_SYMBOL_EVM                                    0x00515018
#define RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR                         0x00515019
#define RFMXWCDMA_ATTR_CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR                             0x0051501a
#define RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_SYMBOL_POWER                                  0x0051501c
#define RFMXWCDMA_ATTR_CDA_RESULTS_CHIP_RATE_ERROR                                    0x0051502d
#define RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_POWER                                        0x0051501b
#define RFMXWCDMA_ATTR_CDA_RESULTS_TOTAL_ACTIVE_POWER                                 0x0051501f
#define RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_ACTIVE_POWER                                  0x00515022
#define RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_ACTIVE_POWER                                  0x00515021
#define RFMXWCDMA_ATTR_CDA_RESULTS_MEAN_INACTIVE_POWER                                0x00515024
#define RFMXWCDMA_ATTR_CDA_RESULTS_PEAK_INACTIVE_POWER                                0x00515023
#define RFMXWCDMA_ATTR_CDA_RESULTS_I_MEAN_ACTIVE_POWER                                0x00515029
#define RFMXWCDMA_ATTR_CDA_RESULTS_Q_MEAN_ACTIVE_POWER                                0x0051502a
#define RFMXWCDMA_ATTR_CDA_RESULTS_I_PEAK_INACTIVE_POWER                              0x0051502b
#define RFMXWCDMA_ATTR_CDA_RESULTS_Q_PEAK_INACTIVE_POWER                              0x0051502c
#define RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_ENABLED                                  0x00516000
#define RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE                                 0x00516007
#define RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_OFFSET                                   0x00516002
#define RFMXWCDMA_ATTR_SLOTPOWER_MEASUREMENT_LENGTH                                   0x00516003
#define RFMXWCDMA_ATTR_SLOTPOWER_SPECTRUM_INVERTED                                    0x00516004
#define RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED                                   0x00516005
#define RFMXWCDMA_ATTR_MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET                  0x0051102f
#define RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE                                  0x00501038
#define RFMXWCDMA_ATTR_ACP_SEQUENTIAL_FFT_SIZE                                        0x00501039
#define RFMXWCDMA_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE                                  0x0050301b
#define RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE                                  0x0050601a
#define RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE                                  0x0050804c
#define RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE                                       0x0050d001
#define RFMXWCDMA_ATTR_SELECTED_PORTS                                                 0x00500ffd
#define RFMXWCDMA_ATTR_REFERENCE_LEVEL_HEADROOM                                       0x00500ffc
#define RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE                                           0x0050103a
#define RFMXWCDMA_ATTR_ACP_FFT_OVERLAP                                                0x0050103b

// Values for RFMXWCDMA_ATTR_TRIGGER_TYPE
#define RFMXWCDMA_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXWCDMA_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXWCDMA_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXWCDMA_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXWCDMA_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXWCDMA_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXWCDMA_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXWCDMA_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXWCDMA_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXWCDMA_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXWCDMA_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXWCDMA_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXWCDMA_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXWCDMA_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXWCDMA_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXWCDMA_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXWCDMA_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXWCDMA_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXWCDMA_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXWCDMA_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXWCDMA_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXWCDMA_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXWCDMA_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXWCDMA_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXWCDMA_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXWCDMA_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXWCDMA_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXWCDMA_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXWCDMA_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXWCDMA_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXWCDMA_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXWCDMA_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXWCDMA_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXWCDMA_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXWCDMA_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXWCDMA_ATTR_CHANNEL_CONFIGURATION_MODE
#define RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT                                         0
#define RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_USER_DEFINED                                        1
#define RFMXWCDMA_VAL_CHANNEL_CONFIGURATION_MODE_TEST_MODEL                                          2

// Values for RFMXWCDMA_ATTR_MODULATION_TYPE
#define RFMXWCDMA_VAL_MODULATION_TYPE_BPSK_QPSK                                                      0
#define RFMXWCDMA_VAL_MODULATION_TYPE_4PAM_16QAM                                                     1
#define RFMXWCDMA_VAL_MODULATION_TYPE_64QAM                                                          2

// Values for RFMXWCDMA_ATTR_BRANCH
#define RFMXWCDMA_VAL_BRANCH_I                                                                       0
#define RFMXWCDMA_VAL_BRANCH_Q                                                                       1
#define RFMXWCDMA_VAL_BRANCH_I_AND_Q                                                                 2

// Values for RFMXWCDMA_ATTR_UPLINK_TEST_MODEL
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_1                                                      0
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_2                                                      1
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_3                                                      2
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_4                                                      3
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_2_5                                                      4
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST1                                          5
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST2                                          6
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST3                                          7
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST4                                          8
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST5                                          9
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R6C_10_1_4_SUBTEST6                                          10
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST1                                          11
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST2                                          12
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST3                                          13
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_10_1_4_SUBTEST4                                          14
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST1                                          15
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST2                                          16
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST3                                          17
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST4                                          18
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R7C_11_1_3_SUBTEST5                                          19
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST1                                          20
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST2                                          21
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST3                                          22
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST4                                          23
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_3_SUBTEST5                                          24
#define RFMXWCDMA_VAL_UPLINK_TEST_MODEL_R8C_11_1_4_SUBTEST1                                          25

// Values for RFMXWCDMA_ATTR_DOWNLINK_TEST_MODEL
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_16DPCH                                        0
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_32DPCH                                        1
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_64DPCH                                        2
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_16DPCH_SCCPCH                                 3
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_32DPCH_SCCPCH                                 4
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_1_64DPCH_SCCPCH                                 5
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_2                                               6
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_2_SCCPCH                                        7
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_16DPCH                                        8
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_32DPCH                                        9
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_16DPCH_SCCPCH                                 10
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_3_32DPCH_SCCPCH                                 11
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_4                                               12
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_4_PCPICH                                        13
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_2HSPDSCH_16QAM                                14
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_4HSPDSCH_4DPCH_16QAM                          15
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_4HSPDSCH_14DPCH_16QAM                         16
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_5_8HSPDSCH_16QAM                                17
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_6_4HSPDSCH_64QAM                                18
#define RFMXWCDMA_VAL_DOWNLINK_TEST_MODEL_TEST_MODEL_6_8HSPDSCH_64QAM                                19

// Values for RFMXWCDMA_ATTR_UPLINK_SCRAMBLING_TYPE
#define RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_LONG                                                    0
#define RFMXWCDMA_VAL_UPLINK_SCRAMBLING_TYPE_SHORT                                                   1

// Values for RFMXWCDMA_ATTR_DOWNLINK_SCRAMBLING_TYPE
#define RFMXWCDMA_VAL_DOWNLINK_SCRAMBLING_TYPE_STANDARD                                              0
#define RFMXWCDMA_VAL_DOWNLINK_SCRAMBLING_TYPE_LEFT                                                  1
#define RFMXWCDMA_VAL_DOWNLINK_SCRAMBLING_TYPE_RIGHT                                                 2

// Values for RFMXWCDMA_ATTR_MODACC_SYNCHRONIZATION_MODE
#define RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_FRAME                                              0
#define RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_SLOT                                               1
#define RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_ARBITRARY                                          2
#define RFMXWCDMA_VAL_MODACC_SYNCHRONIZATION_MODE_MARKER                                             3

// Values for RFMXWCDMA_ATTR_MODACC_SPECTRUM_INVERTED
#define RFMXWCDMA_VAL_MODACC_SPECTRUM_INVERTED_FALSE                                                 0
#define RFMXWCDMA_VAL_MODACC_SPECTRUM_INVERTED_TRUE                                                  1

// Values for RFMXWCDMA_ATTR_MODACC_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                         0
#define RFMXWCDMA_VAL_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                          1

// Values for RFMXWCDMA_ATTR_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE                                 0
#define RFMXWCDMA_VAL_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE                                  1

// Values for RFMXWCDMA_ATTR_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE                               0
#define RFMXWCDMA_VAL_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE                                1

// Values for RFMXWCDMA_ATTR_MODACC_TRANSIENT_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_MODACC_TRANSIENT_REMOVAL_ENABLED_FALSE                                         0
#define RFMXWCDMA_VAL_MODACC_TRANSIENT_REMOVAL_ENABLED_TRUE                                          1

// Values for RFMXWCDMA_ATTR_MODACC_RRC_FILTER_ENABLED
#define RFMXWCDMA_VAL_MODACC_RRC_FILTER_ENABLED_FALSE                                                0
#define RFMXWCDMA_VAL_MODACC_RRC_FILTER_ENABLED_TRUE                                                 1

// Values for RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_CDE_BRANCH
#define RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I                                                       0
#define RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_Q                                                       1
#define RFMXWCDMA_VAL_MODACC_PEAK_CDE_BRANCH_I_AND_Q                                                 2

// Values for RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH
#define RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I                                                0
#define RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q                                                1
#define RFMXWCDMA_VAL_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q                                          2

// Values for RFMXWCDMA_ATTR_MODACC_RESULTS_PEAK_RCDE_BRANCH
#define RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I                                                      0
#define RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_Q                                                      1
#define RFMXWCDMA_VAL_MODACC_PEAK_RCDE_BRANCH_I_AND_Q                                                2

// Values for RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_MODULATION_TYPE
#define RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_BPSK_QPSK                                      0
#define RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_4PAM_16QAM                                     1
#define RFMXWCDMA_VAL_MODACC_DETECTED_MODULATION_TYPE_64QAM                                          2

// Values for RFMXWCDMA_ATTR_MODACC_RESULTS_DETECTED_BRANCH
#define RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I                                                       0
#define RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_Q                                                       1
#define RFMXWCDMA_VAL_MODACC_DETECTED_BRANCH_I_AND_Q                                                 2

// Values for RFMXWCDMA_ATTR_ACP_OFFSET_POWER_REFERENCE_CARRIER
#define RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_CLOSEST                                     0
#define RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_HIGHEST                                     1
#define RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_COMPOSITE                                   2
#define RFMXWCDMA_VAL_ACP_OFFSET_POWER_REFERENCE_CARRIER_SPECIFIC                                    3

// Values for RFMXWCDMA_ATTR_ACP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXWCDMA_VAL_ACP_RBW_AUTO_FALSE                                                             0
#define RFMXWCDMA_VAL_ACP_RBW_AUTO_TRUE                                                              1

// Values for RFMXWCDMA_ATTR_ACP_RBW_FILTER_TYPE
#define RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXWCDMA_VAL_ACP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXWCDMA_ATTR_ACP_SWEEP_TIME_AUTO
#define RFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXWCDMA_VAL_ACP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXWCDMA_ATTR_ACP_MEASUREMENT_METHOD
#define RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_NORMAL                                                  0
#define RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE                                           1
#define RFMXWCDMA_VAL_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT                                          2

// Values for RFMXWCDMA_ATTR_ACP_NOISE_COMPENSATION_ENABLED
#define RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_FALSE                                           0
#define RFMXWCDMA_VAL_ACP_NOISE_COMPENSATION_ENABLED_TRUE                                            1

// Values for RFMXWCDMA_ATTR_ACP_AVERAGING_ENABLED
#define RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWCDMA_VAL_ACP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWCDMA_ATTR_ACP_AVERAGING_TYPE
#define RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_RMS                                                         0
#define RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_LOG                                                         1
#define RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MAX                                                         3
#define RFMXWCDMA_VAL_ACP_AVERAGING_TYPE_MIN                                                         4

// Values for RFMXWCDMA_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO
#define RFMXWCDMA_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE                                          0
#define RFMXWCDMA_VAL_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE                                           1

// Values for RFMXWCDMA_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXWCDMA_VAL_CHP_RBW_AUTO_FALSE                                                             0
#define RFMXWCDMA_VAL_CHP_RBW_AUTO_TRUE                                                              1

// Values for RFMXWCDMA_ATTR_CHP_RBW_FILTER_TYPE
#define RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXWCDMA_VAL_CHP_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXWCDMA_ATTR_CHP_SWEEP_TIME_AUTO
#define RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXWCDMA_VAL_CHP_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXWCDMA_ATTR_CHP_AVERAGING_ENABLED
#define RFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWCDMA_VAL_CHP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWCDMA_ATTR_CHP_AVERAGING_TYPE
#define RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_RMS                                                         0
#define RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_LOG                                                         1
#define RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MAX                                                         3
#define RFMXWCDMA_VAL_CHP_AVERAGING_TYPE_MIN                                                         4

// Values for RFMXWCDMA_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH
#define RFMXWCDMA_VAL_OBW_RBW_AUTO_FALSE                                                             0
#define RFMXWCDMA_VAL_OBW_RBW_AUTO_TRUE                                                              1

// Values for RFMXWCDMA_ATTR_OBW_RBW_FILTER_TYPE
#define RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FFT_BASED                                                  0
#define RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_GAUSSIAN                                                   1
#define RFMXWCDMA_VAL_OBW_RBW_FILTER_TYPE_FLAT                                                       2

// Values for RFMXWCDMA_ATTR_OBW_SWEEP_TIME_AUTO
#define RFMXWCDMA_VAL_OBW_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXWCDMA_VAL_OBW_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXWCDMA_ATTR_OBW_AVERAGING_ENABLED
#define RFMXWCDMA_VAL_OBW_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWCDMA_VAL_OBW_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWCDMA_ATTR_OBW_AVERAGING_TYPE
#define RFMXWCDMA_VAL_OBW_AVERAGING_TYPE_RMS                                                         0
#define RFMXWCDMA_VAL_OBW_AVERAGING_TYPE_LOG                                                         1
#define RFMXWCDMA_VAL_OBW_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXWCDMA_VAL_OBW_AVERAGING_TYPE_MAX                                                         3
#define RFMXWCDMA_VAL_OBW_AVERAGING_TYPE_MIN                                                         4

// Values for RFMXWCDMA_ATTR_SEM_OFFSET_RBW_FILTER_TYPE
#define RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED                                           0
#define RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN                                            1
#define RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_FLAT                                                2
#define RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4                                       3
#define RFMXWCDMA_VAL_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5                                       4

// Values for RFMXWCDMA_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXWCDMA_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXWCDMA_ATTR_SEM_AVERAGING_ENABLED
#define RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWCDMA_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWCDMA_ATTR_SEM_AVERAGING_TYPE
#define RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MAX                                                         3
#define RFMXWCDMA_VAL_SEM_AVERAGING_TYPE_MIN                                                         4

// Values for RFMXWCDMA_ATTR_SEM_RESULTS_MEASUREMENT_STATUS
#define RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXWCDMA_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXWCDMA_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXWCDMA_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXWCDMA_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXWCDMA_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXWCDMA_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXWCDMA_ATTR_QEVM_AVERAGING_ENABLED
#define RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_FALSE                                                   0
#define RFMXWCDMA_VAL_QEVM_AVERAGING_ENABLED_TRUE                                                    1

// Values for RFMXWCDMA_ATTR_QEVM_SPECTRUM_INVERTED
#define RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_FALSE                                                   0
#define RFMXWCDMA_VAL_QEVM_SPECTRUM_INVERTED_TRUE                                                    1

// Values for RFMXWCDMA_ATTR_QEVM_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                           0
#define RFMXWCDMA_VAL_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                            1

// Values for RFMXWCDMA_ATTR_QEVM_RRC_FILTER_ENABLED
#define RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_FALSE                                                  0
#define RFMXWCDMA_VAL_QEVM_RRC_FILTER_ENABLED_TRUE                                                   1

// Values for RFMXWCDMA_ATTR_SLOTPHASE_SYNCHRONIZATION_MODE
#define RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXWCDMA_VAL_SLOTPHASE_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXWCDMA_ATTR_SLOTPHASE_SPECTRUM_INVERTED
#define RFMXWCDMA_VAL_SLOTPHASE_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXWCDMA_VAL_SLOTPHASE_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXWCDMA_ATTR_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED_FALSE                                      0
#define RFMXWCDMA_VAL_SLOTPHASE_TRANSIENT_REMOVAL_ENABLED_TRUE                                       1

// Values for RFMXWCDMA_ATTR_SLOTPHASE_RRC_FILTER_ENABLED
#define RFMXWCDMA_VAL_SLOTPHASE_RRC_FILTER_ENABLED_FALSE                                             0
#define RFMXWCDMA_VAL_SLOTPHASE_RRC_FILTER_ENABLED_TRUE                                              1

// Values for RFMXWCDMA_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXWCDMA_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for Boolean
#define RFMXWCDMA_VAL_FALSE                                                                          0
#define RFMXWCDMA_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXWCDMA_VAL_MODACC                                                                         1 << 0
#define RFMXWCDMA_VAL_ACP                                                                            1 << 1
#define RFMXWCDMA_VAL_CHP                                                                            1 << 2
#define RFMXWCDMA_VAL_OBW                                                                            1 << 3
#define RFMXWCDMA_VAL_SEM                                                                            1 << 4
#define RFMXWCDMA_VAL_QEVM                                                                           1 << 5
#define RFMXWCDMA_VAL_SLOTPHASE                                                                      1 << 6
#define RFMXWCDMA_VAL_CDA                                                                            1 << 7
#define RFMXWCDMA_VAL_SLOTPOWER                                                                      1 << 8

// Values for FrequencyReferenceSource
#define RFMXWCDMA_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXWCDMA_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXWCDMA_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXWCDMA_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for RFMXWCDMA_ATTR_LINK_DIRECTION
#define RFMXWCDMA_VAL_LINK_DIRECTION_DOWNLINK                                                        0
#define RFMXWCDMA_VAL_LINK_DIRECTION_UPLINK                                                          1

// Values for RFAttenuationAuto
#define RFMXWCDMA_VAL_RF_ATTENUATION_AUTO_FALSE                                                      0
#define RFMXWCDMA_VAL_RF_ATTENUATION_AUTO_TRUE                                                       1

// Values for MechanicalAttenuationAuto
#define RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_FALSE                                              0
#define RFMXWCDMA_VAL_MECHANICAL_ATTENUATION_AUTO_TRUE                                               1

// Values for RFMXWCDMA_ATTR_CDA_SYNCHRONIZATION_MODE
#define RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_FRAME                                                 0
#define RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_SLOT                                                  1
#define RFMXWCDMA_VAL_CDA_SYNCHRONIZATION_MODE_ARBITRARY                                             2

// Values for RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE
#define RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_BPSK_QPSK                              0
#define RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE_4PAM_16QAM                             1

// Values for RFMXWCDMA_ATTR_CDA_MEASUREMENT_CHANNEL_BRANCH
#define RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_I                                               0
#define RFMXWCDMA_VAL_CDA_MEASUREMENT_CHANNEL_BRANCH_Q                                               1

// Values for RFMXWCDMA_ATTR_CDA_POWER_UNIT
#define RFMXWCDMA_VAL_CDA_POWER_UNIT_DB                                                              0
#define RFMXWCDMA_VAL_CDA_POWER_UNIT_DBM                                                             1

// Values for RFMXWCDMA_ATTR_CDA_SPECTRUM_INVERTED
#define RFMXWCDMA_VAL_CDA_SPECTRUM_INVERTED_FALSE                                                    0
#define RFMXWCDMA_VAL_CDA_SPECTRUM_INVERTED_TRUE                                                     1

// Values for RFMXWCDMA_ATTR_CDA_IQ_OFFSET_REMOVAL_ENABLED
#define RFMXWCDMA_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE                                            0
#define RFMXWCDMA_VAL_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE                                             1

// Values for RFMXWCDMA_ATTR_CDA_RRC_FILTER_ENABLED
#define RFMXWCDMA_VAL_CDA_RRC_FILTER_ENABLED_FALSE                                                   0
#define RFMXWCDMA_VAL_CDA_RRC_FILTER_ENABLED_TRUE                                                    1

// Values for RFMXWCDMA_ATTR_SLOTPOWER_SYNCHRONIZATION_MODE
#define RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_FRAME                                           0
#define RFMXWCDMA_VAL_SLOTPOWER_SYNCHRONIZATION_MODE_SLOT                                            1

// Values for RFMXWCDMA_ATTR_SLOTPOWER_SPECTRUM_INVERTED
#define RFMXWCDMA_VAL_SLOTPOWER_SPECTRUM_INVERTED_FALSE                                              0
#define RFMXWCDMA_VAL_SLOTPOWER_SPECTRUM_INVERTED_TRUE                                               1

// Values for RFMXWCDMA_ATTR_SLOTPOWER_RRC_FILTER_ENABLED
#define RFMXWCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_FALSE                                             0
#define RFMXWCDMA_VAL_SLOTPOWER_RRC_FILTER_ENABLED_TRUE                                              1

// Values for RFMXWCDMA_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE
#define RFMXWCDMA_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXWCDMA_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXWCDMA_ATTR_CHP_AMPLITUDE_CORRECTION_TYPE
#define RFMXWCDMA_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXWCDMA_VAL_CHP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXWCDMA_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE
#define RFMXWCDMA_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXWCDMA_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXWCDMA_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE
#define RFMXWCDMA_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXWCDMA_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXWCDMA_ATTR_TRANSMITTER_ARCHITECTURE
#define RFMXWCDMA_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_CARRIER                                        0
#define RFMXWCDMA_VAL_TRANSMITTER_ARCHITECTURE_LO_PER_BAND                                           1

// Values for RFMXWCDMA_ATTR_ACP_FFT_OVERLAP_MODE
#define RFMXWCDMA_VAL_ACP_FFT_OVERLAP_MODE_DISABLED                                                  0
#define RFMXWCDMA_VAL_ACP_FFT_OVERLAP_MODE_AUTOMATIC                                                 1

/* ---------------- RFmxWCDMA APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxWCDMA_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxWCDMA_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxWCDMA_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxWCDMA_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxWCDMA_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxWCDMA_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxWCDMA_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxWCDMA_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxWCDMA_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxWCDMA_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxWCDMA_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_BuildCarrierString(
   char selectorString[],
   int32 carrierNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWCDMA_BuildChannelString(
   char selectorString[],
   int32 channelNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWCDMA_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWCDMA_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxWCDMA_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxWCDMA_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval,
   float64* referenceLevel
);

int32 __stdcall RFmxWCDMA_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* done
);

int32 __stdcall RFmxWCDMA_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxWCDMA_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxWCDMA_AnalyzeIQ1Waveform(
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

int32 __stdcall RFmxWCDMA_AnalyzeIQ1WaveformSplit(
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

int32 __stdcall RFmxWCDMA_AnalyzeSpectrum1Waveform(
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

int32 __stdcall RFmxWCDMA_CfgContiguousCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfCarriers,
   int32 carrierAtCenterFrequency
);

int32 __stdcall RFmxWCDMA_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxWCDMA_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxWCDMA_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxWCDMA_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   NIComplexSingle referenceWaveform[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_ModAccCfgReferenceWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_CfgNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfCarriers
);

int32 __stdcall RFmxWCDMA_CfgNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfChannels
);

int32 __stdcall RFmxWCDMA_CfgUplinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkTestModel
);

int32 __stdcall RFmxWCDMA_CfgUplinkScrambling(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkScramblingCode,
   int32 uplinkScramblingType
);

int32 __stdcall RFmxWCDMA_CfgUserDefinedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 spreadingFactor,
   int32 spreadingCode,
   int32 modulationType,
   int32 branch
);

int32 __stdcall RFmxWCDMA_CfgRF(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency,
   float64 referenceLevel,
   float64 externalAttenuation
);

int32 __stdcall RFmxWCDMA_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxWCDMA_CfgBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 band
);

int32 __stdcall RFmxWCDMA_CfgCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 carrierFrequency
);

int32 __stdcall RFmxWCDMA_CfgChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelConfigurationMode
);

int32 __stdcall RFmxWCDMA_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxWCDMA_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxWCDMA_CfgUserDefinedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 spreadingFactor[],
   int32 spreadingCode[],
   int32 modulationType[],
   int32 branch[],
   int32 numberOfElements
);

int32 __stdcall RFmxWCDMA_CfgCarrierFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 carrierFrequency[],
   int32 numberOfElements
);

int32 __stdcall RFmxWCDMA_CfgUplinkScramblingArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkScramblingType[],
   int32 uplinkScramblingCode[],
   int32 numberOfElements
);

int32 __stdcall RFmxWCDMA_CfgUplinkTestModelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 uplinkTestModel[],
   int32 numberOfElements
);

int32 __stdcall RFmxWCDMA_CfgNumberOfChannelsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfChannels[],
   int32 numberOfElements
);

int32 __stdcall RFmxWCDMA_OBWCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxWCDMA_OBWCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxWCDMA_OBWCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxWCDMA_ACPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxWCDMA_ACPCfgMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMethod
);

int32 __stdcall RFmxWCDMA_ACPCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxWCDMA_ACPCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxWCDMA_ACPCfgOffsetPowerReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 offsetPowerReferenceCarrier,
   int32 offsetPowerReferenceSpecific
);

int32 __stdcall RFmxWCDMA_ACPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxWCDMA_ACPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxWCDMA_SlotPhaseCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxWCDMA_QEVMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxWCDMA_QEVMCfgMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementLength
);

int32 __stdcall RFmxWCDMA_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxWCDMA_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxWCDMA_ModAccCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxWCDMA_CHPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxWCDMA_CHPCfgRBWFilter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 RBWAuto,
   float64 RBW,
   int32 RBWFilterType
);

int32 __stdcall RFmxWCDMA_CHPCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxWCDMA_CDACfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxWCDMA_CDACfgMeasurementChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 spreadingFactor,
   int32 spreadingCode,
   int32 modulationType,
   int32 branch
);

int32 __stdcall RFmxWCDMA_CDACfgPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerUnit
);

int32 __stdcall RFmxWCDMA_SlotPowerCfgSynchronizationModeAndInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 synchronizationMode,
   int32 measurementOffset,
   int32 measurementLength
);

int32 __stdcall RFmxWCDMA_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWCDMA_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxWCDMA_CfgFrequencyUARFCN(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 linkDirection,
   int32 band,
   int32 UARFCN
);

int32 __stdcall RFmxWCDMA_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWCDMA_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxWCDMA_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxWCDMA_CfgIQPowerEdgeTrigger(
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

int32 __stdcall RFmxWCDMA_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxWCDMA_OBWFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_OBWFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* occupiedBandwidth,
   float64* absolutePower,
   float64* startFrequency,
   float64* stopFrequency
);

int32 __stdcall RFmxWCDMA_ModAccFetchDetectedChannelArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 detectedSpreadingFactor[],
   int32 detectedSpreadingCode[],
   int32 detectedModulationType[],
   int32 detectedBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   NIComplexSingle referenceWaveform[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchReferenceWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchRCDETrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 RCDE[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchEVMArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 RMSEVM[],
   float64 peakEVM[],
   float64 rho[],
   float64 frequencyError[],
   float64 chipRateError[],
   float64 RMSMagnitudeError[],
   float64 RMSPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchIQImpairmentsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 IQOriginOffset[],
   float64 IQGainImbalance[],
   float64 IQQuadratureError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchPeakCDEArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 peakCDE[],
   int32 peakCDECode[],
   int32 peakCDEBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchPeakActiveCDEArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 peakActiveCDE[],
   int32 peakActiveCDESpreadingFactor[],
   int32 peakActiveCDECode[],
   int32 peakActiveCDEBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchRCDEArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 peakRCDE[],
   int32 peakRCDESpreadingFactor[],
   int32 peakRCDECode[],
   int32 peakRCDEBranch[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannelsArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 numberofDetectedChannels[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccFetchDetectedChannel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* detectedSpreadingFactor,
   int32* detectedSpreadingCode,
   int32* detectedModulationType,
   int32* detectedBranch
);

int32 __stdcall RFmxWCDMA_ModAccFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSEVM,
   float64* peakEVM,
   float64* rho,
   float64* frequencyError,
   float64* chipRateError,
   float64* RMSMagnitudeError,
   float64* RMSPhaseError
);

int32 __stdcall RFmxWCDMA_ModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffset,
   float64* IQGainImbalance,
   float64* IQQuadratureError
);

int32 __stdcall RFmxWCDMA_ModAccFetchNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfDetectedChannels
);

int32 __stdcall RFmxWCDMA_ModAccFetchPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakActiveCDE,
   int32* peakActiveCDESpreadingFactor,
   int32* peakActiveCDECode,
   int32* peakActiveCDEBranch
);

int32 __stdcall RFmxWCDMA_ModAccFetchPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakCDE,
   int32* peakCDECode,
   int32* peakCDEBranch
);

int32 __stdcall RFmxWCDMA_ModAccFetchRCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* peakRCDE,
   int32* peakRCDESpreadingFactor,
   int32* peakRCDECode,
   int32* peakRCDEBranch
);

int32 __stdcall RFmxWCDMA_ModAccFetchMulticarrierIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* multicarrierIQOriginOffset,
   float64* multicarrierIQGainImbalance,
   float64* multicarrierIQQuadratureError
);

int32 __stdcall RFmxWCDMA_SlotPhaseFetchPhaseDiscontinuities(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotPhaseDiscontinuity[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SlotPhaseFetchChipPhaseErrorLinearFitTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chipPhaseErrorLinearFit[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SlotPhaseFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* maximumPhaseDiscontinuity,
   int32* discontinuityCountGreaterThanLimit1,
   int32* discontinuityCountGreaterThanLimit2,
   int32* discontinuityMinimumDistance
);

int32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absoluteIntegratedPower[],
   float64 relativeIntegratedPower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetMarginArray(
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

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetPowerArray(
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

int32 __stdcall RFmxWCDMA_SEMFetchSpectrum(
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

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetMarginArray(
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

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetPowerArray(
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

int32 __stdcall RFmxWCDMA_SEMFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower
);

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxWCDMA_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxWCDMA_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxWCDMA_SEMFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxWCDMA_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absoluteIntegratedPower,
   float64* relativeIntegratedPower,
   float64* absolutePeakPower,
   float64* peakFrequency,
   float64* relativePeakPower
);

int32 __stdcall RFmxWCDMA_QEVMFetchEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_QEVMFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_QEVMFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_QEVMFetchMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 magnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_QEVMFetchPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_QEVMFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanRMSEVM,
   float64* maximumPeakEVM,
   float64* meanFrequencyError,
   float64* meanMagnitudeError,
   float64* meanPhaseError,
   float64* meanChipRateError
);

int32 __stdcall RFmxWCDMA_QEVMFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* meanIQOriginOffset,
   float64* meanIQGainImbalance,
   float64* meanIQQuadratureError,
   float64* maximumIQOriginOffset,
   float64* maximumIQGainImbalance,
   float64* maximumIQQuadratureError
);

int32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurementArray(
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

int32 __stdcall RFmxWCDMA_ACPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ACPFetchRelativePowersTrace(
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

int32 __stdcall RFmxWCDMA_ACPFetchAbsolutePowersTrace(
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

int32 __stdcall RFmxWCDMA_ACPFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxWCDMA_ACPFetchOffsetMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* lowerRelativePower,
   float64* upperRelativePower,
   float64* lowerAbsolutePower,
   float64* upperAbsolutePower
);

int32 __stdcall RFmxWCDMA_ACPFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurementArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 absolutePower[],
   float64 relativePower[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CHPFetchSpectrum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectrum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CHPFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxWCDMA_CHPFetchTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalCarrierPower
);

int32 __stdcall RFmxWCDMA_CDAFetchSymbolEVMTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolEVM[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchSymbolMagnitudeErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolMagnitudeError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPhaseErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPhaseError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 codeDomainPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 ICodeDomainPowers[],
   float32 QCodeDomainPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchSymbolPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 symbolPowers[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_CDAFetchSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSSymbolEVM,
   float64* peakSymbolEVM,
   float64* RMSSymbolMagnitudeError,
   float64* RMSSymbolPhaseError,
   float64* meanSymbolPower,
   float64* chipRateError
);

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainPower(
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

int32 __stdcall RFmxWCDMA_CDAFetchCodeDomainIAndQPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IMeanActivePower,
   float64* QMeanActivePower,
   float64* IPeakInactivePower,
   float64* QPeakInactivePower
);

int32 __stdcall RFmxWCDMA_SlotPowerFetchPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 slotPower[],
   float64 slotPowerDelta[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWCDMA_ModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetIQGainImbalanceRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetIQQuadratureErrorRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetTransientRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetTransientRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetDownlinkTimingChannelSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetDownlinkTimingChannelSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetDownlinkTimingChannelCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccSetDownlinkTimingChannelCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsRMSMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsRMSPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsRho(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsIQGainImbalance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsIQQuadratureError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakCDECode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakActiveCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakActiveCDESpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakActiveCDECode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakActiveCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsSSCHPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsDPCHTimingOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakRCDE(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakRCDESpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakRCDECode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsPeakRCDEBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsNumberOfDetectedChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsDetectedSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsDetectedSpreadingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsDetectedModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsDetectedBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ModAccGetResultsMultiCarrierIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetOffsetFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetOffsetPowerReferenceCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetOffsetPowerReferenceCarrier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetOffsetPowerReferenceSpecific(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetOffsetPowerReferenceSpecific(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetOffsetIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetMeasurementMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetIFOutputPowerOffsetAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetNearIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetFarIFOutputPowerOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsLowerOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsLowerOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsUpperOffsetAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetResultsUpperOffsetRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetSequentialFFTSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_ACPSetFFTOverlapMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_ACPGetFFTOverlap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetResultsCarrierAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetResultsCarrierRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CHPSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetRBWFilterAutoBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetResultsOccupiedBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetResultsAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetResultsStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetResultsStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_OBWSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetOffsetRBWFilterBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetOffsetRBWFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetOffsetBandwidthIntegral(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsTotalCarrierPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsCarrierRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsCarrierAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsCarrierPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SEMSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumPeakEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumFrequencyError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumIQOriginOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMeanChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_QEVMGetResultsMaximumChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetTransientRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetTransientRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetResultsMaximumPhaseDiscontinuity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetResultsDiscontinuityCountGreaterThanLimit1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetResultsDiscontinuityCountGreaterThanLimit2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPhaseGetResultsDiscontinuityMinimumDistance(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetLinkDirection(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetNumberOfCarriers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetCarrierFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetChannelConfigurationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetNumberOfChannels(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetSpreadingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetSpreadingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetUplinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetUplinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetDownlinkTestModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetUplinkScramblingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetUplinkScramblingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetUplinkScramblingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetUplinkScramblingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetDownlinkScramblingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetDownlinkScramblingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetDownlinkScramblingPrimaryCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetDownlinkScramblingPrimaryCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetDownlinkScramblingSecondaryCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetDownlinkScramblingSecondaryCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_GetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SetTransmitterArchitecture(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWCDMA_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementChannelSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementChannelSpreadingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementChannelSpreadingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementChannelSpreadingCode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementChannelModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementChannelModulationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetMeasurementChannelBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetMeasurementChannelBranch(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetPowerUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetIQOffsetRemovalEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_CDASetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsRMSSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsPeakSymbolEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsRMSSymbolMagnitudeError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsRMSSymbolPhaseError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsMeanSymbolPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsChipRateError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsTotalPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsTotalActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsPeakActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsMeanInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsIMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsQMeanActivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsIPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_CDAGetResultsQPeakInactivePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetSynchronizationMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerGetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWCDMA_SlotPowerSetRRCFilterEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxWCDMA_CalculateFrequencyFromUARFCN(
   int32 linkDirection,
   int32 band,
   int32 UARFCN,
   float64 *centerFrequency
);

int32 __stdcall RFmxWCDMA_AnalyzeIQ(
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

int32 __stdcall RFmxWCDMA_AnalyzeIQSplit(
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

int32 __stdcall RFmxWCDMA_AnalyzeSpectrum(
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

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFmxWLAN.h sha256=4ed9eeeefe808acadab58386b02a6ef9bb7f06477f8e24c0e76ff4b7cdaf4e62 bytes=223513 -->
## FILE: imports/include/niRFmxWLAN.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFmxWLAN.h`
- sha256: `4ed9eeeefe808acadab58386b02a6ef9bb7f06477f8e24c0e76ff4b7cdaf4e62`
- bytes: 223513

````c

/****************************************************************************************************
*          National Instruments RFmx WLAN
*----------------------------------------------------------------------------------------------------
*   Copyright(c) National Instruments 2024.  All Rights Reserved.
*----------------------------------------------------------------------------------------------------
*
* Title:    niRFmxWLAN.h
*
* Purpose:  National Instruments RFmx WLAN,
*                                Attribute IDs,
*                                Attribute Values,
*                                Functions Declarations.
*
*****************************************************************************************************/

#ifndef __NI_RFMX_WLAN_H__
#define __NI_RFMX_WLAN_H__

#include "niRFmxInstr.h"

#define RFMXWLAN_ATTR_SELECTED_PORTS                                                    0x00a00ffd
#define RFMXWLAN_ATTR_CENTER_FREQUENCY                                                  0x00a00001
#define RFMXWLAN_ATTR_REFERENCE_LEVEL                                                   0x00a00002
#define RFMXWLAN_ATTR_EXTERNAL_ATTENUATION                                              0x00a00003
#define RFMXWLAN_ATTR_REFERENCE_LEVEL_HEADROOM                                          0x00a00ffc
#define RFMXWLAN_ATTR_TRIGGER_TYPE                                                      0x00a00004
#define RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE                                       0x00a00005
#define RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_EDGE                                         0x00a00006
#define RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SOURCE                                      0x00a00007
#define RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL                                       0x00a00008
#define RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE                                  0x00a00fff
#define RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE                                       0x00a00009
#define RFMXWLAN_ATTR_TRIGGER_DELAY                                                     0x00a0000a
#define RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE                                   0x00a0000b
#define RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_DURATION                               0x00a0000c
#define RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED                                              0x00a0002a
#define RFMXWLAN_ATTR_TRIGGER_GATE_LENGTH                                               0x00a0002b
#define RFMXWLAN_ATTR_STANDARD                                                          0x00a0000d
#define RFMXWLAN_ATTR_CHANNEL_BANDWIDTH                                                 0x00a0000e
#define RFMXWLAN_ATTR_NUMBER_OF_FREQUENCY_SEGMENTS                                      0x00a0000f
#define RFMXWLAN_ATTR_NUMBER_OF_RECEIVE_CHAINS                                          0x00a00010
#define RFMXWLAN_ATTR_OFDM_FREQUENCY_SEGMENT_INDEX                                      0x00a00014
#define RFMXWLAN_ATTR_OFDM_TRANSMIT_POWER_CLASS                                         0x00a00015
#define RFMXWLAN_ATTR_OFDM_FREQUENCY_BAND                                               0x00a00016
#define RFMXWLAN_ATTR_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED                             0x00a00027
#define RFMXWLAN_ATTR_OFDM_PPDU_TYPE                                                    0x00a00017
#define RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED                                      0x00a00028
#define RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED                                      0x00a0003a
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_USERS                                              0x00a00018
#define RFMXWLAN_ATTR_OFDM_MCS_INDEX                                                    0x00a00019
#define RFMXWLAN_ATTR_OFDM_SCRAMBLER_SEED                                               0x00a0003d
#define RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE                                              0x00a00032
#define RFMXWLAN_ATTR_OFDM_RU_SIZE                                                      0x00a0001a
#define RFMXWLAN_ATTR_OFDM_RU_OFFSET_MRU_INDEX                                          0x00a0001b
#define RFMXWLAN_ATTR_OFDM_RU_TYPE                                                      0x00a0003f
#define RFMXWLAN_ATTR_OFDM_DISTRIBUTION_BANDWIDTH                                       0x00a00040
#define RFMXWLAN_ATTR_OFDM_GUARD_INTERVAL_TYPE                                          0x00a0001c
#define RFMXWLAN_ATTR_OFDM_LTF_SIZE                                                     0x00a0001d
#define RFMXWLAN_ATTR_OFDM_PRE_FEC_PADDING_FACTOR                                       0x00a00033
#define RFMXWLAN_ATTR_OFDM_LDPC_EXTRA_SYMBOL_SEGMENT                                    0x00a00034
#define RFMXWLAN_ATTR_OFDM_PE_DISAMBIGUITY                                              0x00a00031
#define RFMXWLAN_ATTR_OFDM_STBC_ENABLED                                                 0x00a00035
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_SPACE_TIME_STREAMS                                 0x00a0001e
#define RFMXWLAN_ATTR_OFDM_SPACE_TIME_STREAM_OFFSET                                     0x00a0001f
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS                                   0x00a00020
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS                                        0x00a0003b
#define RFMXWLAN_ATTR_OFDM_DCM_ENABLED                                                  0x00a00021
#define RFMXWLAN_ATTR_OFDM_2xLDPC_ENABLED                                               0x00a00041
#define RFMXWLAN_ATTR_OFDM_IM_PILOTS_ENABLED                                            0x00a00042
#define RFMXWLAN_ATTR_OFDM_UNEQUAL_MODULATION_ENABLED                                   0x00a00043
#define RFMXWLAN_ATTR_OFDM_UNEQUAL_MODULATION_PATTERN_INDEX                             0x00a00044
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_LTF_SYMBOLS                                        0x00a00022
#define RFMXWLAN_ATTR_OFDM_MU_MIMO_LTF_MODE_ENABLED                                     0x00a00029
#define RFMXWLAN_ATTR_OFDM_PREAMBLE_PUNCTURING_ENABLED                                  0x00a0002f
#define RFMXWLAN_ATTR_OFDM_PREAMBLE_PUNCTURING_BITMAP                                   0x00a00030
#define RFMXWLAN_ATTR_OFDM_AUTO_PHASE_ROTATION_DETECTION_ENABLED                        0x00a0003c
#define RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_1                                 0x00a00037
#define RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_2                                 0x00a00038
#define RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_3                                 0x00a00039
#define RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_STANDARD                              0x00a00011
#define RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_CHANNEL_BANDWIDTH                     0x00a00012
#define RFMXWLAN_ATTR_AUTO_DETECT_SIGNAL_DETECTED_BURST_LENGTH                          0x00a00013
#define RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_ENABLED                                    0x00a0300a
#define RFMXWLAN_ATTR_DSSSMODACC_ACQUISITION_LENGTH_MODE                                0x00a0300b
#define RFMXWLAN_ATTR_DSSSMODACC_ACQUISITION_LENGTH                                     0x00a0300c
#define RFMXWLAN_ATTR_DSSSMODACC_MEASUREMENT_OFFSET                                     0x00a0300d
#define RFMXWLAN_ATTR_DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH                             0x00a0300e
#define RFMXWLAN_ATTR_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE                              0x00a0300f
#define RFMXWLAN_ATTR_DSSSMODACC_PULSE_SHAPING_FILTER_PARAMETER                         0x00a03010
#define RFMXWLAN_ATTR_DSSSMODACC_EQUALIZATION_ENABLED                                   0x00a03011
#define RFMXWLAN_ATTR_DSSSMODACC_BURST_START_DETECTION_ENABLED                          0x00a0307a
#define RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT                                               0x00a03012
#define RFMXWLAN_ATTR_DSSSMODACC_POWER_MEASUREMENT_ENABLED                              0x00a03013
#define RFMXWLAN_ATTR_DSSSMODACC_POWER_NUMBER_OF_CUSTOM_GATES                           0x00a03014
#define RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_START_TIME                           0x00a03015
#define RFMXWLAN_ATTR_DSSSMODACC_POWER_CUSTOM_GATE_STOP_TIME                            0x00a03016
#define RFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED                     0x00a0302c
#define RFMXWLAN_ATTR_DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED                    0x00a0302d
#define RFMXWLAN_ATTR_DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED                    0x00a0302e
#define RFMXWLAN_ATTR_DSSSMODACC_SPECTRUM_INVERTED                                      0x00a0307b
#define RFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLED                                  0x00a0307c
#define RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED                                      0x00a0302f
#define RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_COUNT                                        0x00a03030
#define RFMXWLAN_ATTR_DSSSMODACC_ALL_TRACES_ENABLED                                     0x00a03031
#define RFMXWLAN_ATTR_DSSSMODACC_NUMBER_OF_ANALYSIS_THREADS                             0x00a03071
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_EVM_MEAN                                   0x00a03032
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEAN                      0x00a0303c
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MAXIMUM                   0x00a0303d
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MEAN                      0x00a03035
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MAXIMUM                   0x00a03036
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MEAN                      0x00a03033
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM                   0x00a03034
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED                           0x00a0304d
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_FREQUENCY_ERROR_MEAN                           0x00a0304e
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEAN                          0x00a03052
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN                         0x00a03053
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_QUADRATURE_ERROR_MEAN                       0x00a03057
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN                          0x00a0305b
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_MAGNITUDE_ERROR_MEAN                       0x00a03062
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_RMS_PHASE_ERROR_MEAN                           0x00a03063
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_AVERAGE_POWER_MEAN                    0x00a03072
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_PEAK_POWER_MAXIMUM                    0x00a03073
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_AVERAGE_POWER_MEAN                      0x00a03074
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_PEAK_POWER_MAXIMUM                      0x00a03075
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_AVERAGE_POWER_MEAN                        0x00a03076
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_PEAK_POWER_MAXIMUM                        0x00a03077
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN                        0x00a03078
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM                        0x00a03079
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_AVERAGE_POWER_MEAN                 0x00a0303e
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_CUSTOM_GATE_PEAK_POWER_MAXIMUM                 0x00a0303f
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_MODULATION_FORMAT                         0x00a03068
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PAYLOAD_LENGTH                                 0x00a03069
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_TYPE                                  0x00a0306a
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_LOCKED_CLOCKS_BIT                              0x00a0306c
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS                              0x00a0306d
#define RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PSDU_CRC_STATUS                                0x00a0306e
#define RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_ENABLED                                    0x00a04000
#define RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED                                      0x00a04002
#define RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_COUNT                                        0x00a04003
#define RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE                                         0x00a040ac
#define RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED                0x00a040ad
#define RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED               0x00a040ae
#define RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODE                                       0x00a04066
#define RFMXWLAN_ATTR_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE                        0x00a04093
#define RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT                                               0x00a04008
#define RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH_MODE                                0x00a04009
#define RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH                                     0x00a0400a
#define RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_OFFSET                                     0x00a0400b
#define RFMXWLAN_ATTR_OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTH                             0x00a0400c
#define RFMXWLAN_ATTR_OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED                   0x00a040ca
#define RFMXWLAN_ATTR_OFDMMODACC_REFERENCE_DATA_CONSTELLATION_IDENTIFIER                0x00a040cb
#define RFMXWLAN_ATTR_OFDMMODACC_BURST_START_DETECTION_ENABLED                          0x00a04085
#define RFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD                      0x00a0407e
#define RFMXWLAN_ATTR_OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED                            0x00a0400d
#define RFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE                   0x00a040d1
#define RFMXWLAN_ATTR_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED                             0x00a0400e
#define RFMXWLAN_ATTR_OFDMMODACC_PHASE_TRACKING_ENABLED                                 0x00a0400f
#define RFMXWLAN_ATTR_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED                  0x00a04010
#define RFMXWLAN_ATTR_OFDMMODACC_SPECTRUM_INVERTED                                      0x00a0407a
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_TYPE                                0x00a04011
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE                  0x00a0406a
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_LENGTH                    0x00a0406b
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_RELATIVE_DELAY_SPREAD               0x00a040b7
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED               0x00a040e0
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED                       0x00a04087
#define RFMXWLAN_ATTR_OFDMMODACC_POWER_MEASUREMENT_ENABLED                              0x00a04017
#define RFMXWLAN_ATTR_OFDMMODACC_POWER_NUMBER_OF_CUSTOM_GATES                           0x00a04018
#define RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_START_TIME                           0x00a04019
#define RFMXWLAN_ATTR_OFDMMODACC_POWER_CUSTOM_GATE_STOP_TIME                            0x00a0401a
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED                           0x00a0408d
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED                      0x00a0407b
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_MODEL                                   0x00a0401b
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED                   0x00a0401c
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED                 0x00a0401d
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED                      0x00a0401e
#define RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED                  0x00a0407f
#define RFMXWLAN_ATTR_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE                       0x00a0406c
#define RFMXWLAN_ATTR_OFDMMODACC_DATA_DECODING_ENABLED                                  0x00a0408b
#define RFMXWLAN_ATTR_OFDMMODACC_NOISE_COMPENSATION_ENABLED                             0x00a04067
#define RFMXWLAN_ATTR_OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED           0x00a04068
#define RFMXWLAN_ATTR_OFDMMODACC_NOISE_COMPENSATION_REFERENCE_LEVEL_COERCION_LIMIT      0x00a04069
#define RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED                 0x00a0407c
#define RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN                  0x00a0407d
#define RFMXWLAN_ATTR_OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW                              0x00a040b1
#define RFMXWLAN_ATTR_OFDMMODACC_ALL_TRACES_ENABLED                                     0x00a04005
#define RFMXWLAN_ATTR_OFDMMODACC_NUMBER_OF_ANALYSIS_THREADS                             0x00a04004
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN                         0x00a0406e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_COMPOSITE_DATA_RMS_EVM_MEAN                    0x00a0406f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_COMPOSITE_PILOT_RMS_EVM_MEAN                   0x00a04070
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_RMS_EVM_MEAN                            0x00a04074
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_RMS_EVM_MAXIMUM                         0x00a04096
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_RMS_EVM_MINIMUM                         0x00a04097
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_DATA_RMS_EVM_MEAN                       0x00a04075
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_PILOT_RMS_EVM_MEAN                      0x00a04076
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MEAN                             0x00a04071
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MAXIMUM                          0x00a04098
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MINIMUM                          0x00a04099
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_DATA_RMS_EVM_MEAN                        0x00a04072
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_PILOT_RMS_EVM_MEAN                       0x00a04073
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MEAN                       0x00a04077
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUM                    0x00a0409a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MINIMUM                    0x00a0409b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_DATA_RMS_EVM_MEAN                  0x00a04078
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_STREAM_PILOT_RMS_EVM_MEAN                 0x00a04079
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_L_SIG_RMS_EVM_MEAN                             0x00a040bb
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_RMS_EVM_MEAN                               0x00a040bc
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_B_RMS_EVM_MEAN                             0x00a040bd
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_U_SIG_RMS_EVM_MEAN                             0x00a040be
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEAN                           0x00a040bf
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEAN                           0x00a040d2
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEAN                           0x00a040d4
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_STF_AVERAGE_POWER_MEAN                 0x00a0403a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_STF_PEAK_POWER_MAXIMUM                 0x00a0403b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_LTF_AVERAGE_POWER_MEAN                 0x00a0403c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_LTF_PEAK_POWER_MAXIMUM                 0x00a0403d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_SIG_AVERAGE_POWER_MEAN                 0x00a0403e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_L_SIG_PEAK_POWER_MAXIMUM                 0x00a0403f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_RL_SIG_AVERAGE_POWER_MEAN                0x00a04040
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_RL_SIG_PEAK_POWER_MAXIMUM                0x00a04041
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_SIG_AVERAGE_POWER_MEAN                0x00a04042
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_SIG_PEAK_POWER_MAXIMUM                0x00a04043
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEAN             0x00a04044
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_A_PEAK_POWER_MAXIMUM             0x00a04045
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_A_AVERAGE_POWER_MEAN              0x00a04046
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_A_PEAK_POWER_MAXIMUM              0x00a04047
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_AVERAGE_POWER_MEAN                 0x00a040c0
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUM                 0x00a040c1
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEAN              0x00a040de
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUM              0x00a040df
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEAN             0x00a04048
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUM             0x00a04049
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_AVERAGE_POWER_MEAN              0x00a0404a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUM              0x00a0404b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_SIG_AVERAGE_POWER_MEAN               0x00a040c2
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_SIG_PEAK_POWER_MAXIMUM               0x00a040c3
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEAN               0x00a040da
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUM               0x00a040db
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_SIG_AVERAGE_POWER_MEAN               0x00a040dc
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_ELR_SIG_PEAK_POWER_MAXIMUM               0x00a040dd
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_AVERAGE_POWER_MEAN                0x00a0404c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUM                0x00a0404d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_GF_STF_AVERAGE_POWER_MEAN             0x00a0404e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_GF_STF_PEAK_POWER_MAXIMUM             0x00a0404f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_STF_AVERAGE_POWER_MEAN               0x00a04050
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_STF_PEAK_POWER_MAXIMUM               0x00a04051
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEAN                0x00a04052
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_STF_PEAK_POWER_MAXIMUM                0x00a04053
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_STF_AVERAGE_POWER_MEAN               0x00a040c4
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_STF_PEAK_POWER_MAXIMUM               0x00a040c5
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_AVERAGE_POWER_MEAN               0x00a040d6
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUM               0x00a040d7
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEAN               0x00a04054
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_DLTF_PEAK_POWER_MAXIMUM               0x00a04055
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEAN               0x00a04056
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HT_ELTF_PEAK_POWER_MAXIMUM               0x00a04057
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_LTF_AVERAGE_POWER_MEAN               0x00a04058
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_VHT_LTF_PEAK_POWER_MAXIMUM               0x00a04059
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_LTF_AVERAGE_POWER_MEAN                0x00a0405a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_HE_LTF_PEAK_POWER_MAXIMUM                0x00a0405b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_LTF_AVERAGE_POWER_MEAN               0x00a040c6
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_EHT_LTF_PEAK_POWER_MAXIMUM               0x00a040c7
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_LTF_AVERAGE_POWER_MEAN               0x00a040d8
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_UHR_LTF_PEAK_POWER_MAXIMUM               0x00a040d9
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_DATA_AVERAGE_POWER_MEAN                  0x00a0405c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_DATA_PEAK_POWER_MAXIMUM                  0x00a0405d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PE_AVERAGE_POWER_MEAN                    0x00a0405e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PE_PEAK_POWER_MAXIMUM                    0x00a0405f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEAN                  0x00a04060
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUM                  0x00a04061
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEAN           0x00a04062
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_PEAK_POWER_MAXIMUM           0x00a04063
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CROSS_POWER_MEAN                               0x00a0408e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEAN                  0x00a040e8
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_POWER_MEAN                                0x00a0408f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_POWER_MAXIMUM                             0x00a0409c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_USER_POWER_MINIMUM                             0x00a0409d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_STREAM_POWER_MEAN                              0x00a040cc
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN                       0x00a04023
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_MAXIMUM               0x00a0409e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_MINIMUM               0x00a0409f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SUBCARRIER_INDEX      0x00a04024
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNUSED_TONE_ERROR_MARGIN                       0x00a04025
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNUSED_TONE_ERROR_MARGIN_RU_INDEX              0x00a04026
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_BURST_START_TIME_MEAN                          0x00a040b0
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SYMBOLS_USED                         0x00a04016
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NOISE_COMPENSATION_APPLIED                     0x00a04027
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MEAN                           0x00a04028
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUM                        0x00a040a0
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_MINIMUM                        0x00a040a1
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FREQUENCY_ERROR_CCDF_10_PERCENT                0x00a04029
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MEAN                        0x00a0402a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MAXIMUM                     0x00a040a2
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MINIMUM                     0x00a040a3
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEAN                 0x00a0402b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MAXIMUM              0x00a040a4
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MINIMUM              0x00a040a5
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ABSOLUTE_IQ_ORIGIN_OFFSET_MEAN                 0x00a0402c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN                         0x00a0402d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MAXIMUM                      0x00a040a6
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MINIMUM                      0x00a040a7
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MEAN                       0x00a0402e
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MAXIMUM                    0x00a040a8
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MINIMUM                    0x00a040a9
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IQ_TIMING_SKEW_MEAN                            0x00a0402f
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RMS_COMMON_PHASE_ERROR_MEAN                    0x00a04030
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RMS_COMMON_PILOT_ERROR_MEAN                    0x00a0406d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PPDU_TYPE                                      0x00a04031
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_MCS_INDEX                                      0x00a04032
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_AGGREGATION                                    0x00a040c9
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPE                                0x00a040aa
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RU_SIZE                                        0x00a04033
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RU_OFFSET_MRU_INDEX                            0x00a04034
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RU_TYPE                                        0x00a040e1
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTH                         0x00a040e2
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_USERS                                0x00a04035
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_HE_SIG_B_SYMBOLS                     0x00a04036
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLS                          0x00a040e7
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_GUARD_INTERVAL_TYPE                            0x00a04037
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_LTF_SIZE                                       0x00a04038
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMS                   0x00a04039
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SPACE_TIME_STREAM_OFFSET                       0x00a04090
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DCM_ENABLED                                    0x00a040ab
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_2xLDPC_ENABLED                                 0x00a040e3
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLED                              0x00a040e4
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED                     0x00a040e5
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX               0x00a040e6
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_L_SIG_PARITY_CHECK_STATUS                      0x00a04088
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_CRC_STATUS                                 0x00a04089
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_B_CRC_STATUS                               0x00a0408a
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_U_SIG_CRC_STATUS                               0x00a04091
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_CRC_STATUS                             0x00a04092
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS                             0x00a040d3
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_CRC_STATUS                             0x00a040d5
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PSDU_CRC_STATUS                                0x00a0408c
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SCRAMBLER_SEED                                 0x00a040c8
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PE_DURATION                                    0x00a04095
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_1                   0x00a040b8
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_2                   0x00a040b9
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_3                   0x00a040ba
#define RFMXWLAN_ATTR_SEM_MEASUREMENT_ENABLED                                           0x00a05000
#define RFMXWLAN_ATTR_SEM_MASK_TYPE                                                     0x00a05002
#define RFMXWLAN_ATTR_SEM_CARRIER_INTEGRATION_BANDWIDTH                                 0x00a05005
#define RFMXWLAN_ATTR_SEM_NUMBER_OF_OFFSETS                                             0x00a05006
#define RFMXWLAN_ATTR_SEM_OFFSET_START_FREQUENCY                                        0x00a05007
#define RFMXWLAN_ATTR_SEM_OFFSET_STOP_FREQUENCY                                         0x00a05008
#define RFMXWLAN_ATTR_SEM_OFFSET_SIDEBAND                                               0x00a05009
#define RFMXWLAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_START                                   0x00a0500a
#define RFMXWLAN_ATTR_SEM_OFFSET_RELATIVE_LIMIT_STOP                                    0x00a0500b
#define RFMXWLAN_ATTR_SEM_SPAN_AUTO                                                     0x00a0500c
#define RFMXWLAN_ATTR_SEM_SPAN                                                          0x00a0500d
#define RFMXWLAN_ATTR_SEM_SWEEP_TIME_AUTO                                               0x00a05011
#define RFMXWLAN_ATTR_SEM_SWEEP_TIME_INTERVAL                                           0x00a05012
#define RFMXWLAN_ATTR_SEM_AVERAGING_ENABLED                                             0x00a05013
#define RFMXWLAN_ATTR_SEM_AVERAGING_COUNT                                               0x00a05014
#define RFMXWLAN_ATTR_SEM_AVERAGING_TYPE                                                0x00a05015
#define RFMXWLAN_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE                                     0x00a05016
#define RFMXWLAN_ATTR_SEM_ALL_TRACES_ENABLED                                            0x00a05017
#define RFMXWLAN_ATTR_SEM_NUMBER_OF_ANALYSIS_THREADS                                    0x00a05018
#define RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS                                    0x00a0501b
#define RFMXWLAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER                     0x00a0501c
#define RFMXWLAN_ATTR_SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER                           0x00a0501e
#define RFMXWLAN_ATTR_SEM_RESULTS_CARRIER_PEAK_FREQUENCY                                0x00a0501f
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS                       0x00a05021
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER                0x00a05022
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER                0x00a05023
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER                      0x00a05024
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER                      0x00a05025
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY                           0x00a05026
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN                                   0x00a05027
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER                    0x00a05028
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER                    0x00a05029
#define RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY                         0x00a0502a
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS                       0x00a0502b
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER                0x00a0502c
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER                0x00a0502d
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER                      0x00a0502e
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER                      0x00a0502f
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY                           0x00a05030
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN                                   0x00a05031
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER                    0x00a05032
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER                    0x00a05033
#define RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY                         0x00a05034
#define RFMXWLAN_ATTR_TXP_MEASUREMENT_ENABLED                                           0x00a01000
#define RFMXWLAN_ATTR_TXP_MAXIMUM_MEASUREMENT_INTERVAL                                  0x00a01002
#define RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED                                       0x00a01003
#define RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED                                             0x00a01004
#define RFMXWLAN_ATTR_TXP_AVERAGING_COUNT                                               0x00a01005
#define RFMXWLAN_ATTR_TXP_ALL_TRACES_ENABLED                                            0x00a01006
#define RFMXWLAN_ATTR_TXP_NUMBER_OF_ANALYSIS_THREADS                                    0x00a01007
#define RFMXWLAN_ATTR_TXP_RESULTS_AVERAGE_POWER_MEAN                                    0x00a01009
#define RFMXWLAN_ATTR_TXP_RESULTS_AVERAGE_POWER_MAXIMUM                                 0x00a01015
#define RFMXWLAN_ATTR_TXP_RESULTS_AVERAGE_POWER_MINIMUM                                 0x00a01016
#define RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MEAN                                       0x00a01017
#define RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MAXIMUM                                    0x00a01011
#define RFMXWLAN_ATTR_TXP_RESULTS_PEAK_POWER_MINIMUM                                    0x00a01018
#define RFMXWLAN_ATTR_POWERRAMP_MEASUREMENT_ENABLED                                     0x00a0200a
#define RFMXWLAN_ATTR_POWERRAMP_ACQUISITION_LENGTH                                      0x00a0200c
#define RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED                                       0x00a02014
#define RFMXWLAN_ATTR_POWERRAMP_AVERAGING_COUNT                                         0x00a02015
#define RFMXWLAN_ATTR_POWERRAMP_ALL_TRACES_ENABLED                                      0x00a02016
#define RFMXWLAN_ATTR_POWERRAMP_NUMBER_OF_ANALYSIS_THREADS                              0x00a02017
#define RFMXWLAN_ATTR_POWERRAMP_RESULTS_RISE_TIME_MEAN                                  0x00a02018
#define RFMXWLAN_ATTR_POWERRAMP_RESULTS_FALL_TIME_MEAN                                  0x00a02019
#define RFMXWLAN_ATTR_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL                                0x00a00024
#define RFMXWLAN_ATTR_SAMPLE_CLOCK_RATE_FACTOR                                          0x00a00036
#define RFMXWLAN_ATTR_LIMITED_CONFIGURATION_CHANGE                                      0x00a00025
#define RFMXWLAN_ATTR_RESULT_FETCH_TIMEOUT                                              0x00a0c000

// Values for RFMXWLAN_ATTR_TRIGGER_TYPE
#define RFMXWLAN_VAL_TRIGGER_TYPE_NONE                                                              0
#define RFMXWLAN_VAL_TRIGGER_TYPE_DIGITAL_EDGE                                                      1
#define RFMXWLAN_VAL_TRIGGER_TYPE_IQ_POWER_EDGE                                                     2
#define RFMXWLAN_VAL_TRIGGER_TYPE_SOFTWARE                                                          3

// Values for RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_SOURCE
#define RFMXWLAN_VAL_PFI0_STR                                                                       "PFI0"
#define RFMXWLAN_VAL_PFI1_STR                                                                       "PFI1"
#define RFMXWLAN_VAL_PXI_TRIG0_STR                                                                  "PXI_Trig0"
#define RFMXWLAN_VAL_PXI_TRIG1_STR                                                                  "PXI_Trig1"
#define RFMXWLAN_VAL_PXI_TRIG2_STR                                                                  "PXI_Trig2"
#define RFMXWLAN_VAL_PXI_TRIG3_STR                                                                  "PXI_Trig3"
#define RFMXWLAN_VAL_PXI_TRIG4_STR                                                                  "PXI_Trig4"
#define RFMXWLAN_VAL_PXI_TRIG5_STR                                                                  "PXI_Trig5"
#define RFMXWLAN_VAL_PXI_TRIG6_STR                                                                  "PXI_Trig6"
#define RFMXWLAN_VAL_PXI_TRIG7_STR                                                                  "PXI_Trig7"
#define RFMXWLAN_VAL_PXI_STAR_STR                                                                   "PXI_STAR"
#define RFMXWLAN_VAL_PXIE_DSTARB_STR                                                                "PXIe_DStarB"
#define RFMXWLAN_VAL_TIMER_EVENT_STR                                                                "TimerEvent"
#define RFMXWLAN_VAL_PULSE_IN_STR                                                                   "PulseIn"
#define RFMXWLAN_VAL_DIO_PFI0_STR                                                                   "DIO/PFI0"
#define RFMXWLAN_VAL_DIO_PFI1_STR                                                                   "DIO/PFI1"
#define RFMXWLAN_VAL_DIO_PFI2_STR                                                                   "DIO/PFI2"
#define RFMXWLAN_VAL_DIO_PFI3_STR                                                                   "DIO/PFI3"
#define RFMXWLAN_VAL_DIO_PFI4_STR                                                                   "DIO/PFI4"
#define RFMXWLAN_VAL_DIO_PFI5_STR                                                                   "DIO/PFI5"
#define RFMXWLAN_VAL_DIO_PFI6_STR                                                                   "DIO/PFI6"
#define RFMXWLAN_VAL_DIO_PFI7_STR                                                                   "DIO/PFI7"

// Values for RFMXWLAN_ATTR_DIGITAL_EDGE_TRIGGER_EDGE
#define RFMXWLAN_VAL_DIGITAL_EDGE_RISING_EDGE                                                       0
#define RFMXWLAN_VAL_DIGITAL_EDGE_FALLING_EDGE                                                      1

// Values for RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE
#define RFMXWLAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE                                      0
#define RFMXWLAN_VAL_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE                                      1

// Values for RFMXWLAN_ATTR_IQ_POWER_EDGE_TRIGGER_SLOPE
#define RFMXWLAN_VAL_IQ_POWER_EDGE_RISING_SLOPE                                                     0
#define RFMXWLAN_VAL_IQ_POWER_EDGE_FALLING_SLOPE                                                    1

// Values for RFMXWLAN_ATTR_TRIGGER_MINIMUM_QUIET_TIME_MODE
#define RFMXWLAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL                                         0
#define RFMXWLAN_VAL_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO                                           1

// Values for RFMXWLAN_ATTR_TRIGGER_GATE_ENABLED
#define RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_FALSE                                                     0
#define RFMXWLAN_VAL_TRIGGER_GATE_ENABLED_TRUE                                                      1

// Values for RFMXWLAN_ATTR_STANDARD
#define RFMXWLAN_VAL_STANDARD_802_11_AG                                                             0
#define RFMXWLAN_VAL_STANDARD_802_11_B                                                              1
#define RFMXWLAN_VAL_STANDARD_802_11_J                                                              2
#define RFMXWLAN_VAL_STANDARD_802_11_P                                                              3
#define RFMXWLAN_VAL_STANDARD_802_11_N                                                              4
#define RFMXWLAN_VAL_STANDARD_802_11_AC                                                             5
#define RFMXWLAN_VAL_STANDARD_802_11_AX                                                             6
#define RFMXWLAN_VAL_STANDARD_802_11_BE                                                             7
#define RFMXWLAN_VAL_STANDARD_802_11_BN                                                             8
#define RFMXWLAN_VAL_STANDARD_UNKNOWN                                                               -1

// Values for RFMXWLAN_ATTR_OFDM_TRANSMIT_POWER_CLASS
#define RFMXWLAN_VAL_OFDM_TRANSMIT_POWER_CLASS_A                                                    0
#define RFMXWLAN_VAL_OFDM_TRANSMIT_POWER_CLASS_B                                                    1
#define RFMXWLAN_VAL_OFDM_TRANSMIT_POWER_CLASS_C                                                    2
#define RFMXWLAN_VAL_OFDM_TRANSMIT_POWER_CLASS_D                                                    3

// Values for RFMXWLAN_ATTR_OFDM_FREQUENCY_BAND
#define RFMXWLAN_VAL_OFDM_FREQUENCY_BAND_2_4GHZ                                                     0
#define RFMXWLAN_VAL_OFDM_FREQUENCY_BAND_5GHZ                                                       1

// Values for RFMXWLAN_ATTR_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED
#define RFMXWLAN_VAL_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED_FALSE                                    0
#define RFMXWLAN_VAL_OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED_TRUE                                     1

// Values for RFMXWLAN_ATTR_OFDM_PPDU_TYPE
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_NON_HT                                                          0
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_MIXED                                                           1
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_GREENFIELD                                                      2
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_SU                                                              3
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_MU                                                              4
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_EXTENDED_RANGE_SU                                               5
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_TRIGGER_BASED                                                   6
#define RFMXWLAN_VAL_OFDM_PPDU_TYPE_ELR                                                             7

// Values for RFMXWLAN_ATTR_OFDM_HEADER_DECODING_ENABLED
#define RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_FALSE                                             0
#define RFMXWLAN_VAL_OFDM_HEADER_DECODING_ENABLED_TRUE                                              1

// Values for RFMXWLAN_ATTR_OFDM_SIG_COMPRESSION_ENABLED
#define RFMXWLAN_VAL_OFDM_SIG_COMPRESSION_ENABLED_FALSE                                             0
#define RFMXWLAN_VAL_OFDM_SIG_COMPRESSION_ENABLED_TRUE                                              1

// Values for RFMXWLAN_ATTR_OFDM_FEC_CODING_TYPE
#define RFMXWLAN_VAL_OFDM_FEC_CODING_TYPE_BCC                                                       0
#define RFMXWLAN_VAL_OFDM_FEC_CODING_TYPE_LDPC                                                      1

// Values for RFMXWLAN_ATTR_OFDM_RU_TYPE
#define RFMXWLAN_VAL_OFDM_RU_TYPE_RRU                                                               0
#define RFMXWLAN_VAL_OFDM_RU_TYPE_DRU                                                               1

// Values for RFMXWLAN_ATTR_OFDM_GUARD_INTERVAL_TYPE
#define RFMXWLAN_VAL_OFDM_GUARD_INTERVAL_TYPE_1_4                                                   0
#define RFMXWLAN_VAL_OFDM_GUARD_INTERVAL_TYPE_1_8                                                   1
#define RFMXWLAN_VAL_OFDM_GUARD_INTERVAL_TYPE_1_16                                                  2

// Values for RFMXWLAN_ATTR_OFDM_LTF_SIZE
#define RFMXWLAN_VAL_OFDM_LTF_SIZE_4X                                                               0
#define RFMXWLAN_VAL_OFDM_LTF_SIZE_2X                                                               1
#define RFMXWLAN_VAL_OFDM_LTF_SIZE_1X                                                               2
#define RFMXWLAN_VAL_OFDM_LTF_SIZE_NOT_APPLICABLE                                                   -1

// Values for RFMXWLAN_ATTR_OFDM_STBC_ENABLED
#define RFMXWLAN_VAL_OFDM_STBC_ENABLED_FALSE                                                        0
#define RFMXWLAN_VAL_OFDM_STBC_ENABLED_TRUE                                                         1

// Values for RFMXWLAN_ATTR_OFDM_DCM_ENABLED
#define RFMXWLAN_VAL_OFDM_DCM_ENABLED_FALSE                                                         0
#define RFMXWLAN_VAL_OFDM_DCM_ENABLED_TRUE                                                          1

// Values for RFMXWLAN_ATTR_OFDM_2xLDPC_ENABLED
#define RFMXWLAN_VAL_OFDM_2xLDPC_ENABLED_FALSE                                                      0
#define RFMXWLAN_VAL_OFDM_2xLDPC_ENABLED_TRUE                                                       1

// Values for RFMXWLAN_ATTR_OFDM_IM_PILOTS_ENABLED
#define RFMXWLAN_VAL_OFDM_IM_PILOTS_ENABLED_FALSE                                                   0
#define RFMXWLAN_VAL_OFDM_IM_PILOTS_ENABLED_TRUE                                                    1

// Values for RFMXWLAN_ATTR_OFDM_UNEQUAL_MODULATION_ENABLED
#define RFMXWLAN_VAL_OFDM_UNEQUAL_MODULATION_ENABLED_FALSE                                          0
#define RFMXWLAN_VAL_OFDM_UNEQUAL_MODULATION_ENABLED_TRUE                                           1

// Values for RFMXWLAN_ATTR_OFDM_MU_MIMO_LTF_MODE_ENABLED
#define RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_FALSE                                            0
#define RFMXWLAN_VAL_OFDM_MU_MIMO_LTF_MODE_ENABLED_TRUE                                             1

// Values for RFMXWLAN_ATTR_OFDM_PREAMBLE_PUNCTURING_ENABLED
#define RFMXWLAN_VAL_OFDM_PREAMBLE_PUNCTURING_ENABLED_FALSE                                         0
#define RFMXWLAN_VAL_OFDM_PREAMBLE_PUNCTURING_ENABLED_TRUE                                          1

// Values for RFMXWLAN_ATTR_OFDM_AUTO_PHASE_ROTATION_DETECTION_ENABLED
#define RFMXWLAN_VAL_OFDM_AUTO_PHASE_ROTATION_DETECTION_ENABLED_FALSE                               0
#define RFMXWLAN_VAL_OFDM_AUTO_PHASE_ROTATION_DETECTION_ENABLED_TRUE                                1

// Values for RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_1
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_1_PLUS_ONE                                     0
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_1_MINUS_ONE                                    1

// Values for RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_2
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_2_PLUS_ONE                                     0
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_2_MINUS_ONE                                    1

// Values for RFMXWLAN_ATTR_OFDM_PHASE_ROTATION_COEFFICIENT_3
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_3_PLUS_ONE                                     0
#define RFMXWLAN_VAL_OFDM_PHASE_ROTATION_COEFFICIENT_3_MINUS_ONE                                    1

// Values for RFMXWLAN_ATTR_DSSSMODACC_ACQUISITION_LENGTH_MODE
#define RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_MANUAL                                      0
#define RFMXWLAN_VAL_DSSSMODACC_ACQUISITION_LENGTH_MODE_AUTO                                        1

// Values for RFMXWLAN_ATTR_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE
#define RFMXWLAN_VAL_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE_RECTANGULAR                               0
#define RFMXWLAN_VAL_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE_RAISED_COSINE                             1
#define RFMXWLAN_VAL_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE_ROOT_RAISED_COSINE                        2
#define RFMXWLAN_VAL_DSSSMODACC_PULSE_SHAPING_FILTER_TYPE_GAUSSIAN                                  3

// Values for RFMXWLAN_ATTR_DSSSMODACC_EQUALIZATION_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_EQUALIZATION_ENABLED_FALSE                                          0
#define RFMXWLAN_VAL_DSSSMODACC_EQUALIZATION_ENABLED_TRUE                                           1

// Values for RFMXWLAN_ATTR_DSSSMODACC_BURST_START_DETECTION_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_BURST_START_DETECTION_ENABLED_FALSE                                 0
#define RFMXWLAN_VAL_DSSSMODACC_BURST_START_DETECTION_ENABLED_TRUE                                  1

// Values for RFMXWLAN_ATTR_DSSSMODACC_EVM_UNIT
#define RFMXWLAN_VAL_DSSSMODACC_EVM_UNIT_PERCENTAGE                                                 0
#define RFMXWLAN_VAL_DSSSMODACC_EVM_UNIT_DB                                                         1

// Values for RFMXWLAN_ATTR_DSSSMODACC_POWER_MEASUREMENT_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_FALSE                                     0
#define RFMXWLAN_VAL_DSSSMODACC_POWER_MEASUREMENT_ENABLED_TRUE                                      1

// Values for RFMXWLAN_ATTR_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED_FALSE                            0
#define RFMXWLAN_VAL_DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED_TRUE                             1

// Values for RFMXWLAN_ATTR_DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED_FALSE                           0
#define RFMXWLAN_VAL_DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED_TRUE                            1

// Values for RFMXWLAN_ATTR_DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_FALSE                           0
#define RFMXWLAN_VAL_DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE                            1

// Values for RFMXWLAN_ATTR_DSSSMODACC_SPECTRUM_INVERTED
#define RFMXWLAN_VAL_DSSSMODACC_SPECTRUM_INVERTED_FALSE                                             0
#define RFMXWLAN_VAL_DSSSMODACC_SPECTRUM_INVERTED_TRUE                                              1

// Values for RFMXWLAN_ATTR_DSSSMODACC_DATA_DECODING_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_DATA_DECODING_ENABLED_FALSE                                         0
#define RFMXWLAN_VAL_DSSSMODACC_DATA_DECODING_ENABLED_TRUE                                          1

// Values for RFMXWLAN_ATTR_DSSSMODACC_AVERAGING_ENABLED
#define RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_FALSE                                             0
#define RFMXWLAN_VAL_DSSSMODACC_AVERAGING_ENABLED_TRUE                                              1

// Values for RFMXWLAN_ATTR_DSSSMODACC_RESULTS_DATA_MODULATION_FORMAT
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS1MBPS                                    0
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_DSSS2MBPS                                    1
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK5_5MBPS                                   2
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_CCK11MBPS                                    3
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC5_5MBPS                                  4
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC11MBPS                                   5
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC22MBPS                                   6
#define RFMXWLAN_VAL_DSSSMODACC_DATA_MODULATION_FORMAT_PBCC33MBPS                                   7

// Values for RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PREAMBLE_TYPE
#define RFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_LONG                                                  0
#define RFMXWLAN_VAL_DSSSMODACC_PREAMBLE_TYPE_SHORT                                                 1

// Values for RFMXWLAN_ATTR_DSSSMODACC_RESULTS_HEADER_CRC_STATUS
#define RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_FAIL                                              0
#define RFMXWLAN_VAL_DSSSMODACC_HEADER_CRC_STATUS_PASS                                              1

// Values for RFMXWLAN_ATTR_DSSSMODACC_RESULTS_PSDU_CRC_STATUS
#define RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_FAIL                                                0
#define RFMXWLAN_VAL_DSSSMODACC_PSDU_CRC_STATUS_PASS                                                1

// Values for RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_FALSE                                             0
#define RFMXWLAN_VAL_OFDMMODACC_AVERAGING_ENABLED_TRUE                                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_AVERAGING_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_AVERAGING_TYPE_RMS                                                  0
#define RFMXWLAN_VAL_OFDMMODACC_AVERAGING_TYPE_VECTOR                                               5

// Values for RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED_FALSE                       0
#define RFMXWLAN_VAL_OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED_TRUE                        1

// Values for RFMXWLAN_ATTR_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED_FALSE                      0
#define RFMXWLAN_VAL_OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED_TRUE                       1

// Values for RFMXWLAN_ATTR_OFDMMODACC_MEASUREMENT_MODE
#define RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_MEASURE                                            0
#define RFMXWLAN_VAL_OFDMMODACC_MEASUREMENT_MODE_CALIBRATE_NOISE_FLOOR                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE
#define RFMXWLAN_VAL_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_ACQUIRED_WAVEFORM                   0
#define RFMXWLAN_VAL_OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE_REFERENCE_WAVEFORM                  1

// Values for RFMXWLAN_ATTR_OFDMMODACC_EVM_UNIT
#define RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_PERCENTAGE                                                 0
#define RFMXWLAN_VAL_OFDMMODACC_EVM_UNIT_DB                                                         1

// Values for RFMXWLAN_ATTR_OFDMMODACC_ACQUISITION_LENGTH_MODE
#define RFMXWLAN_VAL_OFDMMODACC_ACQUISITION_LENGTH_MODE_MANUAL                                      0
#define RFMXWLAN_VAL_OFDMMODACC_ACQUISITION_LENGTH_MODE_AUTO                                        1

// Values for RFMXWLAN_ATTR_OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED_FALSE                          0
#define RFMXWLAN_VAL_OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED_TRUE                           1

// Values for RFMXWLAN_ATTR_OFDMMODACC_BURST_START_DETECTION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_BURST_START_DETECTION_ENABLED_FALSE                                 0
#define RFMXWLAN_VAL_OFDMMODACC_BURST_START_DETECTION_ENABLED_TRUE                                  1

// Values for RFMXWLAN_ATTR_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD
#define RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_DISABLED                          0
#define RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_INITIAL_PREAMBLE                  1
#define RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE                          2
#define RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_AND_PILOTS               3
#define RFMXWLAN_VAL_OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD_PREAMBLE_PILOTS_AND_DATA          4

// Values for RFMXWLAN_ATTR_OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED_FALSE                                   0
#define RFMXWLAN_VAL_OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED_TRUE                                    1

// Values for RFMXWLAN_ATTR_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE
#define RFMXWLAN_VAL_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE_NONE                           0
#define RFMXWLAN_VAL_OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE_AVERAGE_CPE                    1

// Values for RFMXWLAN_ATTR_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_FALSE                                    0
#define RFMXWLAN_VAL_OFDMMODACC_AMPLITUDE_TRACKING_ENABLED_TRUE                                     1

// Values for RFMXWLAN_ATTR_OFDMMODACC_PHASE_TRACKING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_FALSE                                        0
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_TRACKING_ENABLED_TRUE                                         1

// Values for RFMXWLAN_ATTR_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_FALSE                         0
#define RFMXWLAN_VAL_OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED_TRUE                          1

// Values for RFMXWLAN_ATTR_OFDMMODACC_SPECTRUM_INVERTED
#define RFMXWLAN_VAL_OFDMMODACC_SPECTRUM_INVERTED_FALSE                                             0
#define RFMXWLAN_VAL_OFDMMODACC_SPECTRUM_INVERTED_TRUE                                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE                                   0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_TYPE_REFERENCE_AND_DATA                          1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE_LINEAR                        0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE_TRIANGULAR_SMOOTHING          1
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE_WIENER_FILTER                 2

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED_FALSE                      0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED_TRUE                       1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED_FALSE                              0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED_TRUE                               1

// Values for RFMXWLAN_ATTR_OFDMMODACC_POWER_MEASUREMENT_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_POWER_MEASUREMENT_ENABLED_FALSE                                     0
#define RFMXWLAN_VAL_OFDMMODACC_POWER_MEASUREMENT_ENABLED_TRUE                                      1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED_FALSE                                  0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED_TRUE                                   1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED_FALSE                             0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED_TRUE                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_MODEL
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_MODEL_TX                                             0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_MODEL_RX                                             1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_FALSE                          0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED_TRUE                           1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_FALSE                        0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED_TRUE                         1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_FALSE                             0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED_TRUE                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_FALSE                         0
#define RFMXWLAN_VAL_OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED_TRUE                          1

// Values for RFMXWLAN_ATTR_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE
#define RFMXWLAN_VAL_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE_LIMIT1                             0
#define RFMXWLAN_VAL_OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE_LIMIT2                             1

// Values for RFMXWLAN_ATTR_OFDMMODACC_DATA_DECODING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_DATA_DECODING_ENABLED_FALSE                                         0
#define RFMXWLAN_VAL_OFDMMODACC_DATA_DECODING_ENABLED_TRUE                                          1

// Values for RFMXWLAN_ATTR_OFDMMODACC_NOISE_COMPENSATION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_FALSE                                    0
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_ENABLED_TRUE                                     1

// Values for RFMXWLAN_ATTR_OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_FALSE                  0
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED_TRUE                   1

// Values for RFMXWLAN_ATTR_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_FALSE                        0
#define RFMXWLAN_VAL_OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED_TRUE                         1

// Values for RFMXWLAN_ATTR_OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW
#define RFMXWLAN_VAL_OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW_FALSE                                     0
#define RFMXWLAN_VAL_OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW_TRUE                                      1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_NOISE_COMPENSATION_APPLIED
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_APPLIED_FALSE                                    0
#define RFMXWLAN_VAL_OFDMMODACC_NOISE_COMPENSATION_APPLIED_TRUE                                     1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_FEC_CODING_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_FEC_CODING_TYPE_BCC                                                 0
#define RFMXWLAN_VAL_OFDMMODACC_FEC_CODING_TYPE_LDPC                                                1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RU_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_RU_TYPE_RRU                                                         0
#define RFMXWLAN_VAL_OFDMMODACC_RU_TYPE_DRU                                                         1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_DCM_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_DCM_ENABLED_FALSE                                                   0
#define RFMXWLAN_VAL_OFDMMODACC_DCM_ENABLED_TRUE                                                    1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_2xLDPC_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_2xLDPC_ENABLED_FALSE                                                0
#define RFMXWLAN_VAL_OFDMMODACC_2xLDPC_ENABLED_TRUE                                                 1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_IM_PILOTS_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_IM_PILOTS_ENABLED_FALSE                                             0
#define RFMXWLAN_VAL_OFDMMODACC_IM_PILOTS_ENABLED_TRUE                                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_UNEQUAL_MODULATION_ENABLED_FALSE                                    0
#define RFMXWLAN_VAL_OFDMMODACC_UNEQUAL_MODULATION_ENABLED_TRUE                                     1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_L_SIG_PARITY_CHECK_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_NOT_APPLICABLE                            -1
#define RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_FAIL                                      0
#define RFMXWLAN_VAL_OFDMMODACC_L_SIG_PARITY_CHECK_STATUS_PASS                                      1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_NOT_APPLICABLE                                       -1
#define RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_FAIL                                                 0
#define RFMXWLAN_VAL_OFDMMODACC_SIG_CRC_STATUS_PASS                                                 1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_SIG_B_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_NOT_APPLICABLE                                     -1
#define RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_FAIL                                               0
#define RFMXWLAN_VAL_OFDMMODACC_SIG_B_CRC_STATUS_PASS                                               1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_U_SIG_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_U_SIG_CRC_STATUS_NOT_APPLICABLE                                     -1
#define RFMXWLAN_VAL_OFDMMODACC_U_SIG_CRC_STATUS_FAIL                                               0
#define RFMXWLAN_VAL_OFDMMODACC_U_SIG_CRC_STATUS_PASS                                               1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_EHT_SIG_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_EHT_SIG_CRC_STATUS_NOT_APPLICABLE                                   -1
#define RFMXWLAN_VAL_OFDMMODACC_EHT_SIG_CRC_STATUS_FAIL                                             0
#define RFMXWLAN_VAL_OFDMMODACC_EHT_SIG_CRC_STATUS_PASS                                             1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_NOT_APPLICABLE                                   -1
#define RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_FAIL                                             0
#define RFMXWLAN_VAL_OFDMMODACC_UHR_SIG_CRC_STATUS_PASS                                             1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_ELR_SIG_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_ELR_SIG_CRC_STATUS_NOT_APPLICABLE                                   -1
#define RFMXWLAN_VAL_OFDMMODACC_ELR_SIG_CRC_STATUS_FAIL                                             0
#define RFMXWLAN_VAL_OFDMMODACC_ELR_SIG_CRC_STATUS_PASS                                             1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PSDU_CRC_STATUS
#define RFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_FAIL                                                0
#define RFMXWLAN_VAL_OFDMMODACC_PSDU_CRC_STATUS_PASS                                                1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_1
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_1_PLUS_ONE                               0
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_1_MINUS_ONE                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_2
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_2_PLUS_ONE                               0
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_2_MINUS_ONE                              1

// Values for RFMXWLAN_ATTR_OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_3
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_3_PLUS_ONE                               0
#define RFMXWLAN_VAL_OFDMMODACC_PHASE_ROTATION_COEFFICIENT_3_MINUS_ONE                              1

// Values for RFMXWLAN_ATTR_SEM_MASK_TYPE
#define RFMXWLAN_VAL_SEM_MASK_TYPE_STANDARD                                                         0
#define RFMXWLAN_VAL_SEM_MASK_TYPE_CUSTOM                                                           1

// Values for RFMXWLAN_ATTR_SEM_OFFSET_SIDEBAND
#define RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_NEGATIVE                                                   0
#define RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_POSITIVE                                                   1
#define RFMXWLAN_VAL_SEM_OFFSET_SIDEBAND_BOTH                                                       2

// Values for RFMXWLAN_ATTR_SEM_SPAN_AUTO
#define RFMXWLAN_VAL_SEM_SPAN_AUTO_FALSE                                                            0
#define RFMXWLAN_VAL_SEM_SPAN_AUTO_TRUE                                                             1

// Values for RFMXWLAN_ATTR_SEM_SWEEP_TIME_AUTO
#define RFMXWLAN_VAL_SEM_SWEEP_TIME_AUTO_FALSE                                                      0
#define RFMXWLAN_VAL_SEM_SWEEP_TIME_AUTO_TRUE                                                       1

// Values for RFMXWLAN_ATTR_SEM_AVERAGING_ENABLED
#define RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWLAN_VAL_SEM_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWLAN_ATTR_SEM_AVERAGING_TYPE
#define RFMXWLAN_VAL_SEM_AVERAGING_TYPE_RMS                                                         0
#define RFMXWLAN_VAL_SEM_AVERAGING_TYPE_LOG                                                         1
#define RFMXWLAN_VAL_SEM_AVERAGING_TYPE_SCALAR                                                      2
#define RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MAXIMUM                                                     3
#define RFMXWLAN_VAL_SEM_AVERAGING_TYPE_MINIMUM                                                     4

// Values for RFMXWLAN_ATTR_SEM_AMPLITUDE_CORRECTION_TYPE
#define RFMXWLAN_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY                              0
#define RFMXWLAN_VAL_SEM_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN                           1

// Values for RFMXWLAN_ATTR_SEM_RESULTS_MEASUREMENT_STATUS
#define RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_FAIL                                                    0
#define RFMXWLAN_VAL_SEM_MEASUREMENT_STATUS_PASS                                                    1

// Values for RFMXWLAN_ATTR_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS
#define RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXWLAN_VAL_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXWLAN_ATTR_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS
#define RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL                                       0
#define RFMXWLAN_VAL_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS                                       1

// Values for RFMXWLAN_ATTR_TXP_BURST_DETECTION_ENABLED
#define RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_FALSE                                              0
#define RFMXWLAN_VAL_TXP_BURST_DETECTION_ENABLED_TRUE                                               1

// Values for RFMXWLAN_ATTR_TXP_AVERAGING_ENABLED
#define RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_FALSE                                                    0
#define RFMXWLAN_VAL_TXP_AVERAGING_ENABLED_TRUE                                                     1

// Values for RFMXWLAN_ATTR_POWERRAMP_AVERAGING_ENABLED
#define RFMXWLAN_VAL_POWERRAMP_AVERAGING_ENABLED_FALSE                                              0
#define RFMXWLAN_VAL_POWERRAMP_AVERAGING_ENABLED_TRUE                                               1

// Values for RFMXWLAN_ATTR_LIMITED_CONFIGURATION_CHANGE
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_DISABLED                                          0
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE                                         1
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY                                         2
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL                                   3
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL                     4
#define RFMXWLAN_VAL_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL      5

// Values for FrequencyReferenceSource
#define RFMXWLAN_VAL_ONBOARD_CLOCK_STR                                                              "OnboardClock"
#define RFMXWLAN_VAL_REF_IN_STR                                                                     "RefIn"
#define RFMXWLAN_VAL_PXI_CLK_STR                                                                    "PXI_Clk"
#define RFMXWLAN_VAL_CLK_IN_STR                                                                     "ClkIn"

// Values for Boolean
#define RFMXWLAN_VAL_FALSE                                                                          0
#define RFMXWLAN_VAL_TRUE                                                                           1

// Values for MeasurementTypes
#define RFMXWLAN_VAL_TXP                                                                            1<<0
#define RFMXWLAN_VAL_POWERRAMP                                                                      1<<1
#define RFMXWLAN_VAL_DSSSMODACC                                                                     1<<2
#define RFMXWLAN_VAL_OFDMMODACC                                                                     1<<3
#define RFMXWLAN_VAL_SEM                                                                            1<<4

// Values for OfdmModAccCalibrationDataValid
#define RFMXWLAN_VAL_OFDMMODACC_CALIBRATION_DATA_VALID_FALSE                                        0
#define RFMXWLAN_VAL_OFDMMODACC_CALIBRATION_DATA_VALID_TRUE                                         1

/* ---------------- RFmxWLAN APIs ------------------ */


#ifdef __cplusplus
extern "C"
{
#endif


int32 __stdcall RFmxWLAN_ResetAttribute(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID
);

int32 __stdcall RFmxWLAN_Initialize(
   char resourceName[],
   char optionString[],
   niRFmxInstrHandle *handleOut,
   int32 *isNewSession
);

int32 __stdcall RFmxWLAN_InitializeFromNIRFSASession(
   uInt32 NIRFSASession,
   niRFmxInstrHandle *handleOut
);

int32 __stdcall RFmxWLAN_Close(
   niRFmxInstrHandle instrumentHandle,
   int32 forceDestroy
);

int32 __stdcall RFmxWLAN_GetErrorString(
   niRFmxInstrHandle instrumentHandle,
   int32 errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxWLAN_GetError(
   niRFmxInstrHandle instrumentHandle,
   int32* errorCode,
   int32 errorDescriptionBufferSize,
   char errorDescription[]
);

int32 __stdcall RFmxWLAN_CfgFrequencyReference(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   char frequencyReferenceSource[],
   float64 frequencyReferenceFrequency
);

int32 __stdcall RFmxWLAN_CfgMechanicalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 mechanicalAttenuationAuto,
   float64 mechanicalAttenuationValue
);

int32 __stdcall RFmxWLAN_CfgRFAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char channelName[],
   int32 RFAttenuationAuto,
   float64 RFAttenuationValue
);

int32 __stdcall RFmxWLAN_WaitForAcquisitionComplete(
   niRFmxInstrHandle instrumentHandle,
   float64 timeout
);


int32 __stdcall RFmxWLAN_BuildSignalString(
   char signalName[],
   char resultName[],
   int32 selectorStringLength,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_BuildChainString(
   char selectorString[],
   int32 chainNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_BuildGateString(
   char selectorString[],
   int32 gateNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_BuildOffsetString(
   char selectorString[],
   int32 offsetNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_BuildSegmentString(
   char selectorString[],
   int32 segmentNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_BuildStreamString(
   char selectorString[],
   int32 streamNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_BuildUserString(
   char selectorString[],
   int32 userNumber,
   int32 selectorStringOutLength,
   char selectorStringOut[]
);

int32 __stdcall RFmxWLAN_SetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeI8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeI8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeI16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int16* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeI32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeI32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeI64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeI64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeU8(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeU8Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt8 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeU16(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt16* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeU32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeU32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeU64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   uInt64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeF32(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeF32Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float32 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetAttributeF64(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64* attrVal
);

int32 __stdcall RFmxWLAN_SetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeF64Array(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   float64 attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeNIComplexSingleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexSingle attrVal[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_SetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_GetAttributeNIComplexDoubleArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   NIComplexDouble attrVal[],
   int32 arraySize,
   int32* actualArraySize
);


int32 __stdcall RFmxWLAN_SetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_GetAttributeString(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attributeID,
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_OFDMModAccClearNoiseCalibrationDatabase(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxWLAN_OFDMModAccCfg1ReferenceWaveform(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   NIComplexSingle referenceWaveform[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccCfg1ReferenceWaveformSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccAutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxWLAN_OFDMModAccValidateCalibrationData(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* calibrationDataValid
);

int32 __stdcall RFmxWLAN_AnalyzeIQ1Waveform(
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

int32 __stdcall RFmxWLAN_AnalyzeIQ1WaveformSplit(
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

int32 __stdcall RFmxWLAN_AnalyzeSpectrum1Waveform(
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

int32 __stdcall RFmxWLAN_AutoDetectSignal(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxWLAN_AutoLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 measurementInterval
);

int32 __stdcall RFmxWLAN_CheckMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32* isDone
);

int32 __stdcall RFmxWLAN_ClearAllNamedResults(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_ClearNamedResult(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_CloneSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char oldSignalName[],
   char newSignalName[]
);

int32 __stdcall RFmxWLAN_Commit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_CfgSelectedPortsMultiple(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char selectedPorts[]
);

int32 __stdcall RFmxWLAN_CreateSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxWLAN_DeleteSignalConfiguration(
   niRFmxInstrHandle instrumentHandle,
   char signalName[]
);

int32 __stdcall RFmxWLAN_Initiate(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultName[]
);

int32 __stdcall RFmxWLAN_ResetToDefault(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_SendSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle
);

int32 __stdcall RFmxWLAN_WaitForMeasurementComplete(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout
);

int32 __stdcall RFmxWLAN_AutoDetectSignalAnalysisOnly(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   NIComplexSingle IQ[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_AutoDetectSignalAnalysisOnlySplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0,
   float64 dx,
   float32 IQI[],
   float32 IQQ[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 acquisitionLengthMode,
   float64 acquisitionLength
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 EVMUnit
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementOffset,
   int32 maximumMeasurementLength
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 powerMeasurementEnabled
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementNumberOfCustomGates(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfCustomGates
);

int32 __stdcall RFmxWLAN_DSSSModAccCfgPowerMeasurementCustomGateArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 startTime[],
   float64 stopTime[],
   int32 numberOfElements
);

int32 __stdcall RFmxWLAN_SEMCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount,
   int32 averagingType
);

int32 __stdcall RFmxWLAN_SEMCfgMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 maskType
);

int32 __stdcall RFmxWLAN_SEMCfgNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfOffsets
);

int32 __stdcall RFmxWLAN_SEMCfgSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 spanAuto,
   float64 span
);

int32 __stdcall RFmxWLAN_SEMCfgSweepTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 sweepTimeAuto,
   float64 sweepTimeInterval
);

int32 __stdcall RFmxWLAN_SEMCfgOffsetFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 offsetStartFrequency[],
   float64 offsetStopFrequency[],
   int32 offsetSideband[],
   int32 numberOfElements
);

int32 __stdcall RFmxWLAN_SEMCfgOffsetRelativeLimitArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 relativeLimitStart[],
   float64 relativeLimitStop[],
   int32 numberOfElements
);

int32 __stdcall RFmxWLAN_CfgChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 channelBandwidth
);

int32 __stdcall RFmxWLAN_CfgExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 externalAttenuation
);

int32 __stdcall RFmxWLAN_CfgFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency
);

int32 __stdcall RFmxWLAN_CfgNumberOfFrequencySegmentsAndReceiveChains(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 numberOfFrequencySegments,
   int32 numberOfReceiveChains
);

int32 __stdcall RFmxWLAN_CfgReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 referenceLevel
);

int32 __stdcall RFmxWLAN_CfgStandard(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 standard
);

int32 __stdcall RFmxWLAN_CfgFrequencyArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 centerFrequency[],
   int32 numberOfElements
);

int32 __stdcall RFmxWLAN_TXPCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxWLAN_TXPCfgBurstDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 burstDetectionEnabled
);

int32 __stdcall RFmxWLAN_TXPCfgMaximumMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 maximumMeasurementInterval
);

int32 __stdcall RFmxWLAN_PowerRampCfgAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 acquisitionLength
);

int32 __stdcall RFmxWLAN_PowerRampCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 acquisitionLengthMode,
   float64 acquisitionLength
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgAmplitudeTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 amplitudeTrackingEnabled
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgAveraging(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 averagingEnabled,
   int32 averagingCount
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 channelEstimationType
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 commonClockSourceEnabled
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 EVMUnit
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgFrequencyErrorEstimationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 frequencyErrorEstimationMethod
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementOffset,
   int32 maximumMeasurementLength
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 measurementMode
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 noiseCompensationEnabled
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgOptimizeDynamicRangeForEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 optimizeDynamicRangeForEVMEnabled,
   float64 optimizeDynamicRangeForEVMMargin
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 phaseTrackingEnabled
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgSymbolClockErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 symbolClockErrorCorrectionEnabled
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgNReferenceWaveforms(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0[],
   float64 dx[],
   NIComplexSingle referenceWaveform[],
   int32 referenceWaveformSize[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccCfgNReferenceWaveformsSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 x0[],
   float64 dx[],
   float32 referenceWaveformI[],
   float32 referenceWaveformQ[],
   int32 referenceWaveformSize[],
   int32 arraySize
);

int32 __stdcall RFmxWLAN_AbortMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_AnalyzeNWaveformsIQ(
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

int32 __stdcall RFmxWLAN_AnalyzeNWaveformsIQSplit(
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

int32 __stdcall RFmxWLAN_AnalyzeNWaveformsSpectrum(
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

int32 __stdcall RFmxWLAN_CfgDigitalEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char digitalEdgeSource[],
   int32 digitalEdge,
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxWLAN_CfgIQPowerEdgeTrigger(
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

int32 __stdcall RFmxWLAN_CfgSoftwareEdgeTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 triggerDelay,
   int32 enableTrigger
);

int32 __stdcall RFmxWLAN_DisableTrigger(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[]
);

int32 __stdcall RFmxWLAN_GetAllNamedResultNames(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char resultNames[],
   int32 resultNamesBufferSize,
   int32* actualResultNamesSize,
   int32* defaultResultExists
);

int32 __stdcall RFmxWLAN_SelectMeasurements(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   uInt32 measurements,
   int32 enableAllTraces
);

int32 __stdcall RFmxWLAN_TXPFetchPowerTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 power[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_TXPFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* averagePowerMean,
   float64* peakPowerMaximum
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle constellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 constellationI[],
   float32 constellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchCustomGatePowersArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 averagePowerMean[],
   float64 peakPowerMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchDecodedHeaderBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedHeaderBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchDecodedPSDUBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedPSDUBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchEVMPerChipMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 EVMPerChipMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchAveragePowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* preambleAveragePowerMean,
   float64* headerAveragePowerMean,
   float64* dataAveragePowerMean,
   float64* PPDUAveragePowerMean
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RMSEVMMean,
   float64* peakEVM80211_2016Maximum,
   float64* peakEVM80211_2007Maximum,
   float64* peakEVM80211_1999Maximum,
   float64* frequencyErrorMean,
   float64* chipClockErrorMean,
   int32* numberOfChipsUsed
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* IQOriginOffsetMean,
   float64* IQGainImbalanceMean,
   float64* IQQuadratureErrorMean
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchPeakPowers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* preamblePeakPowerMaximum,
   float64* headerPeakPowerMaximum,
   float64* dataPeakPowerMaximum,
   float64* PPDUPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_DSSSModAccFetchPPDUInformation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* dataModulationFormat,
   int32* payloadLength,
   int32* preambleType,
   int32* lockedClocksBit,
   int32* headerCRCStatus,
   int32* PSDUCRCStatus
);

int32 __stdcall RFmxWLAN_PowerRampFetchFallTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 rawWaveform[],
   float32 processedWaveform[],
   float32 threshold[],
   float32 powerReference[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_PowerRampFetchRiseTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 rawWaveform[],
   float32 processedWaveform[],
   float32 threshold[],
   float32 powerReference[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_PowerRampFetchMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* riseTimeMean,
   float64* fallTimeMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainDataRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chainDataRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chainPilotRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chainRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 chainRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChannelFrequencyResponseMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 channelFrequencyResponseMeanMagnitude[],
   float32 channelFrequencyResponseMeanPhase[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchGroupDelayMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 groupDelayMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchCommonPilotErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 commonPilotErrorMagnitude[],
   float32 commonPilotErrorPhase[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchCustomGatePowersArray(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 averagePowerMean[],
   float64 peakPowerMaximum[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle dataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 dataConstellationI[],
   float32 dataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle referenceDataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 referenceDataConstellationI[],
   float32 referenceDataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedLSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedLSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedPSDUBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedPSDUBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedServiceBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedServiceBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedSIGBBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedSIGBBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedUSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedEHTSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedEHTSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedUHRSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedUHRSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDecodedELRSIGBitsTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 decodedELRSIGBits[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchEVMSubcarrierIndices(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 subcarrierIndices[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 IQGainImbalancePerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 IQQuadratureErrorPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle pilotConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPilotConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 pilotConstellationI[],
   float32 pilotConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleFrequencyErrorTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 preambleFrequencyError[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatnessMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 spectralFlatnessMean[],
   float32 spectralFlatnessLowerMask[],
   float32 spectralFlatnessUpperMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 streamDataRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 streamPilotRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 streamRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 streamRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 subcarrierIndex,
   float64* x0,
   float64* dx,
   float32 subcarrierChainEVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 subcarrierIndex,
   float64* x0,
   float64* dx,
   float32 subcarrierStreamEVMPerSymbol[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 symbolIndex,
   float64* x0,
   float64* dx,
   float32 symbolChainEVMPerSubcarrier[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32 symbolIndex,
   float64* x0,
   float64* dx,
   float32 symbolStreamEVMPerSubcarrier[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneErrorMarginPerRU(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64 unusedToneErrorMarginPerRU[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneErrorMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 unusedToneError[],
   float32 unusedToneErrorMask[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserDataConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle userDataConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserDataConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 userDataConstellationI[],
   float32 userDataConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserPilotConstellationTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   NIComplexSingle userPilotConstellation[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserPilotConstellationTraceSplit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float32 userPilotConstellationI[],
   float32 userPilotConstellationQ[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 userStreamDataRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 userStreamPilotRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 userStreamRMSEVMPerSubcarrierMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 userStreamRMSEVMPerSymbolMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPhaseNoisePSDMeanTrace(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* x0,
   float64* dx,
   float32 phaseNoisePSDMean[],
   int32 arraySize,
   int32* actualArraySize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchChainRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* chainRMSEVMMean,
   float64* chainDataRMSEVMMean,
   float64* chainPilotRMSEVMMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchCompositeRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* compositeRMSEVMMean,
   float64* compositeDataRMSEVMMean,
   float64* compositePilotRMSEVMMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchCrossPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* crossPowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDataAveragePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* dataAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchDataPeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* dataPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorCCDF10Percent(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* frequencyErrorCCDF10Percent
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchFrequencyErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* frequencyErrorMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchGuardIntervalType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* guardIntervalType
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchLTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* LTFSize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchIQImpairments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* relativeIQOriginOffsetMean,
   float64* IQGainImbalanceMean,
   float64* IQQuadratureErrorMean,
   float64* absoluteIQOriginOffsetMean,
   float64* IQTimingSkewMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchLSIGParityCheckStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* LSIGParityCheckStatus
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchMCSIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* MCSIndex
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfHESIGBSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfHESIGBSymbols
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfSpaceTimeStreams(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfSpaceTimeStreams
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberofSymbolsUsed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfSymbolsUsed
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* numberOfUsers
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPEAveragePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PEAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPEPeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PEPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUAveragePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PPDUAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUPeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PPDUPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPPDUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* PPDUType
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* VHTSIGAAveragePowerMean,
   float64* VHTSTFAveragePowerMean,
   float64* VHTLTFAveragePowerMean,
   float64* VHTSIGBAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RLSIGAveragePowerMean,
   float64* HESIGAAveragePowerMean,
   float64* HESIGBAveragePowerMean,
   float64* HESTFAveragePowerMean,
   float64* HELTFAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RLSIGAveragePowerMean,
   float64* USIGAveragePowerMean,
   float64* EHTSIGAveragePowerMean,
   float64* EHTSTFAveragePowerMean,
   float64* EHTLTFAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* HTSIGAveragePowerMean,
   float64* HTSTFAveragePowerMean,
   float64* HTDLTFAveragePowerMean,
   float64* HTELTFAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreambleAveragePowersCommon(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* LSTFAveragePowerMean,
   float64* LLTFAveragePowerMean,
   float64* LSIGAveragePowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* VHTSIGAPeakPowerMaximum,
   float64* VHTSTFPeakPowerMaximum,
   float64* VHTLTFPeakPowerMaximum,
   float64* VHTSIGBPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RLSIGPeakPowerMaximum,
   float64* HESIGAPeakPowerMaximum,
   float64* HESIGBPeakPowerMaximum,
   float64* HESTFPeakPowerMaximum,
   float64* HELTFPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11be(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* RLSIGPeakPowerMaximum,
   float64* USIGPeakPowerMaximum,
   float64* EHTSIGPeakPowerMaximum,
   float64* EHTSTFPeakPowerMaximum,
   float64* EHTLTFPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* HTSIGPeakPowerMaximum,
   float64* HTSTFPeakPowerMaximum,
   float64* HTDLTFPeakPowerMaximum,
   float64* HTELTFPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPreamblePeakPowersCommon(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* LSTFPeakPowerMaximum,
   float64* LLTFPeakPowerMaximum,
   float64* LSIGPeakPowerMaximum
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPSDUCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* PSDUCRCStatus
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchPEDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* PEDuration
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchRUOffsetAndSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* RUOffset,
   int32* RUSize
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* SIGCRCStatus
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSIGBCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* SIGBCRCStatus
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSpectralFlatness(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* spectralFlatnessMargin,
   int32* spectralFlatnessMarginSubcarrierIndex
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchStreamRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* streamRMSEVMMean,
   float64* streamDataRMSEVMMean,
   float64* streamPilotRMSEVMMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchSymbolClockErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* symbolClockErrorMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUnusedToneError(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* unusedToneErrorMargin,
   int32* unusedToneErrorMarginRUIndex
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* userPowerMean
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchUserStreamRMSEVM(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* userStreamRMSEVMMean,
   float64* userStreamDataRMSEVMMean,
   float64* userStreamPilotRMSEVMMean
);

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetMarginArray(
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

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPowerArray(
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

int32 __stdcall RFmxWLAN_SEMFetchSpectrum(
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

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetMarginArray(
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

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPowerArray(
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

int32 __stdcall RFmxWLAN_SEMFetchCarrierMeasurement(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* absolutePower,
   float64* relativePower
);

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxWLAN_SEMFetchLowerOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAbsolutePower,
   float64* totalRelativePower,
   float64* peakAbsolutePower,
   float64* peakFrequency,
   float64* peakRelativePower
);

int32 __stdcall RFmxWLAN_SEMFetchMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus
);

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* measurementStatus,
   float64* margin,
   float64* marginFrequency,
   float64* marginAbsolutePower,
   float64* marginRelativePower
);

int32 __stdcall RFmxWLAN_SEMFetchUpperOffsetPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   float64* totalAbsolutePower,
   float64* totalRelativePower,
   float64* peakAbsolutePower,
   float64* peakFrequency,
   float64* peakRelativePower
);

int32 __stdcall RFmxWLAN_GetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_SetSelectedPorts(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWLAN_GetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetCenterFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetExternalAttenuation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetReferenceLevelHeadroom(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_SetDigitalEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWLAN_GetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetDigitalEdgeTriggerEdge(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_SetIQPowerEdgeTriggerSource(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWLAN_GetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetIQPowerEdgeTriggerLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetIQPowerEdgeTriggerLevelType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetIQPowerEdgeTriggerSlope(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerDelay(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerMinimumQuietTimeMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerMinimumQuietTimeDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerGateEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerGateEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetTriggerGateLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetTriggerGateLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetStandard(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetStandard(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetNumberOfFrequencySegments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetNumberOfFrequencySegments(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetNumberOfReceiveChains(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetNumberOfReceiveChains(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMFrequencySegmentIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMFrequencySegmentIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMTransmitPowerClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMTransmitPowerClass(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMFrequencyBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMFrequencyBand(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMAutoPPDUTypeDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMAutoPPDUTypeDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPPDUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPPDUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMHeaderDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMHeaderDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMSIGCompressionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMSIGCompressionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMMCSIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMMCSIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMScramblerSeed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMScramblerSeed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMFECCodingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMFECCodingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMRUSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMRUSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMRUOffsetMRUIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMRUOffsetMRUIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMRUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMRUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMDistributionBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMDistributionBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMGuardIntervalType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMGuardIntervalType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMLTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMLTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPreFECPaddingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPreFECPaddingFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMLDPCExtraSymbolSegment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMLDPCExtraSymbolSegment(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPEDisambiguity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPEDisambiguity(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMSTBCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMSTBCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfSpaceTimeStreams(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfSpaceTimeStreams(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMSpaceTimeStreamOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMSpaceTimeStreamOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfHESIGBSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfHESIGBSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfSIGSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfSIGSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMDCMEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMDCMEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDM2xLDPCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDM2xLDPCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMIMPilotsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMIMPilotsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMUnequalModulationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMUnequalModulationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMUnequalModulationPatternIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMUnequalModulationPatternIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfLTFSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfLTFSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMMUMIMOLTFModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMMUMIMOLTFModeEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPreamblePuncturingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPreamblePuncturingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPreamblePuncturingBitmap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPreamblePuncturingBitmap(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int64 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMAutoPhaseRotationDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMAutoPhaseRotationDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPhaseRotationCoefficient1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPhaseRotationCoefficient1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPhaseRotationCoefficient2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPhaseRotationCoefficient2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMPhaseRotationCoefficient3(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMPhaseRotationCoefficient3(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetDetectedStandard(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_GetDetectedChannelBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_GetDetectedBurstLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_GetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetAutoLevelInitialReferenceLevel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetSampleClockRateFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetSampleClockRateFactor(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_GetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetLimitedConfigurationChange(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SetResultFetchTimeout(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetAcquisitionLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetAcquisitionLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetMaximumMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetMaximumMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPulseShapingFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPulseShapingFilterType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPulseShapingFilterParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPulseShapingFilterParameter(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetEqualizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetEqualizationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetBurstStartDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetBurstStartDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPowerMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPowerMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPowerNumberOfCustomGates(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPowerNumberOfCustomGates(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPowerCustomGateStartTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPowerCustomGateStartTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetPowerCustomGateStopTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetPowerCustomGateStopTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetFrequencyErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetFrequencyErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetChipClockErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetChipClockErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetIQOriginOffsetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetIQOriginOffsetCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetDataDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetDataDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2016Mean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2016Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2007Mean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_2007Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_1999Mean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPeakEVM802_11_1999Maximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsNumberOfChipsUsed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsFrequencyErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsChipClockErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsIQGainImbalanceMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsIQQuadratureErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsRMSMagnitudeErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsRMSPhaseErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPreambleAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPreamblePeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsHeaderAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsHeaderPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsDataAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsDataPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPPDUAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPPDUPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsCustomGateAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsCustomGatePeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsDataModulationFormat(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPayloadLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPreambleType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsLockedClocksBit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsHeaderCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_DSSSModAccGetResultsPSDUCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetVectorAveragingTimeAlignmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetVectorAveragingTimeAlignmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetVectorAveragingPhaseAlignmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetVectorAveragingPhaseAlignmentEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetMeasurementMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetEVMReferenceDataSymbolsMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetEVMReferenceDataSymbolsMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetEVMUnit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAcquisitionLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAcquisitionLengthMode(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetMeasurementOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetMaximumMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetMaximumMeasurementLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetCombinedSignalDemodulationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetCombinedSignalDemodulationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetReferenceDataConstellationIdentifier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 arraySize,
   char attrVal[]
);

int32 __stdcall RFmxWLAN_OFDMModAccSetReferenceDataConstellationIdentifier(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   char attrVal[]
);

int32 __stdcall RFmxWLAN_OFDMModAccGetBurstStartDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetBurstStartDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetFrequencyErrorEstimationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetFrequencyErrorEstimationMethod(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetCommonClockSourceEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetCommonPilotErrorScalingReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetCommonPilotErrorScalingReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAmplitudeTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAmplitudeTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetPhaseTrackingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetSymbolClockErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetSymbolClockErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetSpectrumInverted(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationInterpolationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationInterpolationType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationSmoothingLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationSmoothingLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationRelativeDelaySpread(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationRelativeDelaySpread(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationLTFAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationLTFAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationLLTFEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationLLTFEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetPowerMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetPowerMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetPowerNumberOfCustomGates(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetPowerNumberOfCustomGates(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetPowerCustomGateStartTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetPowerCustomGateStartTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetPowerCustomGateStopTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetPowerCustomGateStopTime(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelMatrixPowerEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelMatrixPowerEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQImpairmentsEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQImpairmentsEstimationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQImpairmentsModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQImpairmentsModel(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQGainImbalanceCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQQuadratureErrorCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQTimingSkewCorrectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetIQImpairmentsPerSubcarrierEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetIQImpairmentsPerSubcarrierEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetUnusedToneErrorMaskReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetUnusedToneErrorMaskReference(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetDataDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetDataDecodingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetNoiseCompensationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetNoiseCompensationInputPowerCheckEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetNoiseCompensationInputPowerCheckEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetNoiseCompensationReferenceLevelCoercionLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetNoiseCompensationReferenceLevelCoercionLimit(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetOptimizeDynamicRangeForEVMEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetOptimizeDynamicRangeForEVMEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetOptimizeDynamicRangeForEVMMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetOptimizeDynamicRangeForEVMMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAutoLevelAllowOverflow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAutoLevelAllowOverflow(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCompositeRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCompositeDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCompositePilotRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamRMSEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamRMSEVMMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamPilotRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainRMSEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainRMSEVMMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainPilotRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserStreamRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserStreamRMSEVMMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserStreamRMSEVMMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserStreamDataRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserStreamPilotRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSIGBRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRSIGRMSEVMMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLLTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLLTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRLSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRLSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSIGAAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSIGAPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESIGAAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESIGAPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRMARKAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRMARKPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSIGBAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSIGBPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESIGBAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESIGBPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRSIGAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRSIGPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTGFSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTGFSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHESTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTDLTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTDLTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTELTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHTELTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTLTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsVHTLTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHELTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHELTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTLTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTLTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRLTFAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRLTFPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsDataAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsDataPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPEAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPEPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPPDUAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPPDUPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCustomGateAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCustomGatePeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsCrossPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsChainStreamCrossPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUserPowerMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsStreamPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSpectralFlatnessMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSpectralFlatnessMarginMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSpectralFlatnessMarginMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSpectralFlatnessMarginSubcarrierIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUnusedToneErrorMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUnusedToneErrorMarginRUIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsBurstStartTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNumberOfSymbolsUsed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNoiseCompensationApplied(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsFrequencyErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsFrequencyErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsFrequencyErrorMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsFrequencyErrorCCDF10Percent(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSymbolClockErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSymbolClockErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSymbolClockErrorMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRelativeIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRelativeIQOriginOffsetMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRelativeIQOriginOffsetMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsAbsoluteIQOriginOffsetMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQGainImbalanceMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQGainImbalanceMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQGainImbalanceMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQQuadratureErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQQuadratureErrorMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQQuadratureErrorMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIQTimingSkewMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRMSCommonPhaseErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRMSCommonPilotErrorMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPPDUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsMCSIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsAggregation(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsFECCodingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRUSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRUOffsetMRUIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRUType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsDistributionBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNumberOfUsers(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNumberOfHESIGBSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNumberOfSIGSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsGuardIntervalType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsNumberOfSpaceTimeStreams(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSpaceTimeStreamOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsDCMEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResults2xLDPCEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsIMPilotsEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUnequalModulationEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUnequalModulationPatternIndex(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsLSIGParityCheckStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsSIGBCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsEHTSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsUHRSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsELRSIGCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPSDUCRCStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsScramblerSeed(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPEDuration(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPhaseRotationCoefficient1(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPhaseRotationCoefficient2(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsPhaseRotationCoefficient3(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetMaskType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetCarrierIntegrationBandwidth(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetNumberOfOffsets(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetOffsetStartFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetOffsetStopFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetOffsetSideband(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetOffsetRelativeLimitStart(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetOffsetRelativeLimitStop(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetSpanAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetSpanAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetSpan(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetSweepTimeAuto(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetSweepTimeInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetAveragingType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetAmplitudeCorrectionType(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsCarrierAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsCarrierAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsCarrierPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsLowerOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetMeasurementStatus(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetAbsoluteIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetRelativeIntegratedPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetAbsolutePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetRelativePeakPower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetPeakFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetMargin(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetMarginAbsolutePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetMarginRelativePower(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_SEMGetResultsUpperOffsetMarginFrequency(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetMaximumMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetMaximumMeasurementInterval(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetBurstDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetBurstDetectionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_TXPSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsAveragePowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsAveragePowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsAveragePowerMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsPeakPowerMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsPeakPowerMaximum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_TXPGetResultsPeakPowerMinimum(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetMeasurementEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetAcquisitionLength(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetAveragingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetAveragingCount(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetAllTracesEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampSetNumberOfAnalysisThreads(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetResultsRiseTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

int32 __stdcall RFmxWLAN_PowerRampGetResultsFallTimeMean(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 *attrVal
);

#ifdef __cplusplus
}
#endif

/* ---------------- Obsolete Section ------------------ */

#define RFMXWLAN_ATTR_OFDM_EHT_SIG_COMPRESSION_ENABLED                                  0x00a0003a
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_SIG_SYMBOLS                                        0x00a0003b
#define RFMXWLAN_ATTR_OFDM_HE_LTF_SIZE                                                  0x00a0001d
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_HE_LTF_SIZE                                    0x00a04038
#define RFMXWLAN_ATTR_OFDM_NUMBER_OF_HE_LTF_SYMBOLS                                     0x00a00022
#define RFMXWLAN_ATTR_OFDM_RU_OFFSET                                                    0x00a0001b
#define RFMXWLAN_ATTR_OFDMMODACC_RESULTS_RU_OFFSET                                      0x00a04034
#define RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_ENABLED                   0x00a0406a

// Values for RFMXWLAN_ATTR_OFDM_EHT_SIG_COMPRESSION_ENABLED
#define RFMXWLAN_VAL_OFDM_EHT_SIG_COMPRESSION_ENABLED_FALSE                                         0
#define RFMXWLAN_VAL_OFDM_EHT_SIG_COMPRESSION_ENABLED_TRUE                                          1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_TYPE
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_TYPE_CHANNEL_ESTIMATION_REFERENCE                0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_TYPE_CHANNEL_ESTIMATION_REFERENCE_AND_DATA       1

// Values for RFMXWLAN_ATTR_OFDM_HE_LTF_SIZE
#define RFMXWLAN_VAL_OFDM_HE_LTF_SIZE_4X                                                            0
#define RFMXWLAN_VAL_OFDM_HE_LTF_SIZE_2X                                                            1
#define RFMXWLAN_VAL_OFDM_HE_LTF_SIZE_1X                                                            2
#define RFMXWLAN_VAL_OFDM_HE_LTF_SIZE_NOT_APPLICABLE                                                -1

// Values for RFMXWLAN_ATTR_OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_ENABLED
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_ENABLED_FALSE                          0
#define RFMXWLAN_VAL_OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_ENABLED_TRUE                           1

#ifdef __cplusplus
extern "C"
{
#endif

int32 __stdcall RFmxWLAN_AnalyzeIQ(
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

int32 __stdcall RFmxWLAN_AnalyzeIQSplit(
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

int32 __stdcall RFmxWLAN_AnalyzeSpectrum(
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

int32 __stdcall RFmxWLAN_GetOFDMHELTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMHELTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsHELTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccFetchHELTFSize(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   float64 timeout,
   int32* HELTFSize
);

int32 __stdcall RFmxWLAN_GetOFDMNumberHELTFSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberHELTFSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMRUOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMRUOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetResultsRUOffset(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccGetChannelEstimationSmoothingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_OFDMModAccSetChannelEstimationSmoothingEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMEHTSIGCompressionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMEHTSIGCompressionEnabled(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

int32 __stdcall RFmxWLAN_GetOFDMNumberOfEHTSIGSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 *attrVal
);

int32 __stdcall RFmxWLAN_SetOFDMNumberOfEHTSIGSymbols(
   niRFmxInstrHandle instrumentHandle,
   char selectorString[],
   int32 attrVal
);

#ifdef __cplusplus
}
#endif


#endif
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSA.h sha256=e593df5e117991772b0215cf75981e07c15e44784f97af5a1ca9670cc120820c bytes=85789 -->
## FILE: imports/include/niRFSA.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSA.h`
- sha256: `e593df5e117991772b0215cf75981e07c15e44784f97af5a1ca9670cc120820c`
- bytes: 85789

````c
/****************************************************************************
 *                           NI RF Signal Analyzer
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2006-2020.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niRFSA.h
 * Purpose:  NI RF Signal Analyzer
 *           Instrument Driver declarations.
 *
 ****************************************************************************/
#ifndef ___niRFSA_niRFSA_h___
#define ___niRFSA_niRFSA_h___

#include <ivi.h>
#include "niRFSAErrors.h"

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

// Bitness check for Supported Platforms
#if ((defined(_WIN32) || defined(WIN32)) && !defined(_WIN64))
   #define kRFSA_32BitPlatform 1
#elif defined(_WIN64) || (defined(__linux__) && defined(__x86_64__))
   #define kRFSA_64BitPlatform 1
#else
   #error "Unknown platform"
#endif

/* Pragma used in CVI to indicate that functions in this file have
 * user protection associated with them */
#ifdef _CVI_
 #pragma EnableLibraryRuntimeChecking
#endif

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/

/*- IVI Inherent Attributes --------------------------------------------*/

/*- User Options */
#define NIRFSA_ATTR_CACHE                                  /* ViBoolean */  IVI_ATTR_CACHE
#define NIRFSA_ATTR_RANGE_CHECK                            /* ViBoolean */  IVI_ATTR_RANGE_CHECK
#define NIRFSA_ATTR_QUERY_INSTRUMENT_STATUS                /* ViBoolean */  IVI_ATTR_QUERY_INSTRUMENT_STATUS
#define NIRFSA_ATTR_RECORD_COERCIONS                       /* ViBoolean */  IVI_ATTR_RECORD_COERCIONS
#define NIRFSA_ATTR_SIMULATE                               /* ViBoolean */  IVI_ATTR_SIMULATE
#define NIRFSA_ATTR_INTERCHANGE_CHECK                      /* ViBoolean */  IVI_ATTR_INTERCHANGE_CHECK

/*- Instrument Capabilities --------------------------------------------*/

/*- Specific Driver Information, Read-only -----------------------------*/
#define NIRFSA_ATTR_SPECIFIC_DRIVER_DESCRIPTION               /* ViString */  IVI_ATTR_SPECIFIC_DRIVER_DESCRIPTION
#define NIRFSA_ATTR_SPECIFIC_DRIVER_PREFIX                    /* ViString */  IVI_ATTR_SPECIFIC_DRIVER_PREFIX
#define NIRFSA_ATTR_SPECIFIC_DRIVER_VENDOR                    /* ViString */  IVI_ATTR_SPECIFIC_DRIVER_VENDOR
#define NIRFSA_ATTR_SPECIFIC_DRIVER_REVISION                  /* ViString */  IVI_ATTR_SPECIFIC_DRIVER_REVISION
#define NIRFSA_ATTR_SUPPORTED_INSTRUMENT_MODELS               /* ViString */  IVI_ATTR_SUPPORTED_INSTRUMENT_MODELS
#define NIRFSA_ATTR_CHANNEL_COUNT                             /* ViInt32  */  IVI_ATTR_CHANNEL_COUNT
#define NIRFSA_ATTR_INSTRUMENT_MANUFACTURER                   /* ViString */  IVI_ATTR_INSTRUMENT_MANUFACTURER
#define NIRFSA_ATTR_INSTRUMENT_MODEL                          /* ViString */  IVI_ATTR_INSTRUMENT_MODEL
#define NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION              /* ViString */  IVI_ATTR_INSTRUMENT_FIRMWARE_REVISION
#define NIRFSA_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION  /* ViInt32  */  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION
#define NIRFSA_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION  /* ViInt32  */  IVI_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION
#define NIRFSA_ATTR_GROUP_CAPABILITIES                        /* ViString */  IVI_ATTR_GROUP_CAPABILITIES

/*- Instrument Information -*/
#define NIRFSA_ATTR_MEMORY_SIZE                               /* ViInt64  */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 85L)

/*- Advanced Session Information, read-only ----------------------------*/
#define NIRFSA_ATTR_IO_RESOURCE_DESCRIPTOR                 /* ViString */  IVI_ATTR_RESOURCE_DESCRIPTOR
#define NIRFSA_ATTR_LOGICAL_NAME                           /* ViString */  IVI_ATTR_LOGICAL_NAME
#define NIRFSA_ATTR_DRIVER_SETUP                           /* ViString */  IVI_ATTR_DRIVER_SETUP

/*- Instrument-Specific Attributes -------------------------------------*/

/*- Acquisition Type ---------------------------------------------------*/
#define NIRFSA_ATTR_ACQUISITION_TYPE                       /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 1L)

/*- Vertical -----------------------------------------------------------*/
#define NIRFSA_ATTR_REFERENCE_LEVEL                        /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 4L)
#define NIRFSA_ATTR_REFERENCE_LEVEL_HEADROOM               /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 309L)
#define NIRFSA_ATTR_ATTENUATION                            /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 5L)
#define NIRFSA_ATTR_MIXER_LEVEL                            /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 6L)
#define NIRFSA_ATTR_MIXER_LEVEL_OFFSET                     /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 127L)
#define NIRFSA_ATTR_MECHANICAL_ATTENUATION                 /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 128L)
#define NIRFSA_ATTR_RF_PREAMP_ENABLED                      /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 129L)
#define NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL                  /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 130L)
#define NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET           /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 131L)
#define NIRFSA_ATTR_RF_ATTENUATION_STEP_SIZE               /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 155L)
#define NIRFSA_ATTR_DEVICE_CONFIGURATION_TEMPERATURE       /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 159L)

#define NIRFSA_ATTR_IF_ATTENUATION                         /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 74L)
#define NIRFSA_ATTR_RF_ATTENUATION_INDEX                   /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 76L)
#define NIRFSA_ATTR_RF_ATTENUATION_TABLE                   /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 77L)
#define NIRFSA_ATTR_IF1_ATTEN_VALUE                        /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 78L)
#define NIRFSA_ATTR_IF2_ATTEN_VALUE                        /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 79L)
#define NIRFSA_ATTR_MINIMUM_ACPR                           /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 142L)
#define NIRFSA_ATTR_OSP_DATA_SCALING_FACTOR                /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 151L)
#define NIRFSA_ATTR_OVERFLOW_ERROR_REPORTING               /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 271L)
#define NIRFSA_ATTR_STEP_GAIN_ENABLED                      /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 157L)
#define NIRFSA_ATTR_AMPLITUDE_SETTLING                     /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 163L)
#define NIRFSA_ATTR_DIGITAL_GAIN                           /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 301L)

/*- Signal Path Control (Advanced) --------------------------------------*/
#define NIRFSA_ATTR_CHANNEL_COUPLING                       /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 149L)
#define NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED      /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 132L)
#define NIRFSA_ATTR_INPUT_ISOLATION_ENABLED                /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 170L)
#define NIRFSA_ATTR_RF_PRESELECTOR_FILTER                  /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 166L)
#define NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED           /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 207L)
#define NIRFSA_ATTR_NOTCH_FILTER_ENABLED                   /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 167L)
#define NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED            /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 160L)
#define NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED/* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 161L)
#define NIRFSA_ATTR_IF_FILTER_BANDWIDTH                    /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 205L)
#define NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS         /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 324L)
#define NIRFSA_ATTR_SELECTED_PORTS                         /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 297L)
#define NIRFSA_ATTR_AVAILABLE_PORTS                        /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 306L)

/*- IQ Acquisition -----------------------------------------------------*/
#define NIRFSA_ATTR_IQ_CARRIER_FREQUENCY                   /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 59L)
#define NIRFSA_ATTR_IQ_RATE                                /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 7L)
#define NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE            /* ViBoolean   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 8L)
#define NIRFSA_ATTR_NUMBER_OF_SAMPLES                      /* ViInt64     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 9L)
#define NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE            /* ViBoolean   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 10L)
#define NIRFSA_ATTR_NUMBER_OF_RECORDS                      /* ViInt64     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 11L)
#define NIRFSA_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY         /* ViBoolean   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 154L)

/*- Spectrum Acquisition -----------------------------------------------*/
#define NIRFSA_ATTR_CENTER_FREQUENCY                       /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 2L)
#define NIRFSA_ATTR_SPECTRUM_SPAN                          /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 3L)
#define NIRFSA_ATTR_IF_OUTPUT_FREQUENCY                    /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 86L)
#define NIRFSA_ATTR_POWER_SPECTRUM_UNITS                   /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 12L)
#define NIRFSA_ATTR_RESOLUTION_BANDWIDTH                   /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 13L)
#define NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE              /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 14L)
#define NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES            /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 15L)
#define NIRFSA_ATTR_SPECTRUM_AVERAGING_MODE                /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 16L)
#define NIRFSA_ATTR_FFT_WINDOW_TYPE                        /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 17L)
#define NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES               /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 18L)
#define NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO            /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 144L)
#define NIRFSA_ATTR_FFT_WIDTH                              /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 169L)
#define NIRFSA_ATTR_SMOOTH_SPECTRUM_ENABLED                /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 219L)

/*- Clocking -----------------------------------------------------------*/
#define NIRFSA_ATTR_REF_CLOCK_SOURCE                       /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 19L)
#define NIRFSA_ATTR_REF_CLOCK_RATE                         /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 20L)
#define NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 21L)
#define NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE   /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 22L)
#define NIRFSA_ATTR_PXI_CHASSIS_CLK10_SOURCE               /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 23L)
#define NIRFSA_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL     /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 72L)
#define NIRFSA_ATTR_EXPORTED_REF_CLOCK_RATE                /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 326L)
#define NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_RATE                      /* ViReal64 */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 228L)
#define NIRFSA_ATTR_EXPORTED_DIGITIZER_SAMPLE_CLOCK_OUTPUT_TERMINAL  /* ViString */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 229L)

/*- Start Trigger ------------------------------------------------------*/
#define NIRFSA_ATTR_START_TRIGGER_TYPE                     /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 24L)
#define NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE      /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 25L)
#define NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE        /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 26L)
#define NIRFSA_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 27L)
#define NIRFSA_ATTR_START_TRIGGER_TERMINAL_NAME            /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 122L)

/*- Reference Trigger --------------------------------------------------*/
#define NIRFSA_ATTR_REF_TRIGGER_TYPE                       /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 28L)
#define NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE        /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 29L)
#define NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE          /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 30L)
#define NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME         /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 58L)
#define NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SOURCE       /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 55L)
#define NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL        /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 56L)
#define NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE        /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 57L)
#define NIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL   /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 32L)
#define NIRFSA_ATTR_REF_TRIGGER_TERMINAL_NAME              /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 123L)
#define NIRFSA_ATTR_REF_TRIGGER_DELAY                      /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 60L)
#define NIRFSA_ATTR_START_TO_REF_TRIGGER_HOLDOFF           /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 33L)
#define NIRFSA_ATTR_REF_TO_REF_TRIGGER_HOLDOFF             /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 34L)
#define NIRFSA_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES         /* ViInt64     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 35L)
#define NIRFSA_ATTR_REF_TRIGGER_OSP_DELAY_ENABLED          /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 196L)

/*- Advance Trigger ---------------------------------------------------*/
#define NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE                     /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 36L)
#define NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE      /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 37L)
#define NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 38L)
#define NIRFSA_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME            /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 124L)

/*- Arm Reference Trigger ---------------------------------------------*/
#define NIRFSA_ATTR_ARM_REF_TRIGGER_TYPE                   /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 39L)
#define NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE    /* ViString    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 40L)

/*- Events -------------------------------------------------------------*/
#define NIRFSA_ATTR_EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL   /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 41L)
#define NIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 42L)
#define NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL     /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 43L)
#define NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL     /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 44L)
#define NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL              /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 54L)

#define NIRFSA_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME    /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 117L)
#define NIRFSA_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME  /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 118L)
#define NIRFSA_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME      /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 119L)
#define NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME      /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 120L)
#define NIRFSA_ATTR_DONE_EVENT_TERMINAL_NAME               /* ViString  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 121L)

#define NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS /* ViInt32  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 321L)
#define NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH       /* ViReal64 */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 322L)

/*- Fetching ------------------------------------------------------------*/
#define NIRFSA_ATTR_FETCH_RELATIVE_TO                      /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 45L)
#define NIRFSA_ATTR_FETCH_OFFSET                           /* ViInt64     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 46L)
#define NIRFSA_ATTR_RECORDS_DONE                           /* ViInt64     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 47L)
#define NIRFSA_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH        /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 104L)
#define NIRFSA_ATTR_DATA_TRANSFER_BLOCK_SIZE               /* ViInt32     */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 105L)
#define NIRFSA_ATTR_PHASE_OFFSET                           /* ViReal64    */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 106L)

/*- Advanced ------------------------------------------------------------*/
#define NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED        /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 48L)
#define NIRFSA_ATTR_FFT_WINDOW_SIZE                        /* ViInt32, read-only  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 49L)
#define NIRFSA_ATTR_FFT_SIZE                               /* ViInt32, read-only  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 50L)
#define NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR                /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 206L)
#define NIRFSA_ATTR_DEVICE_TEMPERATURE                     /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 51L)
#define NIRFSA_ATTR_TEMPERATURE_READ_INTERVAL              /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 61L)
#define NIRFSA_ATTR_DOWNCONVERTER_GAIN                     /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 65L)
#define NIRFSA_ATTR_NISCOPE_SESSION                        /* ViSession           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 52L)
#define NIRFSA_ATTR_RF_CONDITIONING_SESSION                /* ViSession           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 200L)
#define NIRFSA_ATTR_IF_CONDITIONING_SESSION                /* ViSession           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 201L)
#define NIRFSA_ATTR_DIGITIZER_VERTICAL_RANGE               /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 70L)
#define NIRFSA_ATTR_ENABLE_FRACTIONAL_RESAMPLING           /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 71L)
#define NIRFSA_ATTR_IF_FILTER                              /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 75L)
#define NIRFSA_ATTR_LO_TEMPERATURE                         /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 89L)
#define NIRFSA_ATTR_DIGITIZER_TEMPERATURE                  /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 90L)
#define NIRFSA_ATTR_RF_CONDITIONING_TEMPERATURE            /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 211L)
#define NIRFSA_ATTR_IF_CONDITIONING_TEMPERATURE            /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 210L)
#define NIRFSA_ATTR_FPGA_TEMPERATURE                       /* ViReal64, read-only */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 254L)

#define NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED               /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 80L)
#define NIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLED          /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 81L)
#define NIRFSA_ATTR_EXTERNAL_GAIN                          /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 94L)
#define NIRFSA_ATTR_5665_PRESELECTOR_TUNING_DAC_VALUE      /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 158L)

#define NIRFSA_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS  /* ViInt32          */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 256L)

#define NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION /* ViReal64         */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 300L)
#define NIRFSA_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE         /* ViReal64         */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 316L)

/*- Inband Retuning -----------------------------------------------------*/
#define NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY         /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 82L)

/*- LO control attributes ----------------------------------------------*/
#define NIRFSA_ATTR_NIRFSG_SESSION                         /* ViSession           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 73L)
#define NIRFSA_ATTR_LO_FREQUENCY                           /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 68L)
#define NIRFSA_ATTR_LO_INJECTION_SIDE                      /* ViInt32,            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 69L)
#define NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH           /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 67L)
#define NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS               /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 87L)
#define NIRFSA_ATTR_FREQUENCY_SETTLING                     /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 88L)
#define NIRFSA_ATTR_LO_EXPORT_ENABLED                      /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 134L)
#define NIRFSA_ATTR_LO2_EXPORT_ENABLED                     /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 235L)
#define NIRFSA_ATTR_LO_YIG_MAIN_COIL_DRIVE                 /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 135L)
#define NIRFSA_ATTR_LO_SOURCE                              /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 162L)
#define NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED               /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 298L)
#define NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG      /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 299L)

/*- Calibration ---------------------------------------------------------*/
#define NIRFSA_ATTR_CAL_RF_PATH_SELECTION                  /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 83L)
#define NIRFSA_ATTR_CAL_IF_FILTER_SELECTION                /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 112L)
#define NIRFSA_ATTR_CAL_LO_PATH_SELECTION                  /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 113L)
#define NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SELECTION     /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 141L)
#define NIRFSA_ATTR_CAL_LO1_ATTENUATION                    /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 114L)
#define NIRFSA_ATTR_CAL_LO2_ATTENUATION                    /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 115L)
#define NIRFSA_ATTR_CAL_LO3_ATTENUATION                    /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 116L)
#define NIRFSA_ATTR_CAL_IF_ATTENUATION_INDEX               /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 109L)
#define NIRFSA_ATTR_CAL_RF_ELECTRONIC_ATTENUATION_INDEX    /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 110L)
#define NIRFSA_ATTR_CAL_RF_MECHANICAL_ATTENUATION_INDEX    /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 111L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_THROUGH_FILTER  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 146L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_300_KHZ_FILTER  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 147L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_5_MHZ_FILTER    /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 148L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_100_MHZ_FILTER  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 223L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_320_MHZ_FILTER  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 224L)
#define NIRFSA_ATTR_CALIBRATION_CORRECTION_765_MHZ_FILTER  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 225L)
#define NIRFSA_ATTR_CAL_DIGITIZER_ID                       /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 226L)
#define NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION /* ViInt32  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 215L)
#define NIRFSA_ATTR_RF_HIGH_PASS_FILTERING                 /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 220L)
#define NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SIZE          /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 216L)

/*- Device Attributes ---------------------------------------------------*/
#define NIRFSA_ATTR_SERIAL_NUMBER                          /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 53L)
#define NIRFSA_ATTR_MODULE_REVISION                        /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 91L)
#define NIRFSA_ATTR_MODULE_POWER_CONSUMPTION               /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 255L)
#define NIRFSA_ATTR_SIGNAL_BANDWIDTH                       /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 267L)
#define NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH         /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 125L)
#define NIRFSA_ATTR_PRESELECTOR_PRESENT                    /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 136L)
#define NIRFSA_ATTR_RF_PREAMP_PRESENT                      /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 137L)
#define NIRFSA_ATTR_MAX_DEVICE_INSTANTANEOUS_BANDWIDTH     /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 236L)
#define NIRFSA_ATTR_MAX_IQ_RATE                            /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 237L)

/*- List mode attributes ------------------------------------------------*/
#define NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST              /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 92L)
#define NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP         /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 93L)
#define NIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE /* ViString*/ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 95L)
#define NIRFSA_ATTR_CONFIGURATION_LIST_STEP_IN_PROGRESS    /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 126L)
#define NIRFSA_ATTR_DDC_REF_TRIGGER_OVERRIDE               /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 164L)
#define NIRFSA_ATTR_MINIMUM_RECONFIG_TIME                  /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 165L)
#define NIRFSA_ATTR_CONTIGUOUS_MULTIRECORD                 /* ViInt32             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 172L)
#define NIRFSA_ATTR_TIMER_START_SOURCE                     /* ViString            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 173L)
#define NIRFSA_ATTR_START_TRIGGER_DELAY                    /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 175L)


/* Timer Event configuration attributes */
#define NIRFSA_ATTR_TIMER_EVENT_INTERVAL                   /* ViReal64            */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 96L)

/*- P2P Attributes ---------------------------------------------------*/
#define NIRFSA_ATTR_P2P_ENABLED                            /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 97L)
#define NIRFSA_ATTR_P2P_FIFO_ENDPOINT_COUNT                /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 98L)
#define NIRFSA_ATTR_P2P_SAMPLES_TRANSFERRED                /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 99L)
#define NIRFSA_ATTR_P2P_SAMPLES_AVAILABLE_IN_ENDPOINT      /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 100L)
#define NIRFSA_ATTR_P2P_MOST_SAMPLES_AVAILABLE_IN_ENDPOINT /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 101L)
#define NIRFSA_ATTR_P2P_ENDPOINT_SIZE                      /* ViInt64             */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 102L)
#define NIRFSA_ATTR_P2P_ENDPOINT_OVERFLOW                  /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 103L)
#define NIRFSA_ATTR_P2P_ONBOARD_MEMORY_ENABLED             /* ViBoolean           */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 107L)

/*- Cal Tone Controls ---------------------------------------*/
#define NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_MODE         /* ViInt32   */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 139L)
#define NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_FREQUENCY    /* ViReal64  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 140L)
#define NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE        /* ViInt32   */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 208L)
#define NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_FREQUENCY   /* ViReal64  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 209L)
#define NIRFSA_ATTR_CAL_TONE_STEP_ATTENUATION           /* ViReal64  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 168L)
#define NIRFSA_ATTR_CAL_TONE_POWER_REFERRED_TO_RF_IN    /* ViReal64  */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 174L)

/*- Misc ----------------------------------------------------*/
#define NIRFSA_ATTR_NOISE_SOURCE_POWER_ENABLED                 /*ViInt32      */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 222L)

/*- Input Port ---------------------------------------------------------------*/
#define NIRFSA_ATTR_INPUT_PORT                                 /* ViInt32     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 180L)

/*- LO control attributes ----------------------------------------------------*/
#define NIRFSA_ATTR_LO_IN_POWER                                /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 186L)
#define NIRFSA_ATTR_LO_OUT_POWER                               /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 246L)
#define NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED             /* ViInt32     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 187L)
#define NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE                     /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 188L)
#define NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE                 /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 312L)

/*- IQ In Port attributes ----------------------------------------------------*/
#define NIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCY               /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 181L)
#define NIRFSA_ATTR_IQ_IN_PORT_TERMINAL_CONFIGURATION          /* ViInt32     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 182L)
#define NIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGE                  /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 183L)
#define NIRFSA_ATTR_IQ_IN_PORT_TEMPERATURE                     /* ViReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 204L)
#define NIRFSA_ATTR_COMMON_MODE                                /* VIReal64    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 269L)

/*- Trigger Synchronization attributes ---------------------------------------*/
#define NIRFSA_ATTR_SYNC_START_TRIGGER_MASTER                  /*ViBoolean    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 176L)
#define NIRFSA_ATTR_SYNC_START_TRIGGER_DIST_LINE               /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 177L)
#define NIRFSA_ATTR_SYNC_REF_TRIGGER_MASTER                    /*ViBoolean    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 178L)
#define NIRFSA_ATTR_SYNC_REF_TRIGGER_DIST_LINE                 /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 179L)
#define NIRFSA_ATTR_SYNC_REF_TRIGGER_DELAY_ENABLED             /*ViInt32      */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 189L)
#define NIRFSA_ATTR_SYNC_ADVANCE_TRIGGER_MASTER                /*ViBoolean    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 184L)
#define NIRFSA_ATTR_SYNC_ADVANCE_TRIGGER_DIST_LINE             /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 185L)
#define NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_MASTER                   /*ViBoolean    */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 217L)
#define NIRFSA_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE                /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 218L)

/*- Trigger attributes -------------------------------------------------------*/
#define NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE          /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 192L)
#define NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE           /*ViInt32      */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 193L)
#define NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL           /*ViReal64     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 194L)
#define NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_HYSTERESIS      /*ViReal64     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 195L)

/*- Signal Path Attributes ---------------------------------------------------*/
#define NIRFSA_ATTR_DECIMATION_DELAY                           /*ViReal64     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 191L)
#define NIRFSA_ATTR_ABSOLUTE_DELAY                             /*ViReal64     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 266L)

/*- RF Downconverter Attributes ---------------------------------------------------*/
#define NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE       /*ViInt32      */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 305L)
#define NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET            /*ViReal64     */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 203L)

/*- FPGA Extensions Attributes -----------------------------------------------*/
#define NIRFSA_ATTR_FPGA_BITFILE_PATH                          /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 221L)
#define NIRFSA_ATTR_FPGA_TARGET_NAME                           /*ViString     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 233L)

/*- Spur Reduction Attributes ---------------------------------------------------------*/
#define NIRFSA_ATTR_SUBSPAN_OVERLAP                            /*ViReal64     */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 234L)

/*- Host DMA Buffer Attributes -----------------------------------------------*/
#define NIRFSA_ATTR_HOST_DMA_BUFFER_SIZE                       /*ViInt64      */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 285L)

/*- De-embedding Attributes -------------------------------------------------*/
#define NIRFSA_ATTR_DEEMBEDDING_TYPE                          /*ViInt32      */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 307L)
#define NIRFSA_ATTR_DEEMBEDDING_SELECTED_TABLE                /*ViString     */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 308L)
#define NIRFSA_ATTR_DEEMBEDDING_COMPENSATION_GAIN             /*ViReal64     */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 325L)

#define NIRFSA_ATTR_SELECTED_PATH                             /* ViString */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 331L)
#define NIRFSA_ATTR_AVAILABLE_PATHS                           /* ViString */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 332L)

#define NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS            /*ViInt32*/          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 337L)

/****************************************************************************
 *------ Device-Specific Attribute Value Defines (5644R/5645R/5646R) -------*
 ****************************************************************************/

/*- NIRFSA_ATTR_INPUT_PORT Values -*/
#define NIRFSA_VAL_RF_IN                                2000
#define NIRFSA_VAL_IQ_IN                                2001
#define NIRFSA_VAL_CAL_IN                               2002
#define NIRFSA_VAL_I_ONLY                               2003

/*- NIRFSA_ATTR_IQ_IN_PORT_TERMINAL_CONFIGURATION Values -*/
#define NIRFSA_VAL_DIFFERENTIAL                         2100
#define NIRFSA_VAL_SINGLE_ENDED                         2101

/*- Additional values for Trigger Type attributes -*/
#define NIRFSA_VAL_IQ_ANALOG_EDGE                       605

/*- Trigger Synchronization attribute values -*/
#define NIRFSA_VAL_SYNC_START_TRIGGER_STR               "Sync_Start"
#define NIRFSA_VAL_SYNC_REF_TRIGGER_STR                 "Sync_Ref"
#define NIRFSA_VAL_SYNC_ADVANCE_TRIGGER_STR             "Sync_Advance"


/****************************************************************************
 *------------------------ Attribute Value Defines -------------------------*
 ****************************************************************************/

/*- NIRFSA_ATTR_ACQUISITION_TYPE Values -*/
#define NIRFSA_VAL_IQ                                   100
#define NIRFSA_VAL_SPECTRUM                             101

/*- NIRFSA_ATTR_POWER_SPECTRUM_UNITS Values -*/
#define NIRFSA_VAL_DBM                                  200
#define NIRFSA_VAL_VOLTS_SQUARED                        201
#define NIRFSA_VAL_DBMV                                 202
#define NIRFSA_VAL_DBUV                                 203
#define NIRFSA_VAL_VOLTS                                204
#define NIRFSA_VAL_WATTS                                205

/*- NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE Values -*/
#define NIRFSA_VAL_RBW_3DB                              300
#define NIRFSA_VAL_RBW_6DB                              301
#define NIRFSA_VAL_RBW_BIN_WIDTH                        302
#define NIRFSA_VAL_RBW_ENBW                             303

/*- NIRFSA_ATTR_AVERAGING_MODE Values -*/
#define NIRFSA_VAL_NO_AVERAGING                         400
#define NIRFSA_VAL_RMS_AVERAGING                        401
#define NIRFSA_VAL_VECTOR_AVERAGING                     402
#define NIRFSA_VAL_PEAK_HOLD_AVERAGING                  403
#define NIRFSA_VAL_MIN_HOLD_AVERAGING                   404
#define NIRFSA_VAL_SCALAR_AVERAGING                     405
#define NIRFSA_VAL_LOG_AVERAGING                        406

/*- NIRFSA_ATTR_FFT_WINDOW_TYPE Values -*/
#define NIRFSA_VAL_UNIFORM                              500
#define NIRFSA_VAL_HANNING                              501
#define NIRFSA_VAL_HAMMING                              502
#define NIRFSA_VAL_BLACKMAN_HARRIS                      503
#define NIRFSA_VAL_EXACT_BLACKMAN                       504
#define NIRFSA_VAL_BLACKMAN                             505
#define NIRFSA_VAL_FLAT_TOP                             506
#define NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS               507
#define NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS               508
#define NIRFSA_VAL_LOW_SIDE_LOBE                        509
#define NIRFSA_VAL_GAUSSIAN                             510
#define NIRFSA_VAL_KAISER_BESSEL                        511

/*- Values For Trigger Type Attributes -*/
#define NIRFSA_VAL_NONE                                 600
#define NIRFSA_VAL_DIGITAL_EDGE                         601
#define NIRFSA_VAL_DIGITAL_LEVEL                        602
#define NIRFSA_VAL_IQ_POWER_EDGE                        603
#define NIRFSA_VAL_SOFTWARE_EDGE                        604

/*- NIRFSA_ATTR_FETCH_RELATIVE_TO Values -*/
#define NIRFSA_VAL_MOST_RECENT_SAMPLE                   700
#define NIRFSA_VAL_FIRST_SAMPLE                         701
#define NIRFSA_VAL_REF_TRIGGER                          702
#define NIRFSA_VAL_FIRST_PRETRIGGER_SAMPLE              703
#define NIRFSA_VAL_CURRENT_READ_POSITION                704

/*- NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH Values -*/
#define NIRFSA_VAL_NARROW                               800
#define NIRFSA_VAL_MEDIUM                               801
#define NIRFSA_VAL_WIDE                                 802

/*- Values For Digital Edge Attributes -*/
#define NIRFSA_VAL_RISING_EDGE                          900
#define NIRFSA_VAL_FALLING_EDGE                         901

/*- Values For Slope Attributes -*/
#define NIRFSA_VAL_RISING_SLOPE                        1000
#define NIRFSA_VAL_FALLING_SLOPE                       1001

/*- Values For Send Software Edge Trigger -*/
#define NIRFSA_VAL_START_TRIGGER                       1100
/* #define NIRFSA_VAL_REF_TRIGGER                       702  (Defined Above) */
#define NIRFSA_VAL_ADVANCE_TRIGGER                     1102
#define NIRFSA_VAL_ARM_REF_TRIGGER                     1103

/*- Values for Export Signals -*/
#define NIRFSA_VAL_READY_FOR_START_EVENT               1200
#define NIRFSA_VAL_READY_FOR_REF_EVENT                 1201
#define NIRFSA_VAL_READY_FOR_ADVANCE_EVENT             1202
#define NIRFSA_VAL_END_OF_RECORD_EVENT                 1203
#define NIRFSA_VAL_DONE_EVENT                          1204
#define NIRFSA_VAL_REF_CLOCK                           1205
#define NIRFSA_VAL_USER                                1206

/*- Values for LO Injection attribute-*/
#define NIRFSA_VAL_LO_INJECTION_HIGH_SIDE              1300
#define NIRFSA_VAL_LO_INJECTION_LOW_SIDE               1301

/*- Values for NIRFSA_ATTR_REF_CLOCK_SOURCE and NIRFSA_ATTR_PXI_CHASSIS_CLK10_SOURCE -*/
#define NIRFSA_VAL_NONE_STR                            "None"
#define NIRFSA_VAL_ONBOARD_CLOCK_STR                   "OnboardClock"
#define NIRFSA_VAL_REF_IN_STR                          "RefIn"
#define NIRFSA_VAL_PXI_CLK_STR                         "PXI_Clk"
#define NIRFSA_VAL_REF_IN_2_STR                        "RefIn2"
#define NIRFSA_VAL_PXI_CLK_MASTER_STR                  "PXI_ClkMaster"

/*- Values for NIRFSA_ATTR_LO_SOURCE -*/
#define NIRFSA_VAL_LO_IN_STR                           "LO_In"
#define NIRFSA_VAL_ONBOARD_STR                         "Onboard"
#define NIRFSA_VAL_LO_SOURCE_SECONDARY_STR             "Secondary"
#define NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED_STR          "SG_SA_Shared"

/*- Values for NIRFSA_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL -*/
/* #define NIRFSA_VAL_NONE_STR                            "None" (Defined Above) */
#define NIRFSA_VAL_CLK_OUT_STR                         "ClkOut"
#define NIRFSA_VAL_REF_OUT_STR                         "RefOut"
#define NIRFSA_VAL_REF_OUT2_STR                        "RefOut2"
#define NIRFSA_VAL_IF_COND_REF_OUT_STR                 "IFCondRefOut"

/*- Values for NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE -*/
#define NIRFSA_VAL_CLK_IN_STR                          "ClkIn"
/* #define NIRFSA_VAL_ONBOARD_CLOCK_STR                "OnboardClock" (Defined Above) */
/* #define NIRFSA_VAL_PXI_STAR_STR                     "PXI_STAR"     (Defined Below) */
#define NIRFSA_VAL_LO_REF_CLK_STR                      "LORefClk"
#define NIRFSA_VAL_DOWNCONVERTER_LO2_OUT_STR           "DownconverterLO2Out"

/*- Values for digital source and export terminal attributes:
    NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE
    NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE
    NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE
    NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE
    NIRFSA_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL
    NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL
-*/

#define NIRFSA_VAL_DO_NOT_EXPORT_STR                   ""
#define NIRFSA_VAL_PFI0_STR                            "PFI0"
#define NIRFSA_VAL_PFI1_STR                            "PFI1"
#define NIRFSA_VAL_PXI_TRIG0_STR                       "PXI_Trig0"
#define NIRFSA_VAL_PXI_TRIG1_STR                       "PXI_Trig1"
#define NIRFSA_VAL_PXI_TRIG2_STR                       "PXI_Trig2"
#define NIRFSA_VAL_PXI_TRIG3_STR                       "PXI_Trig3"
#define NIRFSA_VAL_PXI_TRIG4_STR                       "PXI_Trig4"
#define NIRFSA_VAL_PXI_TRIG5_STR                       "PXI_Trig5"
#define NIRFSA_VAL_PXI_TRIG6_STR                       "PXI_Trig6"
#define NIRFSA_VAL_PXI_TRIG7_STR                       "PXI_Trig7"
#define NIRFSA_VAL_PXI_STAR_STR                        "PXI_STAR"
#define NIRFSA_VAL_PXIE_DSTARB_STR                     "PXIe_DStarB"
#define NIRFSA_VAL_PXIE_DSTARC_STR                     "PXIe_DStarC"
#define NIRFSA_VAL_RTSI0_STR                           NIRFSA_VAL_PXI_TRIG0_STR
#define NIRFSA_VAL_RTSI1_STR                           NIRFSA_VAL_PXI_TRIG1_STR
#define NIRFSA_VAL_RTSI2_STR                           NIRFSA_VAL_PXI_TRIG2_STR
#define NIRFSA_VAL_RTSI3_STR                           NIRFSA_VAL_PXI_TRIG3_STR
#define NIRFSA_VAL_RTSI4_STR                           NIRFSA_VAL_PXI_TRIG4_STR
#define NIRFSA_VAL_RTSI5_STR                           NIRFSA_VAL_PXI_TRIG5_STR
#define NIRFSA_VAL_RTSI6_STR                           NIRFSA_VAL_PXI_TRIG6_STR
#define NIRFSA_VAL_RTSI7_STR                           NIRFSA_VAL_PXI_TRIG7_STR
#define NIRFSA_VAL_TIMER_EVENT_STR                     "TimerEvent"
#define NIRFSA_VAL_END_OF_RECORD_EVENT_STR             "EndOfRecordEvent"
#define NIRFSA_VAL_START_TRIGGER_STR                   "StartTrigger"
#define NIRFSA_VAL_REFERENCE_TRIGGER_STR               "ReferenceTrigger"
#define NIRFSA_VAL_USER_SOURCE0_STR                    "UserSource0"
#define NIRFSA_VAL_USER_SOURCE1_STR                    "UserSource1"
#define NIRFSA_VAL_USER_SOURCE2_STR                    "UserSource2"
#define NIRFSA_VAL_USER_SOURCE3_STR                    "UserSource3"
#define NIRFSA_VAL_USER_SOURCE4_STR                    "UserSource4"
#define NIRFSA_VAL_USER_SOURCE5_STR                    "UserSource5"
#define NIRFSA_VAL_USER_SOURCE6_STR                    "UserSource6"
#define NIRFSA_VAL_USER_SOURCE7_STR                    "UserSource7"
#define NIRFSA_VAL_PULSE_IN_STR                        "PulseIn"
#define NIRFSA_VAL_DIO0_STR                            "DIO/PFI0"
#define NIRFSA_VAL_DIO1_STR                            "DIO/PFI1"
#define NIRFSA_VAL_DIO2_STR                            "DIO/PFI2"
#define NIRFSA_VAL_DIO3_STR                            "DIO/PFI3"
#define NIRFSA_VAL_DIO4_STR                            "DIO/PFI4"
#define NIRFSA_VAL_DIO5_STR                            "DIO/PFI5"
#define NIRFSA_VAL_DIO6_STR                            "DIO/PFI6"
#define NIRFSA_VAL_DIO7_STR                            "DIO/PFI7"

/*- Values for NIRFSA_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE -*/
/* #define NIRFSA_VAL_TIMER_EVENT_STR                     "TimerEvent" (Defined Above) */
/* #define NIRFSA_VAL_END_OR_RECORD_EVENT_STR             "EndOfRecordEvent" (Defined Above) */

/*- Values for NIRFSA_ATTR_TIMER_START_SOURCE -*/
/* #define NIRFSA_VAL_START_TRIGGER_STR                   "StartTrigger" (Defined Above) */
/* #define NIRFSA_VAL_REFERENCE_TRIGGER_STR               "ReferenceTrigger" (Defined Above) */

/*- Values for IF Filter attribute -*/
#define NIRFSA_VAL_187_5_MHZ_WIDE                                 1400
#define NIRFSA_VAL_187_5_MHZ_NARROW                               1401
#define NIRFSA_VAL_53_MHZ                                         1402
#define NIRFSA_VAL_BYPASS                                         1403

/////////////////////////////////////////////////////////////////////////
// Values for External Calibration
/*- Defined values for action in niRFSA_CloseExtCal()  ---------------*/
#define NIRFSA_VAL_EXT_CAL_ABORT                                  1500
#define NIRFSA_VAL_EXT_CAL_COMMIT                                 1501

/*- Defined values for calibration step in niRFSA_InitializeCalibrationStep() ---------------*/
#define NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_CALIBRATION             1600
#define NIRFSA_VAL_EXT_CAL_IF_RESPONSE_CALIBRATION                1601
#define NIRFSA_VAL_EXT_CAL_REF_LEVEL_CALIBRATION                  1602
#define NIRFSA_VAL_EXT_CAL_LO_EXPORT_CALIBRATION                  1603
#define NIRFSA_VAL_EXT_CAL_GAIN_REFERENCE_CALIBRATION             1604

/*- Defined values for NIRFSA_ATTR_CAL_RF_PATH_SELECTION  ---------------*/
#define NIRFSA_VAL_EXT_CAL_RF_BAND_1                              1700
#define NIRFSA_VAL_EXT_CAL_RF_BAND_2                              1701
#define NIRFSA_VAL_EXT_CAL_RF_BAND_3                              1702
#define NIRFSA_VAL_EXT_CAL_RF_BAND_4                              1703

/*- Defined values for refLevelCalDataType in
 * niRFSA_CalAdjustRefLevelCalibration()  ---------------*/
#define NIRFSA_VAL_EXT_CAL_DEFAULT                                1800
#define NIRFSA_VAL_EXT_CAL_MECHANICAL_ATTENUATOR_DISABLED         1801

/*- Values for NIRFSA_ATTR_MECHANICAL_ATTENUATOR_ENABLED, NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED,
 *  NIRFSA_ATTR_REF_TRIGGER_OSP_DELAY_ENABLED, NIRFSA_ATTR_INPUT_ISOLATION_ENABLED,
 *  NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG and NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED.
 *  NIRFSA_VAL_ENABLED is also for NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE. -*/
#define NIRFSA_VAL_DISABLED                                       1900
#define NIRFSA_VAL_ENABLED                                        1901

/*- Value for NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED  -*/
#define NIRFSA_VAL_UNSPECIFIED                                    1902

/*- Additional values for NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE */
#define NIRFSA_VAL_AUTOMATIC                                      1903
#define NIRFSA_VAL_USER_DEFINED                                   1904

/*- Values for Frequency Settling units attribute */
#define NIRFSA_VAL_FSU_PPM                                        2000
#define NIRFSA_VAL_FSU_SECONDS_AFTER_LOCK                         2001
#define NIRFSA_VAL_FSU_SECONDS_AFTER_IO                           2002

/*- Values for NIRFSA_ATTR_CAL_IF_FILTER_SELECTION attribute-*/
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_1                       2100 // 5Mhz Bandpass IF Filter
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_2                       2101 // 300Khz BandPass IF Filter
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_3                       2102 // Bypass Path (no IF Filter)
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4                       2103
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_5                       2104
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_6                       2105
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_7                       2106
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_8                       2107
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_9                       2108
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_10                      2109
#define NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_11                      2110

/*-Values For niRFSA_CalAdjustLOExportCalibration:LONumber-*/
#define NIRFSA_VAL_EXT_CAL_LO1                                    2200 // Variable LO
#define NIRFSA_VAL_EXT_CAL_LO2                                    2201 // 4Ghz LO
#define NIRFSA_VAL_EXT_CAL_LO3                                    2202 // 800Mhz LO

/*- Values for NIRFSA_ATTR_CAL_LO_PATH_SELECTION attribute-*/
#define NIRFSA_VAL_EXT_CAL_LO_PATH_1                              2300 // LO x1
#define NIRFSA_VAL_EXT_CAL_LO_PATH_2                              2301 // LO Doubler Enabled (5605)/LO x2 LF 6.4GHz LPF (5606)
#define NIRFSA_VAL_EXT_CAL_LO_PATH_3                              2302 // LO x2 HF 9.7GHz LPF (5606)
#define NIRFSA_VAL_EXT_CAL_LO_PATH_4                              2303 // LO x4 LF 6.4GHz LPF (5606)
#define NIRFSA_VAL_EXT_CAL_LO_PATH_5                              2304 // LO x4 HF 9.7GHz LPF (5606)

/*- Values for NIRFSA_ATTR_LO_YIG_MAIN_COIL_DRIVE attribute-*/
#define NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_NORMAL                  2400
#define NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_FAST                    2401

/*- Values for NIRFSA_ATTR_RF_PREAMP_ENABLED attribute-*/
#define NIRFSA_VAL_RF_PREAMP_DISABLED                             2500 // Preamp Disabled
#define NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH          2501 // The RF preamp will be automatically enabled when it is in the signal path and will be automatically disabled when it is out of the signal path
#define NIRFSA_VAL_RF_PREAMP_ENABLED                              2502 // Preamp Enabled
#define NIRFSA_VAL_RF_PREAMP_AUTOMATIC                            2503 // Automatic

/*- Values for NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED attribute-*/
#define NIRFSA_VAL_PRESELECTOR_DISABLED                           2600 // Preselector Disabled
#define NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH        2601 // The preselector will be automatically enabled when it is in the signal path and will be automatically disabled when it is out of the signal path.
#define NIRFSA_VAL_PRESELECTOR_ENABLED                            2602 // Preselector Enabled

/*- Values for SELF CAL steps -*/
#define NIRFSA_VAL_SELF_CAL_OMIT_NONE                             0x0000000000000000
#define NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT                 0x0000000000000001
#define NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE                        0x0000000000000002
#define NIRFSA_VAL_SELF_CAL_IF_FLATNESS                           0x0000000000000004
#define NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL                    0x0000000000000008
#define NIRFSA_VAL_SELF_CAL_LO_SELF_CAL                           0x0000000000000010
#define NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY                    0x0000000000000020
#define NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER                     0x0000000000000040
#define NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION                     0x0000000000000080
#define NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT                 0x0000000000000100
#define NIRFSA_VAL_SELF_CAL_DC_OFFSET                             0x0000000000000200


/*- Values for Cal Tone Mode -*/
#define NIRFSA_VAL_CAL_TONE_DISABLED                              2700
#define NIRFSA_VAL_CAL_TONE_LOWBAND_RF                            2701
#define NIRFSA_VAL_CAL_TONE_HIGHBAND_RF                           2702
#define NIRFSA_VAL_CAL_TONE_HIGHBAND_IF                           2703
#define NIRFSA_VAL_CAL_TONE_LOWBAND_RF_WITHOUT_ALC                2704
#define NIRFSA_VAL_CAL_TONE_COMB_GENERATOR                        2705

/* Values for niRFSA_GetDeviceResponse response type */
#define NIRFSA_VAL_DOWNCONVERTER_IF_RESPONSE                      2800
#define NIRFSA_VAL_DOWNCONVERTER_RF_RESPONSE                      2801
#define NIRFSA_VAL_DOWNCONVERTER_COMBINED_RESPONSE                2802
#define NIRFSA_VAL_VSA_IF_RESPONSE                                2803
#define NIRFSA_VAL_VSA_COMBINED_RESPONSE                          2804

/*- Values for NIRFSA_ATTR_CAL_IF_ATTENUATION_TABLE_SELECTION attribute-*/
#define NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_STANDARD          2900
#define NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_ACPR              2901

/*- Values for NIRFSA_ATTR_CHANNEL_COUPLING attribute -*/
#define NIRFSA_VAL_AC                                             3001
#define NIRFSA_VAL_DC                                             3002

/*- Values for External Alignment ----------------------------------*/
/*- Values for External Alignment Steps -                           */
/*- This is an enumeration value. Future values will not be bitwise */
/*- ORed with this value.                                           */
#define NIRFSA_VAL_EXT_ALIGNMENT_PRESELECTOR                         1

/*- Defined values for action in niRFSA_CloseExternalAlignmentCal() -*/
#define NIRFSA_VAL_EXT_ALIGNMENT_ABORT                            3100
#define NIRFSA_VAL_EXT_ALIGNMENT_COMMIT                           3101

/*- Values for NIRFSA_ATTR_STEP_GAIN_ENABLED attribute -*/
#define NIRFSA_VAL_STEP_GAIN_DISABLED                             3200
#define NIRFSA_VAL_STEP_GAIN_ENABLED                              3201

/*- Values for NIRFSA_ATTR_RF_PRESELECTOR_FILTER attribute -*/
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_NONE                3300  // None
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_1                   3301  // 19-35 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_2                   3302  // 33-61 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_3                   3303  // 59-110 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_4                   3304  // 90-167 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_5                   3305  // 140-245 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_6                   3306  // 205-370 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_7                   3307  // 330-595 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_8                   3308  // 550-975 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_9                   3309  // 910-1600 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_10                  3310  // 1520-2040 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_11                  3311  // 1960-2540 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_12                  3312  // 2460-3040 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_13                  3313  // 2960-3840 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_14                  3314  // 3760-4640 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_15                  3315  // 4560-5840 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_16                  3316  // 5760-7040 MHz
#define NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_EXTERNAL_FILTER     3317  // External Filter

/*- Values for NIRFSA_ATTR_NOTCH_FILTER_ENABLED attribute -*/
#define NIRFSA_VAL_NOTCH_FILTER_DISABLED                          3400
#define NIRFSA_VAL_NOTCH_FILTER_ENABLED_WHEN_IN_SIGNAL_PATH       3401
#define NIRFSA_VAL_NOTCH_FILTER_ENABLED                           3402

/*- Values for NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED attribute -*/
#define NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED                    3600
#define NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED                   3601

/*- Values for NIRFSA_ATTR_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION attribute-*/
#define NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1  3700 //Through Path
#define NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2  3701 //Attenuator Only
#define NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_3  3702 //1350MHz HPF
#define NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_4  3703 //2200MHz HPF
#define NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_5  3704 //Preamp Path

/*- Values for S-parameters orientation passed to Create De-embedding S-parameter Table functions -*/
#define NIRFSA_VAL_PORT1_TOWARDS_DUT                              3800
#define NIRFSA_VAL_PORT2_TOWARDS_DUT                              3801

/*- Values for NIRFSA_ATTR_DEEMBEDDING_TYPE attribute -*/
#define NIRFSA_VAL_DEEMBEDDING_TYPE_NONE                          3900
#define NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR                        3901
#define NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR                        3902
#define NIRFSA_VAL_DEEMBEDDING_TYPE_AMPLITUDE_FLATNESS            3903

/*- Values for niRFSA_ConfigureDeembeddingTableInterpolationLinear -*/
#define NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY      4000
#define NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE     4001
#define NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE  4002

/*- Values for NIRFSA_ATTR_OVERFLOW_ERROR_REPORTING attribute -*/
#define NIRFSA_VAL_ERROR_REPORTING_WARNING                        1301
#define NIRFSA_VAL_ERROR_REPORTING_DISABLED                       1302

/*- Values for stepsToOmit in ResetWithOptions-*/
#define NIRFSA_VAL_RESET_WITH_OPTIONS_NONE                        0x0ULL //reset everything
#define NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES                      0x1ULL //do not reset routes
#define NIRFSA_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES          0x2ULL

/*- Values for NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS -*/
#define NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS       6200
#define NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS 6201

/*- Values for NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS -*/
#define NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE                0x0ULL
#define NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES  0x2ULL

/*- SMT Structures -----------------------------------------------*/
#if kRFSA_32BitPlatform
   #pragma pack(push, 1)
#elif kRFSA_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

#ifndef __SmtSpectrumInfo__
#define __SmtSpectrumInfo__
typedef struct {
   unsigned short spectrumType;
   unsigned short linearDB;
   unsigned short window;
   int windowSize;
   int FFTSize;
} SmtSpectrumInfo;
#endif

#if kRFSA_32BitPlatform
   #pragma pack(pop)
#elif kRFSA_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

/*- Init and Close Functions -----------------------------------------------*/
ViStatus _VI_FUNC niRFSA_init (
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean reset,
   ViSession* vi);

ViStatus _VI_FUNC niRFSA_InitWithOptions(
   ViRsrc resourceName,
   ViBoolean IDQuery,
   ViBoolean reset,
   ViConstString optionString,
   ViSession* newVi);

ViStatus _VI_FUNC niRFSA_close(
   ViSession vi);

/*- Peer-to-Peer utility -----------------------------------------------*/
ViStatus _VI_FUNC niRFSA_GetStreamEndpointHandle(
   ViSession vi,
   ViConstString streamEndpoint,
   ViUInt32* writerHandle);

/*- Calibration -----------------------------------------------*/
ViStatus _VI_FUNC niRFSA_InitExtCal(
   ViRsrc resourceName,
   ViConstString password,
   ViConstString optionString,
   ViSession* vi);

ViStatus _VI_FUNC niRFSA_InitializeCalibrationStep(
   ViSession vi,
   ViInt32 calibrationStep);

ViStatus _VI_FUNC niRFSA_CloseCalibrationStep(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_CloseExtCal(
   ViSession vi,
   ViInt32 action);

ViStatus _VI_FUNC niRFSA_SelfCalibrate(
   ViSession vi,
   ViInt64 stepsToOmit);

ViStatus _VI_FUNC niRFSA_IsSelfCalValid(
   ViSession vi,
   ViBoolean* selfCalValid,
   ViInt64* validSteps);

ViStatus _VI_FUNC niRFSA_InitializeExternalAlignment(
   ViRsrc resourceName,
   ViConstString optionString,
   ViSession* vi);

ViStatus _VI_FUNC niRFSA_CloseExternalAlignment(
   ViSession vi,
   ViInt32 action);

ViStatus _VI_FUNC niRFSA_InitializeExternalAlignmentStep(
   ViSession vi,
   ViInt64 externalAlignmentStep);

ViStatus _VI_FUNC niRFSA_CloseExternalAlignmentStep(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_SelfCalibrateRange(
   ViSession vi,
   ViInt64 stepsToOmit,
   ViReal64 minFrequency,
   ViReal64 maxFrequency,
   ViReal64 minReferenceLevel,
   ViReal64 maxReferenceLevel);

/* Calibration Utility Functions */
ViStatus _VI_FUNC niRFSA_GetExtCalLastDateAndTime(
   ViSession vi,
   ViInt32* year,
   ViInt32* month,
   ViInt32* day,
   ViInt32* hour,
   ViInt32* minute);

ViStatus _VI_FUNC niRFSA_GetExtCalLastTemp(
   ViSession vi,
   ViReal64* temperature);

ViStatus _VI_FUNC niRFSA_GetExtCalRecommendedInterval(
   ViSession vi,
   ViInt32* months);

ViStatus _VI_FUNC niRFSA_ChangeExtCalPassword(
   ViSession vi,
   ViConstString oldPassword,
   ViConstString newPassword);

ViStatus _VI_FUNC niRFSA_SetCalUserDefinedInfo(
   ViSession vi,
   ViConstString info);

ViStatus _VI_FUNC niRFSA_GetCalUserDefinedInfo(
   ViSession vi,
   ViChar info[]);

ViStatus _VI_FUNC niRFSA_GetCalUserDefinedInfoMaxSize(
   ViSession vi,
   ViInt32* infoSize);

ViStatus _VI_FUNC niRFSA_ExtCalStoreBaselineForSelfCalibration(
   ViSession vi,
   ViString password,
   ViInt64 selfCalibrationStep);

ViStatus _VI_FUNC niRFSA_GetSelfCalLastDateAndTime(
   ViSession vi,
   ViInt64 selfCalibrationStep,
   ViInt32* year,
   ViInt32* month,
   ViInt32* day,
   ViInt32* hour,
   ViInt32* minute);

ViStatus _VI_FUNC niRFSA_GetSelfCalLastTemp(
   ViSession vi,
   ViInt64 selfCalibrationStep,
   ViReal64* temp);

ViStatus _VI_FUNC niRFSA_GetGainReferenceCalBaseline(
   ViSession vi,
   ViInt32  bufferSize,
   ViReal64 gainReferenceCalConstants[],
   ViInt32* numberOfGainReferenceCalConstants);

ViStatus _VI_FUNC niRFSA_ClearSelfCalibrateRange(
   ViSession vi);

/*- Calibration Adjust Functions-------------------------------------*/
ViStatus _VI_FUNC niRFSA_CalAdjustIFAttenuationCalibration(
   ViSession vi,
   ViConstString channelList,
   ViInt32 IFFilter,
   ViInt32 numberOfAttenuators,
   ViReal64* attenuatorSettings,
   ViReal64 measurement);

ViStatus _VI_FUNC niRFSA_CalAdjustIFResponseCalibration(
   ViSession vi,
   ViConstString channelList,
   ViInt32  IFFilter,
   ViReal64 RFFrequency,
   ViReal64 bandWidth,
   ViInt32  numberOfMeasurements,
   ViReal64* measurements);

ViStatus _VI_FUNC niRFSA_CalAdjustRefLevelCalibration(
   ViSession vi,
   ViConstString channelList,
   ViInt32 referenceLevelDataType,
   ViInt32 rfBand,
   ViInt32 attenuatorTableNumber,
   ViReal64 frequency,
   ViReal64 measurement);

ViStatus _VI_FUNC niRFSA_CalAdjustLOExportCalibration(
   ViSession vi,
   ViConstString channelList,
   ViInt32   loNumber,
   ViInt32   numberOfFrequencyPoints,
   ViReal64* frequencyPoints,
   ViReal64* loAttenuation);

ViStatus _VI_FUNC niRFSA_CalAdjustDeviceGain(
   ViSession vi,
   ViConstString channelList,
   ViReal64 frequency,
   ViReal64 gain);

ViStatus _VI_FUNC niRFSA_CalSetTemperature(
   ViSession vi,
   ViConstString channelList,
   ViReal64 temperature);

ViStatus _VI_FUNC niRFSA_ExternalAlignmentAdjustPreselector(
   ViSession vi,
   ViInt32 numberOfCoefficients,
   ViReal64 coefficients[]);

ViStatus _VI_FUNC niRFSA_CalAdjustCalTonePower(
   ViSession vi,
   ViConstString channelList,
   ViReal64 measurement);

/*- Required VXIplug&play Functions ----------------------------------------*/
ViStatus _VI_FUNC niRFSA_reset(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ResetDevice(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ResetWithOptions(
   ViSession vi,
   ViUInt64 stepsToOmit);

ViStatus _VI_FUNC niRFSA_self_test(
   ViSession vi,
   ViInt16 *testResult,/*Output*/
   ViChar testMessage[]);

ViStatus _VI_FUNC niRFSA_error_query(
   ViSession vi,
   ViInt32 *errorCode,
   ViChar errorMessage[]);

ViStatus _VI_FUNC niRFSA_error_message(
   ViSession vi,
   ViStatus statusCode,
   ViChar errorMessage[]);

ViStatus _VI_FUNC niRFSA_revision_query(
   ViSession vi,
   ViChar driverRev[],
   ViChar instrRev[]);

ViStatus _VI_FUNC niRFSA_Disable(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ResetWithDefaults(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_InvalidateAllAttributes(
   ViSession vi);

/* Save Load Functions --------------------------------------*/
ViStatus _VI_FUNC niRFSA_SaveConfigurationsToFile
(
   ViSession vi,
   ViConstString channelName,
   ViConstString filePath
);

ViStatus _VI_FUNC niRFSA_LoadConfigurationsFromFile
(
   ViSession vi,
   ViConstString channelName,
   ViConstString filePath
);

/*- Error Functions --------------------------------------------------------*/
ViStatus _VI_FUNC niRFSA_GetError(
   ViSession vi,
   ViStatus *errorCode,
   ViInt32 errorDescriptionBufferSize,
   ViChar errorDescription[]);

ViStatus _VI_FUNC niRFSA_ClearError(
   ViSession vi);

/*- Required IVI Functions ---------------------------------------------*/
ViStatus _VI_FUNC niRFSA_LockSession(
   ViSession vi,
   ViBoolean *callerHasLock);

ViStatus _VI_FUNC niRFSA_UnlockSession(
   ViSession vi,
   ViBoolean *callerHasLock);

/*- Acquisition Type Configuration -------------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureAcquisitionType(
   ViSession vi,
   ViInt32 acquisitionType);

/*- Reference Level Configuration --------------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureReferenceLevel(
   ViSession vi,
   ViConstString channelList,
   ViReal64 referenceLevel);

/*- IQ Acquisition Configuration ---------------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureIQCarrierFrequency(
   ViSession vi,
   ViConstString channelList,
   ViReal64 carrierFrequency);

ViStatus _VI_FUNC niRFSA_ConfigureIQRate(
   ViSession vi,
   ViConstString channelList,
   ViReal64 iqRate);

ViStatus _VI_FUNC niRFSA_ConfigureNumberOfSamples(
   ViSession vi,
   ViConstString channelList,
   ViBoolean numberOfSamplesIsFinite,
   ViInt64 samplesPerRecord);

ViStatus _VI_FUNC niRFSA_ConfigureNumberOfRecords(
   ViSession vi,
   ViConstString channelList,
   ViBoolean numberOfRecordsIsFinite,
   ViInt64 numberOfRecords);

/*- Spectrum Acquisition Configuration ---------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyCenterSpan(
   ViSession vi,
   ViConstString channelList,
   ViReal64 centerFrequency,
   ViReal64 span);

ViStatus _VI_FUNC niRFSA_ConfigureSpectrumFrequencyStartStop(
   ViSession vi,
   ViConstString channelList,
   ViReal64 startFrequency,
   ViReal64 stopFrequency);

ViStatus _VI_FUNC niRFSA_ConfigureResolutionBandwidth(
   ViSession vi,
   ViConstString channelList,
   ViReal64 resolutionBandwidth);

/*- Clock Configuration ------------------------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureRefClock(
   ViSession vi,
   ViConstString clockSource,
   ViReal64 refClockRate);

ViStatus _VI_FUNC niRFSA_ConfigurePXIChassisClk10(
   ViSession vi,
   ViConstString pxiClk10Source);

/*- Trigger Configuration ----------------------------------------------*/
ViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeStartTrigger(
   ViSession vi,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_DisableStartTrigger(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeRefTrigger(
   ViSession vi,
   ViConstString source,
   ViInt32 edge,
   ViInt64 pretriggerSamples);

ViStatus _VI_FUNC niRFSA_ConfigureIQPowerEdgeRefTrigger(
   ViSession vi,
   ViConstString source,
   ViReal64 level,
   ViInt32 slope,
   ViInt64 pretriggerSamples);

ViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeRefTrigger(
   ViSession vi,
   ViInt64 pretriggerSamples);

ViStatus _VI_FUNC niRFSA_DisableRefTrigger(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ConfigureDigitalEdgeAdvanceTrigger(
   ViSession vi,
   ViConstString source,
   ViInt32 edge);

ViStatus _VI_FUNC niRFSA_ConfigureSoftwareEdgeAdvanceTrigger(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_DisableAdvanceTrigger(
   ViSession vi);

/*- Reading / Fetching IQ Data ------------------------------------------*/
#if !defined(_NIComplexNumber)
#define _NIComplexNumber

#pragma pack(push, 8)
typedef struct NIComplexNumber_struct {
   ViReal64 real;
   ViReal64 imaginary;
} NIComplexNumber;
#pragma pack(pop)

#endif

#if !defined(_NIComplexNumberF32)
#define _NIComplexNumberF32

#if kRFSA_32BitPlatform
   #pragma pack(push, 1)
#elif kRFSA_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

typedef struct NIComplexNumberF32_struct {
   ViReal32 real;
   ViReal32 imaginary;
} NIComplexNumberF32;

#if kRFSA_32BitPlatform
   #pragma pack(pop)
#elif kRFSA_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

#endif


#if !defined(_niRFSA_wfmInfo)
#define _niRFSA_wfmInfo

#pragma pack(push,8)
typedef struct niRFSA_wfmInfo_struct
{
   ViReal64 absoluteInitialX;
   ViReal64 relativeInitialX;
   ViReal64 xIncrement;
   ViInt64 actualSamples;
   ViReal64 offset;
   ViReal64 gain;
   ViReal64 reserved1;
   ViReal64 reserved2;
} niRFSA_wfmInfo;
#pragma pack(pop)

#endif

#pragma pack(push,8)
typedef struct niRFSA_coefficientInfo_struct
{
   ViReal64 offset;
   ViReal64 gain;
   ViReal64 reserved1;
   ViReal64 reserved2;
} niRFSA_coefficientInfo;
#pragma pack(pop)

#if !defined(_NIComplexI16)
#define _NIComplexI16
typedef struct NIComplexI16_struct {
   ViInt16 real;
   ViInt16 imaginary;
} NIComplexI16;
#endif



ViStatus _VI_FUNC niRFSA_ReadIQSingleRecordComplexF64(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   NIComplexNumber* data,
   ViInt64 dataArraySize,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQSingleRecordComplexF64(
   ViSession vi,
   ViConstString channelList,
   ViInt64 recordNumber,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexNumber* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQSingleRecordComplexF32(
   ViSession vi,
   ViConstString channelList,
   ViInt64 recordNumber,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexNumberF32* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQMultiRecordComplexF64(
   ViSession vi,
   ViConstString channelList,
   ViInt64 startingRecord,
   ViInt64 numberOfRecords,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexNumber* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQMultiRecordComplexF32(
   ViSession vi,
   ViConstString channelList,
   ViInt64 startingRecord,
   ViInt64 numberOfRecords,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexNumberF32* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQSingleRecordComplexI16(
   ViSession vi,
   ViConstString channelList,
   ViInt64 recordNumber,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexI16* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_FetchIQMultiRecordComplexI16
(
   ViSession vi,
   ViConstString channelList,
   ViInt64 startingRecord,
   ViInt64 numberOfRecords,
   ViInt64 numberOfSamples,
   ViReal64 timeout,
   NIComplexI16* data,
   niRFSA_wfmInfo* wfmInfo);

ViStatus _VI_FUNC niRFSA_GetFetchBacklog(
   ViSession vi,
   ViConstString channelList,
   ViInt64 recordNumber,
   ViInt64* backlog);

ViStatus _VI_FUNC niRFSA_GetScalingCoefficients(
   ViSession vi,
   ViConstString channelList,
   ViInt32 arraySize,
   niRFSA_coefficientInfo coefficientInfo[],
   ViInt32* numberOfCoefficientSets);

ViStatus _VI_FUNC niRFSA_GetNormalizationCoefficients(
   ViSession vi,
   ViConstString channelList,
   ViInt32 arraySize,
   niRFSA_coefficientInfo coefficientInfo[],
   ViInt32* numberOfCoefficientSets);

/*- Reading Spectrum Data ----------------------------------------------*/
#if !defined(_niRFSA_spectrumInfo)
#define _niRFSA_spectrumInfo

#pragma pack(push,8)
typedef struct niRFSA_spectrumInfo_struct
{
   ViReal64 initialFrequency;
   ViReal64 frequencyIncrement;
   ViInt32 numberOfSpectralLines;
   ViReal64 reserved1;
   ViReal64 reserved2;
   ViReal64 reserved3;
   ViReal64 reserved4;
   ViReal64 reserved5;
} niRFSA_spectrumInfo;
#pragma pack(pop)

#endif

ViStatus _VI_FUNC niRFSA_ReadPowerSpectrumF64(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViReal64 powerSpectrumData[],
   ViInt32 dataArraySize,
   niRFSA_spectrumInfo* spectrumInfo);

ViStatus _VI_FUNC niRFSA_ReadPowerSpectrumF32(
   ViSession vi,
   ViConstString channelList,
   ViReal64 timeout,
   ViReal32 powerSpectrumData[],
   ViInt32 dataArraySize,
   niRFSA_spectrumInfo* spectrumInfo);

ViStatus _VI_FUNC niRFSA_GetNumberOfSpectralLines(
   ViSession vi,
   ViConstString channelList,
   ViInt32* numberOfSpectralLines);

/*- Control Functions --------------------------------------------------*/
ViStatus _VI_FUNC niRFSA_Initiate(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_Abort(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_Commit(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_CheckAcquisitionStatus(
   ViSession vi,
   ViBoolean* isDone);

/*- Utility Functions --------------------------------------------------*/
ViStatus _VI_FUNC niRFSA_PerformThermalCorrection(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ExportSignal(
   ViSession vi,
   ViInt32 signal,
   ViConstString signalIdentifier,
   ViConstString outputTerminal);

ViStatus _VI_FUNC niRFSA_GetTerminalName
(
   ViSession vi,
   ViInt32 signal,
   ViConstString signalIdentifier,
   ViInt32 bufferSize,
   ViChar terminalName[]);

ViStatus _VI_FUNC niRFSA_SendSoftwareEdgeTrigger(
   ViSession vi,
   ViInt32 trigger,
   ViConstString triggerIdentifier);

ViStatus _VI_FUNC niRFSA_GetSpectralInfoForSMT(
   ViSession vi,
   SmtSpectrumInfo* spectrumInfo);

ViStatus _VI_FUNC niRFSA_GetFrequencyResponse(
   ViSession vi,
   ViConstString channelList,
   ViInt32 bufferSize,
   ViReal64 frequencies[],
   ViReal64 magnitudeResponse[],
   ViReal64 phaseResponse[],
   ViInt32* numberOfFrequencies);

ViStatus _VI_FUNC niRFSA_GetDeviceResponse(
   ViSession vi,
   ViConstString channelList,
   ViInt32 responseType,
   ViInt32 bufferSize,
   ViReal64 frequencies[],
   ViReal64 magnitudeResponse[],
   ViReal64 phaseResponse[],
   ViInt32* numberOfFrequencies);

ViStatus _VI_FUNC niRFSA_GetRelayOperationsCount(
   ViSession vi,
   ViConstString channelList,
   ViInt32 operationsCount[],
   ViInt32* bufferSize);

ViStatus _VI_FUNC niRFSA_GetRelayName(
   ViSession vi,
   ViConstString channelList,
   ViInt32 index,
   ViChar name[],
   ViInt32* bufferSize);

ViStatus _VI_FUNC niRFSA_EnableSessionAccess
(
   ViSession vi,
   ViBoolean enable
);


/*-------------------------------- List Mode API ----------------------------------------*/
ViStatus _VI_FUNC niRFSA_CreateConfigurationList(
   ViSession vi,
   ViConstString listName,
   ViInt32 numberOfListAttributes,
   const ViAttr* listAttributeIDs,
   ViBoolean setAsActiveList);

ViStatus _VI_FUNC niRFSA_CreateConfigurationListStep(
   ViSession vi,
   ViBoolean setAsActiveStep);

ViStatus _VI_FUNC niRFSA_DeleteConfigurationList(
   ViSession vi,
   ViConstString listName);

/*- Attributes ---------------------------------------------------------*/
ViStatus _VI_FUNC niRFSA_SetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 value);

ViStatus _VI_FUNC niRFSA_SetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt64 value);

ViStatus _VI_FUNC niRFSA_SetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64 value);

ViStatus _VI_FUNC niRFSA_SetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViConstString value);

ViStatus _VI_FUNC niRFSA_SetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViBoolean value);

ViStatus _VI_FUNC niRFSA_SetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession value);

ViStatus _VI_FUNC niRFSA_GetAttributeViInt32(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 *value);

ViStatus _VI_FUNC niRFSA_GetAttributeViInt64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt64 *value);

ViStatus _VI_FUNC niRFSA_GetAttributeViReal64(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViReal64 *value) ;

ViStatus _VI_FUNC niRFSA_GetAttributeViString(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 bufSize, ViChar value[]);

ViStatus _VI_FUNC niRFSA_GetAttributeViBoolean(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViBoolean *value);

ViStatus _VI_FUNC niRFSA_GetAttributeViSession(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViSession *value);

ViStatus _VI_FUNC niRFSA_ResetAttribute(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId);

/*-------------------------------- Sparameter de-embedding API ----------------------------------------*/

ViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableS2PFile(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   ViConstString s2pFilePath,
   ViInt32 sparameterOrientation);

ViStatus _VI_FUNC niRFSA_CreateDeembeddingSparameterTableArray(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   const ViReal64 frequencies[], ViInt32 frequenciesSize,
   const NIComplexNumber sparameterTable[], ViInt32 sparameterTableSize,
   ViInt32 numberOfPorts,
   ViInt32 sparameterOrientation);

ViStatus _VI_FUNC niRFSA_DeleteDeembeddingTable(
   ViSession vi,
   ViConstString port,
   ViConstString tableName);

ViStatus _VI_FUNC niRFSA_DeleteAllDeembeddingTables(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationNearest
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName
);

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationLinear
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   ViInt32 format
);

ViStatus _VI_FUNC niRFSA_ConfigureDeembeddingTableInterpolationSpline
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName
);

ViStatus _VI_FUNC niRFSA_GetDeembeddingSparameters
(
   ViSession vi,
   NIComplexNumber *sparameters, ViInt32 sparametersArraySize,
   ViInt32 *numberOfSparameters,
   ViInt32 *numberOfPorts
);

/****************************************************************************
 *--------------------------------- obsolete -------------------------------*
 ****************************************************************************/
#define NIRFSA_ATTR_SPECTRUM_CENTER_FREQUENCY                     /* ViReal64    */ (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 2L)
#define NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_MINIMUM_QUIET_TIME  /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 58L)
#define NIRFSA_VAL_PXI_CLK10_STR                       "PXI_Clk10"
#define NIRFSA_VAL_LOW                                  NIRFSA_VAL_NARROW
#define NIRFSA_VAL_HIGH                                 NIRFSA_VAL_WIDE
// Create an alias in case someone used the unsupported constant
#define NIRFSA_ATTR_RECONFIGURATION_TRIGGER_SOURCE                          NIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE
#define NIRFSA_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE                  NIRFSA_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE
#define NIRFSA_CAL_TONE_FREQUENCY                                           NIRFSA_ATTR_CAL_TONE_FREQUENCY
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_DOWNCONVERTER_ONLY_MODE      NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_EXTERNAL_DIGITIZER_MODE
#define NIRFSA_ATTR_PRESELECTOR_ENABLED                 NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED

#define NIRFSA_ATTR_CAL_TONE_MODE                       NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_MODE
#define NIRFSA_ATTR_CAL_TONE_FREQUENCY                  NIRFSA_ATTR_DOWNCONVERTER_CAL_TONE_FREQUENCY

// Typo created in RFSA 2.5.2
#define NIRFSA_VAL_END_OR_RECORD_EVENT_STR              NIRFSA_VAL_END_OF_RECORD_EVENT_STR

// Added in 14.1. We have the same error description but from different components
#define NIRFSA_WARN_IFDIG_WARN                          NIRFSA_WARN_NISCOPE_WARN
#define NIRFSA_ERROR_IFDIG_ERROR                        NIRFSA_ERROR_NISCOPE_ERROR

// Created RF_CONDITIONING attributes as more general aliases of existing RF_PRESELECTOR attributes
#define NIRFSA_ATTR_RF_PRESELECTOR_CAL_TONE_MODE        NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE
#define NIRFSA_ATTR_RF_PRESELECTOR_CAL_TONE_FREQUENCY   NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_FREQUENCY

ViStatus _VI_FUNC niRFSA_SelfCal(
   ViSession vi);

ViStatus _VI_FUNC niRFSA_CalAdjustDownconverterGain(
   ViSession vi,
   ViConstString channelList,
   ViReal64 frequency,
   ViReal64 gain);

ViStatus _VI_FUNC niRFSA_SetUserData
(
   ViSession vi,
   ViConstString identifier,
   ViInt32 bufferSize,
   ViInt8 data[]
);

ViStatus _VI_FUNC niRFSA_GetUserData
(
   ViSession vi,
   ViConstString identifier,
   ViInt32 bufferSize,
   ViInt8 data[],
   ViInt32* actualDataSize
);

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* ___niRFSA_niRFSA_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSAErrors.h sha256=003487e670dc5303f85fafb182928c4475f9eb2f7229b7ec34fa1f3c5b69a942 bytes=47753 -->
## FILE: imports/include/niRFSAErrors.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSAErrors.h`
- sha256: `003487e670dc5303f85fafb182928c4475f9eb2f7229b7ec34fa1f3c5b69a942`
- bytes: 47753

````c
#ifndef ___niRFSA_niRFSAErrors_h___
#define ___niRFSA_niRFSAErrors_h___

/*******************************/
/*********** Errors ************/
/*******************************/

/* hex:0xBFFA4165 */
/* This function is not supported when the device is configured to run as a debug session while using breakpoints in C/C++/.NET applications. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_DEBUG_SESSION -1074118299

/* hex:0xBFFA4164 */
/* Invalid operation due to the acquired data value reference. Call Delete Data Value Reference on all outstanding data value references before calling this operation. */
#define NIRFSA_ERROR_OUTSTANDING_DATA_VALUE_REFERENCE -1074118300

/* hex:0xBFFA4163 */
/* The signal is outside of the downconverter passband. */
#define NIRFSA_ERROR_SIGNAL_OUTSIDE_DOWNCONVERTER_PASSBAND -1074118301

/* hex:0xBFFA4162 */
/* The calibration synthesizer failed to lock. */
#define NIRFSA_ERROR_CAL_SYNTH_FAILED_TO_LOCK -1074118302

/* hex:0xBFFA4161 */
/* A basecard PLL is unlocked. */
#define NIRFSA_ERROR_BASECARD_PLL_UNLOCKED -1074118303

/* hex:0xBFFA4160 */
/* A calibration measurement error occurred. The ADC overflowed while taking a measurement. */
#define NIRFSA_ERROR_CAL_ADC_OVERFLOW -1074118304

/* hex:0xBFFA415F */
/* The device ADC reported a fatal error. */
#define NIRFSA_ERROR_ADC_REPORTED_FATAL_ERROR -1074118305

/* hex:0xBFFA415E */
/* The number of samples to fetch cannot be set to -1 (default) when fetching from records that have been configured with different numbers of samples. */
#define NIRFSA_ERROR_CANNOT_FETCH_NEG_ONE_SAMPLES_IN_DIFFERENT_SIZE_RECORDS -1074118306

/* hex:0xBFFA415D */
/* This device does not support record-based peer-to-peer streaming. When peer-to-peer is enabled, Number of Records must be set to 1 for finite acquisitions, and Reference and Advance Triggers must be set to None. */
#define NIRFSA_ERROR_P2P_RECORDS_NOT_SUPPORTED -1074118307

/* hex:0xBFFA415C */
/* The peer-to-peer endpoint is not available on the FPGA bitfile for your device. This may be caused by renaming or removing of the peer-to-peer FIFO on the bitfile. */
#define NIRFSA_ERROR_ENDPOINT_NOT_AVAILABLE -1074118308

/* hex:0xBFFA415B */
/* The requested action is invalid while onboard memory is disabled and peer-to-peer is enabled. */
#define NIRFSA_ERROR_ONBOARD_MEMORY_DISABLED -1074118309

/* hex:0xBFFA415A */
/* The endpoint name is invalid. The syntax for valid endpoint names is FIFOEndpointN, where N is an integer that represents the endpoint. 0 represents the first endpoint. */
#define NIRFSA_ERROR_INVALID_ENDPOINT_NAME -1074118310

/* hex:0xBFFA4159 */
/* The given configuration results in a computed acquisition size that is too large. Reduce the span, increase the resolution bandwidth, or use another resolution bandwidth type. */
#define NIRFSA_ERROR_MAX_ACQUISITION_SIZE_EXCEEDED -1074118311

/* hex:0xBFFA4158 */
/* You cannot specify multiple channels or repeated capabilities. */
#define NIRSFA_ERROR_MULTIPLE_REPEATED_CAPABILITY_NOT_ALLOWED -1074118312

/* hex:0xBFFA4157 */
/* External Calibration Missing Measurement */
#define NIRFSA_ERROR_EXTERNAL_CALIBRATION_MISSING_MEASUREMENT -1074118313

/* hex:0xBFFA4156 */
/* The given configuration results in a computed value of Spectral Lines that is too large. Reduce the Span, increase the Resolution Bandwidth, or use another Resolution Bandwidth Type. */
#define NIRFSA_ERROR_MAX_NUMBER_OF_SPECTRAL_LINES_EXCEEDED -1074118314

/* hex:0xBFFA4155 */
/* This trigger type is not supported in multispan spectrum acquisition. */
#define NIRFSA_ERROR_TRIGGERING_TYPE_NOT_SUPPORTED_IN_MULTISPAN -1074118315

/* hex:0xBFFA4154 */
/* Self calibration data is missing or invalid. Try performing a self calibration on the device and try again. */
#define NIRFSA_ERROR_SELF_CALIBRATION_DATA_MISSING_OR_INVALID -1074118316

/* hex:0xBFFA4153 */
/* Selected steps to omit are invalid or unsupported for specific session type or device type. */
#define NIRFSA_ERROR_RESET_WITH_OPTION_STEPS_TO_OMIT_INVALID -1074118317

/* hex:0xBFFA4152 */
/* An acquisition data overflow occurred. Not fetching records or not checking the acquisition status fast enough might cause this. */
#define NIRFSA_ERROR_ACQUISITION_DATA_OVERFLOW -1074118318

/* hex:0xBFFA4151 */
/* The currently installed version of NI-RFSA is not compatible with the currently installed version of  NI PXIe-5668R Support. Upgrade your NI-RFSA installation, or downgrade your NI PXIe-5668R Support installation. */
#define NIRFSA_ERROR_INCOMPATIBLE_IFDIG_DRIVER_VERSION -1074118319

/* hex:0xBFFA4150 */
/* This functionality is not available with the current bitfile */
#define NIRFSA_ERROR_FUNCTIONALITY_NOT_SUPPORTED_WITH_CURRENT_BITFILE -1074118320

/* hex:0xBFFA414F */
/* You cannot simulate a connection to Session Access enabled device. */
#define NIRFSA_ERROR_CLIENT_SESSION_NOT_SUPPORTED_IN_SIMULATION -1074118321

/* hex:0xBFFA414E */
/* The initialize failed due to the device being busy with a pending read or calibration operation. */
#define NIRFSA_ERROR_INIT_FAIL_DEVICE_BUSY -1074118322

/* hex:0xBFFA414D */
/* You cannot simulate a connection to a session access enabled device. */
#define NIRFSA_ERROR_CANNOT_SIMULATE_CONNECTION_TO_SESSION_ACCESS_ENABLED_DEVICE -1074118323

/* hex:0xBFFA414C */
/* Device Session access is not available. Suspend the operation on the device before requesting device session access again. */
#define NIRFSA_ERROR_DEVICE_SESSION_ACCESS_NOT_AVAILABLE -1074118324

/* hex:0xBFFA414B */
/* The module EEPROM is not formatted correctly. Format the EEPROM. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_EEPROM_NOT_FORMATTED -1074118325

/* hex:0xBFFA414A */
/* The resolution bandwidth specified is larger than the instantaneous bandwidth of the device for one or more spans or the configured FFT width in the spectrum acquisition. This can result in the loss of information in the overall spectrum. Reduce the resolution bandwidth to acquire more accurate data. */
#define NIRFSA_ERROR_RBW_LARGER_THAN_DEVICE_BW -1074118326

/* hex:0xBFFA4149 */
/* NI-RFSA failed to detect the calibration tone while running self calibration. Ensure that all the modules in the system are properly connected by running the test panel in MAX. Contact NI technical support at ni.com/support if this problem persists. */
#define NIRFSA_ERROR_CAL_TONE_NOT_DETECTED -1074118327

/* hex:0xBFFA4148 */
/* An RF power overload has occurred on the device. The device's signal chain has been disconnected to protect the device. Remove the input signal, reduce the input signal power, or increase the system attenuation. */
#define NIRFSA_ERROR_RF_OVERLOAD -1074118328

/* hex:0xBFFA4147 */
/* An IF power overload has occurred on the device. The device's signal chain has been disconnected to protect the device. Remove the input signal, reduce the input signal power, or increase the system attenuation. */
#define NIRFSA_ERROR_IF_OVERLOAD -1074118329

/* hex:0xBFFA4146 */
/* An RF and IF power overload has occurred on the device. The device's signal chain has been disconnected to protect the device. Remove the input signal, reduce the input signal power, or increase the system attenuation. */
#define NIRFSA_ERROR_IF_AND_RF_OVERLOAD -1074118330

/* hex:0xBFFA4145 */
/* The IF Conditioning device returned the following error: */
#define NIRFSA_ERROR_IF_CONDITIONING_ERROR -1074118331

/* hex:0xBFFA4144 */
/* The RF Conditioning device returned the following error: */
#define NIRFSA_ERROR_RF_CONDITIONING_ERROR -1074118332

/* hex:0xBFFA4143 */
/* Child device missing in the current combined device configuration. */
#define NIRFSA_ERROR_CHILD_DEVICE_MISSING -1074118333

/* hex:0xBFFA4142 */
/* The IF Conditioning device is not supported in the current combined device configuration. */
#define NIRFSA_ERROR_IF_CONDITIONING_DEVICE_NOT_SUPPORTED_FOR_COMBINED_DEVICE -1074118334

/* hex:0xBFFA4141 */
/* RF Preselector not supported in the current combined device configuration. */
#define NIRFSA_ERROR_RF_PRESELECTOR_NOT_SUPPORTED_FOR_COMBINED_DEVICE -1074118335

/* hex:0xBFFA4140 */
/* The specified IF Conditioning device is not supported by NI-RFSA. */
#define NIRFSA_ERROR_IF_CONDITIONING_DEVICE_NOT_SUPPORTED -1074118336

/* hex:0xBFFA413F */
/* The specified RF Preselector is not supported by NI-RFSA. */
#define NIRFSA_ERROR_RF_PRESELECTOR_NOT_SUPPORTED -1074118337

/* hex:0xBFFA413E */
/* IF Conditioning device resource name is invalid. The resource name can be invalid because you either associated an invalid IF Conditioning device resource name in MAX with the downconverter or because you tried to use niRFSA Init With Options with a DriverSetup string that included an invalid IF Conditioning device resource name. */
#define NIRFSA_ERROR_INVALID_IF_CONDITIONING_DEVICE_RESOURCE_NAME -1074118338

/* hex:0xBFFA413D */
/* RF Preselector resource name is invalid. The resource name can be invalid because you either associated an invalid RF Preselector resource name in MAX with the downconverter or because you tried to use niRFSA Init With Options with a DriverSetup string that included an invalid RF Preselector resource name. */
#define NIRFSA_ERROR_INVALID_RF_PRESELECTOR_RESOURCE_NAME -1074118339

/* hex:0xBFFA413C */
/* The number of samples to fetch cannot be set to -1 (default) when contiguous multi record is enabled. */
#define NIRFSA_ERROR_CANNOT_FETCH_NEG_ONE_SAMPLES_IN_CONTIG_MULTIREC -1074118340

/* hex:0xBFFA413B */
/* The requested amplitude settling is not achievable while in list mode. */
#define NIRFSA_ERROR_AMPLITUDE_SETTLING_NOT_ACHIEVABLE_IN_LIST_MODE -1074118341

/* hex:0xBFFA413A */
/* An attribute value conflicts with the value that the current external alignment step needs to configure. */
#define NIRFSA_ERROR_EXT_ALIGNMENT_ATTR_CONFLICT_WITH_USER -1074118342

/* hex:0xBFFA4139 */
/* The preselector alignment coeffcients are invalid. */
#define NIRFSA_ERROR_INVALID_PRESELECTOR_ALIGNMENT_COEFFICIENTS -1074118343

/* hex:0xBFFA4138 */
/* Requested operation cannot be used during an external alignment session. */
#define NIRFSA_ERROR_INVALID_FUNCTION_IN_EXT_ALIGNMENT_SESSION -1074118344

/* hex:0xBFFA4137 */
/* An external alignment function cannot be used on a non external alignment session. */
#define NIRFSA_ERROR_EXT_ALIGNMENT_FUNC_OUTSIDE_ALIGNMENT_SESSION -1074118345

/* hex:0xBFFA4136 */
/* The device temperature varied more than allowed while performing the external alignment operation. */
#define NIRFSA_ERROR_EXT_ALIGNMENT_TEMP_DEVIATION_EXCEEDED -1074118346

/* hex:0xBFFA4135 */
/* An invalid external alignment step has been provided. */
#define NIRFSA_ERROR_INVALID_EXT_ALIGNMENT_STEP -1074118347

/* hex:0xBFFA4134 */
/* This external alignment function is not supported on this device. */
#define NIRFSA_ERROR_EXT_ALIGNMENT_FUNC_NOT_SUPPORTED -1074118348

/* hex:0xBFFA4133 */
/* External Alignment operations cannot be performed on simulated devices. */
#define NIRFSA_ERROR_EXT_ALIGNMENT_SESSION_NOT_SUPPORTED_IN_SIMULATION -1074118349

/* hex:0xBFFA4132 */
/* Self calibration procedure failed. If this is the first time you have seen this error, check your connections and try again. If the problem persists, contact NI for technical support. */
#define NIRFSA_ERROR_SELF_CALIBRATION_FAILED -1074118350

/* hex:0xBFFA4131 */
/* Size of calibration data adjusted exceeds on board memory capacity. */
#define NIRFSA_ERROR_EEPROM_CALIBRATION_DATA_OVERFLOW -1074118351

/* hex:0xBFFA4130 */
/* Relay count operations are not supported on this device */
#define NIRFSA_ERROR_RELAY_COUNT_NOT_SUPPORTED -1074118352

/* hex:0xBFFA412F */
/* Calibration Tone Frequency was found to exceed maximum deviation. Make sure the PXI chassis backplane clock and the LO Reference Clock are both locked to the same source. */
#define NIRFSA_ERROR_CAL_TONE_FREQUENCY_MAX_DEVIATION_EXCEEDED -1074118353

/* hex:0xBFFA412E */
/* The specified calibration gain adjustment is invalid, verify calibration setup is correct. Contact NI support for further information */
#define NIRFSA_ERROR_EXTCAL_INVALID_GAIN_ADJUSTED -1074118354

/* hex:0xBFFA412D */
/* Adjacent Channel Power Ratio (ACPR) measurements are not supported in the current IF Filter path. Choose a narrower IF Filter by decreasing Span or Device Instantaneous Bandwidth. */
#define NIRFSA_ERROR_ACPR_NOT_SUPPORTED_IN_FILTER_PATH -1074118355

/* hex:0xBFFA412C */
/* Adjacent Channel Power Ratio (ACPR) measurement calibration is not supported with the selected IF filter path, Choose a different table type or a narrower filter. */
#define NIRFSA_ERROR_ACPR_CALIBRATION_NOT_SUPPORTED_IN_FILTER_PATH -1074118356

/* hex:0xBFFA412B */
/* NI-RFSA cannot achieve the specified calibration tone frequency. To solve this issue, try changing the requested resolution. */
#define NIRFSA_ERROR_CALIBRATION_TONE_INVALID -1074118357

/* hex:0xBFFA412A */
/* The number of frequencies and LO attenuation settings being passed to the function are not the same. Ensure the arrays you pass to the function have the same number of elements. */
#define NIRFSA_ERROR_NUMBER_OF_FREQUENCIES_LO_ATTENUATION_MISMATCH -1074118358

/* hex:0xBFFA4129 */
/* NI-RFSA cannot initialize a calibration session because another calibration session for the specified device is already open. Close the open session by calling niRFSA Close Ext Cal or by exiting the application with the open session. */
#define NIRFSA_ERROR_CAL_SESSION_ALREADY_EXISTS -1074118359

/* hex:0xBFFA4128 */
/* Calibration is not supported on simulated devices. */
#define NIRFSA_ERROR_CALIBRATION_SESSION_NOT_SUPPORTED_IN_SIMULATION -1074118360

/* hex:0xBFFA4127 */
/* You have exceeded the EEPROM memory space allocated for Self Cal. Run Self Cal again for all invalid steps, or contact NI technical support. */
#define NIRFSA_ERROR_EEPROM_SPACE_EXCEEDED_FOR_SELF_CAL -1074118361

/* hex:0xBFFA4126 */
/* The gain associated with the specified index is not valid for the specified frequency. */
#define NIRFSA_ERROR_INVALID_IF_GAIN_FOR_FREQUENCY -1074118362

/* hex:0xBFFA4125 */
/* The parameter value specified is not supported when using an external digitizer. */
#define NIRFSA_ERROR_INVALID_PARAMETER_VALUE_FOR_EXTERNAL_DIGITIZER -1074118363

/* hex:0xBFFA4124 */
/* This property or attribute is supported only during a calibration session. */
#define NIRFSA_ERROR_ATTR_NOT_SUPPORTED_IN_NON_CALIBRATION_SESSION -1074118364

/* hex:0xBFFA4123 */
/* LO2 and LO3 calibration adjustment supports adjusting only a single LO frequency (4 GHz  and 800 MHz, respectively). */
#define NIRFSA_ERROR_INVALID_LO_EXPORT_CALIBRATION_NUMBER_OF_FREQUENCIES -1074118365

/* hex:0xBFFA4122 */
/* The device temperature deviation during calibration exceeded the maximum allowed amount. To correct the issue, ensure good ventilation and a stable room temperature, and set the fan speed to its maximum. */
#define NIRFSA_ERROR_CALIBRATION_TEMPERATURE_DEVIATION_EXCEEDED -1074118366

/* hex:0xBFFA4121 */
/* A configuration property or attribute that is required for calibration is missing. Commit these properties and attributes prior to calling calibration adjustment VIs and functions. */
#define NIRFSA_ERROR_REQUIRED_CALIBRATION_PARAMETER_MISSING -1074118367

/* hex:0xBFFA4120 */
/* An invalid LO export number was provided to the niRFSA Cal Adjust LO Export Calibration function. */
#define NIRFSA_ERROR_INVALID_LO_EXPORT_NUMBER -1074118368

/* hex:0xBFFA411F */
/* The LO Export attenuation was adjusted to a value outside the supported range. */
#define NIRFSA_ERROR_LO_EXPORT_ATTENUATION_OUT_OF_RANGE -1074118369

/* hex:0xBFFA411E */
/* The maximum supported mixer level was exceeded. This problem is usually caused by forcing low RF attenuation. To correct the issue, increase the RF attenuation so that the mixer level is equal to the reference level minus the RF attenuation plus RF gain. */
#define NIRFSA_ERROR_MAXIMUM_MIXER_LEVEL_EXCEEDED -1074118370

/* hex:0xBFFA411D */
/* NI-RFSA failed to align the YIG tunable filter (YTF). */
#define NIRFSA_ERROR_YTF_ALIGNMENT_DOES_NOT_COVER_RANGE -1074118371

/* hex:0xBFFA411C */
/* NI-RFSA failed to detect a signal while calibrating the YTF module. Ensure that your LO and digitizer are properly connected by running the test panel in MAX. */
#define NIRFSA_ERROR_YTF_ALIGNMENT_SIGNAL_DETECTION_FAILED -1074118372

/* hex:0xBFFA411B */
/* Creation of the simulated device failed. Connection to the MXS database is taking too long. Restart your system, and if this process does not solve the problem, contact NI technical support. */
#define NIRFSA_ERROR_SIMULATED_DEVICE_CREATION_FAILED -1074118373

/* hex:0xBFFA411A */
/* NI-RFSA does not support the specified LO. */
#define NIRFSA_ERROR_LO_NOT_SUPPORTED -1074118374

/* hex:0xBFFA4119 */
/* The specified keyword is not supported in this session. Real sessions support Digitizer and LO Driver Setup keywords, while simulated sessions support DigitizerModel and LOModel Driver Setup keywords. Refer to the documentation for more information about Driver Setup keywords. */
#define NIRFSA_ERROR_KEYWORD_NOT_SUPPORTED_IN_SESSION -1074118375

/* hex:0xBFFA4118 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: There are too many endpoints for streaming initialization. */
#define NIRFSA_ERROR_TOO_MANY_STREAMING_ENDPOINTS -1074118376

/* hex:0xBFFA4117 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: The file size is too large for parameter block. */
#define NIRFSA_ERROR_FILESIZE_OVERFLOW -1074118377

/* hex:0xBFFA4116 */
/* The Reference clock is not a valid value for this operation. */
#define NIRFSA_ERROR_REF_CLOCK_INVALID_SIGNAL_TYPE -1074118378

/* hex:0xBFFA4115 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: The attenuation table has too many entries. */
#define NIRFSA_ERROR_TOO_MANY_ELEMENTS_IN_ATTENUATION_TABLE -1074118379

/* hex:0xBFFA4114 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: The band has too many frequencies for calibration. */
#define NIRFSA_ERROR_TOO_MANY_FREQUENCIES_IN_BAND -1074118380

/* hex:0xBFFA4113 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: There are too many elements for the EEPROM size. */
#define NIRFSA_ERROR_EEPROM_ELEMENT_OVERFLOW -1074118381

/* hex:0xBFFA4112 */
/* An internal software error has occurred. Contact NI technical support at ni.com/support, with the following information: The size of the LabVIEW array is too large. */
#define NIRFSA_ERROR_LABVIEW_ARRAY_TOO_LARGE -1074118382

/* hex:0xBFFA4111 */
/* You have exceeded the maximum number of configuration list steps supported for your device. */
#define NIRFSA_ERROR_MAX_STEP_COUNT_EXCEEDED -1074118383

/* hex:0xBFFA4110 */
/* NI-RFSA cannot get the frequency response. Calibration data is not available for this device configuration. */
#define NIRFA_ERROR_CANNOT_GET_FREQUENCY_RESPONSE -1074118384

/* hex:0xBFFA410F */
/* The currently installed version of NI-RFSA is not compatible with the currently installed version of NI-RFSG. Downgrade your NI-RFSA installation, or upgrade your NI-RFSG installation. */
#define NIRFSA_ERROR_NIRFSG_DRIVER_VERSION_TOO_OLD -1074118385

/* hex:0xBFFA410E */
/* The currently installed version of NI-RFSA is not compatible with the currently installed version of NI-RFSG. Upgrade your NI-RFSA installation, or downgrade your NI-RFSG installation. */
#define NIRFSA_ERROR_NIRFSG_DRIVER_VERSION_TOO_NEW -1074118386

/* hex:0xBFFA410D */
/* The number of measurements taken for reference level calibration is insufficient. Please refer to the calibration procedure document to see the list of required measurement configurations. */
#define NIRFSA_ERROR_INVALID_ALT_REF_CAL_MEASUREMENTS -1074118387

/* hex:0xBFFA410C */
/* The option string has too many characters. */
#define NIRFSA_ERROR_OPTION_STRING_TOO_LONG -1074118388

/* hex:0xBFFA410B */
/* The LVDLL returned the following error: */
#define NIRFSA_ERROR_LVDLL_ERROR -1074118389

/* hex:0xBFFA410A */
/* The combination of the number of records, number of samples per record, and the size of sample in bytes exceeds maximum allowed allocation size. */
#define NIRFSA_ERROR_REQUESTED_ALLOCATION_TOO_LARGE -1074118390

/* hex:0xBFFA4109 */
/* There are insufficient number of IF Attenuation measurements. The required number of measurements is 256. */
#define NIRFSA_ERROR_INVALID_CAL_NUM_OF_IF_ATTEN_MEASUREMENTS -1074118391

/* hex:0xBFFA4108 */
/* The specified operation cannot be performed while the device is being reset. */
#define NIRFSA_ERROR_OPERATION_NOT_SUPPORTED_DURING_RESET -1074118392

/* hex:0xBFFA4107 */
/* Password is longer than maximum length. */
#define NIRFSA_ERROR_CAL_PASSWORD_LENGTH_VIOLATION -1074118393

/* hex:0xBFFA4106 */
/* The number of frequencies is different than the number of DAC values. They should be the same. */
#define NIRFSA_ERROR_FREQUENCY_DAC_VALUE_ARRAY_SIZE_VIOLATION -1074118394

/* hex:0xBFFA4105 */
/* The calibration close action specified is not supported by this instrument driver. The valid values for calibration action are Commit or Abort. */
#define NIRFSA_ERROR_INVALID_CLOSE_ACTION -1074118395

/* hex:0xBFFA4104 */
/* Requested operation cannot be used during an external calibration session. */
#define NIRFSA_ERROR_INVALID_FUNCTION_IN_CAL_SESSION -1074118396

/* hex:0xBFFA4103 */
/* The calibration number of measurements specified is not supported by this instrument driver. The number of measurements should be greater than 0. */
#define NIRFSA_ERROR_INVALID_CAL_NUM_OF_MEASUREMENTS -1074118397

/* hex:0xBFFA4102 */
/* The calibration number of attenuators specified is not supported by this instrument driver. The number of attenuators should be 2. */
#define NIRFSA_ERROR_INVALID_CAL_NUM_OF_ATTENUATORS -1074118398

/* hex:0xBFFA4101 */
/* The calibration number of frequencies specified is not supported by this instrument driver. The number of frequencies should be greater than 0. */
#define NIRFSA_ERROR_INVALID_CAL_NUM_OF_FREQUENCIES -1074118399

/* hex:0xBFFA4100 */
/* The calibration reference level calibration data type specified is not supported by this instrument driver. The valid values are default or mechanical attenuator disabled. */
#define NIRFSA_ERROR_INVALID_CAL_REF_LEVEL_CAL_DATA_TYPE -1074118400

/* hex:0xBFFA40FF */
/* The calibration attenuator table number parameter specified is not supported by this instrument driver. The valid values for attenuator table numbers are 0 to 2. */
#define NIRFSA_ERROR_INVALID_CAL_ATTENUATOR_TABLE_NUMBER -1074118401

/* hex:0xBFFA40FE */
/* The calibration bandwidth parameter specified is not supported by this instrument driver. The bandwidth specified should be greater than 0. */
#define NIRFSA_ERROR_INVALID_CAL_BANDWIDTH -1074118402

/* hex:0xBFFA40FD */
/* The calibration IF filter parameter specified is not supported by this instrument driver. The valid values for the IF filter are 187.5 MHz Wide, 187.5 MHz Narrow, 53 MHz, and Bypass. */
#define NIRFSA_ERROR_INVALID_CAL_IF_FILTER -1074118403

/* hex:0xBFFA40FC */
/* The calibration RF band specified is not supported by this instrument driver. The valid values for the RF band are RF bands 1 to 4 inclusive. */
#define NIRFSA_ERROR_INVALID_CAL_RF_BAND -1074118404

/* hex:0xBFFA40FB */
/* The calibration frequency specified is not supported by this instrument driver. */
#define NIRFSA_ERROR_INVALID_CAL_FREQUENCY -1074118405

/* hex:0xBFFA40FA */
/* The calibration function specified is not supported in this calibration step. Call the appropriate calibration function or initialize the appropriate calibration step prior to calling this calibration function. */
#define NIRFSA_ERROR_CAL_FUNCTION_CALLED_IN_INCORRECT_CAL_STEP -1074118406

/* hex:0xBFFA40F9 */
/* The previous calibration step is not closed. Close the previous calibration step before calling this function. */
#define NIRFSA_ERROR_CAL_STEP_NOT_CLOSED -1074118407

/* hex:0xBFFA40F8 */
/* The calibration step specified is not supported without first performing an LO ALC DAC alignment. */
#define NIRFSA_ERROR_CAL_STEP_NOT_VALID_WITHOUT_LO_ALC_DAC_ALIGNMENT -1074118408

/* hex:0xBFFA40F7 */
/* The calibration step specified is not supported by this instrument driver. */
#define NIRFSA_ERROR_INVALID_CALIBRATION_STEP -1074118409

/* hex:0xBFFA40F6 */
/* The calibration action specified is not supported by this instrument driver. The valid values for calibration action are Create and Append. */
#define NIRFSA_ERROR_INVALID_CAL_ACTION -1074118410

/* hex:0xBFFA40F5 */
/* The requested device configuration requires you to directly specify an additional property. */
#define NIRFSA_ERROR_REQUIRED_ATTRIBUTE_NOT_SPECIFIED -1074118411

/* hex:0xBFFA40F4 */
/* Cannot compute downconverter gain because no calibration data exists for this device configuration. */
#define NIRFSA_ERROR_CANNOT_FETCH_DC_GAIN_FOR_NON_CALIBRATED_DATA -1074118412

/* hex:0xBFFA40F3 */
/* Multispan spectrum acquisition is not supported while in-band retuning is enabled. Reduce the spectrum span for the acquisition or do not set the Downconverter Center Frequency property or the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attribute. Consult the device documentation for information about supported RF bands and their corresponding real-time bandwidths. */
#define NIRFSA_ERROR_MULTISPAN_NOT_SUPPORTED_WITH_INBAND_RETUNING -1074118413

/* hex:0xBFFA40F2 */
/* The spectrum frequencies specified span two or more frequency bands which have different real-time bandwidths. Reduce the spectrum span or break up the spectrum acquisition into multiple segments. Consult the device documentation for information on its RF bands and their corresponding real-time bandwidths. */
#define NIRFSA_ERROR_SPECTRUM_SPANS_BANDS_OF_DIFFERENT_BANDWIDTH -1074118414

/* hex:0xBFFA40F1 */
/* The IQ Rate specified is larger than the maximum supported IQ Rate for the current settings. Consider lowering your IQ Rate or disabling fractional resampling. */
#define NIRFSA_ERROR_IQ_RATE_TOO_HIGH_FOR_FRACTIONAL_RESAMPLING_MODE -1074118415

/* hex:0xBFFA40F0 */
/* You cannot configure the LO Frequency attribute when NI-RFSA is controlling the LO device. You can only use this attribute to read the coerced LO frequency in this session. */
#define NIRFSA_ERROR_CANNOT_SET_LO_FREQUENCY_WITH_INTERNAL_LO -1074118416

/* hex:0xBFFA40EF */
/* The DriverSetup tags are specified with conflicting settings. Refer to the user documentation for information about the DriverSetup syntax. */
#define NIRFSA_ERROR_CONFLICTING_DRIVER_SETUP_TAGS_SPECIFIED -1074118417

/* hex:0xBFFA40EE */
/* The spectrum span specified is larger than the bandwidth of the device at the given frequency. This is not supported when the LO is external to the RFSA session. */
#define NIRFSA_ERROR_MULTISPAN_NOT_SUPPORTED_WITH_EXTERNAL_LO -1074118418

/* hex:0xBFFA40ED */
/* Only the high downconverter loop bandwidth is configurable for spans greater than 10 MHz. */
#define NIRFSA_ERROR_SPAN_AND_LOOP_BANDWIDTH -1074118419

/* hex:0xBFFA40EC */
/* This function is only supported when using NI-RFSA in external digitizer mode. Specify the digitizer resource name as <external> in MAX or in the Option String. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_DOWNCONVERTER_DIGITIZER_MODE -1074118420

/* hex:0xBFFA40EB */
/* This attribute is only supported when using NI-RFSA in external digitizer mode. Specify the digitizer resource name as <external> in MAX or in the Option String. */
#define NIRFSA_ERROR_ATTR_NOT_SUPPORTED_IN_DOWNCONVERTER_DIGITIZER_MODE -1074118421

/* hex:0xBFFA40E6 */
/* Fetch position and fetch offset cannot be configured in a spectrum acquisition. Reset the attributes in order to read the spectrum. */
#define NIRFSA_ERROR_FETCH_POSITION_AND_OFFSET_IN_SPECTRUM_ACQUISITION -1074118426

/* hex:0xBFFA40E5 */
/* You have configured multiple records to be acquired in a continuous acquisition. You can only configure multiple records when the number of samples is finite parameter is set to TRUE. */
#define NIRFSA_ERROR_MULTIPLE_RECORDS_IN_CONT_ACQ -1074118427

/* hex:0xBFFA40E4 */
/* Driver has stopped operating because a sensor on the device detected a temperature in excess of the maximum recommended operating temperature. Possible causes incude excessive current on the device channels and inadequate chassis cooling.To use the device again, reduce the current and/or improve the chassis cooling. Ensure that the device has cooled before operating it. */
#define NIRFSA_ERROR_TEMPERATURE_EXCEEDS_OPERATING_LIMIT -1074118428

/* hex:0xBFFA40E3 */
/* You cannot call Read IQ when you are acquiring more than one record. Use Initiate and Fetch IQ instead. */
#define NIRFSA_ERROR_READ_IN_MULTIRECORD_ACQUISITION -1074118429

/* hex:0xBFFA40E2 */
/* You cannot call Read IQ when the number of samples is not finite. Use Initiate and Fetch IQ instead. */
#define NIRFSA_ERROR_READ_IN_CONTINUOUS_ACQUISITION -1074118430

/* hex:0xBFFA40E1 */
/* The frequency range specified by the combination of center frequency and span values contains data outside the frequency range allowed for this device. */
#define NIRFSA_ERROR_FREQUENCY_CONTENT_OUTSIDE_SPECIFICATION -1074118431

/* hex:0xBFFA40E0 */
/* The number of records to fetch cannot be set to -1 (default) when the number of records to acquire is not a finite quantity. */
#define NIRFSA_ERROR_CANNOT_FETCH_NEG_ONE_RECORDS_IN_CONT_ACQ -1074118432

/* hex:0xBFFA40DF */
/* The number of samples to fetch cannot be set to -1 (default) when the number of samples to acquire is not a finite quantity. */
#define NIRFSA_ERROR_CANNOT_FETCH_NEG_ONE_SAMPLES_IN_CONT_ACQ -1074118433

/* hex:0xBFFA40DE */
/* Firmware is corrupted or is not working correctly. Reboot your system. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_FIRMWARE -1074118434

/* hex:0xBFFA40DD */
/* The specified value is not a recognized Boolean value. Refer to the user documentation for information about the DriverSetup syntax. */
#define NIRFSA_ERROR_INVALID_BOOLEAN_IN_DRIVER_SETUP -1074118435

/* hex:0xBFFA40DC */
/* Trigger source must be specified for the given trigger type. */
#define NIRFSA_ERROR_TRIGGER_SOURCE_NOT_SPECIFIED -1074118436

/* hex:0xBFFA40DB */
/* This attribute is not supported in a spectrum acquisition. */
#define NIRFSA_ERROR_ATTR_NOT_SUPPORTED_IN_SPECTRUM_ACQUISITION -1074118437

/* hex:0xBFFA40DA */
/* The temperature sensor on the device returned a bad reading. The sensor may be failing and need replacement. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_BAD_TEMPERATURE_READING -1074118438

/* hex:0xBFFA40D9 */
/* The Sample clock timebase rate is unspecified. You must specify a Sample clock timebase rate when a spectrum acquisition is configured and a Sample clock timebase source is configured. */
#define NIRFSA_ERROR_SPECIFY_SOURCE_AND_RATE_IN_SPECTRUM_ACQUISITION -1074118439

/* hex:0xBFFA40D8 */
/* Exporting this event is not supported when the acquisition type is set to Spectrum. */
#define NIRFSA_ERROR_EVENT_NOT_SUPPORTED_IN_SPECTRUM_ACQUISITION -1074118440

/* hex:0xBFFA40D7 */
/* This trigger type is not supported when the acquisition type is set to Spectrum. */
#define NIRFSA_ERROR_TRIG_NOT_SUPPORTED_IN_SPECTRUM_ACQUISITION -1074118441

/* hex:0xBFFA40D6 */
/* You cannot configure the Arm Reference trigger without configuring the device to use the Reference trigger. */
#define NIRFSA_ERROR_ARM_REF_TRIGGER_NOT_ALLOWED_WITHOUT_REF_TRIGGER -1074118442

/* hex:0xBFFA40D5 */
/* The value of reference level minus the value of attenuation must be smaller or equal to 0. */
#define NIRFSA_ERROR_ATTENUATION_TOO_SMALL_FOR_REF_LEVEL -1074118443

/* hex:0xBFFA40D4 */
/* You have attempted to configure a Reference trigger for an acquisition containing an unbounded number of samples. You can only use the Reference trigger if the number of samples per record is finite. */
#define NIRFSA_ERROR_REF_TRIG_IN_CONTINUOUS_ACQUISITION -1074118444

/* hex:0xBFFA40D3 */
/* You have attempted to configure an unbounded number of samples and an unbounded number of records in the same acquisition. At least one of the two quantities must be configured as finite. */
#define NIRFSA_ERROR_BOTH_SAMPLES_AND_RECORDS_ARE_UNBOUNDED -1074118445

/* hex:0xBFFA40D1 */
/* The value of mixer level must be no more than 50 dBm smaller than the value of reference level. */
#define NIRFSA_ERROR_MIXER_LEVEL_TOO_SMALL_FOR_REF_LEVEL -1074118447

/* hex:0xBFFA40D0 */
/* Mixer level must be less than or equal to reference level. */
#define NIRFSA_ERROR_MIXER_LEVEL_GREATER_THAN_REF_LEVEL -1074118448

/* hex:0xBFFA40CF */
/* Driver was unloaded and then reloaded at a different base address after the session was created. Session is unusable. Close and reopen the session. */
#define NIRFSA_ERROR_SESSION_CORRUPTED_BY_DLL_RELOAD -1074118449

/* hex:0xBFFA40CE */
/* You must specify exactly one channel or repeated capability from which to retrieve an attribute. */
#define NIRFSA_ERROR_ONLY_ONE_IDENTIFIER_ALLOWED -1074118450

/* hex:0xBFFA40CD */
/* No value was found for the tag. Valid DriverSetup strings have the form "tag:value; tag:value; ... tag:value". Refer to the user documentation for information about the DriverSetup syntax. */
#define NIRFSA_ERROR_VALUE_NOT_SPECIFIED_FOR_DRIVER_SETUP_TAG -1074118451

/* hex:0xBFFA40CC */
/* The tag is specified more than once. Refer to the user documentation for information about the DriverSetup syntax. */
#define NIRFSA_ERROR_DRIVER_SETUP_TAG_SPECIFIED_MORE_THAN_ONCE -1074118452

/* hex:0xBFFA40CB */
/* The specified tag is not supported. Refer to the user documentation for information about the DriverSetup syntax. */
#define NIRFSA_ERROR_UNSUPPORTED_DRIVER_SETUP_TAG -1074118453

/* hex:0xBFFA40CA */
/* You must specify the reference level, attenuation, and mixer level attributes such that attenuation = reference level - mixer level. If you do not set either mixer level or attenuation, the driver selects the appropriate value for the attribute. */
#define NIRFSA_ERROR_ATTENUATION_RELATIONSHIP_INVALID -1074118454

/* hex:0xBFFA40C9 */
/* Specified PXI Chassis CLK10 Source is invalid given the Reference clock source.  When PXI Chassis CLK10 Source is anything other than None the Reference clock source must be the same as the PXI Chassis CLK10 Source. */
#define NIRFSA_ERROR_INVALID_PXI_CLK10_SRC_GIVEN_REF_CLK_SRC -1074118455

/* hex:0xBFFA40C8 */
/* The IVI engine was unable to create the session. Repair or reinstall the NI-RFSA instrument driver. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_SESSION_FAILED_TO_INITIALIZE -1074118456

/* hex:0xBFFA401E */
/* The configured trigger level value is too high. The maximum value for the trigger level is determined by the configured reference level. */
#define NIRFSA_ERROR_TRIGGER_LEVEL_HIGHER_THAN_REF_LEVEL -1074118626

/* hex:0xBFFA401D */
/* Additional calibration information is necessary to enable this feature. */
#define NIRFSA_ERROR_ADDITIONAL_CALIBRATION_NEEDED_FOR_THIS_FEATURE -1074118627

/* hex:0xBFFA401C */
/* This function is not supported when using NI-RFSA with an external LO module. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_EXTERNAL_LO_MODE -1074118628

/* hex:0xBFFA401B */
/* This attribute is not supported when using NI-RFSA with the external LO module. */
#define NIRFSA_ERROR_ATTR_NOT_SUPPORTED_IN_EXTERNAL_LO_MODE -1074118629

/* hex:0xBFFA401A */
/* The LO returned the following error: */
#define NIRFSA_ERROR_NIRFSG_ERROR -1074118630

/* hex:0xBFFA4019 */
/* LO resource name is invalid. The resource name can be invalid because you either associated an invalid LO resource name in MAX with the downconverter or because you tried to use niRFSA Init With Options with a DriverSetup string that included an invalid LO resource name. */
#define NIRFSA_ERROR_INVALID_LO_RESOURCE_NAME -1074118631

/* hex:0xBFFA4018 */
/* Session could not be opened because the LO resource name was not specified. Specify the LO resource name in MAX or in the Option String. */
#define NIRFSA_ERROR_LO_RESOURCE_NAME_NOT_FOUND -1074118632

/* hex:0xBFFA4017 */
/* The currently installed version of NI-RFSA is not compatible with the currently installed version of NI-SCOPE. Upgrade your NI-RFSA installation, or downgrade your NI-SCOPE installation. */
#define NIRFSA_ERROR_INCOMPATIBLE_NISCOPE_DRIVER_VERSION -1074118633

/* hex:0xBFFA4016 */
/* The attenuator relays are not settled. Repair or reinstall the NI-RFSA instrument driver. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_ATTENUATORS_NOT_SETTLED -1074118634

/* hex:0xBFFA4015 */
/* The frequency tuning PLL is not locked. */
#define NIRFSA_ERROR_FREQUENCY_TUNING_PLL_NOT_LOCKED -1074118635

/* hex:0xBFFA4014 */
/* The Reference clock PLL is not locked. */
#define NIRFSA_ERROR_REF_CLK_PLL_NOT_LOCKED -1074118636

/* hex:0xBFFA4013 */
/* This attribute is not supported when using NI-RFSA with an external digitizer module. */
#define NIRFSA_ERROR_ATTR_NOT_SUPPORTED_IN_DOWNCONVERTER_ONLY_MODE -1074118637

/* hex:0xBFFA4012 */
/* This function is not supported when using NI-RFSA with an external digitizer module. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_EXTERNAL_DIGITIZER_MODE -1074118638

/* hex:0xBFFA4011 */
/* This function is not supported when the acquisition type is set to IQ. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_IQ_ACQUISITION -1074118639

/* hex:0xBFFA4010 */
/* This function is not supported when the acquisition type is set to Spectrum. */
#define NIRFSA_ERROR_FUNCTION_NOT_SUPPORTED_IN_SPECTRUM_ACQUISITION -1074118640

/* hex:0xBFFA400F */
/* You can only get the specified property while the session is committed or while the session is running.Commit or initiate the session prior to getting the property. */
#define NIRFSA_ERROR_GET_WHEN_SESSION_NOT_RUNNING -1074118641

/* hex:0xBFFA400E */
/* Unable to initialize because a session for the specified device is already open from another process. Close the open session by calling niRFSA Close or by exiting the application with the open session.  If you are using NI-RFSA SFP, refer to "Debugging your Application Using SFP Session Access" in the documentation on how to share the device in this process and NI-RFSA SFP. */
#define NIRFSA_ERROR_INSTRUMENT_ALREADY_IN_USE -1074118642

/* hex:0xBFFA400D */
/* Device not available in NI-RFSA. The device may be being used by NI-Tuner or NI-5660, or the device is being reset. After using a device in NI-Tuner, you must reset the device using the Traditional DAQ Device Reset before using it in NI-RFSA. */
#define NIRFSA_ERROR_DEVICE_ABSENT_OR_UNAVAILABLE -1074118643

/* hex:0xBFFA400C */
/* The device's calibration revision is unsupported by this version of the driver. Upgrade the driver. Contact NI Technical Support if you need additional information or the problem persists. */
#define NIRFSA_ERROR_UNSUPPORTED_CALIBRATION_REVISION -1074118644

/* hex:0xBFFA400B */
/* The specified operation cannot be performed because a session has been aborted or a device has been removed from the system. */
#define NIRFSA_ERROR_RUNTIME_ABORTED -1074118645

/* hex:0xBFFA400A */
/* Specified property cannot be set while the session is running.Set the property prior to initiating the session, or abort the session prior to setting the property. */
#define NIRFSA_ERROR_SET_WHEN_SESSION_RUNNING -1074118646

/* hex:0xBFFA4009 */
/* Specified operation is only supported while the session is running.Initiate the session before requesting the operation and ensure that the session has not been aborted. */
#define NIRFSA_ERROR_SESSION_NOT_IN_RUNNING_STATE -1074118647

/* hex:0xBFFA4008 */
/* You cannot perform this action while the session is running. */
#define NIRFSA_ERROR_SESSION_IN_RUNNING_STATE -1074118648

/* hex:0xBFFA4007 */
/* Session could not be opened because the digitizer resource name was not specified. Click on the system device in MAX and select the appropriate digitizer resource name in the Associated Devices. */
#define NIRFSA_ERROR_DIGITIZER_RESOURCE_NAME_NOT_FOUND_IN_INIT -1074118649

/* hex:0xBFFA4006 */
/* Session could not be opened because the digitizer resource name was not specified. Click on the system device in MAX and select the appropriate digitizer resource name in the Associated Devices. If you are specifying the digitizer via the Option String, ensure the digitizer Resource Name is valid. */
#define NIRFSA_ERROR_DIGITIZER_RESOURCE_NAME_NOT_FOUND -1074118650

/* hex:0xBFFA4005 */
/* Digitizer resource name is invalid. The resource name can be invalid because you either associated an invalid digitizer resource name in MAX with the downconverter or because you tried to use niRFSA Init With Options with a DriverSetup string that included an invalid digitizer resource name. */
#define NIRFSA_ERROR_INVALID_DIGITIZER_RESOURCE_NAME -1074118651

/* hex:0xBFFA4004 */
/* The specified digitizer is not supported by NI-RFSA. */
#define NIRFSA_ERROR_DIGITIZER_NOT_SUPPORTED -1074118652

/* hex:0xBFFA4003 */
/* The device specified is not supported by this driver. */
#define NIRFSA_ERROR_DEVICE_NOT_SUPPORTED -1074118653

/* hex:0xBFFA4002 */
/* Maximum time exceeded before the operation completed. */
#define NIRFSA_ERROR_MAX_TIME_EXCEEDED -1074118654

/* hex:0xBFFA4001 */
/* The digitizer returned the following error: */
#define NIRFSA_ERROR_NISCOPE_ERROR -1074118655

/* hex:0xBFFA4000 */
/* The IF Digitizer Host DLL Returned the following Error: */
#define NIRFSA_ERROR_IFDIG_LVDLL_ERROR -1074118656

/*********************************/
/*********** Warnings ************/
/*********************************/

/* hex:0x3FFA4001 */
/* The digitizer returned the following warning: */
#define NIRFSA_WARN_NISCOPE_WARN 1073364993

/* hex:0x3FFA4002 */
/* The reference clock PLL is not locked. */
#define NIRFSA_WARN_REF_CLK_PLL_NOT_LOCKED 1073364994

/* hex:0x3FFA4003 */
/* The LO returned the following warning: */
#define NIRFSA_WARN_NIRFSG_WARN 1073364995

/* hex:0x3FFA4004 */
/* The digitizer returned the following PLL warning: */
#define NIRFSA_WARN_NISCOPE_PLL_WARN 1073364996

/* hex:0x3FFA4005 */
/* The current channel coupling configuration is not calibrated, accuracy levels are not guaranteed */
#define NIRFSA_WARN_DCBLOCK_NOT_CALIBRATED 1073364997

/* hex:0x3FFA4006 */
/* The Speficied IF state is not present in the calibration data, try a different IF filter path, IF Attenuation table type, or IF Index. */
#define NIRFSA_WARN_IF_INDEX_NOT_CALIBRATED 1073364998

/* hex:0x3FFA4007 */
/* The specified Attenuation constraints are not calibrated, Reference level accuracy not guaranteed. */
#define NIRFSA_WARN_ATTENUATION_CONSTRAINT_NOT_CALIBRATED 1073364999

/* hex:0x3FFA4008 */
/* Calibration data not present or invalid, Reference level accuracy not guaranteed */
#define NIRFSA_WARN_CALIBRATION_DATA_NOT_PRESENT 1073365000

/* hex:0x3FFA4009 */
/* The current RF configuration is not calibrated. Try changing the Channel Coupling attribute, Preamp Enabled attribute, or RF attenuation configuration with either Mixer Level or RF Attenuation Attributes */
#define NIRFSA_WARN_RF_CONFIGURATION_NOT_CALIBRATED 1073365001

/* hex:0x3FFA400A */
/* Unable to correct for temperature deviation, reference level accuracy not guaranteed, re-commit settings inorder to regain accuracy. */
#define NIRFSA_WARN_TEMPERATURE_DEVIATION_LIMIT_EXCEEDED 1073365002

/* hex:0x3FFA400B */
/* External Calibration IF Equalization Self Calibration IF Equalization Data is not present. Contact NI for further assistance. */
#define NIRFSA_WARN_EXTERNAL_CAL_IF_EQUALIZATION_DATA_NOT_PRESENT 1073365003

/* hex:0x3FFA400C */
/* The RF Conditioning device returned the following warning: */
#define NIRFSA_WARN_RF_CONDITIONING_WARN 1073365004

/* hex:0x3FFA400D */
/* The IF Conditioning device returned the following warning: */
#define NIRFSA_WARN_IF_CONDITIONING_WARN 1073365005

/* hex:0x3FFA400E */
/* The self calibration offset measured by NI-RFSA was out of bounds. Ensure that all the modules in the system are externally calibrated before running self calibration. */
#define NIRFSA_WARN_SELF_CAL_OFFSET_OUT_OF_BOUNDS 1073365006

/* hex:0x3FFA400F */
/* The cache is not sufficient to store the acquired waveform within the driver. The driver will truncate the waveform and store the truncated data in the cache. */
#define NIRFSA_WARN_WAVEFORM_SIZE_EXCEEDS_MAX_CACHE_SIZE_LIMIT 1073365007

/* hex:0x3FFA4010 */
/* Hardware external calibration data format is older than the earliest revision supported by the currently installed driver.<LF/>Perform an external calibration (this will modify the calibration data).  For more information, contact NI technical support. */
#define NIRFSA_WARN_EXT_CALIBRATION_DATA_TOO_OLD_FOR_SOFTWARE 1073365008

/* hex:0x3FFA40C8 */
/* The frequency range for the spectrum contains data outside the frequency range from the device specifications. Data in this frequency range may be inaccurate. */
#define NIRFSA_WARN_FREQUENCY_CONTENT_OUTSIDE_SPECIFICATION 1073365192

/* hex:0x3FFA40C9 */
/* The device is operating at a frequency outside the frequency range from the device specifications. Data in this frequency range may be inaccurate. */
#define NIRFSA_WARN_CENTER_FREQUENCY_OUTSIDE_SPECIFICATION 1073365193

/* hex:0x3FFA40CA */
/* Hardware external calibration data format is newer than the latest revision supported by the currently installed driver.  Either externally calibrate your device (this may modify the calibration data) or upgrade your driver to the version supplied with the device. Driver updates can also be downloaded from ni.com. If uncertain, contact NI technical support. */
#define NIRFSA_WARN_EXT_CALIBRATION_DATA_TOO_NEW_FOR_SOFTWARE 1073365194

/* hex:0x3FFA40CB */
/* External calibration constants are invalid. Perform an external calibration. Contact NI Technical Support if you need additional information. */
#define NIRFSA_WARN_EXT_CALIBRATION_CONSTS_INVALID 1073365195

/* hex:0x3FFA40CC */
/* A DSP overflow was detected. Reduce the input power level or configure the reference level to a higher value to eliminate overflow. */
#define NIRFSA_WARN_DSP_OVERFLOW 1073365196

/* hex:0x3FFA40CD */
/* One or more peer-to-peer endpoints has overflowed. */
#define NIRFSA_WARN_P2P_OVERFLOW 1073365197


#endif /* ___niRFSA_niRFSAErrors_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSG.h sha256=39996d922fa37a1d60dfe1c232e705b9ed9ab9a1d8de56c90a9f3949fb9e8f81 bytes=80121 -->
## FILE: imports/include/niRFSG.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSG.h`
- sha256: `39996d922fa37a1d60dfe1c232e705b9ed9ab9a1d8de56c90a9f3949fb9e8f81`
- bytes: 80121

````c
/****************************************************************************
 *                          NI RF Signal Generator
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2003-2020.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niRFSG.h
 * Purpose:  NI RF Signal Generator
 *           Instrument Driver declarations.
 *
 ****************************************************************************/

#ifndef ___niRFSG_niRFSG_h___
#define ___niRFSG_niRFSG_h___

#include <ivi.h>

#include <IviRFSigGen.h>

#ifdef _CVI_
   #pragma EnableLibraryRuntimeChecking
#endif


#if defined(__cplusplus) || defined(__cplusplus__)
   extern "C" {
#endif

// Bitness check for Supported Platforms
#if ((defined(_WIN32) || defined(WIN32)) && !defined(_WIN64))
   #define kRFSG_32BitPlatform 1
#elif defined(_WIN64) || (defined(__linux__) && defined(__x86_64__))
   #define kRFSG_64BitPlatform 1
#else
   #error "Unknown platform"
#endif

/****************************************************************************
 *---------------------------- Attribute Defines ---------------------------*
 ****************************************************************************/

/*- IVI Inherent Attributes ---------------------------------------------*/
   /*- User Options -*/
#define NIRFSG_ATTR_CACHE                                   /* ViBoolean */   IVIRFSIGGEN_ATTR_CACHE
#define NIRFSG_ATTR_RANGE_CHECK                             /* ViBoolean */   IVIRFSIGGEN_ATTR_RANGE_CHECK
#define NIRFSG_ATTR_QUERY_INSTRUMENT_STATUS                 /* ViBoolean */   IVIRFSIGGEN_ATTR_QUERY_INSTRUMENT_STATUS
#define NIRFSG_ATTR_RECORD_COERCIONS                        /* ViBoolean */   IVIRFSIGGEN_ATTR_RECORD_COERCIONS
#define NIRFSG_ATTR_SIMULATE                                /* ViBoolean */   IVIRFSIGGEN_ATTR_SIMULATE
#define NIRFSG_ATTR_INTERCHANGE_CHECK                       /* ViBoolean */   IVIRFSIGGEN_ATTR_INTERCHANGE_CHECK
#define NIRFSG_ATTR_SPY                                     /* ViBoolean */   IVIRFSIGGEN_ATTR_SPY
#define NIRFSG_ATTR_USE_SPECIFIC_SIMULATION                 /* ViBoolean */   IVIRFSIGGEN_ATTR_USE_SPECIFIC_SIMULATION

   /*- Instrument Capabilities, Read-only -*/
#define NIRFSG_ATTR_CHANNEL_COUNT                 /* ViInt32,  read-only */   IVIRFSIGGEN_ATTR_CHANNEL_COUNT
#define NIRFSG_ATTR_GROUP_CAPABILITIES            /* ViString, read-only */   IVIRFSIGGEN_ATTR_GROUP_CAPABILITIES
#define NIRFSG_ATTR_FUNCTION_CAPABILITIES         /* ViString, read-only */   IVIRFSIGGEN_ATTR_FUNCTION_CAPABILITIES

   /*- Specific Driver Information, Read-only -*/
#define NIRFSG_ATTR_SPECIFIC_DRIVER_PREFIX                   /* ViString */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_PREFIX
#define NIRFSG_ATTR_IO_RESOURCE_DESCRIPTOR                   /* ViString */   IVIRFSIGGEN_ATTR_IO_RESOURCE_DESCRIPTOR
#define NIRFSG_ATTR_LOGICAL_NAME                             /* ViString */   IVIRFSIGGEN_ATTR_LOGICAL_NAME
#define NIRFSG_ATTR_SPECIFIC_DRIVER_VENDOR                   /* ViString */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_VENDOR
#define NIRFSG_ATTR_SPECIFIC_DRIVER_DESCRIPTION              /* ViString */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION
#define NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION /* ViInt32  */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION
#define NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION /* ViInt32  */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION

   /*- Instrument Information -*/
#define NIRFSG_ATTR_INSTRUMENT_FIRMWARE_REVISION  /* ViString, read-only */   IVIRFSIGGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION
#define NIRFSG_ATTR_INSTRUMENT_MANUFACTURER       /* ViString, read-only */   IVIRFSIGGEN_ATTR_INSTRUMENT_MANUFACTURER
#define NIRFSG_ATTR_INSTRUMENT_MODEL              /* ViString, read-only */   IVIRFSIGGEN_ATTR_INSTRUMENT_MODEL
#define NIRFSG_ATTR_SUPPORTED_INSTRUMENT_MODELS   /* ViString, read-only */   IVIRFSIGGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS

   /*- Version Information -*/
#define NIRFSG_ATTR_SPECIFIC_DRIVER_REVISION      /* ViString, read-only */   IVIRFSIGGEN_ATTR_SPECIFIC_DRIVER_REVISION

   /*- Driver Setup information -*/
#define NIRFSG_ATTR_DRIVER_SETUP                             /* ViString */   IVIRFSIGGEN_ATTR_DRIVER_SETUP

/*- IVI Class-Specific Attributes ---------------------------------------*/

   /*- IviRFSigGen Fundamental Attributes -*/
#define NIRFSG_ATTR_FREQUENCY                               /* ViReal64  */   IVIRFSIGGEN_ATTR_FREQUENCY
#define NIRFSG_ATTR_POWER_LEVEL                             /* ViReal64  */   IVIRFSIGGEN_ATTR_POWER_LEVEL
#define NIRFSG_ATTR_OUTPUT_ENABLED                          /* ViBoolean */   IVIRFSIGGEN_ATTR_OUTPUT_ENABLED

   /*- IviRFSigGenReferenceOscillator Extension Group -*/
#define NIRFSG_ATTR_REF_CLOCK_RATE                          /* ViReal64  */   IVIRFSIGGEN_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY

   /*- IviRFSigGenModulateIQ Extension Group -*/
#define NIRFSG_ATTR_IQ_NOMINAL_VOLTAGE                      /* ViReal64  */   IVIRFSIGGEN_ATTR_IQ_NOMINAL_VOLTAGE
#define NIRFSG_ATTR_IQ_SWAP_ENABLED                         /* ViBoolean */   IVIRFSIGGEN_ATTR_IQ_SWAP_ENABLED

   /*- IviRFSigGenArbGenerator Extension Group -*/
#define NIRFSG_ATTR_ARB_SELECTED_WAVEFORM                   /* ViString  */   IVIRFSIGGEN_ATTR_ARB_SELECTED_WAVEFORM
#define NIRFSG_ATTR_IQ_RATE                                 /* ViReal64  */   IVIRFSIGGEN_ATTR_ARB_CLOCK_FREQUENCY
#define NIRFSG_ATTR_ARB_FILTER_FREQUENCY                    /* ViReal64  */   IVIRFSIGGEN_ATTR_ARB_FILTER_FREQUENCY
#define NIRFSG_ATTR_ARB_MAX_NUMBER_WAVEFORMS       /* ViInt32,  read-only */  IVIRFSIGGEN_ATTR_ARB_MAX_NUMBER_WAVEFORMS
#define NIRFSG_ATTR_ARB_WAVEFORM_QUANTUM           /* ViInt32,  read-only */  IVIRFSIGGEN_ATTR_ARB_WAVEFORM_QUANTUM
#define NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN          /* ViInt32,  read-only */  IVIRFSIGGEN_ATTR_ARB_WAVEFORM_SIZE_MIN
#define NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX          /* ViInt32,  read-only */  IVIRFSIGGEN_ATTR_ARB_WAVEFORM_SIZE_MAX
#define NIRFSG_ATTR_START_TRIGGER_TYPE                      /* ViInt32   */   IVIRFSIGGEN_ATTR_ARB_TRIGGER_SOURCE
#define NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE         /* ViInt32   */   IVIRFSIGGEN_ATTR_ARB_EXTERNAL_TRIGGER_SLOPE

   /*- Pulse Modulation -*/
#define NIRFSG_ATTR_PULSE_MODULATION_ENABLED                         /* ViBoolean */   IVIRFSIGGEN_ATTR_PULSE_MODULATION_ENABLED
#define NIRFSG_ATTR_PULSE_MODULATION_MODE                            /* ViInt32, read-write */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xbe)
#define NIRFSG_ATTR_PULSE_MODULATION_ACTIVE_LEVEL                    /* ViInt32, read-write */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x133)
#define NIRFSG_ATTR_PULSE_MODULATION_SOURCE                          /* ViString, read-write */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x134)
#define NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL  /* ViString, read-write */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x135)
#define NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL     /* ViInt32,  read-write */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x136)

/*- niRFSG Driver-Specific Attributes -----------------------------------*/

   /*- Fundamental Attributes (see IviRFSigGen Fundamental Attributes above) -*/
#define NIRFSG_ATTR_GENERATION_MODE                         /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x12)
#define NIRFSG_ATTR_POWER_LEVEL_TYPE                        /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2b)
#define NIRFSG_ATTR_PEAK_ENVELOPE_POWER           /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0b)

   /*- Arb Waveform (see IviRFSigGenArbGenerator Attributes above) -*/
#define NIRFSG_ATTR_SIGNAL_BANDWIDTH                        /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x07)
#define NIRFSG_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH          /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xe2)
#define NIRFSG_ATTR_DIRECT_DOWNLOAD                         /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2a)
#define NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR    /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x34)
#define NIRFSG_ATTR_FREQUENCY_TOLERANCE                     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x06)
#define NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED                /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x05)
#define NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED            /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0c)
#define NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE     /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9d)
#define NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT               /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9e)

   /*- Waveform Normalization -*/
#define NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION            /* ViInt32 */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x125)

   /*- Burst Detection -*/
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION                        /* ViInt32 */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x111)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE                   /* ViInt32 */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x112)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME     /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x113)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD        /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x114)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME     /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x115)

   /*- Instrument Information -*/
#define NIRFSG_ATTR_MEMORY_SIZE                  /* ViInt64, read-only   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3d)

   /*- Scripting -*/
#define NIRFSG_ATTR_SELECTED_SCRIPT                         /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x17)

   /*- Clocking -*/
#define NIRFSG_ATTR_REF_CLOCK_SOURCE                        /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x01)
#define NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL      /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x35)
#define NIRFSG_ATTR_EXPORTED_REF_CLOCK_RATE                 /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x124)
#define NIRFSG_ATTR_LO_OUT_ENABLED                          /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0d)
#define NIRFSG_ATTR_LO_OUT_POWER                            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x42)
#define NIRFSG_ATTR_LO_IN_POWER                             /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x43)
#define NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE                /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x04)
#define NIRFSG_ATTR_ARB_ONBOARD_SAMPLE_CLOCK_MODE           /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1d)
#define NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE                 /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1e)
#define NIRFSG_ATTR_ARB_SAMPLE_CLOCK_RATE         /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1f)
#define NIRFSG_ATTR_ARB_OSCILLATOR_PHASE_DAC_VALUE          /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x59)
#define NIRFSG_ATTR_REF_PLL_BANDWIDTH                       /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x85)
#define NIRFSG_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA       /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF2)
#define NIRFSG_ATTR_RF_IN_LO_EXPORT_ENABLED                 /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF3)

   /*- Analog Modulation -*/
#define NIRFSG_ATTR_ANALOG_MODULATION_TYPE                      /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x20)
#define NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_TYPE             /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x21)
#define NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_FREQUENCY        /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x22)
#define NIRFSG_ATTR_ANALOG_MODULATION_FM_DEVIATION              /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x23)
#define NIRFSG_ATTR_ANALOG_MODULATION_PM_DEVIATION              /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3e)
#define NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND                   /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xbf)
#define NIRFSG_ATTR_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR  /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xa5)
#define NIRFSG_ATTR_ANALOG_MODULATION_FM_SENSITIVITY            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xa6)
#define NIRFSG_ATTR_ANALOG_MODULATION_AM_SENSITIVITY            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xa7)
#define NIRFSG_ATTR_ANALOG_MODULATION_PM_SENSITIVITY            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xa8)
#define NIRFSG_ATTR_ANALOG_MODULATION_PM_MODE                   /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xc0)

   /*- Digital Modulation -*/
#define NIRFSG_ATTR_DIGITAL_MODULATION_TYPE                 /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x24)
#define NIRFSG_ATTR_DIGITAL_MODULATION_SYMBOL_RATE          /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x25)
#define NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE        /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x26)
#define NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_ORDER           /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x27)
#define NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_SEED            /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x28)
#define NIRFSG_ATTR_DIGITAL_MODULATION_FSK_DEVIATION        /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x29)

   /*- Arb Signal Processing -*/
#define NIRFSG_ATTR_ARB_PRE_FILTER_GAIN                     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x19)
#define NIRFSG_ATTR_ARB_FILTER_TYPE                         /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x38)
#define NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x39)
#define NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA          /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3c)

   /*- Attenuator Hold -*/
#define NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED                 /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x09)
#define NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER               /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0a)

   /*- Script Trigger -*/
#define NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE                                 /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x13)
#define NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE                  /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x14)
#define NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE                    /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x15)
#define NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE                 /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x36)
#define NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL           /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x37)
#define NIRFSG_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL             /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x16)
#define NIRFSG_ATTR_SCRIPT_TRIGGER_TERMINAL_NAME              /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x74)

   /*- Start Trigger (see IviRFSigGenArbGenerator Attributes above) -*/
#define NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE          /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x02)
#define NIRFSG_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL     /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x03)
#define NIRFSG_ATTR_START_TRIGGER_TERMINAL_NAME                /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x72)
#define NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL  /* ViInt64   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x80)

   /*- Done Event -*/
#define NIRFSG_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL                 /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3f)
#define NIRFSG_ATTR_DONE_EVENT_TERMINAL_NAME                  /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x71)

   /*- Marker Event -*/
#define NIRFSG_ATTR_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL               /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x40)
#define NIRFSG_ATTR_MARKER_EVENT_TERMINAL_NAME                          /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x73)
#define NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR                        /* ViInt32 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xce)
#define NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH                            /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xcf)
#define NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS                      /* ViInt32 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd0)
#define NIRFSG_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE                   /* ViInt32 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd1)

   /*- Started Event -*/
#define NIRFSG_ATTR_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL              /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x41)
#define NIRFSG_ATTR_STARTED_EVENT_TERMINAL_NAME               /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x70)

   /*- Configuration Settled Event -*/
#define NIRFSG_ATTR_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL   /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x81)
#define NIRFSG_ATTR_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME              /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xC2)

   /*- Data Transfer -*/
#define NIRFSG_ATTR_DATA_TRANSFER_BLOCK_SIZE                /* ViInt32   */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x30)
#define NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH         /* ViReal64  */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x56)
#define NIRFSG_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE     /* ViInt32   */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x57)
#define NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS   /* ViInt32   */        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x58)

   /*- Streaming -*/
#define NIRFSG_ATTR_STREAMING_ENABLED                       /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2d)
#define NIRFSG_ATTR_STREAMING_WAVEFORM_NAME                 /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2e)
#define NIRFSG_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM   /* ViInt64   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2f)
#define NIRFSG_ATTR_STREAMING_WRITE_TIMEOUT                 /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x8c)

   /*- Upconverter -*/
#define NIRFSG_ATTR_UPCONVERTER_GAIN                        /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1001)
#define NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1002)

   /*- Advanced -*/
#define NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS/* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0e)
#define NIRFSG_ATTR_ARB_CARRIER_FREQUENCY                   /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x0f)
#define NIRFSG_ATTR_ARB_DIGITAL_GAIN                        /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xcc)
#define NIRFSG_ATTR_ARB_POWER                     /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10)
#define NIRFSG_ATTR_DEVICE_TEMPERATURE            /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11)
#define NIRFSG_ATTR_ARB_TEMPERATURE               /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x44)
#define NIRFSG_ATTR_LO_TEMPERATURE                /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4b)
#define NIRFSG_ATTR_AE_TEMPERATURE                /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xb6)
#define NIRFSG_ATTR_FPGA_TEMPERATURE              /* ViReal64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd3)
#define NIRFSG_ATTR_TEMPERATURE_READ_INTERVAL               /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd4)
#define NIRFSG_ATTR_AUTOMATIC_THERMAL_CORRECTION            /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x08)
#define NIRFSG_ATTR_LOOP_BANDWIDTH                          /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1b)
#define NIRFSG_ATTR_FGEN_SESSION                 /* ViSession, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1c)
#define NIRFSG_ATTR_LO_SESSION                   /* ViSession, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4a)
#define NIRFSG_ATTR_AE_SESSION                   /* ViSession, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xb7)
#define NIRFSG_ATTR_DIGITAL_PATTERN                         /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x2c)
#define NIRFSG_ATTR_PHASE_OFFSET                            /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x18)
#define NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS                /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x52)
#define NIRFSG_ATTR_FREQUENCY_SETTLING                      /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x53)
#define NIRFSG_ATTR_AMPLITUDE_SETTLING                      /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x89)
#define NIRFSG_ATTR_EXTERNAL_GAIN                           /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x55)
#define NIRFSG_ATTR_YIG_MAIN_COIL_DRIVE                     /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x76)
#define NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT                   /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x84)
#define NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE       /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x8d)
#define NIRFSG_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY       /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xb10)
#define NIRFSG_ATTR_CORRECTION_TEMPERATURE                  /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x68)
#define NIRFSG_ATTR_ALC_CONTROL                             /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xc3)
#define NIRFSG_ATTR_AUTO_POWER_SEARCH                       /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xc4)
#define NIRFSG_ATTR_AMP_PATH                                /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xb9)
#define NIRFSG_ATTR_ATTENUATOR_SETTING                      /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xad)
#define NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING                /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xe4)
#define NIRFSG_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION  /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF4)
#define NIRFSG_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE          /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x102)
#define NIRFSG_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS          /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10F)
#define NIRFSG_ATTR_SELECTED_PORTS                          /* ViString */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF1)
#define NIRFSG_ATTR_AVAILABLE_PORTS                         /* ViString */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF9)
#define NIRFSG_ATTR_SELECTED_PATH                           /* ViString */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x137)
#define NIRFSG_ATTR_AVAILABLE_PATHS                         /* ViString */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x138)

   /*- IQ Impairments -*/
#define NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED                   /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x45)
#define NIRFSG_ATTR_IQ_OFFSET_UNITS                         /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x51)
#define NIRFSG_ATTR_IQ_I_OFFSET                             /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x46)
#define NIRFSG_ATTR_IQ_Q_OFFSET                             /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x47)
#define NIRFSG_ATTR_IQ_GAIN_IMBALANCE                       /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x48)
#define NIRFSG_ATTR_IQ_SKEW                                 /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x49)

   /*- Device Attributes -*/
#define NIRFSG_ATTR_SERIAL_NUMBER                /* ViString, read-only  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x1a)
#define NIRFSG_ATTR_MODULE_REVISION              /* ViString, read-only  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x54)
#define NIRFSG_ATTR_MODULE_POWER_CONSUMPTION     /* ViReal64, read-only  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd2)

#define NIRFSG_ATTR_FAST_TUNING_OPTION          /* ViBoolean, read-only  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xbc)

   /*- Calibration Attributes -*/
#define NIRFSG_ATTR_EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL       /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4c)
#define NIRFSG_ATTR_EXTERNAL_CALIBRATION_TEMPERATURE                /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4d)
#define NIRFSG_ATTR_SELF_CALIBRATION_TEMPERATURE                    /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x88)

   /*- Configuration List -*/
#define NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST                                         /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x60)
#define NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST_STEP                                    /* ViInt64   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x61)
#define NIRFSG_ATTR_CONFIGURATION_LIST_STEP_IN_PROGRESS                      /* ViInt64, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7a)
#define NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE                              /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x62)
#define NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE               /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x63)
#define NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE                 /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x67)
#define NIRFSG_ATTR_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL          /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x69)
#define NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME           /* ViString, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x75)
#define NIRFSG_ATTR_CONFIGURATION_LIST_REPEAT                                         /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x66)
#define NIRFSG_ATTR_CONFIGURATION_LIST_IS_DONE                             /* ViBoolean, read-only */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xAF)

   /*- Timer -*/
#define NIRFSG_ATTR_TIMER_EVENT_INTERVAL     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x64)

   /*- Peer-to-Peer (P2P) -*/
#define NIRFSG_ATTR_P2P_ENABLED                                      /* ViBoolean  */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7b)
#define NIRFSG_ATTR_P2P_ENDPOINT_SIZE                        /* ViInt64, read-only */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7c)
#define NIRFSG_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT          /* ViInt64, read-only */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7d)
#define NIRFSG_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT     /* ViInt64, read-only */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7e)
#define NIRFSG_ATTR_P2P_ENDPOINT_COUNT                       /* ViInt32, read-only */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x7f)
#define NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL               /* ViInt64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x86)
#define NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS        /* ViInt64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x87)
#define NIRFSG_ATTR_P2P_IS_FINITE_GENERATION                          /* ViBoolean */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xd9)
#define NIRFSG_ATTR_P2P_NUMBER_OF_SAMPLES_TO_GENERATE                   /* ViInt64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xda)
#define NIRFSG_ATTR_P2P_GENERATION_FIFO_SAMPLE_QUANTUM                  /* ViInt64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xdb)

/*- niRFSG Attribute Aliases --------------------------------------------*/

/* Attribute Aliases. The attribute names on the right (native names) are consistent
   with the names of their related Driver-Specific attributes.  The attribute names on
   the left (attribute aliases) are consistent with the IVI-defined attribute names.
   Either name can be used.  niRFSG (Driver-Specific) documentation and examples will
   use the names on the right (native names).
*/
#define NIRFSG_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY                   NIRFSG_ATTR_REF_CLOCK_RATE
#define NIRFSG_ATTR_ARB_CLOCK_FREQUENCY                                       NIRFSG_ATTR_IQ_RATE
#define NIRFSG_ATTR_ARB_TRIGGER_SOURCE                                        NIRFSG_ATTR_START_TRIGGER_TYPE
#define NIRFSG_ATTR_ARB_EXTERNAL_TRIGGER_SLOPE                                NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE


/****************************************************************************
 *--------- Device-Specific Attribute Defines (5644R/5645R/5646R) ----------*
 ****************************************************************************/

/*- Trigger Synchronization Attributes ---------------------------------------------*/
#define NIRFSG_ATTR_SYNC_START_TRIGGER_MASTER                          /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9B)
#define NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE                       /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9C)
#define NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_MASTER                         /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x8E)
#define NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_DIST_LINE                      /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x8F)
#define NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_MASTER                           /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xB4)
#define NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE                        /* ViString  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xB5)

/*- Events Attributes -------------------------------------------------------------*/
#define NIRFSG_ATTR_EVENTS_DELAY                                       /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9A)

/*- Signal Path Attributes ---------------------------------------------------------*/
#define NIRFSG_ATTR_INTERPOLATION_DELAY                                /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x99)
#define NIRFSG_ATTR_RELATIVE_DELAY                                     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xDC)
#define NIRFSG_ATTR_ABSOLUTE_DELAY                                     /* ViReal64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xE1)

/*- Output Port -------------------------------------------------------------------*/
#define NIRFSG_ATTR_OUTPUT_PORT                                        /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x90)

/*- LO control attributes ---------------------------------------------------------*/
#define NIRFSG_ATTR_LO_SOURCE                                          /* ViString */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x96)
#define NIRFSG_ATTR_LO_FREQUENCY                                       /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xC7)
#define NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE                             /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x97)
#define NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED                     /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x98)
#define NIRFSG_ATTR_LO_VCO_FREQUENCY_STEP_SIZE                         /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x101)

/*- IQ Out Port attributes --------------------------------------------------------*/
#define NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY                      /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x91)
#define NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION                 /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x92)
#define NIRFSG_ATTR_IQ_OUT_PORT_LEVEL                                  /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x93)
#define NIRFSG_ATTR_IQ_OUT_PORT_COMMON_MODE_OFFSET                     /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x94)
#define NIRFSG_ATTR_IQ_OUT_PORT_OFFSET                                 /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x95)
#define NIRFSG_ATTR_IQ_OUT_PORT_TEMPERATURE                            /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xA1)
#define NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE                         /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xA3)

/*- RF Blanking Attributes --------------------------------------------------------*/
#define NIRFSG_ATTR_RF_BLANKING_SOURCE                                 /* ViString  */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xA2)

/*- RF Upconverter attributes -----------------------------------------------------*/
#define NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE                  /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF8)
#define NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET                       /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xA0)

/*- FPGA Extensions attributes ----------------------------------------------------*/
#define NIRFSG_ATTR_FPGA_BITFILE_PATH                                  /* ViString */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xBA)
#define NIRFSG_ATTR_FPGA_TARGET_NAME                                   /* ViString */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFB)

/*- Host DMA Buffer Attributes ----------------------------------------------------*/
#define NIRFSG_ATTR_HOST_DMA_BUFFER_SIZE                               /* ViInt64  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xEF)

/*- De-embedding Attributes -------------------------------------------------------*/
#define NIRFSG_ATTR_DEEMBEDDING_TYPE                                   /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFC)
#define NIRFSG_ATTR_DEEMBEDDING_SELECTED_TABLE                         /* ViString */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFD)
#define NIRFSG_ATTR_DEEMBEDDING_COMPENSATION_GAIN                      /* ViReal64 */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x121)


/*- Per-Waveform Attributes. -------------------------------------------------------*/
#define NIRFSG_ATTR_WAVEFORM_IQ_RATE                           /* ViReal64 */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x107)
#define NIRFSG_ATTR_WAVEFORM_SIGNAL_BANDWIDTH                  /* ViReal64 */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x108)
#define NIRFSG_ATTR_WAVEFORM_RUNTIME_SCALING                   /* ViReal64 */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x109)
#define NIRFSG_ATTR_WAVEFORM_PAPR                              /* ViReal64 */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10A)
#define NIRFSG_ATTR_WAVEFORM_FILEPATH                          /* ViString, read only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x110)
#define NIRFSG_ATTR_WAVEFORM_RF_BLANKING                       /* ViInt32 */                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x116)
#define NIRFSG_ATTR_WAVEFORM_WAVEFORM_SIZE                     /* ViInt32 */                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x129)

/****************************************************************************
 *------ Device-Specific Attribute Value Defines (5644R/5645R/5646R) -------*
 ****************************************************************************/

/*- Values for NIRFSG_ATTR_OUTPUT_PORT */
#define NIRFSG_VAL_RF_OUT              14000
#define NIRFSG_VAL_IQ_OUT              14001
#define NIRFSG_VAL_CAL_OUT             14002
#define NIRFSG_VAL_I_ONLY              14003

/*- Values for niRFSG 5840 Lo Align Daisy Chain.vi in the niRFSG RF Port Type.ctl -*/
#define NIRFSG_VAL_PORT_RF_IN          14500
#define NIRFSG_VAL_PORT_RF_OUT         14501

/*- Values for NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION */
#define NIRFSG_VAL_DIFFERENTIAL        15000
#define NIRFSG_VAL_SINGLE_ENDED        15001

/*- Trigger Synchronization attribute values -*/
#define NIRFSG_VAL_SYNC_START_TRIGGER_STR               "Sync_Start"
#define NIRFSG_VAL_SYNC_SCRIPT_TRIGGER_STR              "Sync_Script"

/*- LO Source attribute values -*/
#define NIRFSG_VAL_LO_SOURCE_ONBOARD_STR                    "Onboard"
#define NIRFSG_VAL_LO_SOURCE_LO_IN_STR                      "LO_In"
#define NIRFSG_VAL_LO_SOURCE_SECONDARY_STR                  "Secondary"
#define NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR               "SG_SA_Shared"
#define NIRFSG_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED_STR     "Automatic_SG_SA_Shared"

/****************************************************************************
 *------------------------ Attribute Value Defines -------------------------*
 ****************************************************************************/

/*- Values for function WaitUntilSetttled -*/
#define NIRFSG_VAL_MAX_TIME_IMMEDIATE                                  IVIRFSIGGEN_VAL_MAX_TIME_IMMEDIATE
#define NIRFSG_VAL_MAX_TIME_INFINITE                                   IVIRFSIGGEN_VAL_MAX_TIME_INFINITE

/*- Values for attributes NIRFSG_ATTR_START_TRIGGER_TYPE and NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE -*/
#define NIRFSG_VAL_ARB_TRIGGER_SOURCE_IMMEDIATE                        NIRFSG_VAL_NONE
#define NIRFSG_VAL_ARB_TRIGGER_SOURCE_EXTERNAL                         NIRFSG_VAL_DIGITAL_EDGE
#define NIRFSG_VAL_ARB_TRIGGER_SOURCE_SOFTWARE                         NIRFSG_VAL_SOFTWARE

/*- Alias Values for attributes NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE and NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE -*/
#define NIRFSG_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_POSITIVE                 NIRFSG_VAL_RISING_EDGE
#define NIRFSG_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_NEGATIVE                 NIRFSG_VAL_FALLING_EDGE

/*- Values for boolean (enabled/disabled) attributes -*/
#define NIRFSG_VAL_ENABLE                       VI_TRUE
#define NIRFSG_VAL_DISABLE                      VI_FALSE

/*- Additional value for NIRFSG_ATTR_PHASE_CONTINUITY and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE */
#define NIRFSG_VAL_AUTO                         -1

/*-Enum value for attribute NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE. */
#define NIRFSG_VAL_MANUAL                       0

/*- Additional value for NIRFSG_ATTR_RF_IN_LO_EXPORT_ENABLED */
#define NIRFSG_VAL_UNSPECIFIED                  -2

/*- Values for NIRFSG_ATTR_START_TRIGGER_TYPE, NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE
    and NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE-*/
#define NIRFSG_VAL_NONE                         IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_IMMEDIATE
#define NIRFSG_VAL_DIGITAL_EDGE                 IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_EXTERNAL
#define NIRFSG_VAL_SOFTWARE                     IVIRFSIGGEN_VAL_ARB_TRIGGER_SOURCE_SOFTWARE

/*- Additional value for NIRFSG_ATTR_START_TRIGGER_TYPE */
#define NIRFSG_VAL_P2P_ENDPOINT_FULLNESS        3

/*- Additional value for NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE */
#define NIRFSG_VAL_DIGITAL_LEVEL                8000

/*- Values for NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE & NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE -*/
#define NIRFSG_VAL_RISING_EDGE                  IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_POSITIVE
#define NIRFSG_VAL_FALLING_EDGE                 IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_NEGATIVE

/*- Values for NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE */
/* #define NIRFSG_VAL_RISING_EDGE                  IVIRFSIGGEN_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_POSITIVE (Defined Elsewhere)*/

/*- Values for NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL */
#define NIRFSG_VAL_ACTIVE_HIGH                  9000
#define NIRFSG_VAL_ACTIVE_LOW                   9001

/*- Values for Signals -*/
#define NIRFSG_VAL_START_TRIGGER                      0
#define NIRFSG_VAL_SCRIPT_TRIGGER                     1
#define NIRFSG_VAL_MARKER_EVENT                       2
#define NIRFSG_VAL_REF_CLOCK                          3
#define NIRFSG_VAL_STARTED_EVENT                      4
#define NIRFSG_VAL_DONE_EVENT                         5
#define NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER    6
#define NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT        7

/*- Values for attributes NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE,
    NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE,
    NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE,
    NIRFSG_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL,
    and NIRFSG_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL -*/
#define NIRFSG_VAL_DO_NOT_EXPORT_STR            ""
#define NIRFSG_VAL_TRIG_IN_STR                  "TrigIn"
#define NIRFSG_VAL_TRIG_OUT_STR                 "TrigOut"
#define NIRFSG_VAL_PFI0_STR                     "PFI0"
#define NIRFSG_VAL_PFI1_STR                     "PFI1"
#define NIRFSG_VAL_PFI2_STR                     "PFI2"
#define NIRFSG_VAL_PFI3_STR                     "PFI3"
#define NIRFSG_VAL_PFI4_STR                     "PFI4"
#define NIRFSG_VAL_PFI5_STR                     "PFI5"
#define NIRFSG_VAL_PXI_TRIG0_STR                "PXI_Trig0"
#define NIRFSG_VAL_PXI_TRIG1_STR                "PXI_Trig1"
#define NIRFSG_VAL_PXI_TRIG2_STR                "PXI_Trig2"
#define NIRFSG_VAL_PXI_TRIG3_STR                "PXI_Trig3"
#define NIRFSG_VAL_PXI_TRIG4_STR                "PXI_Trig4"
#define NIRFSG_VAL_PXI_TRIG5_STR                "PXI_Trig5"
#define NIRFSG_VAL_PXI_TRIG6_STR                "PXI_Trig6"
#define NIRFSG_VAL_PXI_TRIG7_STR                "PXI_Trig7"
#define NIRFSG_VAL_PXI_STAR_STR                 "PXI_STAR"
#define NIRFSG_VAL_PXIE_DSTARB_STR              "PXIe_DStarB"
#define NIRFSG_VAL_PXIE_DSTARC_STR              "PXIe_DStarC"
#define NIRFSG_VAL_RTSI0_STR                    "RTSI0"
#define NIRFSG_VAL_RTSI1_STR                    "RTSI1"
#define NIRFSG_VAL_RTSI2_STR                    "RTSI2"
#define NIRFSG_VAL_RTSI3_STR                    "RTSI3"
#define NIRFSG_VAL_RTSI4_STR                    "RTSI4"
#define NIRFSG_VAL_RTSI5_STR                    "RTSI5"
#define NIRFSG_VAL_RTSI6_STR                    "RTSI6"
#define NIRFSG_VAL_RTSI7_STR                    "RTSI7"
#define NIRFSG_VAL_DIO0_STR                     "DIO/PFI0"
#define NIRFSG_VAL_DIO1_STR                     "DIO/PFI1"
#define NIRFSG_VAL_DIO2_STR                     "DIO/PFI2"
#define NIRFSG_VAL_DIO3_STR                     "DIO/PFI3"
#define NIRFSG_VAL_DIO4_STR                     "DIO/PFI4"
#define NIRFSG_VAL_DIO5_STR                     "DIO/PFI5"
#define NIRFSG_VAL_DIO6_STR                     "DIO/PFI6"
#define NIRFSG_VAL_DIO7_STR                     "DIO/PFI7"

/*- Values for NIRFSG_ATTR_REF_CLOCK_RATE -*/
#define NIRFSG_VAL_10MHz                        10000000
/* #define NIRFSG_VAL_AUTO                         -1     (Defined Elsewhere) */
/* NIRFSG_ATTR_REF_CLOCK_RATE can also accept any value that the underlying hardware supports */

/*- Additional values for NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE -*/
#define NIRFSG_VAL_TIMER_EVENT_STR              "TimerEvent"
#define NIRFSG_VAL_MARKER0_EVENT_STR            "Marker0Event"
#define NIRFSG_VAL_MARKER1_EVENT_STR            "Marker1Event"
#define NIRFSG_VAL_MARKER2_EVENT_STR            "Marker2Event"
#define NIRFSG_VAL_MARKER3_EVENT_STR            "Marker3Event"

/*- Values for attribute NIRFSG_ATTR_CONFIGURATION_LIST_REPEAT -*/
#define NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_CONTINUOUS          0
#define NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_SINGLE              1

/*- Values for attributes NIRFSG_ATTR_REF_CLOCK_SOURCE and NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE -*/
#define NIRFSG_VAL_ONBOARD_CLOCK_STR            "OnboardClock"
#define NIRFSG_VAL_REF_IN_STR                   "RefIn"
#define NIRFSG_VAL_PXI_CLK_STR                  "PXI_CLK"
#define NIRFSG_VAL_NONE_STR                     "None"
#define NIRFSG_VAL_REF_IN_2_STR                 "RefIn2"
#define NIRFSG_VAL_PXI_CLK_MASTER_STR           "PXI_ClkMaster"
/* #define NIRFSG_VAL_CLK_IN_STR                "ClkIn" (Defined Elsewhere)*/

/*- Values for NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL -*/
#define NIRFSG_VAL_REF_OUT_STR                  "RefOut"
#define NIRFSG_VAL_REF_OUT2_STR                 "RefOut2"
#define NIRFSG_VAL_CLK_OUT_STR                  "ClkOut"
/* #define NIRFSG_VAL_DO_NOT_EXPORT_STR         ""        (Defined Elsewhere)*/

/* Values for signal names */
#define NIRFSG_VAL_SCRIPT_TRIGGER0              "scriptTrigger0"
#define NIRFSG_VAL_SCRIPT_TRIGGER1              "scriptTrigger1"
#define NIRFSG_VAL_SCRIPT_TRIGGER2              "scriptTrigger2"
#define NIRFSG_VAL_SCRIPT_TRIGGER3              "scriptTrigger3"
#define NIRFSG_VAL_MARKER0                      "marker0"
#define NIRFSG_VAL_MARKER1                      "marker1"
#define NIRFSG_VAL_MARKER2                      "marker2"
#define NIRFSG_VAL_MARKER3                      "marker3"

/* Values for endpoint names */
#define NIRFSG_VAL_P2P_ENDPOINT0                "FIFOEndpoint0"

/*- Values for attribute NIRFSG_ATTR_GENERATION_MODE -*/
#define NIRFSG_VAL_CW                           1000
#define NIRFSG_VAL_ARB_WAVEFORM                 1001
#define NIRFSG_VAL_SCRIPT                       1002

/*- Values for attribute NIRFSG_ATTR_LOOP_BANDWIDTH, NIRFSG_ATTR_REF_PLL_BANDWIDTH,
    and NIRFSG_ATTR_ANALOG_MODULATION_PM_LOOP_BANDWIDTH  -*/
#define NIRFSG_VAL_NARROW                       0
#define NIRFSG_VAL_MEDIUM                       1
#define NIRFSG_VAL_WIDE                         2

/*- Values for attribute NIRFSG_ATTR_YIG_MAIN_COIL_DRIVE -*/
#define NIRFSG_VAL_SLOW                         0
#define NIRFSG_VAL_FAST                         1

/*- Values for attribute NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE -*/
/* #define NIRFSG_VAL_ONBOARD_CLOCK_STR         "OnboardClock" (Defined Elsewhere)*/
#define NIRFSG_VAL_CLK_IN_STR                   "ClkIn"

/*- Values for attribute NIRFSG_ATTR_ANALOG_MODULATION_TYPE -*/
/* #define NIRFSG_VAL_NONE                      0     (Defined Elsewhere)*/
#define NIRFSG_VAL_FM                           2000
#define NIRFSG_VAL_PM                           2001
#define NIRFSG_VAL_AM                           2002

/*- Values for attribute NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_TYPE -*/
#define NIRFSG_VAL_SINE                         3000
#define NIRFSG_VAL_SQUARE                       3001
#define NIRFSG_VAL_TRIANGLE                     3002

/*- Values for attribute NIRFSG_ATTR_DIGITAL_MODULATION_TYPE -*/
/* #define NIRFSG_VAL_NONE                         0     (Defined Elsewhere)*/
#define NIRFSG_VAL_FSK                          4000
#define NIRFSG_VAL_OOK                          4001
#define NIRFSG_VAL_PSK                          4002

/*- Values for attribute NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE;
    NIRFSG_VAL_USER_DEFINED is also for NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE -*/
#define NIRFSG_VAL_PRBS                         5000
#define NIRFSG_VAL_USER_DEFINED                 5001

/*- Values for attribute NIRFSG_ATTR_ARB_ONBOARD_SAMPLE_CLOCK_MODE -*/
#define NIRFSG_VAL_HIGH_RESOLUTION              6000
#define NIRFSG_VAL_DIVIDE_DOWN                  6001

/*- Values for attribute NIRFSG_ATTR_POWER_LEVEL_TYPE -*/
#define NIRFSG_VAL_AVERAGE_POWER                7000
#define NIRFSG_VAL_PEAK_POWER                   7001

/*- Values for niRFSG_SetArbWaveformNextWritePosition relativeTo -*/
#define NIRFSG_VAL_START_OF_WAVEFORM            8000
#define NIRFSG_VAL_CURRENT_POSITION             8001

/*- Values for attribute NIRFSG_ATTR_ARB_FILTER_TYPE -*/
#define NIRFSG_VAL_ARB_FILTER_TYPE_NONE                10000
#define NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE  10001
#define NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE       10002

/*- Values for attribute NIRFSG_ATTR_IQ_OFFSET_UNITS -*/
#define NIRFSG_VAL_PERCENT                      11000
#define NIRFSG_VAL_VOLTS                        11001

/*- Values for attribute NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS -*/
#define NIRFSG_VAL_TIME_AFTER_LOCK              12000
#define NIRFSG_VAL_TIME_AFTER_IO                12001
#define NIRFSG_VAL_PPM                          12002

/*- Values for Modules -*/
#define NIRFSG_VAL_PRIMARY_MODULE               13000
#define NIRFSG_VAL_AWG                          13001
#define NIRFSG_VAL_LO                           13002

/*- Values for attribute NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE -*/
#define NIRFSG_VAL_EXACT_MATCH                  0
#define NIRFSG_VAL_MINIMUM                      1
#define NIRFSG_VAL_MAXIMUM                      2

/*- Values for attribute NIRFSG_ATTR_AMP_PATH -*/
#define NIRFSG_VAL_HIGH_POWER                   16000
#define NIRFSG_VAL_LOW_HARMONIC                 16001

/*- Values for attribute NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND -*/
#define NIRFSG_VAL_NARROWBAND                   17000
#define NIRFSG_VAL_WIDEBAND                     17001

/*- Values for attribute NIRFSG_ATTR_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR -*/
#define NIRFSG_VAL_100HZ_TO_1KHZ                18000
#define NIRFSG_VAL_1KHZ_TO_10KHZ                18001
#define NIRFSG_VAL_10KHZ_TO_100KHZ              18002

/*- Values for attribute NIRFSG_ATTR_ANALOG_MODULATION_PM_MODE -*/
#define NIRFSG_VAL_HIGH_DEVIATION               19000
#define NIRFSG_VAL_LOW_PHASE_NOISE              19001

/*- Values for attribute NIRFSG_ATTR_PULSE_MODULATION_MODE -*/
#define NIRFSG_VAL_OPTIMAL_MATCH                20000
#define NIRFSG_VAL_HIGH_ISOLATION               20001
#define NIRFSG_VAL_PULSE_MODULATION_ANALOG      20002
#define NIRFSG_VAL_PULSE_MODULATION_DIGITAL     20003
#define NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION   NIRFSG_VAL_HIGH_ISOLATION

/*- Values for attribute NIRFSG_ATTR_PULSE_MODULATION_SOURCE -*/
#define NIRFSG_VAL_PULSE_IN_STR                 "PulseIn"

/*- Values for attribute NIRFSG_ATTR_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL -*/
#define NIRFSG_VAL_PULSE_OUT_STR                "PulseOut"

/*- Values for attribute NIRFSG_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE -*/
#define NIRFSG_VAL_DIGITAL_LOW                  21000
#define NIRFSG_VAL_DIGITAL_HIGH                 21001

/*- Values for attribute NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS -*/
#define NIRFSG_VAL_SECONDS                      22000
#define NIRFSG_VAL_SAMPLE_CLOCK_PERIODS         22001

/*- Values for attribute NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR -*/
#define NIRFSG_VAL_PULSE                        23000
#define NIRFSG_VAL_TOGGLE                       23001

/*- Values for S-parameters orientation passed to Create De-embedding S-parameter Table functions -*/
#define NIRFSG_VAL_PORT1_TOWARDS_DUT            24000
#define NIRFSG_VAL_PORT2_TOWARDS_DUT            24001

/*- Values for NIRFSG_ATTR_DEEMBEDDING_TYPE attribute -*/
#define NIRFSG_VAL_DEEMBEDDING_TYPE_NONE        25000
#define NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR      25001
#define NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR      25002

/*- Values for niRFSG_ConfigureDeembeddingTableInterpolationLinear -*/
#define NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY      26000
#define NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE     26001
#define NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE  26002

// Values for NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE
/* #define NIRFSG_VAL_AUTO                         -1      (Defined Elsewhere) */
/* #define NIRFSG_VAL_USER_DEFINED                 5001    (Defined Elsewhere) */
/* #define NIRFSG_VAL_ENABLE                       VI_TRUE (Defined Elsewhere) */

/*- Values for attribute NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING -*/
#define NIRFSG_VAL_ERROR_REPORTING_WARNING      1301
#define NIRFSG_VAL_ERROR_REPORTING_DISABLED     1302

/*- Values for niRFSG_SelfCalibrateRange stepsToOmit -*/
#define NIRFSG_VAL_SELF_CAL_OMIT_NONE               0x0000000000000000
#define NIRFSG_VAL_SELF_CAL_LO_SELF_CAL             0x0000000000000001
#define NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY    0x0000000000000002
#define NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER       0x0000000000000004
#define NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION       0x0000000000000008
#define NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT   0x0000000000000010

/*- Values for niRFSG_ResetWithOptions stepsToOmit -*/
#define NIRFSG_VAL_RESET_WITH_OPTIONS_NONE               0x0ULL // reset everything
#define NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS          0x1ULL
#define NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS            0x2ULL
#define NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES             0x4ULL
#define NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES 0x8ULL

#define NIRFSG_MAX_ERROR_MESSAGE_SIZE           1024

/*- Enum values for Load Configuration Load Skip Options -*/
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE       0
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS  1

/*- Enum values for Load Configuration Reset Skip Options. Keeping the values same as the enum values for niRFSG_ResetWithOptions -*/
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE                0x0ULL
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS           0x1ULL
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS             0x2ULL
#define RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES  0x8ULL

/*-Enum value for attribute NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE. */
/* #define NIRFSG_VAL_AUTO                        -1      (Defined Elsewhere) */
/* #define NIRFSG_VAL_MANUAL                       0      (Defined Elsewhere) */

/****************************************************************************
 *---------------- Instrument Driver struct definititions  -----------------*
 ****************************************************************************/

/*- Use with:
      niRFSG_WriteArbWaveformComplexF64
*/
#if !defined(_NIComplexNumber)
typedef struct NIComplexNumber_struct {
   ViReal64 real;
   ViReal64 imaginary;
} NIComplexNumber;
#define _NIComplexNumber
#endif

/*- Use with:
      niRFSG_WriteArbWaveformComplexF32
*/
#if !defined(_NIComplexNumberF32)
#define _NIComplexNumberF32

#if kRFSG_32BitPlatform
   #pragma pack(push, 1)
#elif kRFSG_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

typedef struct NIComplexNumberF32_struct {
   ViReal32 real;
   ViReal32 imaginary;
} NIComplexNumberF32;

#if kRFSG_32BitPlatform
   #pragma pack(pop)
#elif kRFSG_64BitPlatform
   // Nothing needed for 64 bit platforms
#else
   #error Unknown Platform
#endif

#endif
/*- Use with:
      niRFSG_WriteArbWaveformComplexI16
*/
#if !defined(_NIComplexI16)
typedef struct NIComplexI16_struct {
   ViInt16 real;
   ViInt16 imaginary;
} NIComplexI16;
#define _NIComplexI16
#endif

/****************************************************************************
 *---------------- Instrument Driver Function Declarations -----------------*
 ****************************************************************************/

/*- Init and Close Functions -----------------------------------------------*/
ViStatus _VI_FUNC niRFSG_init
(
   ViRsrc      resourceName,
   ViBoolean   IDQuery,
   ViBoolean   resetDevice,
   ViSession*  newVi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_InitWithOptions
(
   ViRsrc        resourceName,
   ViBoolean     IDQuery,
   ViBoolean     resetDevice,
   ViConstString optionString,
   ViSession*    newVi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_close
(
   ViSession vi
);
/*- RFSigGenBase Functions -------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_ConfigureRF
(
   ViSession   vi,
   ViReal64    frequency,
   ViReal64    powerLevel
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigurePowerLevelType
(
   ViSession vi,
   ViInt32 powerLevelType
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DisableAllModulation
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_WaitUntilSettled
(
   ViSession   vi,
   ViInt32     maxTimeMilliseconds
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureOutputEnabled
(
   ViSession vi,
   ViBoolean outputEnabled
);

/*- Control Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_Commit
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_Initiate
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_Abort
(
   ViSession vi
);

/*- Arb Generator Functions ------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_AllocateArbWaveform
(
   ViSession      vi,
   ViConstString  waveformName,
   ViInt32        sizeInSamples
);

ViStatus _VI_FUNC niRFSG_WriteArbWaveform
(
   ViSession      vi,
   ViConstString  waveformName,
   ViInt32        numberOfSamples,
   const ViReal64 iData[],
   const ViReal64 qData[],
   ViBoolean      moreDataPending
);

ViStatus _VI_FUNC niRFSG_WriteArbWaveformF32
(
   ViSession      vi,
   ViConstString  waveformName,
   ViInt32        numberOfSamples,
   const ViReal32 iData[],
   const ViReal32 qData[],
   ViBoolean      moreDataPending
);

ViStatus _VI_FUNC niRFSG_WriteArbWaveformComplexF64
(
   ViSession               vi,
   ViConstString           waveformName,
   ViInt32                 numberOfSamples,
   const NIComplexNumber   wfmData[],
   ViBoolean               moreDataPending
);

ViStatus _VI_FUNC niRFSG_WriteArbWaveformComplexF32
(
   ViSession                vi,
   ViConstString            waveformName,
   ViInt32                  numberOfSamples,
   const NIComplexNumberF32 wfmData[],
   ViBoolean                moreDataPending
);

ViStatus _VI_FUNC niRFSG_WriteArbWaveformComplexI16
(
   ViSession            vi,
   ViConstString        waveformName,
   ViInt32              numberOfSamples,
   const NIComplexI16   wfmData[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ReadAndDownloadWaveformFromFileTDMS
(
   ViSession vi,
   ViConstString waveformName,
   ViConstString filePath,
   ViUInt32 waveformIndex
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetArbWaveformNextWritePosition
(
   ViSession vi,
   ViConstString waveformName,
   ViInt32 relativeTo,
   ViInt32 offset
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ClearArbWaveform
(
   ViSession      vi,
   ViConstString  name
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SelectArbWaveform
(
   ViSession      vi,
   ViConstString  name
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ClearAllArbWaveforms
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_QueryArbWaveformCapabilities
(
   ViSession   vi,
   ViInt32*    maxNumberWaveforms,
   ViInt32*    waveformQuantum,
   ViInt32*    minWaveformSize,
   ViInt32*    maxWaveformSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureSignalBandwidth
(
   ViSession vi,
   ViReal64 signalBandwidth
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CheckIfWaveformExists
(
   ViSession vi,
   ViConstString waveformName,
   ViBoolean* waveformExists
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CheckIfScriptExists
(
   ViSession vi,
   ViConstString scriptName,
   ViBoolean* scriptExists
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetWaveformBurstStartLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetWaveformBurstStartLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations,
   ViInt32* requiredSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetWaveformBurstStopLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetWaveformBurstStopLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations,
   ViInt32* requiredSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetWaveformMarkerEventLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetWaveformMarkerEventLocations
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 numberOfLocations,
   ViReal64* locations,
   ViInt32* requiredSize
);
/*- Configuration List Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_CreateConfigurationList
(
   ViSession      vi,
   ViConstString  listName,
   ViInt32        numberOfAttributes,
   const ViAttr   configurationListAttributes[],
   ViBoolean      setAsActiveList
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CreateConfigurationListStep
(
   ViSession      vi,
   ViBoolean      setAsActiveStep
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DeleteConfigurationList
(
   ViSession      vi,
   ViConstString  listName
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CheckIfConfigurationListExists
(
   ViSession vi,
   ViConstString listName,
   ViBoolean* listExists
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/

/*- Trigger Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_SendSoftwareEdgeTrigger
(
   ViSession      vi,
   ViInt32        trigger,
   ViConstString  triggerIdentifier
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureDigitalEdgeStartTrigger
(
   ViSession      vi,
   ViConstString  source,
   ViInt32        edge
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureP2PEndpointFullnessStartTrigger
(
   ViSession vi,
   ViInt64 p2pEndpointFullnessLevel
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DisableStartTrigger
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureSoftwareStartTrigger
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger
(
   ViSession      vi,
   ViConstString  source,
   ViInt32        edge
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DisableConfigurationListStepTrigger
(
   ViSession vi
);

/*- Clocking Functions -----------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_ConfigureRefClock
(
   ViSession      vi,
   ViConstString  refClockSource,
   ViReal64       refClockRate
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigurePXIChassisClk10
(
   ViSession      vi,
   ViConstString  pxiClk10Source
);

/*- Scripting Functions ----------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_ConfigureGenerationMode
(
   ViSession   vi,
   ViInt32     generationMode
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_WriteScript
(
   ViSession      vi,
   ViConstString  script
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DeleteScript
(
   ViSession vi,
   ViConstString scriptName
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureDigitalEdgeScriptTrigger
(
   ViSession      vi,
   ViConstString  triggerID,
   ViConstString  source,
   ViInt32        edge
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureDigitalLevelScriptTrigger
(
   ViSession      vi,
   ViConstString  triggerID,
   ViConstString  source,
   ViInt32        level
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_DisableScriptTrigger
(
   ViSession      vi,
   ViConstString  triggerID
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureSoftwareScriptTrigger
(
   ViSession      vi,
   ViConstString  triggerID
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ExportSignal
(
   ViSession      vi,
   ViInt32        signal,
   ViConstString  signalIdentifier,
   ViConstString  outputTerminal
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetTerminalName
(
   ViSession      vi,
   ViInt32        signal,
   ViConstString  signalIdentifier,
   ViInt32        bufferSize,
   ViChar         terminalName[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetAllScriptNames
(
   ViSession  vi,
   ViChar     scriptNames[],
   ViInt32    bufferSize,
   ViInt32*   actualBufferSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetScript
(
    ViSession vi,
    ViConstString scriptName,
    ViChar script[],
    ViInt32 bufferSize,
    ViInt32* actualBufferSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetAllNamedWaveformNames
(
   ViSession  vi,
   ViChar     waveformNames[],
   ViInt32    bufferSize,
   ViInt32*   actualBufferSize
);

/*- Peer-to-Peer (P2P) Functions -------------------------------------------*/
ViStatus _VI_FUNC niRFSG_GetStreamEndpointHandle
(
   ViSession      vi,
   ViConstString  streamEndpoint,
   ViUInt32*      readerHandle
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_WriteP2PEndpointI16
(
   ViSession vi,
   ViConstString streamEndpoint,
   ViInt32 numberOfSamples,
   ViInt16 endpointData[]
);
/*- Instrument Specific Functions ------------------------------------------*/
ViStatus _VI_FUNC niRFSG_CheckGenerationStatus
(
   ViSession  vi,
   ViBoolean* isDone
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureUpconverterPLLSettlingTime
(
   ViSession   vi,
   ViReal64    pllSettlingTime,
   ViBoolean   ensurePLLLocked,
   ViInt32     reservedForFutureUse    /* pass 0 */
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureDigitalModulationUserDefinedWaveform
(
   ViSession vi,
   ViInt32 numberOfSamples,
   const ViInt8 userDefinedWaveform[]
);

/*- Channel Info Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_GetChannelName
(
   ViSession vi,
   ViInt32 index,
   ViInt32 bufferSize,
   ViChar name[]
);

/*- Utility Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_reset
(
   ViSession vi
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ResetAttribute
(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ResetDevice
(
   ViSession vi
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ResetWithDefaults
(
   ViSession vi
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ResetWithOptions
(
   ViSession vi,
   ViUInt64 stepsToOmit
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SaveConfigurationsToFile
(
   ViSession vi,
   ViConstString channelName,
   ViConstString filePath
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_LoadConfigurationsFromFile
(
   ViSession vi,
   ViConstString channelName,
   ViConstString filePath
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_InvalidateAllAttributes
(
   ViSession vi
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetUserData
(
   ViSession vi,
   ViConstString identifier,
   ViInt32 bufferSize,
   ViInt8 data[]
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetUserData
(
   ViSession vi,
   ViConstString identifier,
   ViInt32 bufferSize,
   ViInt8 data[],
   ViInt32* actualDataSize
);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_self_test
(
   ViSession   vi,
   ViInt16*    selfTestResult,
   ViChar      selfTestMessage[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ChangeExternalCalibrationPassword
(
   ViSession      vi,
   ViConstString  oldPassword,
   ViConstString  newPassword
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetExternalCalibrationLastDateAndTime
(
   ViSession      vi,
   ViInt32*       year,
   ViInt32*       month,
   ViInt32*       day,
   ViInt32*       hour,
   ViInt32*       minute,
   ViInt32*       second
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetSelfCalibrationDateAndTime
(
   ViSession      vi,
   ViInt32        module,
   ViInt32*       year,
   ViInt32*       month,
   ViInt32*       day,
   ViInt32*       hour,
   ViInt32*       minute,
   ViInt32*       second
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetSelfCalibrationTemperature
(
   ViSession      vi,
   ViInt32        module,
   ViReal64*      temperature
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ClearSelfCalibrateRange
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_revision_query
(
   ViSession   vi,
   ViChar      instrumentDriverRevision[],
   ViChar      firmwareRevision[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_Disable
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_PerformThermalCorrection
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_PerformPowerSearch
(
   ViSession vi
);
/*- Error Functions --------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_error_query
(
   ViSession   vi,
   ViInt32*    errorCode,
   ViChar      errorMessage[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ClearError
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_error_message
(
   ViSession   vi,
   ViStatus    errorCode,
   ViChar      errorMessage[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetError
(
   ViSession   vi,
   ViStatus*   errorCode,
   ViInt32     errorDescriptionBufferSize,
   ViChar      errorDescription[]
);

/*- Calibration Functions --------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_SelfCal
(
   ViSession   vi
);

ViStatus _VI_FUNC niRFSG_SelfCalibrateRange
(
   ViSession vi,
   ViInt64   stepsToOmit,
   ViReal64  minFrequency,
   ViReal64  maxFrequency,
   ViReal64  minPowerLevel,
   ViReal64  maxPowerLevel
);

ViStatus _VI_FUNC niRFSG_5840_AlignLODaisyChain
(
   ViBoolean      useExternalLo,
   ViRsrc         externalLo,
   ViConstString  resourceNames, // comma separated
   ViInt32        portTypesLen,
   ViInt32        *portTypes,
   ViReal64       startFrequency,
   ViReal64       stopFrequency
);

/*- Locking Functions ------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_LockSession
(
   ViSession   vi,
   ViBoolean*  callerHasLock
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_UnlockSession
(
   ViSession   vi,
   ViBoolean*  callerHasLock
);

/*- Set, Get, and Check Attribute Functions --------------------------------*/
ViStatus _VI_FUNC niRFSG_GetAttributeViInt32 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 *value);
ViStatus _VI_FUNC niRFSG_GetAttributeViInt64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt64 *value);
ViStatus _VI_FUNC niRFSG_GetAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 *value);
ViStatus _VI_FUNC niRFSG_GetAttributeViString (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 bufSize, ViChar value[]);
ViStatus _VI_FUNC niRFSG_GetAttributeViSession (ViSession vi, ViConstString channelName, ViAttr attribute, ViSession *value);
ViStatus _VI_FUNC niRFSG_GetAttributeViBoolean (ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean *value);

ViStatus _VI_FUNC niRFSG_SetAttributeViInt32 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 value);
ViStatus _VI_FUNC niRFSG_SetAttributeViInt64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt64 value);
ViStatus _VI_FUNC niRFSG_SetAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 value);
ViStatus _VI_FUNC niRFSG_SetAttributeViString (ViSession vi, ViConstString channelName, ViAttr attribute, ViConstString value);
ViStatus _VI_FUNC niRFSG_SetAttributeViSession (ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value);
ViStatus _VI_FUNC niRFSG_SetAttributeViBoolean (ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value);

ViStatus _VI_FUNC niRFSG_CheckAttributeViInt32 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt32 value);
ViStatus _VI_FUNC niRFSG_CheckAttributeViInt64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViInt64 value);
ViStatus _VI_FUNC niRFSG_CheckAttributeViReal64 (ViSession vi, ViConstString channelName, ViAttr attribute, ViReal64 value);
ViStatus _VI_FUNC niRFSG_CheckAttributeViString (ViSession vi, ViConstString channelName, ViAttr attribute, ViConstString value);
ViStatus _VI_FUNC niRFSG_CheckAttributeViSession (ViSession vi, ViConstString channelName, ViAttr attribute, ViSession value);
ViStatus _VI_FUNC niRFSG_CheckAttributeViBoolean (ViSession vi, ViConstString channelName, ViAttr attribute, ViBoolean value);

ViStatus _VI_FUNC niRFSG_GetMaxSettablePower (ViSession vi, ViReal64 *value);

/*- Sparameter de-embedding API --------------------------------------------*/
ViStatus _VI_FUNC niRFSG_CreateDeembeddingSparameterTableS2PFile(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   ViConstString s2pFilePath,
   ViInt32 sparameterOrientation);

ViStatus _VI_FUNC niRFSG_CreateDeembeddingSparameterTableArray(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   const ViReal64 frequencies[], ViInt32 frequenciesSize,
   const NIComplexNumber sparameterTable[], ViInt32 sparameterTableSize,
   ViInt32 numberOfPorts,
   ViInt32 sparameterOrientation);

ViStatus _VI_FUNC niRFSG_DeleteDeembeddingTable(
   ViSession vi,
   ViConstString port,
   ViConstString tableName);

ViStatus _VI_FUNC niRFSG_DeleteAllDeembeddingTables(
   ViSession vi);

ViStatus _VI_FUNC niRFSG_ConfigureDeembeddingTableInterpolationNearest
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName
);

ViStatus _VI_FUNC niRFSG_ConfigureDeembeddingTableInterpolationLinear
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   ViInt32 format
);

ViStatus _VI_FUNC niRFSG_ConfigureDeembeddingTableInterpolationSpline
(
   ViSession vi,
   ViConstString port,
   ViConstString tableName
);

ViStatus _VI_FUNC niRFSG_GetDeembeddingSparameters
(
   ViSession vi,
   NIComplexNumber *sparameters, ViInt32 sparametersArraySize,
   ViInt32 *numberOfSparameters,
   ViInt32 *numberOfPorts
);

/****************************************************************************
 *------------------------ Error And Completion Codes ----------------------*
 ****************************************************************************/
#include "niRFSGErrors.h"

// IVI_SPECIFIC_ERROR_BASE == 0xbffa4000
#define NIRFSG_ERROR_BASE (IVI_SPECIFIC_ERROR_BASE + 0x3ff)

// IVI_SPECIFIC_WARN_BASE == 0x3ffa4000
#define NIRFSG_WARN_BASE (IVI_SPECIFIC_WARN_BASE + 0x3ff)

/****************************************************************************
 *---------------------------- End Include File ----------------------------*
 ****************************************************************************/
#include "niRFSGObsolete.h"

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif /* ___niRFSG_niRFSG_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSGErrors.h sha256=302d3bbeb3772a583c3ed50507db9f14fd55412cb2085031c5b7952d64ea8cfe bytes=32773 -->
## FILE: imports/include/niRFSGErrors.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSGErrors.h`
- sha256: `302d3bbeb3772a583c3ed50507db9f14fd55412cb2085031c5b7952d64ea8cfe`
- bytes: 32773

````c
#ifndef ___niRFSG_niRFSGErrors_h___
#define ___niRFSG_niRFSGErrors_h___

/*******************************/
/*********** Errors ************/
/*******************************/

/* hex: 0xBFFA43FF */
/* Session is not usable. If you are using multiple threads, this error may have been caused by attempting to use the session closed in a different thread. */
#define NIRFSG_ERROR_INVALID_SESSION -1074117633

/* hex: 0xBFFA43FE */
/* Unable to initialize because a session for the specified device is already open from another process. Close on the open session by calling niRFSG Close or by exiting the application with the open session. */
#define NIRFSG_ERROR_PREVIOUS_SESSION -1074117634

/* hex: 0xBFFA43FD */
/* Invalid resource name. Note: if the resource name is an IVI Logical name, it must match the entry in the IVI Configuration Store in a case sensitive manner. */
#define NIRFSG_ERROR_INVALID_RESOURCE_NAME -1074117635

/* hex: 0xBFFA43FC */
/* The device specified is not supported by this driver. */
#define NIRFSG_ERROR_DEVICE_NOT_SUPPORTED -1074117636

/* hex: 0xBFFA43FB */
/* Operation failed because the signal generator is not in the Configuration state. Call niRFSG Abort prior to making this call. */
#define NIRFSG_ERROR_NOT_CONFIGURABLE -1074117637

/* hex: 0xBFFA43FA */
/* Operation failed because the signal generator is not in the Generation state. Call niRFSG Initiate prior to making this call. */
#define NIRFSG_ERROR_NOT_GENERATING -1074117638

/* hex: 0xBFFA43F9 */
/* The maximum number of waveforms has been reached. To write more waveforms, clear already written waveforms by using niRFSG Clear All Waveforms. To find out the maximum number of supported waveforms, call niRFSG Query ARB Waveform Capabilities. */
#define NIRFSG_ERROR_EXCEEDED_MAX_WAVEFORMS -1074117639

/* hex: 0xBFFA43F8 */
/* Invalid IQ Rate. */
#define NIRFSG_ERROR_INVALID_IQ_RATE -1074117640

/* hex: 0xBFFA43F7 */
/* Invalid waveform. */
#define NIRFSG_ERROR_INVALID_WAVEFORM -1074117641

/* hex: 0xBFFA43F6 */
/* The combination of the specified Reference Clock Source and PXI Clk Source is not supported. Refer to the documentation for more information. */
#define NIRFSG_ERROR_CLOCK_CONFIGURATION_NOT_SUPPORTED -1074117642

/* hex: 0xBFFA43F5 */
/* The trigger configuration specified is not supported. Refer to the documentation for more information. */
#define NIRFSG_ERROR_INVALID_TRIGGER_CONFIGURATION -1074117643

/* hex: 0xBFFA43F4 */
/* The 'DriverSetup' entry in the Option String is invalid. */
#define NIRFSG_ERROR_DRIVER_SETUP_SYNTAX -1074117644

/* hex: 0xBFFA43F3 */
/* Operation failed because the signal generator is not in the Committed state. Call niRFSG Commit or niRFSG Initiate prior to making this call. */
#define NIRFSG_ERROR_NOT_COMMITTED -1074117645

/* hex: 0xBFFA43F2 */
/* The signal generator's waveform memory is full. */
#define NIRFSG_ERROR_NO_WFMS_AVAILABLE -1074117646

/* hex: 0xBFFA43F1 */
/* The specified digital equalization coefficients are not supported. */
#define NIRFSG_ERROR_INVALID_FILTER -1074117647

/* hex: 0xBFFA43EF */
/* Hardware error has occurred. Frequency PLL did not lock in the expected amount of time. Execute Self Test and Self Cal in MAX, or contact NI technical support at ni.com/support */
#define NIRFSG_ERROR_FREQUENCY_NOT_SETTLED -1074117649

/* hex: 0xBFFA43EE */
/* Hardware error has occurred. Output Gain did not settle in the expected amount of time. Execute Self Test and Self Cal in MAX, or contact NI technical support at ni.com/support */
#define NIRFSG_ERROR_ATTENUATION_NOT_SETTLED -1074117650

/* hex: 0xBFFA43ED */
/* Hardware error has occurred. Debounce Timer for Reverse Power Protection Relay did not expire in the expected amount of time. Execute Self Test in MAX, or contact NI technical support at ni.com/support */
#define NIRFSG_ERROR_REVERSE_POWER_PROTECTION -1074117651

/* hex: 0xBFFA43EC */
/* A session cannot be created because the maximum number of session is already open. To open a new session, close one of the existing sessions by calling niRFSG Close. */
#define NIRFSG_ERROR_MAX_SESSIONS_EXCEEDED -1074117652

/* hex: 0xBFFA43EA */
/* A session cannot be created because the AWG resource name is invalid. Verify the AWG resource name in MAX by selecting the upconverter and specifying the AWG name within the Associated Devices section. If you are specifying the AWG via the Option String, ensure the AWG resource name is valid. */
#define NIRFSG_ERROR_INVALID_AWG_RESOURCE_NAME -1074117654

/* hex: 0xBFFA43E9 */
/* The requested Power Level requires a Peak Envelope Power (PEP) that exceeds the device specifications. */
#define NIRFSG_ERROR_PEP_OUT_OF_RANGE -1074117655

/* hex: 0xBFFA43E8 */
/* Initialization failed because another session with conflicting initialization options is already open for this device. Call niRFSG Close on the opened session, or close and reopen the application. */
#define NIRFSG_ERROR_PREVIOUS_CONFLICTING_SESSION -1074117656

/* hex: 0xBFFA43E7 */
/* The reservedForFutureUse parameter must be 0. */
#define NIRFSG_ERROR_RESERVED_PARAMETER_NOT_ZERO -1074117657

/* hex: 0xBFFA43E6 */
/* Requested Power Level requires an AWG Gain that exceeds device limits. Ensure the requested Power Level is within device specifications. */
#define NIRFSG_ERROR_ARB_GAIN_PAST_LIMIT -1074117658

/* hex: 0xBFFA43E5 */
/* Invalid or unsupported model specified. Note: Valid values for model include 5610, 5611, 5650, 5651,  5652, 5653, 5670, 5671, 5672, 5673 and 5673E. Valid values for AWG include 5421, 5441, 5442, 5450, and 5451. Valid values for LO include 5650, 5651 and 5652. */
#define NIRFSG_ERROR_MODEL_NOT_RECOGNIZED -1074117659

/* hex: 0xBFFA43E4 */
/* Invalid or unsupported product number specified. */
#define NIRFSG_ERROR_PRODUCT_NUMBER_NOT_RECOGNIZED -1074117660

/* hex: 0xBFFA43E3 */
/* The specified generation mode is invalid. */
#define NIRFSG_ERROR_INVALID_GENERATION_MODE -1074117661

/* hex: 0xBFFA43E2 */
/* Invalid waveform size. The waveform size must be a multiple of the waveform quantum. */
#define NIRFSG_ERROR_WFM_QUANTUM_VIOLATION -1074117662

/* hex: 0xBFFA43E1 */
/* Invalid waveform size. */
#define NIRFSG_ERROR_WFM_SIZE_VIOLATION -1074117663

/* hex: 0xBFFA43E0 */
/* The specified waveform has not been completed. The waveform was last written with 'more Data Pending' marked true. */
#define NIRFSG_ERROR_INCOMPLETE_WAVEFORM -1074117664

/* hex: 0xBFFA43DF */
/* You are using script generation mode, but no scripts have been written. */
#define NIRFSG_ERROR_NO_SCRIPTS_WRITTEN -1074117665

/* hex: 0xBFFA43DE */
/* Invalid Power Level Type. */
#define NIRFSG_ERROR_INVALID_POWER_LEVEL_TYPE -1074117666

/* hex: 0xBFFA43DD */
/* This combination of attributes is not supported. */
#define NIRFSG_ERROR_INVALID_CONFIGURATION -1074117667

/* hex: 0xBFFA43DC */
/* The specified signal identifier is invalid for this signal. */
#define NIRFSG_ERROR_INVALID_SIGNAL_IDENTIFIER -1074117668

/* hex: 0xBFFA43DB */
/* Maximum time exceeded before the operation completed. */
#define NIRFSG_ERROR_MAX_TIME_EXCEEDED -1074117669

/* hex: 0xBFFA43DA */
/* Invalid waveform size. Since each I-Q sample consists of two array elements, the total number of array elements needs to be even. */
#define NIRFSG_ERROR_INVALID_NUMBER_OF_IQ_SAMPLES -1074117670

/* hex: 0xBFFA43D9 */
/* A session cannot be created because the LO resource name is invalid. Verify the LO resource name in MAX by selecting the upconverter and specifying the LO name within the Associated Devices section. If you are specifying the LO via the Option String, ensure the LO resource name is valid. */
#define NIRFSG_ERROR_INVALID_LO_RESOURCE_NAME -1074117671

/* hex: 0xBFFA43D8 */
/* Failed to communicate with the RF processing module. Contact NI technical support at ni.com/support */
#define NIRFSG_ERROR_RF_MODULE_COMMUNICATION_FAILURE -1074117672

/* hex: 0xBFFA43D7 */
/* The device is in an invalid state for self test. Call reset before calling self test. */
#define NIRFSG_ERROR_INVALID_STATE_FOR_SELFTEST -1074117673

/* hex: 0xBFFA43D6 */
/* This device does not support the specified driver setup keyword. */
#define NIRFSG_ERROR_DRIVER_SETUP_KEYWORD_NOT_SUPPORTED -1074117674

/* hex: 0xBFFA43D5 */
/* A session cannot be created because the AWG resource name is invalid. Verify the AWG resource name in MAX by selecting the upconverter and specifying the AWG name within the Associated Devices section.<LF/><LF/>If you are specifying the AWG via the Option String, ensure the AWG resource name is valid and supported by this upconverter. The NI 5610 upconverter supports the NI PXI-5421, NI PXI-5441, and NI PXIe-5442 AWGs. The NI 5611 upconverter supports the NI PXIe-5450 and NI-PXIe-5451 AWGs. */
#define NIRFSG_ERROR_ARB_NOT_SUPPORTED -1074117675

/* hex: 0xBFFA43D4 */
/* You cannot use Streaming in CW mode. Change the generation mode to Arb Waveform or Script to use Streaming. */
#define NIRFSG_ERROR_STREAMING_NOT_SUPPORTED_IN_CW_MODE -1074117676

/* hex: 0xBFFA43D3 */
/* After the session was created, the driver DLL was unloaded and then reloaded at a different base address.  Session is unusable.  Unload all instances of the driver DLL and verify that previous operations do not unload the driver DLL. */
#define NIRFSG_ERROR_DLL_LOADED_AT_DIFFERENT_BASE_ADDRESS -1074117677

/* hex: 0xBFFA43D2 */
/* An IQ Rate of 50 MS/s is only valid when the signal bandwidth is less than 5 MHz. */
#define NIRFSG_ERROR_INVALID_IQ_RATE_AND_BANDWIDTH_CONFIGURATION -1074117678

/* hex: 0xBFFA43D1 */
/* Values must be set in increments of 1MHz. */
#define NIRFSG_ERROR_VALUE_MUST_BE_MULTIPLE_OF_1MHZ -1074117679

/* hex: 0xBFFA43D0 */
/* You cannot change the Power Level Type or Normalization property if you have already allocated one or more waveforms. Either use the previous Power Level Type/normalization property value or clear your waveforms. */
#define NIRFSG_ERROR_POWER_LEVEL_TYPE_CHANGED_DURING_RECONFIGURATION -1074117680

/* hex: 0xBFFA43CF */
/* This function is not supported when the Power Level Type is set to Average Power. Either change the Power Level Type to Peak Power or use a different write function. */
#define NIRFSG_ERROR_AVERAGE_POWER_NOT_SUPPORTED_FOR_BINARY_WRITE -1074117681

/* hex: 0xBFFA43CE */
/* You are trying to query a Streaming property without enabling Streaming. Set Streaming Enabled to True before your query. */
#define NIRFSG_ERROR_STREAMING_NOT_ENABLED -1074117682

/* hex: 0xBFFA43CD */
/* You have not specified which waveform to generate. */
#define NIRFSG_ERROR_WAVEFORM_NOT_SELECTED -1074117683

/* hex: 0xBFFA43CC */
/* You cannot call write multiple times on the same waveform name with the Power Level Type set to Average Power or Normalization set to Enabled. You must set Power Level Type to Peak Power or Normalization property to Disabled to append data to a previously written waveform. */
#define NIRFSG_ERROR_WRITING_IN_CHUNKS_NOT_SUPPORTED_WITH_AVERAGE_POWER -1074117684

/* hex: 0xBFFA43CB */
/* NaN, +Inf, and -Inf are not valid values. */
#define NIRFSG_ERROR_VALUE_CANNOT_BE_INF_OR_NAN -1074117685

/* hex: 0xBFFA43CA */
/* The value must be nonzero. */
#define NIRFSG_ERROR_VALUE_MUST_BE_NONZERO -1074117686

/* hex: 0xBFFA43C9 */
/* You are using Digital Equalization with Direct Download enabled. Either disable Digital Equalization or disable Direct Download. */
#define NIRFSG_ERROR_DIGITAL_EQUALIZATION_NOT_SUPPORTED_WITH_DIRECT_DOWNLOAD -1074117687

/* hex: 0xBFFA43C8 */
/* You are using Direct Download to download a waveform without allocating the waveform.  Call niRFSG Allocate Arb Waveform to allocate the waveform prior to making this call. */
#define NIRFSG_ERROR_ALLOCATE_NOT_CALLED_WITH_DIRECT_DOWNLOAD_ENABLED -1074117688

/* hex: 0xBFFA43C7 */
/* You are using Direct Download with the Average Power as the Power Level Type.  Either change the Power Level Type to Peak Power or disable Direct Download. */
#define NIRFSG_ERROR_DIRECT_DOWNLOAD_INVALID_WITH_AVERAGE_POWER -1074117689

/* hex: 0xBFFA43C6 */
/* You are using IQ Swap Enabled with Direct Download enabled.  Either disable IQ Swap or disable Direct Download. */
#define NIRFSG_ERROR_IQ_SWAP_NOT_SUPPORTED_WITH_DIRECT_DOWNLOAD -1074117690

/* hex: 0xBFFA43C5 */
/* This device does not support resetting attributes. */
#define NIRFSG_ERROR_RESETTING_ATTRIBUTES_NOT_SUPPORTED -1074117691

/* hex: 0xBFFA43C4 */
/* Resetting this attribute is not supported. */
#define NIRFSG_ERROR_RESETTING_THIS_ATTRIBUTE_NOT_SUPPORTED -1074117692

/* hex: 0xBFFA43C3 */
/* Scripts are not supported when the Phase Continuity Enabled attribute is enabled. */
#define NIRFSG_ERROR_SCRIPT_MODE_WITH_PHASE_CONTINUITY -1074117693

/* hex: 0xBFFA43C2 */
/* Your waveform data is invalid.  The magnitude of the I-Q signal multiplied by the scaling factor should be less than or equal to 1. */
#define NIRFSG_ERROR_IQ_MAGNITUDE_PAST_LIMIT -1074117694

/* hex: 0xBFFA43C1 */
/* You cannot query Peak Envelope Power with the Power Level Type set to Peak Power. */
#define NIRFSG_ERROR_PEAK_ENVELOPE_POWER_NOT_SUPPORTED_WITH_PEAK_POWER -1074117695

/* hex: 0xBFFA43C0 */
/* Function not supported in Script Mode. */
#define NIRFSG_ERROR_FUNCTION_NOT_SUPPORTED_IN_SCRIPT_MODE -1074117696

/* hex: 0xBFFA43BF */
/* RFDAP reported the following error: */
#define NIRFSG_ERROR_RFDAP_ERROR -1074117697

/* hex: 0xBFFA43BE */
/* Self calibration failed.  Contact NI technical support at ni.com/support. */
#define NIRFSG_ERROR_SELF_CAL_FAILED_CONTACT_SUPPORT -1074117698

/* hex: 0xBFFA43BD */
/* Self calibration failed to converge.  Performing an external calibration may fix the problem. */
#define NIRFSG_ERROR_SELF_CAL_FAILED_TO_CONVERGE -1074117699

/* hex: 0xBFFA43BC */
/* Self calibration failed.  Performing an external calibration may fix the problem. */
#define NIRFSG_ERROR_SELF_CAL_FAILED_TRY_EXT_CAL -1074117700

/* hex: 0xBFFA43BB */
/* A power supply fault has been detected.  Reset the device to clear the fault.  If the fault occurs again contact NI technical support at ni.com/support. */
#define NIRFSG_ERROR_POWER_SUPPLY_FAULT -1074117701

/* hex: 0xBFFA43B9 */
/* You cannot specify multiple channels or repeated capabilities. */
#define NIRSFG_ERROR_MULTIPLE_REPEATED_CAPABILITY_NOT_ALLOWED -1074117703

/* hex: 0xBFFA43B8 */
/* The frequency cannot be changed while attenuator hold is enabled. */
#define NIRFSG_ERROR_CHANGE_FREQUENCY_IN_ATTENUATOR_HOLD -1074117704

/* hex: 0xBFFA43B7 */
/* The Filter Type must be set to None when the Digital Upconverter is disabled. Either change the Filter Type to None or change the IQ Rate to enable the Digital Upconverter. */
#define NIRFSG_ERROR_INVALID_FILTER_TYPE_WITH_DUC_DISABLED -1074117705

/* hex: 0xBFFA43B6 */
/* You are using Direct Download with the Digital Upconverter disabled. Either change the IQ Rate to enable the Digital Upconverter or disable Direct Download. */
#define NIRFSG_ERROR_DIRECT_DOWNLOAD_INVALID_WITH_DUC_DISABLED -1074117706

/* hex: 0xBFFA43B5 */
/* The size of the sine pattern needed to achieve the specified frequency with the specified precision is too large. Either increase the tolerance or modify the center frequency. */
#define NIRFSG_ERROR_SIZE_SINE_PATTERN -1074117707

/* hex: 0xBFFA43B4 */
/* Requested Power Level requires an AWG Gain that exceeds device limits. When Attenuator Hold is enabled, the Power Level must be in the range (Attenuator Hold Max Power - 70, Attenuator Hold Max Power). */
#define NIRFSG_ERROR_ARB_GAIN_PAST_LIMIT_WITH_ATTENUATOR_HOLD -1074117708

/* hex: 0xBFFA43B3 */
/* IQ Rates greater than 25 MS/s and less than 42.5 MS/s and rates greater than 50 MS/s and less than 85 MS/s are only supported when the Arb Sample Clock Source is set to OnboardClock and the Arb Sample Clock Mode is set to Divide Down. */
#define NIRFSG_ERROR_INVALID_IQ_RATE_FOR_NON_DIVIDE_DOWN_MODES -1074117709

/* hex: 0xBFFA43B2 */
/* You have at least one waveform that has not been configured with the same value as the current value of Direct Download. */
#define NIRFSG_ERROR_ALL_WAVEFORMS_NOT_DOWNLOADED_IN_THE_SAME_MODE -1074117710

/* hex: 0xBFFA43B1 */
/* The qData may be an empty array to indicate the absence of qData. However, when writing a waveform in segments (moreDataPending = true), you cannot alternate between setting the qData to an empty array and setting it to specific values. */
#define NIRFSG_ERROR_VECTOR_Q_USAGE -1074117711

/* hex: 0xBFFA43B0 */
/* INF (infinite) or NaN (Not a Number) values encountered while making calculations based on waveform data.  Waveform may contain INF or NaN values, or the scale of the waveform data may be too large or too small. */
#define NIRFSG_ERROR_NAN_OR_INF_FROM_IQ_CALCULATION -1074117712

/* hex: 0xBFFA43AF */
/* You must allocate and write your waveform with direct download set to the same value. */
#define NIRFSG_ERROR_WAVEFORM_WRITE_ALLOCATE_DIRECT_DOWNLOAD_MISMATCH -1074117713

/* hex: 0xBFFA43AE */
/* This function is not supported when using an external AWG. */
#define NIRFSG_ERROR_FUNCTION_NOT_SUPPORTED_WITH_EXTERNAL_AWG -1074117714

/* hex: 0xBFFA43AD */
/* The signal is outside of the upconverter passband. */
#define NIRFSG_ERROR_SIGNAL_OUTSIDE_PASSBAND -1074117715

/* hex: 0xBFFA43AC */
/* You cannot set the Power Level Type to Average Power in Script Mode.  Either change the Power Level Type to Peak Power or use the Arb Waveform Mode. */
#define NIRFSG_ERROR_AVERAGE_POWER_INVALID_IN_SCRIPT_MODE -1074117716

/* hex: 0xBFFA43AB */
/* The instrument driver does not support changing the value of the Simulation property after the session is created.  Use the Option String to configure the instrument driver for simulation. */
#define NIRFSG_ERROR_SIMULATION_NOT_WRITABLE -1074117717

/* hex: 0xBFFA43AA */
/* No waveforms were found.  The current configuration requires at least one waveform. */
#define NIRFSG_ERROR_NO_WAVEFORM_EXISTS -1074117718

/* hex: 0xBFFA43A9 */
/* The version of TClk NI-FGEN is using is not compatible with the NI-RFSG version.  Install the version of NI-FGEN that came with NI-RFSG. */
#define NIRFSG_ERROR_INCOMPATIBLE_ARB_TCLK_PROTOCOL -1074117719

/* hex: 0xBFFA43A8 */
/* The requested signal type is not valid. */
#define NIRFSG_ERROR_INVALID_SIGNAL_TYPE -1074117720

/* hex: 0xBFFA43A7 */
/* The Reference Clock is not a valid signal type for this operation. */
#define NIRFSG_ERROR_REF_CLOCK_INVALID_SIGNAL_TYPE -1074117721

/* hex: 0xBFFA43A6 */
/* The specified BoardType is not supported by the specified LO. The NI 5650/5651/5652 LO supported BoardTypes are PXI and PXIe. The NI 5653 LO supported BoardType is PXIe. */
#define NIRFSG_ERROR_BOARDTYPE_NOT_SUPPORTED -1074117722

/* hex: 0xBFFA43A5 */
/* The specified LOBoardType is not supported. The valid LOBoardTypes are PXI and PXIe. */
#define NIRFSG_ERROR_LO_BOARDTYPE_NOT_SUPPORTED -1074117723

/* hex: 0xBFFA43A4 */
/* The specified LO is not supported by the specified upconverter. The NI 5611 upconverter supported LOs include the NI PXI-5650, NI PXI-5651, NI PXI-5652, NI PXIe-5650, NI PXIe-5651, and NI PXIe-5652. */
#define NIRFSG_ERROR_LO_NOT_SUPPORTED -1074117724

/* hex: 0xBFFA43A3 */
/* The model you specified for simulation automatically selects the appropiate AWG. If you want to use a different AWG, specify the corresponding model or use the upconverter model and manually specify the AWG you want to use. */
#define NIRFSG_ERROR_DRIVER_AWG_KEYWORD_NOT_SUPPORTED -1074117725

/* hex: 0xBFFA43A2 */
/* The following attributes cannot be set simultaneously. */
#define NIRFSG_ERROR_CONFLICTING_CONFIGURATION -1074117726

/* hex: 0xBFFA43A1 */
/* Calibration is not supported on simulated devices. */
#define NIRFSG_ERROR_CALIBRATION_SESSION_NOT_SUPPORTED_IN_SIMULATION -1074117727

/* hex: 0xBFFA43A0 */
/* The session was closed, but the calibration data was not updated.  You must use niRFSG Close External Calibration to close your calibration session and save your calibration data. */
#define NIRFSG_ERROR_WRONG_CLOSE_FOR_CAL_SESSION -1074117728

/* hex: 0xBFFA439F */
/* A PLL lock error occurred.<LF/><LF/>If you are using an external reference, make sure it is connected and meets the frequency accuracy and voltage level requirements.  Also make sure the device has fully warmed up. */
#define NIRFSG_ERROR_PLL_LOCK -1074117729

/* hex: 0xBFFA439E */
/* Streaming does not work in Average Power mode. Change the power level type to Peak Power to use streaming. */
#define NIRFSG_ERROR_AVERAGE_POWER_INVALID_WITH_STREAMING -1074117730

/* hex: 0xBFFA439D */
/* Performing sets or gets on the non-active context while the device is running is not allowed. */
#define NIRFSG_ERROR_NON_ACTIVE_CONTEXT_WHILE_RUNNING -1074117731

/* hex: 0xBFFA439C */
/* The values the script is trying to inherit from the waveforms are incompatible with each other. */
#define NIRFSG_ERROR_INCOMPATIBLE_SCRIPT_INHERITANCE -1074117732

/* hex: 0xBFFA439B */
/* Changing the value to or from the special value while the device is running is not allowed. */
#define NIRFSG_ERROR_SPECIAL_VALUE_WHILE_RUNNING -1074117733

/* hex: 0xBFFA439A */
/* Resetting an attribute with a context is not allowed. */
#define NIRFSG_ERROR_WAVEFORM_ATTRIBUTE_AND_RESET_ATTRIBUTE -1074117734

/* hex: 0xBFFA4399 */
/* The peer-to-peer endpoint is not available on the FPGA bitfile for your device. This may be caused by renaming or removing the peer-to-peer FIFO on the bitfile. */
#define NIRFSG_ERROR_ENDPOINT_NOT_AVAILABLE -1074117735

/* hex: 0xBFFA4398 */
/* A session cannot be created because the AE resource name is invalid. Verify the AE resource name in MAX by selecting the NI 5654 in the configuration tree and specifying the AE name within the Associated Devices section. If you specify the AE using the Option String, ensure the AE resource name is valid. */
#define NIRFSG_ERROR_INVALID_AE_RESOURCE_NAME -1074117736

/* hex: 0xBFFA4397 */
/* This function is not supported when an AE is not associated. */
#define NIRFSG_ERROR_FUNCTION_NOT_SUPPORTED_IF_AE_IS_NOT_ASSOCIATED -1074117737

/* hex: 0xBFFA4396 */
/* The niRFSG Perform Power Search function is not supported when the output is disabled. */
#define NIRFSG_ERROR_PWR_SEARCH_NOT_SUPPORTED_IF_OUTPUT_IS_DISABLED -1074117738

/* hex: 0xBFFA4395 */
/* The niRFSG Perform Power Search function is not supported when the ALC Control property is enabled. */
#define NIRFSG_ERROR_PWR_SEARCH_NOT_SUPPORTED_IF_ALC_IS_ENABLED -1074117739

/* hex: 0xBFFA4394 */
/* Modulation is not supported when the ALC Control property is enabled. */
#define NIRFSG_ERROR_MODULATION_NOT_SUPPORTED_IF_ALC_IS_ENABLED -1074117740

/* hex: 0xBFFA4393 */
/* The configured Reference Clock rate does not match the actual Reference Clock rate detected by the device. */
#define NIRFSG_ERROR_CONFIGURED_REF_CLOCK_RATE_NOT_MATCHING_ACTUAL_REF_CLOCK_RATE -1074117741

/* hex: 0xBFFA4392 */
/* The number of attributes specified does not match the number of values provided. */
#define NIRFSG_ERROR_LIST_MODE_NUMBER_OF_ATTRIBUTES_NOT_MATCHING_NUMBER_OF_VALUES -1074117742

/* hex: 0xBFFA4391 */
/* The configuration list data provided cannot be null or empty. */
#define NIRFSG_ERROR_LIST_MODE_CONFIGURATION_LIST_DATA_CANNOT_BE_NULL_OR_EMPTY -1074117743

/* hex: 0xBFFA4390 */
/* A trigger source must be specified for the given trigger type. */
#define NIRFSG_ERROR_TRIGGER_SOURCE_NOT_SPECIFIED -1074117744

/* hex: 0xBFFA438F */
/* Attempted to initiate a generation session with multiple scripts without selecting a script to generate.  Use the Selected Script property to specify a script for the device to execute. */
#define NIRFSG_ERROR_ACTIVE_SCRIPT_NOT_SPECIFIED -1074117745

/* hex: 0xBFFA438E */
/* The endpoint name is invalid. The syntax for valid endpoint names is FIFOEndpointN, where N is an integer that represents the endpoint. 0 represents the first endpoint. */
#define NIRFSG_ERROR_INVALID_ENDPOINT_NAME -1074117746

/* hex: 0xBFFA438D */
/* An underflow occurred during the peer-to-peer stream. Ensure the writer endpoint is writing data at a high enough rate to keep up with generation. */
#define NIRFSG_ERROR_P2P_UNDERFLOW -1074117747

/* hex: 0xBFFA438C */
/* The LO alignment procedure failed because the power at the LO IN terminal is too high. */
#define NIRFSG_ERROR_LO_ALIGNMENT_LO_IN_POWER_TOO_HIGH -1074117748

/* hex: 0xBFFA438B */
/* The LO alignment procedure failed because the power at the LO IN terminal is too low. */
#define NIRFSG_ERROR_LO_ALIGNMENT_LO_IN_POWER_TOO_LOW -1074117749

/* hex: 0xBFFA438A */
/* LO alignment is not supported for configurations where the RF input LO OUT is connected to the RF output LO IN on the same module. */
#define NIRFSG_ERROR_LO_ALIGNMENT_SA_EXPORT_TO_SG_ON_SAME_MODULE -1074117750

/* hex: 0xBFFA4389 */
/* Set the following waveform attribute to continue. */
#define NIRFSG_ERROR_WAVEFORM_ATTRIBUTE_NOT_SET -1074117751

/* hex: 0xBFFA4388 */
/* An interaction with TDMS has caused the following error */
#define NIRFSG_ERROR_TDMS_INTERACTION_FAILED -1074117752

/* hex: 0xBFFA4387 */
/* Waveform file version is not supported. Minimum supported version is 2.0.0. */
#define NIRFSG_ERROR_WAVEFORM_FILE_VERSION_NOT_SUPPORTED -1074117753

/* hex: 0xBFFA4386 */
/* Waveform data must be interleaved I and Q samples. */
#define NIRFSG_ERROR_WAVEFORM_DATA_NOT_INTERLEAVED_I_Q -1074117754

/* hex: 0xBFFA4385 */
/* Waveform data type not supported. */
#define NIRFSG_ERROR_WAVEFORM_DATA_TYPE_NOT_SUPPORTED -1074117755

/* hex: 0xBFFA4384 */
/* One or more required waveform properties are missing in the waveform file. */
#define NIRFSG_ERROR_WAVEFORM_PROPERTY_MISSING_FROM_FILE -1074117756

/* hex: 0xBFFA4383 */
/* Number of RF blanking marker positions present in the waveform file is invalid. RF blanking marker positions should always be in pairs. */
#define NIRFSG_ERROR_INVALID_RF_BLANKING_POSITIONS -1074117757

/* hex: 0xBFFA4382 */
/* Marker event locations must be whole numbers. */
#define NIRFSG_ERROR_INVALID_MARKER_EVENT_LOCATIONS -1074117758

/* hex: 0xBFFA4381 */
/* Burst Start Locations and Burst Stop Locations must be in ascending order. */
#define NIRFSG_ERROR_BURST_LOCATIONS_NOT_IN_ASCENDING_ORDER -1074117759

/* hex: 0xBFFA4380 */
/* Burst Start Locations and Burst Stop Locations must be whole numbers. */
#define NIRFSG_ERROR_BURST_LOCATIONS_NOT_WHOLE_NUMBERS -1074117760

/* hex: 0xBFFA437F */
/* Burst Start Locations and Burst Stop Locations must be less than waveform size. */
#define NIRFSG_ERROR_BURST_LOCATIONS_OUTSIDE_WAVEFORM -1074117761

/* hex: 0xBFFA437E */
/* Burst Start Locations count must be equal to or greater than Burst Stop Locations count by 1. */
#define NIRFSG_ERROR_INVALID_BURST_LOCATIONS -1074117762

/* hex: 0xBFFA437D */
/* Burst Start and Stop Locations should be configured to perform blanking. */
#define NIRFSG_ERROR_BURST_LOCATIONS_NOT_CONFIGURED -1074117763

/* hex: 0xBFFA437C */
/* Burst Start Locations must be less than the corresponding Burst Stop Locations. */
#define NIRFSG_ERROR_BURST_START_LOCATION_GREATER_THAN_BURST_STOP_LOCATION -1074117764

/* hex: 0xBFFA437B */
/* The driver version saved in the file is higher than the current installed driver. */
#define NIRFSG_ERROR_INCOMPATIBLE_DRIVER_VERSION -1074117765

/* hex: 0xBFFA437A */
/* Loading configuration is not allowed while session is running. */
#define NIRFSG_ERROR_LOAD_WHILE_SESSION_IS_RUNNING -1074117766

/*********************************/
/*********** Warnings ************/
/*********************************/

/* hex: 0x3FFA43ED */
/* Waveform could not be downloaded. */
#define NIRFSG_WARN_READ_AND_DOWNLOAD_UNSUCCESSFUL 1073365997

/* hex: 0x3FFA43EE */
/* Waveform filepath is invalid. */
#define NIRFSG_WARN_INVALID_WAVEFORM_FILEPATH 1073365998

/* hex: 0x3FFA43EF */
/* Calibration constants stored in the EEPROM are missing or invalid. The device will continue to function, but the accuracy of the measurements may be compromised. This may be due to an incorrect calibration or corrupted calibration data in the EEPROM. Perform either an external calibration, self-calibration, or contact NI technical support. */
#define NIRFSG_WARN_CALIBRATION_DATA_NOT_PRESENT 1073365999

/* hex: 0x3FFA43F0 */
/* Unable to correct for temperature deviation. The power level accuracy is not guaranteed. Re-commit the settings to regain accuracy. */
#define NIRFSG_WARN_TEMPERATURE_DEVIATION_LIMIT_EXCEEDED 1073366000

/* hex: 0x3FFA43F1 */
/* Overflow detected in the Arb's Digital Gain circuit. Output waveform was clipped. Reduce the Arb Pre Filter Gain to eliminate overflow. */
#define NIRFSG_WARN_ARB_OVERFLOW_DIGITAL_GAIN 1073366001

/* hex: 0x3FFA43F3 */
/* Attenuator Hold is enabled, but the held attenuator combination is not calibrated at the new frequency. The nearest calibrated attenuator combination was selected. This is expected for some frequency changes. The ideal attenuation distribution between amplifiers varies across frequency bands, and only the ideal attenuation combination is calibrated. */
#define NIRFSG_WARN_ATTENUATOR_HOLD_OVERRIDDEN_INVALID_ATTENUATOR 1073366003

/* hex: 0x3FFA43F4 */
/* Requested attribute value exceeds device specification limits. Device performance is not guaranteed. */
#define NIRFSG_WARN_OUT_OF_SPECIFICATION_USER_SETTING 1073366004

/* hex: 0x3FFA43F5 */
/* Attenuator Hold is enabled, and the requested Power Level is out of range for the selected attenuator. Note that once the attenuator is selected, the max power for that attenuator varies with configuration changes, including changes to frequency, IQ impairments, and prefilter gain. */
#define NIRFSG_WARN_POWER_OUT_OF_RANGE_FOR_ATTENUATOR_HOLD 1073366005

/* hex: 0x3FFA43F6 */
/* The signal is outside of the upconverter passband. */
#define NIRFSG_WARN_SIGNAL_OUTSIDE_PASSBAND 1073366006

/* hex: 0x3FFA43F7 */
/* Thermal Correction has reached its limit. Note: The amount of correction that can be applied is limited because Attenuator Hold is currently enabled. */
#define NIRFSG_WARN_COMPENSATION_LIMITED_BY_ATTENUATOR_HOLD 1073366007

/* hex: 0x3FFA43F8 */
/* IQ Rate was coerced, but coerced IQ Rate was never read. To eliminate this warning, read the IQ Rate before committing or initiating the generation, and account for the coerced IQ Rate as appropriate in your application. */
#define NIRFSG_WARN_COERCED_IQ_RATE_NEVER_READ 1073366008

/* hex: 0x3FFA43F9 */
/* Signal Bandwidth exceeds FIR Filter Passband Bandwidth. Ensure the specified Signal Bandwidth is correct, or increase the IQ Rate. The Arb FIR Filter Passband is -0.4*IQ Rate to +0.4*IQ Rate. */
#define NIRFSG_WARN_ARB_FILTER_BANDWIDTH_EXCEEDED 1073366009

/* hex: 0x3FFA43FA */
/* The Arb's OSP circuit detected an overflow due to an IQ pair with an absolute value greater than 1.0 (after the FIR and CIC filters). Output waveform was clipped. Reduce the Arb Pre Filter Gain to eliminate overflow. */
#define NIRFSG_WARN_ARB_OVERFLOW_IQ_SUM 1073366010

/* hex: 0x3FFA43FB */
/* Overflow detected in the Arb's CIC Filter. Output waveform was clipped. Reduce the Arb Pre Filter Gain to eliminate overflow. */
#define NIRFSG_WARN_ARB_OVERFLOW_CIC_FILTER 1073366011

/* hex: 0x3FFA43FC */
/* Overflow detected in the Arb's FIR Filter. Output waveform was clipped. Reduce the Arb Pre Filter Gain to eliminate overflow. */
#define NIRFSG_WARN_ARB_OVERFLOW_FIR_FILTER 1073366012

/* hex: 0x3FFA43FD */
/* Output signal may not be phase continuous. Remove this notification by setting the Phase Continuity Mode attribute to Disable. Refer to the documentation for more information. */
#define NIRFSG_WARN_SIGNAL_NOT_PHASE_CONTINUOUS 1073366013

/* hex: 0x3FFA43FE */
/* Output generation had been aborted by the reverse power protection circuitry of the device. Either the output signal exceeded the output power limit, or power was driven back into the output of the device by an external source. Error state is cleared. */
#define NIRFSG_WARN_REVERSE_POWER_PROTECTION 1073366014

/* hex: 0x3FFA43FF */
/* The specified value is outside the valid range. Device performance is not guaranteed. */
#define NIRFSG_WARN_OUT_OF_RANGE 1073366015


#endif /* ___niRFSG_niRFSGErrors_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSGObsolete.h sha256=c62b8d410c460fdeaa8624a3c25181049609dc731ee213130d0c1428c8f42c0f bytes=7243 -->
## FILE: imports/include/niRFSGObsolete.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSGObsolete.h`
- sha256: `c62b8d410c460fdeaa8624a3c25181049609dc731ee213130d0c1428c8f42c0f`
- bytes: 7243

````c
/****************************************************************************
 *                          NI RF Signal Generator
 *---------------------------------------------------------------------------
 *   Copyright (c) National Instruments 2003.  All Rights Reserved.
 *---------------------------------------------------------------------------
 *
 * Title:    niRFSGObsolete.h
 * Purpose:  NI RF Signal Generator
 *           Obsolete functions and attributes declarations.
 *
 ****************************************************************************/
#ifndef ___niRFSG_niRFSGObsolete_h___
#define ___niRFSG_niRFSGObsolete_h___

#include <ivi.h>

#include <IviRFSigGen.h>


/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NIRFSG_MAJOR_VERSION               19     /* Instrument driver major version   */
#define NIRFSG_MINOR_VERSION              100     /* Instrument driver minor version   */

/*  Compatibility with older versions ------*/

/*-  Deprecated Attributes and Values --------*/

/*
   Do not rely on driver support for these items.  These items
   have been deprecated.  Future versions of this driver may not support them
   (code that uses these items may no longer compile).
*/
#define NIRFSG_ATTR_THERMAL_CORRECTION_ENABLED                 NIRFSG_ATTR_AUTOMATIC_THERMAL_CORRECTION
#define NIRFSG_ATTR_SAMPLE_CLOCK_RATE                          NIRFSG_ATTR_IQ_RATE
#define NIRFSG_ATTR_UPCONVERTER_TEMPERATURE                    NIRFSG_ATTR_DEVICE_TEMPERATURE
#define NIRFSG_ATTR_LOCAL_OSCILLATOR_OUT_0_ENABLED             NIRFSG_ATTR_LO_OUT_ENABLED
#define NIRFSG_VAL_REF_CLOCK_SOURCE_PXI_CLK10                  NIRFSG_VAL_REF_CLOCK_SOURCE_PXI_CLK
#define NIRFSG_VAL_PXI_CLK10_STR                               "PXI_CLK10"
#define NIRFSG_ATTR_IF_CARRIER_FREQUENCY                       NIRFSG_ATTR_ARB_CARRIER_FREQUENCY
#define NIRFSG_ATTR_IF_POWER                                   NIRFSG_ATTR_ARB_POWER
#define NIRFSG_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED            NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED
#define NIRFSG_ATTR_DUC_PRE_FILTER_GAIN                        NIRFSG_ATTR_ARB_PRE_FILTER_GAIN
#define NIRFSG_ATTR_DUC_FIR_FILTER_TYPE                        NIRFSG_ATTR_ARB_FILTER_TYPE
#define NIRFSG_ATTR_DUC_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA    NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA
#define NIRFSG_ATTR_DUC_FIR_FILTER_RAISED_COSINE_ALPHA         NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA
#define NIRFSG_VAL_DUC_NONE                                    NIRFSG_VAL_ARB_FILTER_TYPE_NONE
#define NIRFSG_VAL_DUC_ROOT_RAISED_COSINE                      NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE
#define NIRFSG_VAL_DUC_RAISED_COSINE                           NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE
#define NIRFSG_VAL_MARKER_EVENT0                               NIRFSG_VAL_MARKER0
#define NIRFSG_VAL_MARKER_EVENT1                               NIRFSG_VAL_MARKER1
#define NIRFSG_VAL_MARKER_EVENT2                               NIRFSG_VAL_MARKER2
#define NIRFSG_VAL_MARKER_EVENT3                               NIRFSG_VAL_MARKER3
#define NIRFSG_WARN_DUC_OVERFLOW_FIR_FILTER                    NIRFSG_WARN_ARB_OVERFLOW_FIR_FILTER
#define NIRFSG_WARN_DUC_OVERFLOW_CIC_FILTER                    NIRFSG_WARN_ARB_OVERFLOW_CIC_FILTER
#define NIRFSG_WARN_DUC_OVERFLOW_IQ_SUM                        NIRFSG_WARN_ARB_OVERFLOW_IQ_SUM
#define NIRFSG_WARN_DUC_FILTER_BANDWIDTH_EXCEEDED              NIRFSG_WARN_ARB_FILTER_BANDWIDTH_EXCEEDED
#define NIRFSG_ERROR_AWG_RESOURCE_NAME_NOT_FOUND               NIRFSG_ERROR_INVALID_AWG_RESOURCE_NAME
#define NIRFSG_ERROR_AWG_RESOURCE_NAME_NOT_FOUND_IN_INIT       NIRFSG_ERROR_INVALID_AWG_RESOURCE_NAME
#define NIRFSG_ATTR_UPCONVERTER_LOOP_BANDWIDTH                 NIRFSG_ATTR_LOOP_BANDWIDTH
#define NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY_INCREMENT        (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3a)
#define NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY_INCREMENT_ANCHOR (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x3b)
#define NIRFSG_ATTR_RF_BLANKING_EVENT_SOURCE                   NIRFSG_ATTR_RF_BLANKING_SOURCE
#define NIRFSG_ATTR_REFERENCE_OSCILLATOR_SOURCE                IVIRFSIGGEN_ATTR_REFERENCE_OSCILLATOR_SOURCE
#define NIRFSG_ATTR_EXTERNAL_CALIBRATION_USER_DEFINED_INFO          /* ViString */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4e)
#define NIRFSG_ATTR_EXTERNAL_CALIBRATION_USER_DEFINED_INFO_MAX_SIZE /* ViInt32  */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x4f)
#define NIRFSG_ATTR_PEAK_POWER_ADJSUTMENT_INHERITANCE          NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE
#define NIRFSG_ATTR_IQ_ENABLED               /* ViBoolean */   IVIRFSIGGEN_ATTR_IQ_ENABLED
/*- Direct DMA is deprecated starting with RFSG 17.5 -*/
#define NIRFSG_ATTR_DIRECT_DMA_ENABLED                      /* ViBoolean */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x31)
#define NIRFSG_ATTR_DIRECT_DMA_WINDOW_ADDRESS               /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x32)
#define NIRFSG_ATTR_DIRECT_DMA_WINDOW_SIZE                  /* ViInt32   */   (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x33)
/*
   NIRFSG_ATTR_REFERENCE_OSCILLATOR_SOURCE (ViInt32) is like an alias for NIRFSG_ATTR_REF_CLOCK_SOURCE (ViString)
   However, since they are different types, they must be two separate attributes.  When you set one, niRFSG automatically sets the other.
*/

/*- Values for attribute NIRFSG_ATTR_REFERENCE_OSCILLATOR_SOURCE -*/
#define NIRFSG_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL                IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_INTERNAL
#define NIRFSG_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL                IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_EXTERNAL
#define NIRFSG_VAL_REF_CLOCK_SOURCE_PXI_CLK                            (IVIRFSIGGEN_VAL_REFERENCE_OSCILLATOR_SOURCE_SPECIFIC_EXT_BASE + 1)

/*
   Old values for attributes NIRFSG_ATTR_LOOP_BANDWIDTH and NIRFSG_ATTR_REF_PLL_BANDWIDTH.
   These have been replaced by NIRFSG_VAL_NARROW and NIRFSG_VAL_WIDE.
*/
#define NIRFSG_VAL_LOW                          NIRFSG_VAL_NARROW
#define NIRFSG_VAL_HIGH                         NIRFSG_VAL_WIDE

/*- Error Info -*/
#define NIRFSG_ATTR_PRIMARY_ERROR                            /* ViInt32  */   IVIRFSIGGEN_ATTR_PRIMARY_ERROR
#define NIRFSG_ATTR_SECONDARY_ERROR                          /* ViInt32  */   IVIRFSIGGEN_ATTR_SECONDARY_ERROR
#define NIRFSG_ATTR_ERROR_ELABORATION                        /* ViString */   IVIRFSIGGEN_ATTR_ERROR_ELABORATION

/*- Deprecated (typo).  Kept in here only for RFSG 1.1 and earlier compatibility. -*/
#define NIRFSG_VAL_ON_BOARD_CLOCK_STR           "OnBoardClock"

/*- This attribute was replaced by NIRFSG_ATTR_ALC_CONTROL-*/
#define NIRFSG_ATTR_ALC_ENABLED                             /* ViBoolean */   IVIRFSIGGEN_ATTR_ALC_ENABLED

/*- IQ Modulation ----------------------------------------------------------*/
ViStatus _VI_FUNC niRFSG_ConfigureIQEnabled
(
   ViSession vi,
   ViBoolean enabled
);

#endif /* ___niRFSG_niRFSGObsolete_h___ */
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSGPrivate.h sha256=33732643d8c825a32497ee3ba37457e2212e7022c502d4b4755f30ac7198b9a7 bytes=53551 -->
## FILE: imports/include/niRFSGPrivate.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSGPrivate.h`
- sha256: `33732643d8c825a32497ee3ba37457e2212e7022c502d4b4755f30ac7198b9a7`
- bytes: 53551

````c
#ifndef ___niRFSG_niRFSGPrivate_h___
#define ___niRFSG_niRFSGPrivate_h___

#include "niRFSG.h"
#include "ivi.h"

#if defined(__cplusplus) || defined(__cplusplus__)
extern "C" {
#endif

/****************************************************************************
 *----------------- Instrument Driver Revision Information -----------------*
 ****************************************************************************/
#define NIRFSG_DRIVER_VENDOR                "National Instruments"
#if kRFSG_32BitPlatform
   #define NIRFSG_DRIVER_DESCRIPTION           "RF Signal Generator Instrument Driver"
#elif kRFSG_64BitPlatform
   #define NIRFSG_DRIVER_DESCRIPTION           "RF Signal Generator Instrument Driver [Compiled for 64-bit]"
#else
   #error Unknown Platform
#endif


#define MAX_BUFF_SIZE   IVI_MAX_MESSAGE_BUF_SIZE // 256
#define MAX_NUM_DEVS    64L
#define NIRFSG_VAL_NO_OPTION_FLAGS  0
#define NIRFSG_IVI_FP_PRECISION_MAX 0
#define NIRFSG_FGEN_VAL_AUTO_IQ_RATE -1.0

/*
   niRFSG.h defines some Attribute Aliases.  These attribute names are consistent with their equivalent
   IVI-Defined Attribute names.  Our code and documentation will only use the Driver-Specific names.
   Clear the Alias Name to force our code to always use the Driver-Specific name (helps maintainability).
*/
#undef NIRFSG_ATTR_REFERENCE_OSCILLATOR_EXTERNAL_FREQUENCY     // instead use NIRFSG_ATTR_REF_CLOCK_RATE
#undef NIRSFG_ATTR_ARB_CLOCK_FREQUENCY                         // instead use NIRFSG_ATTR_IQ_RATE
#undef NIRFSG_ATTR_ARB_TRIGGER_SOURCE                          // instead use NIRFSG_ATTR_START_TRIGGER_TYPE
#undef NIRFSG_ATTR_ARB_EXTERNAL_TRIGGER_SLOPE                  // instead use NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE

/*
   Similar to aliased attribute names, clear aliased attribute values.
*/
#undef NIRFSG_VAL_ARB_TRIGGER_SOURCE_IMMEDIATE                 // instead use NIRFSG_VAL_NONE
#undef NIRFSG_VAL_ARB_TRIGGER_SOURCE_EXTERNAL                  // instead use NIRFSG_VAL_DIGITAL_EDGE
#undef NIRFSG_VAL_ARB_TRIGGER_SOURCE_SOFTWARE                  // instead use NIRFSG_VAL_SOFTWARE
#undef NIRFSG_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_POSITIVE          // instead use NIRFSG_VAL_RISING_EDGE
#undef NIRFSG_VAL_ARB_EXTERNAL_TRIGGER_SLOPE_NEGATIVE          // instead use NIRFSG_VAL_FALLING_EDGE

/*
   Starting in 440, IVI remapped IVI_SPECIFIC_PRIVATE_ATTR_BASE from
   (IVI_ATTR_BASE + 100000)
    to
   (IVI_ATTR_BASE + 200000)
   We have decided to continue using the old range in order to avoid
   compatibility issues. (see CAR 530516)
*/
#define RFSG_SPECIFIC_PRIVATE_ATTR_BASE (IVI_ATTR_BASE + 100000)

/*****************************************************************************
 *-----------------------  Hidden Attributes  ---------------*
 *****************************************************************************/
// (numeric gap)
#define NIRFSG_ATTR_ARB_PRODUCT_CODE                                          (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x02)
#define NIRFSG_ATTR_UPCONVERTER_PRODUCT_CODE                                  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x03)
#define NIRFSG_ATTR_IRFSG_POINTER                           /* ViAddr    */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x04)
// (numeric gap)
#define NIRFSG_ATTR_UPCONVERTER_TASK_ID                     /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x06)
#define NIRFSG_ATTR_INIT_WAITS_UNTIL_SETTLED                /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x07)
// (numeric gap)
#define NIRFSG_ATTR_ARB_DIGITAL_FILTER_INTERPOLATION_FACTOR /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x0a)
#define NIRFSG_ATTR_USE_CALIBRATION                         /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x0d)
#define NIRFSG_ATTR_TEMPERATURE_AVERAGES                    /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x0f)
#define NIRFSG_ATTR_RF_USED_AS_LO                           /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x10)
#define NIRFSG_ATTR_ARB_FILTER_FLAT_PASSBAND                /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x13)
#define NIRFSG_ATTR_ARB_FILTER_GAUSSIAN_BT                  /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x14)
// Not sure what to name this but probably best to use an enum rather than a boolean
#define NIRFSG_ATTR_ARB_AMPLITUDE_CORRECTION_METHOD         /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x15)
#define NIRFSG_ATTR_5611_LO_FILTER                          /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x16)
#define NIRFSG_ATTR_LO_IN_ATTENUATOR                        /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x17)
#define NIRFSG_ATTR_LO_FILTER_DAC                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x18)
#define NIRFSG_ATTR_5611_RF_FILTER                          /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x19)
#define NIRFSG_ATTR_RF_ATTENUATOR                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1a)
#define NIRFSG_ATTR_EXTERNAL_CALIBRATION_LAST_DATE_TIME     /* Timestamp */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1b)
#define NIRFSG_ATTR_POWER_BOTH_MODULATORS                   /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1c)
#define NIRFSG_ATTR_HAS_REF_OUT2                            /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1d)
#define NIRFSG_ATTR_DIGITAL_MODULATION_USER_DEFINED_WFM     /*    i8[]   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1e)
#define NIRFSG_ATTR_5653_MASTER_REF_DAC                     /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x1f)
#define NIRFSG_ATTR_5653_YIG_DAC                            /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x20)
#define NIRFSG_ATTR_5653_LO1_ALC_DAC                        /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x21)
#define NIRFSG_ATTR_5653_LO1_OUTPUT_FILTER                  /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x22)
#define NIRFSG_ATTR_5653_LO2_VVA_DAC                        /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x23)
#define NIRFSG_ATTR_5653_LO3_VVA_DAC                        /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x24)
#define NIRFSG_ATTR_5653_100MHz_PLL_LOCKING_ENABLED         /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x25)
#define NIRFSG_ATTR_5653_LO2_PLL_LOCKING_ENABLED            /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x26)
#define NIRFSG_ATTR_CONFIGURATION_LIST_DMA_ENABLED          /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x27)
#define NIRFSG_ATTR_YIG_PLL_COARSE_FREQUENCY                /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0X28)
#define NIRFSG_ATTR_YIG_PLL_FINE_FREQUENCY                  /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0X29)
#define NIRFSG_ATTR_DEBUGGING_OPTIONS                       /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2a)
#define NIRFSG_ATTR_SELF_CALIBRATION_VALID                  /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2b)
#define NIRFSG_ATTR_5652_REFERENCE_FREQ_DAC                 /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2d)
#define NIRFSG_ATTR_5652_ALC_DAC                            /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2e)
#define NIRFSG_ATTR_5652_ATTENUATION                        /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2f)
#define NIRFSG_ATTR_5652_BYPASS_MAIN_ATTENUATORS            /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x30)
#define NIRFSG_ATTR_EXTRA_LIST_MODE_ATTRIBUTES_ENABLED      /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x31)
#define NIRFSG_ATTR_RFSA_PROTOCOL                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x32)
#define NIRFSG_ATTR_RFSA_OLDEST_COMPATIBLE_PROTOCOL         /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x33)
#define NIRFSG_ATTR_REF_CLOCK_TOKEN0                        /* ViInt64   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x42)
#define NIRFSG_ATTR_REF_CLOCK_TOKEN1                        /* ViInt64   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x46)
#define NIRFSG_ATTR_REF_CLOCK_TOKEN2                        /* ViInt64   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x47)
#define NIRFSG_ATTR_ALC_ADC_READING                /*ViInt32, read-only  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x34)
#define NIRFSG_ATTR_5696_KNEE                               /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x35)
#define NIRFSG_ATTR_5696_OFFSET                             /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x36)
#define NIRFSG_ATTR_5696_DETECTOR_REF_DAC                   /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x37)
#define NIRFSG_ATTR_5696_ATTN_CELL_10_ON                    /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x38)
#define NIRFSG_ATTR_5696_ATTN_CELL_20_ON                    /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x39)
#define NIRFSG_ATTR_5696_ATTN_CELL_40A_ON                   /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3A)
#define NIRFSG_ATTR_5696_ATTN_CELL_40B_ON                   /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3B)
#define NIRFSG_ATTR_5654_OCXO_REF_DAC                       /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3C)
#define NIRFSG_ATTR_5654_OCXO_REF_DAC_FLUSH_TO_HW           /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x48)
#define NIRFSG_ATTR_5654_COARSE_AMPLITUDE_DAC               /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3D)
#define NIRFSG_ATTR_AE_GAIN                                 /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3E)
#define NIRFSG_ATTR_5654_POWER_SEARCH_ADC          /* ViInt32, read-only */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x49)
#define NIRFSG_ATTR_LO_CASCADE_ID                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4A)
#define NIRFSG_ATTR_LO_OUT_CASCADE_ID                       /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x52)
#define NIRFSG_ATTR_RF_CASCADE_ID                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4B)
#define NIRFSG_ATTR_IQ_CASCADE_ID                           /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4C)
#define NIRFSG_ATTR_ONBOARD_REF_CLK_DAC                     /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4D)
#define NIRFSG_ATTR_VCO_SELF_CAL_ENABLED                    /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4E)
#define NIRFSG_ATTR_VCO_CAL_VOLTAGE                         /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x4F)
#define NIRFSG_ATTR_VCO_PFD                                 /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x50)
#define NIRFSG_ATTR_VCO_CHARGE_PUMP                         /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x51)
#define NIRFSG_ATTR_LO_FILTER                               /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x53)
#define NIRFSG_ATTR_RF_FILTER                               /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x54)
#define NIRFSG_ATTR_5840_MODULATOR                          /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x55)
#define NIRFSG_ATTR_CAL_DSP_FREQ_SHIFT                      /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x56)
#define NIRFSG_ATTR_CAL_DSP_STATIC_I                        /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x57)
#define NIRFSG_ATTR_CAL_DSP_STATIC_Q                        /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x58)
#define NIRFSG_ATTR_CAL_DSP_STATIC_IQ_ENABLED               /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x59)
#define NIRFSG_ATTR_EQ_FILTER_ENABLED                       /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5A)
#define NIRFSG_ATTR_VCO_CAL_RESULT                          /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5B)
#define NIRFSG_ATTR_LO_POWER_METER_ENABLED                  /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5C)
#define NIRFSG_ATTR_LO_POWER_METER_RESULT                   /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5D)
#define NIRFSG_ATTR_LO_GAIN_STATES                          /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5E)
#define NIRFSG_ATTR_LO_OUT_GAIN_STATES                      /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x5F)
#define NIRFSG_ATTR_RF_GAIN_STATES                          /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x60)
#define NIRFSG_ATTR_RF_CASCADE_STATE                        /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x65)
#define NIRFSG_ATTR_VCO_CAL_FREQUENCY                       /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x61)
#define NIRFSG_ATTR_WAVEFORM_ANALYSIS_MAP                   /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x62)
#define NIRFSG_ATTR_LO_CAL_FREQUENCY                        /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x63)
#define NIRFSG_ATTR_TCLK_ADJUSTMENT                         /* ViReal64  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x64)
#define NIRFSG_ATTR_USER_COMMON_MODE_DAC_OFFSET             /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x66)
#define NIRFSG_ATTR_PRIMARY_COMMON_MODE_DAC_OFFSET          /* ViReal64[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x67)
#define NIRFSG_ATTR_SECONDARY_COMMON_MODE_DAC_OFFSET        /* ViReal64[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x68)
#define NIRFSG_ATTR_RF_POWER_METER_RESULT                   /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x69)
#define NIRFSG_ATTR_VCO_CAL_CORE                   /* ViInt32, read-only */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6A)
#define NIRFSG_ATTR_VCO_CAL_OUTPUT_POWER           /* ViInt32, read-only */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6B)
#define NIRFSG_ATTR_HARDWARE_STATE_OVERRIDE_UIDS            /* ViReal64[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6C)
#define NIRFSG_ATTR_HARDWARE_STATE_OVERRIDE_STATES          /* ViReal64[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6D)
#define NIRFSG_ATTR_RF_POWER_METER_ENABLED                  /* ViInt32   */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6E)
#define NIRFSG_ATTR_5653_REFERENCE_CLOCK_ONLY_COMMIT        /* ViBoolean */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x6F)
#define NIRFSG_ATTR_2795_SPARAMETER_DATA                    /* NIComplexNumber[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x70)
#define NIRFSG_ATTR_2795_SPARAMETER_FREQUENCIES             /* ViReal64[] */         (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x71)
#define NIRFSG_ATTR_DEEMBEDDING_SPARAMETERS                 /* NIComplexNumber[] */  (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x72)
#define NIRFSG_ATTR_DEEMBEDDING_TABLE_NUMBER_OF_PORTS       /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x73)
#define NIRFSG_ATTR_LO_FREQUENCY_AT_MIXER                   /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x74)
#define NIRFSG_ATTR_VCO_ID                                  /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x75)
#define NIRFSG_ATTR_COMPOSITE_IDLE_TRACKER_ID               /* ViInt32*/      (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x76)
#define NIRFSG_ATTR_RF_ACCESSORY_POWER_OFFSET               /* ViReal64*/     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x77)
#define NIRFSG_ATTR_RF_ACCESSORY_PATH_GAIN                  /* ViReal64*/     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x78)
#define NIRFSG_ATTR_RF_ACCESSORY_DIGITAL_GAIN               /* ViReal64*/     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x79)
#define NIRFSG_ATTR_SYSTEM_CONFIGURATION        /* ViString, read-only  */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7a)

#define NIRFSG_ATTR_ASSOC_AUX_SWITCH_GAIN_UID   /* ViInt32, read-only */      (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x88)

// This attribute is only used by VST now and should not be used for newer devices.
#define NIRFSG_ATTR_SELF_CALIBRATION_DATE_TIME              /* Timestamp */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x2C)

/*
   NIRFSG_ATTR_SELF_CALIBRATION_MODULE is not used as an Attribute, only declared as such so that enums
   used for the self calibration "module" parameter (i32) can return enum values as strings via tEnglishAttributeStringTable.
*/
#define NIRFSG_ATTR_SELF_CALIBRATION_MODULE                 /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x40)
#define NIRFSG_ATTR_5696_AMP_BAND                           /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x41)
#define NIRFSG_ATTR_5696_LOWHARMONIC_LEVEL_DAC              /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x43)
#define NIRFSG_ATTR_5696_TEMP_COMP_DAC                      /* ViInt32 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x44)

// Per-Waveform Internal Attributes
#define NIRFSG_ATTR_IQ_RATE_INTERNAL                        /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7b)
#define NIRFSG_ATTR_SIGNAL_BANDWIDTH_INTERNAL               /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7c)
#define NIRFSG_ATTR_RUNTIME_SCALING_INTERNAL                /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7d)
#define NIRFSG_ATTR_PAPR_INTERNAL                           /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7e)
#define NIRFSG_ATTR_WAVEFORM_INDEX_FROM_FILE_INTERNAL       /* ViUInt32 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x80)

#define NIRFSG_ATTR_SENSOR_TEMPERATURE                      /* ViReal64 */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x81)

#define NIRFSG_ATTR_ASSOC_LO_GAIN_STATES                    /* Internal  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x82)
#define NIRFSG_ATTR_ASSOC_LO_FILTER                         /* ViUInt32  */   (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x83)

// NIRFSG_ATTR_OOP_SESSION_MANAGER_PTR attribute stores OutOfProcessSessionManager pointer. This attribute is used in Remote component.
#define NIRFSG_ATTR_OOP_SESSION_MANAGER_PTR                 /* ViAddr */      (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x7f)
#define NIRFSG_ATTR_OOP_SESSION_PIPE_ID                     /* ViInt64 */     (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x86)

// This attribute stores the channel number specified at initialize (first used in MCVST)
#define NIRFSG_ATTR_CREATED_SESSION_CHANNEL                 /* ViInt32 */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x139)

// Leaving these attributes in the public attribute space but in the private header file
#define NIRFSG_ATTR_CONFIGURATION_TRIGGER_DELAY                /* ViReal64  */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x65)
#define NIRFSG_ATTR_LO2_OUT_ENABLED                            /* ViBoolean */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x77)
#define NIRFSG_ATTR_LO3_OUT_ENABLED                            /* ViBoolean */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x78)
#define NIRFSG_ATTR_MIN_PLL_LOCK_TIME                          /* ViReal64  */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x82)
#define NIRFSG_ATTR_PLL_CHECK_ENABLED                          /* ViBoolean */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x83)
#define NIRFSG_ATTR_INCLUDE_SETTLING_FOR_FREQUENCY_DIVIDER_AND_MULTIPLIER_CHANGE /* ViBoolean */      (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x8B)
#define NIRFSG_ATTR_TIMER_START_SOURCE                         /* ViString */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xC1) /* VST only right now */
#define NIRFSG_ATTR_ATTENUATION                                /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xAE)
#define NIRFSG_ATTR_AMP_GAIN                                   /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xAC)
#define NIRFSG_ATTR_LOW_PHASE_NOISE_OPTION                     /* ViBoolean, read-only */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xBD)
#define NIRFSG_ATTR_POWER_CALIBRATION_TEMPERATURE              /* ViReal64, read-write */    (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x3F)
#define NIRFSG_ATTR_EQUALIZER_COEFFICIENTS                     /* ViReal64[], read-write */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xC8)
#define NIRFSG_ATTR_EQUALIZER_COEFFICIENTS_GROUP_DELAY         /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xC9)
#define NIRFSG_ATTR_EQUALIZER_COEFFICIENTS_GAIN                /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xDD)
#define NIRFSG_ATTR_EQUALIZER_COEFFICIENTS_PHASE_OFFSET        /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xDE)
#define NIRFSG_ATTR_EQUALIZER_COEFFICIENTS_BANDWIDTH           /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xDF)
#define NIRFSG_ATTR_DC_OFFSET_CORRECTION_I_OFFSET              /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xCA)
#define NIRFSG_ATTR_DC_OFFSET_CORRECTION_Q_OFFSET              /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xCB)
#define NIRFSG_ATTR_LO_OUT_SOURCE                              /* ViString, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xCD)
#define NIRFSG_ATTR_MIN_FREQUENCY                              /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xD5)
#define NIRFSG_ATTR_MAX_FREQUENCY                              /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xD6)
#define NIRFSG_ATTR_MIN_UPCONVERTER_CENTER_FREQUENCY           /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xD7)
#define NIRFSG_ATTR_MAX_UPCONVERTER_CENTER_FREQUENCY           /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xD8)
#define NIRFSG_ATTR_RF_POWER_PROTECTION_ENABLED                /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xE0)
#define NIRFSG_ATTR_MAX_DEVICE_INSTANTANEOUS_BANDWIDTH         /* ViReal64  */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xe7)
#define NIRFSG_ATTR_MAX_IQ_RATE                                /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x9F)
#define NIRFSG_ATTR_MIN_IQ_RATE                                /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xE3)
#define NIRFSG_ATTR_DMM_ACQUISITION_LENGTH                     /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xE8)
#define NIRFSG_ATTR_DMM_READ                                   /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xE9)
#define NIRFSG_ATTR_DMM_READ_Q                                 /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xEA)
#define NIRFSG_ATTR_DMM_CORRECTION_FREQUENCY                   /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xEB)
#define NIRFSG_ATTR_FINE_TUNE_ADJUSTMENT                       /* ViReal64, read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xED)
#define NIRFSG_ATTR_CONFIGURATION_LIST_STATUS_CHECKS_DISABLED  /* ViInt64,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xEE)
#define NIRFSG_ATTR_P2P_ENDPOINT_HANDLE                        /* ViUInt32  read-only */     (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF5)
#define NIRFSG_ATTR_FREQUENCY_RESPONSE_FILTER_ENABLED          /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF6)
#define NIRFSG_ATTR_IMPAIRMENTS_FILTER_ENABLED                 /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF7)
#define NIRFSG_ATTR_GAIN_STATE_FROM_SELF_CAL                   /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFE)
#define NIRFSG_ATTR_TRIGGER_MIN_IMPORT_PULSE_WIDTH             /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFF)
#define NIRFSG_ATTR_INTERNAL_CALIBRATION_ELEMENT_TERMINATION   /* ViString, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x100)
#define NIRFSG_ATTR_WAVEFORM_SOURCE                            /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x104)
#define NIRFSG_ATTR_ASSOC_AUX_SWITCH_GAIN                      /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x106)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION             /* ViInt32, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x111)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE        /* ViInt32, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x112)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME     /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x113)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD        /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x114)
#define NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME     /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x115)

#define NIRFSG_ATTR_FREQUENCY_RESPONSE_EQUALIZER_COEFFICIENTS              /* ViReal64[] */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x117)
#define NIRFSG_ATTR_FREQUENCY_RESPONSE_EQUALIZER_COEFFICIENTS_GAIN         /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x118)
#define NIRFSG_ATTR_FREQUENCY_RESPONSE_EQUALIZER_COEFFICIENTS_BANDWIDTH    /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x119)
#define NIRFSG_ATTR_FREQUENCY_RESPONSE_EQUALIZER_COEFFICIENTS_PHASE_OFFSET /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11A)
#define NIRFSG_ATTR_FREQUENCY_RESPONSE_EQUALIZER_COEFFICIENTS_GROUP_DELAY  /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11B)
#define NIRFSG_ATTR_IMPAIRMENTS_EQUALIZER_COEFFICIENTS                     /* ViReal64[] */  (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11C)
#define NIRFSG_ATTR_IMPAIRMENTS_EQUALIZER_COEFFICIENTS_GAIN                /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11D)
#define NIRFSG_ATTR_IMPAIRMENTS_EQUALIZER_COEFFICIENTS_BANDWIDTH           /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11E)
#define NIRFSG_ATTR_IMPAIRMENTS_EQUALIZER_COEFFICIENTS_PHASE_OFFSET        /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x11F)
#define NIRFSG_ATTR_IMPAIRMENTS_EQUALIZER_COEFFICIENTS_GROUP_DELAY         /* ViReal64 */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x120)

#define NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS             /*ViInt32*/          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x122)
#define NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS            /*ViInt32*/          (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x123)

#define NIRFSG_ATTR_ASSOC_AUX_POWER_CUTOFF_LEVEL               /* ViReal64, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x128)

#define NIRFSG_ATTR_DAC_DECODER_MODE                          /* ViInt32,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x130)

#define NIRFSG_ATTR_OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH        /* ViInt64,  read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x132)

/* System Correction attributes ---------------------------------------------------*/
#define NIRFSG_ATTR_CHANNEL_GAIN_IMBALANCE                     /* ViReal64 */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xEC)

#define NIRFSG_ATTR_HOST_DMA_BUFFER_MIRROR_SIZE                /* ViInt64  */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xF0)

#define NIRFSG_ATTR_AVAILABLE_INTERNAL_PORTS                   /* ViString */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x103)
#define NIRFSG_ATTR_INTERNAL_PORT_MAP                          /* ViString */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x105)
#define NIRFSG_ATTR_STS_5532_SIGNAL_PATH                       /* ViInt32  */                (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0xFA)

#define NIRFSG_ATTR_WAVEFORM_BURST_START_LOCATIONS             /* ViReal64[] */              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10B)
#define NIRFSG_ATTR_WAVEFORM_BURST_STOP_LOCATIONS              /* ViReal64[] */              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10C)
#define NIRFSG_ATTR_WAVEFORM_MARKER_EVENT_LOCATIONS            /* ViReal64[] */              (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x10D)

#define NIRFSG_ATTR_MISMATCH_CORRECTION_ENABLED                /* ViInt32 */                 (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x126)

#define NIRFSG_ATTR_FREQUENCY_SHIFT                            /* ViReal64  */               (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x127)

#define NIRFSG_ATTR_ACCESSORY_INTERNAL_CONNECTION              /* ViString, read-write */    (IVI_SPECIFIC_PUBLIC_ATTR_BASE + 0x131)

#define NIRFSG_ATTR_CONVERTER_DELAY_BASELINE                   /* ViReal64 */                (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x84)

#define NIRFSG_ATTR_MTS_DELAY_BASELINE                         /* ViInt32 */                 (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x85)

#define NIRFSG_ATTR_COERCE_POWER_LEVEL_TO_MAX_POWER            /* ViInt32 */                 (RFSG_SPECIFIC_PRIVATE_ATTR_BASE + 0x87)

/*****************************************************************************
 *-----------------------  Hidden Constants  ---------------*
 *****************************************************************************/

// Unique values allows better error checking (detect using wrong value for this attribute).
// In general, split up the ranges like this to make it easier to ensure unique values:
//    0    to ~50k:  Public values
//   ~50k  to  99k:  Private values
//    101k to 200k:  Values synchronized with RFSA (ie, Willy LO filter is same on generator and analyzer)

/*------------------- Private Values (99k downto ~50k) -----------------------*/

// Values for attribute NIRFSG_ATTR_ARB_FILTER_TYPE
#define NIRFSG_VAL_ARB_FILTER_TYPE_GAUSSIAN                 99001
#define NIRFSG_VAL_ARB_FILTER_TYPE_CUSTOM                   99002

// Values for attribute NIRFSG_ATTR_ARB_AMPLITUDE_CORRECTION_METHOD
#define NIRFSG_VAL_ANALOG_GAIN                  98000
#define NIRFSG_VAL_DIGITAL_GAIN                 98001

// Values for NIRFSG_ATTR_5696_AMP_BAND
#define NIRFSG_VAL_5696_AMPBAND_HIGHPOWER_250K_TO_250M            96000
#define NIRFSG_VAL_5696_AMPBAND_LOWHARMONICS_250M_TO_1G           96001
#define NIRFSG_VAL_5696_AMPBAND_1G_TO_2_4G                        96002
#define NIRFSG_VAL_5696_AMPBAND_2_4G_TO_3_86G                     96003
#define NIRFSG_VAL_5696_AMPBAND_3_86G_TO_5_37G                    96004
#define NIRFSG_VAL_5696_AMPBAND_5_37G_TO_7_45G                    96005
#define NIRFSG_VAL_5696_AMPBAND_7_45G_TO_10_4G                    96006
#define NIRFSG_VAL_5696_AMPBAND_10_4G_TO_14_4G                    96007
#define NIRFSG_VAL_5696_AMPBAND_14_4G_TO_20_0G                    96008
#define NIRFSG_VAL_5696_AMPBAND_LOWGROUPDELAY_14_4G_TO_17G        96009
#define NIRFSG_VAL_5696_AMPBAND_LOWGROUPDELAY_17G_TO_20G          96010

// For 565x, this is an alias for "RefIn" or "RefOut" (depending on context).  Use of "RefIn" or "RefOut" is preferred.
#define NIRFSG_VAL_REF_INOUT_STR                "RefIn/Out"

// Values for repository selection on the GetFPGAExtensionsBitfileDir function
#define NIRFSG_VAL_FPGA_BITFILE_REPOSITORY_USER 0

// Additional Values for attribute NIRFSG_ATTR_AMP_PATH
#define NIRFSG_VAL_OFF                          16002 // Uses the public range since it is a public attribute. Make sure it is unique across other values for this enum in niRFSG.h
#define NIRFSG_VAL_LOW_GROUP_DELAY              16003

// Values for niRFSG_ResetWithOption
// These are now obsolete and the public versions should be now used.
#define NIRFSG_VAL_RESET_WITH_OPTION_RESET                       NIRFSG_VAL_RESET_WITH_OPTIONS_NONE
#define NIRFSG_VAL_RESET_WITH_OPTION_PRESERVE_WAVEFORM           NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS
#define NIRFSG_VAL_RESET_WITH_OPTION_PRESERVE_SCRIPT             NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS
#define NIRFSG_VAL_RESET_WITH_OPTION_PRESERVE_ROUTES             NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES
#define NIRFSG_VAL_RESET_WITH_OPTION_PRESERVE_DEEMBEDDING_TABLES NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES

// Values for NIRFSG_ATTR_5840_MODULATOR
#define NIRFSG_VAL_5840_MODULATOR_BYPASS     95000
#define NIRFSG_VAL_5840_MODULATOR_ENABLED    95001   // Module uses a single modulator for now.  Layout allows for 1 to be added.

// For NIRFSG_ATTR_LO_OUT_SOURCE attribute
// Internal_LO means match the LO_SOURCE attribute
#define NIRFSG_VAL_LO_OUT_SOURCE_INTERNAL_LO_STR            "Internal_LO"
// Onboard means export the lo synth signal regardless of the LO_SOURCE attribute
#define NIRFSG_VAL_LO_OUT_SOURCE_ONBOARD_STR                NIRFSG_VAL_LO_SOURCE_ONBOARD_STR

// Values used internally to match RFSA amp modes
// note these continue the NIRFSG_ATTR_AMP_PATH values that are public, using the 16xxx range.
#define NIRFSG_VAL_RF_AMP_DISABLED                             16002
#define NIRFSG_VAL_RF_AMP_ENABLED_WHEN_IN_SIGNAL_PATH          16003
#define NIRFSG_VAL_RF_AMP_ENABLED                              16004
#define NIRFSG_VAL_RF_AMP_AUTOMATIC                            16005

// Values for NIRFSG_ATTR_OUTPUT_PORT
// note there are other enum values that are not private in niRFSG.h
#define NIRFSG_VAL_IQ_IN                      14100 // Output to IQ In Port
#define NIRFSG_VAL_IMPORT_SIGNAL              14101 // Measure via IQ Out Port
#define NIRFSG_VAL_IF_POWER_METER             14102 // Route to internal power meter

// Values for NIRFSG_ATTR_CONFIGURATION_LIST_STATUS_CHECKS_DISABLED
#define NIRFSG_VAL_STATUS_CHECK_NONE                0x0000000000000000
#define NIRFSG_VAL_STATUS_CHECK_POWER_PROTECTION    0x0000000000000001
#define NIRFSG_VAL_STATUS_CHECK_DSP                 0x0000000000000002
#define NIRFSG_VAL_STATUS_CHECK_LO_PLL              0x0000000000000004
#define NIRFSG_VAL_STATUS_CHECK_ALL                 0xFFFFFFFFFFFFFFFF

// Values for NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE
#define NIRFSG_VAL_IF_MODE_COMPATIBILITY                       26000

// Values for NIRFSG_ATTR_WAVEFORM_SOURCE
// note using values that are public; expect attribute to be public in future release.
#define NIRFSG_VAL_WAVEFORM_SOURCE_NONE                        NIRFSG_VAL_NONE
#define NIRFSG_VAL_WAVEFORM_SOURCE_WGEN                        27000
#define NIRFSG_VAL_WAVEFORM_SOURCE_P2P                         27001
#define NIRFSG_VAL_WAVEFORM_SOURCE_USER                        27002

// Enum values for getting attribute authorship
#define NIRFSG_VAL_ATTR_AUTHOR_DEFAULT          0
#define NIRFSG_VAL_ATTR_AUTHOR_USER             1
#define NIRFSG_VAL_ATTR_AUTHOR_DRIVER           2

// Private marker used for RF Blanking
#define NIRFSG_VAL_RF_BLANKING_MARKER                       "marker7"

// "PulseIn" is an alias for the following two signal names.  We want customers to use
// the public alias, which allows the driver to choose the appropriate signal for the
// configured use case.
#define NIRFSG_VAL_PULSE_IN_HIGH_RESOLUTION_STR             "PulseInHighResolution"
#define NIRFSG_VAL_PULSE_IN_LOW_LATENCY_STR                 "PulseInLowLatency"

//Enum values for DAC decoder modes

#define NIRFSG_VAL_DAC_DECODER_MAX_SNR          28001
#define NIRFSG_VAL_DAC_DECODER_MAX_LINEARITY    28002

/*****************************************************************************
 *-------------------  Global Variables (driver internal use) ---------------*
 *****************************************************************************/

/*****************************************************************************
 *------------------  Hidden Functions (but exported from dll)  -------------*
 *****************************************************************************/
ViStatus _VI_FUNC niRFSG_SetDigitalIFEqualizationCoefficients
(
   ViSession   vi,
   ViInt32     numberOfCoefficients,
   ViReal32*   coefficients
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetDigitalIFEqualizationCoefficients
(
   ViSession   vi,
   ViInt32*    numberOfCoefficients,
   ViReal32*   coefficients
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_IsCalibrationSession
(
   ViSession   vi,
   ViBoolean*  isCalibrationSessionPtr
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_readCalibrationBytestream
(
   ViSession   vi,
   ViUInt8*    bytestream,
   ViUInt32*   numberOfBytes
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_writeCalibrationBytestream
(
   ViSession      vi,
   const ViUInt8* bytestream,
   ViUInt32       numberOfBytes
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetExternalCalibrationLastDateAndTime
(
   ViSession      vi,
   ViInt32        year,
   ViInt32        month,
   ViInt32        day,
   ViInt32        hour,
   ViInt32        minute,
   ViInt32        second
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_UpdateExternalCalibrationDateAndTime
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_UpdateExternalCalibrationTemperature
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_InitExternalCalibration
(
   ViRsrc        resourceName,
   ViConstString password,
   ViConstString optionString,
   ViSession*    newVi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CloseExternalCalibration
(
   ViSession vi,
   ViBoolean writeCalibrationInformationToHardware
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetErrorMessage
(
   ViSession   vi,
   ViStatus    errorCode,
   ViInt32     errorDescriptionBufferSize,
   ViChar      errorDescription[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetRalInstructions
(
   ViSession   vi,
   ViInt32     instructionsBufferSize,
   ViInt32*    instructionsBuffer
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetRalInstructions
(
   ViSession   vi,
   ViInt32     instructionsBufferSize,
   ViInt32*    instructionsBuffer,
   ViInt32*    actualInstructionsBufferSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_5653_GetYigPllCoarseAndFineFrequencyOptions
(
   ViSession vi,
   ViReal64 desiredLO1Frequency,
   ViBoolean allowUntestedCoarseFrequencies,
   ViInt32 optionsArrayCapacity,
   ViReal64 coarseFrequencies[],
   ViReal64 fineFrequencies[],
   ViUInt32 spurBitfield[],
   ViInt32* optionsArraySize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetRefClockPLLStickyBit
(
   ViSession vi,
   ViBoolean* refClockPLLStickyBitPtr
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetRefClockToken
(
   ViSession vi,
   ViUInt32 tokenNumber,
   ViInt64* refClockTokenPtr
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_5654_WriteCalTable
(
   ViSession       vi,
   ViInt32         table,                 /* CalTableEnum defined in ni5654 */
   ViInt32         powersSize,
   const ViInt16   powers_centi_dBm[],
   ViInt32         frequenciesSize,
   const ViUInt64  frequencies_mHz[],
   const ViUInt16  values[]          /* size = powersSize * frequenciesSize */
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_5654_ReadCalTable
(
   ViSession       vi,
   ViInt32         table,                 /* CalTableEnum defined in ni5654 */
   ViInt32         powersSize,
   const ViInt16   powers_centi_dBm[],
   ViInt32         frequenciesSize,
   const ViUInt64  frequencies_mHz[],
   ViUInt16        values[]          /* size = powersSize * frequenciesSize */
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_5654_OCXOCal
(
   ViSession       vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViInt32
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attribute,
   ViInt32*        value
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViInt64
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attribute,
   ViInt64*        value
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViReal64
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attribute,
   ViReal64*       value
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
// ViStatus is returning the length of the string when positive
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViString
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attribute,
   ViInt32         bufSize,
   ViChar          value[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViBoolean
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attribute,
   ViBoolean*      value
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
// ViStatus is returning the size of the array when positive
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeViReal64Array
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attributeId,
   ViInt32         valueLengthInElements,
   ViReal64        value[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
// ViStatus is returning the size of the array when positive
ViStatus _VI_FUNC niRFSG_GetDesiredAttributeNIComplexNumberArray
(
   ViSession       vi,
   ViConstString   channelName,
   ViAttr          attributeId,
   ViInt32         valueLengthInElements,
   NIComplexNumber value[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/

// This is the original private ResetWithOption, but is now obsolete.  The public version
// is ResetWithOptions to match the already RFSA public version.  This entrypoint is kept
// to keep backwards compatibility.
ViStatus _VI_FUNC niRFSG_ResetWithOption
(
   ViSession vi,
   ViUInt64 resetOption
);


/*****************************************************************************
 *-----------------------  Included for IVI-compiance only ------------------*
 *  None of these will be useful to customers using the niRFSG API directly. *
 *  These are for IVI class driver customers only, and were removed from the *
 *  public header file to eliminate clutter (show only what niRFSG supports. *
 *****************************************************************************/
#define NIRFSG_ATTR_IQ_SOURCE                               /* ViInt32   */   IVIRFSIGGEN_ATTR_IQ_SOURCE
#define NIRFSG_VAL_IQ_SOURCE_ARB_GENERATOR                                    IVIRFSIGGEN_VAL_IQ_SOURCE_ARB_GENERATOR

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureArb
(
   ViSession   vi,
   ViReal64    clockFrequency,
   ViReal64    filterFrequency
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SendSoftwareTrigger
(
   ViSession vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_IsSettled
(
   ViSession   vi,
   ViBoolean*  isSettledPtr
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_ConfigureALCEnabled
(
   ViSession vi,
   ViBoolean ALCEnabled
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_CalibrateIQ
(
   ViSession   vi
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetCfgTime
(
   ViSession   vi,
   ViInt64     step,
   ViBoolean   includeSettling,
   ViReal64*   configurationTime
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_PerformThermalCorrectionIfNeeded
(
   ViSession vi,
   ViBoolean* thermalCorrectionPerformedPtr
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetFPGAExtensionsBitfileDir
(
   ViRsrc resourceName,
   ViConstString deviceContext,
   ViUInt32 repositorySelect,
   ViUInt32 bitfileDirBufferSize,
   ViChar* bitfileDir,
   ViUInt32* requiredBitfileDirBufferSize
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetAttributeViReal64Array
(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 valueLengthInElements,
   const ViReal64 value[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
// ViStatus is returning the size of the array when positive
ViStatus _VI_FUNC niRFSG_GetAttributeViReal64Array
(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 valueLengthInElements,
   ViReal64 value[]
);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_SetAttributeNIComplexNumberArray(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 valueLengthInElements,
   NIComplexNumber value[]);
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
// ViStatus is returning the size of the array when positive
ViStatus _VI_FUNC niRFSG_GetAttributeNIComplexNumberArray(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32 valueLengthInElements,
   NIComplexNumber value[]);

ViStatus _VI_FUNC niRFSG_GetSensorTemperature(
   ViSession vi,
   ViConstString sensorString,
   ViReal64* temperature);

ViStatus _VI_FUNC niRFSG_MfgOverride(
   ViSession vi,
   ViConstString value);

// The difference between the Unix timestamp epoch (1970) and the Mac timestamp epoch (1904) is 2082844800 seconds.
const ViUInt64 kRfsgTimeDiff_Epoch_1904_1970 = 2082844800ull;

// This was excluded from the public API, but is currently used by RFPM.
// See https://nitalk.jiveon.com/docs/DOC-462757#comment-334603
// begin private GetSelfCalibrateRangeState

/*- Time Structures and Helpers ----------------------------------*/

// Please visit ni.com/info and enter the Info Code NI_BTF for more information
#ifndef CVITime_DECLARED
#define CVITime_DECLARED
     typedef struct CVITime { ViUInt64 lsb; ViInt64 msb; } CVITime;
#endif
#ifndef CVIAbsoluteTime_DECLARED
#define CVIAbsoluteTime_DECLARED
     typedef union CVIAbsoluteTime { CVITime cviTime; ViUInt32 u32Data[4]; } CVIAbsoluteTime;
#endif

/*
 * Converts a timestamp to seconds and fractional seconds.
 */
ViStatus _VI_FUNC niRFSG_ValuesFromTimestamp(
   CVIAbsoluteTime timestamp,
   ViInt64* secondsSince1970,
   ViReal64* fractionalSeconds);
/*
 * Converts seconds and fractional seconds to a timestamp.
 */
ViStatus _VI_FUNC niRFSG_TimestampFromValues(
   ViInt64 secondsSince1970,
   ViReal64 fractionalSeconds,
   CVIAbsoluteTime* timestamp);

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*/
ViStatus _VI_FUNC niRFSG_GetSelfCalibrateRangeState
(
   ViSession vi,
   ViInt32 bufferSize,
   ViInt64 step[],
   CVIAbsoluteTime timestamp[],
   ViReal64 temperature[],
   ViReal64 minFrequency[],
   ViReal64 maxFrequency[],
   ViReal64 minReferenceLevel[],
   ViReal64 maxReferenceLevel[],
   ViInt32* actualDataSize
);

// end private GetSelfCalibrateRangeState

// Returns the number of ports in the currently selected de-embedding table.
// Used to resize the 2D array in LabVIEW for calls to niRFSA_GetDeembeddingSparameters
ViStatus _VI_FUNC niRFSG_GetDeembeddingTableNumberOfPorts(
   ViSession vi,
   ViInt32 *numberOfPorts);

// Calls to support creation of de-embedding S-parameter tables in RFmx SCPI API

ViStatus _VI_FUNC niRFSG_CreateDeembeddingSparameterTable(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   ViInt32 numberOfFrequencies,
   ViInt32 numberOfPorts);

ViStatus _VI_FUNC niRFSG_ConfigureSparameterTableFrequencies(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   const ViReal64 frequencies[], ViInt32 frequenciesSize);

ViStatus _VI_FUNC niRFSG_ConfigureSparameterTableSparameters(
   ViSession vi,
   ViConstString port,
   ViConstString tableName,
   const NIComplexNumber sparameterTable[], ViInt32 sparameterTableSize,
   ViInt32 sparameterOrientation);

ViStatus _VI_FUNC niRFSG_GetViSessionByName(
   ViRsrc resourceName,
   ViSession* existingVi);

ViStatus _VI_FUNC niRFSG_GetAssociatedDevicesForName
(
   ViConstString deviceName,
   ViUInt32 stringBufferSize,
   ViChar* associatedArb,
   ViChar* associatedLO,
   ViChar* associatedDevX,
   ViChar* associatedDevY,
   ViChar* associatedDevZ
);

ViStatus _VI_FUNC niRFSG_GetErrorUP
(
   ViSession   vi,
   ViStatus*   errorCodePtr,
   ViInt32     errorDescriptionBufferSize,
   ViChar      errorDescription[]
);

ViStatus _VI_FUNC niRFSG_GetTickCount
(
   ViSession vi,
   ViUInt64 *tickCountPtr,
   ViReal64 *secondsPerTickPtr
);

ViStatus _VI_FUNC niRFSG_GetAssociatedDevicesForGUID
(
   ViUInt32 configHandle,
   ViConstString deviceGUIDString,
   ViUInt32 stringBufferSize,
   ViChar* associatedArb,
   ViChar* associatedLO,
   ViChar* associatedDevX,
   ViChar* associatedDevY,
   ViChar* associatedDevZ
);

ViStatus _VI_FUNC niRFSG_SetAssociatedDevicesForGUID
(
   ViUInt32 configHandle,
   ViConstString deviceGUIDString,
   const ViChar* associatedArb,
   const ViChar* associatedLO,
   const ViChar* associatedDevX,
   const ViChar* associatedDevY,
   const ViChar* associatedDevZ
);

ViStatus _VI_FUNC niRFSG_GetWaveformNames
(
   ViSession vi,
   ViChar waveformNames[],
   ViInt32 bufferSize,
   ViInt32* actualBufferSize,
   ViInt32* numberOfWaveforms
);

// Remote entrypoints.
ViStatus _VI_FUNC InitializeSessionForServer
(
   ViRsrc resourceName,
   ViBoolean idQuery,
   ViBoolean resetDevice,
   ViConstString options,
   ViConstString additionalOpts,
   ViSession* newVi
);

ViStatus _VI_FUNC ReleaseSessionForServer
(
   ViSession vi
);

ViStatus _VI_FUNC niRFSG_StartDebugServer
(
   ViSession vi,
   ViRsrc resourceName
);

ViStatus _VI_FUNC niRFSG_RequestPrivilege
(
   ViSession vi,
   ViInt32 privilegeLevel
);

ViStatus _VI_FUNC niRFSG_GetOpenSessionsInformation
(
   ViRsrc resourceName,
   ViString infoJSON,
   ViUInt64 bufferSize,
   ViUInt64* bufferSizeNeededInBytes
);

ViStatus _VI_FUNC niRFSG_GetAttributeAuthor
(
   ViSession vi,
   ViConstString channelName,
   ViAttr attributeId,
   ViInt32* value
);

ViStatus _VI_FUNC niRFSG_GetAttributeContexts
(
   ViSession vi,
   ViAttr attributeId,
   ViInt32 bufSize,
   ViString contexts,
   ViInt32* requiredBufSize
);

ViStatus _VI_FUNC niRFSG_GetPrivilegeLevel
(
   ViSession vi,
   ViInt32* privilegeLevel
);

ViStatus _VI_FUNC niRFSG_GetSparameterTableS2pFilePathAndOrientation
(
    ViSession vi,
    ViConstString port,
    ViConstString tableName,
    ViInt32 filePathBufferSize,
    ViChar* s2pFilePath,
    ViInt32* requiredFilePathBufferSize,
    ViInt32* s2pOrientation
);

ViStatus _VI_FUNC niRFSG_GetDeembeddingTableNames
(
   ViSession vi,
   ViConstString port,
   ViChar tableNames[],
   ViInt32 bufferSize,
   ViInt32* actualBufferSize
);

ViStatus _VI_FUNC niRFSG_ExportConfigurationBuffer
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 size,
   ViChar* configuration,
   ViInt32* requiredSize
);

ViStatus _VI_FUNC niRFSG_ImportConfigurationBuffer
(
   ViSession vi,
   ViConstString channelName,
   ViInt32 size,
   ViChar* configuration
);

/*****************************************************************************
 *---------------------------- Internal Error Codes -------------------------*
 *****************************************************************************/
 // This document describes the IVI error ranges:
 //   P:\Measurements\Infrastructure\InstrDriverComponents\secm\export\100\100f1\documentation\ErrorsForNIInstrumentDrivers.doc

 // Sqeeze these between niFGEN and niRFSG public Errors/Warnings.           //IVI_SPECIFIC_ERROR_BASE + 0x200 == 0xbffa4200
#define NIRFSG_INTERNAL_ERROR_BASE                                            (IVI_SPECIFIC_ERROR_BASE + 0x200)
#define NIRFSG_INTERNAL_WARN_BASE                                             (IVI_SPECIFIC_WARN_BASE + 0x200)

#include "niRFSGPrivateErrors.h"

#if defined(__cplusplus) || defined(__cplusplus__)
}
#endif
#endif //___niRFSG_niRFSGPrivate_h___
````

<!--NI_OSS_SOURCE repo=grpc-device path=imports/include/niRFSGPrivateErrors.h sha256=7cdee69b6f7a0612efcb67843d93a2d92462ac8e9e2d0f08867516f658abb02a bytes=9301 -->
## FILE: imports/include/niRFSGPrivateErrors.h

- repository: `ni/grpc-device`
- source_path: `imports/include/niRFSGPrivateErrors.h`
- sha256: `7cdee69b6f7a0612efcb67843d93a2d92462ac8e9e2d0f08867516f658abb02a`
- bytes: 9301

````c
#ifndef ___niRFSG_niRFSGPrivateErrors_h___
#define ___niRFSG_niRFSGPrivateErrors_h___

/*******************************/
/*********** Errors ************/
/*******************************/

/* hex:0xBFFA4241 */
/* An internal hardware error has occurred.  A PLL lock error occurred.If the Frequency Settling Units property is set to Time After I/O, ensure that the Frequency Settling property is set to a value sufficient for this frequency change.Make sure the device has fully warmed up.  If self calibration is supported, self calibrate the device and attempt the operation again.  If the problem persists, contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_PLL_LOCK -1074118079

/* hex:0xBFFA4240 */
/* The calibration data is outside the DAC range.  No data was written to the EEPROM. */
#define NIRFSG_ERROR_CAL_DATA_OUTSIDE_DAC_RANGE -1074118080

/* hex:0xBFFA423F */
/* Harmonic peak lacks sufficient ampliturde or signal is not present. */
#define NIRFSG_ERROR_CAL_HARMONIC_NOT_MEASURABLE -1074118081

/* hex:0xBFFA423E */
/* Fundamental peak lacks sufficient amplitude or no signal is present. */
#define NIRFSG_ERROR_CAL_FUNDAMENTAL_NOT_MEASURABLE -1074118082

/* hex:0xBFFA423D */
/* The board read a bad temperature.  Please contact National Instruments Support. */
#define NIRFSG_ERROR_BAD_TEMPERATURE_READING -1074118083

/* hex:0xBFFA423C */
/* The option string has too many characters. */
#define NIRFSG_ERROR_OPTION_STRING_TOO_LONG -1074118084

/* hex:0xBFFA423A */
/* Simulation is not supported. */
#define NIRFSG_ERROR_SIMULATION_NOT_SUPPORTED -1074118086

/* hex:0xBFFA4239 */
/* The LO reported the following error: */
#define NIRFSG_ERROR_LO_ERROR -1074118087

/* hex:0xBFFA4238 */
/* Internal error (kNITNRErrorInternalEEPROMCommunicationFailure). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_EEPROM_COMMUNICATION_FAILURE -1074118088

/* hex:0xBFFA4237 */
/* Internal error (kNITNRErrorInternalMainPLLCommunicationFailure). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_MAIN_PLL_COMMUNICATION_FAILURE -1074118089

/* hex:0xBFFA4236 */
/* Internal error (kNITNRErrorInternalDDSCommunicationFailure). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_DDS_COMMUNICATION_FAILURE -1074118090

/* hex:0xBFFA4235 */
/* Internal error (kNITNRErrorInternalHardwareError). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_HARDWARE_ERROR -1074118091

/* hex:0xBFFA4234 */
/* Internal error (kNITNRErrorInternalCalibrationError). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_CALIBRATION_ERROR -1074118092

/* hex:0xBFFA4233 */
/* Internal error (kNITNRErrorInvalidCalibrationParam). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INVALID_CALIBRATION_PARAM -1074118093

/* hex:0xBFFA4232 */
/* Internal error (kNITNRErrorInvalidControlCode). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INVALID_CONTROL_CODE -1074118094

/* hex:0xBFFA4231 */
/* Internal error (kNITNRErrorInternalSoftwareError). Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_TNR_INTERNAL_SOFTWARE_ERROR -1074118095

/* hex:0xBFFA422A */
/* The type of modulation cannot be performed with the loop bandwidth setting requested. */
#define NIRFSG_ERROR_MODULATION_AND_LOOP_BANDWIDTH_INCOMPATIBLE -1074118102

/* hex:0xBFFA4229 */
/* A non-zero phase offset is not supported with modulation enabled. */
#define NIRFSG_ERROR_NONZERO_PHASE_OFFSET_WITH_MODULATION -1074118103

/* hex:0xBFFA4228 */
/* The detected hardware version is unsupported by this version of NI-RFSG.  Please upgrade to the latest NI-RFSG driver version. */
#define NIRFSG_ERROR_HARDWARE_TOO_NEW_FOR_DRIVER -1074118104

/* hex:0xBFFA4227 */
/* Timed out waiting for device power level to settle. */
#define NIRFSG_ERROR_565X_POWER_LEVEL_NOT_SETTLED -1074118105

/* hex:0xBFFA4226 */
/* Timed out waiting for device frequency to settle. */
#define NIRFSG_ERROR_565X_FREQUENCY_NOT_SETTLED -1074118106

/* hex:0xBFFA4225 */
/* Invalid PRBS seed for this PRBS order. At least one of the least-significant n bits of the seed must be non-zero, where 'n' is the PRBS order. */
#define NIRFSG_ERROR_PRBS_SEED_INVALID_FOR_PRBS_ORDER -1074118107

/* hex:0xBFFA4224 */
/* Power level is too low to be used with OOK modulation enabled. Increase the power level or disable OOK modulation. */
#define NIRFSG_ERROR_POWER_LEVEL_TOO_LOW_FOR_OOK -1074118108

/* hex:0xBFFA4210 */
/* The waveform input cluster contains no values. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21837 -1074118128

/* hex:0xBFFA420F */
/* The values of the dt element of the waveform cluster must be greater than 0. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21836 -1074118129

/* hex:0xBFFA420E */
/* The ratio of the old and new sample rates must be in the range of 1E-4 to 1E+4. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21863 -1074118130

/* hex:0xBFFA420D */
/* Resampling error: internal error. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21852 -1074118131

/* hex:0xBFFA420C */
/* Sample phase offset must be greater or equal to 0. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21851 -1074118132

/* hex:0xBFFA420B */
/* Sample rates must be greater than 0. */
#define NIRFSG_ERROR_INTERNAL_FRACTIONAL_RESAMPLING_21850 -1074118133

/* hex:0xBFFA420A */
/* Internal Driver Error: Function has not been implemented yet. */
#define NIRFSG_ERROR_FUNCTION_NOT_IMPLEMENTED_YET -1074118134

/* hex:0xBFFA4209 */
/* The upconverter reported the following error: */
#define NIRFSG_ERROR_UNMAPPED_5610_ERROR -1074118135

/* hex:0xBFFA4208 */
/* The AWG reported the following error: */
#define NIRFSG_ERROR_UNMAPPED_FGEN_ERROR -1074118136

/* hex:0xBFFA4207 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_FGEN -1074118137

/* hex:0xBFFA4205 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_INVALID_NUMBER_OF_CYCLES -1074118139

/* hex:0xBFFA4204 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_PARSING_OPTIONS_STRING -1074118140

/* hex:0xBFFA4203 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_VALUE_OUT_OF_RANGE -1074118141

/* hex:0xBFFA4202 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_WAVEFORM_NOT_FOUND -1074118142

/* hex:0xBFFA4201 */
/* An internal software error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_INVALID_PARAMETER -1074118143

/* hex:0xBFFA4200 */
/* An internal error has occurred. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_ERROR_INTERNAL_ERROR -1074118144

/*********************************/
/*********** Warnings ************/
/*********************************/

/* hex:0x3FFA4200 */
/* An internal warning was generated. Contact National Instruments technical support at ni.com/support. */
#define NIRFSG_WARN_INTERNAL_WARNING 1073365504

/* hex:0x3FFA4201 */
/* The AWG reported the following warning: */
#define NIRFSG_WARN_UNMAPPED_FGEN_WARNING 1073365505

/* hex:0x3FFA4202 */
/* The upconverter reported the following warning: */
#define NIRFSG_WARN_UNMAPPED_5610_WARNING 1073365506

/* hex:0x3FFA4203 */
/* FIR Calibration constants are invalid. Perform an external calibration.Contact National Instruments Technical Support if you need additional information. */
#define NIRFSG_WARN_INTERNAL_FAKE_IF_CALIBRATION 1073365507

/* hex:0x3FFA4204 */
/* An internal device setting is out of range.  This could be due to calibration problems or compensation for extreme temperatures.  The device setting was coerced to the maximum or minimum supported value.  Device performance is not guaranteed. */
#define NIRFSG_WARN_INTERNAL_SETTING_OUT_OF_RANGE 1073365508

/* hex:0x3FFA4210 */
/* Requested attribute value exceeds device specification limits. Device performance is not guaranteed. */
#define NIRFSG_WARN_DEVICE_SPECIFICATIONS_EXCEEDED 1073365520

/* hex:0x3FFA4211 */
/* While averaging temperature sensor readings, found more variation in the readings than expected.  Temperature reading may not be accurate. */
#define NIRFSG_WARN_INCONSISTENT_TEMPERATURE_READING 1073365521

/* hex:0x3FFA4212 */
/* The LO reported the following warning: */
#define NIRFSG_WARN_LO_WARNING 1073365522

#endif /* ___niRFSG_niRFSGPrivateErrors_h___ */
````
