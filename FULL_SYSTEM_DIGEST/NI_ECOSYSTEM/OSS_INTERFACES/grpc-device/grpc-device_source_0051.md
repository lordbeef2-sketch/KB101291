# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/enums.py sha256=b55e0314316a67590d79b5250d199a27f1dfe35e8dd9aa6a2bb9ef6a98fd7b36 bytes=43636 -->
## FILE: source/codegen/metadata/nirfmxwlan/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/enums.py`
- sha256: `b55e0314316a67590d79b5250d199a27f1dfe35e8dd9aa6a2bb9ef6a98fd7b36`
- bytes: 43636

````python
enums = {
    'DigitalEdgeTriggerEdge': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'DigitalEdgeTriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'name': 'PULSE_IN',
                'value': 'PulseIn'
            },
            {
                'name': 'DIO_PFI0',
                'value': 'DIO/PFI0'
            },
            {
                'name': 'DIO_PFI1',
                'value': 'DIO/PFI1'
            },
            {
                'name': 'DIO_PFI2',
                'value': 'DIO/PFI2'
            },
            {
                'name': 'DIO_PFI3',
                'value': 'DIO/PFI3'
            },
            {
                'name': 'DIO_PFI4',
                'value': 'DIO/PFI4'
            },
            {
                'name': 'DIO_PFI5',
                'value': 'DIO/PFI5'
            },
            {
                'name': 'DIO_PFI6',
                'value': 'DIO/PFI6'
            },
            {
                'name': 'DIO_PFI7',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'DsssModAccAcquisitionLengthMode': {
        'enum-value-prefix': 'DSSSMODACC_ACQUISITION_LENGTH_MODE',
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'DsssModAccAveragingEnabled': {
        'enum-value-prefix': 'DSSSMODACC_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccBurstStartDetectionEnabled': {
        'enum-value-prefix': 'DSSSMODACC_BURST_START_DETECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccChipClockErrorCorrectionEnabled': {
        'enum-value-prefix': 'DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccDataDecodingEnabled': {
        'enum-value-prefix': 'DSSSMODACC_DATA_DECODING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccDataModulationFormat': {
        'enum-value-prefix': 'DSSSMODACC_DATA_MODULATION_FORMAT',
        'values': [
            {
                'name': 'DSSS1MBPS',
                'value': 0
            },
            {
                'name': 'DSSS2MBPS',
                'value': 1
            },
            {
                'name': 'CCK5_5MBPS',
                'value': 2
            },
            {
                'name': 'CCK11MBPS',
                'value': 3
            },
            {
                'name': 'PBCC5_5MBPS',
                'value': 4
            },
            {
                'name': 'PBCC11MBPS',
                'value': 5
            },
            {
                'name': 'PBCC22MBPS',
                'value': 6
            },
            {
                'name': 'PBCC33MBPS',
                'value': 7
            }
        ]
    },
    'DsssModAccEqualizationEnabled': {
        'enum-value-prefix': 'DSSSMODACC_EQUALIZATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccEvmUnit': {
        'enum-value-prefix': 'DSSSMODACC_EVM_UNIT',
        'values': [
            {
                'name': 'PERCENTAGE',
                'value': 0
            },
            {
                'name': 'DB',
                'value': 1
            }
        ]
    },
    'DsssModAccFrequencyErrorCorrectionEnabled': {
        'enum-value-prefix': 'DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccIQOriginOffsetCorrectionEnabled': {
        'enum-value-prefix': 'DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccPayloadHeaderCrcStatus': {
        'enum-value-prefix': 'DSSSMODACC_PAYLOAD_HEADER_CRC_STATUS',
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'DsssModAccPowerMeasurementEnabled': {
        'enum-value-prefix': 'DSSSMODACC_POWER_MEASUREMENT_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DsssModAccPreambleType': {
        'enum-value-prefix': 'DSSSMODACC_PREAMBLE_TYPE',
        'values': [
            {
                'name': 'LONG',
                'value': 0
            },
            {
                'name': 'SHORT',
                'value': 1
            }
        ]
    },
    'DsssModAccPsduCrcStatus': {
        'enum-value-prefix': 'DSSSMODACC_PSDU_CRC_STATUS',
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'DsssModAccPulseShapingFilterType': {
        'enum-value-prefix': 'DSSSMODACC_PULSE_SHAPING_FILTER_TYPE',
        'values': [
            {
                'name': 'RECTANGULAR',
                'value': 0
            },
            {
                'name': 'RAISED_COSINE',
                'value': 1
            },
            {
                'name': 'ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'name': 'GAUSSIAN',
                'value': 3
            }
        ]
    },
    'DsssModAccSpectrumInverted': {
        'enum-value-prefix': 'DSSSMODACC_SPECTRUM_INVERTED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'FrequencyReferenceSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'name': 'REF_IN',
                'value': 'RefIn'
            },
            {
                'name': 'PXI_CLK',
                'value': 'PXI_Clk'
            },
            {
                'name': 'CLK_IN',
                'value': 'ClkIn'
            }
        ]
    },
    'IQPowerEdgeTriggerLevelType': {
        'values': [
            {
                'name': 'RELATIVE',
                'value': 0
            },
            {
                'name': 'ABSOLUTE',
                'value': 1
            }
        ]
    },
    'IQPowerEdgeTriggerSlope': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'LimitedConfigurationChange': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'NO_CHANGE',
                'value': 1
            },
            {
                'name': 'FREQUENCY',
                'value': 2
            },
            {
                'name': 'REFERENCE_LEVEL',
                'value': 3
            },
            {
                'name': 'FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 4
            },
            {
                'name': 'SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 5
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'TXP',
                'value': 1
            },
            {
                'name': 'POWERRAMP',
                'value': 2
            },
            {
                'name': 'DSSSMODACC',
                'value': 4
            },
            {
                'name': 'OFDMMODACC',
                'value': 8
            },
            {
                'name': 'SEM',
                'value': 16
            }
        ]
    },
    'MechanicalAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'Ofdm2xLdpcEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmAutoPhaseRotationDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmAutoPpduTypeDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmDcmEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmFecCodingType': {
        'values': [
            {
                'name': 'BCC',
                'value': 0
            },
            {
                'name': 'LDPC',
                'value': 1
            }
        ]
    },
    'OfdmFrequencyBand': {
        'values': [
            {
                'name': '2_4GHZ',
                'value': 0
            },
            {
                'name': '5GHZ',
                'value': 1
            }
        ]
    },
    'OfdmGuardIntervalType': {
        'values': [
            {
                'name': '1_4',
                'value': 0
            },
            {
                'name': '1_8',
                'value': 1
            },
            {
                'name': '1_16',
                'value': 2
            }
        ]
    },
    'OfdmHeaderDecodingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmIMPilotsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmLtfSize': {
        'values': [
            {
                'name': '4X',
                'value': 0
            },
            {
                'name': '2X',
                'value': 1
            },
            {
                'name': '1X',
                'value': 2
            },
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            }
        ]
    },
    'OfdmMUMimoLtfModeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAcc2xLdpcEnabled': {
        'enum-value-prefix': 'OFDMMODACC2X_LDPC_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccAcquisitionLengthMode': {
        'enum-value-prefix': 'OFDMMODACC_ACQUISITION_LENGTH_MODE',
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'OfdmModAccAmplitudeTrackingEnabled': {
        'enum-value-prefix': 'OFDMMODACC_AMPLITUDE_TRACKING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccAutoLevelAllowOverflow': {
        'enum-value-prefix': 'OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccAveragingEnabled': {
        'enum-value-prefix': 'OFDMMODACC_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccAveragingType': {
        'enum-value-prefix': 'OFDMMODACC_AVERAGING_TYPE',
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'VECTOR',
                'value': 5
            }
        ]
    },
    'OfdmModAccBurstStartDetectionEnabled': {
        'enum-value-prefix': 'OFDMMODACC_BURST_START_DETECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccCalibrationDataValid': {
        'enum-value-prefix': 'OFDMMODACC_CALIBRATION_DATA_VALID',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccChannelEstimationInterpolationType': {
        'enum-value-prefix': 'OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE',
        'values': [
            {
                'name': 'LINEAR',
                'value': 0
            },
            {
                'name': 'TRIANGULAR_SMOOTHING',
                'value': 1
            },
            {
                'name': 'WIENER_FILTER',
                'value': 2
            }
        ]
    },
    'OfdmModAccChannelEstimationLLtfEnabled': {
        'enum-value-prefix': 'OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccChannelEstimationLtfAveragingEnabled': {
        'enum-value-prefix': 'OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccChannelEstimationType': {
        'enum-value-prefix': 'OFDMMODACC_CHANNEL_ESTIMATION_TYPE',
        'values': [
            {
                'name': 'REFERENCE',
                'value': 0
            },
            {
                'name': 'REFERENCE_AND_DATA',
                'value': 1
            }
        ]
    },
    'OfdmModAccChannelMatrixPowerEnabled': {
        'enum-value-prefix': 'OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccCombinedSignalDemodulationEnabled': {
        'enum-value-prefix': 'OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccCommonClockSourceEnabled': {
        'enum-value-prefix': 'OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccCommonPilotErrorScalingReference': {
        'enum-value-prefix': 'OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE',
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'AVERAGE_CPE',
                'value': 1
            }
        ]
    },
    'OfdmModAccDataDecodingEnabled': {
        'enum-value-prefix': 'OFDMMODACC_DATA_DECODING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccDcmEnabled': {
        'enum-value-prefix': 'OFDMMODACC_DCM_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccEhtSigCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_EHT_SIG_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccElrSigCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_ELR_SIG_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccEvmReferenceDataSymbolsMode': {
        'enum-value-prefix': 'OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE',
        'values': [
            {
                'name': 'ACQUIRED_WAVEFORM',
                'value': 0
            },
            {
                'name': 'REFERENCE_WAVEFORM',
                'value': 1
            }
        ]
    },
    'OfdmModAccEvmUnit': {
        'enum-value-prefix': 'OFDMMODACC_EVM_UNIT',
        'values': [
            {
                'name': 'PERCENTAGE',
                'value': 0
            },
            {
                'name': 'DB',
                'value': 1
            }
        ]
    },
    'OfdmModAccFecCodingType': {
        'enum-value-prefix': 'OFDMMODACC_FEC_CODING_TYPE',
        'values': [
            {
                'name': 'BCC',
                'value': 0
            },
            {
                'name': 'LDPC',
                'value': 1
            }
        ]
    },
    'OfdmModAccFrequencyErrorEstimationMethod': {
        'enum-value-prefix': 'OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD',
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'INITIAL_PREAMBLE',
                'value': 1
            },
            {
                'name': 'PREAMBLE',
                'value': 2
            },
            {
                'name': 'PREAMBLE_AND_PILOTS',
                'value': 3
            },
            {
                'name': 'PREAMBLE_PILOTS_AND_DATA',
                'value': 4
            }
        ]
    },
    'OfdmModAccIMPilotsEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IM_PILOTS_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQGainImbalanceCorrectionEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQImpairmentsEstimationEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQImpairmentsModel': {
        'enum-value-prefix': 'OFDMMODACC_IQ_IMPAIRMENTS_MODEL',
        'values': [
            {
                'name': 'TX',
                'value': 0
            },
            {
                'name': 'RX',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQImpairmentsPerSubcarrierEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQQuadratureErrorCorrectionEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccIQTimingSkewCorrectionEnabled': {
        'enum-value-prefix': 'OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccLSigParityCheckStatus': {
        'enum-value-prefix': 'OFDMMODACC_L_SIG_PARITY_CHECK_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccMeasurementMode': {
        'enum-value-prefix': 'OFDMMODACC_MEASUREMENT_MODE',
        'values': [
            {
                'name': 'MEASURE',
                'value': 0
            },
            {
                'name': 'CALIBRATE_NOISE_FLOOR',
                'value': 1
            }
        ]
    },
    'OfdmModAccNoiseCompensationApplied': {
        'enum-value-prefix': 'OFDMMODACC_NOISE_COMPENSATION_APPLIED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccNoiseCompensationEnabled': {
        'enum-value-prefix': 'OFDMMODACC_NOISE_COMPENSATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccNoiseCompensationInputPowerCheckEnabled': {
        'enum-value-prefix': 'OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccOptimizeDynamicRangeForEvmEnabled': {
        'enum-value-prefix': 'OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPhaseRotationCoefficient1': {
        'enum-value-prefix': 'OFDMMODACC_PHASE_ROTATION_COEFFICIENT_1',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPhaseRotationCoefficient2': {
        'enum-value-prefix': 'OFDMMODACC_PHASE_ROTATION_COEFFICIENT_2',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPhaseRotationCoefficient3': {
        'enum-value-prefix': 'OFDMMODACC_PHASE_ROTATION_COEFFICIENT_3',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPhaseTrackingEnabled': {
        'enum-value-prefix': 'OFDMMODACC_PHASE_TRACKING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPowerMeasurementEnabled': {
        'enum-value-prefix': 'OFDMMODACC_POWER_MEASUREMENT_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccPsduCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_PSDU_CRC_STATUS',
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccRUType': {
        'enum-value-prefix': 'OFDMMODACC_RU_TYPE',
        'values': [
            {
                'name': 'RRU',
                'value': 0
            },
            {
                'name': 'DRU',
                'value': 1
            }
        ]
    },
    'OfdmModAccSigBCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_SIG_B_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccSigCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_SIG_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccSpectrumInverted': {
        'enum-value-prefix': 'OFDMMODACC_SPECTRUM_INVERTED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccSymbolClockErrorCorrectionEnabled': {
        'enum-value-prefix': 'OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccUSigCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_U_SIG_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccUhrSigCrcStatus': {
        'enum-value-prefix': 'OFDMMODACC_UHR_SIG_CRC_STATUS',
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'OfdmModAccUnequalModulationEnabled': {
        'enum-value-prefix': 'OFDMMODACC_UNEQUAL_MODULATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccUnusedToneErrorMaskReference': {
        'enum-value-prefix': 'OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE',
        'values': [
            {
                'name': 'LIMIT1',
                'value': 0
            },
            {
                'name': 'LIMIT2',
                'value': 1
            }
        ]
    },
    'OfdmModAccVectorAveragingPhaseAlignmentEnabled': {
        'enum-value-prefix': 'OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmModAccVectorAveragingTimeAlignmentEnabled': {
        'enum-value-prefix': 'OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmPhaseRotationCoefficient1': {
        'enum-value-prefix': 'OFDM_PHASE_ROTATION_COEFFICIENT_1',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmPhaseRotationCoefficient2': {
        'enum-value-prefix': 'OFDM_PHASE_ROTATION_COEFFICIENT_2',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmPhaseRotationCoefficient3': {
        'enum-value-prefix': 'OFDM_PHASE_ROTATION_COEFFICIENT_3',
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'OfdmPpduType': {
        'values': [
            {
                'name': 'NON_HT',
                'value': 0
            },
            {
                'name': 'MIXED',
                'value': 1
            },
            {
                'name': 'GREENFIELD',
                'value': 2
            },
            {
                'name': 'SU',
                'value': 3
            },
            {
                'name': 'MU',
                'value': 4
            },
            {
                'name': 'EXTENDED_RANGE_SU',
                'value': 5
            },
            {
                'name': 'TRIGGER_BASED',
                'value': 6
            },
            {
                'name': 'ELR',
                'value': 7
            }
        ]
    },
    'OfdmPreamblePuncturingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmRUType': {
        'values': [
            {
                'name': 'RRU',
                'value': 0
            },
            {
                'name': 'DRU',
                'value': 1
            }
        ]
    },
    'OfdmSigCompressionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmStbcEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OfdmTransmitPowerClass': {
        'values': [
            {
                'name': 'A',
                'value': 0
            },
            {
                'name': 'B',
                'value': 1
            },
            {
                'name': 'C',
                'value': 2
            },
            {
                'name': 'D',
                'value': 3
            }
        ]
    },
    'OfdmUnequalModulationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PowerRampAveragingEnabled': {
        'enum-value-prefix': 'POWERRAMP_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'RFAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemAmplitudeCorrectionType': {
        'values': [
            {
                'name': 'RF_CENTER_FREQUENCY',
                'value': 0
            },
            {
                'name': 'SPECTRUM_FREQUENCY_BIN',
                'value': 1
            }
        ]
    },
    'SemAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            },
            {
                'name': 'SCALAR',
                'value': 2
            },
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            }
        ]
    },
    'SemLowerOffsetMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'SemMaskType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            }
        ]
    },
    'SemMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'SemOffsetSideband': {
        'values': [
            {
                'name': 'NEGATIVE',
                'value': 0
            },
            {
                'name': 'POSITIVE',
                'value': 1
            },
            {
                'name': 'BOTH',
                'value': 2
            }
        ]
    },
    'SemSpanAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemSweepTimeAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemUpperOffsetMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'Standard': {
        'values': [
            {
                'name': '802_11_AG',
                'value': 0
            },
            {
                'name': '802_11_B',
                'value': 1
            },
            {
                'name': '802_11_J',
                'value': 2
            },
            {
                'name': '802_11_P',
                'value': 3
            },
            {
                'name': '802_11_N',
                'value': 4
            },
            {
                'name': '802_11_AC',
                'value': 5
            },
            {
                'name': '802_11_AX',
                'value': 6
            },
            {
                'name': '802_11_BE',
                'value': 7
            },
            {
                'name': '802_11_BN',
                'value': 8
            },
            {
                'name': 'UNKNOWN',
                'value': -1
            }
        ]
    },
    'TriggerGateEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'TriggerMinimumQuietTimeMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'name': 'IQ_POWER_EDGE',
                'value': 2
            },
            {
                'name': 'SOFTWARE',
                'value': 3
            }
        ]
    },
    'TxpAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'TxpBurstDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nirfmxwlan/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/functions.py sha256=961df2f6b57e9e84c42deb1b7eeeac07a02dd0d38c081317d9e9aa3822b8c07b bytes=295844 -->
## FILE: source/codegen/metadata/nirfmxwlan/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/functions.py`
- sha256: `961df2f6b57e9e84c42deb1b7eeeac07a02dd0d38c081317d9e9aa3822b8c07b`
- bytes: 295844

````python
functions = {
    'AbortMeasurements': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1Waveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1WaveformInterleavedIQ': {
        'cname': 'RFmxWLAN_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(iq)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1WaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iqi',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'iqq',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeNWaveformsIQ': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'iqSize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'iq_sizes',
                'name': 'iqSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeNWaveformsIQInterleavedIQ': {
        'cname': 'RFmxWLAN_AnalyzeNWaveformsIQ',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'iqSize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(iq)'
            },
            {
                'direction': 'in',
                'grpc_name': 'iq_sizes',
                'name': 'iqSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeNWaveformsIQSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'iqi',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'iqq',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'iq_sizes',
                'name': 'iqSize',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeNWaveformsSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'spectrumSize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'spectrum_sizes',
                'name': 'spectrumSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeSpectrum1Waveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AutoDetectSignal': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AutoDetectSignalAnalysisOnly': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AutoDetectSignalAnalysisOnlyInterleavedIQ': {
        'cname': 'RFmxWLAN_AutoDetectSignalAnalysisOnly',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(iq)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            }
        ],
        'returns': 'int32'
    },
    'AutoDetectSignalAnalysisOnlySplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iqi',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'iqq',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AutoLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementInterval',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'BuildChainString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'chainNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildGateString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'gateNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildOffsetString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildSegmentString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'segmentNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildSignalString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'selectorStringLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildStreamString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'streamNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildUserString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'userNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgChannelBandwidth': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'channelBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgDigitalEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerSource',
                'name': 'digitalEdgeSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerEdge',
                'name': 'digitalEdge',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'centerFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequencyArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'centerFrequency',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequencyReference': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FrequencyReferenceSource',
                'name': 'frequencyReferenceSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequencyReferenceFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgIQPowerEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'iqPowerEdgeSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'IQPowerEdgeTriggerSlope',
                'name': 'iqPowerEdgeSlope',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'iqPowerEdgeLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'TriggerMinimumQuietTimeMode',
                'name': 'triggerMinQuietTimeMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'triggerMinQuietTimeDuration',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'IQPowerEdgeTriggerLevelType',
                'name': 'iqPowerEdgeLevelType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgMechanicalAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MechanicalAttenuationAuto',
                'name': 'mechanicalAttenuationAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'mechanicalAttenuationValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfFrequencySegmentsAndReceiveChains': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfFrequencySegments',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfReceiveChains',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgRFAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'RFAttenuationAuto',
                'name': 'rfAttenuationAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rfAttenuationValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgReferenceLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgSelectedPortsMultiple': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'selectedPorts',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgSoftwareEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgStandard': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'Standard',
                'name': 'standard',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CheckMeasurementStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ClearAllNamedResults': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'ClearNamedResult': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CloneSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'oldSignalName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'newSignalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'Close': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'forceDestroy',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'Commit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CreateSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgAcquisitionLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DsssModAccAcquisitionLengthMode',
                'name': 'acquisitionLengthMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'acquisitionLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DsssModAccAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgEVMUnit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DsssModAccEvmUnit',
                'name': 'evmUnit',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgMeasurementLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'maximumMeasurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgPowerMeasurementCustomGateArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'startTime',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'stopTime',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgPowerMeasurementEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DsssModAccPowerMeasurementEnabled',
                'name': 'powerMeasurementEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccCfgPowerMeasurementNumberOfCustomGates': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfCustomGates',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchAveragePowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'preambleAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headerAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ppduAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_DSSSModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(constellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'constellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchCustomGatePowersArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakPowerMaximum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchDecodedHeaderBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'decodedHeaderBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchDecodedPSDUBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'decodedPSDUBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rms_evm_mean',
                'name': 'rmsevmMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'peak_evm_80211_2016_maximum',
                'name': 'peakEVM80211_2016Maximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'peak_evm_80211_2007_maximum',
                'name': 'peakEVM80211_2007Maximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'peak_evm_80211_1999_maximum',
                'name': 'peakEVM80211_1999Maximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyErrorMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'chipClockErrorMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberOfChipsUsed',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchEVMPerChipMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'evmPerChipMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqOriginOffsetMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalanceMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureErrorMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchPPDUInformation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'DsssModAccDataModulationFormat',
                'name': 'dataModulationFormat',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'payloadLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'DsssModAccPreambleType',
                'name': 'preambleType',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'lockedClocksBit',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'DsssModAccPayloadHeaderCrcStatus',
                'name': 'headerCRCStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'DsssModAccPsduCrcStatus',
                'grpc_name': 'psdu_crc_status',
                'name': 'psducrcStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DSSSModAccFetchPeakPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'preamblePeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headerPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ppduPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DeleteSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'DisableTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAllNamedResultNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'resultNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'resultNamesBufferSize',
                    'value_twist': 'actualResultNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultNamesBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualResultNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'defaultResultExists',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int16'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int8'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeNIComplexDoubleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeNIComplexSingleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt16'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt8'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'Initialize': {
        'custom_close': 'Close(id, RFMXWLAN_VAL_FALSE)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'instrument',
                'name': 'handleOut',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'isNewSession',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'char[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'InitializeFromNIRFSASession': {
        'custom_close': 'Close(id, RFMXWLAN_VAL_FALSE)',
        'init_method': True,
        'parameters': [
            {
                'cross_driver_session': 'ViSession',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'nirfsaSession',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'grpc_name': 'instrument',
                'name': 'handleOut',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'char[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'Initiate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccAutoLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfg1ReferenceWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfg1ReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccCfg1ReferenceWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(referenceWaveform)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfg1ReferenceWaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveformI',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveformQ',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgAcquisitionLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccAcquisitionLengthMode',
                'name': 'acquisitionLengthMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'acquisitionLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgAmplitudeTrackingEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccAmplitudeTrackingEnabled',
                'name': 'amplitudeTrackingEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgChannelEstimationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccChannelEstimationType',
                'name': 'channelEstimationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgCommonClockSourceEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccCommonClockSourceEnabled',
                'name': 'commonClockSourceEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgEVMUnit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccEvmUnit',
                'name': 'evmUnit',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgFrequencyErrorEstimationMethod': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccFrequencyErrorEstimationMethod',
                'name': 'frequencyErrorEstimationMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgMeasurementLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'maximumMeasurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgMeasurementMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccMeasurementMode',
                'name': 'measurementMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgNReferenceWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveform',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'referenceWaveformSize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'reference_waveform_sizes',
                'name': 'referenceWaveformSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgNReferenceWaveformsInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccCfgNReferenceWaveforms',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveform',
                'size': {
                    'mechanism': 'two-dimension',
                    'value': 'referenceWaveformSize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(referenceWaveform)'
            },
            {
                'direction': 'in',
                'grpc_name': 'reference_waveform_sizes',
                'name': 'referenceWaveformSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgNReferenceWaveformsSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveformI',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'referenceWaveformQ',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'reference_waveform_sizes',
                'name': 'referenceWaveformSize',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgNoiseCompensationEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccNoiseCompensationEnabled',
                'name': 'noiseCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgOptimizeDynamicRangeForEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccOptimizeDynamicRangeForEvmEnabled',
                'name': 'optimizeDynamicRangeForEVMEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'optimizeDynamicRangeForEVMMargin',
                'type': 'double'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgPhaseTrackingEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccPhaseTrackingEnabled',
                'name': 'phaseTrackingEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccCfgSymbolClockErrorCorrectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OfdmModAccSymbolClockErrorCorrectionEnabled',
                'name': 'symbolClockErrorCorrectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccClearNoiseCalibrationDatabase': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChainDataRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_data_rms_evm_per_symbol_mean',
                'name': 'chainDataRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChainPilotRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_pilot_rms_evm_per_symbol_mean',
                'name': 'chainPilotRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChainRMSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_rms_evm_mean',
                'name': 'chainRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_data_rms_evm_mean',
                'name': 'chainDataRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_pilot_rms_evm_mean',
                'name': 'chainPilotRMSEVMMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChainRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_rms_evm_per_subcarrier_mean',
                'name': 'chainRMSEVMPerSubcarrierMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChainRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'chain_rms_evm_per_symbol_mean',
                'name': 'chainRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchChannelFrequencyResponseMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'channelFrequencyResponseMeanMagnitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'channelFrequencyResponseMeanPhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchCommonPilotErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'commonPilotErrorMagnitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'commonPilotErrorPhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchCompositeRMSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'composite_rms_evm_mean',
                'name': 'compositeRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'composite_data_rms_evm_mean',
                'name': 'compositeDataRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'composite_pilot_rms_evm_mean',
                'name': 'compositePilotRMSEVMMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchCrossPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'crossPowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchCustomGatePowersArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakPowerMaximum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDataAveragePower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccFetchDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDataPeakPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedEHTSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_eht_sig_bits',
                'name': 'decodedEHTSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedELRSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_elr_sig_bits',
                'name': 'decodedELRSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedLSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_l_sig_bits',
                'name': 'decodedLSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedPSDUBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'decodedPSDUBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedSIGBBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_sig_b_bits',
                'name': 'decodedSIGBBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'decodedSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedServiceBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'decodedServiceBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedUHRSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_uhr_sig_bits',
                'name': 'decodedUHRSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchDecodedUSIGBitsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'decoded_u_sig_bits',
                'name': 'decodedUSIGBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchEVMSubcarrierIndices': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subcarrierIndices',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchFrequencyErrorCCDF10Percent': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'frequency_error_ccdf_10_percent',
                'name': 'frequencyErrorCCDF10Percent',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchFrequencyErrorMean': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyErrorMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchGroupDelayMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'groupDelayMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchGuardIntervalType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmGuardIntervalType',
                'name': 'guardIntervalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchIQGainImbalancePerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalancePerSubcarrierMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativeIQOriginOffsetMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalanceMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureErrorMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absoluteIQOriginOffsetMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqTimingSkewMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureErrorPerSubcarrierMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchLSIGParityCheckStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmModAccLSigParityCheckStatus',
                'grpc_name': 'l_sig_parity_check_status',
                'name': 'lsigParityCheckStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchLTFSize': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmLtfSize',
                'name': 'ltfSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchMCSIndex': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'mcsIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchNumberOfHESIGBSymbols': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'number_of_he_sig_b_symbols',
                'name': 'numberOfHESIGBSymbols',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchNumberOfSpaceTimeStreams': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberOfSpaceTimeStreams',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchNumberOfUsers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberOfUsers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchNumberofSymbolsUsed': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberOfSymbolsUsed',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPEAveragePower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPEDuration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peDuration',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPEPeakPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pePeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPPDUAveragePower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ppduAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPPDUPeakPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ppduPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPPDUType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmPpduType',
                'name': 'ppduType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPSDUCRCStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmModAccPsduCrcStatus',
                'grpc_name': 'psdu_crc_status',
                'name': 'psducrcStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPhaseNoisePSDMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'phaseNoisePSDMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPilotConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pilotConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPilotConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPilotConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pilotConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pilotConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPilotConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pilotConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pilotConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleAveragePowers80211ac': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ac',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_sig_a_average_power_mean',
                'name': 'vhtsigaAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_stf_average_power_mean',
                'name': 'vhtstfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_ltf_average_power_mean',
                'name': 'vhtltfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_sig_b_average_power_mean',
                'name': 'vhtsigbAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleAveragePowers80211ax': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11ax',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rl_sig_average_power_mean',
                'name': 'rlsigAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_sig_a_average_power_mean',
                'name': 'hesigaAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_sig_b_average_power_mean',
                'name': 'hesigbAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_stf_average_power_mean',
                'name': 'hestfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_ltf_average_power_mean',
                'name': 'heltfAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleAveragePowers80211be': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11be',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rl_sig_average_power_mean',
                'name': 'rlsigAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'u_sig_average_power_mean',
                'name': 'usigAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_sig_average_power_mean',
                'name': 'ehtsigAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_stf_average_power_mean',
                'name': 'ehtstfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_ltf_average_power_mean',
                'name': 'ehtltfAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleAveragePowers80211n': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreambleAveragePowers802_11n',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_sig_average_power_mean',
                'name': 'htsigAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_stf_average_power_mean',
                'name': 'htstfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_dltf_average_power_mean',
                'name': 'htdltfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_eltf_average_power_mean',
                'name': 'hteltfAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleAveragePowersCommon': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_stf_average_power_mean',
                'name': 'lstfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_ltf_average_power_mean',
                'name': 'lltfAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_sig_average_power_mean',
                'name': 'lsigAveragePowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreambleFrequencyErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'preambleFrequencyError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreamblePeakPowers80211ac': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ac',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_sig_a_peak_power_maximum',
                'name': 'vhtsigaPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_stf_peak_power_maximum',
                'name': 'vhtstfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_ltf_peak_power_maximum',
                'name': 'vhtltfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'vht_sig_b_peak_power_maximum',
                'name': 'vhtsigbPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreamblePeakPowers80211ax': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11ax',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rl_sig_peak_power_maximum',
                'name': 'rlsigPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_sig_a_peak_power_maximum',
                'name': 'hesigaPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_sig_b_peak_power_maximum',
                'name': 'hesigbPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_stf_peak_power_maximum',
                'name': 'hestfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'he_ltf_peak_power_maximum',
                'name': 'heltfPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreamblePeakPowers80211be': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11be',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rl_sig_peak_power_maximum',
                'name': 'rlsigPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'u_sig_peak_power_maximum',
                'name': 'usigPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_sig_peak_power_maximum',
                'name': 'ehtsigPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_stf_peak_power_maximum',
                'name': 'ehtstfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'eht_ltf_peak_power_maximum',
                'name': 'ehtltfPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreamblePeakPowers80211n': {
        'cname': 'RFmxWLAN_OFDMModAccFetchPreamblePeakPowers802_11n',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_sig_peak_power_maximum',
                'name': 'htsigPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_stf_peak_power_maximum',
                'name': 'htstfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_dltf_peak_power_maximum',
                'name': 'htdltfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'ht_eltf_peak_power_maximum',
                'name': 'hteltfPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchPreamblePeakPowersCommon': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_stf_peak_power_maximum',
                'name': 'lstfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_ltf_peak_power_maximum',
                'name': 'lltfPeakPowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'l_sig_peak_power_maximum',
                'name': 'lsigPeakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchRUOffsetAndSize': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ruOffset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'ruSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchReferenceDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchReferenceDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccFetchReferenceDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(referenceDataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchReferenceDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceDataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'referenceDataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSIGBCRCStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmModAccSigBCrcStatus',
                'grpc_name': 'sig_b_crc_status',
                'name': 'sigbcrcStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSIGCRCStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'OfdmModAccSigCrcStatus',
                'grpc_name': 'sig_crc_status',
                'name': 'sigcrcStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSpectralFlatness': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectralFlatnessMargin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectralFlatnessMarginSubcarrierIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSpectralFlatnessMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectralFlatnessMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'spectralFlatnessLowerMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'spectralFlatnessUpperMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchStreamDataRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_data_rms_evm_per_symbol_mean',
                'name': 'streamDataRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchStreamPilotRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_pilot_rms_evm_per_symbol_mean',
                'name': 'streamPilotRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchStreamRMSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_rms_evm_mean',
                'name': 'streamRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_data_rms_evm_mean',
                'name': 'streamDataRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_pilot_rms_evm_mean',
                'name': 'streamPilotRMSEVMMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchStreamRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_rms_evm_per_subcarrier_mean',
                'name': 'streamRMSEVMPerSubcarrierMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchStreamRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'stream_rms_evm_per_symbol_mean',
                'name': 'streamRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSubcarrierChainEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'subcarrierIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subcarrierChainEVMPerSymbol',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSubcarrierStreamEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'subcarrierIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subcarrierStreamEVMPerSymbol',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSymbolChainEVMPerSubcarrierTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'symbolIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolChainEVMPerSubcarrier',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSymbolClockErrorMean': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolClockErrorMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchSymbolStreamEVMPerSubcarrierTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'symbolIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolStreamEVMPerSubcarrier',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUnusedToneError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'unusedToneErrorMargin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'unusedToneErrorMarginRUIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUnusedToneErrorMarginPerRU': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'unusedToneErrorMarginPerRU',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUnusedToneErrorMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'unusedToneError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'unusedToneErrorMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccFetchUserDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(userDataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userDataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'userDataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserPilotConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userPilotConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserPilotConstellationTraceInterleavedIQ': {
        'cname': 'RFmxWLAN_OFDMModAccFetchUserPilotConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userPilotConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(userPilotConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserPilotConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userPilotConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'userPilotConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'userPowerMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserStreamDataRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_data_rms_evm_per_symbol_mean',
                'name': 'userStreamDataRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserStreamPilotRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_pilot_rms_evm_per_symbol_mean',
                'name': 'userStreamPilotRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserStreamRMSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_rms_evm_mean',
                'name': 'userStreamRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_data_rms_evm_mean',
                'name': 'userStreamDataRMSEVMMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_pilot_rms_evm_mean',
                'name': 'userStreamPilotRMSEVMMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserStreamRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_rms_evm_per_subcarrier_mean',
                'name': 'userStreamRMSEVMPerSubcarrierMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchUserStreamRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'user_stream_rms_evm_per_symbol_mean',
                'name': 'userStreamRMSEVMPerSymbolMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccValidateCalibrationData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'enum': 'OfdmModAccCalibrationDataValid',
                'name': 'calibrationDataValid',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampCfgAcquisitionLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'acquisitionLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerRampAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampFetchFallTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rawWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'threshold',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'powerReference',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'riseTimeMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'fallTimeMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampFetchRiseTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rawWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'threshold',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'powerReference',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetToDefault': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'SemAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgMaskType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemMaskType',
                'name': 'maskType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgNumberOfOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetFrequencyArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetStartFrequency',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'offsetStopFrequency',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetSideband',
                'name': 'offsetSideband',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetRelativeLimitArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'relativeLimitStart',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'relativeLimitStop',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'numberOfElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgSpan': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemSpanAuto',
                'name': 'spanAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgSweepTime': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemSweepTimeAuto',
                'name': 'sweepTimeAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sweepTimeInterval',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchLowerOffsetMargin': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'SemLowerOffsetMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'margin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchLowerOffsetMarginArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'SemLowerOffsetMeasurementStatus',
                'name': 'measurementStatus',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'margin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchLowerOffsetPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchLowerOffsetPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'totalRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchMeasurementStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'SemMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'compositeMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchUpperOffsetMargin': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'SemUpperOffsetMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'margin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'marginRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchUpperOffsetMarginArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'SemUpperOffsetMeasurementStatus',
                'name': 'measurementStatus',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'margin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'marginRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchUpperOffsetPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchUpperOffsetPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'totalRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SelectMeasurements': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MeasurementTypes',
                'name': 'measurements',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enableAllTraces',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SendSoftwareEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int16'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int8'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeNIComplexDoubleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeNIComplexSingleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt16'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt8'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'TxpAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgBurstDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'TxpBurstDetectionEnabled',
                'name': 'burstDetectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgMaximumMeasurementInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'maximumMeasurementInterval',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakPowerMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'power',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'WaitForAcquisitionComplete': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'WaitForMeasurementComplete': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxwlan/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/__init__.py`
- sha256: `b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41`
- bytes: 246

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/config.py sha256=7bf9f2517cf4de33b5709ac042a4ab1ce4d5b2baf4982bd0743b5b975c81f389 bytes=1967 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/config.py`
- sha256: `7bf9f2517cf4de33b5709ac042a4ab1ce4d5b2baf4982bd0743b5b975c81f389`
- bytes: 1967

````python
# -*- coding: utf-8 -*-
config = {
    "code_readiness": "Release",
    "is_restricted": True,
    "api_version": "21.0.0",
    "c_header": "niRFmxWLAN.h",
    "c_function_prefix": "RFmxWLAN_",
    "service_class_prefix": "NiRFmxWLANRestricted",
    "java_package": "com.ni.grpc.nirfmxwlanrestricted",
    "csharp_namespace": "NationalInstruments.Grpc.NiRFmxWLANRestricted",
    "namespace_component": "nirfmxwlan_restricted",
    'close_function': None,
    "custom_types": [],
    "type_to_grpc_type": {
        "char[]": "string",
        "float32": "float",
        "float64": "double",
        "int16": "int32",
        "int32": "int32",
        "int64": "int64",
        "niRFmxInstrHandle": "nidevice_grpc.Session",
        "int8": "int32",
        "uInt16": "uint32",
        "uInt32": "uint32",
        "uInt64": "uint64",
        "uInt8": "uint32",
        "uInt8[]": "bytes",
        "NIComplexSingle": "nidevice_grpc.NIComplexNumberF32",
        "NIComplexDouble": "nidevice_grpc.NIComplexNumber",
    },
    "driver_name": "NI-RFMXWLAN-RESTRICTED",
    "resource_handle_type": "niRFmxInstrHandle",
    "status_ok": "status >= 0",
    "windows_only": True,
    "library_info": {
        "Linux": {
            "64bit": {
                "name": "nirfmxwlan",
                "type": "cdll",
                "abi_version": "1"
            }
        },
        "Windows": {
            "32bit": {
                "name": "niRFmxWLAN.dll",
                "type": "windll"
            },
            "64bit": {
                "name": "niRFmxWLAN.dll",
                "type": "cdll"
            }
        },
    },
    "linux_rt_support": False,
    "metadata_version": "0.1",
    "module_name": "nirfmxwlan_restricted",
    "session_class_description": "An NI-RFmxWLAN instrument handle",
    'session_handle_parameter_name': 'instrumentHandle',
    "duplicate_resource_handles_allowed": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/enums.py sha256=b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc bytes=14 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/enums.py`
- sha256: `b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc`
- bytes: 14

````python
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/functions.py sha256=698f77ff504cf1fcd867931456f9d7c81354433eac8abe0aa24573021aa5d7ed bytes=6682 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/functions.py`
- sha256: `698f77ff504cf1fcd867931456f9d7c81354433eac8abe0aa24573021aa5d7ed`
- bytes: 6682

````python
functions = {
    'GetChannelList': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'WLANBand',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'centerFrequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'channelBandwidths',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'GetError': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccFetchCommonPilotErrorTraceIndB': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'commonPilotErrorMagnitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'commonPilotErrorPhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccLoad1ReferenceWaveformFromTDMSFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OFDMModAccNoiseCalibrate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sharedLOConnection',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan_restricted/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxwlan_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan_restricted/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxwlangen/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/__init__.py`
- sha256: `b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41`
- bytes: 246

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/attributes.py sha256=ec706562609b27cf627a5b23c79c3e79c1cf657540b07066c5e352ec4945dd7c bytes=22740 -->
## FILE: source/codegen/metadata/nirfmxwlangen/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/attributes.py`
- sha256: `ec706562609b27cf627a5b23c79c3e79c1cf657540b07066c5e352ec4945dd7c`
- bytes: 22740

````python
attributes = {
    0: {
        'access': 'read-write',
        'name': 'CARRIER_FREQUENCY',
        'type': 'float64'
    },
    2: {
        'access': 'read-write',
        'name': 'OVERSAMPLING_FACTOR',
        'type': 'int32'
    },
    3: {
        'access': 'read-write',
        'name': 'IDLE_INTERVAL',
        'type': 'float64'
    },
    4: {
        'access': 'read-write',
        'enum': 'DsssPreambleType',
        'name': 'DSSS_PREAMBLE_TYPE',
        'type': 'int32'
    },
    5: {
        'access': 'read-write',
        'name': 'PAYLOAD_DATA_LENGTH',
        'type': 'int32'
    },
    6: {
        'access': 'read-write',
        'name': 'NUMBER_OF_FRAMES',
        'type': 'int32'
    },
    7: {
        'access': 'read-write',
        'enum': 'PayloadDataType',
        'name': 'PAYLOAD_DATA_TYPE',
        'type': 'int32'
    },
    8: {
        'access': 'read-write',
        'name': 'PAYLOAD_PN_ORDER',
        'type': 'int32'
    },
    9: {
        'access': 'read-write',
        'name': 'PAYLOAD_PN_SEED',
        'type': 'int32'
    },
    10: {
        'access': 'read-write',
        'name': 'PAYLOAD_USER_DEFINED_BITS',
        'type': 'int32[]'
    },
    11: {
        'access': 'read-write',
        'enum': 'MacHeaderEnabled',
        'name': 'MAC_HEADER_ENABLED',
        'type': 'int32'
    },
    12: {
        'access': 'read-write',
        'name': 'SUBCARRIER_MASK',
        'type': 'float64[]'
    },
    13: {
        'access': 'read-write',
        'enum': 'LockedClockBitEnabled',
        'name': 'LOCKED_CLOCK_BIT_ENABLED',
        'type': 'int32'
    },
    14: {
        'access': 'read-write',
        'enum': 'HeaderEncoderEnabled',
        'name': 'HEADER_ENCODER_ENABLED',
        'type': 'int32'
    },
    15: {
        'access': 'read-write',
        'enum': 'HeaderInterleaverEnabled',
        'name': 'HEADER_INTERLEAVER_ENABLED',
        'type': 'int32'
    },
    16: {
        'access': 'read-write',
        'enum': 'PayloadScramblerEnabled',
        'name': 'PAYLOAD_SCRAMBLER_ENABLED',
        'type': 'int32'
    },
    17: {
        'access': 'read-write',
        'name': 'PAYLOAD_SCRAMBLER_SEED',
        'type': 'int32'
    },
    18: {
        'access': 'read-write',
        'enum': 'PayloadEncoderEnabled',
        'name': 'PAYLOAD_ENCODER_ENABLED',
        'type': 'int32'
    },
    19: {
        'access': 'read-write',
        'enum': 'PayloadInterleaverEnabled',
        'name': 'PAYLOAD_INTERLEAVER_ENABLED',
        'type': 'int32'
    },
    20: {
        'access': 'read-write',
        'name': 'CARRIER_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    21: {
        'access': 'read-write',
        'name': 'IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    22: {
        'access': 'read-write',
        'name': 'I_DC_OFFSET',
        'type': 'float64'
    },
    23: {
        'access': 'read-write',
        'name': 'Q_DC_OFFSET',
        'type': 'float64'
    },
    24: {
        'access': 'read-write',
        'name': 'QUADRATURE_SKEW',
        'type': 'float64'
    },
    25: {
        'access': 'read-write',
        'name': 'SAMPLE_CLOCK_OFFSET',
        'type': 'float64'
    },
    26: {
        'access': 'read-write',
        'enum': 'PulseShapingFilterType',
        'name': 'PULSE_SHAPING_FILTER_TYPE',
        'type': 'int32'
    },
    27: {
        'access': 'read-write',
        'name': 'PULSE_SHAPING_FILTER_PARAMETER',
        'type': 'float64'
    },
    29: {
        'access': 'read-write',
        'name': 'DSSS_WINDOW_LENGTH',
        'type': 'float64'
    },
    31: {
        'access': 'read-write',
        'enum': 'Standard',
        'name': 'STANDARD',
        'type': 'int32'
    },
    32: {
        'access': 'read-write',
        'enum': 'OfdmDataRate',
        'name': 'OFDM_DATA_RATE',
        'type': 'int32'
    },
    33: {
        'access': 'read-write',
        'enum': 'DsssDataRate',
        'name': 'DSSS_DATA_RATE',
        'type': 'int32'
    },
    35: {
        'access': 'read-write',
        'name': 'IQ_RATE',
        'type': 'float64'
    },
    37: {
        'access': 'read-write',
        'name': 'IQ_WAVEFORM_SIZE',
        'type': 'int32'
    },
    40: {
        'access': 'read-write',
        'name': 'HEADROOM',
        'type': 'float64'
    },
    41: {
        'access': 'read-write',
        'name': 'MCS_INDEX',
        'type': 'int32'
    },
    42: {
        'access': 'read-write',
        'name': 'CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    43: {
        'access': 'read-write',
        'enum': 'PlcpFrameFormat80211n',
        'name': '80211N_PLCP_FRAME_FORMAT',
        'type': 'int32'
    },
    46: {
        'access': 'read-write',
        'name': 'NUMBER_OF_EXTENSION_SPATIAL_STREAMS',
        'type': 'int32'
    },
    47: {
        'access': 'read-write',
        'name': 'NUMBER_OF_TRANSMIT_CHANNELS',
        'type': 'int32'
    },
    49: {
        'access': 'read-write',
        'name': 'STBC_INDEX',
        'type': 'int32'
    },
    53: {
        'access': 'read-write',
        'enum': 'MacQosControlEnabled',
        'name': 'MAC_QOS_CONTROL_ENABLED',
        'type': 'int32'
    },
    54: {
        'access': 'read-write',
        'enum': 'PulseShapingFilterEnabled',
        'name': 'PULSE_SHAPING_FILTER_ENABLED',
        'type': 'int32'
    },
    55: {
        'access': 'read-write',
        'enum': 'MappingMatrixType',
        'name': 'MAPPING_MATRIX_TYPE',
        'type': 'int32'
    },
    56: {
        'access': 'read-write',
        'enum': 'CompatibilityVersion',
        'name': 'COMPATIBILITY_VERSION',
        'type': 'int32'
    },
    57: {
        'access': 'read-write',
        'name': 'MAC_FRAME_CONTROL',
        'type': 'int32'
    },
    58: {
        'access': 'read-write',
        'name': 'MAC_DURATION_OR_ID',
        'type': 'int32'
    },
    59: {
        'access': 'read-write',
        'enum': 'MacAddress1Enabled',
        'name': 'MAC_ADDRESS1_ENABLED',
        'type': 'int32'
    },
    60: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS1',
        'type': 'int64'
    },
    61: {
        'access': 'read-write',
        'enum': 'MacAddress2Enabled',
        'name': 'MAC_ADDRESS2_ENABLED',
        'type': 'int32'
    },
    62: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS2',
        'type': 'int64'
    },
    63: {
        'access': 'read-write',
        'enum': 'MacAddress3Enabled',
        'name': 'MAC_ADDRESS3_ENABLED',
        'type': 'int32'
    },
    64: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS3',
        'type': 'int64'
    },
    65: {
        'access': 'read-write',
        'enum': 'MacSequenceControlEnabled',
        'name': 'MAC_SEQUENCE_CONTROL_ENABLED',
        'type': 'int32'
    },
    66: {
        'access': 'read-write',
        'name': 'MAC_SEQUENCE_CONTROL',
        'type': 'int32'
    },
    67: {
        'access': 'read-write',
        'enum': 'MacAddress4Enabled',
        'name': 'MAC_ADDRESS4_ENABLED',
        'type': 'int32'
    },
    68: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS4',
        'type': 'int64'
    },
    70: {
        'access': 'read-write',
        'enum': 'FecCodingType',
        'name': 'FEC_CODING_TYPE',
        'type': 'int32'
    },
    71: {
        'access': 'read-write',
        'name': 'MAC_QOS_CONTROL',
        'type': 'int32'
    },
    72: {
        'access': 'read-write',
        'enum': 'MacHTControlEnabled',
        'name': 'MAC_HT_CONTROL_ENABLED',
        'type': 'int32'
    },
    73: {
        'access': 'read-write',
        'name': 'MAC_HT_CONTROL',
        'type': 'int32'
    },
    74: {
        'access': 'read-write',
        'enum': 'WindowingMethod',
        'name': 'WINDOWING_METHOD',
        'type': 'int32'
    },
    75: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    76: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SPACE_TIME_STREAMS',
        'type': 'int32'
    },
    77: {
        'access': 'read-write',
        'enum': 'StbcAllStreamsEnabled',
        'name': 'STBC_ALL_STREAMS_ENABLED',
        'type': 'int32'
    },
    78: {
        'access': 'read-write',
        'enum': 'SwapIAndQEnabled',
        'name': 'SWAP_I_AND_Q_ENABLED',
        'type': 'int32'
    },
    79: {
        'access': 'read-write',
        'name': 'TIMING_SKEW',
        'type': 'float64'
    },
    80: {
        'access': 'read-write',
        'enum': 'MacSequenceNumberIncrementEnabled',
        'name': 'MAC_SEQUENCE_NUMBER_INCREMENT_ENABLED',
        'type': 'int32'
    },
    81: {
        'access': 'read-write',
        'name': 'MAC_SEQUENCE_NUMBER_INCREMENT_INTERVAL',
        'type': 'int32'
    },
    82: {
        'access': 'read-write',
        'enum': 'MacFragmentNumberIncrementEnabled',
        'name': 'MAC_FRAGMENT_NUMBER_INCREMENT_ENABLED',
        'type': 'int32'
    },
    83: {
        'access': 'read-write',
        'name': 'MPDU_LENGTH',
        'type': 'int32'
    },
    86: {
        'access': 'read-write',
        'name': 'NOT_SOUNDING_BIT',
        'type': 'int32'
    },
    87: {
        'access': 'read-write',
        'enum': 'AutoHeadroomEnabled',
        'name': 'AUTO_HEADROOM_ENABLED',
        'type': 'int32'
    },
    88: {
        'access': 'read-write',
        'name': 'ACTUAL_HEADROOM',
        'type': 'float64'
    },
    89: {
        'access': 'read-write',
        'name': 'ACTUAL_OFDM_DATA_RATE',
        'type': 'float64'
    },
    90: {
        'access': 'read-write',
        'enum': 'RFBlankingEnabled',
        'name': 'RF_BLANKING_ENABLED',
        'type': 'int32'
    },
    91: {
        'access': 'read-write',
        'name': 'RF_BLANKING_MARKER_POSITIONS',
        'type': 'int32[]'
    },
    94: {
        'access': 'read-write',
        'name': 'NUMBER_OF_DATA_SYMBOLS',
        'type': 'int32'
    },
    95: {
        'access': 'read-write',
        'enum': 'PpduType',
        'name': 'PPDU_TYPE',
        'type': 'int32'
    },
    96: {
        'access': 'read-write',
        'enum': 'AllIQImpairmentsEnabled',
        'name': 'ALL_IQ_IMPAIRMENTS_ENABLED',
        'type': 'int32'
    },
    97: {
        'access': 'read-write',
        'enum': 'AwgnEnabled',
        'name': 'AWGN_ENABLED',
        'type': 'int32'
    },
    98: {
        'access': 'read-write',
        'name': 'CARRIER_TO_NOISE_RATIO',
        'type': 'float64'
    },
    100: {
        'access': 'read-write',
        'enum': 'MacFcsEnabled',
        'name': 'MAC_FCS_ENABLED',
        'type': 'int32'
    },
    102: {
        'access': 'read-write',
        'name': 'MAXIMUM_HARDWARE_IQ_RATE',
        'type': 'float64'
    },
    103: {
        'access': 'read-write',
        'enum': 'AmpduEnabled',
        'name': 'AMPDU_ENABLED',
        'type': 'int32'
    },
    104: {
        'access': 'read-write',
        'name': 'PAYLOAD_NUMBER_OF_MPDUS',
        'type': 'int32'
    },
    107: {
        'access': 'read-write',
        'name': 'SAMPLE_CLOCK_RATE_FACTOR',
        'type': 'float64'
    },
    112: {
        'access': 'read-write',
        'name': 'PULSE_SHAPING_FILTER_LENGTH',
        'type': 'int32'
    },
    115: {
        'access': 'read-write',
        'name': 'NUMBER_OF_USERS',
        'type': 'int32'
    },
    118: {
        'access': 'read-write',
        'enum': 'LOSharingEnabled',
        'name': 'LO_SHARING_ENABLED',
        'type': 'int32'
    },
    119: {
        'access': 'read-write',
        'enum': 'PreambleType80211ah',
        'name': '80211AH_PREAMBLE_TYPE',
        'type': 'int32'
    },
    120: {
        'access': 'read-write',
        'enum': 'MacFrameFormat',
        'name': 'MAC_FRAME_FORMAT',
        'type': 'int32'
    },
    121: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS1_LENGTH',
        'type': 'int32'
    },
    122: {
        'access': 'read-write',
        'name': 'MAC_ADDRESS2_LENGTH',
        'type': 'int32'
    },
    123: {
        'access': 'read-write',
        'enum': 'GuardIntervalType',
        'name': 'GUARD_INTERVAL_TYPE',
        'type': 'int32'
    },
    124: {
        'access': 'read-write',
        'enum': 'TransmissionMode',
        'name': 'TRANSMISSION_MODE',
        'type': 'int32'
    },
    125: {
        'access': 'read-write',
        'name': 'OFDM_WINDOW_LENGTH',
        'type': 'int32'
    },
    127: {
        'access': 'read-write',
        'enum': 'NonHTModulationMode',
        'name': 'NON_HT_MODULATION_MODE',
        'type': 'int32'
    },
    132: {
        'access': 'read-write',
        'enum': 'RUSize',
        'name': 'RU_SIZE',
        'type': 'int32'
    },
    133: {
        'access': 'read-write',
        'name': 'RU_OFFSET_MRU_INDEX',
        'type': 'int32'
    },
    134: {
        'access': 'read-write',
        'enum': 'MultiSegmentGenerationMode',
        'name': 'MULTI_SEGMENT_GENERATION_MODE',
        'type': 'int32'
    },
    135: {
        'access': 'read-write',
        'name': 'TIME_DELAY',
        'type': 'float64'
    },
    136: {
        'access': 'read-write',
        'name': 'RELATIVE_POWER',
        'type': 'float64'
    },
    144: {
        'access': 'read-write',
        'enum': 'LtfSize',
        'name': 'LTF_SIZE',
        'type': 'int32'
    },
    154: {
        'access': 'read-write',
        'enum': 'DualCarrierModulationEnabled',
        'name': 'DUAL_CARRIER_MODULATION_ENABLED',
        'type': 'int32'
    },
    159: {
        'access': 'read-write',
        'name': 'PACKET_EXTENSION_DURATION',
        'type': 'float64'
    },
    161: {
        'access': 'read-write',
        'name': 'HE_SIG_B_MCS_INDEX',
        'type': 'int32'
    },
    162: {
        'access': 'read-write',
        'enum': 'HESigBDualCarrierModulationEnabled',
        'name': 'HE_SIG_B_DUAL_CARRIER_MODULATION_ENABLED',
        'type': 'int32'
    },
    163: {
        'access': 'read-write',
        'name': 'STA_ID',
        'type': 'int32'
    },
    164: {
        'access': 'read-write',
        'name': 'POWER_BOOST_FACTOR',
        'type': 'float64'
    },
    165: {
        'access': 'read-write',
        'name': 'NUMBER_OF_LTF_SYMBOLS',
        'type': 'int32'
    },
    168: {
        'access': 'read-write',
        'name': 'FULLSCALE_BACKOFF',
        'type': 'float64'
    },
    170: {
        'access': 'read-write',
        'enum': 'AveragePowerReference',
        'name': 'AVERAGE_POWER_REFERENCE',
        'type': 'int32'
    },
    172: {
        'access': 'read-write',
        'name': 'TRIGGER_FRAME_AP_TX_POWER',
        'type': 'int32'
    },
    173: {
        'access': 'read-write',
        'name': 'TRIGGER_FRAME_TARGET_RSSI',
        'type': 'int32'
    },
    174: {
        'access': 'read-write',
        'name': 'BURST_START_LOCATIONS',
        'type': 'int32[]'
    },
    175: {
        'access': 'read-write',
        'name': 'BURST_STOP_LOCATIONS',
        'type': 'int32[]'
    },
    176: {
        'access': 'read-write',
        'enum': 'LOFrequencyOffsetMode',
        'name': 'LO_FREQUENCY_OFFSET_MODE',
        'type': 'int32'
    },
    177: {
        'access': 'read-write',
        'name': 'LO_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    178: {
        'access': 'read-write',
        'enum': 'PayloadAutoNumberOfMpdus',
        'name': 'PAYLOAD_AUTO_NUMBER_OF_MPDUS',
        'type': 'int32'
    },
    179: {
        'access': 'read-write',
        'enum': 'AutoPayloadDataLengthMode',
        'name': 'AUTO_PAYLOAD_DATA_LENGTH_MODE',
        'type': 'int32'
    },
    180: {
        'access': 'read-write',
        'name': 'L_SIG_LENGTH',
        'type': 'int32'
    },
    181: {
        'access': 'read-write',
        'name': 'PRE_FEC_PADDING_FACTOR',
        'type': 'int32'
    },
    182: {
        'access': 'read-write',
        'name': 'PE_DISAMBIGUITY',
        'type': 'int32'
    },
    183: {
        'access': 'read-write',
        'name': 'LDPC_EXTRA_SYMBOL_SEGMENT',
        'type': 'int32'
    },
    184: {
        'access': 'read-write',
        'name': 'BSS_COLOR',
        'type': 'int32'
    },
    185: {
        'access': 'read-write',
        'enum': 'SpatialMappingMode',
        'name': 'SPATIAL_MAPPING_MODE',
        'type': 'int32'
    },
    186: {
        'access': 'read-write',
        'enum': 'MUMimoLtfModeEnabled',
        'name': 'MU_MIMO_LTF_MODE_ENABLED',
        'type': 'int32'
    },
    187: {
        'access': 'read-write',
        'name': 'SPACE_TIME_STREAM_OFFSET',
        'type': 'int32'
    },
    188: {
        'access': 'read-write',
        'enum': 'PayloadMacFrameType',
        'name': 'PAYLOAD_MAC_FRAME_TYPE',
        'type': 'int32'
    },
    189: {
        'access': 'read-write',
        'enum': 'TriggerFrameMacPaddingDuration',
        'name': 'TRIGGER_FRAME_MAC_PADDING_DURATION',
        'type': 'int32'
    },
    190: {
        'access': 'read-write',
        'name': 'TRIGGER_FRAME_CS_REQUIRED',
        'type': 'int32'
    },
    191: {
        'access': 'read-write',
        'enum': 'PreamblePuncturingEnabled',
        'name': 'PREAMBLE_PUNCTURING_ENABLED',
        'type': 'int32'
    },
    192: {
        'access': 'read-write',
        'name': 'PRIMARY_20MHZ_CHANNEL_INDEX',
        'type': 'int32'
    },
    193: {
        'access': 'read-write',
        'name': 'PREAMBLE_PUNCTURING_MASK',
        'type': 'int32'
    },
    194: {
        'access': 'read-write',
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'float64'
    },
    195: {
        'access': 'read-write',
        'enum': 'NominalPacketPadding',
        'name': 'NOMINAL_PACKET_PADDING',
        'type': 'int32'
    },
    196: {
        'access': 'read-write',
        'name': 'TRIGGER_FRAME_AID12',
        'type': 'int32'
    },
    199: {
        'access': 'read-write',
        'enum': 'IdleIntervalMode',
        'name': 'IDLE_INTERVAL_MODE',
        'type': 'int32'
    },
    201: {
        'access': 'read-write',
        'name': 'RUN_TIME_SCALING',
        'type': 'float64'
    },
    202: {
        'access': 'read-write',
        'enum': 'WaveformFileVersion',
        'name': 'WAVEFORM_FILE_VERSION',
        'type': 'int32'
    },
    204: {
        'access': 'read-write',
        'enum': 'MidamblePeriodicity',
        'name': 'MIDAMBLE_PERIODICITY',
        'type': 'int32'
    },
    205: {
        'access': 'read-write',
        'enum': 'RUAllocationMode',
        'name': 'RU_ALLOCATION_MODE',
        'type': 'int32'
    },
    206: {
        'access': 'read-write',
        'name': 'RU_ALLOCATION',
        'type': 'int32[]'
    },
    207: {
        'access': 'read-write',
        'enum': 'UserEnabled',
        'name': 'USER_ENABLED',
        'type': 'int32'
    },
    209: {
        'access': 'read-write',
        'name': 'FRAME_DURATION',
        'type': 'float64'
    },
    210: {
        'access': 'read-write',
        'enum': 'UnframedDataModulationEnabled',
        'name': 'UNFRAMED_DATA_MODULATION_ENABLED',
        'type': 'int32'
    },
    211: {
        'access': 'read-write',
        'name': 'OVERSAMPLING_RATIO',
        'type': 'float64'
    },
    212: {
        'access': 'read-write',
        'name': 'SIG_MCS_INDEX',
        'type': 'int32'
    },
    213: {
        'access': 'read-write',
        'enum': 'SigCompressionEnabled',
        'name': 'SIG_COMPRESSION_ENABLED',
        'type': 'int32'
    },
    214: {
        'access': 'read-write',
        'enum': 'PhaseRotationCoefficient1',
        'name': 'PHASE_ROTATION_COEFFICIENT_1',
        'type': 'int32'
    },
    215: {
        'access': 'read-write',
        'enum': 'PhaseRotationCoefficient2',
        'name': 'PHASE_ROTATION_COEFFICIENT_2',
        'type': 'int32'
    },
    216: {
        'access': 'read-write',
        'enum': 'PhaseRotationCoefficient3',
        'name': 'PHASE_ROTATION_COEFFICIENT_3',
        'type': 'int32'
    },
    217: {
        'access': 'read-write',
        'name': 'CYCLIC_TIME_SHIFT',
        'type': 'float64'
    },
    222: {
        'access': 'read-write',
        'enum': 'RUType',
        'name': 'RU_TYPE',
        'type': 'int32'
    },
    223: {
        'access': 'read-write',
        'enum': 'HybridLOSharingMode',
        'name': 'HYBRID_LO_SHARING_MODE',
        'type': 'int32'
    },
    224: {
        'access': 'read-write',
        'enum': 'MultiChassisTClkSynchronizationMode',
        'name': 'MULTI_CHASSIS_TCLK_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    225: {
        'access': 'read-write',
        'name': 'LO_SPLITTER_LOSS',
        'type': 'float64[]'
    },
    226: {
        'access': 'read-write',
        'name': 'LO_SPLITTER_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    227: {
        'access': 'read-write',
        'name': 'DISTRIBUTION_BANDWIDTH',
        'type': 'float64'
    },
    228: {
        'access': 'read-write',
        'enum': 'TwoxLdpcEnabled',
        'name': '2XLDPC_ENABLED',
        'type': 'int32'
    },
    229: {
        'access': 'read-write',
        'enum': 'UnequalModulationEnabled',
        'name': 'UNEQUAL_MODULATION_ENABLED',
        'type': 'int32'
    },
    230: {
        'access': 'read-write',
        'name': 'UNEQUAL_MODULATION_PATTERN_INDEX',
        'type': 'int32'
    },
    231: {
        'access': 'read-write',
        'enum': 'Channelization',
        'name': 'CHANNELIZATION',
        'type': 'int32'
    },
    232: {
        'access': 'read-write',
        'enum': 'HESigBCompressionMode',
        'name': 'HE_SIG_B_COMPRESSION_MODE',
        'type': 'int32'
    },
    233: {
        'access': 'read-write',
        'enum': 'InterferenceMitigationPilotsEnabled',
        'name': 'INTERFERENCE_MITIGATION_PILOTS_ENABLED',
        'type': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxwlangen/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/config.py sha256=bdb65fa10cfca8418d2a24879af86ef72268848f47787674fd187afa6b983b99 bytes=2331 -->
## FILE: source/codegen/metadata/nirfmxwlangen/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/config.py`
- sha256: `bdb65fa10cfca8418d2a24879af86ef72268848f47787674fd187afa6b983b99`
- bytes: 2331

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.3.0',
    'c_header': 'niWLANGeneration.h',  
    'c_function_prefix': 'niWLANG_',
    'service_class_prefix': 'NiRFmxWLANGen',
    'java_package': 'com.ni.grpc.nirfmxwlangen',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxWLANGen',
    'namespace_component': 'nirfmxwlangen',
    'close_function': 'CloseSession',
    'custom_types': [],
    'additional_headers': { 'custom/nirfmx_errors.h': ['service.cpp'],
    'niWLANGenerationRfsg.h': ['library.h', 'library.cpp', 'library_interface.h', 'compilation_test.cpp']},
    'type_to_grpc_type': {
        "char[]": "string",
        "float32": "float",
        "float64": "double",
        "int16": "int32",
        "int32": "int32",
        "int64": "int64",
        "int8": "int32",
        "uInt16": "uint32",
        "uInt32": "uint32",
        "uInt64": "uint64",
        "uInt8": "uint32",
        "uInt8[]": "bytes",
        "NIComplexSingle": "nidevice_grpc.NIComplexNumberF32",
        "NIComplexDouble": "nidevice_grpc.NIComplexNumber",
        "NIComplexNumber": "nidevice_grpc.NIComplexNumber",
        "niWLANGenerationSession": "nidevice_grpc.Session",
        "ViSession": "nidevice_grpc.Session"
    },
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-RFMXWLANGEN',
    'extra_errors_used': [],
    'init_function': 'OpenSession',
    'resource_handle_type': ['niWLANGenerationSession', 'ViSession'],
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxwlangen',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niWLANGeneration_net.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niWLANGeneration_net.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxwlangen',
    'session_class_description': 'An RFmx WLAN Generation handle',
    'session_handle_parameter_name': 'session',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxwlangen/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/enums.py sha256=be085374d65bdaa8d53f0c5c8b1da73486ce8dfa94ca78ee6acd8178b4a6ef35 bytes=26876 -->
## FILE: source/codegen/metadata/nirfmxwlangen/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/enums.py`
- sha256: `be085374d65bdaa8d53f0c5c8b1da73486ce8dfa94ca78ee6acd8178b4a6ef35`
- bytes: 26876

````python
enums = {
    'AllIQImpairmentsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AmpduEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoHeadroomEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoPayloadDataLengthMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'L_SIG_LENGTH',
                'value': 1
            },
            {
                'name': 'FRAME_DURATION',
                'value': 2
            }
        ]
    },
    'AveragePowerReference': {
        'values': [
            {
                'name': 'NON_BOOSTED_FIELDS',
                'value': 0
            },
            {
                'name': 'POWER_BOOSTED_FIELDS',
                'value': 1
            },
            {
                'name': 'ENTIRE_PACKET',
                'value': 2
            }
        ]
    },
    'AwgnEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'Channelization': {
        'values': [
            {
                'name': '320_MHZ_1',
                'value': 0
            },
            {
                'name': '320_MHZ_2',
                'value': 1
            }
        ]
    },
    'CompatibilityVersion': {
        'values': [
            {
                'name': '010000',
                'value': 10000
            },
            {
                'name': '020000',
                'value': 20000
            },
            {
                'name': '030000',
                'value': 30000
            },
            {
                'name': '040000',
                'value': 40000
            },
            {
                'name': '050000',
                'value': 50000
            },
            {
                'name': '060000',
                'value': 60000
            }
        ]
    },
    'DsssDataRate': {
        'values': [
            {
                'name': '1',
                'value': 0
            },
            {
                'name': '2',
                'value': 1
            },
            {
                'name': '5P_5_CCK',
                'value': 2
            },
            {
                'name': '5P_5_PBCC',
                'value': 3
            },
            {
                'name': '11_CCK',
                'value': 4
            },
            {
                'name': '11_PBCC',
                'value': 5
            },
            {
                'name': '22',
                'value': 6
            },
            {
                'name': '33',
                'value': 7
            }
        ]
    },
    'DsssPreambleType': {
        'values': [
            {
                'name': 'SHORT',
                'value': 0
            },
            {
                'name': 'LONG',
                'value': 1
            }
        ]
    },
    'DualCarrierModulationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'FecCodingType': {
        'values': [
            {
                'name': 'BCC',
                'value': 0
            },
            {
                'name': 'LDPC',
                'value': 1
            }
        ]
    },
    'FileOperationMode': {
        'values': [
            {
                'name': 'OPEN',
                'value': 0
            },
            {
                'name': 'OPEN_OR_CREATE',
                'value': 1
            },
            {
                'name': 'CREATE_OR_REPLACE',
                'value': 2
            },
            {
                'name': 'CREATE',
                'value': 3
            }
        ]
    },
    'GuardIntervalType': {
        'values': [
            {
                'name': 'ONE_BY_FOUR',
                'value': 0
            },
            {
                'name': 'ONE_BY_EIGHT',
                'value': 1
            },
            {
                'name': 'ONE_BY_SIXTEEN',
                'value': 2
            }
        ]
    },
    'HESigBCompressionMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'MANUAL',
                'value': 1
            }
        ]
    },
    'HESigBDualCarrierModulationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'HeaderEncoderEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'HeaderInterleaverEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'HybridLOSharingMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'MODE_0',
                'value': 1
            }
        ]
    },
    'IdleIntervalMode': {
        'values': [
            {
                'name': 'SPLIT',
                'value': 0
            },
            {
                'name': 'POST_BURST',
                'value': 1
            }
        ]
    },
    'InterferenceMitigationPilotsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOFrequencyOffsetMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            },
            {
                'name': 'DISABLED',
                'value': 2
            }
        ]
    },
    'LOSharingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOSource': {
        'values': [
            {
                'name': 'EXTERNAL',
                'value': 0
            },
            {
                'name': 'ONBOARD',
                'value': 2
            },
            {
                'name': 'SG_SA_SHARED',
                'value': 3
            }
        ]
    },
    'LockedClockBitEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LtfSize': {
        'values': [
            {
                'name': 'AUTO',
                'value': -1
            },
            {
                'name': '4X',
                'value': 0
            },
            {
                'name': '2X',
                'value': 1
            },
            {
                'name': '1X',
                'value': 2
            }
        ]
    },
    'MUMimoLtfModeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacAddress1Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacAddress2Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacAddress3Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacAddress4Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacFcsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacFragmentNumberIncrementEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacFrameFormat': {
        'values': [
            {
                'name': 'LONG',
                'value': 0
            },
            {
                'name': 'SHORT',
                'value': 1
            }
        ]
    },
    'MacHTControlEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacHeaderEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacQosControlEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacSequenceControlEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MacSequenceNumberIncrementEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MappingMatrixType': {
        'values': [
            {
                'name': 'DIRECT',
                'value': 0
            },
            {
                'name': 'HADAMARD',
                'value': 1
            },
            {
                'name': 'FOURIER',
                'value': 2
            },
            {
                'name': 'USER_DEFINED',
                'value': 3
            }
        ]
    },
    'MidamblePeriodicity': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'TEN_SYMBOLS',
                'value': 1
            },
            {
                'name': 'TWENTY_SYMBOLS',
                'value': 2
            }
        ]
    },
    'MultiChassisTClkSynchronizationMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'TIMING_MODULE',
                'value': 1
            }
        ]
    },
    'MultiSegmentGenerationMode': {
        'values': [
            {
                'name': 'SINGLE_GENERATOR',
                'value': 0
            },
            {
                'name': 'MULTIPLE_GENERATORS',
                'value': 1
            }
        ]
    },
    'NominalPacketPadding': {
        'values': [
            {
                'name': 'AUTO',
                'value': -1
            },
            {
                'name': '0US',
                'value': 0
            },
            {
                'name': '8US',
                'value': 1
            },
            {
                'name': '16US',
                'value': 2
            },
            {
                'name': '20US',
                'value': 3
            }
        ]
    },
    'NonHTModulationMode': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ON',
                'value': 1
            }
        ]
    },
    'OfdmDataRate': {
        'values': [
            {
                'name': '6',
                'value': 0
            },
            {
                'name': '9',
                'value': 1
            },
            {
                'name': '12',
                'value': 2
            },
            {
                'name': '18',
                'value': 3
            },
            {
                'name': '24',
                'value': 4
            },
            {
                'name': '36',
                'value': 5
            },
            {
                'name': '48',
                'value': 6
            },
            {
                'name': '54',
                'value': 7
            }
        ]
    },
    'PayloadAutoNumberOfMpdus': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PayloadDataType': {
        'values': [
            {
                'name': 'USER_DEFINED_PATTERN',
                'value': 0
            },
            {
                'name': 'PN_SEQUENCE',
                'value': 1
            }
        ]
    },
    'PayloadEncoderEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PayloadInterleaverEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PayloadMacFrameType': {
        'values': [
            {
                'name': 'GENERAL_FRAME',
                'value': 0
            },
            {
                'name': 'DATA_FRAME',
                'value': 1
            },
            {
                'name': 'TRIGGER_FRAME',
                'value': 2
            }
        ]
    },
    'PayloadScramblerEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PhaseRotationCoefficient1': {
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'PhaseRotationCoefficient2': {
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'PhaseRotationCoefficient3': {
        'values': [
            {
                'name': 'PLUS_ONE',
                'value': 0
            },
            {
                'name': 'MINUS_ONE',
                'value': 1
            }
        ]
    },
    'PlcpFrameFormat80211n': {
        'values': [
            {
                'name': '80211N_PLCP_FRAME_FORMAT_MIXED',
                'value': 0
            },
            {
                'name': '80211N_PLCP_FRAME_FORMAT_GREENFIELD',
                'value': 1
            }
        ]
    },
    'PpduType': {
        'values': [
            {
                'name': 'SU_PPDU',
                'value': 0
            },
            {
                'name': 'MU_PPDU',
                'value': 1
            },
            {
                'name': 'EXTENDED_RANGE_SU_PPDU',
                'value': 2
            },
            {
                'name': 'TRIGGER_BASED_PPDU',
                'value': 3
            },
            {
                'name': 'ELR_PPDU',
                'value': 4
            }
        ]
    },
    'PreamblePuncturingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PreambleType80211ah': {
        'values': [
            {
                'name': '80211AH_PREAMBLE_TYPE_SHORT',
                'value': 0
            },
            {
                'name': '80211AH_PREAMBLE_TYPE_LONG',
                'value': 1
            }
        ]
    },
    'PulseShapingFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PulseShapingFilterType': {
        'values': [
            {
                'name': 'RECTANGULAR',
                'value': 0
            },
            {
                'name': 'RAISED_COSINE',
                'value': 1
            },
            {
                'name': 'ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'name': 'GAUSSIAN',
                'value': 3
            }
        ]
    },
    'RFBlankingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'RUAllocationMode': {
        'values': [
            {
                'name': 'INDIVIDUAL',
                'value': 0
            },
            {
                'name': 'GROUP',
                'value': 1
            }
        ]
    },
    'RUSize': {
        'values': [
            {
                'name': '26',
                'value': 26
            },
            {
                'name': '52',
                'value': 52
            },
            {
                'name': '106',
                'value': 106
            },
            {
                'name': '242',
                'value': 242
            },
            {
                'name': '484',
                'value': 484
            },
            {
                'name': '996',
                'value': 996
            },
            {
                'name': '2X_996',
                'value': 1992
            },
            {
                'name': '4X_996',
                'value': 3984
            },
            {
                'name': '52_PLUS_26',
                'value': 78
            },
            {
                'name': '106_PLUS_26',
                'value': 132
            },
            {
                'name': '484_PLUS_242',
                'value': 726
            },
            {
                'name': '996_PLUS_484',
                'value': 1480
            },
            {
                'name': '996_PLUS_484_PLUS_242',
                'value': 1722
            },
            {
                'name': '2X_996_PLUS_484',
                'value': 2476
            },
            {
                'name': '3X_996',
                'value': 2988
            },
            {
                'name': '3X_996_PLUS_484',
                'value': 3472
            }
        ]
    },
    'RUType': {
        'values': [
            {
                'name': 'RRU',
                'value': 0
            },
            {
                'name': 'DRU',
                'value': 1
            }
        ]
    },
    'SigCompressionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SpatialMappingMode': {
        'values': [
            {
                'name': 'COMMON',
                'value': 0
            },
            {
                'name': 'USER_SPECIFIC',
                'value': 1
            }
        ]
    },
    'Standard': {
        'values': [
            {
                'name': '80211AG_OFDM',
                'value': 0
            },
            {
                'name': '80211J_OFDM',
                'value': 7
            },
            {
                'name': '80211P_OFDM',
                'value': 8
            },
            {
                'name': '80211BG_DSSS',
                'value': 1
            },
            {
                'name': '80211G_DSSS_OFDM',
                'value': 2
            },
            {
                'name': '80211N_MIMO_OFDM',
                'value': 3
            },
            {
                'name': '80211AC_MIMO_OFDM',
                'value': 4
            },
            {
                'name': '80211AH_MIMO_OFDM',
                'value': 5
            },
            {
                'name': '80211AF_MIMO_OFDM',
                'value': 6
            },
            {
                'name': '80211AX_MIMO_OFDM',
                'value': 9
            },
            {
                'name': '80211BE_MIMO_OFDM',
                'value': 10
            },
            {
                'name': '80211BN_MIMO_OFDM',
                'value': 11
            }
        ]
    },
    'StbcAllStreamsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SwapIAndQEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'TransmissionMode': {
        'values': [
            {
                'name': 'DOWNLINK',
                'value': 0
            },
            {
                'name': 'UPLINK',
                'value': 1
            }
        ]
    },
    'TriggerFrameMacPaddingDuration': {
        'values': [
            {
                'name': 'PADDING_DURATION_0US',
                'value': 0
            },
            {
                'name': 'PADDING_DURATION_8US',
                'value': 1
            },
            {
                'name': 'PADDING_DURATION_16US',
                'value': 2
            }
        ]
    },
    'TvhtMode': {
        'values': [
            {
                'name': '1',
                'value': 0
            },
            {
                'name': '2C',
                'value': 1
            },
            {
                'name': '2N',
                'value': 2
            },
            {
                'name': '4C',
                'value': 3
            },
            {
                'name': '4N',
                'value': 4
            }
        ]
    },
    'TwoxLdpcEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'UnequalModulationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'UnframedDataModulationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'UserEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'WaveformFileVersion': {
        'values': [
            {
                'name': '1_0',
                'value': 0
            },
            {
                'name': '2_0',
                'value': 1
            }
        ]
    },
    'WindowingMethod': {
        'values': [
            {
                'name': 'CENTERED_AT_SYMBOL_BOUNDARY',
                'value': 0
            },
            {
                'name': 'STARTING_AT_SYMBOL_BOUNDARY',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/enums_addon.py sha256=ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57 bytes=290 -->
## FILE: source/codegen/metadata/nirfmxwlangen/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/enums_addon.py`
- sha256: `ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57`
- bytes: 290

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "Standard": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/functions.py sha256=65303e44670fa5736cb65dbf66ed1258e9b19fda27edc05b2906edb1e812e1e0 bytes=63413 -->
## FILE: source/codegen/metadata/nirfmxwlangen/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/functions.py`
- sha256: `65303e44670fa5736cb65dbf66ed1258e9b19fda27edc05b2906edb1e812e1e0`
- bytes: 63413

````python
functions = {
    'ChannelNumberToCarrierFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'frequencyBand',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'secondaryFactor',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelStartingFactor',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency80211abgjpn': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelStartingFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'secondaryFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency80211ac': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelStartingFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency80211af': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelStartingFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'TvhtMode',
                'name': 'tvhtMode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency80211ah': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelStartingFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency80211ax': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelStartingFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CloseSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            }
        ],
        'returns': 'int32'
    },
    'CreateAndWriteWaveformsToFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FileOperationMode',
                'name': 'fileOperation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateMIMOWaveformsComplexF64': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'numberOfTxChains'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'numberOfTxChains'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveforms',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'individualWaveformSize',
                    'value_twist': 'actualNumSamplesInEachWfm'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfTxChains',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'individualWaveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumSamplesInEachWfm',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateMIMOWaveformsComplexF64InterleavedIQ': {
        'cname': 'niWLANG_CreateMIMOWaveformsComplexF64',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'numberOfTxChains'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'numberOfTxChains'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'waveforms',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'individualWaveformSize',
                    'value_twist': 'actualNumSamplesInEachWfm'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(waveforms)'
            },
            {
                'direction': 'in',
                'name': 'numberOfTxChains',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'individualWaveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumSamplesInEachWfm',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'done',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateTriggerFrameMSDU': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'generationDone',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'triggerFrameMsduBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateWaveformComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateWaveformComplexF64InterleavedIQ': {
        'cname': 'niWLANG_CreateWaveformComplexF64',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(waveform)'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorMessageLength'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'errorMessageLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetMappingMatrix': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'mappingMatrix',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'matrix_size'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixRows',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixColumns',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetMappingMatrixInterleavedIQ': {
        'cname': 'niWLANG_GetMappingMatrix',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'mappingMatrix',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'matrix_size'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(mappingMatrix)'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixRows',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixColumns',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetNumberOfUsersFromRUAllocation': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfUsers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'GetVectorAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualNumDataArrayElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumDataArrayElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetVectorAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualNumDataArrayElements'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumDataArrayElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadConfigurationFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resetSession',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OpenSession': {
        'custom_close': 'CloseSession(id)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CompatibilityVersion',
                'name': 'toolkitCompatibilityVersion',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isNewSession',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGClearDatabase': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureFrequencyMultipleLO': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfRFSGSessions'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfRFSGSessions',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'LOSource',
                'name': 'loSource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'externalLOHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfExternalLOHandles'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfExternalLOHandles',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'carrierFrequency',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'rfsgLODaisyChainEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'loExportToExternalDevicesEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureFrequencySingleLO': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfRFSGSessions'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfRFSGSessions',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'LOSource',
                'name': 'loSource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'externalLoHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'carrierFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'rfsgLODaisyChainEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'loExportToExternalDevicesEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureMultipleDeviceSynchronization': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfRFSGSessions'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfRFSGSessions',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'masterReferenceClockSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerLines',
                'size': {
                    'mechanism': 'len',
                    'value': 'noOfTriggerLines'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'noOfTriggerLines',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigurePowerLevel': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'powerLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureSampleClockDelay': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'noOfChannels'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'sampleClockDelay',
                'size': {
                    'mechanism': 'len',
                    'value': 'noOfChannels'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'noOfChannels',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureScript': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'powerLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGCreateAndDownloadMIMOWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfTxChains'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfTxChains',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGCreateAndDownloadWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGForceTClkSynchronization': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfRFSGSessions'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfRFSGSessions',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'forceSync',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGInsertRFBlankingMarkerPositions': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'scriptOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'lenOfScriptOut',
                    'value_twist': 'actualLenOfScriptOut'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'lenOfScriptOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualLenOfScriptOut',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGMultipleDeviceInitiate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfRFSGSessions'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfRFSGSessions',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGReadAndDownloadWaveformsFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandles',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfChannels'
                },
                'type': 'ViSession[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfChannels',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveBurstStartLocations': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'burstStartLocations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveBurstStopLocations': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'burstStopLocations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveIQRate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveIQRateAllWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveMinimumPAPRAllWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrievePAPR': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveRFBlankingMarkerPositions': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'rfBlankingMarkerPositions',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveWaveformSize': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'waveformSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreBurstStartLocations': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'burstStartLocations',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreBurstStopLocations': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'burstStopLocations',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreIQRate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStorePAPR': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreRFBlankingMarkerPositions': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'rfBlankingMarkerPositions',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBurstStartLocationsFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'burstStartLocations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ReadBurstStopLocationsFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'burstStopLocations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualDataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualDataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ReadWaveformFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'eof',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ReadWaveformFromFileInterleavedIQ': {
        'cname': 'niWLANG_ReadWaveformFromFile',
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(waveform)'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'eof',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            }
        ],
        'returns': 'int32'
    },
    'SaveConfigurationToFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FileOperationMode',
                'name': 'fileOperation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetMappingMatrix': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'mappingMatrix',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'matrix_size'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixRows',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixColumns',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetMappingMatrixInterleavedIQ': {
        'cname': 'niWLANG_SetMappingMatrix',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'mappingMatrix',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'matrix_size'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(mappingMatrix)'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixRows',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numMappingMatrixColumns',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetOFDMPacketExtensionThresholds': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'ppet16',
                'size': {
                    'mechanism': 'len',
                    'value': 'ppet16ArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'ppet8',
                'size': {
                    'mechanism': 'len',
                    'value': 'ppet8ArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfSpaceTimeStreams',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSpaceTimeStreamsArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'ruSize',
                'size': {
                    'mechanism': 'len',
                    'value': 'ruArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'ppet16ArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'ppet8ArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfSpaceTimeStreamsArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'ruArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'SetVectorAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetVectorAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niWLANGenerationSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxWLANGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlangen/functions_addon.py sha256=2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679 bytes=34 -->
## FILE: source/codegen/metadata/nirfmxwlangen/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlangen/functions_addon.py`
- sha256: `2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679`
- bytes: 34

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/__init__.py sha256=611949f4948381f8b291e6d6ea1085f16bc0b35b6bdec6305e929480e44cf5b0 bytes=373 -->
## FILE: source/codegen/metadata/nirfsa/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/__init__.py`
- sha256: `611949f4948381f8b291e6d6ea1085f16bc0b35b6bdec6305e929480e44cf5b0`
- bytes: 373

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/attributes.py sha256=c4f0ce1db5599934af40c17a515de64cd17537c81bc86e0a88357019248be42e bytes=192203 -->
## FILE: source/codegen/metadata/nirfsa/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/attributes.py`
- sha256: `c4f0ce1db5599934af40c17a515de64cd17537c81bc86e0a88357019248be42e`
- bytes: 192203

````python
attributes = {
    1050002: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to validate attribute values and function parameters.  If enabled, NI-RFSA validates the parameter values that you  pass to NI-RFSA functions. Range checking parameters is very useful for  debugging. After you validate your program, you can set this attribute to  VI_FALSE to disable range checking and maximize performance.\n\n Default Value: VI_TRUE \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Use niRFSA_InitWithOptions function to override this value.\n\n'
        },
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether NI-RFSA queries the NI-RFSA device status after each operation. Querying  the device status is useful for debugging. After you validate your program, you can set  this attribute to VI_FALSE to disable status checking and maximize performance. \n\n NI-RFSA can choose to ignore status checking for  particular attributes, regardless of the setting of this attribute.\n\n Default Value: VI_FALSE  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Use niRFSA_InitWithOptions function to override this value.\n\n'
        },
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to cache the value of attributes. If you set this attribute to VI_TRUE,  NI-RFSA tracks the current NI-RFSA device settings and avoids sending redundant commands  to the device. \n\n NI-RFSA can always cache or never cache  particular attributes, regardless of the setting of this attribute.\n\n Use the niRFSA_InitWithOptions function to override the default value.\n\n Default Value: VI_TRUE  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read only',
        'documentation': {
            'description': ' Specifies whether NI-RFSA simulates I/O operations. This attribute is  useful for debugging applications without using hardware. After a session  is opened, you cannot change the simulation state. Use the niRFSA_InitWithOptions  function to enable simulation.\n\n Default Value: VI_FALSE  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' PXI-5600/5661 support setting this attribute to VI_FALSE only. \n\n'
        },
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the IVI engine keeps a list of the value coercions it  makes for integer and real type attributes.\n\n Default Value: VI_FALSE  \n\n Supported Devices: None     ',
            'note': ' This attribute is currently not supported.\n\n'
        },
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': ' The Driver Setup string is used to set the initial values for attributes that  are specific to NI-RFSA. The format of the Driver Setup string is:\n Tag: Value\n Tag is the name of the DriverSetup string attribute. Value is the value set to  the attribute. To set multiple attributes, separate their assignments with a  semicolon.\n\n The DriverSetup string can include the following tags:\n\n PXI-5661, PXIe-5663/5663E/5665/5667-Digitizer-Specifies the resource name of the digitizer to use for  this session. If this Driver Setup tag is not specified, the resource name for the  downconverter associated in MAX is used. An example of a Driver Setup string  is DriverSetup=Digitizer:pxi1slot4. If you want to use the PXI-5600, PXIe-5601/5603 with an  external digitizer, use the following Driver Setup tag:  DriverSetup=Digitizer:<external>.\n\n PXIe-5663/5663E/5665/5667-LO-Specifies the resource name of the LO source to use for this  session. If you want to use the PXIe-5601 with an LO other than the PXI/PXIe-5652 or use the  5603 with an LO other than the 5653, use the following Driver Setup  tag: DriverSetup=LO:<external>.\n\n 5667—RFConditioning—Specifies the resource name of the RF Conditioning source to use for this session. \n\n 5667—IFConditioning—Specifies the resource name of the IF Conditioning source to use for this session. \n\n Refer to the niRFSA_InitWithOptions function for additional information about the  optionString parameter. Refer to the getting started guide for your device for information  about configuring your device in MAX. \n\n Default Value:  (empty string) \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings.\n\n Default Value: VI_FALSE  \n\n Supported Devices: None      ',
            'note': ' Interchangeability check is unsupported.\n\n'
        },
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read-write',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the prefix for NI-RFSA. The name of each user-callable  function in NI-RFSA starts with this prefix. This attribute returns niRFSA. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates the resource descriptor NI-RFSA uses to identify the physical device.  If you initialize NI-RFSA with a logical name, this attribute contains the resource  name that corresponds to the entry in the IVI Configuration Utility. \n\n If you initialize NI-RFSA with the resource name, this attribute  contains that value.\n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': ' Contains the logical name you specified when opening the current IVI session. You may pass  a logical name to the niRFSA_init function or the niRFSA_InitWithOptions function.  The IVI Configuration Utility must contain an entry for the logical name. The logical name  entry refers to a driver session section in the IVI Configuration file. The driver  session section specifies a physical device and initial user options. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a comma-separated list of supported devices.\n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'access': 'read-write',
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the firmware revision information for the  NI-RFSA device you are currently using.\n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the name of the manufacturer for the NI-RFSA device you are  currently using.\n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the model number or name of the NI-RFSA  device that you are currently using.\n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the name of the vendor that supplies NI-RFSA.  This attribute returns National Instruments. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains a brief description of NI-RFSA. This attribute returns  RF Signal Analyzer Instrument Driver. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read-write',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read-write',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains additional version information about NI-RFSA.  For example, NI-RFSA can return Driver: NI-RFSA 2.6, Compiler: MSVC 7.10,  Components: IVI Engine 4.00, VISA-Spec 4.00 as the value of this attribute. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the session to either acquire I/Q data or to compute a power  spectrum over the specified frequency range.\n\n Default Value: NIRFSA_VAL_IQ \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'AcquisitionType',
        'name': 'ACQUISITION_TYPE',
        'type': 'ViInt32'
    },
    1150002: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the center frequency in a spectrum acquisition.  An acquisition consists of a span of data surrounding  the center frequency.  The value is expressed in hertz (Hz).\n\n  Units: hertz (Hz) \n\n Default Values: \n\n PXIe-5694: 193.6 MHz \n\n PXIe-5820: 0 Hz \n\n PXIe-5830/5831: 6.5 GHz \n\n All other devices: 1 GHz \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Use this attribute to tune the downconverter when using external digitizer mode. \n\n'
        },
        'name': 'CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150003: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency range of the computed spectrum, in hertz (Hz).  For example, if you specify a center frequency of 1 GHz and a span of 100 MHz,  the spectrum ranges from 950 MHz to 1,050 MHz after zoom processing. This value  may be coerced based on hardware settings and RF downconverter specifications. \n\n NI-RFSA performs multispan acquisitions by dividing the total requested span into equally  sized subspans based on the device instantaneous bandwidth at the range of frequencies you  specify. NI-RFSA combines these subspans to yield a multispan acquisition. You can use the  NIRFSA_ATTR_FFT_WIDTH attribute to improve amplitude accuracy and avoid unwanted effects  such as filter roll-off and spurs across the span you select.\n\n instantaneous bandwidth, NI-RFSA performs multiple acquisitions and combines  them into a spectrum of the size you requested. \n\n At spans wider than 40 MHz,  the dither noise can leak into the lower frequencies and the upper frequencies  of the IF pass band.  The amount of leakage depends on the resolution bandwidth, resolution bandwidth type,  and FFT window  you select. Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more  information about dithering. \n\n PXIe-5663/5663E-NI-RFSA does not support multispan acquisitions from frequency  ranges that correspond with different instantaneous bandwidths. For example, you cannot configure  a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a  second from 120 MHz to  130 MHz  because the instantaneous bandwidth for frequencies above 120 MHz is different  than instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.\n\n PXIe-5665 (14 GHz)/5667 (7 GHz)-If you enable the downconverter preselector, the device instantaneous bandwidth is only a  typical specification. \n\n Default Value: 10 MHz  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     ',
            'note': ' For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. '
        },
        'name': 'SPECTRUM_SPAN',
        'type': 'ViReal64'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the reference level, in dBm. The reference level represents the maximum expected power of an RF input signal. \n\n Refer to the NIRFSA_ATTR_REFERENCE_LEVEL_HEADROOM attribute for information about margin that NI-RFSA adds.  Refer to the NIRFSA_ATTR_EXTERNAL_GAIN attribute for information about how configuring  an external gain and a reference level affect attenuation. \n\n Default Value: 0 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661,  PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5840/5841     ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n\n'
        },
        'name': 'REFERENCE_LEVEL',
        'type': 'ViReal64'
    },
    1150005: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the nominal attenuation setting, in dB, for all  attenuators before the first mixer in the RF signal chain.  If you do not set this attribute, NI-RFSA automatically chooses  an attenuation setting based on the reference level you configure.  The valid values for this attribute depend on the device configuration. \n\n PXI-5600/5661-You can change the attenuation value to modify the amount of noise and distortion.  Higher attenuation levels increase the noise level while decreasing distortion; lower  attenuation levels  decrease the noise level while increasing distortion.\n\n PXIe-5601/5663/5663E-You can change the attenuation value  to modify the amount of noise and distortion. Higher attenuation  levels increase the noise level while decreasing distortion; lower attenuation levels  decrease the noise  level while increasing distortion.\n\n PXIe-5603/5605/5606/5665/5668-You can set multiple attributes to modify the attenuation values for the device.  Refer to PXIe-5665 RF Attenuation and Signal Levels for more information about  configuring attenuation. \n\n  PXIe-5667-This attribute specifies the nominal attenuation setting for all attenuators before the first  RF mixer in the input signal path. This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED  attribute is set to NIRFSA_VAL_DISABLED. \n\n PXIe-5693—This attribute is read-only and returns the nominal RF attenuation of the PXIe-5693. \n\n Units: dB \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661,  PXIe-5663/5663E/5665/5667/5668, PXIe-5693     '
        },
        'name': 'ATTENUATION',
        'type': 'ViReal64'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the mixer level, in dBm. The mixer level represents the attenuation value to apply to  the input RF signal as it reaches the first mixer in the signal chain.  If you do not set this attribute, NI-RFSA automatically selects an optimal mixer level value based  on the reference level. The valid values for this attribute depend on your device configuration. \n If you set the NIRFSA_ATTR_MIXER_LEVEL and NIRFSA_ATTR_MIXER_LEVEL_OFFSET attributes at the same time,  NI-RFSA returns an error. \n\n Default Values: \n PXI-5600/5661: -30 \n PXIe-5601: N/A \n PXIe-5603/5605/5665/5667: -10 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668     ',
            'note': ' This attribute is read-only for the PXIe-5667 when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED. \n\n'
        },
        'name': 'MIXER_LEVEL',
        'type': 'ViReal64'
    },
    1150007: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the I/Q rate for the acquisition The value is expressed in samples per second (S/s). \n\n Refer to the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute for more information about device specific instantaneous  bandwidth limits. You can also refer to the NI PXIe-5665 Specifications for more information about instantaneous bandwidth device specifications.\n\n phase coherency performance and leak into the lower frequencies and the upper frequencies of the IF passband.  Refer to the NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED attribute for more information about dithering. \n For the PXIe-5663/5663E/5665/5667, when you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute  to NIRFSA_VAL_ONBOARD_CLOCK_STR, the downconverter instantaneous bandwidth is greater than or equal to the  coerced I/Q rate times 0.8. For the PXIe-5665, the actual signal bandwidth is further limited by the combination of the  chosen IF filter and anti-aliasing filter.\n\n PXI-5661-You should not need to configure an I/Q rate higher than 25 megasamples per second (MS/s) because  the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing  effects at negative frequencies because the IF frequency of the PXI-5600 is 15 MHz.\n\n PXIe-5663/5663E-Your maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use.  Refer to the PXIe-5601 RF downconverter overview for more information about instantaneous bandwidth. \n\n PXIe-5665-Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency if you have enabled the preselector (YIG-tuned filter). \n\n PXIe-5667—Your maximum allowed instantaneous bandwidth depends on the selected RF preselector filter and whether the preselector on the RF dowconverter is enabled. \n\n PXIe-5668-Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use and  whether or not you enable the highpass filter or preselector (YIG-tuned filter). \n\n Units: S/s \n\n Default Value: 1 MHz  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. At I/Q rates above 50 MS/s, the dither noise can affect '
        },
        'name': 'IQ_RATE',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device acquires a finite number of samples or acquires continuously. Default Value: VI_TRUE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'NUMBER_OF_SAMPLES_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of samples to acquire. This attribute is only valid if the  NIRFSA_ATTR_NUM_SAMPLES_IS_FINITE attribute is set to VI_TRUE. \n\n This attribute is supported in RF list mode. You can use this attribute in RF list mode to acquire  variable length records when using the NIRFSA_ATTR_CONTIGUOUS_MULTIRECORD attribute. \n\n Default Value: 1,000  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'NUMBER_OF_SAMPLES',
        'type': 'ViInt64'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device stops after acquiring the specified number of records or acquires records continuously. \n\n Default Value: VI_TRUE \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'NUMBER_OF_RECORDS_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150011: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of records to acquire if the  NIRFSA_ATTR_NUM_RECORDS_IS_FINITE attribute is set to VI_TRUE. Default Value: 1 \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'NUMBER_OF_RECORDS',
        'type': 'ViInt64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the units of the power spectrum. \n\n Default Value: NIRFSA_VAL_DBM  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'PowerSpectrumUnits',
        'name': 'POWER_SPECTRUM_UNITS',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the resolution along the x-axis of the spectrum.  NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If the  NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES attribute is specified, that value overrides  this value. \n\n Units: hertz (Hz) \n\n Default Value: 100 kHz  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'RESOLUTION_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies how the NIRFSA_ATTR_RESOLUTION_BANDWIDTH attribute is expressed. \n\n Default Value: NIRFSA_VAL_RBW_3DB \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'BandwidthType',
        'name': 'RESOLUTION_BANDWIDTH_TYPE',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of acquisitions to average.  The averaging process returns the final result after the number  of averages is complete.\n\n Default Value: 10  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECTRUM_NUMBER_OF_AVERAGES',
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the averaging mode for the spectrum acquisition. \n\n Default Value: NIRFSA_VAL_NO_AVERAGING  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'AveragingMode',
        'name': 'SPECTRUM_AVERAGING_MODE',
        'type': 'ViInt32'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the time-domain window type. \n\n Default Values: \n\n PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841: NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS \n\n PXIe-5667: NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'FftWindowType',
        'name': 'FFT_WINDOW_TYPE',
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of spectral lines expected with the current power spectrum configuration.  If you do not configure this attribute, NI-RFSA selects an appropriate value based on  the NIRFSA_ATTR_RESOLUTION_BANDWIDTH attribute. If you configure this attribute,  NI-RFSA coerces the NIRFSA_ATTR_RESOLUTION_BANDWIDTH value based on the number of  spectral lines requested and the value of the NIRFSA_ATTR_SPECTRUM_SPAN attribute. \n\n Default Value: N/A  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'NUMBER_OF_SPECTRAL_LINES',
        'type': 'ViInt32'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Reference clock source. \n\n Default Values: \n\n PXIe-5694: NIRFSA_VAL_REF_IN_STR \n\n PXIe-5840 with PXIe-5653: NIRFSA_VAL_REF_IN_2_STR \n\n All other devices: NIRFSA_VAL_ONBOARD_CLOCK_STR \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5694, if your application requires an external LO source, set this property to NIRFSA_VAL_NONE_STR. \n\n'
        },
        'enum': 'RefClockSource',
        'name': 'REF_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150020: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Reference clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector.  This attribute is only valid when the NIRFSA_ATTR_REF_CLOCK_SOURCE attribute is set to  NIRFSA_VAL_CLK_IN_STR, NIRFSA_VAL_REF_IN_STR, or NIRFSA_VAL_REF_IN_2_STR. \n\n Valid Values: \n PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5840/5841: 10 MHz \n PXIe-5603/5605/5665/5667/5668: 5 MHz to 100 MHz, in increments of 1 MHz \n PXIe-5841 with PXIe-5655: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz * y, where y is 4, 8, 16, 24, 25, or 32. \n\n Default Value: 10 MHz  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source of the Sample clock timebase, which is the timebase used  to control waveform sampling.\n\n Default Value: NIRFSA_VAL_ONBOARD_CLOCK_STR  \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668     '
        },
        'enum': 'DigitizerSampleClockTimebaseSource',
        'name': 'DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'type': 'ViString'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency, in hertz (Hz), of the external clock used as the timebase  source if you set the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute  to an external source, such as NIRFSA_VAL_CLK_IN_STR or NIRFSA_VAL_LO_REF_CLK_STR. \n\n PXI-5661-If this attribute is set to a value less than 60 MHz, signals at frequencies  just above the 20 MHz passband of the downconverter may be aliased back into the  passband. This aliasing occurs because the IF frequency of the downconverter is 15 MHz,  and the upper end of the passband is 25 MHz. At sampling rates below 60 MHz, the  Nyquist frequency is close to the end of the passband and creates aliases that are  not filtered effectively by the downconverter.\n\n PXIe-5663/5663E/5665/5667-The PXIe-5663/5663E/5665/5667 supports only a 150 MHz external clock. \n\n PXIe-5668-The PXIe-5668 supports only a 2 GHz external clock. \n\n Units: hertz (Hz) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668     '
        },
        'name': 'DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE',
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the signal to drive the 10 MHz Reference clock on the PXI  backplane. This option can be configured only when the PXI-5600 is installed in  Slot 2 of the PXI chassis. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600 (external digitizer mode), PXI-5661     '
        },
        'enum': 'PxiChassisClk10Source',
        'name': 'PXI_CHASSIS_CLK10_SOURCE',
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether you want the Start trigger to be a digital edge or  software trigger.\n\n attribute to NIRFSA_VAL_SPECTRUM or if you set the acquisitionType parameter to NIRFSA_VAL_SPECTRUM  using the cviniRFSA_ConfigureAcquisitionType function.\n\n Default Value: NIRFSA_VAL_NONE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Set this property to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE '
        },
        'enum': 'GeneralTriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Start trigger. This attribute is used  only when the NIRFSA_ATTR_START_TRIGGER_TYPE attribute is set to  NIRFSA_VAL_DIGITAL_EDGE.\n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150026: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active edge for the Start trigger. This attribute is used only  when NIRFSA_ATTR_START_TRIGGER_TYPE is set to NIRFSA_VAL_DIGITAL_EDGE. \n\n Default Value: NIRFSA_VAL_RISING_EDGE \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     '
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150027: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the exported Start trigger.\n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150028: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether you want the Reference trigger to be a digital edge, I/Q  power edge, or software trigger. \n\n attribute to NIRFSA_VAL_SPECTRUM or if you set the acquisitionType parameter to NIRFSA_VAL_SPECTRUM  using the cviniRFSA_ConfigureAcquisitionType function.\n\n Default Value: NIRFSA_VAL_NONE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     ',
            'note': ' Set this property to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE '
        },
        'enum': 'RefTriggerType',
        'name': 'REF_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the digital edge Reference trigger. This  attribute is used only when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set  to NIRFSA_VAL_DIGITAL_EDGE. \n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150030: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active edge for the Reference trigger. This attribute is used only  when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to  NIRFSA_VAL_DIGITAL_EDGE. Default Value: NIRFSA_VAL_RISING_EDGE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'DigitalEdge',
        'name': 'DIGITAL_EDGE_REF_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the exported Reference trigger. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the minimum time, in seconds, that must elapse after the Start trigger is  received before the device recognizes a Reference trigger. \n\n Units: seconds \n\n Default Value: 0 \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'type': 'ViReal64'
    },
    1150034: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the minimum time, in seconds, that must elapse between Reference triggers of  two records. The device does not recognize the Reference trigger of the next record  before this minimum time elapses. \n\n Units: seconds \n\n Default Value: 0 \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'REF_TO_REF_TRIGGER_HOLDOFF',
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of pretrigger samples--the samples acquired before the  Reference trigger is received--to be acquired per record. \n\n Default Value: 0 \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'REF_TRIGGER_PRETRIGGER_SAMPLES',
        'type': 'ViInt64'
    },
    1150036: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether you want the Advance trigger to be a digital edge or  software trigger. \n\n attribute to NIRFSA_VAL_SPECTRUM or if you set the acquisitionType parameter to NIRFSA_VAL_SPECTRUM  using the niRFSA_ConfigureAcquisitionType function.\n\n Default Value: NIRFSA_VAL_NONE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Set this property to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE '
        },
        'enum': 'GeneralTriggerType',
        'name': 'ADVANCE_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Advance trigger. This attribute is used  only when the NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE attribute is set to  NIRFSA_VAL_DIGITAL_EDGE. \n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150038: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the exported Advance trigger. \n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150039: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether you want the Arm Reference trigger to be a digital edge or software trigger. \n\n attribute to NIRFSA_VAL_SPECTRUM or if you set the acquisitionType parameter to NIRFSA_VAL_SPECTRUM  using the niRFSA_ConfigureAcquisitionType function.\n\n Default Value: NIRFSA_VAL_NONE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Set this property to NIRFSA_VAL_NONE if you set the NIRFSA_ATTR_ACQUISITION_TYPE '
        },
        'enum': 'GeneralTriggerType',
        'name': 'ARM_REF_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150040: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the digital edge Arm Reference trigger. This attribute  is used only when the NIRFSA_ATTR_ARM_REF_TRIGGER_TYPE attribute  is set to NIRFSA_VAL_DIGITAL_EDGE. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5840/5841 devices only support  (empty string). \n\n'
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the Ready for Start event. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150042: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the Ready for Advance event. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150043: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the Ready for Reference event. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150044: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the End of Record event. \n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the reference location within the acquired record from which to  begin fetching. \n\n  Default Value: N/A  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'FetchRelativeTo',
        'name': 'FETCH_RELATIVE_TO',
        'type': 'ViInt32'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the offset relative to the position specified by the  NIRFSA_ATTR_FETCH_RELATIVE_TO attribute from which to start fetching data.  Offset can be a positive or negative value. \n\n Default Value: 0 \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FETCH_OFFSET',
        'type': 'ViInt64'
    },
    1150047: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the number of records the RF vector signal analyzer has acquired. \n\n Default Value: N/A  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'RECORDS_DONE',
        'type': 'ViInt32'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables use of the digital equalization filter for the RF downconverter.\n PXIe-5820/5830/5831/5840/5841-The only valid value for this attribute is VI_TRUE. \n\n cannot set this attribute  to VI_TRUE if the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute  is set to NIRFSA_VAL_LO_REF_CLK_STR.\n\n parameter to NIRFSA_VAL_SPECTRUM using the niRFSA_ConfigureAcquisitionType function.  If you set acquisitionType to NIRFSA_VAL_IQ, digital IF equalization is enabled for  instantaneous bandwidths larger than 300 kHz (PXIe-5665) or 20 MHz (PXIe-5667).  You cannot perform digital IF equalization for instantaneous bandwidths less than or  equal to 300 kHz (PXIe-5665) or 20 MHz (PXIe-5667).\n\n so NI-RFSA does not equalize the preselector distortions.\n\n Default Value: VI_TRUE, if the device configuration is supported. \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5665 (14 GHz))/5667 (7 GHz)  device, the preselector is not part of the IF filter path, '
        },
        'name': 'DIGITAL_IF_EQUALIZATION_ENABLED',
        'type': 'ViBoolean'
    },
    1150049: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FFT_WINDOW_SIZE',
        'type': 'ViInt32'
    },
    1150050: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the size of the fast Fourier transform (FFT). \n\n Default Value: N/A  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FFT_SIZE',
        'type': 'ViInt32'
    },
    1150051: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the module. \n\n PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n PXIe-5830/5831: To use this attribute, you must first set the channelName parameter of the niRFSA_SetAttributeViReal64 function  using the appropriate string for your instrument configuration. Setting the niRFSA_SetAttributeViReal64 attribute is not required for the PXIe-3621/3622.  Refer to the NI-RFSA C Function Reference for more inforamation about the appropriate string to use for your hardware configuration. \n\n Units: degrees C \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'DEVICE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150053: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the serial number of the RF downconverter module. \n\n For the PXIe-5830/5831, this attribute returns the serial number of the PXIe-3621/3622. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this attribute returns the serial number of the VST module.'
        },
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150054: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for the Done event. \n\n Default Value:  (empty string)  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'ExportTerminal',
        'name': 'EXPORTED_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the channel from which the device monitors the trigger. NI-RFSA  currently supports only 0  as the value of this attribute. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150056: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the power level, in dBm, at which the device triggers. The device  asserts the trigger when the signal crosses the level specified by the value  of this attribute, taking into consideration the specified slope. If you are  using external gain, refer to the NIRFSA_ATTR_EXTERNAL_GAIN attribute for more information  about how this attribute affects the I/Q power edge trigger level. \n\n Default Value: 0 \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     '
        },
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_LEVEL',
        'type': 'ViReal64'
    },
    1150057: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device asserts the trigger when the signal power is rising or  falling. When you set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute to  NIRFSA_VAL_IQ_POWER_EDGE, the device asserts the trigger when the signal power exceeds  the specified level with the slope you specify. \n\n Default Value: NIRFSA_VAL_RISING_SLOPE \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'AnalogSlope',
        'name': 'IQ_POWER_EDGE_REF_TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1150058: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies a time duration, in seconds, for which the signal must be quiet  before the device arms the trigger. The signal is quiet when it is below the  trigger level if the trigger slope, specified by the  NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE attribute, is set to  NIRFSA_VAL_RISING_SLOPE or above the trigger level if the trigger slope is  set to NIRFSA_VAL_FALLING_SLOPE.\n\n By default this value is set to 0, which means the device does not wait for a  quiet time before arming the trigger. This attribute is useful to trigger the  acquisition on signals containing repeated bursts, but for which each burst  may have large changes in signal power within itself. By configuring the  minimum quiet time to the time between bursts, you can ensure that the trigger  occurs at the beginning of a burst rather than at the  signal power change within  a burst.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     '
        },
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'type': 'ViReal64'
    },
    1150059: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the expected carrier frequency of the incoming signal for demodulation. The  RF vector signal analyzer tunes to this frequency. NI-RFSA may coerce this value  based on hardware settings and the RF downconverter specifications. \n\n Units: hertz (Hz) \n\n Default Values:  \n\n PXIe-5644/5645/5646, PXIe-5840/5841: 1 GHz \n\n PXIe-5820: 0 Hz \n\n PXIe-5830/5831: 6.5 GHz \n\n All other devices: 100 MHz \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n\n'
        },
        'name': 'IQ_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150060: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the trigger delay time, in seconds. The trigger delay time is the  length of time the IF digitizer waits after it receives the trigger  before it asserts the Reference event. \n\n Units: seconds \n\n Default Value: 0  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'REF_TRIGGER_DELAY',
        'type': 'ViReal64'
    },
    1150061: {
        'access': 'read-write',
        'documentation': {
            'description': ' Indicates the minimum time between temperature sensor readings in seconds. When you  call the niRFSA_ReadPowerSpectrumF64 function, the niRFSA_ReadIQSingleRecordComplexF64 function,  or the niRFSA_Initiate function, NI-RFSA checks whether at least the amount of  time specified by this attribute has elapsed before reading the hardware temperature. \n\n function or the NIRFSA_ATTR_DOWNCONVERTER_GAIN attribute. \n\n Default Value: 30 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' NI-RFSA ignores this attribute if you called the niRFSA_PerformThermalCorrection '
        },
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'ViReal64'
    },
    1150065: {
        'access': 'read-write',
        'documentation': {
            'description': ' Returns the net signal gain for the NI-RFSA device at the current NI-RFSA settings and temperature.  NI-RFSA scales the acquired I/Q and spectrum data from the digitizer using the value of this attribute. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661,  PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5830/5831/5840/5841    '
        },
        'name': 'DOWNCONVERTER_GAIN',
        'type': 'ViReal64'
    },
    1150067: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the loop bandwidth of the RF downconverter tuning PLLs. To  set this attribute, the NI-RFSA device must be in the Configuration state.\n\n PXI-5600/5661: For signal bandwidths greater than 10 MHz, NIRFSA_VAL_WIDE is the only  value supported for this attribute.\n\n PXIe-5601/5663/5663E: The PXIe-5601 does not support the NIRFSA_VAL_MEDIUM value.  This attribute is not supported if you are using an external LO. \n\n PXIe-5830/5831/5840/5841: The PXIe-5840/5841 supports only NIRFSA_VAL_MEDIUM for this attribute. This attribute is not supported if you are using an external LO. \n\n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViInt32  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Default Values: \n PXI-5600: NIRFSA_VAL_WIDE \n PXIe-5601: NIRFSA_VAL_NARROW \n\n PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841: NIRFSA_VAL_MEDIUM \n\n Supported Devices: PXI-5600, PXIe-5601 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E, PXIe-5830/5831/5840/5841     '
        },
        'enum': 'LoopBandwidth',
        'name': 'DOWNCONVERTER_LOOP_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150068: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the LO signal frequency for the configured center frequency.\n\n If you are using the NI RF vector signal analyzer with an external LO, use this  attribute to specify  the LO frequency that the external LO source passes into the LO IN or LO IN1 connector, located  on the RF downconverter front panel. If you are using an external LO, reading the value of this  attribute after configuring the rest of the parameters returns the LO frequency needed  by the device. \n\n Set this attribute to the actual LO frequency because NI-RFSA corrects  for any difference between expected and actual LO frequencies. \n\n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViReal64  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Default Value: \n\n PXIe-5694: 215 MHz All other devices: 0 \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5840/5841     '
        },
        'name': 'LO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the LO injection side.\n\n PXIe-5601/5663/5663E-For frequencies below 517.5 MHz or above 6.4125 GHz, the LO  injection side is fixed and NI-RFSA returns an error if you specify the incorrect value.  If you do not configure this attribute, NI-RFSA selects the default LO injection side  based on the downconverter center frequency. Reset this attribute to  return to automatic behavior. \n\n PXIe-5603/5605/5665 (3.6 GHz)/5667 (3.6 GHz)-Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is not  supported for this device. PXIe-5605/5665 (14 GHz)/5667 (7 GHz)-Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is supported for this device for frequencies  greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed. \n\n PXIe-5606/5668-Setting this attribute to NIRFSA_VAL_LO_INJECTION_LOW_SIDE is supported for certain frequencies in  high band, varying by final IF frequency. This configuration is not calibrated and device specifications are not  guaranteed. \n\n'
        },
        'enum': 'LoInjectionSideValues',
        'name': 'LO_INJECTION_SIDE',
        'type': 'ViInt32'
    },
    1150070: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the vertical range of the digitizer. The vertical range is defined as the absolute value  of the input range for a channel. The default vertical range works for all device configurations,  but you can use this attribute to optimize performance if you know that the signal level at the  digitizer input terminal is low. \n\n This value is expressed in volts. For example, to acquire a sine wave that  spans between -0.05 V and +0.05 V, set this attribute to 1.0. \n\n Default Value: 1.0 \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5840/5841     ',
            'note': ' This attribute is read-only for the PXIe-5840/5841. \n\n'
        },
        'name': 'DIGITIZER_VERTICAL_RANGE',
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether fractional resampling is enabled on the digitizer.  Fractional resampling allows the digitizer to achieve very fine resolution on its I/Q rate value.  Setting this attribute to VI_FALSE improves spectral performance. \n\n PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841——The only valid value for this attribute is VI_TRUE. \n\n PXIe-5668—When using a 400 MHz FPGA image, the only valid value for this attribute is VI_TRUE.  When using a 800 MHz FPGA image, the only valid value for this attribute is VI_FALSE.  Refer to the NI-RFSA Instrument Driver FPGA Extension topic for more information on FPGA images. \n\n Default Value: VI_TRUE \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'ENABLE_FRACTIONAL_RESAMPLING',
        'type': 'ViBoolean'
    },
    1150072: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies a comma-separated list of the terminals at which to export the Reference clock. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5840/5841    '
        },
        'enum': 'RefClockOutTerminal',
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150074: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the device attenuation to a value that has the actual calibrated IF attenuation  closest to the desired value. \n\n Valid Values: 0 to 30 \n\n Default Value: N/A \n\n Supported Devices: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667, PXIe-5693     '
        },
        'name': 'IF_ATTENUATION',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the desired IF filter path, regardless of the RF band chosen by NI-RFSA.\n\n Default Value: N/A \n\n Supported Devices: PXIe-5601     '
        },
        'enum': 'IfFilter',
        'name': 'IF_FILTER',
        'type': 'ViInt32'
    },
    1150076: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the value of the RF attenuation from a table of valid configurations.  This attribute is valid only during a calibration session and when you set the  NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute to NIRFSA_VAL_DISABLED.\n\n Valid Values: 0 to 64 \n\n Default Value: N/A \n\n Supported Devices: PXIe-5693     '
        },
        'name': 'RF_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150077: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which RF attenuator table to use.\n\n Valid Values: 0 to 1 \n\n Default Value: N/A \n\n Supported Devices: PXIe-5601 (external digitizer mode), PXIe-5663/5663E     '
        },
        'name': 'RF_ATTENUATION_TABLE',
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF1 attenuation, in dB. The device IF1 attenuator is set to this nominal value.  Use this attribute, along with the NIRFSA_ATTR_IF2_ATTEN_VALUE attribute, when you  set the NIRFSA_ATTR_IF_FILTER attribute to NIRFSA_VAL_BYPASS. \n\n Valid Values: 0 to 15 \n\n Units: dB \n\n Default Value: N/A \n\n Supported Devices: PXIe-5601 (external digitizer mode), PXIe-5663/5663E     '
        },
        'name': 'IF1_ATTEN_VALUE',
        'type': 'ViReal64'
    },
    1150079: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF2 attenuation, in dB. The device IF2 attenuator is set to this nominal value.  Use this attribute, along with the NIRFSA_ATTR_IF1_ATTEN_VALUE attribute, when you  set the NIRFSA_ATTR_IF_FILTER attribute to NIRFSA_VAL_BYPASS. \n\n Valid Values: 0 to 15 \n\n Units: dB \n\n Default Value: N/A  \n\n Supported Devices: PXIe-5601 (external digitizer mode), PXIe-5663/5663E     '
        },
        'name': 'IF2_ATTEN_VALUE',
        'type': 'ViReal64'
    },
    1150080: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether dithering is enabled on the digitizer. \n\n Dithering adds band-limited noise in the analog signal path to help reduce  the quantization effects  of the A/D converter and improve spectral performance. On the PXIe-5622,  this out-of-band noise is  added at low frequencies up to approximately 12 MHz.\n\n PXIe-5663/5663E/5665/5667—When you enable dithering, the maximum signal level is reduced by up to 3 dB.  This signal level reduction  is accounted for in the nominal input ranges of the PXIe-5622. Therefore,  you can overrange the input  by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal  levels up to +7  dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering  to eliminate residual leakage of the dither signal into the  lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz.  This leakage can slightly raise the noise floor in the lower frequencies, thus  degrading the performance in high-sensitivity applications. When taking spectral  measurements, this leakage can also appear as a wide, low-amplitude signal  near 12.5 MHz and 62.5 MHz. The width and amplitude of the signal depends on your  resolution bandwidth and the type of time-domain window you apply to your FFT. \n\n PXIe-5668—When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the  PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power  with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains  the dither even if the dither signal is not in the displayed spectrum. The dither can affect  actions like power level triggering. \n\n Default Value: NIRFSA_VAL_ENABLED \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5820/5830/5831/5840/5841, only NIRFSA_VAL_ENABLED is supported. \n\n'
        },
        'enum': 'EnabledAttr',
        'name': 'DIGITIZER_DITHER_ENABLED',
        'type': 'ViInt32'
    },
    1150081: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the mechanical attenuator is enabled. Set this attribute to NIRFSA_VAL_ENABLED to use the mechanical atteuator.\n\n Disabling this attenuator can improve device performance. Refer to the PXIe-5663/5663E  RF Attenuation and Signal Levels for more information about the attenuators. \n\n Default Value: NIRFSA_VAL_ENABLED \n\n Supported Devices: PXIe-5601 (external digitizer mode), PXIe-5663/5663E     '
        },
        'enum': 'EnabledAttr',
        'name': 'MECHANICAL_ATTENUATOR_ENABLED',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables in-band retuning and specifies the current frequency, in hertz (Hz),  of the downconverter.   If you set this attribute, any measurements outside the instantaneous bandwidth  of the device are invalid.  To disable in-band retuning, reset the attribute or call the call the niRFSA_ResetDevice function. \n\n After you set this attribute, the downconverter is locked to that frequency  until the value is changed  or the attribute is reset. Locking the downconverter to a fixed value allows  frequencies within the  instantaneous bandwidth of the converter to be measured with minimal  overhead, decreasing tuning time. \n\n Valid Values: Any supported tuning frequency of the device \n PXIe-5820: The only valid value for this attribute is 0 Hz. \n\n Default Value: \n\n PXIe-5694: The default value for the PXIe-5694 is 193.6 MHz unless you set the  NIRFSA_ATTR_SIGNAL_CONDITIONING attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED,  in which case the default value is 187.5 MHz. \n\n All other devices: The carrier frequency or spectrum center frequency.  NI-RFSA sets this attribute to the default value based on the value of  the NIRFSA_ATTR_ACQUISITION_TYPE attribute. \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'DOWNCONVERTER_CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150083: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the RF path to use during calibration. This attribute is valid only during a  calibration session. When you set this attribute, NI-RFSA does not select the RF path based  on the downconverter center frequency.\n\n The following RF bands and associated frequency ranges apply to the PXIe-5601:\n RF band 1: 3 GHz to 6.6 GHz \n RF band 2: 330 MHz to 3 GHz \n RF band 3: 120 MHz to 330 MHz  \n RF band 4: 10 MHz to 120 MHz \n\n PXIe-5603—PXIe-5603 only uses RF band 1, which specifies a frequency range of 20 Hz to 3.6 GHz. \n\n PXIe-5605—The PXIe-5605 uses RF band 1 from 20 Hz to 3.6 GHz, the low band signal path, and RF band 2 from 3.6 GHz to 14 GHz, the high band signal path. \n\n PXIe-5606-The PXIe-5606 uses RF band 1 from 20 Hz to 3.6 GHz (20 Hz to 3.41 GHz if using the 320 MHz IF filter)  and RF band 2 from 3.6 GHz to 26.5 GHz (3.41 GHz to 26.5 GHz if using the 320 MHz IF filter). \n\n Default Values: \n PXIe-5603/5605 (low band)/5606—NIRFSA_VAL_EXT_CAL_RF_BAND_1  \n\n PXIe-5601/5605 (high band)—NIRFSA_VAL_EXT_CAL_RF_BAND_2 \n\n Supported Devices: PXIe-5601/5603/5605/5606, PXIe-5698     '
        },
        'enum': 'RfPathSelection',
        'name': 'CAL_RF_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150085: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the digitizer onboard memory in bytes. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841    '
        },
        'name': 'MEMORY_SIZE',
        'type': 'ViInt64'
    },
    1150086: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the center frequency of the IF output that corresponds to  the configured RF center frequency.\n\n The downconverter translates RF input frequency to the IF output  frequency by mixing it with the LO signal.  The following values are the nominal values for the IF frequency:\n\n PXI-5600 15 MHz\n PXIe-5601 53 MHz or 187.5 MHz\n PXIe-5603 187.5 MHz or 199 MHz\n PXIe-5605 187.5 MHz, 190 MHz, or 199 MHz \n PXIe-5606 187.5 MHz, 190 MHz, 199 MHz, 507.5 MHz, or 730 MHz \n PXIe-5694 NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED set to NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED and  NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED set to NIRFSA_VAL_DISABLED: 193.6 MHz \n NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED set to NIRFSA_VAL_ENABLED: 21.4 MHz \n NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED set to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED: 162.5 MHz to 212.5 MHz \n\n However, the coarse nature of the LO settings can cause the  downconverter to be unable to tune to the exact  LO frequency that would produce the nominal IF output. Any coercion  in the actual LO frequency results in the  IF output frequency being slightly off from the nominal value.\n\n Additionally, if you use the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY  and NIRFSA_ATTR_LO_FREQUENCY attributes  to program the downconverter, then the IF output frequency could be very  different from the nominal value.  NI-RFSA adjusts the acquired spectrum or I/Q data for the difference between  nominal and actual IF output  frequency. If you use an external digitizer with the NI RF downconverter,  use this attribute to specify the  actual IF output frequency. \n\n  Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694     '
        },
        'name': 'IF_OUTPUT_FREQUENCY',
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the delay duration units and interpretation for LO settling. Specify  the actual settling value using the NIRFSA_ATTR_FREQUENCY_SETTLING attribute.  This attribute is not supported if you are using an external LO. \n\n Default Value: NIRFSA_VAL_FSU_PPM \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5840/5841     '
        },
        'enum': 'FrequencySettlingUnits',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'ViInt32'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the value used for LO frequency settling. The units and interpretation  for this scalar value are specified using the NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS  attribute. This attribute is not supported if you are using an external LO. \n\n The valid values for this attribute depend on the NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS attribute. \n\n Valid Values:\n NIRFSA_VAL_FSU_SECONDS_AFTER_LOCK:\n 2 microseconds* to 80 milliseconds, resolution of approximately 2 microseconds (PXIe-5663/5663E)\n 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds (PXIe-5665/5667/5668) \n\n 1 microsecond* to 65 milliseconds, resolution of 1 microsecond (PXIe-5645/5646) \n\n 1 microsecond* to 10 seconds, resolution of 1 microsecond (PXIe-5830/5831/5840, PXIe-5840 with PXIe-5653 (using the PXIe-5840 internal LO),  PXIe-5831 with PXIe-5653 (using the PXIe-3622 LO)) \n\n 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds (PXIe-5840 with PXIe-5653 (using the PXIe-5653 LO),  PXIe-5831 with PXIe-5653 (using the PXIe-5653 LO)) \n\n NIRFSA_VAL_FSU_SECONDS_AFTER_IO:\n 0 microseconds to 80 milliseconds**, resolution of 1 microsecond (PXIe-5663/5663E/5665/5667/5668, PXIe-5840 with PXIe-5653 (using the PXIe-5653 LO), PXIe-5831 with PXIe-5653 (using the PXIe-5653 LO)) \n 1 microsecond to 65 milliseconds, resolution of 1 microsecond (PXIe-5645/5646) \n\n 0 microseconds to 10 seconds, resolution of 1 microsecond (PXIe-5830/5831/5840, PXIe-5840 with PXIe-5653 (using the PXIe-5840 internal LO) PXIe-5831 with PXIe-5653 (using PXIe-3622 LO)) \n\n NIRFSA_VAL_FSU_PPM:\n 1.0, 0.1, 0.01(PXIe-5663/5663E) \n 1.0, 0.1, 0.01, 0.001 (PXIe-5665/5667/5668) \n\n 1.0, 0.1, 0.01 (PXIe-5645/5646) \n\n 1.0 to 0.01 (PXIe-5830/5831/5840/5841, PXIe-5840 with PXIe-5653 (using the PXIe-5840 internal LO), PXIe-5831 with PXIe-5653) \n\n 1.0 to 0.001 (PXIe-5840 with PXIe-5653 (using the PXIe-5653 LO)) \n\n *If the NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS attribute is set to NIRFSA_VAL_FSU_TIME_AFTER_LOCK and the NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH  attribute is set to NIRFSA_VAL_NARROW, NI recommends a minimum settling time of 128 microseconds to ensure that the PLL lock stabilizes.  If the NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH is set to NIRFSA_VAL_WIDE, NI recommends a minimum settling time of 16 microseconds. \n **When in RF list mode, the valid values for NIRFSA_VAL_FSU_TIME_AFTER_IO are 0 microseconds to 50 milliseconds. \n\n Refer to the NIRFSA_ATTR_LO_SOURCE attribute for more information. \n\n Default Value: 0.1 \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5840/5841     ',
            'note': ' For the PXIe-5840 with PXIe-5653, the valid values depend on the module used as the LO source. '
        },
        'name': 'FREQUENCY_SETTLING',
        'type': 'ViReal64'
    },
    1150089: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the LO module.  this attribute is not supported if you are using an external LO. \n\n PXIe-5840/5841—If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5840/5841     ',
            'note': ' For the 5601/5603/5605/5606 (external digitizer mode) and PXI-5661, PXIe-5663/5663E/5665/5667/5668, '
        },
        'name': 'LO_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150090: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the digitizer module. \n\n PXIe-5820/5840/5841—If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n Default Value: N/A \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     '
        },
        'name': 'DIGITIZER_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150091: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the revision of the RF downconverter module.\n\n For the PXIe-5830/5831, this attribute returns the revision of the PXIe-3621/3622. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668,  PXIe-5693/5694/5698, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this attribute returns the revision of the VST module. '
        },
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150092: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the configuration list for RF list mode to make active  for configuration or initiation. \n\n Activating a list makes all attributes in the list reflect the value of the attributes  that correspond to the set specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST and  the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attributes. Set this attribute to an empty  string to disable RF list mode. \n\n Default Value:  (empty string) for devices that support RF list mode. For all other devices, the default value is N/A. \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'ACTIVE_CONFIGURATION_LIST',
        'type': 'ViString'
    },
    1150093: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step in the configuration list for RF list mode to make active  for configuration or initiation. \n\n Activating a list makes all attributes in the list reflect the value of the attributes  that correspond to the set specified by the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST and  the NIRFSA_ATTR_ACTIVE_CONFIGURATION_LIST_STEP attributes. \n\n Default Value: 0 for devices that support RF list mode. For all other devices, the default value is N/A.\n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'ACTIVE_CONFIGURATION_LIST_STEP',
        'type': 'ViInt64'
    },
    1150094: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the gain, in dB, of a switch (or cable) connected before the RF IN connector  of an NI-RFSA system. When you set this attribute and the NIRFSA_ATTR_ATTENUATION and NIRFSA_ATTR_IF_ATTENUATION  values, NI-RFSA calculates appropriate attenuator settings based on the value of this attribute and the  value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute. In this case, NI-RFSA interprets the reference level  as the maximum expected power level of the signal at the input of the external gain device.  For more information about attenuation, refer to the Attenuation and Signal Levels  topic for your device in the NI RF Vector Signal Analyzers Help. \n\n With this attribute set, NI-RFSA reads the NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL  attribute value as the power level at the input of the external gain device at  which the NI-RFSA device should trigger. \n\n  Negative values indicate attenuation. \n\n the IQ IN connector.  Valid Values: -INF to +INF \n\n Units: dB \n\n Default Value: 0 \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841      ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n'
        },
        'name': 'EXTERNAL_GAIN',
        'type': 'ViReal64'
    },
    1150095: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n     '
        },
        'name': 'CONFIGURATION_LIST_STEP_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150096: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the time, in seconds, that the timer waits before sending a Timer event. \n\n After the timer reaches zero, it automatically restarts. \n\n Units: seconds \n\n Default Value: 0.01  \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For the PXIe-5820/5830/5831/5840/5841, this attribute must be set for the timer to start. If you do not set this attribute, the timer is disabled. \n\n'
        },
        'name': 'TIMER_EVENT_INTERVAL',
        'type': 'ViReal64'
    },
    1150097: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether peer-to-peer streaming is enabled for the active stream endpoint.\n\n This attribute is endpoint based. \n\n Default Value: VI_FALSE \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_ENABLED',
        'type': 'ViBoolean'
    },
    1150098: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the number of peer-to-peer streams supported by the device. \n\n Default Value: 0  \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_FIFO_ENDPOINT_COUNT',
        'type': 'ViInt64'
    },
    1150099: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the number of complex samples transferred through the peer-to-peer stream endpoint  since the endpoint was last reset. \n\n Default Value: 0 \n\n Supported Devices: PXIe-5663/5663E/5665, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_SAMPLES_TRANSFERRED',
        'type': 'ViInt64'
    },
    1150100: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current number of complex samples available in the peer-to-peer endpoint.\n\n Default Value: 0  \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' The complex samples are composed of two 16-bit words, with the I data as the LSB. \n\n'
        },
        'name': 'P2P_SAMPLES_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150101: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the largest number of complex samples available in the peer-to-peer endpoint since this  attribute was last read. \n\n Default Value: 0  \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_MOST_SAMPLES_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150102: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the size, in samples, of the peer-to-peer endpoint.\n\n  Default Value: 0 \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_ENDPOINT_SIZE',
        'type': 'ViInt64'
    },
    1150103: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates whether the endpoint has overflowed. An overflow condition occurs when data  is written to the endpoint faster than it can be streamed from it. During an overflow,  data in the endpoint begins to be overwritten. Reset the device or close the session to  reset the overflow condition. \n\n Default Value: VI_FALSE  \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_ENDPOINT_OVERFLOW',
        'type': 'ViBoolean'
    },
    1150104: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum bandwidth that the device can consume. \n\n  than the value you specify for this attribute. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665     ',
            'note': ' The NI device limits itself to transfer fewer bytes per second on the PCI Express bus '
        },
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum number of samples to transfer at one time from  the device to host memory. Increasing this number should result in better  fetching performance because the driver does not need to restart the transfers  as often. However, increasing this number may increase the amount of page-locked  memory required from the system. \n\n Default Value: 0x400000 \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668     '
        },
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150106: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the offset to apply to the initial I and Q phases.\n\n Valid Values: -180 to 180 \n Default Value: 0  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'PHASE_OFFSET',
        'type': 'ViReal64'
    },
    1150107: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether a limit is placed on the number of records and the size of the records by  the size of the device onboard memory. When a peer-to-peer stream is enabled and onboard memory  is disabled, any fetch calls result in an error. \n\n Default Value: VI_FALSE  \n\n Supported Devices: PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'P2P_ONBOARD_MEMORY_ENABLED',
        'type': 'ViBoolean'
    },
    1150109: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF attenuation index from a table of valid settings.  To select a correct attenuation table, set this attribute in conjunction with  the NIRFSA_ATTR_CAL_IF_FILTER_SELECTION attribute. This attribute is valid only  during a calibration session. \n\n Valid Values: 0 to 25 \n\n Default Value: 0 \n\n Supported Devices: PXIe-5694     '
        },
        'name': 'CAL_IF_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150110: {
        'access': 'read-write',
        'documentation': {
            'description': ' Selects the value of RF electronic attenuation from a table of valid configurations.  This attribute is valid only during a calibration session and when you set  the NIRFSA_ATTR_CAL_RF_PATH_SELECTION attribute to NIRFSA_ATTR_VAL_EXT_CAL_RF_BAND_1. \n\n Default Value: N/A  \n\n Supported Devices: PXIe-5603/5605/5606     '
        },
        'name': 'CAL_RF_ELECTRONIC_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150111: {
        'access': 'read-write',
        'documentation': {
            'description': ' Selects the value of the RF mechanical attenuation configuration from a table of  valid configurations. This attribute is valid only during a calibration session. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5603/5605/5606     '
        },
        'name': 'CAL_RF_MECHANICAL_ATTENUATION_INDEX',
        'type': 'ViInt32'
    },
    1150112: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF filter path during calibration. The attribute is  valid only during a calibration session. \n\n Default Value: NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4 \n\n Supported Devices: PXIe-5694     '
        },
        'enum': 'CalIFFilterSelection',
        'name': 'CAL_IF_FILTER_SELECTION',
        'type': 'ViInt32'
    },
    1150113: {
        'access': 'read-write',
        'documentation': {
            'description': ' Selects the LO signal path used during calibration. During noncalibration sessions,  NI-RFSA implicitly derives the LO signal path from the center frequency. During  calibration sessions, you must explicitly specify the LO signal path. This attribute is  valid only during a calibration session. \n\n Default Value: NIRFSA_VAL_EXT_CAL_LO_PATH_1  \n\n Supported Devices: PXIe-5603/5605/5606     '
        },
        'enum': 'LoPathSelection',
        'name': 'CAL_LO_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150114: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the LO1 attenuation, in dB, during a calibration session. The default value is  31.5 dB. This attribute is valid only during a calibration session. \n\n Valid Values: 0 to 31.5 \n\n Default Value: 31.5  \n\n Supported Devices: PXIe-5603/5605/5606     '
        },
        'name': 'CAL_LO1_ATTENUATION',
        'type': 'ViReal64'
    },
    1150115: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the LO2 attenuation, in dB, during a calibration session. The default value is  15.5 dB. This attribute is valid only during a  calibration session. \n\n Valid Values: 0 to 15.5 \n\n Default Value: 15.5 \n\n Supported Devices: PXIe-5603/5605/5606      '
        },
        'name': 'CAL_LO2_ATTENUATION',
        'type': 'ViReal64'
    },
    1150116: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the LO3 attenuation, in dB, during a calibration session. The default  value is 15.5 dB. This attribute is valid only during a calibration session. \n\n Valid Values: 0 to 15.5 \n\n Default Value: 15.5  \n\n Supported Devices: PXIe-5603/5605/5606      '
        },
        'name': 'CAL_LO3_ATTENUATION',
        'type': 'ViReal64'
    },
    1150117: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values:  \n\n PXIe-5820/5840/5841:  /ModuleName/ai/0/ReadyForStartEvent, where ModuleName is the name of your device in MAX. \n\n All other devices: /DigitizerName/ReadyForStartEvent, where DigitizerName is the name associated with your digitizer module in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/ReadyForStartEvent, where BasebandModule is the name of the baseband module of your device in MAX. \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'READY_FOR_START_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150118: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/ReadyForAdvanceEvent, where ModuleName is the name of your device in MAX. \n\n All other devices: /DigitizerName/ReadyForAdvanceEvent, where DigitizerName is the name associated with your digitizer module in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/ReadyForAdvanceEvent, where BasebandModule is the name of the baseband module of your device in MAX. \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'READY_FOR_ADVANCE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150119: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/ReadyForReferenceEvent, where ModuleName is the name of your device in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/ReadyForReferenceEvent, where BasebandModule is the name of the baseband module of your device in MAX. \n\n All other devices: /DigitizerName/ReadyForReferenceEvent, where DigitizerName is the name associated with your digitizer module in MAX. \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'READY_FOR_REF_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150120: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values:  \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/EndOfRecordEvent, where ModuleName is the name of your device in MAX. \n\n All other devices: /DigitizerName/EndOfRecordEvent, where DigitizerName is the name associated with your digitizer module in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/EndOfRecordEvent, where BasebandModule is the name of the baseband module of your device in MAX. \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'END_OF_RECORD_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150121: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/DoneEvent, where ModuleName is the name of your device in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/DoneEvent, where BasebandModule is the name of the baseband module of your device in MAX. \n\n All other devices: /DigitizerName/DoneEvent, where DigitizerName is the name associated with your digitizer module in MAX. \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150122: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/StartTrigger, where ModuleName is the name of your device in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/StartTrigger, where BasebandModule is the name of the baseband module of your device in MAX. \n\n All other devices: /DigitizerName/StartTrigger, where DigitizerName is the name associated with your digitizer module in MAX.  Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150123: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/RefTrigger, where ModuleName is the name of your device in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/RefTrigger, where BasebandModule is the name of your baseband module of your device in MAX. \n\n All other devices: /DigitizerName/RefTrigger, where DigitizerName is the name associated with your digitizer module in MAX. \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'REF_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150124: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n\n Default Values: \n\n PXIe-5820/5840/5841: /ModuleName/ai/0/AdvanceTrigger, where ModuleName is the name of your device in MAX. \n\n All other devices: /DigitizerName/AdvanceTrigger, where DigitizerName is the name associated with your digitizer module in MAX. \n\n PXIe-5830/5831: /BasebandModule/ai/0/AdvanceTrigger, where BasebandModule is the name of the baseband module of your device in MAX. \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841  \t'
        },
        'name': 'ADVANCE_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150125: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the instantaneous bandwidth of the device. The instantaneous bandwidth is  the effective real-time bandwidth of the signal path for your configuration. The value  is expressed in hertz (Hz). \n\n To change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans,  use the NIRFSA_ATTR_FFT_WIDTH attribute.\n\n  bandwidth is constrained to 50 MHz or 25 MHz, depending on the digitizer option you  purchased.\n\n PXI-5661-The PXI-5600 RF downconverter bandwidth is 20 MHz.\n\n PXIe-5663/5663E-Your maximum allowed instantaneous bandwidth depends on the downconverter center  frequency you use. Refer to the PXIe-5601 RF downconverter overview for more information about  instantaneous bandwidth.\n\n correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one  span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous  bandwidth for frequencies above 120 MHz is different than the instantaneous bandwidth for  frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.\n\n PXIe-5665-Your maximum allowed instantaneous bandwidth is independent of the downconverter center frequency.\n Refer to the NI PXIe-5665 Specifications for more information about instantaneous bandwidth.\n\n PXIe-5665 (14 GHz), PXIe-5668-If you have enabled the preselector for the PXIe-5605, the device instantaneous  bandwidth value is only a typical specification. For multispan acquisitions, NI-RFSA uses this  typical specification as the maximum size for the acquisition subspans.\n\n  PXIe-5605 provide a nominal 80 MHz bandwidth at -6 dB.  At frequencies greater than 3.6 GHz, the PXIe-5605 provides a nominal bandwidth of 47 MHz at -6 dB  with the preselector (YIG-tuned filter) enabled.\n\n PXIe-5693—This attribute is read-only for the PXIe-5693. The value for the device instantaneous bandwidth  depends on the value for the RF preselector filter. \n\n PXIe-5694, PXIe-5667—If your application uses the PXIe-5694 as part of an PXIe-5667 spectrum monitoring receiver  or the PXIe-5694 as a stand-alone device, NI-RFSA determines the appropriate IF filter to use based on the  value that you set for this attribute. \n\n conditioning by setting the NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED attribute to  NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED. \n\n PXIe-5644/5645/5646-This attribute is read-only for the PXIe-5644/5645/5646. Refer to the specifications  document for your devices for more information about instantaneous bandwidth. \n\n PXIe-5840/5841-Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the PXIe-5840 Specifications for more information about instantaneous bandwidth. Set this attribute to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select will be greater than or equal to the requested instantaneous  bandwidth. If this attribute is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth. \n\n Default Value: N/A  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693/5694, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' Device instantaneous bandwidths greater than 20 MHz are available only when you bypass all signal '
        },
        'name': 'DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150126: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the index of the current RF configuration list step that is executing in RF list  mode. The list is zero-indexed. You can query this attribute only when a list is executed. \n\n PXIe-5663E/5665/5667—This attribute can be read only when a configuration list is running. \n PXIe-5644/5645/5646—This attribute always returns 0 when the configuration list is not running.\n PXIe-5820/5830/5831/5840/5841—If a configuration list is not running, this attribute returns the last step of a configuration list that is programmed  to the hardware. If the device was last initiated without an active configuration list, this attribute returns 0. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5663E/5665/5667, PXIe-5820/5830/5831/5840/5841 \t'
        },
        'name': 'CONFIGURATION_LIST_STEP_IN_PROGRESS',
        'type': 'ViInt64'
    },
    1150127: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of dB by which to adjust the device mixer level. The default value  is 0, which specifies device settings that are the best compromise between  distortion and noise.  Specifying a positive value for this attribute configures the device for moderate distortion and  low noise, and specifying a negative value results in low distortion and higher noise. \n\n You cannot set the NIRFSA_ATTR_MIXER_LEVEL and NIRFSA_ATTR_MIXER_LEVEL_OFFSET attributes at  the same time. \n\n Units: dB  Default Value: 0 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668     ',
            'note': ' This attribute is read-only for the PXIe-5667 when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED. \n\n'
        },
        'name': 'MIXER_LEVEL_OFFSET',
        'type': 'ViReal64'
    },
    1150128: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the level of mechanical attenuation for the RF path, in dB.\n\n PXIe-5667—This attribute is read-only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED attribute is set to NIRFSA_VAL_DISABLED. \n\n PXIe-5668 with PXIe-5698—This attribute is read-only when the NIRFSA_ATTR_RF_PREAMP_ENABLED attribute is set to NIRFSA_VAL_RF_PREAMP_ENABLED. \n\n Units: dB \n\n Valid Values:\n PXIe-5601/5663/5663E-0, 16 \n PXIe-5603/5665 (3.6 GHz)-0, 10, 20, 30 \n PXIe-5605/5665 (14 GHz), PXIe-5606/5668-0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75 \n PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path—0, 10, 20, 30 \n PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path—0 \n PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path—0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75 \n PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path—0 \n PXIe-5668 with PXIe-5698 with the NIRFSA_ATTR_RF_PREAMP_ENABLED attribute set to NIRFSA_VAL_RF_PREAMP_ENABLED—5 \n\n Default Value: N/A \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668     '
        },
        'name': 'MECHANICAL_ATTENUATION',
        'type': 'ViReal64'
    },
    1150129: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the RF preamplifier is enabled in the system. \n PXIe-5667, PXIe-5830/5831/5840/5841—If you set this attribute to NIRFSA_VAL_RF_PREAMP_AUTOMATIC, NI-RFSA selects the  preamplifier state based on the value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute. \n\n PXIe-5667—The NIRFSA_VAL_RF_PREAMP_AUTOMATIC value is supported only when the NIRFSA_ATTR_LOW_FREQUENCY_BYPASS_ENABLED  attribute is set to NIRFSA_VAL_DISABLED. If the reference level is greater than -25 dBm,  NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm,  NI-RFSA sets the NIRFSA_ATTR_RF_PREAMP_ENABLED attribute to NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH. \n\n PXIe-5668 with PXIe-5698—If you set this attribute to NIRFSA_ATTR_RF_PREAMP_ENABLED, only the  preamplifier on the PXIe-5698 is used, and the preamplifier on the PXIe-5668 remains disabled. \n\n Only devices with an RF preamplifier support setting this attribute  to NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH or NIRFSA_VAL_RF_PREAMP_ENABLED. \n\n Default Value:  \n\n PXIe-5830/5831: NIRFSA_VAL_PREAMP_AUTOMATIC \n All other devices: NIRFSA_VAL_RF_PREAMP_DISABLED \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646,  PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5840/5841     ',
            'note': ' All devices support setting this attribute to NIRFSA_VAL_RF_PREAMP_DISABLED. '
        },
        'enum': 'RfPreampEnabled',
        'name': 'RF_PREAMP_ENABLED',
        'type': 'ViInt32'
    },
    1150130: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the level of the IF signal leaving the system, in dBm.  Use this attribute to increase or decrease the nominal IF signal output level to  achieve better measurement results.\n If you set the NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL and  NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET attributes at the same time,  NI-RFSA returns an error.\n\n the IF output power level may be higher than the value you request. Read the value of this  attribute to determine the configured IF output power level. \n\n can apply, the NIRFSA_ATTR_REFERENCE_LEVEL attribute, the  NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attribute, and the NIRFSA_ATTR_SPECTRUM_CENTER_FREQUENCY  attribute or NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute, depending on your acquisition type. \n\n Units: dBm \n\n Default Value: \n\n PXIe-5667: -2 dBm \n PXIe-5668: -1 dBm \n All other devices: –6 dBm \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694    ',
            'note': ' The value of this attribute is limited by the amount of IF attenuation that the downconverter '
        },
        'name': 'IF_OUTPUT_POWER_LEVEL',
        'type': 'ViReal64'
    },
    1150131: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of dB by which to adjust the default IF output power level. This  attribute does  not depend on absolute IF output power levels, so you can use it to adjust  the IF output power level  on all NI-RFSA devices without knowing the exact default value. Use this attribute to increase or  decrease the nominal output level to achieve better measurement results. The  default value for the offset  is 0 dB, which results in an IF OUT output power level of -6 dBm. \n\n You cannot set the  NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL and NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET attributes at  the same time. \n\n Units: dB \n\n Default Value: 0 \n\n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668    '
        },
        'name': 'IF_OUTPUT_POWER_LEVEL_OFFSET',
        'type': 'ViReal64'
    },
    1150132: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the tunable preselector is enabled on the downconverter. \n\n NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH.  Only devices with a preselector support setting this attribute to NIRFSA_VAL_PRESLECTOR_ENABLED. \n\n Default Value: NIRFSA_VAL_PRESELECTOR_DISABLED if the device has no preselector. \n NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH if the device has a preselector.  \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5840/5841     ',
            'note': ' All devices support setting this attribute to NIRFSA_VAL_PRESELECTOR_DISABLED or '
        },
        'enum': 'DownconverterPreselectorEnabledAttr',
        'name': 'DOWNCONVERTER_PRESELECTOR_ENABLED',
        'type': 'ViInt32'
    },
    1150134: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to enable the LO OUT terminals on the installed devices. \n\n PXIe-5601-The only valid value for this attribute is VI_TRUE. \n\n PXIe-5603/5605/5606—If you want to daisy-chain multiple devices together using the same LO source,  set this attribute to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN  terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively. \n\n PXIe-5694-You can enable this attribute only if you set the NIRFSA_ATTR_LO_SOURCE attribute  to NIRFSA_VAL_LO_IN_STR, or if you set the NIRFSA_ATTR_LO_SOURCE attribute to  NIRFSA_VAL_ONBOARD_STR and the NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED attribute to  NIRFSA_VAL_ENABLED. \n\n PXIe-5830/5831-To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViBoolean  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Default Values: \n PXIe-5601, PXIe-5663/5663E: VI_TRUE \n PXIe-5603/5605/5606, PXIe-5644/5645/5646, PXIe-5665/5667/5668, PXIe-5694, PXIe-5830/5831/5840/5841: VI_FALSE  \n\n Supported Devices: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5830/5831/5840/5841     ',
            'note': ' If you are sharing an LO for the PXIe-5830/5831 between and NI-RFSA and NI-RFSG session, ensure both sessions use the same shared setting. \n\n'
        },
        'name': 'LO_EXPORT_ENABLED',
        'type': 'ViBoolean'
    },
    1150135: {
        'access': 'read-write',
        'documentation': {
            'description': ' Adjusts the dynamics of the current driving the YIG main coil.\n\n frequency to settle significantly faster for some frequency transitions at the  expense of increased phase noise. This attribute is not supported if you are  using an external LO. \n\n Default Value: NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_NORMAL  \n\n Supported Devices: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668     ',
            'note': ' Setting this attribute to NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_FAST allows the '
        },
        'enum': 'LoYIGMainCoilDrive',
        'name': 'LO_YIG_MAIN_COIL_DRIVE',
        'type': 'ViInt32'
    },
    1150136: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns whether a preselector is available on the RF downconverter module. \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841     '
        },
        'name': 'PRESELECTOR_PRESENT',
        'type': 'ViBoolean'
    },
    1150137: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns whether an RF preamplifier is available on the downconverter module.\n\n  Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'RF_PREAMP_PRESENT',
        'type': 'ViBoolean'
    },
    1150139: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the location in a path where a calibration tone is injected or whether  the tone is disabled. \n\n Default Value: NIRFSA_VAL_CAL_TONE_DISABLED  \n\n Supported Devices: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668      '
        },
        'enum': 'CalToneMode',
        'name': 'DOWNCONVERTER_CAL_TONE_MODE',
        'type': 'ViInt32'
    },
    1150140: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the RF downconverter calibration tone, in hertz (Hz).\n\n  Valid Values: 134 MHz to 13.2 GHz \n\n Default Value: 612.5 MHz \n\n Supported Devices: PXIe-5603/5605/5606 (external digitizer mode), NI, 5665/5667/5668      '
        },
        'name': 'DOWNCONVERTER_CAL_TONE_FREQUENCY',
        'type': 'ViReal64'
    },
    1150141: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF attenuation table to be used for external calibration. This attribute is  valid only in a calibration session. \n\n Default Value: NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_STANDARD  \n\n Supported Devices: PXIe-5603/5605     '
        },
        'enum': 'CalIFAttenTableSelection',
        'name': 'CAL_IF_ATTENUATION_TABLE_SELECTION',
        'type': 'ViInt32'
    },
    1150142: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.  This attribute configures NI-RFSA to optimize downconverter gain to measure a lower power adjacent channel, adding  gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.  attribute to a value less than 300 kHz. For the PXIe-5665 (14 GHz), this attribute is supported only if you set the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH  or NIRFSA_ATTR_SPECTRUM_SPAN attribute to a value less than 300 kHz by using the 300 kHz IF filter, or to a value  between 300 kHz and 5 MHz by using the 5 MHz IF filter. \n\n NI-RFSA coerces this attribute to zero for the PXI-5600, PXIe-5601 and the PXIe-5667. For all other devices, read the coerced value  of this attribute to determine the actual amount of gain applied. \n\n Default Value: 0 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668     ',
            'note': ' For the PXIe-5665 (3.6 GHz), this attribute is supported only if you set the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH or NIRFSA_ATTR_SPECTRUM_SPAN '
        },
        'name': 'MINIMUM_ACPR',
        'type': 'ViReal64'
    },
    1150144: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the oversampling ratio used by the the digitizer onboard signal processing (OSP)  when you are in spectrum acquisition mode. This attribute allows you to acquire a larger  bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows. \n\n PXIe-5644/5645/5646: The only valid value for this attribute is 1. Default Value: 1.0 \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SPECTRUM_OSP_SAMPLING_RATIO',
        'type': 'ViReal64'
    },
    1150146: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the IF filter through path  with the value you set for this attribute. \n\n Default Value: 0 \n\n Supported Devices: PXIe-5603/5605      '
        },
        'name': 'CALIBRATION_CORRECTION_THROUGH_FILTER',
        'type': 'ViReal64'
    },
    1150147: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the 300 kHz IF filter path  with the value you set for this attribute.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5603/5605/5606      '
        },
        'name': 'CALIBRATION_CORRECTION_300_KHZ_FILTER',
        'type': 'ViReal64'
    },
    1150148: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the 5 MHz IF filter path  with the value you set for this attribute.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5603/5605/5606      '
        },
        'name': 'CALIBRATION_CORRECTION_5_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150149: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the RF input channel is AC- or DC-coupled on a downconverter. \n\n is present and set to NIRFSA_VAL_DC when the DC block is not present to ensure device  specifications are met and to ensure the use of proper calibration data. For more  information about removing or attaching the DC block on the PXIe-5605, refer to the  PXIe-5665 Theory of Operation topic, the PXIe-5605 RF Downconverter Front Panel topic, or the PXIe-5667 Theory of Operation topic  in this help file. \n\n Default Value: NIRFSA_VAL_AC \n\n Supported Devices: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668     ',
            'note': ' For the PXIe-5605/5606/5665/5667/5668, this attribute must be set to NIRFSA_VAL_AC when the DC block '
        },
        'enum': 'ChannelCoupling',
        'name': 'CHANNEL_COUPLING',
        'type': 'ViInt32'
    },
    1150151: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer. Use this attribute to maximize  the dynamic range of the digitizer by increasing the maximum IF power the ADC can measure without creating OSP overflows.  Because of the device amplitude response, some wide-band signals normally attenuated by the signal analyzer go through the  IF digitizer without causing an ADC overflow warning. During IF equalization, these wide-band digitizer input signals may become  mathematically amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.  You can use this attribute when OSP calculations would generate an overflow while applying digital filters to the data.  The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified attribute value before  further onboard processing. Set this attribute to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to  use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the  correct scaled data, in absolute levels, is always returned regardless of the value of this attribute. \n\n Valid Values: 0.25 to 1.0 \n\n Default Values:\n PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5840/5841: 1.0 \n PXIe-5665 (14 GHz))/5667 (7 GHz): 0.8 \n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841    '
        },
        'name': 'OSP_DATA_SCALING_FACTOR',
        'type': 'ViReal64'
    },
    1150154: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to allow the device to acquire more records than can fit in the device memory of the PXIe-5622/5624. \n\n NI-RFSA returns an error. If this attribute is set to TRUE, NI-RFSA returns an error only in the event of an acquisition buffer overflow.\n\n Default Value: VI_FALSE  \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' This attribute is always set to VI_TRUE for the PXIe-5644/5645/5646 and the PXIe-5820/5830/5831/5840/5841. \n\n'
        },
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'type': 'ViBoolean'
    },
    1150155: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step size for the RF attenuation level. The actual RF attenuation is coerced up to the  next highest multiple of this step size.  You can also set this value to change the step size for the device within the supported device precision and configuration. \n\n PXI-5600-The device configuration supports only the following attenuation step size values: 10, 20, 30, 40, and 50. \n PXIe-5601-The attenuation is calculated based on the actual calibrated value closest to the  desired value, so the step size varies as the actual gain values vary between consecutive attenuation settings.\n PXIe-5603-The device configuration supports attenuation changes in 1 dB steps.\n PXIe-5605-The available attenuation step size depends on the specified center frequency. In  the high band signal path (input frequencies greater than 3.6 GHz), the only available attenuation is the step attenuator  that you can change in 5 dB steps. In the low band signal path (input frequencies less than or  equal to 3.6 GHz), an additional 31 dB of solid-state attenuation is available in 1 dB steps.  The 5 dB default value indicates that, even when in the low band signal path, NI-RFSA changes the  attenuation in 5 dB steps using only the mechanical attenuator. You can use this attribute to affect  when the device changes the attenuation settings. To use the solid-state attenuation in the low band  signal path, change the step size to a value other than a multiple of 5 (for example, a step size of 1 dB).  If you use a value other than a multiple of 5 while in the high band of the PXIe-5605, NI-RFSA returns an error.\n\n Valid Values: \n PXI-5600/5661:10, 20, 30, 40, and 50 \n PXIe-5601/5663/5663E:0.0 to 93.0, continuous \n PXIe-5603/5665 (3.6 GHz):1.0 to 74.0, in 1 dB steps \n PXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band): 1.0 to 106.0, in 1 dB steps \n PXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (hight band): 5.0 to 75.0, in 5 dB steps \n PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path—1.0 to 74.0, in 1 dB steps \n PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path— 1.0 \n PXIe-5667 (7 GHz) using the PXIe-5693 preselector low frequency bypass path— 1.0 to 106.0 in 1 dB steps \n PXIe-5667 7 GHz) using the PXIe-5693 RF preselector filter path— 1.0 \n\n Default Value: \n PXI-5600/5661: 10.0 \n PXIe-5601/5663/5663E: 0.0 \n PXIe-5603/5665 (3.6 GHz): 1.0 \n PXIe-5605/5665 (14 GHz): 5.0 \n PXIe-5667—1.0 \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668     '
        },
        'name': 'RF_ATTENUATION_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150157: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to enable or disable the step gain amplifier. \n\n Default Value: NIRFSA_VAL_STEP_GAIN_DISABLED \n\n Supported Devices: PXIe-5694      '
        },
        'enum': 'StepGainEnabled',
        'name': 'STEP_GAIN_ENABLED',
        'type': 'ViInt32'
    },
    1150158: {
        'access': 'read-write',
        'name': '5665_PRESELECTOR_TUNING_DAC_VALUE',
        'type': 'ViInt32'
    },
    1150159: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the temperature, in degrees Celsius, that NI-RFSA uses to calculate the device configuration settings. \n\n temperature to calculate best attenuation settings. Set this attribute only if you want NI-RFSA to maintain the same device configuration settings from acquisition to acquisition, independent  of device temperature changes.\n\n PXIe-5820/5830/5831/5840/5841- This attribute is read-only. \n\n Units:  degrees C \n\n Default Value: N/A \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' For most applications, you can choose not to set this attribute, so NI-RFSA uses the device '
        },
        'name': 'DEVICE_CONFIGURATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150160: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether all signal conditioning is enabled on the PXIe-5694. \n\n NI-RFSA bypasses all signal conditioning, prevents any signal downconversion,  and fixes the values for NIRFSA_ATTR_DOWNCONVERTER_GAIN attribute, the  NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, and the NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute. \n\n Default Value: NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED \n\n Supported Devices: PXIe-5694     ',
            'note': ' If you set this attribute to NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, '
        },
        'enum': 'SignalConditioningEnabled',
        'name': 'SIGNAL_CONDITIONING_ENABLED',
        'type': 'ViInt32'
    },
    1150161: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether downconversion to 21.4 MHz is enabled for the IF conditioning module.  The IF output frequency is 21.4 MHz when you enable this attribute, and it is 193.6 MHz  when you disable this attribute. \n\n NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED, you cannot set the  NIRFSA_ATTR_IF_CONDITIONING_DOWN_CONVERSION_ENABLED attribute to NIRFSA_VAL_ENABLED. \n\n Default Values: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5667, PXIe-5694     ',
            'note': ' For the PXI-5661, PXIe-5663/5663E/5665, the only valid value for this attribute is NIRFSA_VAL_DISABLED. \n\n'
        },
        'enum': 'EnabledAttr',
        'name': 'IF_CONDITIONING_DOWN_CONVERSION_ENABLED',
        'type': 'ViInt32'
    },
    1150162: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source for the LO to be used to downconvert. If this attribute is set to  (empty string),  NI-RFSA uses the internal LO source. \n If no signal down conversion is required, this attribute will be ignored. \n\n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViString  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Default Value: NIRFSA_VAL_ONBOARD_STR Supported Devices: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5840/5841     ',
            'note': ' For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED_STR. \n\n'
        },
        'enum': 'LoSourceSelection',
        'name': 'LO_SOURCE',
        'type': 'ViString'
    },
    1150163: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the amplitude settling accuracy in decibels. \n NI-RFSA waits until the RF path settles within the specified accuracy level after calling the niRFSA_Initiate function. \n Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value. \n Units: dB \n\n Default Value: 0.5 \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'AMPLITUDE_SETTLING',
        'type': 'ViReal64'
    },
    1150164: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n     '
        },
        'name': 'DDC_REF_TRIGGER_OVERRIDE',
        'type': 'ViBoolean'
    },
    1150165: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n Default Value: 0 \n\n     '
        },
        'name': 'MINIMUM_RECONFIG_TIME',
        'type': 'ViReal64'
    },
    1150166: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the RF preselector filter to use. \n\n Default Values: \n PXIe-5667, PXIe-5693: NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_9 \n PXIe-5665: NIRFSA_VAL_RF_PRESELECTOR_FILTER_PATH_NONE \n\n Supported Devices: PXIe-5665/5667, PXIe-5693     ',
            'note': ' You can write to this attribute when using only the PXIe-5693 as a stand-alone device. \n\n '
        },
        'enum': 'RfPreselectorFilter',
        'name': 'RF_PRESELECTOR_FILTER',
        'type': 'ViInt32'
    },
    1150167: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the notch filter is enabled on the RF conditioning module. \n\n Default Value: NIRFSA_VAL_NOTCH_FILTER_DISABLED \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5693     '
        },
        'enum': 'NotchFilterEnabled',
        'name': 'NOTCH_FILTER_ENABLED',
        'type': 'ViInt32'
    },
    1150168: {
        'access': 'read-write',
        'name': 'CAL_TONE_STEP_ATTENUATION',
        'type': 'ViReal64'
    },
    1150169: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal  path during each signal acquisition.\n\n depending on the digitizer option you purchased.\n\n For more information about in-band retuning, refer to the  NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attribute.\n\n NI-RFSA treats the device instantaneous bandwidth as the effective real-time bandwidth  of the signal path. The span specifies the frequency range of the computed spectrum.  An RF vector signal analyzer can acquire a bandwidth only within the device instantaneous  bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth,  NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying  the FFT width, you can control the specific bandwidth obtained in each signal acquisition.  If you read the NIRFSA_ATTR_FFT_WIDTH attribute without setting it, NI-RFSA returns the  value of the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute.\n\n Valid Values:\n The lower limit for all FFT width supported devices is 7.325 kHz.\n\n PXIe-5663/5663E—The FFT width upper limit for the PXIe-5663/5663E depends on the  downconverter center frequency and on the module revision of the PXIe-5601 as illustrated  in the NIRFSA_ATTR_FFT_WIDTH attribute topic in the NI RF Vector Signal Analyzers help file. Refer to the  Identifying Module Revision topic for more information about determining which revision of  the PXIe-5601 RF downconverter you have installed. \n\n PXIe-5665/5667/5668—The upper limit of the FFT width is the maximum device instantaneous bandwidth.\n\n NI-RFSA determines the appropriate IF filter to use based on the value that you set  for the FFT width and your specific device. Refer to the NIRFSA_ATTR_FFT_WIDTH  topic in the NI RF Vector Signal Analzyers help for more information about the IF filters NI-RFSA uses with  the NIRSA_ATTR_FFT_WIDTH attribute.\n\n If you set the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, NI-RFSA selects the appropriate  IF filter based on the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute and the NIRFSA_ATTR_FFT_WIDTH  attribute determines how much bandwidth of that filter is used during acquisition. Refer to the  NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute to determine which IF filter corresponds to the  NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute setting.\n\n 47 MHz at -6 dB with the preselector enabled. The NIRFSA_ATTR_FFT_WIDTH attribute can override  the typical bandwidth of the PXIe-5605 up to 57 MHz using an external digitizer and up to 50 MHz  or 25 MHz depending on the PXIe-5622 digitizer option you purchased. The increase in bandwidth  results in faster signal acquisitions, but amplitude accuracy is decreased for spectrum  acquisitions, and magnitude and phase accuracy is decreased for I/Q acquisitions. National Instruments does not guarantee device specifications if you set the NIRFSA_ATTR_FFT_WIDTH  attribute greater than the warranted instantaneous bandwidth specification.\n\n and above. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5663/5663E/5665/5667/5668     ',
            'note': ' When using the PXIe-5606, the 765 MHz IF filter is only available at center frequencies of 3.6 GHz '
        },
        'name': 'FFT_WIDTH',
        'type': 'ViReal64'
    },
    1150170: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether input isolation is enabled.\n\n Enabling this attribute isolates the input signal at the RF IN connector on the RF downconverter  from the rest of the RF downconverter signal path. Disabling this attribute reintegrates the  input signal into the RF downconverter signal path.\n\n characteristic 50 Ohm impedance. A change in the device impedance may also cause a VSWR value  higher than the device specifications.\n\n For the PXIe-5830/5831, input isolation is supported for all available ports for your hardware configuration. \n\n Default Values: NIRFSA_VAL_DISABLED, if the device configuration is supported. \n Supported Devices: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5840/5841     ',
            'note': ' If you enable input isolation for your device, the device impedance is changed from the '
        },
        'enum': 'EnabledAttr',
        'name': 'INPUT_ISOLATION_ENABLED',
        'type': 'ViInt32'
    },
    1150172: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n     '
        },
        'enum': 'EnabledAttr',
        'name': 'CONTIGUOUS_MULTIRECORD',
        'type': 'ViInt32'
    },
    1150173: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n     '
        },
        'name': 'TIMER_START_SOURCE',
        'type': 'ViString'
    },
    1150174: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the power of a virtual signal connected to the RF IN connector on the  PXIe-5693 front panel when the calibration tone is enabled. \n You can enable a calibration tone for the PXIe-5693 by setting the  NIRFSA_ATTR_RF_CONDITIONING_CAL_TONE_MODE attribute to  NIRFSA_VAL_CAL_TONE_LOWBAND_RF or NIRFSA_VAL_CAL_TONE_HIGHBAND_RF. \n\n Units: dBm \n\n Default Value: N/A \n\n Supported Devices: PXIe-5693       '
        },
        'name': 'CAL_TONE_POWER_REFERRED_TO_RF_IN',
        'type': 'ViReal64'
    },
    1150175: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute is not for customer use. \n\n     '
        },
        'name': 'START_TRIGGER_DELAY',
        'type': 'ViReal64'
    },
    1150176: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master for synchronizing the shared  Start Trigger between multiple devices. The master device distributes the  synchronized Start Trigger to all devices in the system through the  Start Trigger distribution line. \n\n When synchronizing the Start Trigger, one device must always be designated  as the master. When the device is configured as a master, it actively drives  the Start Trigger distribution line. When the device is configured as a slave,  set the NIRFSA_ATTR_START_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE,  and the NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to NIRFSA_VAL_SYNC_START_TRIGGER_STR. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Default Value: VI_FALSE \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'SYNC_START_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150177: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the synchronized Start  Trigger signal. When synchronizing the Start Trigger, configure all  devices to use the same Start Trigger distribution line. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Valid Values: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4,  PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0 \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'SYNC_START_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150178: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master for synchronizing the shared  Reference Trigger between multiple devices. The master device distributes  the synchronized Reference Trigger to all devices in the system through  the Reference Trigger distribution line. \n\n When synchronizing the Reference Trigger, one device must always be designated  as the master. When the device is configured as a master, it actively drives  the Reference Trigger distribution line. When the device is configured as a  slave, set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE,  and the NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE attribute to NIRFSA_VAL_SYNC_REF_TRIGGER_STR. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Default Value: VI_FALSE \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'SYNC_REF_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150179: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the synchronized  Reference Trigger signal. When synchronizing the Reference Trigger,  configure all devices to use the same Reference Trigger distribution line. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Valid Values: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4,  PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0 \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645 \n\n '
        },
        'name': 'SYNC_REF_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150180: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the connector(s) to use to acquire the signal.  To set this attribute, the NI-RFSA device must be in the  Configuration state. \n\n Default Values: \n\n PXIe-5820: NIRFSA_VAL_IQ_IN \n All other devices: NIRFSA_VAL_RF_IN \n Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841 '
        },
        'enum': 'InputPort',
        'name': 'INPUT_PORT',
        'type': 'ViInt32'
    },
    1150181: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the frequency of the signal. The onboard signal  processing (OSP) will frequency shift the signal at this  frequency to baseband prior to acquiring it. \n\n Valid Values:  \n PXIe-5645: -60 MHz to +60 MHz \n PXIe-5820: -500 MHz to +500 MHz \n Default Value: 0 \n\n Supported Devices: PXIe-5645, PXIe-5820 \n\n ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_IN_PORT_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150182: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the terminal configuration of the I/Q terminals. \n\n To use this attribute, you must use the channelname parameter of the niRFSA_SetAttributeViInt32 function  to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q  channels by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n PXIe-5820-The only valid value for this attribute is NIRFSA_VAL_DIFFERENTIAL. \n Default Value: NIRFSA_VAL_DIFFERENTIAL Supported Devices: PXIe-5645, PXIe-5820 ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n\n'
        },
        'enum': 'IqInPortTermConfig',
        'name': 'IQ_IN_PORT_TERMINAL_CONFIGURATION',
        'type': 'ViInt32'
    },
    1150183: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the voltage range for the I/Q terminals. \n\n To use this attribute, you must use the channelname parameter of the niRFSA_SetAttributeViReal64 function  to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q  channels by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n The voltage range in differential mode is configurable from 2 Vpk-pk to 0.032 Vpk-pk in  1 dB steps. In single-ended mode, valid ranges are half those for  differential. Values are always coerced up to the next valid range. \n\n Valid Values: \n PXIe-5645: 0 Vpk-pk to 2 Vpk-pk for differential terminal configuration,  0 Vpk-pk to 1 Vpk-pk for single-ended terminal configuration. \n PXIe-5820: 0 Vpk-pk to 4 Vpk-pk for differential terminal configuration. \n Default Value: 2 Vpk-pk \n\n Supported Devices: PXIe-5645, PXIe-5820 \n\n ',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n\n'
        },
        'name': 'IQ_IN_PORT_VERTICAL_RANGE',
        'type': 'ViReal64'
    },
    1150184: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master for synchronizing the  shared Advance Trigger between multiple devices. The master device  distributes the synchronized Advance Trigger to all devices in the  system through the Advance Trigger distribution line. \n\n When synchronizing the Advance Trigger, one device must always be designated  as the master. When the device is configured as a master, it actively drives  the Advance Trigger distribution line. When the device is configured as a slave,  set the NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE attribute to NIRFSA_VAL_DIGITAL_EDGE,  and the NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE attribute to  NIRFSA_VAL_SYNC_ADVANCE_TRIGGER_STR. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Default Value: VI_FALSE \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'SYNC_ADVANCE_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150185: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the synchronized Advance  Trigger signal. When synchronizing the Advance Trigger, configure all  devices to use the same Advance Trigger distribution line. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Valid Values: PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4,  PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0 \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5644/5645 \n\n '
        },
        'name': 'SYNC_ADVANCE_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150186: {
        'access': 'read-write',
        'documentation': {
            'description': ' Returns the power level, in dBm, expected at the LO IN terminal  when the NIRFSA_ATTR_LO_SOURCE attribute is set to NIRFSA_VAL_LO_IN_STR. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841 ',
            'note': ' For the PXIe-5644/5645/5646, this attribute is always read-only. \n\n'
        },
        'name': 'LO_IN_POWER',
        'type': 'ViReal64'
    },
    1150187: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to use fractional mode for the LO PLL or not. Fractional mode  gives a finer frequency step resolution, but may result in non-harmonic spurs.  Refer to the PXIe-5644 Specifications or the PXIe-5645 Specifications  for more information about fractional mode and non harmonic spurs. \n\n For the PXIe-5841 with PXIe-5655, this attribute is ignored if the PXIe-5655 is used as the LO source. \n\n applicable when using the internal LO. \n\n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViInt32  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Default Value: NIRFSA_VAL_ENABLED \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841 \n\n ',
            'note': ' The NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is only '
        },
        'enum': 'EnabledAttr',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'type': 'ViInt32'
    },
    1150188: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL). \n\n The LO frequency can only be tuned by multiples of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE  attribute. The LO frequency can therefore be offset from the requested  center frequency by as much as half of the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE  attribute. This offset is corrected by digitally frequency shifting the  NIRFSA_ATTR_LO_FREQUENCY attribute to the value requested in either the  NIRFSA_ATTR_IQ_CARRIER_FREQUENCY attribute or the NIRFSA_ATTR_SPECTRUM_CENTER_FREQUENCY attribute. \n\n When the NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is set to  NIRFSA_VAL_ENABLED, the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute can  accept any value from 50 kHz to 24 MHz. \n\n When the NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is set to  NIRFSA_VAL_DISABLED, the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute is  coerced to 4 MHz, 5 MHz, 6 MHz, 12 MHz or 24 MHz. \n\n Refer to the Instrument Configurations topic for more information about available ports for your hardware configuration. \n\n Default Values: \n\n PXIe-5644/5645/5646: 200 kHz \n PXIe-5830: 2 MHz \n PXIe-5831 (RF port): 8 MHz \n PXIe-5831 (IF port): 2 MHz, 4 MHz \n PXIe-5840/5841 (fractional mode): 500 kHz \n PXIe-5840/5841 (integer mode): 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.\n PXIe-5841 with PXIe-5655: 500 kHz \n Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841 ',
            'note': ' The default value for the PXIe-5831 depends on the frequency range of the selected port for your instrument configuration. '
        },
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150189: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the Reference Trigger is delayed with the data. Set this  attribute to NIRFSA_VAL_DISABLED when the NIRFSA_ATTR_REF_TRIGGER_TYPE  attribute is set to NIRFSA_VAL_IQ_POWER_EDGE or NIRFSA_VAL_IQ_ANALOG_EDGE. \n\n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your  device in the NI RF Vector Signal Analyzers Help for more information about  device synchronization for vector signal transceivers.\n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5644/5645 \n\n '
        },
        'enum': 'EnabledAttr',
        'name': 'SYNC_REF_TRIGGER_DELAY_ENABLED',
        'type': 'ViInt32'
    },
    1150191: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the sub-sample delay, in seconds, to apply to the  acquired signal. To set this property, the NI-RFSA device  must be in the Configuration state. \n\n Valid Values: -4.16 ns to +4.16 ns \n\n Default Value: 0 \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'DECIMATION_DELAY',
        'type': 'ViReal64'
    },
    1150192: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the channel from which the device monitors the trigger.  Use a value of I to monitor the I channel. Use a value of Q to monitor  the Q channel. Use a value of IQ to monitor both I and Q channels.  This attribute affects the device operation only when the  NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE. \n\n Valid Values: I, Q, IQ, QI \n\n Default Value: I \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150193: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device asserts the trigger when the voltage level is  rising or falling. When you set the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute  to NIRFSA_VAL_IQ_ANALOG_EDGE, the device asserts the trigger when the signal  level exceeds the specified level with the slope you specify. This attribute  affects the device operation only when the NIRFSA_ATTR_REF_TRIGGER_TYPE  attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE. \n\n Default Value: NIRFSA_VAL_RISING_SLOPE \n\n Supported Devices: PXIe-5644/5645 '
        },
        'enum': 'AnalogSlope',
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE',
        'type': 'ViInt32'
    },
    1150194: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the analog level, in volts, at which the device triggers.  The device asserts the trigger when the signal exceeds the level  specified by the value of this property, taking into consideration  the specified slope. This attribute affects the device operation only  when the NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE. \n\n Default Value: 0 V \n\n Supported Devices: PXIe-5644/5645 '
        },
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL',
        'type': 'ViReal64'
    },
    1150195: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the size of the hysteresis window on either side of the trigger  level. The device triggers when the signal passes through the threshold  you specify with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_LEVEL attribute,  has the slope you specify with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE  attribute, and passes through the hysteresis window that you specify with this  attribute. This attribute affects the device operation only when the  NIRFSA_ATTR_REF_TRIGGER_TYPE attribute is set to NIRFSA_VAL_IQ_ANALOG_EDGE. \n\n Valid Values: 0 to (Voltage Range/2 + Trigger Level) for Rising Slope.  0 to (Voltage Range/2 – Trigger Level) for Falling Slope. These values limit  the hysteresis to the entire voltage range that is below the trigger level for  Rising Slope or that is above the trigger level for Falling Slope.\n\n Default Value: The default is calculated by the driver as (Range x 0.025). \n\n Supported Devices: PXIe-5644/5645 \n\n '
        },
        'name': 'IQ_ANALOG_EDGE_REF_TRIGGER_HYSTERESIS',
        'type': 'ViReal64'
    },
    1150196: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the digitizer OSP block delays Reference triggers, along with the data  samples, moving through the OSP block or if the Reference triggers bypass the OSP block  and are processed immediately.\n\n Enabling this attribute requires the following equipment configurations:\n All digitizers being used must be the same model and hardware revision.\n All digitizers must use the same firmware.\n All digitizers must be configured with the same I/Q rate. \n All devices must use the same signal path. \n\n PXI-5661—The IF filters for the PXI-5661are determined by the incoming frequency.\n\n PXIe-5663/5663E—Read the value of the NIRFSA_ATTR_IF_FILTER attribute to determine the  IF filters used by the PXIe-5663/5663E.\n\n PXIe-5665/5667/5668—Refer to the device-specific information in the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute to determine the IF filters used by  the PXIe-5665/5667/5668. If you set the NIRFSA_ATTR_FFT_WIDTH attribute, refer to the device-specific  information for this attribute and the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute  to determine the IF filters used. For frequencies less than 3.6 GHz, set the  NIRFSA_ATTR_RF_PREAMP_ENABLED to the same value for all devices.\n\n PXIe-5665 14 GHz—Set the NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED to the same value for all devices.\n\n If the I/Q rate is set programmatically for I/Q acquisitions, the following attributes  should be identical for the best device synchronization:\n\n NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED \n NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO \n\n For spectrum acquisitions, the following attributes should be identical for the  best device synchronization:\n\n NIRFSA_ATTR_SPECTRUM_SPAN \n NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE \n NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED\n NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO \n\n For more information about the digitizer OSP block and reference triggers,  refer to the following topics in the NI High-Speed Digitizers Help:\n\n NI-5622 Onboard Signal Processing (OSP) \n NI-5142 Onboard Signal Processing (OSP) \n NI PXIe-5622 Trigger Sources \n NI PXI 5142 Trigger Sources \n NI PXIe-5622 Block Diagram \n NI PXI-5142 Trigger Sources \n Default Value: NIRFSA_VAL_ENABLED \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'EnabledAttr',
        'name': 'REF_TRIGGER_OSP_DELAY_ENABLED',
        'type': 'ViInt32'
    },
    1150203: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies an offset from the I/Q carrier frequency for the downconverter.  If you set this attribute, any measurements outside the instantaneous bandwidth  of the device are invalid. After you set this attribute, the RF downconverter is  locked to that frequency offset until the value is changed or the attribute is reset. \n\n Valid Values: \n\n PXIe-5646: -100 MHz to +100 MHz PXIe-5830/5831/5840/5841: -625 MHz to +625 MHz \n\n All other devices:  -42 MHz to +42 MHz \n\n Default Values: For spectrum acquisition types the driver automatically calculates  the default to avoid residual LO power. For I/Q acquisition types the default is 0 Hz.  If the center frequency is set to a non-multiple of the  NIRFSA_ATTR_SIGNAL_PATH_LO_FREQUENCY_STEP_SIZE attribute, the  NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET attribute is set to compensate for the difference.\n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841 '
        },
        'name': 'DOWNCONVERTER_FREQUENCY_OFFSET',
        'type': 'ViReal64'
    },
    1150204: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the temperature of the I/Q IN circuitry on the device. \n\n Units: degrees C \n\n Supported Devices: PXIe-5645, PXIe-5820 '
        },
        'name': 'IQ_IN_PORT_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150205: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the IF filter path bandwidth for your device configuration. \n\n bandwidth includes all IF filters across the component modules of a composite device. \n\n Default Values: For spectrum acquisition types the default is greater than or  equal to the NIRFSA_ATTR_SPECTRUM_SPAN attribute. NI-RFSA chooses the default  value of the NIRFSA_ATTR_IF_FILTER_BANDWIDTH attribute to correspond to the  appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default  value corresponding to the widest IF filter possible for your equipment setup.\n\n Supported Devices: PXIe-5601/5603/5605/5606, PXIe-5663/5663E/5665/5667/5668, PXIe-5694     ',
            'note': ' For composite devices, such as the PXIe-5663/5663E/5665/5667, the IF filter path '
        },
        'name': 'IF_FILTER_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the shape factor of the window used in the fast Fourier transform (FFT).  The Window Shape Factor is defined as ratio of the 60 dB to 6 dB bandwidths. \n\n Default Value: N/A \n\n Supported Devices: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FFT_WINDOW_SHAPE_FACTOR',
        'type': 'ViReal64'
    },
    1150207: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to use the low-frequency bypass path for the incoming RF signal. \n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5693, PXIe-5667     '
        },
        'enum': 'EnabledAttr',
        'name': 'LOW_FREQUENCY_BYPASS_ENABLED',
        'type': 'ViInt32'
    },
    1150208: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the location in a signal path where an RF conditioning calibration  tone is injected or whether the tone is disabled. \n\n Default Value: NIRFSA_VAL_CAL_TONE_DISABLED  \n\n Supported Devices: PXIe-5667, PXIe-5668, PXIe-5693/5698      '
        },
        'enum': 'ConditioningCalToneMode',
        'name': 'RF_CONDITIONING_CAL_TONE_MODE',
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the RF conditioning calibration tone, in hertz (Hz). \n\n  Valid Values: 34.5 MHz to 7.5 GHz \n\n Default Value: 612.5 MHz \n\n Supported Devices: PXIe-5667, PXIe-5668, PXIe-5693/5698      '
        },
        'name': 'RF_CONDITIONING_CAL_TONE_FREQUENCY',
        'type': 'ViReal64'
    },
    1150210: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the IF conditioning module. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5667     '
        },
        'name': 'IF_CONDITIONING_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the RF conditioning module. \n\n Default Value: N/A \n\n Supported Devices: PXIe-5667     '
        },
        'name': 'RF_CONDITIONING_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150215: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifics the RF lowband signal conditioning path used during calibration. This attribute is  valid only during a calibration session. \n\n Default Value: NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1  \n\n Supported Devices: PXIe-5606     '
        },
        'enum': 'RfLBSigCondPathSel',
        'name': 'CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_SELECTION',
        'type': 'ViInt32'
    },
    1150216: {
        'access': 'read-write',
        'documentation': {
            'description': ' Reads the IF attenuation table size based on valid path settings. This attribute is valid only during a calibration session. \n\n Valid Values: N/A \n\n Default Value: N/A \n\n Supported Devices: PXIe-5606     '
        },
        'name': 'CAL_IF_ATTENUATION_TABLE_SIZE',
        'type': 'ViInt32'
    },
    1150217: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master for synchronizing the sample clock between multiple devices.\n \n The master device distributes the sync signal to all devices in the system through the Sync Sample Clock distribution line. \n \n When synchronizing the Sample Clock, one device must always be designated as the master. When the device is configured as a master, it actively drives the Sync Sample Clock distribution line.\n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the NI RF Vector Signal Analyzers Help for more information about device synchronization for vector signal transceivers.\n'
        },
        'name': 'SYNC_SAMPLE_CLOCK_MASTER',
        'type': 'ViBoolean'
    },
    1150218: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the Sample Clock Sync signal. When synchronizing the Sample Clock, configure all devices to use the same Sync Sample Clock distribution line.\n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the NI RF Vector Signal Analyzers Help for more information about device synchronization for vector signal transceivers.\n'
        },
        'name': 'SYNC_SAMPLE_CLOCK_DIST_LINE',
        'type': 'ViString'
    },
    1150219: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during  spectrum acquisition. \n\n Default Value: Disabled \n\n Supported Devices: PXIe-5665/5668     '
        },
        'name': 'SMOOTH_SPECTRUM_ENABLED',
        'type': 'ViInt32'
    },
    1150220: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum corner frequency of the highpass filter in the RF signal path.  The device uses the highest frequency highpass filter option below or equal to the value you  specify and returns a coerced value. Specifying a value of 0 disables highpass filtering. \n\n Valid Values: 0 to 26.5 \n\n Default Value: 0 \n\n Supported Devices: PXIe-5606, PXIe-5668     '
        },
        'name': 'RF_HIGH_PASS_FILTERING',
        'type': 'ViReal64'
    },
    1150221: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string containing the path to the location of the current FPGA Extensions bitfile, a .lvbitx file, that is programmed on the device. \n \n An FPGA Extensions bitfile controls the behavior of the FPGA. You can use a custom bitfile with the NI-RFSA instrument driver to override the default FPGA bitfile and change the default behavior of the FPGA. Before reading this property, you must specify the bitfile location using the Driver Setup keyword in the options string parameter of the niRFSA_InitWithOptions function. \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150222: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables the 28 V DC source on the device front panel. \n\n PXIe-5668 with PXIe-5698—When this attribute is set to NIRFSA_VAL_ENABLED, the PXIe-5698 noise source is used instead of the PXIe-5668 noise source. \n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5606, PXIe-5668, PXIe-5698     '
        },
        'name': 'NOISE_SOURCE_POWER_ENABLED',
        'type': 'ViInt32'
    },
    1150223: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the 100 MHz IF filter path  with the value you set for this attribute.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5606      '
        },
        'name': 'CALIBRATION_CORRECTION_100_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150224: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the 320 MHz IF filter path  with the value you set for this attribute.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5606      '
        },
        'name': 'CALIBRATION_CORRECTION_320_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150225: {
        'access': 'read-write',
        'documentation': {
            'description': ' Overrides the internal gain self-calibration correction for the 765 MHz IF filter path  with the value you set for this attribute.\n\n Default Value: 0 \n\n Supported Devices: PXIe-5606      '
        },
        'name': 'CALIBRATION_CORRECTION_765_MHZ_FILTER',
        'type': 'ViReal64'
    },
    1150226: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the currently associated digitizer ID.\n Allows the use of self calibration data when configured in external digitizer mode.\n\n Default Value:  (empty string) in external digitizer mode\n\n Supported Devices: PXIe-5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668     '
        },
        'name': 'CAL_DIGITIZER_ID',
        'type': 'ViString'
    },
    1150228: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency, in hertz (Hz), of the digitizer sample clock. \n\n Units: hertz (Hz) \n\n Supported Devices: PXIe-5668     '
        },
        'name': 'DIGITIZER_SAMPLE_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150229: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the terminal at which to export the Digitizer Sample Clock. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5668    '
        },
        'enum': 'DigitizerSampleClockOutTerminal',
        'name': 'EXPORTED_DIGITIZER_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150233: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string containing the name of the FPGA target being used. \n\n Supported Devices: PXIe-5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'FPGA_TARGET_NAME',
        'type': 'ViString'
    },
    1150234: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the amount of overlap between consecutive subspans in a multispan spectrum acquisition. Overlapping  subspans can reduce the power level of spurs in acquired data. The value you specify determines the amount of  shift as a percentage of the subspan width. \n\n Valid Values:\n 0 (inclusive) to 100 (exclusive)\n Default Values: \n\n PXIe-5820/5830/5831/5840/5841: 0 \n\n PXIe-5665/5668: 0 to <100 \n\n Supported Devices: PXIe-5665/5668, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SUBSPAN_OVERLAP',
        'type': 'ViReal64'
    },
    1150235: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to enable the LO2 OUT terminal on the installed devices. \n\n Set this attribute to NIRFSA_VAL_ENABLED to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal. \n\n You can also export the LO2 signal by setting the NIRFSA_ATTR_LO_EXPORT_ENABLED attribute  and the NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE attribute. \n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668     '
        },
        'enum': 'EnabledAttr',
        'name': 'LO2_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150236: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the maximum instantaneous bandwidth of the device.\n\n Units: Hz \n\n Supported Devices: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5840/5841 '
        },
        'name': 'MAX_DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150237: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the max I/Q rate of the device.\n\n Units: S/s \n\n Supported Devices: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5840/5841'
        },
        'name': 'MAX_IQ_RATE',
        'type': 'ViReal64'
    },
    1150246: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the power level, in dBm, of the signal at the LO OUT terminal  when the NIRFSA_ATTR_LO_EXPORT_ENABLED attribute is set to VI_TRUE. \n\n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter of the niRFSA_SetAttributeViReal64  function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1  or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices,  the only valid value for the channel string is  (empty string). \n\n Units: dBm \n\n Supported Devices: PXIe-5830/5831/5840/5841 '
        },
        'name': 'LO_OUT_POWER',
        'type': 'ViReal64'
    },
    1150254: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current temperature, in degrees Celsius, of the FPGA. \n\n Defualt Value: N/A \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     ',
            'note': ' If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n'
        },
        'name': 'FPGA_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150255: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the module power consumption. \n\n Units: Watts \n\n Default Value: N/A \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841 ',
            'note': ' If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n\n'
        },
        'name': 'MODULE_POWER_CONSUMPTION',
        'type': 'ViReal64'
    },
    1150256: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device  specifications. When you set this attribute to NIRFSA_VAL_ENABLED, the driver does not report out-of-specification warnings and errors. \n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'EnabledAttr',
        'name': 'ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS',
        'type': 'ViInt32'
    },
    1150266: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the sub-sample clock delay, in seconds, to apply to the acquired signal.  Use this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk.  This attribute can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurment to the current session. \n\n To set this attribute, your device must be in the Configuration state. \n\n Valid Values: Plus or minus half of one sample clock period \n\n Default Value: 0 \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841 ',
            'note': ' If this value is set, TClk cannot do any sub-sample clock adjustment. \n\n'
        },
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64'
    },
    1150267: {
        'access': 'read-write',
        'documentation': {
            'description': " Specifies the bandwidth of the input signal around the NIRFSA_ATTR_IQ_CARRIER_FREQUENCY. \n\n This value must be less than or equal to (0.8 x I/Q rate). NI-RFSA defines signal bandwidth as twice the maximum I/Q signal deviation from 0 Hz.  Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth  is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or fmax - fmin. \n\n If you do not set this attribute, NI-RFSA uses the maximum available signal bandwidth. Depending on your  device settings, setting this attribute enables certain optimizations. Based on the specified signal  bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain. \n\n Ensure you set the signal bandwidth wide enough to encompass all significant anticipated input power.  In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside  the signal bandwidth can lead to clipping and associated overflow warnings if you do not have enough margin in your reference level. \n\n Units: hertz (Hz) \n\n Default Value: 0 Hz \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     ",
            'note': ' You must set this attribute to enable the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE attribute. \n\n'
        },
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150269: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the common-mode level presented at each differential input terminal. Common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). \n\n Units: volts \n\n Default Value: 0 V \n\n Supported Devices: PXIe-5820 \n\n '
        },
        'name': 'COMMON_MODE',
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures error reporting for ADC and onboard signal processing overflows. Overflows lead to clipping of the waveform. \n\n Default Value: NIRFSA_VAL_ERROR_REPORTING_WARNING \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'OverflowErrorReporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'ViInt32'
    },
    1150285: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the size of the DMA buffer in computer memory, in bytes. To  set this attribute, the NI-RFSA device must be in the Configuration state. \n\n large fetches to be transferred more efficiently.\n\n Default Value: 8 MB \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     ',
            'note': ' A sufficiently large host DMA buffer improves performance by allowing '
        },
        'name': 'HOST_DMA_BUFFER_SIZE',
        'type': 'ViInt64'
    },
    1150297: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the port to configure. \n\n Valid Values: \n\n PXIe-5644/5645/5646, PXIe-5820/5840/5841:  (empty string) \n PXIe-5830: if0, if1 PXIe-5831: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel. \n\n Default Value: \n\n PXIe-5830/5831: if1 \n PXIe-5644/5645/5646, PXIe-5820/5840/5841:  (empty string) \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'SELECTED_PORTS',
        'type': 'ViReal64'
    },
    1150298: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840/5841.  This attribute cannot be set to NIRFSA_VAL_ENABLED or NIRFSA_VAL_DISABLED unless an NI-RFSG session on the  PXIe-5840 has set the NIRFSG_ATTR_LO_EXPORT_CONFIGURE_FROM_RFSA attribute to NIRFSG_VAL_ENABLE.\n\n When this attribute is enabled, if the NIRFSA_ATTR_LO_SOURCE attribute is set to NIRFSA_VAL_LO_IN_STR and you  do not set the NIRFSA_ATTR_LO_FREQUENCY or NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attributes, NI-RFSA rounds the  LO frequency to approximately an LO step size as if the source was NIRFSA_VAL_ONBOARD_STR. This ensures that when you  configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible. \n\n Default Value: NIRFSA_VAL_UNSPECIFIED \n\n Supported Devices: PXIe-5840/5841     '
        },
        'enum': 'UnspecifiedAttr',
        'name': 'RF_OUT_LO_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150299: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.  Set this attribute to NIRFSA_VAL_ENABLED to allow NI-RFSG to control the LO out export.  Use the NIRFSG_ATTR_RF_IN_LO_EXPORT_ENABLED attribute to control the NI-RFSA LO out export from NI-RFSG. \n\n Default Value: NIRFSA_VAL_DISABLED \n\n Supported Devices: PXIe-5840/5841     '
        },
        'enum': 'EnabledAttr',
        'name': 'LO_OUT_EXPORT_CONFIGURE_FROM_RFSG',
        'type': 'ViInt32'
    },
    1150300: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the temperature change, in degrees Celsius, required before NI-RFSA recalculates the thermal correction settings when entering the Running state. \n\n Units: degrees Celsius \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841 Default Values: PXIe-5830/5831: 0.2 PXIe-5840/5841: 1.0    '
        },
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'ViReal64'
    },
    1150301: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the scaling factor applied to the time-domain voltage data in the digitizer. NI-RFSA does not compensate for the specified digital gain.  You can use this attribute to account for external gain changes without changing the analog signal path.  Units: dB \n\n Default Value: 0 dB \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841    ',
            'note': ' The PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices. \n\n'
        },
        'name': 'DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150305: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to allow NI-RFSA to select the downconveter frequency offset. You can either set an offset yourself or let NI-RFSA select one for you. \n\n Placing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage. \n To set an offset yourself, set this attribute to NIRFSA_VAL_AUTOMATIC or NIRFSA_VAL_USER_DEFINED,  and set either the  NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY or the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET attributes. \n To allow NI-RFSA to automatically select the downconverter frequency offset, set this attribute to NIRFSA_VAL_AUTOMATIC  or NIRFSA_VAL_ENABLED and configure the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute to describe your expected input signal. \n The signal bandwidth must be no greater than half the specified value of the NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute,  minus a device-specific guard band. Do not set the NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY or NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET  attributes. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. \n Set this attribute to NIRFSA_VAL_ENABLED if you want to receive an error any time NI-RFSA is unable to apply automatic offset. \n\n When you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency,  and NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSA_VAL_USER_DEFINED. When NI-RFSA automatically sets an offset,  the reference frequency for gain is the I/Q carrier frequency, and NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSA_VAL_ENABLED.  Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies. \n\n Default Value: NIRFSA_VAL_AUTOMATIC \n\n Supported Devices: PXIe-5830/5831/5841     '
        },
        'enum': 'DownconverterFrequencyOffsetMode',
        'name': 'DOWNCONVERTER_FREQUENCY_OFFSET_MODE',
        'type': 'ViInt32'
    },
    1150306: {
        'access': 'read-write',
        'documentation': {
            'description': ' Returns a comma-separated list of the available ports to use based on your hardware configuration. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5840/5841, PXIe-5830/5831     '
        },
        'name': 'AVAILABLE_PORTS',
        'type': 'ViReal64'
    },
    1150307: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the type of de-embedding to apply to measurements on the specified port. To use this attribute, you must use the channelName parameter of the niRFSA_SetAttributeViInt32 function to specify the name of the port to configure for de-embedding. \n\n If you set this attribute to NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT. \n\n Default Value: NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR \n\n Valid Values for PXIe-5830/5832/5840/5841: NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR, NIRFSA_VAL_DEEMBEDDING_TYPE_NONE \n\n Valid Values for PXIe-5831: NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR, NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR, or NIRFSA_VAL_DEEMBEDDING_TYPE_NONE. NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).\n\n Supported Devices: PXIe-5830/5831/5832/5840/5841     '
        },
        'enum': 'DeembeddingType',
        'name': 'DEEMBEDDING_TYPE',
        'type': 'ViInt32'
    },
    1150308: {
        'access': 'read-write',
        'documentation': {
            'description': ' Selects the de-embedding table to apply to the measurements on the specified port. To use this attribute, you must use the channelName parameter of the niRFSA_SetAttributeViString function to specify the name of the port to configure for de-embedding. \n\n If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT. \n\n Use the niRFSA_CreateDeembeddingSparameterTableArray function to create tables. \n\n Supported Devices: PXIe-5830/5831/5840/5841     '
        },
        'name': 'DEEMBEDDING_SELECTED_TABLE',
        'type': 'ViString'
    },
    1150309: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the margin NI-RFSA adds to the NIRFSA_ATTR_REFERENCE_LEVEL attribute.  The margin helps to avoid clipping and overflow warnings if the input signal  exceeds the configured reference level. \n\n NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as  the instantaneous power of the input signal remains within the reference level plus the reference level headroom.  If you know the input power of the signal precisely or have already included margin in the  reference level, you may be able to improve the signal-to-noise ratio by reducing  the reference level headroom. \n\n Units: dB \n\n Default Value: \n\n PXIe-5830/5831/5841: 1 dB \n PXIe-5840: 0 dB \n\n Supported Devices: PXIe-5830/5831/5840/5841     '
        },
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'ViReal64'
    },
    1150312: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step size for tuning the internal VCO used to generate the LO. \n\n Valid Values: 1 Hz to 50 MHz for LO1 and 1 Hz to 100 MHz for LO2 \n\n Default Value: 1 MHz \n\n Supported Devices: PXIe-5830/5831 ',
            'note': ' Do not set this attribute with the NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE attribute. \n\n'
        },
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150316: {
        'access': 'read-write',
        'documentation': {
            'description': " Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the NIRFSA_ATTR_DEVICE_TEMPERATURE attribute. \n\n' For example, if this attribute is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then you can  expect to run the device from 30 degrees Celsius to 40 degrees Celsius with corrected accuracy and no overflows.  Setting this attribute with a smaller value can result in improved dynamic range, but you must ensure thermal stability  while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows. \n\n Units: degrees Celsius \n\n Supported Devices: PXIe-5840/5830/5831 Default Value: \n\n PXIe-5830/5831: 5 \n PXIe-5840/5841: 10 \n\n Supported Devices: PXIe-5830/5831/5840/5841    "
        },
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'ViReal64'
    },
    1150321: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse width units for the User Source. When the value is NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS, it is assumed that the clock rate of the signal  is the data clock. Use NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS if the user source clock rate is anything else \n\n. Valid Values: NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS, NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS \n\n Default Value: NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     '
        },
        'enum': 'PulseWidthUnitType',
        'name': 'USER_SOURCE_PULSE_WIDTH_UNITS',
        'type': 'ViInt32'
    },
    1150322: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse width for the User Source. Use the NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS attribute to set the units for the pulse width. \n\n Default Value: 200E(-9) \n\n Supported Devices: PXIe-5820/5830/5831/5840/5841     '
        },
        'name': 'USER_SOURCE_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150324: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies a comma-separated list of ports for which to fix the group delay. \n\n Valid Values: \n\n PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel. \n\n Default Value:  \n\n PXIe-5831/5832:  (empty string) \n\n Supported Devices: PXIe-5831/5832     '
        },
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'ViString'
    },
    1150325: {
        'access': 'read-write',
        'name': 'DEEMBEDDING_COMPENSATION_GAIN',
        'type': 'ViReal64'
    },
    1150326: {
        'access': 'read-write',
        'name': 'EXPORTED_REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150331: {
        'access': 'read-write',
        'name': 'SELECTED_PATH',
        'type': 'ViString'
    },
    1150332: {
        'access': 'read only',
        'name': 'AVAILABLE_PATHS',
        'type': 'ViString'
    },
    1150333: {
        'access': 'read-write',
        'name': 'CREATED_SESSION_CHANNEL',
        'type': 'ViInt32'
    },
    1150334: {
        'access': 'read only',
        'name': 'MIN_FUNDAMENTAL_SILO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150335: {
        'access': 'read only',
        'name': 'MAX_FUNDAMENTAL_SILO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150337: {
        'access': 'read-write',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS',
        'type': 'ViInt32'
    },
    1150356: {
        'access': 'read only',
        'name': 'ASSOC_AUX_SWITCH_GAIN_UID',
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/attributes_addon.py sha256=c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845 bytes=39 -->
## FILE: source/codegen/metadata/nirfsa/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/attributes_addon.py`
- sha256: `c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845`
- bytes: 39

````python
attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/config.py sha256=4dda27839451030df1dd9c7f74753de9958c518eba63abce3d000354006186b3 bytes=4701 -->
## FILE: source/codegen/metadata/nirfsa/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/config.py`
- sha256: `4dda27839451030df1dd9c7f74753de9958c518eba63abce3d000354006186b3`
- bytes: 4701

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '21.0.0',
    'c_header': 'niRFSA.h',
    'c_function_prefix': 'niRFSA_',
    'service_class_prefix': 'NiRFSA',
    'java_package': 'com.ni.grpc.rfsa',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFSA',
    'namespace_component': 'nirfsa',
    'close_function': 'Close',
    'custom_types': [
        {
            'name': 'niRFSA_wfmInfo_struct',
            'grpc_name': 'WaveformInfo',
            'fields': [
                {
                    'type': 'ViReal64',
                    'name': 'absoluteInitialX'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'relativeInitialX'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'xIncrement'
                },
                {
                    'type': 'ViInt64', 
                    'name': 'actualSamples'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'offset'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'gain'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved1',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved2',
                    'include_in_proto': False,
                },
            ]
        },
        {
            'name': 'niRFSA_coefficientInfo_struct',
            'grpc_name': 'CoefficientInfo',
            'fields': [
                {
                    'type': 'ViReal64', 
                    'name': 'offset'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'gain'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved1',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved2',
                    'include_in_proto': False,
                },
            ]
        },
        {
            'name': 'niRFSA_spectrumInfo_struct',
            'grpc_name': 'SpectrumInfo',
            'fields': [
                {
                    'type': 'ViReal64', 
                    'name': 'initialFrequency'
                },
                {
                    'type': 'ViReal64', 
                    'name': 'frequencyIncrement'
                },
                {
                    'type': 'ViInt32', 
                    'name': 'numberOfSpectralLines'
                },
                
                {
                    'type': 'ViReal64', 
                    'name': 'reserved1',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved2',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved3',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved4',
                    'include_in_proto': False,
                },
                {
                    'type': 'ViReal64', 
                    'name': 'reserved5',
                    'include_in_proto': False,
                },
            ]
        }
    ],
    'additional_headers': { 'custom/nirfsa_aliases.h': ['service.cpp', 'library_interface.h'], 'custom/ivi_errors.h': ['service.cpp'] },
    'driver_name': 'NI-RFSA',
    'init_function': 'InitWithOptions',
    'status_ok': 'status >= 0',
    'code_readiness': 'Release',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsa',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSA_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSA_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '1.0',
    'module_name': 'nirfsa',
    'session_class_description': 'An NI-RFSA session.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/config_addon.py sha256=a0296c82de9bd48f588b7ddb8a91dbb13d7117e8606a1a575c12d93dee890aa1 bytes=33 -->
## FILE: source/codegen/metadata/nirfsa/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/config_addon.py`
- sha256: `a0296c82de9bd48f588b7ddb8a91dbb13d7117e8606a1a575c12d93dee890aa1`
- bytes: 33

````python
config_additional_config = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/enums.py sha256=0e0657a78c2d26f8e8e0d96457b006edb2aa5be914473c6ce1b321aea7b5e3dc bytes=79769 -->
## FILE: source/codegen/metadata/nirfsa/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/enums.py`
- sha256: `0e0657a78c2d26f8e8e0d96457b006edb2aa5be914473c6ce1b321aea7b5e3dc`
- bytes: 79769

````python
enums = {
    'AcquisitionType': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures NI-RFSA for I/Q acquisitions.'
                },
                'name': 'IQ',
                'value': 100
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSA for spectrum acquisitions.'
                },
                'name': 'SPECTRUM',
                'value': 101
            }
        ]
    },
    'AnalogSlope': {
        'values': [
            {
                'documentation': {
                    'description': ' The trigger asserts when the signal power is rising.'
                },
                'name': 'RISING_SLOPE',
                'value': 1000
            },
            {
                'documentation': {
                    'description': ' The trigger asserts when the signal power is falling.'
                },
                'name': 'FALLING_SLOPE',
                'value': 1001
            }
        ]
    },
    'AveragingMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures NI-RFSA to perform no averaging on acquisitions.'
                },
                'name': 'NO_AVERAGING',
                'value': 400
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSA for root-mean-square (RMS) averaging. RMS averaging reduces signal  fluctuations but not the  noise floor. RMS averaging averages the energy, or power, of the signal. This  averaging prevents noise floor reduction and gives averaged RMS quantities of  single-channel measurements zero phase. RMS averaging for dual-channel  measurements preserves important phase information.'
                },
                'name': 'RMS_AVERAGING',
                'value': 401
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSA for vector averaging. Vector averaging reduces noise  from synchronous signals. Vector averaging computes the average of complex  quantities directly, which means that it allows separate averaging for real  and imaginary parts. Complex averaging such as vector averaging reduces  noise and usually requires a trigger to improve block-to-block phase coherence.'
                },
                'name': 'VECTOR_AVERAGING',
                'value': 402
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSA for peak-hold averaging. Peak-hold averaging retains the  RMS peak levels of the averaged quantities. The peak-hold averaging process  performs peak-hold at each frequency bin separately to retain peak RMS levels  from one FFT record to the next.'
                },
                'name': 'PEAK_HOLD_AVERAGING',
                'value': 403
            },
            {
                'documentation': {
                    'description': ' Min Hold averaging'
                },
                'name': 'MIN_HOLD_AVERAGING',
                'value': 404
            },
            {
                'documentation': {
                    'description': ' Scalar averaging'
                },
                'name': 'SCALAR_AVERAGING',
                'value': 405
            },
            {
                'documentation': {
                    'description': ' Log averaging'
                },
                'name': 'LOG_AVERAGING',
                'value': 406
            }
        ]
    },
    'BandwidthType': {
        'values': [
            {
                'documentation': {
                    'description': ' Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the  window specified by the NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'RBW_3_DB',
                'value': 300
            },
            {
                'documentation': {
                    'description': ' Defines the RBW in terms of the 6 dB bandwidth of the window specified by the  NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'RBW_6_DB',
                'value': 301
            },
            {
                'documentation': {
                    'description': ' Defines the RBW in terms of the display resolution, which is the ratio of the  sampling frequency to the number of samples that you acquire.'
                },
                'name': 'RBW_BIN_WIDTH',
                'value': 302
            },
            {
                'documentation': {
                    'description': ' Defines the RBW in terms of the equivalent noise bandwidth  (ENBW) of the window specified by the NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'RBW_ENBW',
                'value': 303
            }
        ]
    },
    'CalIFAttenTableSelection': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the standard IF attenuation table is used for the external calibration.'
                },
                'name': 'EXT_CAL_IF_ATTENUATION_TABLE_STANDARD',
                'value': 2900
            },
            {
                'documentation': {
                    'description': ' Specifies that the adjacent channel power ratio (ACPR) IF attenuation table is used for the  external calibration. You can only select this value if you set the  NIRFSA_ATTR_CAL_IF_FILTER_SELECTION attribute to NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_1  or NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_2. '
                },
                'name': 'EXT_CAL_IF_ATTENUATION_TABLE_ACPR',
                'value': 2901
            }
        ]
    },
    'CalIFFilterSelection': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the 5 MHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_1',
                'value': 2100
            },
            {
                'documentation': {
                    'description': ' Specifies that the through filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_2',
                'value': 2101
            },
            {
                'documentation': {
                    'description': ' Specifies that the 300 kHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_3',
                'value': 2102
            },
            {
                'documentation': {
                    'description': ' Specifies that the 20 MHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_4',
                'value': 2103
            },
            {
                'documentation': {
                    'description': ' Specifies that the 1.4 MHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_5',
                'value': 2104
            },
            {
                'documentation': {
                    'description': ' Specifies that the 425 kHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_6',
                'value': 2105
            },
            {
                'documentation': {
                    'description': ' Specifies that the 110 kHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_7',
                'value': 2106
            },
            {
                'documentation': {
                    'description': ' Specifies that the 30 kHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_8',
                'value': 2107
            },
            {
                'documentation': {
                    'description': ' Specifies that the 100 MHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_9',
                'value': 2108
            },
            {
                'documentation': {
                    'description': ' Specifies that the 320 MHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_10',
                'value': 2109
            },
            {
                'documentation': {
                    'description': ' Specifies that the 1 GHz filter path is used during calibration.'
                },
                'name': 'EXT_CAL_IF_FILTER_PATH_11',
                'value': 2110
            }
        ]
    },
    'CalToneMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables the calibration tone for the associated path.'
                },
                'name': 'DISABLED',
                'value': 2700
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the low band RF path.'
                },
                'name': 'LOWBAND_RF',
                'value': 2701
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the high band RF path.'
                },
                'name': 'HIGHBAND_RF',
                'value': 2702
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the high band IF path.'
                },
                'name': 'HIGHBAND_IF',
                'value': 2703
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the low band RF path (bypass the ALC).'
                },
                'name': 'LOWBAND_RF_WITHOUT_ALC',
                'value': 2704
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the high band RF path (through the Comb Generator).'
                },
                'name': 'COMB_GENERATOR',
                'value': 2705
            }
        ]
    },
    'ChannelCoupling': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the RF input channel is AC-coupled. For low frequencies  (less than 10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration.'
                },
                'name': 'AC',
                'value': 3001
            },
            {
                'documentation': {
                    'description': ' Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum  RF attenuation for device protection.'
                },
                'name': 'DC',
                'value': 3002
            }
        ]
    },
    'ConditioningCalToneMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables the calibration tone for the associated path.'
                },
                'name': 'DISABLED',
                'value': 2700
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the low band RF path.'
                },
                'name': 'LOWBAND_RF',
                'value': 2701
            },
            {
                'documentation': {
                    'description': ' Injects the calibration tone into the high band RF path.'
                },
                'name': 'HIGHBAND_RF',
                'value': 2702
            }
        ]
    },
    'DeembeddingType': {
        'values': [
            {
                'documentation': {
                    'description': ' De-embedding is not applied to the measurement.'
                },
                'name': 'NONE',
                'value': 3900
            },
            {
                'documentation': {
                    'description': ' De-embeds the measurement using only the gain term.'
                },
                'name': 'SCALAR',
                'value': 3901
            },
            {
                'documentation': {
                    'description': ' De-embeds the measurement using the gain term and the reflection term.'
                },
                'name': 'VECTOR',
                'value': 3902
            }
        ]
    },
    'DeviceResponse': {
        'values': [
            {
                'name': 'DOWNCONVERTER_IF_RESPONSE',
                'value': 2800
            },
            {
                'name': 'DOWNCONVERTER_RF_RESPONSE',
                'value': 2801
            },
            {
                'name': 'DOWNCONVERTER_COMBINED_RESPONSE',
                'value': 2802
            },
            {
                'name': 'VSA_IF_RESPONSE',
                'value': 2803
            },
            {
                'name': 'VSA_COMBINED_RESPONSE',
                'value': 2804
            }
        ]
    },
    'DigitalEdge': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSA detects a rising edge.'
                },
                'name': 'RISING_EDGE',
                'value': 900
            },
            {
                'documentation': {
                    'description': ' NI-RFSA detects a falling edge.'
                },
                'name': 'FALLING_EDGE',
                'value': 901
            }
        ]
    },
    'DigitalEdgeTriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'name': 'RTSI0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'RTSI1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'RTSI2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'RTSI3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'RTSI4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'RTSI5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'RTSI6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'RTSI7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            }
        ]
    },
    'DigitizerSampleClockOutTerminal': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The Sample clock is not exported.'
                },
                'name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': ' Export the clock on the CLK OUT terminal on the Digitizer.'
                },
                'name': 'CLK_OUT',
                'value': 'ClkOut'
            }
        ]
    },
    'DigitizerSampleClockTimebaseSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The digitizer uses its onboard clock as the Sample clock timebase.'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' The digitizer uses the signal present at the CLK IN connector as the  Sample clock timebase.'
                },
                'name': 'CLK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': ' The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the  Sample clock timebase. This value is supported only for PXIe-5603 and PXIe-5665.'
                },
                'name': 'LO_REF_CLK',
                'value': 'LORefClk'
            },
            {
                'documentation': {
                    'description': ' The digitizer uses the signal present at the PXI Star line as the  Sample clock timebase.'
                },
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            }
        ]
    },
    'DownconverterFrequencyOffsetMode': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the  NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. '
                },
                'name': 'AUTOMATIC',
                'value': 1903
            },
            {
                'documentation': {
                    'description': ' NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the NIRFSA_ATTR_SIGNAL_BANDWIDTH  attribute has been set and can be avoided. NI-RFSA returns an error if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has  not been set, or if the signal bandwidth is too large. '
                },
                'name': 'ENABLED',
                'value': 1901
            },
            {
                'documentation': {
                    'description': ' NI-RFSA uses the offset that you specified with the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET or  NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attributes. '
                },
                'name': 'USER_DEFINED',
                'value': 1904
            }
        ]
    },
    'DownconverterPreselectorEnabledAttr': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables the preselector.'
                },
                'name': 'DISABLED',
                'value': 2600
            },
            {
                'documentation': {
                    'description': ' The preselector is automatically enabled when it is in the signal path and is automatically  disabled when it is not in the signal path. Only devices with a preselector on the downconverter support this option.  Use the NIRFSA_ATTR_PRESELECTOR_PRESENT attribute to determine if the downconverter has a preselector.'
                },
                'name': 'ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 2601
            },
            {
                'documentation': {
                    'description': ' Enables the preselector. If the preselector is not in a signal path or if the preselector is not supported on the device,  NI-RFSA returns an error. Select the NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH whenever possible avoid an error.'
                },
                'name': 'ENABLED',
                'value': 2602
            }
        ]
    },
    'EnabledAttr': {
        'values': [
            {
                'documentation': {
                    'description': ' Disable.'
                },
                'name': 'DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': ' Enable.'
                },
                'name': 'ENABLED',
                'value': 1901
            }
        ]
    },
    'ExportTerminal': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The signal is not exported.'
                },
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PFI 0.  For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PFI 1.'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 0.'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 1.'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 2.'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 3.'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 4.'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 5.'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 6.'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to PXI trigger line 7.'
                },
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to the PXI star trigger line.'
                },
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.'
                },
                'name': 'PXIE_DSTARC',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to the PXI/PXIe-5652 Ref Out.'
                },
                'name': 'REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to the PXI/PXIe-5652 Ref Out 2.'
                },
                'name': 'REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': ' The signal is exported to the PXIe-5622 Clk Out.'
                },
                'name': 'CLK_OUT',
                'value': 'ClkOut'
            }
        ]
    },
    'FetchRelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': ' Fetching occurs relative to the most recently acquired data. The value of the  NIRFSA_ATTR_FETCH_OFFSET attribute must be negative.'
                },
                'name': 'MOST_RECENT_SAMPLE',
                'value': 700
            },
            {
                'documentation': {
                    'description': ' Fetching occurs at the first sample acquired by the device. If the device wraps  its buffer, the first sample is no longer available. In this case, NI-RFSA  returns an error if the fetch offset is in the overwritten data.'
                },
                'name': 'FIRST_SAMPLE',
                'value': 701
            },
            {
                'documentation': {
                    'description': ' Fetching occurs relative to the Reference trigger. This value behaves like  NIRFSA_VAL_FIRST_SAMPLE if no Reference trigger is configured.'
                },
                'name': 'REF_TRIGGER',
                'value': 702
            },
            {
                'documentation': {
                    'description': ' Fetching occurs relative to the first pretrigger sample acquired. This value  behaves like NIRFSA_VAL_FIRST_SAMPLE if no Reference trigger is configured.'
                },
                'name': 'FIRST_PRETRIGGER_SAMPLE',
                'value': 703
            },
            {
                'documentation': {
                    'description': ' Fetching occurs after the last fetched sample.'
                },
                'name': 'CURRENT_READ_POSITION',
                'value': 704
            }
        ]
    },
    'FftWindowType': {
        'values': [
            {
                'documentation': {
                    'description': ' No window is applied.'
                },
                'name': 'UNIFORM',
                'value': 500
            },
            {
                'documentation': {
                    'description': ' The Hanning window is useful for analyzing transients longer than the time  duration of the window, and also for general-purpose applications. A Hanning  window is applied to the waveform using the  following equation:\n y[i] = 0.5 x x[i] x [1-cos(w)]\n where w = (2 pi)i/n and n = waveform size. '
                },
                'name': 'HANNING',
                'value': 501
            },
            {
                'documentation': {
                    'description': ' A Hamming window is applied to the waveform using the following equation: \n y[i] = x[i] [0.54 - 0.46cos(w)] \n where w = (2 pi)i/n and n = the waveform size.\n\n  the Hamming window does not get as close to zero near the edges as does the  Hanning window. ',
                    'note': ' Hanning and Hamming windows are somewhat similar. However, in the time domain, '
                },
                'name': 'HAMMING',
                'value': 502
            },
            {
                'documentation': {
                    'description': ' A Blackman-Harris window is applied to the waveform using the following  equation:\n y[i] = x[i] x [0.42323 - 0.49755cos(w) + 0.07922cos(2w)]\n where w = (2)i/n and n = the waveform size. '
                },
                'name': 'BLACKMAN_HARRIS',
                'value': 503
            },
            {
                'documentation': {
                    'description': ' An Exact Blackman window is applied to the waveform using the following  equation:\n y[i] = x[i] x [a0 - a1cos(w) + a2cos(2w)]\n where    w = (2 pi)i/n\n          n = the waveform size\n \t\ta0 = 7938/18608\n \t\ta1 = 9240/18608\n \t\ta2 = 1430/18608 '
                },
                'name': 'EXACT_BLACKMAN',
                'value': 504
            },
            {
                'documentation': {
                    'description': ' A Blackman window is useful for analyzing transient signals, and provides  similar windowing to Hanning and Hamming windows but adds one additional  cosine term to reduce ripple. A Blackman window is applied to the waveform  using the following equation:\n y[i] = x[i] x [0.42 - 0.50cos(w) + 0.08cos(2w)]\n where w = (2 pi)i/n and n = the waveform size. '
                },
                'name': 'BLACKMAN',
                'value': 505
            },
            {
                'documentation': {
                    'description': ' The fifth-order Flat Top window has the best amplitude accuracy of all the  window functions. The increased amplitude accuracy (+/-0.02 dB for signals  exactly between integral cycles) is at the expense of frequency selectivity.  The Flat Top window is most useful in accurately measuring the amplitude of  single frequency components with little nearby spectral energy in the signal.\n A fifth-order Flat Top window is applied to the waveform using the following equation:\n y[i] = x[i] x [a0 - a1cos(w) + a2cos(2w) - a3cos(3w) + a4cos(4w)]\n where w = (2 pi)i/n\n \t   n = the waveform size\n       a0 = 0.215578948\n       a1 = 0.41663158\n \t   a2 = 0.277263158\n \t   a3 = 0.083578947\n \t   a4 = 0.006947368 '
                },
                'name': 'FLAT_TOP',
                'value': 506
            },
            {
                'documentation': {
                    'description': ' A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection  in the upper 90 dB, with moderately wide side lobe.\n\n A 4-term Blackman Harris window is applied to the waveform using the following  equation:\n y[i] = x[i] x [0.422323 - 0.49755cos(w) + 0.07922cos(2w)]\n where w = (2 pi)i/n and n = the waveform size. '
                },
                'name': '4_TERM_BLACKMAN_HARRIS',
                'value': 507
            },
            {
                'documentation': {
                    'description': ' A 7-term Blackman-Harris window has the highest dynamic range;  it is ideal for signal-to-noise ratio applications.\n\n A 7-term Blackman Harris window is applied to the waveform using the following  equation:\n y[i] = x[i] x [a0 - a1cos(w) + a2cos(2w) - a3cos(3w) + a4cos(4w) - a5cos(5w) + a6cos(6w)]\n where w = (2 pi)i/n\n n is the waveform size\n a0 = 0.27105140069342\n a1 = 0.43329793923448\n a2 = 0.21812299954311\n a3 = 0.06592544638803\n a4 = 0.01081174209837\n a5 = 0.00077658482522\n a6 = 0.00001388721735 '
                },
                'name': '7_TERM_BLACKMAN_HARRIS',
                'value': 508
            },
            {
                'documentation': {
                    'description': ' The Low Side Lobe window further reduces the size of the main lobe.  Refer to the NIRFSA_ATTR_FFT_WINDOW_TYPE topic in the NI RF Vector Signal Analyzers  Help for the equation that defines the Low Side Lobe window. '
                },
                'name': 'LOW_SIDE_LOBE',
                'value': 509
            },
            {
                'documentation': {
                    'description': ' Gaussian Window.  '
                },
                'name': 'GAUSSIAN',
                'value': 510
            },
            {
                'documentation': {
                    'description': ' Kaiser-Bessel window.  '
                },
                'name': 'KAISER_BESSEL',
                'value': 511
            }
        ]
    },
    'FrequencySettlingUnits': {
        'values': [
            {
                'documentation': {
                    'description': ' Specify frequency settling time in parts per million (PPM).'
                },
                'name': 'PPM',
                'value': 2000
            },
            {
                'documentation': {
                    'description': ' Specify frequency settling in time after lock (seconds).'
                },
                'name': 'SECONDS_AFTER_LOCK',
                'value': 2001
            },
            {
                'documentation': {
                    'description': ' Specify frequency settling time after I/O (seconds).'
                },
                'name': 'SECONDS_AFTER_IO',
                'value': 2002
            }
        ]
    },
    'GeneralTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': ' The trigger is not configured.'
                },
                'name': 'NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': ' The trigger is configured to be a digital edge trigger.'
                },
                'name': 'DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': ' The trigger is configured to be a software trigger. You can assert the software  trigger by calling the niRFSA_SendSoftwareEdgeTrigger function.'
                },
                'name': 'SOFTWARE_EDGE',
                'value': 604
            }
        ]
    },
    'IfFilter': {
        'values': [
            {
                'documentation': {
                    'description': ' Uses the 187.5 MHz wide bandwidth filter.'
                },
                'name': '187_5_MHZ_WIDE',
                'value': 1400
            },
            {
                'documentation': {
                    'description': ' Uses the 187.5 MHz narrow bandwidth filter.'
                },
                'name': '187_5_MHZ_NARROW',
                'value': 1401
            },
            {
                'documentation': {
                    'description': ' Uses the 53 MHz filter.'
                },
                'name': '53_MHZ',
                'value': 1402
            },
            {
                'documentation': {
                    'description': ' Bypasses the IF filter.'
                },
                'name': 'BYPASS',
                'value': 1403
            }
        ]
    },
    'InputPort': {
        'values': [
            {
                'documentation': {
                    'description': ' Enables the RF IN port.'
                },
                'name': 'RF_IN',
                'value': 2000
            },
            {
                'documentation': {
                    'description': ' Enables the I/Q IN port.'
                },
                'name': 'IQ_IN',
                'value': 2001
            },
            {
                'documentation': {
                    'description': ' Enables the CAL IN port.'
                },
                'name': 'CAL_IN',
                'value': 2002
            },
            {
                'documentation': {
                    'description': ' Enables the I terminals of the I/Q IN port.'
                },
                'name': 'I_ONLY',
                'value': 2003
            }
        ]
    },
    'IqInPortTermConfig': {
        'values': [
            {
                'documentation': {
                    'description': ' Sets the terminal configuration to Differential.'
                },
                'name': 'DIFFERENTIAL',
                'value': 2100
            },
            {
                'documentation': {
                    'description': ' Sets the terminal configuration to Single-Ended.'
                },
                'name': 'SINGLE_ENDED',
                'value': 2101
            }
        ]
    },
    'LinearInterpolationFormat': {
        'values': [
            {
                'name': 'REAL_AND_IMAGINARY',
                'value': 4000
            },
            {
                'name': 'MAGNITUDE_AND_PHASE',
                'value': 4001
            },
            {
                'name': 'MAGNITUDE_DB_AND_PHASE',
                'value': 4002
            }
        ]
    },
    'LoInjectionSideValues': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures the LO signal that the NI-RFSA device generates at a frequency higher than  the RF frequency. This LO frequency is given by the formula fLO = fRF + fIF.'
                },
                'name': 'HIGH_SIDE',
                'value': 1300
            },
            {
                'documentation': {
                    'description': ' Configures the LO signal that the NI-RFSA device generates at a frequency lower than  the RF frequency. This LO frequency is given by the formula fLO = fRF - fIF.'
                },
                'name': 'LOW_SIDE',
                'value': 1301
            }
        ]
    },
    'LoPathSelection': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the LO path 1 is used. This value is the default. '
                },
                'name': 'EXT_CAL_LO_PATH_1',
                'value': 2300
            },
            {
                'documentation': {
                    'description': ' Specifies that the LO path 2 is used.'
                },
                'name': 'EXT_CAL_LO_PATH_2',
                'value': 2301
            },
            {
                'documentation': {
                    'description': ' Specifies that the LO path 3 is used.'
                },
                'name': 'EXT_CAL_LO_PATH_3',
                'value': 2302
            },
            {
                'documentation': {
                    'description': ' Specifies that the LO path 4 is used.'
                },
                'name': 'EXT_CAL_LO_PATH_4',
                'value': 2303
            },
            {
                'documentation': {
                    'description': ' Specifies that the LO path 5 is used.'
                },
                'name': 'EXT_CAL_LO_PATH_5',
                'value': 2304
            }
        ]
    },
    'LoSourceSelection': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. \n\n PXIe-5831—This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage. \n PXIe-5831 with PXIe-5653—This configuration uses the onboard LO of the PXIe5653 when associated with the PXIe-3622. \n PXIe-5840 with PXIe-5653—If the center frequency is greater than or equal to 3.2 GHz,  this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz, this configuration  uses the PXIe-5840 internal LO. If NI-RFSA is operating in Spectrum mode, this configuration uses the  PXIe-5840 internal LO regardless of the frequency. \n PXIe-5841 with PXIe-5655—This configuration uses the onboard LO of the PXIe-5655.'
                },
                'name': 'ONBOARD',
                'value': 'Onboard'
            },
            {
                'documentation': {
                    'description': ' Specifies that the LO source used to downconvert the RF input signal is  connected to the LO IN connector on the front panel.'
                },
                'name': 'LO_IN',
                'value': 'LO_In'
            },
            {
                'documentation': {
                    'description': ' Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5840 with PXIe-5653 or PXIe-5831 with PXIe-5653.'
                },
                'name': 'LO_SOURCE_SECONDARY',
                'value': 'Secondary'
            },
            {
                'documentation': {
                    'description': ' Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer  and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5841 with PXIe-5655.'
                },
                'name': 'LO_SOURCE_SG_SA_SHARED',
                'value': 'SG_SA_Shared'
            }
        ]
    },
    'LoYIGMainCoilDrive': {
        'values': [
            {
                'documentation': {
                    'description': ' Adjusts the YIG main coil on the LO for an underdamped response.'
                },
                'name': 'NORMAL',
                'value': 2400
            },
            {
                'documentation': {
                    'description': ' Adjusts the YIG main coil on the LO for an overdamped response.'
                },
                'name': 'FAST',
                'value': 2401
            }
        ]
    },
    'LoopBandwidth': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the downconverter module uses a narrow loop bandwidth.'
                },
                'name': 'NARROW',
                'value': 800
            },
            {
                'documentation': {
                    'description': ' Specifies that the downconverter module uses a medium loop bandwidth.'
                },
                'name': 'MEDIUM',
                'value': 801
            },
            {
                'documentation': {
                    'description': ' Specifies that the downconverter module uses a wide loop bandwidth.'
                },
                'name': 'WIDE',
                'value': 802
            }
        ]
    },
    'NotchFilterEnabled': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the notch filter will not be used.'
                },
                'name': 'DISABLED',
                'value': 3400
            },
            {
                'documentation': {
                    'description': ' Specifies that a notch filter will be used if available.'
                },
                'name': 'ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 3401
            },
            {
                'documentation': {
                    'description': ' Specifies that the notch filter will be used.'
                },
                'name': 'ENABLED',
                'value': 3402
            }
        ]
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures NI-RFSA to return a warning when an ADC or onboard signal processing (OSP) overflow occurs.'
                },
                'name': 'WARNING',
                'value': 1301
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSA to not return an error or a warning when an ADC or OSP overflow occurs.'
                },
                'name': 'DISABLED',
                'value': 1302
            }
        ]
    },
    'PowerSpectrumUnits': {
        'values': [
            {
                'documentation': {
                    'description': ' Units are dB with reference to 1 milliwatt.'
                },
                'name': 'DBM',
                'value': 200
            },
            {
                'documentation': {
                    'description': ' Units are in volts squared.'
                },
                'name': 'VOLTS_SQUARED',
                'value': 201
            },
            {
                'documentation': {
                    'description': ' Units are dB with reference to 1 millivolt.'
                },
                'name': 'DBMV',
                'value': 202
            },
            {
                'documentation': {
                    'description': ' Units are dB with reference to 1 microvolt.'
                },
                'name': 'DBUV',
                'value': 203
            },
            {
                'documentation': {
                    'description': ' Units are in volts.'
                },
                'name': 'VOLTS',
                'value': 204
            },
            {
                'documentation': {
                    'description': ' Units are in watts.'
                },
                'name': 'WATTS',
                'value': 205
            }
        ]
    },
    'PulseWidthUnitType': {
        'values': [
            {
                'documentation': {
                    'description': ' Units are seconds.'
                },
                'name': 'SECONDS',
                'value': 6200
            },
            {
                'documentation': {
                    'description': ' Units are clock periods.'
                },
                'name': 'CLOCK_PERIODS',
                'value': 6201
            }
        ]
    },
    'PxiChassisClk10Source': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The device does not drive the PXI 10 MHz backplane Reference clock.'
                },
                'name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': ' The device drives the PXI 10 MHz backplane Reference clock with the PXI-5600  onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz  I/O connector on the PXI-5600 front panel to use this option.'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' The device drives the PXI 10 MHz backplane Reference clock with the reference  source attached to the PXI-5600 FREQ REF IN connector. You must connect the  10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front  panel to use this option.'
                },
                'name': 'REF_IN',
                'value': 'RefIn'
            }
        ]
    },
    'RefClockOutTerminal': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The Reference clock is not exported.'
                },
                'name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': ' Export the clock on the REF IN/OUT terminal on the 5652 or on the REF OUT terminals on the PXIe-5653,  or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, and PXIe-5820/5830/5831/5840/5841.'
                },
                'name': 'REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': ' Export the clock on the REF OUT2 terminal on the LO. This connector does not  exist on some versions of the PXI/PXIe-5652.'
                },
                'name': 'REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': ' Export the clock on the CLK OUT terminal on the Digitizer.'
                },
                'name': 'CLK_OUT',
                'value': 'ClkOut'
            },
            {
                'documentation': {
                    'description': ' Export the RF Condiioner REF OUT terminal on the PXIe-5694. This value is  valid only for the PXIe-5667.'
                },
                'name': 'IF_COND_REF_OUT',
                'value': 'IFCondRefOut'
            }
        ]
    },
    'RefClockSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' No Reference clock is required for the current device configuration. This value is valid only for the PXIe-5694. '
                },
                'name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': ' PXI-5661-NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock. \n\n PXIe-5663/5663E-NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect  the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the  PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652,  connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. \n\n PXIe-5665-NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT  terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. \n\n PXIe-5667-NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock.  Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622,  and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694.\n\n PXIe-5668-Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2  OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. \n\n PXIe-5644/5645/5646, PXIe-5820/5840/5841—Lock the NI-RFSA device to its onboard clock. PXIe-5830/5831—For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe3621 REF OUT connector. For the PXIe-5831,  connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. \n\n PXIe-5831 with PXIe-5653—Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz)  connector to the PXIe-3622 REF IN connector. \n\n PXIe-5840 with PXIe-5653—Lock to the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz) connector on the  PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSG sessions to the device to use NIRFSG_VAL_REF_IN_STR  for the PXIe-5840 or NIRFSG_VAL_REF_IN_2_STR for the PXIe-5840 with PXIe-5653. \n\n PXIe-5841 with PXIe-5655—Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on  the PXIe-5655 to the PXIe-5841 REF IN connector.'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' PXI-5661—NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN  connector on the PXI-5600. \n\n PXIe-5663/5663E—Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the  REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On  versions of the 5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration  can only be used in external digitizer mode.\n\n PXIe-5665—Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT  terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz,  set the NIRFSA_ATTR_REF_CLOCK_RATE attribute according to the frequency of your external clock signal.\n\n PXIe-5667—Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal  on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on  the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is  set to a frequency other than 10 MHz, set the NIRFSA_ATTR_REF_CLOCK_RATE attribute according  to the frequency of your external clock signal. \n\n PXIe-5694—Connect the Reference clock signal to the REF/LO IN connector on the PXIe-5694 front panel.\n\n PXIe-5644/5645/5646, PXIe-5820/5840/5841—Lock the NI-RFSA device to the signal at the external REF IN connector. \n PXIe-5830/5831—For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe3621 REF OUT connector.  For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.  For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831,  lock the external signal to the PXIe-3622 REF IN connector. \n PXIe-5831 with PXIe-5653—Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.  Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. \n PXIe-5840 with PXIe-5653—Lock to the signal at the REF IN connector on the associated PXIe-5653. Connect the  REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. \n PXIe-5841 with PXIe-5655—Lock to the signal at the REF IN connector on the associated PXIe-5655.  Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN.'
                },
                'name': 'REF_IN',
                'value': 'RefIn'
            },
            {
                'documentation': {
                    'description': ' PXI-5661-NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600.  You must connect the PXI 10 MHz connector to the REF IN connector on the  PXI-5600 front panel to use this option. \n\n PXIe-5668-Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2  OUT to the LO2 IN connector on the PXIe-5624. \n\n PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5830/5831/5831 with PXIe-5653/5840/5841/5840 with PXIe-5653/5841/5841 with PXIe-5655-Lock the device to the PXI backplane clock. '
                },
                'name': 'PXI_CLK',
                'value': 'PXI_Clk'
            },
            {
                'documentation': {
                    'description': ' PXI-5661-This configuration does not apply to the PXI-5661. \n\n PXIe-5663/5663E-Lock the PXIe-5663/5663E to an external 10 MHz signal.  Connect the external signal to the  CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the  FREQ REF IN connector  on the PXI/PXIe-5652.\n\n PXIe-5665-NI-RFSA locks the PXIe-5665 to an external 100 MHz signal.  Connect the external signal to the CLK IN  connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN  connector on the PXIe-5653. Set the NIRFSA_ATTR_REF_CLOCK_RATE attribute to 100 MHz. \n\n PXIe-5667-NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal  to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN  connector on the PXIe-5653. Connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector  on the PXIe-5694. Set the NIRFSA_ATTR_REF_CLOCK_RATE attribute to 100 MHz.\n\n PXIe-5668-Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN  connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653.  Set the clock rate parameter to 100 MHz. \n\n PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655-This configuration does not apply. '
                },
                'name': 'CLK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': ' PXIe-5840 with PXIe-5653—NI-RFSA locks the device to the clock sourced at the PXIe-5840 REF IN terminal that  is already configured by an NI-RFSG session. Connect the PXIe-5840 REF OUT connector to the PXIe-5653 REF IN connector.  Configure open NI-RFSG sessions to the device to use NIRFSG_VAL_REF_IN_2_STR for the PXIe-5840 or NIRFSG_VAL_ONBOARD_CLOCK_STR for the PXIe-5840 with PXIe-5653. \n\n PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5840/5841/5841 with PXIe-5655—This configuration does not apply. '
                },
                'name': 'REF_IN_2',
                'value': 'RefIn2'
            },
            {
                'documentation': {
                    'description': ' PXIe-5831 with PXIe-5653—NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622  to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. \n PXIe-5840 with PXIe-5653—NI-RFSA configures the PXIe-5653 to export the Reference Clock, and configures the  PXIe-5840 to use NIRFSA_VAL_PXI_CLK_STR. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.  For best performance, configure all other devices in the system to use NIRFSA_VAL_PXI_CLK_STR as the Reference Clock source. \n\n PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5840/5841/5841 with PXIe-5655—This configuration does not apply. '
                },
                'name': 'PXI_CLK_MASTER',
                'value': 'PXI_ClkMaster'
            }
        ]
    },
    'RefTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': ' No Reference trigger is configured.'
                },
                'name': 'NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': ' The Reference trigger is not asserted until a digital edge is detected. The  source of the digital edge is specified with the NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE attribute.'
                },
                'name': 'DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': ' The Reference trigger is asserted when the signal is changing past the level  specified with the slope (rising or falling) configured with the  NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE attribute.'
                },
                'name': 'IQ_POWER_EDGE',
                'value': 603
            },
            {
                'documentation': {
                    'description': ' The Reference trigger is not asserted until a software trigger occurs. You can  assert the software trigger by calling the niRFSA_SendSoftwareEdgeTrigger  function and passing NIRFSA_VAL_REF_TRIGGER as the trigger parameter.'
                },
                'name': 'SOFTWARE_EDGE',
                'value': 604
            },
            {
                'documentation': {
                    'description': ' The Reference trigger is asserted when the I or Q signal is changed past the level  specified with the slope configured with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE  attribute. This value is supported only for the PXIe-5644/5645 devices.'
                },
                'name': 'IQ_ANALOG_EDGE',
                'value': 605
            }
        ]
    },
    'ResetWithOptionsStepsToOmit': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'ROUTES',
                'value': 1
            },
            {
                'name': 'DEEMBEDDING_TABLES',
                'value': 2
            }
        ]
    },
    'RfLBSigCondPathSel': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies to use RF Lowband Signal Conditioning Path 1. This value is default.'
                },
                'name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1',
                'value': 3700
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF Lowband Signal Conditioning Path 2.'
                },
                'name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2',
                'value': 3701
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF Lowband Signal Conditioning Path 3.'
                },
                'name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_3',
                'value': 3702
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF Lowband Signal Conditioning Path 4.'
                },
                'name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_4',
                'value': 3703
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF Lowband Signal Conditioning Path 5.'
                },
                'name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_5',
                'value': 3704
            }
        ]
    },
    'RfPathSelection': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies to use RF band 1. This value is the default.'
                },
                'name': 'EXT_CAL_RF_BAND_1',
                'value': 1700
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF band 2.'
                },
                'name': 'EXT_CAL_RF_BAND_2',
                'value': 1701
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF band 3.'
                },
                'name': 'EXT_CAL_RF_BAND_3',
                'value': 1702
            },
            {
                'documentation': {
                    'description': ' Specifies to use RF band 4.'
                },
                'name': 'EXT_CAL_RF_BAND_4',
                'value': 1703
            }
        ]
    },
    'RfPreampEnabled': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables the RF preamplifier. '
                },
                'name': 'DISABLED',
                'value': 2500
            },
            {
                'documentation': {
                    'description': ' Enables the RF preamplifier when the RF preamplifier is present in the signal path  and disables the preamplifier when it is not in the path. Only devices with an RF  preamplifier on the downconverter support this option. Use the NIRFSA_ATTR_RF_PREAMP_PRESENT  attribute to determine whether the downconverter has a preamplifier.'
                },
                'name': 'ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 2501
            },
            {
                'documentation': {
                    'description': ' Enables the RF preamplifier. If the RF preamplifier is not in a signal path,  NI-RFSA returns an error. Select the NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH  option whenever possible to avoid an error.'
                },
                'name': 'ENABLED',
                'value': 2502
            },
            {
                'documentation': {
                    'description': ' Enables the RF preamplifier automatically based on the value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5840/5841.'
                },
                'name': 'AUTOMATIC',
                'value': 2503
            }
        ]
    },
    'RfPreselectorFilter': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that no filter is used'
                },
                'name': 'FILTER_PATH_NONE',
                'value': 3300
            },
            {
                'documentation': {
                    'description': ' Specifies that the 19-35 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_1',
                'value': 3301
            },
            {
                'documentation': {
                    'description': ' Specifies that the 33-61 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_2',
                'value': 3302
            },
            {
                'documentation': {
                    'description': ' Specifies that the 59-110 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_3',
                'value': 3303
            },
            {
                'documentation': {
                    'description': ' Specifies that the 90-167 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_4',
                'value': 3304
            },
            {
                'documentation': {
                    'description': ' Specifies that the 140-245 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_5',
                'value': 3305
            },
            {
                'documentation': {
                    'description': ' Specifies that the 205-370 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_6',
                'value': 3306
            },
            {
                'documentation': {
                    'description': ' Specifies that the 330-595 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_7',
                'value': 3307
            },
            {
                'documentation': {
                    'description': ' Specifies that the 550-975 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_8',
                'value': 3308
            },
            {
                'documentation': {
                    'description': ' Specifies that the 910-1600 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_9',
                'value': 3309
            },
            {
                'documentation': {
                    'description': ' Specifies that the 1520-2040 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_10',
                'value': 3310
            },
            {
                'documentation': {
                    'description': ' Specifies that the 1960-2540 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_11',
                'value': 3311
            },
            {
                'documentation': {
                    'description': ' Specifies that the 2460-3040 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_12',
                'value': 3312
            },
            {
                'documentation': {
                    'description': ' Specifies that the 2960-3840 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_13',
                'value': 3313
            },
            {
                'documentation': {
                    'description': ' Specifies that the 3760-4640 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_14',
                'value': 3314
            },
            {
                'documentation': {
                    'description': ' Specifies that the 4560-5840 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_15',
                'value': 3315
            },
            {
                'documentation': {
                    'description': ' Specifies that the 5760-7040 MHz pre-selector filter is used'
                },
                'name': 'FILTER_PATH_16',
                'value': 3316
            },
            {
                'documentation': {
                    'description': ' Specifies that the external pre-selector filter is used'
                },
                'name': 'FILTER_PATH_EXTERNAL_FILTER',
                'value': 3317
            }
        ]
    },
    'SelfCalibrateSteps': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'ALIGNMENT',
                'value': 1
            },
            {
                'name': 'GAIN_REFERENCE',
                'value': 2
            },
            {
                'name': 'IF_FLATNESS',
                'value': 4
            },
            {
                'name': 'DIGITIZER_SELF_CAL',
                'value': 8
            },
            {
                'name': 'LO_SELF_CAL',
                'value': 16
            },
            {
                'name': 'AMPLITUDE_ACCURACY',
                'value': 32
            },
            {
                'name': 'RESIDUAL_LO_POWER',
                'value': 64
            },
            {
                'name': 'IMAGE_SUPPRESSION',
                'value': 128
            },
            {
                'name': 'SYNTHESIZER_ALIGNMENT',
                'value': 256
            },
            {
                'name': 'DC_OFFSET',
                'value': 512
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'START_TRIGGER',
                'value': 1100
            },
            {
                'name': 'REF_TRIGGER',
                'value': 702
            },
            {
                'name': 'ADVANCE_TRIGGER',
                'value': 1102
            },
            {
                'name': 'ARM_REF_TRIGGER',
                'value': 1103
            },
            {
                'name': 'READY_FOR_START_EVENT',
                'value': 1200
            },
            {
                'name': 'READY_FOR_REF_EVENT',
                'value': 1201
            },
            {
                'name': 'READY_FOR_ADVANCE_EVENT',
                'value': 1202
            },
            {
                'name': 'END_OF_RECORD_EVENT',
                'value': 1203
            },
            {
                'name': 'DONE_EVENT',
                'value': 1204
            },
            {
                'name': 'REF_CLOCK',
                'value': 1205
            },
            {
                'name': 'USER',
                'value': 1206
            }
        ]
    },
    'SignalConditioningEnabled': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the signal conditioning will be enabled.'
                },
                'name': 'ENABLED',
                'value': 3600
            },
            {
                'documentation': {
                    'description': ' Specifies that all signal conditioning will be bypassed.'
                },
                'name': 'BYPASSED',
                'value': 3601
            }
        ]
    },
    'SparameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 3800
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 3801
            }
        ]
    },
    'StepGainEnabled': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the step gain amplifier will be disabled.'
                },
                'name': 'DISABLED',
                'value': 3200
            },
            {
                'documentation': {
                    'description': ' Specifies that the step gain amplifier will be enabled.'
                },
                'name': 'ENABLED',
                'value': 3201
            }
        ]
    },
    'TriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The trigger is received on PFI 0.  For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PFI 1.'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 0.'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 1.'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 2.'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 3.'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 4.'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 5.'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 6.'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on PXI trigger line 7.'
                },
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on the PXI star trigger line.'
                },
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.'
                },
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': ' The trigger is received on expiration of the specified Timer Event Interval.'
                },
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'documentation': {
                    'description': ' The device is reconfigured when the acquisition reaches the end of record event.'
                },
                'name': 'END_OF_RECORD_EVENT',
                'value': 'EndOfRecordEvent'
            },
            {
                'documentation': {
                    'description': ' The device uses the Start trigger to start the timer.'
                },
                'name': 'START_TRIGGER',
                'value': 'StartTrigger'
            },
            {
                'documentation': {
                    'description': ' The device uses the Reference trigger to start the timer.'
                },
                'name': 'REFERENCE_TRIGGER',
                'value': 'ReferenceTrigger'
            },
            {
                'name': 'SYNC_START_TRIGGER',
                'value': 'Sync_Start'
            },
            {
                'name': 'SYNC_REF_TRIGGER',
                'value': 'Sync_Ref'
            },
            {
                'name': 'SYNC_ADVANCE_TRIGGER',
                'value': 'Sync_Advance'
            }
        ]
    },
    'UnspecifiedAttr': {
        'values': [
            {
                'documentation': {
                    'description': ' The LO signal is not exported from the RF OUT LO OUT terminal.'
                },
                'name': 'DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': ' The LO signal is exported from the RF OUT LO OUT terminal.'
                },
                'name': 'ENABLED',
                'value': 1901
            },
            {
                'documentation': {
                    'description': ' The LO signal may or may not be exported to the RF OUT LO OUT terminal, because NI-RFSG may be controlling it.'
                },
                'name': 'UNSPECIFIED',
                'value': 1902
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/enums_addon.py sha256=551322a6ca359a50afe041c2f67b9bb3bfe36ba0cbd435afafaba6d99822c2a6 bytes=304 -->
## FILE: source/codegen/metadata/nirfsa/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/enums_addon.py`
- sha256: `551322a6ca359a50afe041c2f67b9bb3bfe36ba0cbd435afafaba6d99822c2a6`
- bytes: 304

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "DigitalEdgeTriggerSource": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/functions.py sha256=24e2387e8de5b1112615e236c394d01ac820cf9f89a0f9fa9c4bca3c00b85362 bytes=74918 -->
## FILE: source/codegen/metadata/nirfsa/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/functions.py`
- sha256: `24e2387e8de5b1112615e236c394d01ac820cf9f89a0f9fa9c4bca3c00b85362`
- bytes: 74918

````python
functions = {
    'Abort': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAcquisitionStatus': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'isDone',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearSelfCalibrateRange': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niRFSA_close',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisitionType': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'AcquisitionType',
                'name': 'acquisitionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationLinear': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'LinearInterpolationFormat',
                'name': 'format',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationNearest': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDeembeddingTableInterpolationSpline': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeAdvanceTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdge',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeRefTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdge',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdge',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureIQCarrierFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'carrierFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureIQPowerEdgeRefTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'hardcoded_value': '"0"',
                'include_in_proto': False,
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'enum': 'AnalogSlope',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureIQRate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'iqRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureNumberOfRecords': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecordsIsFinite',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureNumberOfSamples': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamplesIsFinite',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'samplesPerRecord',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePXIChassisClk10': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'PxiChassisClk10Source',
                'name': 'pxiClk10Source',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefClock': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'RefClockSource',
                'name': 'clockSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'refClockRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureReferenceLevel': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureResolutionBandwidth': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'resolutionBandwidth',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeAdvanceTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeRefTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'pretriggerSamples',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSpectrumFrequencyCenterSpan': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'centerFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'span',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSpectrumFrequencyStartStop': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'startFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationList': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'listName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfListAttributes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'listAttributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfListAttributes'
                },
                'type': 'ViAttr[]'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveList',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateConfigurationListStep': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableArray': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequenciesSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'frequenciesSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'sparameterTable',
                'size': {
                    'mechanism': 'len',
                    'value': 'sparameterTableSize'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'sparameterTableSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateDeembeddingSparameterTableS2PFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 's2pFilePath',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'SparameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllDeembeddingTables': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteConfigurationList': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'listName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteDeembeddingTable': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableAdvanceTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableRefTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableSessionAccess': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'enable',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niRFSA_error_message',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'statusCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1024
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorQuery': {
        'cname': 'niRFSA_error_query',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1024
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Signal',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'ExportTerminal',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQMultiRecordComplexF32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'startingRecord',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumberF32',
                'name': 'data',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'numberOfSamples * numberOfRecords'
                },
                'type': 'NIComplexNumberF32_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfRecords'
                },
                'type': 'struct niRFSA_wfmInfo_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQMultiRecordComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'startingRecord',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'data',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'numberOfSamples * numberOfRecords'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfRecords'
                },
                'type': 'struct niRFSA_wfmInfo_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQMultiRecordComplexI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'startingRecord',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'data',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'numberOfSamples * numberOfRecords'
                },
                'type': 'NIComplexI16_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfRecords'
                },
                'type': 'struct niRFSA_wfmInfo_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQSingleRecordComplexF32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumberF32',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumberF32_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'WaveformInfo',
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQSingleRecordComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'WaveformInfo',
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchIQSingleRecordComplexI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexI16_struct[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'WaveformInfo',
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'info',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfoMaxSize': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'infoSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingSparameters': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'sparameters',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'sparametersArraySize',
                    'value_twist': 'numberOfSparameters'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'sparametersArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'numberOfSparameters',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeviceResponse': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DeviceResponse',
                'name': 'responseType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'magnitudeResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'phaseResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfFrequencies',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFetchBacklog': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'recordNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'backlog',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFrequencyResponse': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'magnitudeResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'phaseResponse',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfFrequencies',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNormalizationCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated CoefficientInfo',
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'numberOfCoefficientSets'
                },
                'type': 'struct niRFSA_coefficientInfo_struct[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNumberOfSpectralLines': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'numberOfSpectralLines',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayName': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'tags': [
                        'strlen-bug'
                    ],
                    'value': 'bufferSize',
                    'value_twist': 'bufferSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'bufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayOperationsCount': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'operationsCount',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'bufferSize'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'bufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetScalingCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated CoefficientInfo',
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'numberOfCoefficientSets'
                },
                'type': 'struct niRFSA_coefficientInfo_struct[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'selfCalibrationStep',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'selfCalibrationStep',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'temp',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSpectralInfoForSMT': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.SmtSpectrumInfo',
                'name': 'spectrumInfo',
                'type': 'SmtSpectrumInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStreamEndpointHandle': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'streamEndpoint',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'writerHandle',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTerminalName': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Signal',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'terminalName',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetUserData': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'identifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualDataSize'
                },
                'type': 'ViInt8[]'
            },
            {
                'direction': 'out',
                'name': 'actualDataSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niRFSA_init',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsSelfCalValid': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'selfCalValid',
                'type': 'ViBoolean'
            },
            {
                'bitfield_as_enum_array': 'SelfCalibrateSteps',
                'direction': 'out',
                'name': 'validSteps',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadConfigurationsFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformThermalCorrection': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadIQSingleRecordComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'grpc_type': 'WaveformInfo',
                'name': 'wfmInfo',
                'type': 'struct niRFSA_wfmInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadPowerSpectrumF32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'powerSpectrumData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'ViReal32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'SpectrumInfo',
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadPowerSpectrumF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'powerSpectrumData',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'dataArraySize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'grpc_type': 'SpectrumInfo',
                'name': 'spectrumInfo',
                'type': 'struct niRFSA_spectrumInfo_struct'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niRFSA_reset',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithOptions': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'ResetWithOptionsStepsToOmit',
                'name': 'stepsToOmit',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niRFSA_revision_query',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'driverRev',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'instrRev',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SaveConfigurationsToFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalibrateSteps',
                'name': 'stepsToOmit',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrateRange': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalibrateSteps',
                'name': 'stepsToOmit',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'minFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'maxFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minReferenceLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'maxReferenceLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niRFSA_self_test',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'testResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'testMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Signal',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCalUserDefinedInfo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'info',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetUserData': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'identifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsa/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfsa/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsa/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/__init__.py sha256=80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad bytes=250 -->
## FILE: source/codegen/metadata/nirfsg/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/__init__.py`
- sha256: `80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad`
- bytes: 250

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}
````
