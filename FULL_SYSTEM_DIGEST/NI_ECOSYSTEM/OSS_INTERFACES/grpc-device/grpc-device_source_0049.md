# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/enums.py sha256=9d59ef595b1ef2784a6ceaf917871d5eb2a23425565f01ce7bb3eba6ab28c3f9 bytes=12751 -->
## FILE: source/codegen/metadata/nirfmxpulse/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/enums.py`
- sha256: `9d59ef595b1ef2784a6ceaf917871d5eb2a23425565f01ce7bb3eba6ab28c3f9`
- bytes: 12751

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
            },
            {
                'name': 'REF_IN2',
                'value': 'RefIn2'
            },
            {
                'name': 'PXI_CLK_MASTER',
                'value': 'PXI_Clk_Master'
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
                'name': 'RISING_SLOPE',
                'value': 0
            },
            {
                'name': 'FALLING_SLOPE',
                'value': 1
            }
        ]
    },
    'MaximumPulseCountEnabled': {
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
    'MeasurementFilterType': {
        'values': [
            {
                'name': 'RECTANGULAR',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'PULSE',
                'value': 1
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
    'MultiburstEnabled': {
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
    'PulseAcquisitionTraceSelect': {
        'values': [
            {
                'name': 'ALL_PULSES',
                'value': 0
            },
            {
                'name': 'SUBSET',
                'value': 1
            }
        ]
    },
    'PulseAmplitudeLevelDomain': {
        'values': [
            {
                'name': 'VOLTS',
                'value': 0
            },
            {
                'name': 'WATTS',
                'value': 1
            }
        ]
    },
    'PulseAmplitudeTraceUnit': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'VOLTS',
                'value': 1
            },
            {
                'name': 'WATTS',
                'value': 2
            }
        ]
    },
    'PulseCWFrequencyOffsetAuto': {
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
    'PulseDetectionReference': {
        'values': [
            {
                'name': 'REFERENCE_LEVEL',
                'value': 0
            },
            {
                'name': 'ABSOLUTE',
                'value': 1
            },
            {
                'name': 'PEAK',
                'value': 2
            }
        ]
    },
    'PulseDroopCompensationEnabled': {
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
    'PulseFrequencyAndPhaseDeviationRangeReference': {
        'values': [
            {
                'name': 'EDGE',
                'value': 0
            },
            {
                'name': 'CENTER',
                'value': 1
            }
        ]
    },
    'PulseLevelComputationMethod': {
        'values': [
            {
                'name': 'MEAN',
                'value': 0
            },
            {
                'name': 'MEDIAN',
                'value': 1
            },
            {
                'name': 'MODE',
                'value': 2
            }
        ]
    },
    'PulseMeasurementPointReference': {
        'values': [
            {
                'name': 'RISE',
                'value': 0
            },
            {
                'name': 'CENTER',
                'value': 1
            },
            {
                'name': 'FALL',
                'value': 2
            }
        ]
    },
    'PulseMetricsAmplitudeDeviationUnit': {
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
    'PulseMetricsEnabled': {
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
    'PulseModulationType': {
        'values': [
            {
                'name': 'CW',
                'value': 0
            },
            {
                'name': 'LINEAR_FM',
                'value': 1
            },
            {
                'name': 'TRIANGULAR_FM',
                'value': 2
            }
        ]
    },
    'PulseMultipleMeasurementPointsEnabled': {
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
    'PulseStabilityEnabled': {
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
    'PulseStabilityFrequencyErrorCompensation': {
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
    'PulseTimeSidelobeEnabled': {
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
    'PulseTimeSidelobeKeepOutTimeAuto': {
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
    'PulseTimeSidelobeReferenceWindowType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLATTOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'DOLPH_CHEBYSHEV',
                'value': 6
            }
        ]
    },
    'PulseTraceRangeAuto': {
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
    'PulseTraceRangeReference': {
        'values': [
            {
                'name': 'RISE',
                'value': 0
            },
            {
                'name': 'CENTER',
                'value': 1
            },
            {
                'name': 'FALL',
                'value': 2
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
    'SegmentedAcquisitionEnabled': {
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
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/enums_addon.py sha256=67149519d49e2a7016bdc78ff16db650e492f9f02b68d8941d7876f3f3d43b18 bytes=188 -->
## FILE: source/codegen/metadata/nirfmxpulse/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/enums_addon.py`
- sha256: `67149519d49e2a7016bdc78ff16db650e492f9f02b68d8941d7876f3f3d43b18`
- bytes: 188

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/functions.py sha256=f51e3ff91e5f3eaf6e8a14960f74fe6181d31c01a3bda9a7b33ff0c08d118a80 bytes=100532 -->
## FILE: source/codegen/metadata/nirfmxpulse/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/functions.py`
- sha256: `f51e3ff91e5f3eaf6e8a14960f74fe6181d31c01a3bda9a7b33ff0c08d118a80`
- bytes: 100532

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
        'cname': 'RFmxPulse_AnalyzeIQ1Waveform',
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
                'name': 'bandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'measurementInterval',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceLevel',
                'type': 'float64'
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
    'Cfg1ReferenceWaveform': {
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
    'Cfg1ReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxPulse_Cfg1ReferenceWaveform',
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
    'Cfg1ReferenceWaveformSplit': {
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
    'CfgRF': {
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
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
                'type': 'float64'
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
    'FetchAcquiredAmplitudeTrace': {
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
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'sampleDuration',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'amplitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'amplitudeArraySize',
                    'value_twist': 'amplitudeActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'amplitudeArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'amplitudeActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'startIndex',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'startArraySize',
                    'value_twist': 'startActualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'startTimeStamp',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'startArraySize',
                    'value_twist': 'startActualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'startArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'startActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'FetchAmplitudeTrace': {
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
                'name': 'amplitude',
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
    'FetchBurstIntrapulseStabilityTrace': {
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
                'name': 'intrapulseAverageAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'intrapulseAveragePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'intrapulseAverageTotalStability',
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
    'FetchBurstSelectedPositionStabilityTrace': {
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
                'name': 'pulseAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulsePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulseTotalStability',
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
    'FetchFrequencyTrace': {
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
                'name': 'frequency',
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
    'FetchIQTrace': {
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
                'name': 'iqData',
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
    'FetchIQTraceInterleavedIQ': {
        'cname': 'RFmxPulse_FetchIQTrace',
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
                'name': 'iqData',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(iqData)'
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
    'FetchIQTraceSplit': {
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
                'name': 'iqDataI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'iqDataQ',
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
    'FetchIntrapulseStabilityTrace': {
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
                'name': 'intrapulseAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'intrapulsePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'intrapulseTotalStability',
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
    'FetchMultipleMeasurementPointsStabilityTrace': {
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
                'name': 'pulseAverageAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulseAveragePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulseAverageTotalStability',
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
    'FetchPhaseWrappedTrace': {
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
                'name': 'wrappedPhase',
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
    'FetchPulseToPulseStabilityTrace': {
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
                'name': 'pulseIndex',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'pulseToPulseAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'pulseToPulsePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'pulseToPulseTotalStability',
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
    'FetchStabilityTrace': {
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
                'name': 'pulseAmplitudeStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulsePhaseStability',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pulseTotalStability',
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
    'FetchTimeSidelobeTrace': {
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
                'name': 'timeSidelobe',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
        'custom_close': 'Close(id, RFMXPULSE_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXPULSE_VAL_FALSE)',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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
                'grpc_type': 'NiRFmxPulseAttribute',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/functions_addon.py sha256=2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679 bytes=34 -->
## FILE: source/codegen/metadata/nirfmxpulse/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/functions_addon.py`
- sha256: `2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679`
- bytes: 34

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/__init__.py sha256=abf24fd9033411911dc53045c75ccb618c079c177433aaf01d88f16a8403b7b3 bytes=363 -->
## FILE: source/codegen/metadata/nirfmxspecan/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/__init__.py`
- sha256: `abf24fd9033411911dc53045c75ccb618c079c177433aaf01d88f16a8403b7b3`
- bytes: 363

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}

metadata['functions'].update(functions_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/attributes.py sha256=bf5f5198c4736f1129778f45c53d61eac36a43b15e9badca8768697fc943f126 bytes=106345 -->
## FILE: source/codegen/metadata/nirfmxspecan/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/attributes.py`
- sha256: `bf5f5198c4736f1129778f45c53d61eac36a43b15e9badca8768697fc943f126`
- bytes: 106345

````python
attributes = {
    1048577: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    1048578: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    1048579: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    1048580: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    1048581: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    1048582: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    1048583: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    1048584: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    1048585: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    1048586: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    1048587: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    1048588: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    1048589: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    1048590: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    1048591: {
        'access': 'read-write',
        'name': 'SELECTED_PATH',
        'type': 'char[]'
    },
    1052663: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_OFFSET',
        'type': 'float64'
    },
    1052664: {
        'access': 'read-write',
        'name': 'NUMBER_OF_STEPS',
        'type': 'int32'
    },
    1052665: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_DURATION',
        'type': 'float64'
    },
    1052668: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    1052669: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    1052671: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    1052672: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1052674: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1052675: {
        'access': 'read-write',
        'enum': 'AcpCarrierMode',
        'name': 'ACP_CARRIER_MODE',
        'type': 'int32'
    },
    1052676: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1052677: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1052678: {
        'access': 'read-write',
        'enum': 'AcpCarrierRrcFilterEnabled',
        'name': 'ACP_CARRIER_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    1052679: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_RRC_FILTER_ALPHA',
        'type': 'float64'
    },
    1052680: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    1052681: {
        'access': 'read-write',
        'enum': 'AcpOffsetEnabled',
        'name': 'ACP_OFFSET_ENABLED',
        'type': 'int32'
    },
    1052682: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    1052683: {
        'access': 'read-write',
        'enum': 'AcpOffsetSideband',
        'name': 'ACP_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    1052684: {
        'access': 'read-write',
        'enum': 'AcpOffsetPowerReferenceCarrier',
        'name': 'ACP_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1052685: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_POWER_REFERENCE_SPECIFIC',
        'type': 'int32'
    },
    1052686: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1052687: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_RELATIVE_ATTENUATION',
        'type': 'float64'
    },
    1052688: {
        'access': 'read-write',
        'enum': 'AcpOffsetRrcFilterEnabled',
        'name': 'ACP_OFFSET_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    1052689: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_RRC_FILTER_ALPHA',
        'type': 'float64'
    },
    1052690: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    1052691: {
        'access': 'read-write',
        'enum': 'AcpPowerUnits',
        'name': 'ACP_POWER_UNITS',
        'type': 'int32'
    },
    1052692: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1052693: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    1052694: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1052696: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    1052697: {
        'access': 'read-write',
        'enum': 'AcpFftWindow',
        'name': 'ACP_FFT_WINDOW',
        'type': 'int32'
    },
    1052698: {
        'access': 'read-write',
        'name': 'ACP_FFT_PADDING',
        'type': 'float64'
    },
    1052699: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1052700: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1052701: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1052702: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1052703: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1052704: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1052705: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1052706: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    1052707: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_FREQUENCY_RESOLUTION',
        'type': 'float64'
    },
    1052708: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1052709: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1052710: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1052711: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_TOTAL_RELATIVE_POWER',
        'type': 'float64'
    },
    1052712: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_FREQUENCY_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1052713: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    1052714: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1052715: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1052716: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1052717: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    1052718: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_FREQUENCY_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1052719: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    1052720: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1052721: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1052722: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1052723: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    1052724: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    1052725: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    1052726: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    1052727: {
        'access': 'read-write',
        'enum': 'AcpOffsetFrequencyDefinition',
        'name': 'ACP_OFFSET_FREQUENCY_DEFINITION',
        'type': 'int32'
    },
    1052728: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterBandwidthDefinition',
        'name': 'ACP_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1052729: {
        'access': 'read-write',
        'enum': 'AcpAmplitudeCorrectionType',
        'name': 'ACP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1052730: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    1052731: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    1052732: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    1052733: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMode',
        'name': 'ACP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    1052734: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationType',
        'name': 'ACP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    1052735: {
        'access': 'read-write',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    1052736: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationAveragingAuto',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    1052737: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationMode',
        'name': 'ACP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    1052738: {
        'access': 'read-write',
        'enum': 'AcpDetectorType',
        'name': 'ACP_DETECTOR_TYPE',
        'type': 'int32'
    },
    1052739: {
        'access': 'read-write',
        'name': 'ACP_DETECTOR_POINTS',
        'type': 'int32'
    },
    1056768: {
        'access': 'read-write',
        'name': 'CCDF_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1056770: {
        'access': 'read-write',
        'name': 'CCDF_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1056771: {
        'access': 'read-write',
        'name': 'CCDF_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1056772: {
        'access': 'read-write',
        'name': 'CCDF_NUMBER_OF_RECORDS',
        'type': 'int32'
    },
    1056774: {
        'access': 'read-write',
        'name': 'CCDF_RBW_FILTER_RRC_ALPHA',
        'type': 'float64'
    },
    1056775: {
        'access': 'read-write',
        'name': 'CCDF_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1056776: {
        'access': 'read-write',
        'enum': 'CcdfRbwFilterType',
        'name': 'CCDF_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1056777: {
        'access': 'read-write',
        'enum': 'CcdfThresholdEnabled',
        'name': 'CCDF_THRESHOLD_ENABLED',
        'type': 'int32'
    },
    1056778: {
        'access': 'read-write',
        'name': 'CCDF_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    1056779: {
        'access': 'read-write',
        'enum': 'CcdfThresholdType',
        'name': 'CCDF_THRESHOLD_TYPE',
        'type': 'int32'
    },
    1056781: {
        'access': 'read-write',
        'name': 'CCDF_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1056782: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_MEAN_POWER',
        'type': 'float64'
    },
    1056783: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_MEAN_POWER_PERCENTILE',
        'type': 'float64'
    },
    1056784: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_TEN_PERCENT_POWER',
        'type': 'float64'
    },
    1056785: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_ONE_PERCENT_POWER',
        'type': 'float64'
    },
    1056786: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_ONE_TENTH_PERCENT_POWER',
        'type': 'float64'
    },
    1056787: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_ONE_HUNDREDTH_PERCENT_POWER',
        'type': 'float64'
    },
    1056788: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWER',
        'type': 'float64'
    },
    1056789: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_ONE_TEN_THOUSANDTH_PERCENT_POWER',
        'type': 'float64'
    },
    1056790: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_PEAK_POWER',
        'type': 'float64'
    },
    1056791: {
        'access': 'read-write',
        'name': 'CCDF_RESULTS_MEASURED_SAMPLES_COUNT',
        'type': 'int32'
    },
    1060864: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1060866: {
        'access': 'read-write',
        'name': 'CHP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1060867: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1060868: {
        'access': 'read-write',
        'name': 'CHP_SPAN',
        'type': 'float64'
    },
    1060870: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    1060871: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1060873: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    1060874: {
        'access': 'read-write',
        'enum': 'ChpFftWindow',
        'name': 'CHP_FFT_WINDOW',
        'type': 'int32'
    },
    1060875: {
        'access': 'read-write',
        'name': 'CHP_FFT_PADDING',
        'type': 'float64'
    },
    1060876: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1060877: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1060878: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1060879: {
        'access': 'read-write',
        'enum': 'ChpCarrierRrcFilterEnabled',
        'name': 'CHP_CARRIER_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    1060880: {
        'access': 'read-write',
        'name': 'CHP_CARRIER_RRC_FILTER_ALPHA',
        'type': 'float64'
    },
    1060881: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1060882: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1060883: {
        'access': 'read-write',
        'enum': 'ChpDetectorType',
        'name': 'CHP_DETECTOR_TYPE',
        'type': 'int32'
    },
    1060884: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1060885: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1060886: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_PSD',
        'type': 'float64'
    },
    1060887: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_FREQUENCY_RESOLUTION',
        'type': 'float64'
    },
    1060888: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1060889: {
        'access': 'read-write',
        'name': 'CHP_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1060890: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    1060891: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1060892: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1060893: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    1060894: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterBandwidthDefinition',
        'name': 'CHP_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1060895: {
        'access': 'read-write',
        'enum': 'ChpAmplitudeCorrectionType',
        'name': 'CHP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1060896: {
        'access': 'read-write',
        'enum': 'ChpMeasurementMode',
        'name': 'CHP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    1060897: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationEnabled',
        'name': 'CHP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1060898: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationType',
        'name': 'CHP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    1060899: {
        'access': 'read-write',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    1060900: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationAveragingAuto',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    1060901: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationMode',
        'name': 'CHP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    1060902: {
        'access': 'read-write',
        'name': 'CHP_DETECTOR_POINTS',
        'type': 'int32'
    },
    1064960: {
        'access': 'read-write',
        'name': 'FCNT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1064962: {
        'access': 'read-write',
        'name': 'FCNT_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1064963: {
        'access': 'read-write',
        'name': 'FCNT_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1064965: {
        'access': 'read-write',
        'name': 'FCNT_AVERAGING_COUNT',
        'type': 'int32'
    },
    1064966: {
        'access': 'read-write',
        'enum': 'FcntAveragingEnabled',
        'name': 'FCNT_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1064968: {
        'access': 'read-write',
        'enum': 'FcntAveragingType',
        'name': 'FCNT_AVERAGING_TYPE',
        'type': 'int32'
    },
    1064969: {
        'access': 'read-write',
        'name': 'FCNT_RBW_FILTER_RRC_ALPHA',
        'type': 'float64'
    },
    1064970: {
        'access': 'read-write',
        'name': 'FCNT_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1064971: {
        'access': 'read-write',
        'enum': 'FcntRbwFilterType',
        'name': 'FCNT_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1064972: {
        'access': 'read-write',
        'enum': 'FcntThresholdEnabled',
        'name': 'FCNT_THRESHOLD_ENABLED',
        'type': 'int32'
    },
    1064973: {
        'access': 'read-write',
        'name': 'FCNT_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    1064974: {
        'access': 'read-write',
        'enum': 'FcntThresholdType',
        'name': 'FCNT_THRESHOLD_TYPE',
        'type': 'int32'
    },
    1064976: {
        'access': 'read-write',
        'name': 'FCNT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1064977: {
        'access': 'read-write',
        'name': 'FCNT_RESULTS_AVERAGE_RELATIVE_FREQUENCY',
        'type': 'float64'
    },
    1064978: {
        'access': 'read-write',
        'name': 'FCNT_RESULTS_MEAN_PHASE',
        'type': 'float64'
    },
    1064979: {
        'access': 'read-write',
        'name': 'FCNT_RESULTS_AVERAGE_ABSOLUTE_FREQUENCY',
        'type': 'float64'
    },
    1064980: {
        'access': 'read-write',
        'name': 'FCNT_RESULTS_ALLAN_DEVIATION',
        'type': 'float64'
    },
    1069056: {
        'access': 'read-write',
        'name': 'HARM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1069058: {
        'access': 'read-write',
        'name': 'HARM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1069059: {
        'access': 'read-write',
        'name': 'HARM_FUNDAMENTAL_RBW_FILTER_ALPHA',
        'type': 'float64'
    },
    1069060: {
        'access': 'read-write',
        'name': 'HARM_FUNDAMENTAL_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1069061: {
        'access': 'read-write',
        'enum': 'HarmRbwFilterType',
        'name': 'HARM_FUNDAMENTAL_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1069062: {
        'access': 'read-write',
        'name': 'HARM_FUNDAMENTAL_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1069063: {
        'access': 'read-write',
        'name': 'HARM_NUMBER_OF_HARMONICS',
        'type': 'int32'
    },
    1069064: {
        'access': 'read-write',
        'enum': 'HarmAutoHarmonicsSetupEnabled',
        'name': 'HARM_AUTO_SETUP_ENABLED',
        'type': 'int32'
    },
    1069065: {
        'access': 'read-write',
        'enum': 'HarmHarmonicEnabled',
        'name': 'HARM_HARMONIC_ENABLED',
        'type': 'int32'
    },
    1069066: {
        'access': 'read-write',
        'name': 'HARM_HARMONIC_ORDER',
        'type': 'int32'
    },
    1069067: {
        'access': 'read-write',
        'name': 'HARM_HARMONIC_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1069068: {
        'access': 'read-write',
        'name': 'HARM_AVERAGING_COUNT',
        'type': 'int32'
    },
    1069069: {
        'access': 'read-write',
        'enum': 'HarmAveragingEnabled',
        'name': 'HARM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1069071: {
        'access': 'read-write',
        'enum': 'HarmAveragingType',
        'name': 'HARM_AVERAGING_TYPE',
        'type': 'int32'
    },
    1069072: {
        'access': 'read-write',
        'name': 'HARM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1069073: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_FUNDAMENTAL_FREQUENCY',
        'type': 'float64'
    },
    1069074: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_AVERAGE_FUNDAMENTAL_POWER',
        'type': 'float64'
    },
    1069075: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_TOTAL_HARMONIC_DISTORTION',
        'type': 'float64'
    },
    1069076: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_HARMONIC_FREQUENCY',
        'type': 'float64'
    },
    1069077: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_HARMONIC_RBW',
        'type': 'float64'
    },
    1069078: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_HARMONIC_AVERAGE_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1069079: {
        'access': 'read-write',
        'name': 'HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER',
        'type': 'float64'
    },
    1069080: {
        'access': 'read-write',
        'name': 'HARM_HARMONIC_BANDWIDTH',
        'type': 'float64'
    },
    1069082: {
        'access': 'read-write',
        'enum': 'HarmMeasurementMethod',
        'name': 'HARM_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    1069083: {
        'access': 'read-write',
        'enum': 'HarmNoiseCompensationEnabled',
        'name': 'HARM_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1073152: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1073154: {
        'access': 'read-write',
        'name': 'OBW_BANDWIDTH_PERCENTAGE',
        'type': 'float64'
    },
    1073155: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1073156: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    1073158: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    1073159: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1073161: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    1073162: {
        'access': 'read-write',
        'enum': 'ObwFftWindow',
        'name': 'OBW_FFT_WINDOW',
        'type': 'int32'
    },
    1073163: {
        'access': 'read-write',
        'name': 'OBW_FFT_PADDING',
        'type': 'float64'
    },
    1073164: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1073165: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1073166: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1073167: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1073168: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1073170: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1073171: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    1073172: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_AVERAGE_POWER',
        'type': 'float64'
    },
    1073173: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    1073174: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    1073175: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_FREQUENCY_RESOLUTION',
        'type': 'float64'
    },
    1073176: {
        'access': 'read-write',
        'enum': 'ObwPowerUnits',
        'name': 'OBW_POWER_UNITS',
        'type': 'int32'
    },
    1073177: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterBandwidthDefinition',
        'name': 'OBW_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1073178: {
        'access': 'read-write',
        'enum': 'ObwAmplitudeCorrectionType',
        'name': 'OBW_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1077248: {
        'access': 'read-write',
        'name': 'PAVT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1077250: {
        'access': 'read-write',
        'enum': 'PavtMeasurementLocationType',
        'name': 'PAVT_MEASUREMENT_LOCATION_TYPE',
        'type': 'int32'
    },
    1077251: {
        'access': 'read-write',
        'name': 'PAVT_NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    1077252: {
        'access': 'read-write',
        'name': 'PAVT_SEGMENT_START_TIME',
        'type': 'float64'
    },
    1077253: {
        'access': 'read-write',
        'name': 'PAVT_MEASUREMENT_OFFSET',
        'type': 'float64'
    },
    1077254: {
        'access': 'read-write',
        'name': 'PAVT_MEASUREMENT_LENGTH',
        'type': 'float64'
    },
    1077255: {
        'access': 'read-write',
        'name': 'PAVT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1077258: {
        'access': 'read-write',
        'name': 'PAVT_RESULTS_MEAN_RELATIVE_PHASE',
        'type': 'float64'
    },
    1077259: {
        'access': 'read-write',
        'name': 'PAVT_RESULTS_MEAN_RELATIVE_AMPLITUDE',
        'type': 'float64'
    },
    1077260: {
        'access': 'read-write',
        'enum': 'PavtFrequencyOffsetCorrectionEnabled',
        'name': 'PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    1077261: {
        'access': 'read-write',
        'name': 'PAVT_MEASUREMENT_BANDWIDTH',
        'type': 'float64'
    },
    1077262: {
        'access': 'read-write',
        'name': 'PAVT_RESULTS_MEAN_ABSOLUTE_AMPLITUDE',
        'type': 'float64'
    },
    1077263: {
        'access': 'read-write',
        'name': 'PAVT_RESULTS_MEAN_ABSOLUTE_PHASE',
        'type': 'float64'
    },
    1077264: {
        'access': 'read-write',
        'enum': 'PavtSegmentType',
        'name': 'PAVT_SEGMENT_TYPE',
        'type': 'int32'
    },
    1077265: {
        'access': 'read-write',
        'name': 'PAVT_SEGMENT_MEASUREMENT_OFFSET',
        'type': 'float64'
    },
    1077266: {
        'access': 'read-write',
        'name': 'PAVT_SEGMENT_MEASUREMENT_LENGTH',
        'type': 'float64'
    },
    1077267: {
        'access': 'read-write',
        'enum': 'PavtPhaseUnwrapEnabled',
        'name': 'PAVT_PHASE_UNWRAP_ENABLED',
        'type': 'int32'
    },
    1077268: {
        'access': 'read-write',
        'name': 'PAVT_RESULTS_FREQUENCY_ERROR_MEAN',
        'type': 'float64'
    },
    1077269: {
        'access': 'read-write',
        'enum': 'PavtMeasurementIntervalMode',
        'name': 'PAVT_MEASUREMENT_INTERVAL_MODE',
        'type': 'int32'
    },
    1077270: {
        'access': 'read-write',
        'enum': 'PavtFrequencyTrackingEnabled',
        'name': 'PAVT_FREQUENCY_TRACKING_ENABLED',
        'type': 'int32'
    },
    1081344: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1081346: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1081347: {
        'access': 'read-write',
        'enum': 'SemCarrierEnabled',
        'name': 'SEM_CARRIER_ENABLED',
        'type': 'int32'
    },
    1081348: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1081349: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1081350: {
        'access': 'read-write',
        'enum': 'SemCarrierRbwAutoBandwidth',
        'name': 'SEM_CARRIER_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1081351: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1081352: {
        'access': 'read-write',
        'enum': 'SemCarrierRbwFilterType',
        'name': 'SEM_CARRIER_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1081353: {
        'access': 'read-write',
        'enum': 'SemCarrierRrcFilterEnabled',
        'name': 'SEM_CARRIER_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    1081354: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_RRC_FILTER_ALPHA',
        'type': 'float64'
    },
    1081355: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    1081356: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    1081357: {
        'access': 'read-write',
        'enum': 'SemOffsetLimitFailMask',
        'name': 'SEM_OFFSET_LIMIT_FAIL_MASK',
        'type': 'int32'
    },
    1081358: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_ATTENUATION',
        'type': 'float64'
    },
    1081359: {
        'access': 'read-write',
        'enum': 'SemOffsetAbsoluteLimitMode',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_MODE',
        'type': 'int32'
    },
    1081360: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_START',
        'type': 'float64'
    },
    1081361: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_STOP',
        'type': 'float64'
    },
    1081362: {
        'access': 'read-write',
        'enum': 'SemOffsetEnabled',
        'name': 'SEM_OFFSET_ENABLED',
        'type': 'int32'
    },
    1081363: {
        'access': 'read-write',
        'enum': 'SemOffsetSideband',
        'name': 'SEM_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    1081364: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    1081365: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    1081366: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwAutoBandwidth',
        'name': 'SEM_OFFSET_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1081367: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1081368: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1081369: {
        'access': 'read-write',
        'enum': 'SemOffsetRelativeLimitMode',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_MODE',
        'type': 'int32'
    },
    1081370: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_START',
        'type': 'float64'
    },
    1081371: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_STOP',
        'type': 'float64'
    },
    1081372: {
        'access': 'read-write',
        'enum': 'SemPowerUnits',
        'name': 'SEM_POWER_UNITS',
        'type': 'int32'
    },
    1081373: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1081374: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    1081375: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1081377: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    1081378: {
        'access': 'read-write',
        'enum': 'SemFftWindow',
        'name': 'SEM_FFT_WINDOW',
        'type': 'int32'
    },
    1081379: {
        'access': 'read-write',
        'name': 'SEM_FFT_PADDING',
        'type': 'float64'
    },
    1081380: {
        'access': 'read-write',
        'enum': 'SemReferenceType',
        'name': 'SEM_REFERENCE_TYPE',
        'type': 'int32'
    },
    1081381: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1081382: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1081383: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1081384: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    1081385: {
        'access': 'read-write',
        'enum': 'SemCompositeMeasurementStatus',
        'name': 'SEM_RESULTS_COMPOSITE_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    1081386: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_FREQUENCY_RESOLUTION',
        'type': 'float64'
    },
    1081387: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1081388: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    1081389: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081390: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_TOTAL_RELATIVE_POWER',
        'type': 'float64'
    },
    1081391: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_PEAK_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081392: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_PEAK_FREQUENCY',
        'type': 'float64'
    },
    1081393: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    1081394: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    1081395: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1081396: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_TOTAL_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081397: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_TOTAL_RELATIVE_POWER',
        'type': 'float64'
    },
    1081398: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081399: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_RELATIVE_POWER',
        'type': 'float64'
    },
    1081400: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    1081401: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    1081402: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081403: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    1081404: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    1081405: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    1081406: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    1081407: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    1081408: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    1081409: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_TOTAL_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081410: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_TOTAL_RELATIVE_POWER',
        'type': 'float64'
    },
    1081411: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081412: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_RELATIVE_POWER',
        'type': 'float64'
    },
    1081413: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    1081414: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    1081415: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1081416: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    1081417: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    1081418: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    1081419: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    1081420: {
        'access': 'read-write',
        'enum': 'SemOffsetFrequencyDefinition',
        'name': 'SEM_OFFSET_FREQUENCY_DEFINITION',
        'type': 'int32'
    },
    1081421: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterBandwidthDefinition',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1081422: {
        'access': 'read-write',
        'enum': 'SemCarrierRbwFilterBandwidthDefinition',
        'name': 'SEM_CARRIER_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1081423: {
        'access': 'read-write',
        'enum': 'SemAmplitudeCorrectionType',
        'name': 'SEM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1085440: {
        'access': 'read-write',
        'name': 'SPECTRUM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1085442: {
        'access': 'read-write',
        'name': 'SPECTRUM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1085443: {
        'access': 'read-write',
        'name': 'SPECTRUM_SPAN',
        'type': 'float64'
    },
    1085445: {
        'access': 'read-write',
        'name': 'SPECTRUM_AVERAGING_COUNT',
        'type': 'int32'
    },
    1085446: {
        'access': 'read-write',
        'enum': 'SpectrumAveragingEnabled',
        'name': 'SPECTRUM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1085448: {
        'access': 'read-write',
        'enum': 'SpectrumAveragingType',
        'name': 'SPECTRUM_AVERAGING_TYPE',
        'type': 'int32'
    },
    1085449: {
        'access': 'read-write',
        'enum': 'SpectrumFftWindow',
        'name': 'SPECTRUM_FFT_WINDOW',
        'type': 'int32'
    },
    1085450: {
        'access': 'read-write',
        'name': 'SPECTRUM_FFT_PADDING',
        'type': 'float64'
    },
    1085451: {
        'access': 'read-write',
        'enum': 'SpectrumRbwAutoBandwidth',
        'name': 'SPECTRUM_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1085452: {
        'access': 'read-write',
        'name': 'SPECTRUM_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1085453: {
        'access': 'read-write',
        'enum': 'SpectrumRbwFilterType',
        'name': 'SPECTRUM_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1085454: {
        'access': 'read-write',
        'enum': 'SpectrumSweepTimeAuto',
        'name': 'SPECTRUM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1085455: {
        'access': 'read-write',
        'name': 'SPECTRUM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1085456: {
        'access': 'read-write',
        'enum': 'SpectrumNoiseCompensationEnabled',
        'name': 'SPECTRUM_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1085458: {
        'access': 'read-write',
        'name': 'SPECTRUM_RESULTS_PEAK_AMPLITUDE',
        'type': 'float64'
    },
    1085459: {
        'access': 'read-write',
        'name': 'SPECTRUM_RESULTS_PEAK_FREQUENCY',
        'type': 'float64'
    },
    1085460: {
        'access': 'read-write',
        'name': 'SPECTRUM_RESULTS_FREQUENCY_RESOLUTION',
        'type': 'float64'
    },
    1085461: {
        'access': 'read-write',
        'enum': 'SpectrumPowerUnits',
        'name': 'SPECTRUM_POWER_UNITS',
        'type': 'int32'
    },
    1085462: {
        'access': 'read-write',
        'enum': 'SpectrumRbwFilterBandwidthDefinition',
        'name': 'SPECTRUM_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1085463: {
        'access': 'read-write',
        'enum': 'SpectrumAmplitudeCorrectionType',
        'name': 'SPECTRUM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1085464: {
        'access': 'read-write',
        'enum': 'SpectrumDetectorType',
        'name': 'SPECTRUM_DETECTOR_TYPE',
        'type': 'int32'
    },
    1085465: {
        'access': 'read-write',
        'name': 'SPECTRUM_DETECTOR_POINTS',
        'type': 'int32'
    },
    1085466: {
        'access': 'read-write',
        'enum': 'SpectrumVbwFilterAutoBandwidth',
        'name': 'SPECTRUM_VBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1085467: {
        'access': 'read-write',
        'name': 'SPECTRUM_VBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1085468: {
        'access': 'read-write',
        'name': 'SPECTRUM_VBW_FILTER_VBW_TO_RBW_RATIO',
        'type': 'float64'
    },
    1085470: {
        'access': 'read-write',
        'enum': 'SpectrumMeasurementMode',
        'name': 'SPECTRUM_MEASUREMENT_MODE',
        'type': 'int32'
    },
    1085471: {
        'access': 'read-write',
        'enum': 'SpectrumNoiseCompensationType',
        'name': 'SPECTRUM_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    1085472: {
        'access': 'read-write',
        'name': 'SPECTRUM_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    1085473: {
        'access': 'read-write',
        'enum': 'SpectrumNoiseCalibrationAveragingAuto',
        'name': 'SPECTRUM_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    1085474: {
        'access': 'read-write',
        'enum': 'SpectrumNoiseCalibrationMode',
        'name': 'SPECTRUM_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    1085475: {
        'access': 'read-write',
        'enum': 'SpectrumAnalysisInput',
        'name': 'SPECTRUM_ANALYSIS_INPUT',
        'type': 'int32'
    },
    1085476: {
        'access': 'read-write',
        'enum': 'SpectrumFftOverlapMode',
        'name': 'SPECTRUM_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    1085477: {
        'access': 'read-write',
        'name': 'SPECTRUM_FFT_OVERLAP',
        'type': 'float64'
    },
    1085478: {
        'access': 'read-write',
        'enum': 'SpectrumFftOverlapType',
        'name': 'SPECTRUM_FFT_OVERLAP_TYPE',
        'type': 'int32'
    },
    1085479: {
        'access': 'read-write',
        'enum': 'SpectrumMeasurementMethod',
        'name': 'SPECTRUM_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    1085480: {
        'access': 'read-write',
        'name': 'SPECTRUM_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    1089536: {
        'access': 'read-write',
        'name': 'SPUR_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1089539: {
        'access': 'read-write',
        'name': 'SPUR_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1089540: {
        'access': 'read-write',
        'name': 'SPUR_NUMBER_OF_RANGES',
        'type': 'int32'
    },
    1089541: {
        'access': 'read-write',
        'enum': 'SpurRangeEnabled',
        'name': 'SPUR_RANGE_ENABLED',
        'type': 'int32'
    },
    1089542: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_RELATIVE_ATTENUATION',
        'type': 'float64'
    },
    1089543: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_NUMBER_OF_SPURS_TO_REPORT',
        'type': 'int32'
    },
    1089544: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_START_FREQUENCY',
        'type': 'float64'
    },
    1089545: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_STOP_FREQUENCY',
        'type': 'float64'
    },
    1089546: {
        'access': 'read-write',
        'name': 'SPUR_AVERAGING_COUNT',
        'type': 'int32'
    },
    1089547: {
        'access': 'read-write',
        'enum': 'SpurAveragingEnabled',
        'name': 'SPUR_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1089549: {
        'access': 'read-write',
        'enum': 'SpurAveragingType',
        'name': 'SPUR_AVERAGING_TYPE',
        'type': 'int32'
    },
    1089551: {
        'access': 'read-write',
        'enum': 'SpurFftWindow',
        'name': 'SPUR_FFT_WINDOW',
        'type': 'int32'
    },
    1089552: {
        'access': 'read-write',
        'enum': 'SpurAbsoluteLimitMode',
        'name': 'SPUR_RANGE_ABSOLUTE_LIMIT_MODE',
        'type': 'int32'
    },
    1089553: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_ABSOLUTE_LIMIT_START',
        'type': 'float64'
    },
    1089554: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_ABSOLUTE_LIMIT_STOP',
        'type': 'float64'
    },
    1089555: {
        'access': 'read-write',
        'enum': 'SpurRbwAutoBandwidth',
        'name': 'SPUR_RANGE_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1089556: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1089557: {
        'access': 'read-write',
        'enum': 'SpurRbwFilterType',
        'name': 'SPUR_RANGE_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1089558: {
        'access': 'read-write',
        'enum': 'SpurSweepTimeAuto',
        'name': 'SPUR_RANGE_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1089559: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1089560: {
        'access': 'read-write',
        'name': 'SPUR_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1089561: {
        'access': 'read-write',
        'enum': 'SpurMeasurementStatus',
        'name': 'SPUR_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    1089562: {
        'access': 'read-write',
        'name': 'SPUR_RESULTS_RANGE_FREQUENCY',
        'type': 'float64'
    },
    1089563: {
        'access': 'read-write',
        'name': 'SPUR_RESULTS_RANGE_AMPLITUDE',
        'type': 'float64'
    },
    1089564: {
        'access': 'read-write',
        'name': 'SPUR_RESULTS_RANGE_ABSOLUTE_LIMIT',
        'type': 'float64'
    },
    1089565: {
        'access': 'read-write',
        'name': 'SPUR_RESULTS_RANGE_MARGIN',
        'type': 'float64'
    },
    1089566: {
        'access': 'read-write',
        'enum': 'SpurRangeStatus',
        'name': 'SPUR_RESULTS_RANGE_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    1089567: {
        'access': 'read-write',
        'name': 'SPUR_RESULTS_RANGE_NUMBER_OF_DETECTED_SPURS',
        'type': 'int32'
    },
    1089568: {
        'access': 'read-write',
        'name': 'SPUR_TRACE_RANGE_INDEX',
        'type': 'int32'
    },
    1089569: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_PEAK_THRESHOLD',
        'type': 'float64'
    },
    1089570: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_PEAK_EXCURSION',
        'type': 'float64'
    },
    1089571: {
        'access': 'read-write',
        'enum': 'SpurRbwFilterBandwidthDefinition',
        'name': 'SPUR_RANGE_RBW_FILTER_BANDWIDTH_DEFINITION',
        'type': 'int32'
    },
    1089572: {
        'access': 'read-write',
        'enum': 'SpurAmplitudeCorrectionType',
        'name': 'SPUR_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1089573: {
        'access': 'read-write',
        'enum': 'SpurRangeDetectorType',
        'name': 'SPUR_RANGE_DETECTOR_TYPE',
        'type': 'int32'
    },
    1089574: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_DETECTOR_POINTS',
        'type': 'int32'
    },
    1089575: {
        'access': 'read-write',
        'enum': 'SpurRangeVbwFilterAutoBandwidth',
        'name': 'SPUR_RANGE_VBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1089576: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_VBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1089577: {
        'access': 'read-write',
        'name': 'SPUR_RANGE_VBW_FILTER_VBW_TO_RBW_RATIO',
        'type': 'float64'
    },
    1093632: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1093634: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1093635: {
        'access': 'read-write',
        'name': 'TXP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1093637: {
        'access': 'read-write',
        'name': 'TXP_AVERAGING_COUNT',
        'type': 'int32'
    },
    1093638: {
        'access': 'read-write',
        'enum': 'TxpAveragingEnabled',
        'name': 'TXP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1093640: {
        'access': 'read-write',
        'enum': 'TxpAveragingType',
        'name': 'TXP_AVERAGING_TYPE',
        'type': 'int32'
    },
    1093641: {
        'access': 'read-write',
        'name': 'TXP_RBW_FILTER_ALPHA',
        'type': 'float64'
    },
    1093642: {
        'access': 'read-write',
        'name': 'TXP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1093643: {
        'access': 'read-write',
        'enum': 'TxpRbwFilterType',
        'name': 'TXP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1093644: {
        'access': 'read-write',
        'enum': 'TxpThresholdEnabled',
        'name': 'TXP_THRESHOLD_ENABLED',
        'type': 'int32'
    },
    1093645: {
        'access': 'read-write',
        'name': 'TXP_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    1093646: {
        'access': 'read-write',
        'enum': 'TxpThresholdType',
        'name': 'TXP_THRESHOLD_TYPE',
        'type': 'int32'
    },
    1093648: {
        'access': 'read-write',
        'name': 'TXP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1093649: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_MEAN_POWER',
        'type': 'float64'
    },
    1093650: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_TO_AVERAGE_RATIO',
        'type': 'float64'
    },
    1093651: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_MAXIMUM_POWER',
        'type': 'float64'
    },
    1093652: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_MINIMUM_POWER',
        'type': 'float64'
    },
    1093655: {
        'access': 'read-write',
        'enum': 'TxpVbwFilterAutoBandwidth',
        'name': 'TXP_VBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1093656: {
        'access': 'read-write',
        'name': 'TXP_VBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1093657: {
        'access': 'read-write',
        'name': 'TXP_VBW_FILTER_VBW_TO_RBW_RATIO',
        'type': 'float64'
    },
    1097728: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    1105920: {
        'access': 'read-write',
        'name': 'AMPM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1105922: {
        'access': 'read-write',
        'name': 'AMPM_AM_TO_AM_CURVE_FIT_ORDER',
        'type': 'int32'
    },
    1105923: {
        'access': 'read-write',
        'enum': 'AmpmAMToAMCurveFitType',
        'name': 'AMPM_AM_TO_AM_CURVE_FIT_TYPE',
        'type': 'int32'
    },
    1105924: {
        'access': 'read-write',
        'name': 'AMPM_AM_TO_PM_CURVE_FIT_ORDER',
        'type': 'int32'
    },
    1105925: {
        'access': 'read-write',
        'enum': 'AmpmAMToPMCurveFitType',
        'name': 'AMPM_AM_TO_PM_CURVE_FIT_TYPE',
        'type': 'int32'
    },
    1105926: {
        'access': 'read-write',
        'enum': 'AmpmAveragingEnabled',
        'name': 'AMPM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1105927: {
        'access': 'read-write',
        'name': 'AMPM_AVERAGING_COUNT',
        'type': 'int32'
    },
    1105929: {
        'access': 'read-write',
        'name': 'AMPM_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1105930: {
        'access': 'read-write',
        'enum': 'AmpmSignalType',
        'name': 'AMPM_SIGNAL_TYPE',
        'type': 'int32'
    },
    1105931: {
        'access': 'read-write',
        'enum': 'AmpmMeasurementSampleRateMode',
        'name': 'AMPM_MEASUREMENT_SAMPLE_RATE_MODE',
        'type': 'int32'
    },
    1105932: {
        'access': 'read-write',
        'name': 'AMPM_MEASUREMENT_SAMPLE_RATE',
        'type': 'float64'
    },
    1105933: {
        'access': 'read-write',
        'enum': 'AmpmThresholdEnabled',
        'name': 'AMPM_THRESHOLD_ENABLED',
        'type': 'int32'
    },
    1105934: {
        'access': 'read-write',
        'enum': 'AmpmThresholdType',
        'name': 'AMPM_THRESHOLD_TYPE',
        'type': 'int32'
    },
    1105935: {
        'access': 'read-write',
        'name': 'AMPM_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    1105936: {
        'access': 'read-write',
        'name': 'AMPM_DUT_AVERAGE_INPUT_POWER',
        'type': 'float64'
    },
    1105937: {
        'access': 'read-write',
        'name': 'AMPM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1105938: {
        'access': 'read-write',
        'name': 'AMPM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1105940: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_AM_TO_AM_CURVE_FIT_COEFFICIENTS',
        'type': 'float32[]'
    },
    1105941: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_AM_TO_PM_CURVE_FIT_COEFFICIENTS',
        'type': 'float32[]'
    },
    1105942: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_MEAN_LINEAR_GAIN',
        'type': 'float64'
    },
    1105943: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_MEAN_PHASE_ERROR',
        'type': 'float64'
    },
    1105944: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_MEAN_RMS_EVM',
        'type': 'float64'
    },
    1105945: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUAL',
        'type': 'float64'
    },
    1105946: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUAL',
        'type': 'float64'
    },
    1105947: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_GAIN_ERROR_RANGE',
        'type': 'float64'
    },
    1105948: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_PHASE_ERROR_RANGE',
        'type': 'float64'
    },
    1105949: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_1_DB_COMPRESSION_POINT',
        'type': 'float64'
    },
    1105953: {
        'access': 'read-write',
        'enum': 'AmpmFrequencyOffsetCorrectionEnabled',
        'name': 'AMPM_FREQUENCY_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    1105954: {
        'access': 'read-write',
        'name': 'AMPM_MAXIMUM_TIMING_ERROR',
        'type': 'float64'
    },
    1105955: {
        'access': 'read-write',
        'enum': 'AmpmReferencePowerType',
        'name': 'AMPM_REFERENCE_POWER_TYPE',
        'type': 'int32'
    },
    1105956: {
        'access': 'read-write',
        'enum': 'AmpmCompressionPointEnabled',
        'name': 'AMPM_COMPRESSION_POINT_ENABLED',
        'type': 'int32'
    },
    1105957: {
        'access': 'read-write',
        'name': 'AMPM_COMPRESSION_POINT_LEVEL',
        'type': 'float64[]'
    },
    1105958: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_INPUT_COMPRESSION_POINT',
        'type': 'float64[]'
    },
    1105959: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_OUTPUT_COMPRESSION_POINT',
        'type': 'float64[]'
    },
    1105960: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_LOOKUP_TABLE_INPUT_POWER',
        'type': 'float32[]'
    },
    1105961: {
        'access': 'read-write',
        'enum': 'AmpmIQOriginOffsetCorrectionEnabled',
        'name': 'AMPM_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    1105962: {
        'access': 'read-write',
        'enum': 'AmpmSynchronizationMethod',
        'name': 'AMPM_SYNCHRONIZATION_METHOD',
        'type': 'int32'
    },
    1105963: {
        'access': 'read-write',
        'enum': 'AmpmAutoCarrierDetectionEnabled',
        'name': 'AMPM_AUTO_CARRIER_DETECTION_ENABLED',
        'type': 'int32'
    },
    1105964: {
        'access': 'read-write',
        'name': 'AMPM_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1105965: {
        'access': 'read-write',
        'name': 'AMPM_CARRIER_OFFSET',
        'type': 'float64'
    },
    1105966: {
        'access': 'read-write',
        'name': 'AMPM_CARRIER_BANDWIDTH',
        'type': 'float64'
    },
    1105967: {
        'access': 'read-write',
        'enum': 'AmpmEqualizerMode',
        'name': 'AMPM_EQUALIZER_MODE',
        'type': 'int32'
    },
    1105968: {
        'access': 'read-write',
        'name': 'AMPM_EQUALIZER_FILTER_LENGTH',
        'type': 'int32'
    },
    1105969: {
        'access': 'read-write',
        'enum': 'AmpmAMToAMEnabled',
        'name': 'AMPM_AM_TO_AM_ENABLED',
        'type': 'int32'
    },
    1105970: {
        'access': 'read-write',
        'enum': 'AmpmAMToPMEnabled',
        'name': 'AMPM_AM_TO_PM_ENABLED',
        'type': 'int32'
    },
    1105971: {
        'access': 'read-write',
        'enum': 'AmpmEvmEnabled',
        'name': 'AMPM_EVM_ENABLED',
        'type': 'int32'
    },
    1105972: {
        'access': 'read-write',
        'enum': 'AmpmCompressionPointGainReference',
        'name': 'AMPM_COMPRESSION_POINT_GAIN_REFERENCE',
        'type': 'int32'
    },
    1105973: {
        'access': 'read-write',
        'name': 'AMPM_COMPRESSION_POINT_GAIN_REFERENCE_POWER',
        'type': 'float64'
    },
    1105974: {
        'access': 'read-write',
        'name': 'AMPM_COMPRESSION_POINT_USER_GAIN',
        'type': 'float64'
    },
    1105975: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_COMPRESSION_POINT_GAIN_REFERENCE',
        'type': 'float64'
    },
    1105976: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_PEAK_REFERENCE_POWER',
        'type': 'float64'
    },
    1105977: {
        'access': 'read-write',
        'name': 'AMPM_RESULTS_PEAK_REFERENCE_POWER_GAIN',
        'type': 'float64'
    },
    1105980: {
        'access': 'read-write',
        'enum': 'AmpmThresholdDefinition',
        'name': 'AMPM_THRESHOLD_DEFINITION',
        'type': 'int32'
    },
    1110016: {
        'access': 'read-write',
        'name': 'DPD_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1110018: {
        'access': 'read-write',
        'enum': 'DpdMeasurementSampleRateMode',
        'name': 'DPD_MEASUREMENT_SAMPLE_RATE_MODE',
        'type': 'int32'
    },
    1110019: {
        'access': 'read-write',
        'name': 'DPD_MEASUREMENT_SAMPLE_RATE',
        'type': 'float64'
    },
    1110020: {
        'access': 'read-write',
        'name': 'DPD_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1110021: {
        'access': 'read-write',
        'enum': 'DpdSignalType',
        'name': 'DPD_SIGNAL_TYPE',
        'type': 'int32'
    },
    1110023: {
        'access': 'read-write',
        'name': 'DPD_DUT_AVERAGE_INPUT_POWER',
        'type': 'float64'
    },
    1110024: {
        'access': 'read-write',
        'enum': 'DpdModel',
        'name': 'DPD_MODEL',
        'type': 'int32'
    },
    1110025: {
        'access': 'read-write',
        'name': 'DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_ORDER',
        'type': 'int32'
    },
    1110026: {
        'access': 'read-write',
        'enum': 'DpdLookupTableAMToAMCurveFitType',
        'name': 'DPD_LOOKUP_TABLE_AM_TO_AM_CURVE_FIT_TYPE',
        'type': 'int32'
    },
    1110027: {
        'access': 'read-write',
        'name': 'DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDER',
        'type': 'int32'
    },
    1110028: {
        'access': 'read-write',
        'enum': 'DpdLookupTableAMToPMCurveFitType',
        'name': 'DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE',
        'type': 'int32'
    },
    1110029: {
        'access': 'read-write',
        'enum': 'DpdLookupTableThresholdEnabled',
        'name': 'DPD_LOOKUP_TABLE_THRESHOLD_ENABLED',
        'type': 'int32'
    },
    1110030: {
        'access': 'read-write',
        'enum': 'DpdLookupTableThresholdType',
        'name': 'DPD_LOOKUP_TABLE_THRESHOLD_TYPE',
        'type': 'int32'
    },
    1110031: {
        'access': 'read-write',
        'name': 'DPD_LOOKUP_TABLE_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    1110032: {
        'access': 'read-write',
        'name': 'DPD_LOOKUP_TABLE_STEP_SIZE',
        'type': 'float64'
    },
    1110033: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_ORDER',
        'type': 'int32'
    },
    1110034: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110035: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_LEAD_ORDER',
        'type': 'int32'
    },
    1110036: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_LAG_ORDER',
        'type': 'int32'
    },
    1110037: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_LEAD_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110038: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_LAG_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110039: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_MAXIMUM_LEAD',
        'type': 'int32'
    },
    1110040: {
        'access': 'read-write',
        'name': 'DPD_MEMORY_POLYNOMIAL_MAXIMUM_LAG',
        'type': 'int32'
    },
    1110042: {
        'access': 'read-write',
        'enum': 'DpdIterativeDpdEnabled',
        'name': 'DPD_ITERATIVE_DPD_ENABLED',
        'type': 'int32'
    },
    1110044: {
        'access': 'read-write',
        'enum': 'DpdAveragingEnabled',
        'name': 'DPD_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1110045: {
        'access': 'read-write',
        'name': 'DPD_AVERAGING_COUNT',
        'type': 'int32'
    },
    1110047: {
        'access': 'read-write',
        'name': 'DPD_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1110048: {
        'access': 'read-write',
        'name': 'DPD_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1110049: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdConfigurationInput',
        'name': 'DPD_APPLY_DPD_CONFIGURATION_INPUT',
        'type': 'int32'
    },
    1110050: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdLookupTableCorrectionType',
        'name': 'DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1110053: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_DUT_AVERAGE_INPUT_POWER',
        'type': 'float64'
    },
    1110054: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdUserDpdModel',
        'name': 'DPD_APPLY_DPD_USER_DPD_MODEL',
        'type': 'int32'
    },
    1110055: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEASUREMENT_SAMPLE_RATE',
        'type': 'float64'
    },
    1110058: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_ORDER',
        'type': 'int32'
    },
    1110059: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110060: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_LEAD_ORDER',
        'type': 'int32'
    },
    1110061: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_LAG_ORDER',
        'type': 'int32'
    },
    1110062: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_LEAD_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110063: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_LAG_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110064: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MAXIMUM_LEAD',
        'type': 'int32'
    },
    1110065: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MAXIMUM_LAG',
        'type': 'int32'
    },
    1110067: {
        'access': 'read-write',
        'name': 'DPD_RESULTS_AVERAGE_GAIN',
        'type': 'float64'
    },
    1110070: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdMemoryModelCorrectionType',
        'name': 'DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE',
        'type': 'int32'
    },
    1110071: {
        'access': 'read-write',
        'enum': 'DpdTargetGainType',
        'name': 'DPD_TARGET_GAIN_TYPE',
        'type': 'int32'
    },
    1110072: {
        'access': 'read-write',
        'enum': 'DpdLookupTableType',
        'name': 'DPD_LOOKUP_TABLE_TYPE',
        'type': 'int32'
    },
    1110073: {
        'access': 'read-write',
        'enum': 'DpdFrequencyOffsetCorrectionEnabled',
        'name': 'DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    1110074: {
        'access': 'read-write',
        'name': 'DPD_MAXIMUM_TIMING_ERROR',
        'type': 'float64'
    },
    1110075: {
        'access': 'read-write',
        'enum': 'DpdNmseEnabled',
        'name': 'DPD_NMSE_ENABLED',
        'type': 'int32'
    },
    1110076: {
        'access': 'read-write',
        'enum': 'DpdPreDpdCfrEnabled',
        'name': 'DPD_PRE_DPD_CFR_ENABLED',
        'type': 'int32'
    },
    1110077: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_MAXIMUM_ITERATIONS',
        'type': 'int32'
    },
    1110078: {
        'access': 'read-write',
        'enum': 'DpdPreDpdCfrMethod',
        'name': 'DPD_PRE_DPD_CFR_METHOD',
        'type': 'int32'
    },
    1110080: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdUserLookupTableType',
        'name': 'DPD_APPLY_DPD_USER_LOOKUP_TABLE_TYPE',
        'type': 'int32'
    },
    1110081: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_TARGET_PAPR',
        'type': 'float64'
    },
    1110082: {
        'access': 'read-write',
        'enum': 'DpdPreDpdCfrWindowType',
        'name': 'DPD_PRE_DPD_CFR_WINDOW_TYPE',
        'type': 'int32'
    },
    1110083: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_WINDOW_LENGTH',
        'type': 'int32'
    },
    1110084: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_SHAPING_FACTOR',
        'type': 'float64'
    },
    1110085: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_SHAPING_THRESHOLD',
        'type': 'float64'
    },
    1110086: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdCfrEnabled',
        'name': 'DPD_APPLY_DPD_CFR_ENABLED',
        'type': 'int32'
    },
    1110087: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdCfrMethod',
        'name': 'DPD_APPLY_DPD_CFR_METHOD',
        'type': 'int32'
    },
    1110088: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_CFR_MAXIMUM_ITERATIONS',
        'type': 'int32'
    },
    1110089: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdCfrTargetPaprType',
        'name': 'DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE',
        'type': 'int32'
    },
    1110090: {
        'access': 'read-write',
        'enum': 'DpdSynchronizationMethod',
        'name': 'DPD_SYNCHRONIZATION_METHOD',
        'type': 'int32'
    },
    1110091: {
        'access': 'read-write',
        'enum': 'DpdAutoCarrierDetectionEnabled',
        'name': 'DPD_AUTO_CARRIER_DETECTION_ENABLED',
        'type': 'int32'
    },
    1110092: {
        'access': 'read-write',
        'name': 'DPD_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1110093: {
        'access': 'read-write',
        'name': 'DPD_CARRIER_OFFSET',
        'type': 'float64'
    },
    1110094: {
        'access': 'read-write',
        'name': 'DPD_CARRIER_BANDWIDTH',
        'type': 'float64'
    },
    1110095: {
        'access': 'read-write',
        'enum': 'DpdMemoryPolynomialOrderType',
        'name': 'DPD_MEMORY_POLYNOMIAL_ORDER_TYPE',
        'type': 'int32'
    },
    1110096: {
        'access': 'read-write',
        'enum': 'DpdMemoryPolynomialLeadOrderType',
        'name': 'DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE',
        'type': 'int32'
    },
    1110097: {
        'access': 'read-write',
        'enum': 'DpdMemoryPolynomialLagOrderType',
        'name': 'DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE',
        'type': 'int32'
    },
    1110106: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_CFR_TARGET_PAPR',
        'type': 'float64'
    },
    1110107: {
        'access': 'read-write',
        'enum': 'DpdApplyDpdCfrWindowType',
        'name': 'DPD_APPLY_DPD_CFR_WINDOW_TYPE',
        'type': 'int32'
    },
    1110108: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_CFR_WINDOW_LENGTH',
        'type': 'int32'
    },
    1110109: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_CFR_SHAPING_FACTOR',
        'type': 'float64'
    },
    1110110: {
        'access': 'read-write',
        'name': 'DPD_APPLY_DPD_CFR_SHAPING_THRESHOLD',
        'type': 'float64'
    },
    1110111: {
        'access': 'read-write',
        'name': 'DPD_RESULTS_NMSE',
        'type': 'float64'
    },
    1110112: {
        'access': 'read-write',
        'enum': 'DpdPreDpdCfrFilterEnabled',
        'name': 'DPD_PRE_DPD_CFR_FILTER_ENABLED',
        'type': 'int32'
    },
    1110114: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CFR_NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    1110115: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CARRIER_OFFSET',
        'type': 'float64'
    },
    1110116: {
        'access': 'read-write',
        'name': 'DPD_PRE_DPD_CARRIER_BANDWIDTH',
        'type': 'float64'
    },
    1110117: {
        'access': 'read-write',
        'enum': 'DpdIQOriginOffsetCorrectionEnabled',
        'name': 'DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    1110119: {
        'access': 'read-write',
        'name': 'DPD_DVR_NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    1110120: {
        'access': 'read-write',
        'name': 'DPD_DVR_LINEAR_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110121: {
        'access': 'read-write',
        'name': 'DPD_DVR_NONLINEAR_MEMORY_DEPTH',
        'type': 'int32'
    },
    1110122: {
        'access': 'read-write',
        'enum': 'DpdDvrDdrEnabled',
        'name': 'DPD_DVR_DDR_ENABLED',
        'type': 'int32'
    },
    1110123: {
        'access': 'read-write',
        'enum': 'DpdMeasurementMode',
        'name': 'DPD_MEASUREMENT_MODE',
        'type': 'int32'
    },
    1110125: {
        'access': 'read-write',
        'enum': 'DpdLookupTableThresholdDefinition',
        'name': 'DPD_LOOKUP_TABLE_THRESHOLD_DEFINITION',
        'type': 'int32'
    },
    1110272: {
        'access': 'read-write',
        'name': 'IQ_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1110274: {
        'access': 'read-write',
        'name': 'IQ_SAMPLE_RATE',
        'type': 'float64'
    },
    1110275: {
        'access': 'read-write',
        'name': 'IQ_NUMBER_OF_RECORDS',
        'type': 'int32'
    },
    1110276: {
        'access': 'read-write',
        'name': 'IQ_ACQUISITION_TIME',
        'type': 'float64'
    },
    1110277: {
        'access': 'read-write',
        'name': 'IQ_PRETRIGGER_TIME',
        'type': 'float64'
    },
    1110280: {
        'access': 'read-write',
        'enum': 'IQBandwidthAuto',
        'name': 'IQ_BANDWIDTH_AUTO',
        'type': 'int32'
    },
    1110281: {
        'access': 'read-write',
        'name': 'IQ_BANDWIDTH',
        'type': 'float64'
    },
    1110282: {
        'access': 'read-write',
        'enum': 'IQDeleteRecordOnFetch',
        'name': 'IQ_DELETE_RECORD_ON_FETCH',
        'type': 'int32'
    },
    1110284: {
        'access': 'read-write',
        'enum': 'IQMeasurementMode',
        'name': 'IQ_MEASUREMENT_MODE',
        'type': 'int32'
    },
    1114112: {
        'access': 'read-write',
        'name': 'IM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1114114: {
        'access': 'read-write',
        'enum': 'IMFrequencyDefinition',
        'name': 'IM_FREQUENCY_DEFINITION',
        'type': 'int32'
    },
    1114115: {
        'access': 'read-write',
        'name': 'IM_FUNDAMENTAL_LOWER_TONE_FREQUENCY',
        'type': 'float64'
    },
    1114116: {
        'access': 'read-write',
        'name': 'IM_FUNDAMENTAL_UPPER_TONE_FREQUENCY',
        'type': 'float64'
    },
    1114117: {
        'access': 'read-write',
        'enum': 'IMAutoIntermodsSetupEnabled',
        'name': 'IM_AUTO_INTERMODS_SETUP_ENABLED',
        'type': 'int32'
    },
    1114118: {
        'access': 'read-write',
        'name': 'IM_MAXIMUM_INTERMOD_ORDER',
        'type': 'int32'
    },
    1114119: {
        'access': 'read-write',
        'name': 'IM_NUMBER_OF_INTERMODS',
        'type': 'int32'
    },
    1114120: {
        'access': 'read-write',
        'enum': 'IMIntermodEnabled',
        'name': 'IM_INTERMOD_ENABLED',
        'type': 'int32'
    },
    1114121: {
        'access': 'read-write',
        'name': 'IM_INTERMOD_ORDER',
        'type': 'int32'
    },
    1114122: {
        'access': 'read-write',
        'enum': 'IMIntermodSide',
        'name': 'IM_INTERMOD_SIDE',
        'type': 'int32'
    },
    1114123: {
        'access': 'read-write',
        'name': 'IM_LOWER_INTERMOD_FREQUENCY',
        'type': 'float64'
    },
    1114124: {
        'access': 'read-write',
        'name': 'IM_UPPER_INTERMOD_FREQUENCY',
        'type': 'float64'
    },
    1114125: {
        'access': 'read-write',
        'enum': 'IMMeasurementMethod',
        'name': 'IM_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    1114126: {
        'access': 'read-write',
        'enum': 'IMRbwFilterAutoBandwidth',
        'name': 'IM_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    1114127: {
        'access': 'read-write',
        'name': 'IM_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    1114128: {
        'access': 'read-write',
        'enum': 'IMRbwFilterType',
        'name': 'IM_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    1114129: {
        'access': 'read-write',
        'enum': 'IMSweepTimeAuto',
        'name': 'IM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    1114130: {
        'access': 'read-write',
        'name': 'IM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    1114131: {
        'access': 'read-write',
        'enum': 'IMAveragingEnabled',
        'name': 'IM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1114132: {
        'access': 'read-write',
        'name': 'IM_AVERAGING_COUNT',
        'type': 'int32'
    },
    1114134: {
        'access': 'read-write',
        'enum': 'IMAveragingType',
        'name': 'IM_AVERAGING_TYPE',
        'type': 'int32'
    },
    1114135: {
        'access': 'read-write',
        'enum': 'IMFftWindow',
        'name': 'IM_FFT_WINDOW',
        'type': 'int32'
    },
    1114136: {
        'access': 'read-write',
        'name': 'IM_FFT_PADDING',
        'type': 'float64'
    },
    1114137: {
        'access': 'read-write',
        'enum': 'IMIFOutputPowerOffsetAuto',
        'name': 'IM_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    1114138: {
        'access': 'read-write',
        'name': 'IM_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    1114139: {
        'access': 'read-write',
        'name': 'IM_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    1114140: {
        'access': 'read-write',
        'name': 'IM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1114141: {
        'access': 'read-write',
        'name': 'IM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1114143: {
        'access': 'read-write',
        'name': 'IM_RESULTS_LOWER_TONE_POWER',
        'type': 'float64'
    },
    1114145: {
        'access': 'read-write',
        'name': 'IM_RESULTS_UPPER_TONE_POWER',
        'type': 'float64'
    },
    1114146: {
        'access': 'read-write',
        'name': 'IM_RESULTS_INTERMOD_ORDER',
        'type': 'int32'
    },
    1114148: {
        'access': 'read-write',
        'name': 'IM_RESULTS_LOWER_INTERMOD_POWER',
        'type': 'float64'
    },
    1114150: {
        'access': 'read-write',
        'name': 'IM_RESULTS_UPPER_INTERMOD_POWER',
        'type': 'float64'
    },
    1114151: {
        'access': 'read-write',
        'name': 'IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER',
        'type': 'float64'
    },
    1114152: {
        'access': 'read-write',
        'name': 'IM_RESULTS_UPPER_OUTPUT_INTERCEPT_POWER',
        'type': 'float64'
    },
    1114153: {
        'access': 'read-write',
        'name': 'IM_RESULTS_WORST_CASE_OUTPUT_INTERCEPT_POWER',
        'type': 'float64'
    },
    1114154: {
        'access': 'read-write',
        'enum': 'IMLocalPeakSearchEnabled',
        'name': 'IM_LOCAL_PEAK_SEARCH_ENABLED',
        'type': 'int32'
    },
    1114155: {
        'access': 'read-write',
        'enum': 'IMAmplitudeCorrectionType',
        'name': 'IM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    1114160: {
        'access': 'read-write',
        'name': 'IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER',
        'type': 'float64'
    },
    1114161: {
        'access': 'read-write',
        'name': 'IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER',
        'type': 'float64'
    },
    1114162: {
        'access': 'read-write',
        'name': 'IM_RESULTS_WORST_CASE_INTERMOD_ABSOLUTE_POWER',
        'type': 'float64'
    },
    1114163: {
        'access': 'read-write',
        'name': 'IM_RESULTS_WORST_CASE_INTERMOD_RELATIVE_POWER',
        'type': 'float64'
    },
    1179649: {
        'access': 'read-write',
        'name': 'NF_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1179652: {
        'access': 'read-write',
        'name': 'NF_FREQUENCY_LIST',
        'type': 'float64[]'
    },
    1179653: {
        'access': 'read-write',
        'name': 'NF_MEASUREMENT_BANDWIDTH',
        'type': 'float64'
    },
    1179654: {
        'access': 'read-write',
        'name': 'NF_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    1179655: {
        'access': 'read-write',
        'enum': 'NFAveragingEnabled',
        'name': 'NF_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1179656: {
        'access': 'read-write',
        'name': 'NF_AVERAGING_COUNT',
        'type': 'int32'
    },
    1179657: {
        'access': 'read-write',
        'enum': 'NFMeasurementMethod',
        'name': 'NF_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    1179658: {
        'access': 'read-write',
        'enum': 'NFYFactorMode',
        'name': 'NF_Y_FACTOR_MODE',
        'type': 'int32'
    },
    1179660: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_ENR',
        'type': 'float64[]'
    },
    1179661: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY',
        'type': 'float64[]'
    },
    1179662: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_COLD_TEMPERATURE',
        'type': 'float64'
    },
    1179663: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_OFF_TEMPERATURE',
        'type': 'float64'
    },
    1179664: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_SETTLING_TIME',
        'type': 'float64'
    },
    1179665: {
        'access': 'read-write',
        'enum': 'NFDutInputLossCompensationEnabled',
        'name': 'NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1179666: {
        'access': 'read-write',
        'name': 'NF_DUT_INPUT_LOSS',
        'type': 'float64[]'
    },
    1179667: {
        'access': 'read-write',
        'name': 'NF_DUT_INPUT_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    1179668: {
        'access': 'read-write',
        'name': 'NF_DUT_INPUT_LOSS_TEMPERATURE',
        'type': 'float64'
    },
    1179669: {
        'access': 'read-write',
        'enum': 'NFDutOutputLossCompensationEnabled',
        'name': 'NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1179670: {
        'access': 'read-write',
        'name': 'NF_DUT_OUTPUT_LOSS',
        'type': 'float64[]'
    },
    1179671: {
        'access': 'read-write',
        'name': 'NF_DUT_OUTPUT_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    1179672: {
        'access': 'read-write',
        'name': 'NF_DUT_OUTPUT_LOSS_TEMPERATURE',
        'type': 'float64'
    },
    1179673: {
        'access': 'read-write',
        'enum': 'NFYFactorNoiseSourceLossCompensationEnabled',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1179674: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS',
        'type': 'float64[]'
    },
    1179675: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    1179676: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURE',
        'type': 'float64'
    },
    1179677: {
        'access': 'read-write',
        'enum': 'NFCalibrationLossCompensationEnabled',
        'name': 'NF_CALIBRATION_LOSS_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    1179678: {
        'access': 'read-write',
        'name': 'NF_CALIBRATION_LOSS',
        'type': 'float64[]'
    },
    1179679: {
        'access': 'read-write',
        'name': 'NF_CALIBRATION_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    1179680: {
        'access': 'read-write',
        'name': 'NF_CALIBRATION_LOSS_TEMPERATURE',
        'type': 'float64'
    },
    1179681: {
        'access': 'read-write',
        'name': 'NF_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1179682: {
        'access': 'read-write',
        'name': 'NF_RESULTS_DUT_NOISE_FIGURE',
        'type': 'float64[]'
    },
    1179683: {
        'access': 'read-write',
        'name': 'NF_RESULTS_DUT_NOISE_TEMPERATURE',
        'type': 'float64[]'
    },
    1179684: {
        'access': 'read-write',
        'name': 'NF_RESULTS_DUT_GAIN',
        'type': 'float64[]'
    },
    1179685: {
        'access': 'read-write',
        'name': 'NF_RESULTS_ANALYZER_NOISE_FIGURE',
        'type': 'float64[]'
    },
    1179686: {
        'access': 'read-write',
        'name': 'NF_RESULTS_MEASUREMENT_Y_FACTOR',
        'type': 'float64[]'
    },
    1179687: {
        'access': 'read-write',
        'name': 'NF_RESULTS_CALIBRATION_Y_FACTOR',
        'type': 'float64[]'
    },
    1179688: {
        'access': 'read-write',
        'name': 'NF_RESULTS_Y_FACTOR_HOT_POWER',
        'type': 'float64[]'
    },
    1179689: {
        'access': 'read-write',
        'name': 'NF_RESULTS_Y_FACTOR_COLD_POWER',
        'type': 'float64[]'
    },
    1179690: {
        'access': 'read-write',
        'name': 'NF_RESULTS_COLD_SOURCE_POWER',
        'type': 'float64[]'
    },
    1179691: {
        'access': 'read-write',
        'enum': 'NFColdSourceMode',
        'name': 'NF_COLD_SOURCE_MODE',
        'type': 'int32'
    },
    1179692: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_INPUT_TERMINATION_VSWR',
        'type': 'float64[]'
    },
    1179693: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_INPUT_TERMINATION_VSWR_FREQUENCY',
        'type': 'float64[]'
    },
    1179694: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURE',
        'type': 'float64'
    },
    1179695: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_DUT_S21',
        'type': 'float64[]'
    },
    1179696: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_DUT_S12',
        'type': 'float64[]'
    },
    1179697: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_DUT_S11',
        'type': 'float64[]'
    },
    1179698: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_DUT_S22',
        'type': 'float64[]'
    },
    1179699: {
        'access': 'read-write',
        'name': 'NF_COLD_SOURCE_DUT_S_PARAMETERS_FREQUENCY',
        'type': 'float64[]'
    },
    1179700: {
        'access': 'read-write',
        'name': 'NF_CALIBRATION_SETUP_ID',
        'type': 'char[]'
    },
    1179701: {
        'access': 'read-write',
        'enum': 'NFExternalPreampPresent',
        'name': 'NF_EXTERNAL_PREAMP_PRESENT',
        'type': 'int32'
    },
    1179702: {
        'access': 'read-write',
        'name': 'NF_EXTERNAL_PREAMP_FREQUENCY',
        'type': 'float64[]'
    },
    1179703: {
        'access': 'read-write',
        'name': 'NF_EXTERNAL_PREAMP_GAIN',
        'type': 'float64[]'
    },
    1179705: {
        'access': 'read-write',
        'name': 'NF_DEVICE_TEMPERATURE_TOLERANCE',
        'type': 'float64'
    },
    1179706: {
        'access': 'read-write',
        'enum': 'NFDutType',
        'name': 'NF_DUT_TYPE',
        'type': 'int32'
    },
    1179708: {
        'access': 'read-write',
        'name': 'NF_FREQUENCY_CONVERTER_LO_FREQUENCY',
        'type': 'float64'
    },
    1179710: {
        'access': 'read-write',
        'enum': 'NFFrequencyConverterFrequencyContext',
        'name': 'NF_FREQUENCY_CONVERTER_FREQUENCY_CONTEXT',
        'type': 'int32'
    },
    1179711: {
        'access': 'read-write',
        'enum': 'NFFrequencyConverterSideband',
        'name': 'NF_FREQUENCY_CONVERTER_SIDEBAND',
        'type': 'int32'
    },
    1179712: {
        'access': 'read-write',
        'name': 'NF_FREQUENCY_CONVERTER_IMAGE_REJECTION',
        'type': 'float64'
    },
    1179713: {
        'access': 'read-write',
        'enum': 'NFYFactorNoiseSourceType',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_TYPE',
        'type': 'int32'
    },
    1179714: {
        'access': 'read-write',
        'name': 'NF_Y_FACTOR_NOISE_SOURCE_RF_SIGNAL_GENERATOR_PORT',
        'type': 'char[]'
    },
    1245184: {
        'access': 'read-write',
        'name': 'PHASENOISE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1245186: {
        'access': 'read-write',
        'enum': 'PhaseNoiseRangeDefinition',
        'name': 'PHASENOISE_RANGE_DEFINITION',
        'type': 'int32'
    },
    1245187: {
        'access': 'read-write',
        'name': 'PHASENOISE_START_FREQUENCY',
        'type': 'float64'
    },
    1245188: {
        'access': 'read-write',
        'name': 'PHASENOISE_STOP_FREQUENCY',
        'type': 'float64'
    },
    1245189: {
        'access': 'read-write',
        'name': 'PHASENOISE_RBW_PERCENTAGE',
        'type': 'float64'
    },
    1245190: {
        'access': 'read-write',
        'name': 'PHASENOISE_AVERAGING_MULTIPLIER',
        'type': 'int32'
    },
    1245191: {
        'access': 'read-write',
        'enum': 'PhaseNoiseFftWindow',
        'name': 'PHASENOISE_FFT_WINDOW',
        'type': 'int32'
    },
    1245192: {
        'access': 'read-write',
        'name': 'PHASENOISE_NUMBER_OF_RANGES',
        'type': 'int32'
    },
    1245193: {
        'access': 'read-write',
        'name': 'PHASENOISE_RANGE_START_FREQUENCY',
        'type': 'float64'
    },
    1245194: {
        'access': 'read-write',
        'name': 'PHASENOISE_RANGE_STOP_FREQUENCY',
        'type': 'float64'
    },
    1245195: {
        'access': 'read-write',
        'name': 'PHASENOISE_RANGE_RBW_PERCENTAGE',
        'type': 'float64'
    },
    1245196: {
        'access': 'read-write',
        'name': 'PHASENOISE_RANGE_AVERAGING_COUNT',
        'type': 'int32'
    },
    1245197: {
        'access': 'read-write',
        'enum': 'PhaseNoiseSmoothingType',
        'name': 'PHASENOISE_SMOOTHING_TYPE',
        'type': 'int32'
    },
    1245198: {
        'access': 'read-write',
        'name': 'PHASENOISE_SMOOTHING_PERCENTAGE',
        'type': 'float64'
    },
    1245199: {
        'access': 'read-write',
        'name': 'PHASENOISE_SPOT_NOISE_FREQUENCY_LIST',
        'type': 'float64[]'
    },
    1245200: {
        'access': 'read-write',
        'enum': 'PhaseNoiseIntegratedNoiseRangeDefinition',
        'name': 'PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION',
        'type': 'int32'
    },
    1245201: {
        'access': 'read-write',
        'name': 'PHASENOISE_INTEGRATED_NOISE_START_FREQUENCY',
        'type': 'float64[]'
    },
    1245202: {
        'access': 'read-write',
        'name': 'PHASENOISE_INTEGRATED_NOISE_STOP_FREQUENCY',
        'type': 'float64[]'
    },
    1245203: {
        'access': 'read-write',
        'name': 'PHASENOISE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1245205: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_CARRIER_POWER',
        'type': 'float64'
    },
    1245206: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    1245207: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_SPOT_PHASE_NOISE',
        'type': 'float64[]'
    },
    1245208: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_INTEGRATED_PHASE_NOISE',
        'type': 'float64[]'
    },
    1245209: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIAN',
        'type': 'float64[]'
    },
    1245210: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREE',
        'type': 'float64[]'
    },
    1245211: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_FM',
        'type': 'float64[]'
    },
    1245212: {
        'access': 'read-write',
        'name': 'PHASENOISE_RESULTS_INTEGRATED_NOISE_JITTER',
        'type': 'float64[]'
    },
    1245213: {
        'access': 'read-write',
        'enum': 'PhaseNoiseSpurRemovalEnabled',
        'name': 'PHASENOISE_SPUR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    1245214: {
        'access': 'read-write',
        'name': 'PHASENOISE_SPUR_REMOVAL_PEAK_EXCURSION',
        'type': 'float64'
    },
    1245215: {
        'access': 'read-write',
        'enum': 'PhaseNoiseCancellationEnabled',
        'name': 'PHASENOISE_CANCELLATION_ENABLED',
        'type': 'int32'
    },
    1245216: {
        'access': 'read-write',
        'name': 'PHASENOISE_CANCELLATION_THRESHOLD',
        'type': 'float64'
    },
    1245217: {
        'access': 'read-write',
        'name': 'PHASENOISE_CANCELLATION_FREQUENCY',
        'type': 'float32[]'
    },
    1245218: {
        'access': 'read-write',
        'name': 'PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE',
        'type': 'float32[]'
    },
    1310720: {
        'access': 'read-write',
        'name': 'IDPD_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1310722: {
        'access': 'read-write',
        'enum': 'IdpdEqualizerMode',
        'name': 'IDPD_EQUALIZER_MODE',
        'type': 'int32'
    },
    1310723: {
        'access': 'read-write',
        'name': 'IDPD_EQUALIZER_FILTER_LENGTH',
        'type': 'int32'
    },
    1310724: {
        'access': 'read-write',
        'enum': 'IdpdMeasurementSampleRateMode',
        'name': 'IDPD_MEASUREMENT_SAMPLE_RATE_MODE',
        'type': 'int32'
    },
    1310725: {
        'access': 'read-write',
        'name': 'IDPD_MEASUREMENT_SAMPLE_RATE',
        'type': 'float64'
    },
    1310726: {
        'access': 'read-write',
        'enum': 'IdpdSignalType',
        'name': 'IDPD_SIGNAL_TYPE',
        'type': 'int32'
    },
    1310731: {
        'access': 'read-write',
        'enum': 'IdpdReferenceWaveformIdleDurationPresent',
        'name': 'IDPD_REFERENCE_WAVEFORM_IDLE_DURATION_PRESENT',
        'type': 'int32'
    },
    1310732: {
        'access': 'read-write',
        'name': 'IDPD_DUT_AVERAGE_INPUT_POWER',
        'type': 'float64'
    },
    1310735: {
        'access': 'read-write',
        'enum': 'IdpdAveragingEnabled',
        'name': 'IDPD_AVERAGING_ENABLED',
        'type': 'int32'
    },
    1310736: {
        'access': 'read-write',
        'name': 'IDPD_AVERAGING_COUNT',
        'type': 'int32'
    },
    1310739: {
        'access': 'read-write',
        'enum': 'IdpdEvmEnabled',
        'name': 'IDPD_EVM_ENABLED',
        'type': 'int32'
    },
    1310740: {
        'access': 'read-write',
        'enum': 'IdpdEvmUnit',
        'name': 'IDPD_EVM_UNIT',
        'type': 'int32'
    },
    1310741: {
        'access': 'read-write',
        'name': 'IDPD_IMPAIRMENT_ESTIMATION_START',
        'type': 'float64'
    },
    1310742: {
        'access': 'read-write',
        'name': 'IDPD_IMPAIRMENT_ESTIMATION_STOP',
        'type': 'float64'
    },
    1310743: {
        'access': 'read-write',
        'name': 'IDPD_SYNCHRONIZATION_ESTIMATION_START',
        'type': 'float64'
    },
    1310744: {
        'access': 'read-write',
        'name': 'IDPD_SYNCHRONIZATION_ESTIMATION_STOP',
        'type': 'float64'
    },
    1310745: {
        'access': 'read-write',
        'name': 'IDPD_GAIN_EXPANSION',
        'type': 'float64'
    },
    1310747: {
        'access': 'read-write',
        'name': 'IDPD_POWER_LINEARITY_TRADEOFF',
        'type': 'float64'
    },
    1310749: {
        'access': 'read-write',
        'name': 'IDPD_RESULTS_GAIN',
        'type': 'float64'
    },
    1310750: {
        'access': 'read-write',
        'name': 'IDPD_RESULTS_MEAN_RMS_EVM',
        'type': 'float64'
    },
    1310751: {
        'access': 'read-write',
        'name': 'IDPD_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    1310753: {
        'access': 'read-write',
        'name': 'IDPD_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    1310759: {
        'access': 'read-write',
        'name': 'IDPD_TARGET_GAIN',
        'type': 'float64'
    },
    1376256: {
        'access': 'read-write',
        'name': 'POWERLIST_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    1376258: {
        'access': 'read-write',
        'name': 'POWERLIST_NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    1376259: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_LENGTH',
        'type': 'float64[]'
    },
    1376260: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_FREQUENCY',
        'type': 'float64[]'
    },
    1376261: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_REFERENCE_LEVEL',
        'type': 'float64[]'
    },
    1376262: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_MEASUREMENT_LENGTH',
        'type': 'float64[]'
    },
    1376263: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_MEASUREMENT_OFFSET',
        'type': 'float64[]'
    },
    1376264: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_RBW_FILTER_BANDWIDTH',
        'type': 'float64[]'
    },
    1376265: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_RBW_FILTER_TYPE',
        'type': 'int32[]'
    },
    1376266: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_RBW_FILTER_ALPHA',
        'type': 'float64[]'
    },
    1376267: {
        'access': 'read-write',
        'name': 'POWERLIST_SEGMENT_TRIGGER_TYPE',
        'type': 'int32[]'
    },
    1376268: {
        'access': 'read-write',
        'name': 'POWERLIST_RESULTS_MEAN_ABSOLUTE_POWER',
        'type': 'float64[]'
    },
    1376269: {
        'access': 'read-write',
        'name': 'POWERLIST_RESULTS_MAXIMUM_POWER',
        'type': 'float64[]'
    },
    1376270: {
        'access': 'read-write',
        'name': 'POWERLIST_RESULTS_MINIMUM_POWER',
        'type': 'float64[]'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfmxspecan/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/config.py sha256=bc26d024b24327e6b68db078e647be3ea84c9dee047fe658d94b311f76551af0 bytes=2075 -->
## FILE: source/codegen/metadata/nirfmxspecan/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/config.py`
- sha256: `bc26d024b24327e6b68db078e647be3ea84c9dee047fe658d94b311f76551af0`
- bytes: 2075

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.8.0',
    'c_header': 'niRFmxSpecAn.h',
    'c_function_prefix': 'RFmxSpecAn_',
    'service_class_prefix': 'NiRFmxSpecAn',
    'java_package': 'com.ni.grpc.nirfmxspecan',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxSpecAn',
    'namespace_component': 'nirfmxspecan',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': { 'custom/nirfmx_errors.h': ['service.cpp'] },
    'type_to_grpc_type': {
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
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-RFMXSPECAN',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxspecan',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxSpecAn.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxSpecAn.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxspecan',
    'session_class_description': 'An NI-RFmxSpecAn instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxspecan/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/enums.py sha256=0163b41c3c823c875893ea7832bd615800d90cae99ad18e4a89d3d16d99f3b98 bytes=91894 -->
## FILE: source/codegen/metadata/nirfmxspecan/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/enums.py`
- sha256: `0163b41c3c823c875893ea7832bd615800d90cae99ad18e4a89d3d16d99f3b98`
- bytes: 91894

````python
enums = {
    'AcpAmplitudeCorrectionType': {
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
    'AcpAveragingEnabled': {
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
    'AcpAveragingType': {
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
    'AcpCarrierMode': {
        'values': [
            {
                'name': 'PASSIVE',
                'value': 0
            },
            {
                'name': 'ACTIVE',
                'value': 1
            }
        ]
    },
    'AcpCarrierRrcFilterEnabled': {
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
    'AcpDetectorType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SAMPLE',
                'value': 1
            },
            {
                'name': 'NORMAL',
                'value': 2
            },
            {
                'name': 'PEAK',
                'value': 3
            },
            {
                'name': 'NEGATIVE_PEAK',
                'value': 4
            },
            {
                'name': 'AVERAGE_RMS',
                'value': 5
            },
            {
                'name': 'AVERAGE_VOLTAGE',
                'value': 6
            },
            {
                'name': 'AVERAGE_LOG',
                'value': 7
            }
        ]
    },
    'AcpFftOverlapMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'AUTOMATIC',
                'value': 1
            },
            {
                'name': 'USER_DEFINED',
                'value': 2
            }
        ]
    },
    'AcpFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'AcpIFOutputPowerOffsetAuto': {
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
    'AcpMeasurementMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'DYNAMIC_RANGE',
                'value': 1
            },
            {
                'name': 'SEQUENTIAL_FFT',
                'value': 2
            }
        ]
    },
    'AcpMeasurementMode': {
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
    'AcpNoiseCalibrationAveragingAuto': {
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
    'AcpNoiseCalibrationDataValid': {
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
    'AcpNoiseCalibrationMode': {
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
    'AcpNoiseCompensationEnabled': {
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
    'AcpNoiseCompensationType': {
        'values': [
            {
                'name': 'ANALYZER_AND_TERMINATION',
                'value': 0
            },
            {
                'name': 'ANALYZER_ONLY',
                'value': 1
            }
        ]
    },
    'AcpOffsetEnabled': {
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
    'AcpOffsetFrequencyDefinition': {
        'values': [
            {
                'name': 'CARRIER_CENTER_TO_OFFSET_CENTER',
                'value': 0
            },
            {
                'name': 'CARRIER_CENTER_TO_OFFSET_EDGE',
                'value': 1
            }
        ]
    },
    'AcpOffsetPowerReferenceCarrier': {
        'values': [
            {
                'name': 'CLOSEST',
                'value': 0
            },
            {
                'name': 'HIGHEST',
                'value': 1
            },
            {
                'name': 'COMPOSITE',
                'value': 2
            },
            {
                'name': 'SPECIFIC',
                'value': 3
            }
        ]
    },
    'AcpOffsetRrcFilterEnabled': {
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
    'AcpOffsetSideband': {
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
    'AcpPowerUnits': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'DBM_PER_HZ',
                'value': 1
            }
        ]
    },
    'AcpRbwAutoBandwidth': {
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
    'AcpRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            }
        ]
    },
    'AcpRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'AcpSweepTimeAuto': {
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
    'AmpmAMToAMCurveFitType': {
        'values': [
            {
                'name': 'LEAST_SQUARE',
                'value': 0
            },
            {
                'name': 'LEAST_ABSOLUTE_RESIDUAL',
                'value': 1
            },
            {
                'name': 'BISQUARE',
                'value': 2
            }
        ]
    },
    'AmpmAMToAMEnabled': {
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
    'AmpmAMToPMCurveFitType': {
        'values': [
            {
                'name': 'LEAST_SQUARE',
                'value': 0
            },
            {
                'name': 'LEAST_ABSOLUTE_RESIDUAL',
                'value': 1
            },
            {
                'name': 'BISQUARE',
                'value': 2
            }
        ]
    },
    'AmpmAMToPMEnabled': {
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
    'AmpmAutoCarrierDetectionEnabled': {
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
    'AmpmAveragingEnabled': {
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
    'AmpmCompressionPointEnabled': {
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
    'AmpmCompressionPointGainReference': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'REFERENCE_POWER',
                'value': 1
            },
            {
                'name': 'MAX_GAIN',
                'value': 2
            },
            {
                'name': 'USER_DEFINED',
                'value': 3
            }
        ]
    },
    'AmpmEqualizerMode': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'TRAIN',
                'value': 1
            }
        ]
    },
    'AmpmEvmEnabled': {
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
    'AmpmFrequencyOffsetCorrectionEnabled': {
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
    'AmpmIQOriginOffsetCorrectionEnabled': {
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
    'AmpmMeasurementSampleRateMode': {
        'values': [
            {
                'name': 'USER',
                'value': 0
            },
            {
                'name': 'REFERENCE_WAVEFORM',
                'value': 1
            }
        ]
    },
    'AmpmReferencePowerType': {
        'values': [
            {
                'name': 'INPUT',
                'value': 0
            },
            {
                'name': 'OUTPUT',
                'value': 1
            }
        ]
    },
    'AmpmReferenceWaveformIdleDurationPresent': {
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
    'AmpmSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
                'value': 1
            }
        ]
    },
    'AmpmSynchronizationMethod': {
        'values': [
            {
                'name': 'DIRECT',
                'value': 1
            },
            {
                'name': 'ALIAS_PROTECTED',
                'value': 2
            }
        ]
    },
    'AmpmThresholdDefinition': {
        'values': [
            {
                'name': 'INPUT_AND_OUTPUT',
                'value': 0
            },
            {
                'name': 'REFERENCE_POWER_TYPE',
                'value': 1
            }
        ]
    },
    'AmpmThresholdEnabled': {
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
    'AmpmThresholdType': {
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
    'CcdfRbwFilterType': {
        'values': [
            {
                'name': 'NONE',
                'value': 5
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            },
            {
                'name': 'RRC',
                'value': 6
            }
        ]
    },
    'CcdfThresholdEnabled': {
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
    'CcdfThresholdType': {
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
    'ChpAmplitudeCorrectionType': {
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
    'ChpAveragingEnabled': {
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
    'ChpAveragingType': {
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
    'ChpCarrierRrcFilterEnabled': {
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
    'ChpDetectorType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SAMPLE',
                'value': 1
            },
            {
                'name': 'NORMAL',
                'value': 2
            },
            {
                'name': 'PEAK',
                'value': 3
            },
            {
                'name': 'NEGATIVE_PEAK',
                'value': 4
            },
            {
                'name': 'AVERAGE_RMS',
                'value': 5
            },
            {
                'name': 'AVERAGE_VOLTAGE',
                'value': 6
            },
            {
                'name': 'AVERAGE_LOG',
                'value': 7
            }
        ]
    },
    'ChpFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'ChpMeasurementMode': {
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
    'ChpNoiseCalibrationAveragingAuto': {
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
    'ChpNoiseCalibrationDataValid': {
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
    'ChpNoiseCalibrationMode': {
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
    'ChpNoiseCompensationEnabled': {
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
    'ChpNoiseCompensationType': {
        'values': [
            {
                'name': 'ANALYZER_AND_TERMINATION',
                'value': 0
            },
            {
                'name': 'ANALYZER_ONLY',
                'value': 1
            }
        ]
    },
    'ChpRbwAutoBandwidth': {
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
    'ChpRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            }
        ]
    },
    'ChpRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'ChpSweepTimeAuto': {
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
    'DpdApplyDpdCfrEnabled': {
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
    'DpdApplyDpdCfrMethod': {
        'values': [
            {
                'name': 'CLIPPING',
                'value': 0
            },
            {
                'name': 'PEAK_WINDOWING',
                'value': 1
            },
            {
                'name': 'SIGMOID',
                'value': 2
            }
        ]
    },
    'DpdApplyDpdCfrTargetPaprType': {
        'values': [
            {
                'name': 'INPUT_PAPR',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            }
        ]
    },
    'DpdApplyDpdCfrWindowType': {
        'values': [
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'DpdApplyDpdConfigurationInput': {
        'values': [
            {
                'name': 'MEASUREMENT',
                'value': 0
            },
            {
                'name': 'USER',
                'value': 1
            }
        ]
    },
    'DpdApplyDpdIdleDurationPresent': {
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
    'DpdApplyDpdLookupTableCorrectionType': {
        'values': [
            {
                'name': 'MAGNITUDE_AND_PHASE',
                'value': 0
            },
            {
                'name': 'MAGNITUDE_ONLY',
                'value': 1
            },
            {
                'name': 'PHASE_ONLY',
                'value': 2
            }
        ]
    },
    'DpdApplyDpdMemoryModelCorrectionType': {
        'values': [
            {
                'name': 'MAGNITUDE_AND_PHASE',
                'value': 0
            },
            {
                'name': 'MAGNITUDE_ONLY',
                'value': 1
            },
            {
                'name': 'PHASE_ONLY',
                'value': 2
            }
        ]
    },
    'DpdApplyDpdUserDpdModel': {
        'values': [
            {
                'name': 'LOOKUP_TABLE',
                'value': 0
            },
            {
                'name': 'MEMORY_POLYNOMIAL',
                'value': 1
            },
            {
                'name': 'GENERALIZED_MEMORY_POLYNOMIAL',
                'value': 2
            }
        ]
    },
    'DpdApplyDpdUserLookupTableType': {
        'values': [
            {
                'name': 'LOG',
                'value': 0
            },
            {
                'name': 'LINEAR',
                'value': 1
            }
        ]
    },
    'DpdAutoCarrierDetectionEnabled': {
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
    'DpdAveragingEnabled': {
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
    'DpdDvrDdrEnabled': {
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
    'DpdFrequencyOffsetCorrectionEnabled': {
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
    'DpdIQOriginOffsetCorrectionEnabled': {
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
    'DpdIterativeDpdEnabled': {
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
    'DpdLookupTableAMToAMCurveFitType': {
        'values': [
            {
                'name': 'LEAST_SQUARE',
                'value': 0
            },
            {
                'name': 'LEAST_ABSOLUTE_RESIDUAL',
                'value': 1
            },
            {
                'name': 'BISQUARE',
                'value': 2
            }
        ]
    },
    'DpdLookupTableAMToPMCurveFitType': {
        'values': [
            {
                'name': 'LEAST_SQUARE',
                'value': 0
            },
            {
                'name': 'LEAST_ABSOLUTE_RESIDUAL',
                'value': 1
            },
            {
                'name': 'BISQUARE',
                'value': 2
            }
        ]
    },
    'DpdLookupTableThresholdDefinition': {
        'values': [
            {
                'name': 'INPUT_AND_OUTPUT',
                'value': 0
            },
            {
                'name': 'INPUT',
                'value': 1
            }
        ]
    },
    'DpdLookupTableThresholdEnabled': {
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
    'DpdLookupTableThresholdType': {
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
    'DpdLookupTableType': {
        'values': [
            {
                'name': 'LOG',
                'value': 0
            },
            {
                'name': 'LINEAR',
                'value': 1
            }
        ]
    },
    'DpdMeasurementMode': {
        'values': [
            {
                'name': 'ACQUIRE_AND_EXTRACT',
                'value': 0
            },
            {
                'name': 'EXTRACT_ONLY',
                'value': 1
            }
        ]
    },
    'DpdMeasurementSampleRateMode': {
        'values': [
            {
                'name': 'USER',
                'value': 0
            },
            {
                'name': 'REFERENCE_WAVEFORM',
                'value': 1
            }
        ]
    },
    'DpdMemoryPolynomialLagOrderType': {
        'values': [
            {
                'name': 'ALL_ORDERS',
                'value': 0
            },
            {
                'name': 'ODD_ORDERS_ONLY',
                'value': 1
            },
            {
                'name': 'EVEN_ORDERS_ONLY',
                'value': 2
            }
        ]
    },
    'DpdMemoryPolynomialLeadOrderType': {
        'values': [
            {
                'name': 'ALL_ORDERS',
                'value': 0
            },
            {
                'name': 'ODD_ORDERS_ONLY',
                'value': 1
            },
            {
                'name': 'EVEN_ORDERS_ONLY',
                'value': 2
            }
        ]
    },
    'DpdMemoryPolynomialOrderType': {
        'values': [
            {
                'name': 'ALL_ORDERS',
                'value': 0
            },
            {
                'name': 'ODD_ORDERS_ONLY',
                'value': 1
            },
            {
                'name': 'EVEN_ORDERS_ONLY',
                'value': 2
            }
        ]
    },
    'DpdModel': {
        'values': [
            {
                'name': 'LOOKUP_TABLE',
                'value': 0
            },
            {
                'name': 'MEMORY_POLYNOMIAL',
                'value': 1
            },
            {
                'name': 'GENERALIZED_MEMORY_POLYNOMIAL',
                'value': 2
            },
            {
                'name': 'DECOMPOSED_VECTOR_ROTATION',
                'value': 3
            }
        ]
    },
    'DpdNmseEnabled': {
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
    'DpdPreDpdCfrEnabled': {
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
    'DpdPreDpdCfrFilterEnabled': {
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
    'DpdPreDpdCfrMethod': {
        'values': [
            {
                'name': 'CLIPPING',
                'value': 0
            },
            {
                'name': 'PEAK_WINDOWING',
                'value': 1
            },
            {
                'name': 'SIGMOID',
                'value': 2
            }
        ]
    },
    'DpdPreDpdCfrWindowType': {
        'values': [
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'DpdReferenceWaveformIdleDurationPresent': {
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
    'DpdSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
                'value': 1
            }
        ]
    },
    'DpdSynchronizationMethod': {
        'values': [
            {
                'name': 'DIRECT',
                'value': 1
            },
            {
                'name': 'ALIAS_PROTECTED',
                'value': 2
            }
        ]
    },
    'DpdTargetGainType': {
        'values': [
            {
                'name': 'AVERAGE_GAIN',
                'value': 0
            },
            {
                'name': 'LINEAR_REGION_GAIN',
                'value': 1
            },
            {
                'name': 'PEAK_INPUT_POWER_GAIN',
                'value': 2
            }
        ]
    },
    'FcntAveragingEnabled': {
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
    'FcntAveragingType': {
        'values': [
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            },
            {
                'name': 'MEAN',
                'value': 6
            },
            {
                'name': 'MINMAX',
                'value': 7
            }
        ]
    },
    'FcntRbwFilterType': {
        'values': [
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            },
            {
                'name': 'NONE',
                'value': 5
            },
            {
                'name': 'RRC',
                'value': 6
            }
        ]
    },
    'FcntThresholdEnabled': {
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
    'FcntThresholdType': {
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
    'HarmAutoHarmonicsSetupEnabled': {
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
    'HarmAveragingEnabled': {
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
    'HarmAveragingType': {
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
    'HarmHarmonicEnabled': {
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
    'HarmMeasurementMethod': {
        'values': [
            {
                'name': 'TIME_DOMAIN',
                'value': 0
            },
            {
                'name': 'DYNAMIC_RANGE',
                'value': 2
            }
        ]
    },
    'HarmNoiseCompensationEnabled': {
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
    'HarmRbwFilterType': {
        'values': [
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            },
            {
                'name': 'NONE',
                'value': 5
            },
            {
                'name': 'RRC',
                'value': 6
            }
        ]
    },
    'IMAmplitudeCorrectionType': {
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
    'IMAutoIntermodsSetupEnabled': {
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
    'IMAveragingEnabled': {
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
    'IMAveragingType': {
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
    'IMFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'IMFrequencyDefinition': {
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
    'IMIFOutputPowerOffsetAuto': {
        'enum-value-prefix': 'IM_IF_OUTPUT_POWER_OFFSET_AUTO',
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
    'IMIntermodEnabled': {
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
    'IMIntermodSide': {
        'values': [
            {
                'name': 'LOWER',
                'value': 0
            },
            {
                'name': 'UPPER',
                'value': 1
            },
            {
                'name': 'BOTH',
                'value': 2
            }
        ]
    },
    'IMLocalPeakSearchEnabled': {
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
    'IMMeasurementMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'DYNAMIC_RANGE',
                'value': 1
            },
            {
                'name': 'SEGMENTED',
                'value': 2
            }
        ]
    },
    'IMRbwFilterAutoBandwidth': {
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
    'IMRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'IMSweepTimeAuto': {
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
    'IQBandwidthAuto': {
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
    'IQDeleteRecordOnFetch': {
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
    'IQMeasurementMode': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'RAWIQ',
                'value': 1
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
    'IdpdAveragingEnabled': {
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
    'IdpdEqualizerMode': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'TRAIN',
                'value': 1
            },
            {
                'name': 'HOLD',
                'value': 2
            }
        ]
    },
    'IdpdEvmEnabled': {
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
    'IdpdEvmUnit': {
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
    'IdpdMeasurementSampleRateMode': {
        'values': [
            {
                'name': 'USER',
                'value': 0
            },
            {
                'name': 'REFERENCE_WAVEFORM',
                'value': 1
            }
        ]
    },
    'IdpdReferenceWaveformIdleDurationPresent': {
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
    'IdpdSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
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
    'MarkerFunctionType': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'BAND_POWER',
                'value': 1
            }
        ]
    },
    'MarkerNextPeak': {
        'values': [
            {
                'name': 'NEXT_HIGHEST',
                'value': 0
            },
            {
                'name': 'NEXT_LEFT',
                'value': 1
            },
            {
                'name': 'NEXT_RIGHT',
                'value': 2
            }
        ]
    },
    'MarkerPeakExcursionEnabled': {
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
    'MarkerThresholdEnabled': {
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
    'MarkerTrace': {
        'values': [
            {
                'name': 'ACP_SPECTRUM',
                'value': 0
            },
            {
                'name': 'CCDF_GAUSSIAN_PROBABILITIES_TRACE',
                'value': 1
            },
            {
                'name': 'CCDF_PROBABILITIES_TRACE',
                'value': 2
            },
            {
                'name': 'CHP_SPECTRUM',
                'value': 3
            },
            {
                'name': 'FCNT_POWER_TRACE',
                'value': 4
            },
            {
                'name': 'OBW_SPECTRUM',
                'value': 5
            },
            {
                'name': 'SEM_SPECTRUM',
                'value': 6
            },
            {
                'name': 'SPECTRUM',
                'value': 7
            },
            {
                'name': 'TXP_POWER_TRACE',
                'value': 8
            }
        ]
    },
    'MarkerType': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'NORMAL',
                'value': 1
            },
            {
                'name': 'DELTA',
                'value': 3
            },
            {
                'name': 'FIXED',
                'value': 4
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'ACP',
                'value': 1
            },
            {
                'name': 'CCDF',
                'value': 2
            },
            {
                'name': 'CHP',
                'value': 4
            },
            {
                'name': 'FCNT',
                'value': 8
            },
            {
                'name': 'HARMONICS',
                'value': 16
            },
            {
                'name': 'OBW',
                'value': 32
            },
            {
                'name': 'SEM',
                'value': 64
            },
            {
                'name': 'SPECTRUM',
                'value': 128
            },
            {
                'name': 'SPUR',
                'value': 256
            },
            {
                'name': 'TXP',
                'value': 512
            },
            {
                'name': 'AMPM',
                'value': 1024
            },
            {
                'name': 'DPD',
                'value': 2048
            },
            {
                'name': 'IQ',
                'value': 4096
            },
            {
                'name': 'IM',
                'value': 8192
            },
            {
                'name': 'NF',
                'value': 16384
            },
            {
                'name': 'PHASENOISE',
                'value': 32768
            },
            {
                'name': 'PAVT',
                'value': 65536
            },
            {
                'name': 'IDPD',
                'value': 131072
            },
            {
                'name': 'POWERLIST',
                'value': 262144
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
    'NFAveragingEnabled': {
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
    'NFCalibrationDataValid': {
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
    'NFCalibrationLossCompensationEnabled': {
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
    'NFCalibrationLossS2pSParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFColdSourceDutS2pSParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFColdSourceMode': {
        'values': [
            {
                'name': 'MEASURE',
                'value': 0
            },
            {
                'name': 'CALIBRATE',
                'value': 1
            }
        ]
    },
    'NFDutInputLossCompensationEnabled': {
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
    'NFDutInputLossS2pSParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFDutOutputLossCompensationEnabled': {
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
    'NFDutOutputLossS2pSParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFDutType': {
        'values': [
            {
                'name': 'AMPLIFIER',
                'value': 0
            },
            {
                'name': 'DOWNCONVERTER',
                'value': 1
            },
            {
                'name': 'UPCONVERTER',
                'value': 2
            }
        ]
    },
    'NFExternalPreampGainS2pSParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFExternalPreampPresent': {
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
    'NFFrequencyConverterFrequencyContext': {
        'values': [
            {
                'name': 'RF',
                'value': 0
            },
            {
                'name': 'IF',
                'value': 1
            }
        ]
    },
    'NFFrequencyConverterSideband': {
        'values': [
            {
                'name': 'LSB',
                'value': 0
            },
            {
                'name': 'USB',
                'value': 1
            }
        ]
    },
    'NFMeasurementMethod': {
        'values': [
            {
                'name': 'Y_FACTOR',
                'value': 0
            },
            {
                'name': 'COLD_SOURCE',
                'value': 1
            }
        ]
    },
    'NFYFactorMode': {
        'enum-value-prefix': 'NF_Y_FACTOR_MODE',
        'values': [
            {
                'name': 'MEASURE',
                'value': 0
            },
            {
                'name': 'CALIBRATE',
                'value': 1
            }
        ]
    },
    'NFYFactorNoiseSourceLossCompensationEnabled': {
        'enum-value-prefix': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED',
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
    'NFYFactorNoiseSourceLossS2pSParameterOrientation': {
        'enum-value-prefix': 'NF_Y_FACTOR_NOISE_SOURCE_LOSS_S2P_S_PARAMETER_ORIENTATION',
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 1
            }
        ]
    },
    'NFYFactorNoiseSourceType': {
        'enum-value-prefix': 'NF_Y_FACTOR_NOISE_SOURCE_TYPE',
        'values': [
            {
                'name': 'EXTERNAL_NOISE_SOURCE',
                'value': 0
            },
            {
                'name': 'RF_SIGNAL_GENERATOR',
                'value': 1
            }
        ]
    },
    'ObwAmplitudeCorrectionType': {
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
    'ObwAveragingEnabled': {
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
    'ObwAveragingType': {
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
    'ObwFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'ObwPowerUnits': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'DBM_PER_HZ',
                'value': 1
            }
        ]
    },
    'ObwRbwAutoBandwidth': {
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
    'ObwRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            }
        ]
    },
    'ObwRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'ObwSweepTimeAuto': {
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
    'PavtFrequencyOffsetCorrectionEnabled': {
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
    'PavtFrequencyTrackingEnabled': {
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
    'PavtMeasurementIntervalMode': {
        'values': [
            {
                'name': 'UNIFORM',
                'value': 0
            },
            {
                'name': 'VARIABLE',
                'value': 1
            }
        ]
    },
    'PavtMeasurementLocationType': {
        'values': [
            {
                'name': 'TIME',
                'value': 0
            },
            {
                'name': 'TRIGGER',
                'value': 1
            }
        ]
    },
    'PavtPhaseUnwrapEnabled': {
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
    'PavtSegmentType': {
        'values': [
            {
                'name': 'PHASE_AND_AMPLITUDE',
                'value': 0
            },
            {
                'name': 'AMPLITUDE',
                'value': 1
            },
            {
                'name': 'FREQUENCY_ERROR_MEASUREMENT',
                'value': 2
            }
        ]
    },
    'PhaseNoiseCancellationEnabled': {
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
    'PhaseNoiseFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'PhaseNoiseIntegratedNoiseRangeDefinition': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'MEASUREMENT',
                'value': 1
            },
            {
                'name': 'CUSTOM',
                'value': 2
            }
        ]
    },
    'PhaseNoiseRangeDefinition': {
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
    'PhaseNoiseSmoothingType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'LINEAR',
                'value': 1
            },
            {
                'name': 'LOGARITHMIC',
                'value': 2
            },
            {
                'name': 'MEDIAN',
                'value': 3
            }
        ]
    },
    'PhaseNoiseSpurRemovalEnabled': {
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
    'SemCarrierEnabled': {
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
    'SemCarrierRbwAutoBandwidth': {
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
    'SemCarrierRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            }
        ]
    },
    'SemCarrierRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'SemCarrierRrcFilterEnabled': {
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
    'SemCompositeMeasurementStatus': {
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
    'SemFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
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
    'SemOffsetAbsoluteLimitMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'COUPLE',
                'value': 1
            }
        ]
    },
    'SemOffsetEnabled': {
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
    'SemOffsetFrequencyDefinition': {
        'values': [
            {
                'name': 'CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_CENTER',
                'value': 0
            },
            {
                'name': 'CARRIER_CENTER_TO_MEASUREMENT_BANDWIDTH_EDGE',
                'value': 1
            },
            {
                'name': 'CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_CENTER',
                'value': 2
            },
            {
                'name': 'CARRIER_EDGE_TO_MEASUREMENT_BANDWIDTH_EDGE',
                'value': 3
            }
        ]
    },
    'SemOffsetLimitFailMask': {
        'values': [
            {
                'name': 'ABSOLUTE_AND_RELATIVE',
                'value': 0
            },
            {
                'name': 'ABSOLUTE_OR_RELATIVE',
                'value': 1
            },
            {
                'name': 'ABSOLUTE',
                'value': 2
            },
            {
                'name': 'RELATIVE',
                'value': 3
            }
        ]
    },
    'SemOffsetRbwAutoBandwidth': {
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
    'SemOffsetRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            }
        ]
    },
    'SemOffsetRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'SemOffsetRelativeLimitMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'COUPLE',
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
    'SemPowerUnits': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'DBM_PER_HZ',
                'value': 1
            }
        ]
    },
    'SemReferenceType': {
        'values': [
            {
                'name': 'INTEGRATION',
                'value': 0
            },
            {
                'name': 'PEAK',
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
    'SpectrumAmplitudeCorrectionType': {
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
    'SpectrumAnalysisInput': {
        'values': [
            {
                'name': 'IQ',
                'value': 0
            },
            {
                'name': 'I_ONLY',
                'value': 1
            },
            {
                'name': 'Q_ONLY',
                'value': 2
            }
        ]
    },
    'SpectrumAveragingEnabled': {
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
    'SpectrumAveragingType': {
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
    'SpectrumDetectorType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SAMPLE',
                'value': 1
            },
            {
                'name': 'NORMAL',
                'value': 2
            },
            {
                'name': 'PEAK',
                'value': 3
            },
            {
                'name': 'NEGATIVE_PEAK',
                'value': 4
            },
            {
                'name': 'AVERAGE_RMS',
                'value': 5
            },
            {
                'name': 'AVERAGE_VOLTAGE',
                'value': 6
            },
            {
                'name': 'AVERAGE_LOG',
                'value': 7
            }
        ]
    },
    'SpectrumFftOverlapMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'AUTOMATIC',
                'value': 1
            },
            {
                'name': 'USER_DEFINED',
                'value': 2
            }
        ]
    },
    'SpectrumFftOverlapType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'MAX',
                'value': 3
            }
        ]
    },
    'SpectrumFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'SpectrumMeasurementMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'SEQUENTIAL_FFT',
                'value': 2
            }
        ]
    },
    'SpectrumMeasurementMode': {
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
    'SpectrumNoiseCalibrationAveragingAuto': {
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
    'SpectrumNoiseCalibrationDataValid': {
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
    'SpectrumNoiseCalibrationMode': {
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
    'SpectrumNoiseCompensationEnabled': {
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
    'SpectrumNoiseCompensationType': {
        'values': [
            {
                'name': 'ANALYZER_AND_TERMINATION',
                'value': 0
            },
            {
                'name': 'ANALYZER_ONLY',
                'value': 1
            }
        ]
    },
    'SpectrumPowerUnits': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'DBM_PER_HZ',
                'value': 1
            },
            {
                'name': 'DBW',
                'value': 2
            },
            {
                'name': 'DBV',
                'value': 3
            },
            {
                'name': 'DBMV',
                'value': 4
            },
            {
                'name': 'DBUV',
                'value': 5
            },
            {
                'name': 'WATTS',
                'value': 6
            },
            {
                'name': 'VOLTS',
                'value': 7
            },
            {
                'name': 'VOLTS_SQUARED',
                'value': 8
            }
        ]
    },
    'SpectrumRbwAutoBandwidth': {
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
    'SpectrumRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': '6DB',
                'value': 1
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            },
            {
                'name': 'ENBW',
                'value': 3
            }
        ]
    },
    'SpectrumRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'SpectrumSweepTimeAuto': {
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
    'SpectrumVbwFilterAutoBandwidth': {
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
    'SpurAbsoluteLimitMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'COUPLE',
                'value': 1
            }
        ]
    },
    'SpurAmplitudeCorrectionType': {
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
    'SpurAveragingEnabled': {
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
    'SpurAveragingType': {
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
    'SpurFftWindow': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            }
        ]
    },
    'SpurMeasurementStatus': {
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
    'SpurRangeDetectorType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SAMPLE',
                'value': 1
            },
            {
                'name': 'NORMAL',
                'value': 2
            },
            {
                'name': 'PEAK',
                'value': 3
            },
            {
                'name': 'NEGATIVE_PEAK',
                'value': 4
            },
            {
                'name': 'AVERAGE_RMS',
                'value': 5
            },
            {
                'name': 'AVERAGE_VOLTAGE',
                'value': 6
            },
            {
                'name': 'AVERAGE_LOG',
                'value': 7
            }
        ]
    },
    'SpurRangeEnabled': {
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
    'SpurRangeStatus': {
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
    'SpurRangeVbwFilterAutoBandwidth': {
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
    'SpurRbwAutoBandwidth': {
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
    'SpurRbwFilterBandwidthDefinition': {
        'values': [
            {
                'name': '3DB',
                'value': 0
            },
            {
                'name': 'BIN_WIDTH',
                'value': 2
            },
            {
                'name': 'ENBW',
                'value': 3
            }
        ]
    },
    'SpurRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'SpurSweepTimeAuto': {
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
    'TxpAveragingType': {
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
    'TxpRbwFilterType': {
        'values': [
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            },
            {
                'name': 'NONE',
                'value': 5
            },
            {
                'name': 'RRC',
                'value': 6
            }
        ]
    },
    'TxpThresholdEnabled': {
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
    'TxpThresholdType': {
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
    'TxpVbwFilterAutoBandwidth': {
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nirfmxspecan/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/functions.py sha256=adc70038e57de224e8b73236aa654fc7b90a8bb4b32fb7efe8e1346c8125d5ff bytes=548292 -->
## FILE: source/codegen/metadata/nirfmxspecan/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/functions.py`
- sha256: `adc70038e57de224e8b73236aa654fc7b90a8bb4b32fb7efe8e1346c8125d5ff`
- bytes: 548292

````python
functions = {
    'ACPCfgAveraging': {
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
                'enum': 'AcpAveragingEnabled',
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
                'enum': 'AcpAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgCarrierAndOffsets': {
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
                'name': 'integrationBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'numberOfOffsets',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelSpacing',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgCarrierFrequency': {
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
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgCarrierIntegrationBandwidth': {
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
                'name': 'integrationBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgCarrierMode': {
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
                'enum': 'AcpCarrierMode',
                'name': 'carrierMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgCarrierRRCFilter': {
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
                'enum': 'AcpCarrierRrcFilterEnabled',
                'name': 'rrcFilterEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgDetector': {
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
                'enum': 'AcpDetectorType',
                'name': 'detectorType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'detectorPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgFFT': {
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
                'enum': 'AcpFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgMeasurementMethod': {
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
                'enum': 'AcpMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNoiseCompensationEnabled': {
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
                'enum': 'AcpNoiseCompensationEnabled',
                'name': 'noiseCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfCarriers': {
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
                'name': 'numberOfCarriers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfOffsets': {
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
    'ACPCfgOffset': {
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
                'name': 'offsetFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'AcpOffsetSideband',
                'name': 'offsetSideband',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AcpOffsetEnabled',
                'name': 'offsetEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetArray': {
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
                'name': 'offsetFrequency',
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
                'enum': 'AcpOffsetSideband',
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
                'enum': 'AcpOffsetEnabled',
                'name': 'offsetEnabled',
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
    'ACPCfgOffsetFrequencyDefinition': {
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
                'enum': 'AcpOffsetFrequencyDefinition',
                'name': 'offsetFrequencyDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetIntegrationBandwidth': {
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
                'name': 'integrationBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetIntegrationBandwidthArray': {
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
                'name': 'integrationBandwidth',
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
    'ACPCfgOffsetPowerReference': {
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
                'enum': 'AcpOffsetPowerReferenceCarrier',
                'name': 'offsetReferenceCarrier',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'offsetReferenceSpecific',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetPowerReferenceArray': {
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
                'enum': 'AcpOffsetPowerReferenceCarrier',
                'name': 'offsetPowerReferenceCarrier',
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
                'name': 'offsetPowerReferenceSpecific',
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
    'ACPCfgOffsetRRCFilter': {
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
                'enum': 'AcpOffsetRrcFilterEnabled',
                'name': 'rrcFilterEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetRRCFilterArray': {
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
                'enum': 'AcpOffsetRrcFilterEnabled',
                'name': 'rrcFilterEnabled',
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
                'name': 'rrcAlpha',
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
    'ACPCfgOffsetRelativeAttenuation': {
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
                'name': 'relativeAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetRelativeAttenuationArray': {
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
                'name': 'relativeAttenuation',
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
    'ACPCfgPowerUnits': {
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
                'enum': 'AcpPowerUnits',
                'name': 'powerUnits',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgRBWFilter': {
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
                'enum': 'AcpRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'AcpRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgSweepTime': {
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
                'enum': 'AcpSweepTimeAuto',
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
    'ACPFetchAbsolutePowersTrace': {
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
                'name': 'traceIndex',
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
                'name': 'absolutePowersTrace',
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
    'ACPFetchCarrierMeasurement': {
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
                'name': 'totalRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'carrierOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchFrequencyResolution': {
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
                'name': 'frequencyResolution',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchOffsetMeasurement': {
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
                'name': 'lowerRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperAbsolutePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchOffsetMeasurementArray': {
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
                'name': 'lowerRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'lowerAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperAbsolutePower',
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
    'ACPFetchRelativePowersTrace': {
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
                'name': 'traceIndex',
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
                'name': 'relativePowersTrace',
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
    'ACPFetchSpectrum': {
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
    'ACPFetchTotalCarrierPower': {
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
                'name': 'totalCarrierPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPRead': {
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
                'name': 'carrierAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetCh0LowerRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetCh0UpperRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetCh1LowerRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetCh1UpperRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPValidateNoiseCalibrationData': {
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
                'enum': 'AcpNoiseCalibrationDataValid',
                'name': 'noiseCalibrationDataValid',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgAMToAMCurveFit': {
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
                'name': 'amToAMCurveFitOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmAMToAMCurveFitType',
                'name': 'amToAMCurveFitType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgAMToPMCurveFit': {
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
                'name': 'amToPMCurveFitOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmAMToPMCurveFitType',
                'name': 'amToPMCurveFitType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgAveraging': {
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
                'enum': 'AmpmAveragingEnabled',
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
    'AMPMCfgCompressionPoints': {
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
                'enum': 'AmpmCompressionPointEnabled',
                'name': 'compressionPointEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'compressionLevel',
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
    'AMPMCfgDUTAverageInputPower': {
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
                'name': 'dutAverageInputPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgMeasurementInterval': {
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
    'AMPMCfgMeasurementSampleRate': {
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
                'enum': 'AmpmMeasurementSampleRateMode',
                'name': 'sampleRateMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sampleRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgReferencePowerType': {
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
                'enum': 'AmpmReferencePowerType',
                'name': 'referencePowerType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgReferenceWaveform': {
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
            },
            {
                'direction': 'in',
                'enum': 'AmpmReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_AMPMCfgReferenceWaveform',
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
            },
            {
                'direction': 'in',
                'enum': 'AmpmReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgReferenceWaveformSplit': {
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
            },
            {
                'direction': 'in',
                'enum': 'AmpmReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgSynchronizationMethod': {
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
                'enum': 'AmpmSynchronizationMethod',
                'name': 'synchronizationMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMCfgThreshold': {
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
                'enum': 'AmpmThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'AmpmThresholdType',
                'name': 'thresholdType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AMPMFetchAMToAMTrace': {
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
                'name': 'referencePowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'measuredAMToAM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'curveFitAMToAM',
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
    'AMPMFetchAMToPMTrace': {
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
                'name': 'referencePowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'measuredAMToPM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'curveFitAMToPM',
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
    'AMPMFetchCompressionPoints': {
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
                'name': 'inputCompressionPoint',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'outputCompressionPoint',
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
    'AMPMFetchCurveFitCoefficients': {
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
                'name': 'amToAMCoefficients',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'amToPMCoefficients',
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
    'AMPMFetchCurveFitResidual': {
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
                'name': 'amToAMResidual',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'amToPMResidual',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AMPMFetchDUTCharacteristics': {
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
                'name': 'meanLinearGain',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'one_db_compression_point',
                'name': 'onedBCompressionPoint',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_evm',
                'name': 'meanRMSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AMPMFetchError': {
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
                'name': 'gainErrorRange',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'phaseErrorRange',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AMPMFetchProcessedMeanAcquiredWaveform': {
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
                'name': 'processedMeanAcquiredWaveform',
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
    'AMPMFetchProcessedMeanAcquiredWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_AMPMFetchProcessedMeanAcquiredWaveform',
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
                'name': 'processedMeanAcquiredWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedMeanAcquiredWaveform)'
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
    'AMPMFetchProcessedMeanAcquiredWaveformSplit': {
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
                'name': 'processedMeanAcquiredWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedMeanAcquiredWaveformQ',
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
    'AMPMFetchProcessedReferenceWaveform': {
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
                'name': 'processedReferenceWaveform',
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
    'AMPMFetchProcessedReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_AMPMFetchProcessedReferenceWaveform',
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
                'name': 'processedReferenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedReferenceWaveform)'
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
    'AMPMFetchProcessedReferenceWaveformSplit': {
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
                'name': 'processedReferenceWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedReferenceWaveformQ',
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
    'AMPMFetchRelativePhaseTrace': {
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
                'name': 'relativePhase',
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
    'AMPMFetchRelativePowerTrace': {
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
                'name': 'relativePower',
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
        'cname': 'RFmxSpecAn_AnalyzeIQ1Waveform',
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
                'name': 'bandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'measurementInterval',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'BuildCarrierString': {
        'cname': 'RFmxSpecAn_BuildCarrierString2',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'carrierNumber',
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
    'BuildHarmonicString': {
        'cname': 'RFmxSpecAn_BuildHarmonicString2',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'harmonicNumber',
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
    'BuildIntermodString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'intermodNumber',
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
    'BuildListStepString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'listName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'stepNumber',
                'type': 'int32'
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
    'BuildListString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'listName',
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
    'BuildMarkerString': {
        'cname': 'RFmxSpecAn_BuildMarkerString2',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'markerNumber',
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
        'cname': 'RFmxSpecAn_BuildOffsetString2',
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
    'BuildRangeSpurString': {
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
                'name': 'rangeNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'spurNumber',
                'type': 'int32'
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
    'BuildRangeString': {
        'cname': 'RFmxSpecAn_BuildRangeString2',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'rangeNumber',
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
    'BuildSpurString': {
        'cname': 'RFmxSpecAn_BuildSpurString2',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'spurNumber',
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
    'CCDFCfgMeasurementInterval': {
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
    'CCDFCfgNumberOfRecords': {
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
                'name': 'numberOfRecords',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CCDFCfgRBWFilter': {
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
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'CcdfRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CCDFCfgThreshold': {
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
                'enum': 'CcdfThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'CcdfThresholdType',
                'name': 'thresholdType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CCDFFetchBasicPowerProbabilities': {
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
                'name': 'tenPercentPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'onePercentPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'oneTenthPercentPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'oneHundredthPercentPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'oneThousandthPercentPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'oneTenThousandthPercentPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CCDFFetchGaussianProbabilitiesTrace': {
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
                'name': 'gaussianProbabilities',
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
    'CCDFFetchPower': {
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
                'name': 'meanPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPowerPercentile',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'measuredSamplesCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CCDFFetchProbabilitiesTrace': {
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
                'name': 'probabilities',
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
    'CCDFRead': {
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
                'name': 'meanPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPowerPercentile',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'measuredSamplesCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgAveraging': {
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
                'enum': 'ChpAveragingEnabled',
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
                'enum': 'ChpAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgCarrierOffset': {
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
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgDetector': {
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
                'enum': 'ChpDetectorType',
                'name': 'detectorType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'detectorPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgFFT': {
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
                'enum': 'ChpFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgIntegrationBandwidth': {
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
                'name': 'integrationBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgNumberOfCarriers': {
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
                'name': 'numberOfCarriers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgRBWFilter': {
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
                'enum': 'ChpRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'ChpRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgRRCFilter': {
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
                'enum': 'ChpCarrierRrcFilterEnabled',
                'name': 'rrcFilterEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgSpan': {
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
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPCfgSweepTime': {
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
                'enum': 'ChpSweepTimeAuto',
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
    'CHPFetchCarrierMeasurement': {
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
                'name': 'psd',
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
    'CHPFetchSpectrum': {
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
    'CHPFetchTotalCarrierPower': {
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
                'name': 'totalCarrierPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPRead': {
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
                'name': 'psd',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPValidateNoiseCalibrationData': {
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
                'enum': 'ChpNoiseCalibrationDataValid',
                'name': 'noiseCalibrationDataValid',
                'type': 'int32'
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
                'name': 'iqPowerEdgeLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'IQPowerEdgeTriggerSlope',
                'name': 'iqPowerEdgeSlope',
                'type': 'int32'
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
    'CfgRF': {
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
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
                'type': 'float64'
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
    'ClearNoiseCalibrationDatabase': {
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
    'CreateList': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'listName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CreateListStep': {
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
                'name': 'createdStepIndex',
                'type': 'int32'
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
    'DPDApplyDigitalPredistortion': {
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementTimeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyDigitalPredistortionInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDApplyDigitalPredistortion',
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(waveformIn)'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySizeIn/2'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementTimeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(waveformOut)'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyDigitalPredistortionSplit': {
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformInI',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'waveformInQ',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementTimeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOutI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'waveformOutQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyPreDPDSignalConditioning': {
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyPreDPDSignalConditioningInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDApplyPreDPDSignalConditioning',
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformIn',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(waveformIn)'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySizeIn/2'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(waveformOut)'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyPreDPDSignalConditioningSplit': {
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
                'name': 'x0In',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dxIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformInI',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'waveformInQ',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySizeIn'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeIn',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdApplyDpdIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOutI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'waveformOutQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgApplyDPDConfigurationInput': {
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
                'enum': 'DpdApplyDpdConfigurationInput',
                'name': 'configurationInput',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgApplyDPDLookupTableCorrectionType': {
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
                'enum': 'DpdApplyDpdLookupTableCorrectionType',
                'name': 'lutCorrectionType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgApplyDPDMemoryModelCorrectionType': {
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
                'enum': 'DpdApplyDpdMemoryModelCorrectionType',
                'name': 'memoryModelCorrectionType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgApplyDPDUserDPDPolynomial': {
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
                'name': 'dpdPolynomial',
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
    'DPDCfgApplyDPDUserDPDPolynomialInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgApplyDPDUserDPDPolynomial',
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
                'name': 'dpdPolynomial',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dpdPolynomial)'
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
    'DPDCfgApplyDPDUserDPDPolynomialSplit': {
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
                'name': 'dpdPolynomialI',
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
                'name': 'dpdPolynomialQ',
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
    'DPDCfgApplyDPDUserLookupTable': {
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
                'name': 'lutInputPowers',
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
                'name': 'lutComplexGains',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
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
    'DPDCfgApplyDPDUserLookupTableInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgApplyDPDUserLookupTable',
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
                'name': 'lutInputPowers',
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
                'name': 'lutComplexGains',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(lutComplexGains)'
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
    'DPDCfgApplyDPDUserLookupTableSplit': {
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
                'name': 'lutInputPowers',
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
                'name': 'lutComplexGainsI',
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
                'name': 'lutComplexGainsQ',
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
    'DPDCfgAveraging': {
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
                'enum': 'DpdAveragingEnabled',
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
    'DPDCfgDPDModel': {
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
                'enum': 'DpdModel',
                'name': 'dpdModel',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgDUTAverageInputPower': {
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
                'name': 'dutAverageInputPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgExtractModelTargetWaveform': {
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
                'name': 'targetWaveform',
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
    'DPDCfgExtractModelTargetWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgExtractModelTargetWaveform',
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
                'name': 'targetWaveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(targetWaveform)'
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
    'DPDCfgExtractModelTargetWaveformSplit': {
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
                'name': 'targetWaveformI',
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
                'name': 'targetWaveformQ',
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
    'DPDCfgGeneralizedMemoryPolynomialCrossTerms': {
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
                'name': 'memoryPolynomialLeadOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialLagOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialLeadMemoryDepth',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialLagMemoryDepth',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialMaximumLead',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialMaximumLag',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgIterativeDPDEnabled': {
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
                'enum': 'DpdIterativeDpdEnabled',
                'name': 'iterativeDPDEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgLookupTableAMToAMCurveFit': {
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
                'name': 'amToAMCurveFitOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdLookupTableAMToAMCurveFitType',
                'name': 'amToAMCurveFitType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgLookupTableAMToPMCurveFit': {
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
                'name': 'amToPMCurveFitOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdLookupTableAMToPMCurveFitType',
                'name': 'amToPMCurveFitType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgLookupTableStepSize': {
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
                'name': 'stepSize',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgLookupTableThreshold': {
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
                'enum': 'DpdLookupTableThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'DpdLookupTableThresholdType',
                'name': 'thresholdType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgLookupTableType': {
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
                'enum': 'DpdLookupTableType',
                'name': 'lookupTableType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgMeasurementInterval': {
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
    'DPDCfgMeasurementSampleRate': {
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
                'enum': 'DpdMeasurementSampleRateMode',
                'name': 'sampleRateMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sampleRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgMemoryPolynomial': {
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
                'name': 'memoryPolynomialOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'memoryPolynomialMemoryDepth',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgPreviousDPDPolynomial': {
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
                'name': 'previousDPDPolynomial',
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
    'DPDCfgPreviousDPDPolynomialInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgPreviousDPDPolynomial',
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
                'name': 'previousDPDPolynomial',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(previousDPDPolynomial)'
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
    'DPDCfgPreviousDPDPolynomialSplit': {
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
                'name': 'previousDPDPolynomialI',
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
                'name': 'previousDPDPolynomialQ',
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
    'DPDCfgReferenceWaveform': {
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
            },
            {
                'direction': 'in',
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgReferenceWaveform',
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
            },
            {
                'direction': 'in',
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgReferenceWaveformSplit': {
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
            },
            {
                'direction': 'in',
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgSynchronizationMethod': {
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
                'enum': 'DpdSynchronizationMethod',
                'name': 'synchronizationMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDFetchApplyDPDPreCFRPAPR': {
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
                'grpc_name': 'pre_cfr_papr',
                'name': 'preCFRPAPR',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDFetchAverageGain': {
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
                'name': 'averageGain',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDFetchDPDPolynomial': {
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
                'name': 'dpdPolynomial',
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
    'DPDFetchDPDPolynomialInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDFetchDPDPolynomial',
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
                'name': 'dpdPolynomial',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dpdPolynomial)'
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
    'DPDFetchDPDPolynomialSplit': {
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
                'name': 'dpdPolynomialI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dpdPolynomialQ',
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
    'DPDFetchDVRModel': {
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
                'name': 'dvrModel',
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
    'DPDFetchDVRModelInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDFetchDVRModel',
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
                'name': 'dvrModel',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dvrModel)'
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
    'DPDFetchDVRModelSplit': {
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
                'name': 'dvrModelI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dvrModelQ',
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
    'DPDFetchLookupTable': {
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
                'name': 'inputPowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'complexGains',
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
    'DPDFetchLookupTableInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDFetchLookupTable',
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
                'name': 'inputPowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'complexGains',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(complexGains)'
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
    'DPDFetchLookupTableSplit': {
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
                'name': 'inputPowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'complexGainsI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'complexGainsQ',
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
    'DPDFetchNMSE': {
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
                'name': 'nmse',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDFetchProcessedMeanAcquiredWaveform': {
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
                'name': 'processedMeanAcquiredWaveform',
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
    'DPDFetchProcessedMeanAcquiredWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDFetchProcessedMeanAcquiredWaveform',
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
                'name': 'processedMeanAcquiredWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedMeanAcquiredWaveform)'
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
    'DPDFetchProcessedMeanAcquiredWaveformSplit': {
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
                'name': 'processedMeanAcquiredWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedMeanAcquiredWaveformQ',
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
    'DPDFetchProcessedReferenceWaveform': {
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
                'name': 'processedReferenceWaveform',
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
    'DPDFetchProcessedReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDFetchProcessedReferenceWaveform',
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
                'name': 'processedReferenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedReferenceWaveform)'
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
    'DPDFetchProcessedReferenceWaveformSplit': {
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
                'name': 'processedReferenceWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedReferenceWaveformQ',
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
    'DeleteList': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'listName',
                'type': 'char[]'
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
    'FCntCfgAveraging': {
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
                'enum': 'FcntAveragingEnabled',
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
                'enum': 'FcntAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'FCntCfgMeasurementInterval': {
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
    'FCntCfgRBWFilter': {
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
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'FcntRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'FCntCfgThreshold': {
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
                'enum': 'FcntThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'FcntThresholdType',
                'name': 'thresholdType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'FCntFetchAllanDeviation': {
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
                'name': 'allanDeviation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'FCntFetchFrequencyTrace': {
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
                'name': 'frequencyTrace',
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
    'FCntFetchMeasurement': {
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
                'name': 'averageRelativeFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageAbsoluteFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhase',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'FCntFetchPhaseTrace': {
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
                'name': 'phaseTrace',
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
    'FCntFetchPowerTrace': {
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
                'name': 'powerTrace',
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
    'FCntRead': {
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
                'name': 'averageRelativeFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageAbsoluteFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhase',
                'type': 'float64'
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
    'HarmCfgAutoHarmonics': {
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
                'enum': 'HarmAutoHarmonicsSetupEnabled',
                'name': 'autoHarmonicsSetupEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'HarmCfgAveraging': {
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
                'enum': 'HarmAveragingEnabled',
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
                'enum': 'HarmAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'HarmCfgFundamentalMeasurementInterval': {
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
    'HarmCfgFundamentalRBW': {
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
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'HarmRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'HarmCfgHarmonic': {
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
                'name': 'harmonicOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'harmonicBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'HarmHarmonicEnabled',
                'name': 'harmonicEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'harmonicMeasurementInterval',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'HarmCfgHarmonicArray': {
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
                'name': 'harmonicOrder',
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
                'name': 'harmonicBandwidth',
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
                'enum': 'HarmHarmonicEnabled',
                'name': 'harmonicEnabled',
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
                'name': 'harmonicMeasurementInterval',
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
    'HarmCfgNumberOfHarmonics': {
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
                'name': 'numberOfHarmonics',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'HarmFetchHarmonicMeasurement': {
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
                'name': 'averageRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'HarmFetchHarmonicMeasurementArray': {
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
                'name': 'averageRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'averageAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'rbw',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'frequency',
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
    'HarmFetchHarmonicPowerTrace': {
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
    'HarmFetchTHD': {
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
                'name': 'totalHarmonicDistortion',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageFundamentalPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'fundamentalFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'HarmRead': {
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
                'name': 'totalHarmonicDistortion',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageFundamentalPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgEqualizerCoefficients': {
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
                'name': 'equalizerCoefficients',
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
    'IDPDCfgEqualizerCoefficientsInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDCfgEqualizerCoefficients',
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
                'name': 'equalizerCoefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerCoefficients)'
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
    'IDPDCfgEqualizerCoefficientsSplit': {
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
                'name': 'equalizerCoefficientsI',
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
                'name': 'equalizerCoefficientsQ',
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
    'IDPDCfgPredistortedWaveform': {
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
                'name': 'predistortedWaveform',
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
                'name': 'targetGain',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgPredistortedWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDCfgPredistortedWaveform',
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
                'name': 'predistortedWaveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(predistortedWaveform)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            },
            {
                'direction': 'in',
                'name': 'targetGain',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgPredistortedWaveformSplit': {
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
                'name': 'predistortedWaveformI',
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
                'name': 'predistortedWaveformQ',
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
                'name': 'targetGain',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgReferenceWaveform': {
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
            },
            {
                'direction': 'in',
                'enum': 'IdpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IdpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDCfgReferenceWaveform',
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
            },
            {
                'direction': 'in',
                'enum': 'IdpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IdpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IDPDCfgReferenceWaveformSplit': {
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
            },
            {
                'direction': 'in',
                'enum': 'IdpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IdpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IDPDFetchEqualizerCoefficients': {
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
                'name': 'equalizerCoefficients',
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
    'IDPDFetchEqualizerCoefficientsInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDFetchEqualizerCoefficients',
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
                'name': 'equalizerCoefficients',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerCoefficients)'
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
    'IDPDFetchEqualizerCoefficientsSplit': {
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
                'name': 'equalizerCoefficientsI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'equalizerCoefficientsQ',
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
    'IDPDFetchPredistortedWaveform': {
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
                'name': 'predistortedWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'float64'
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
    'IDPDFetchPredistortedWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDFetchPredistortedWaveform',
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
                'name': 'predistortedWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(predistortedWaveform)'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'float64'
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
    'IDPDFetchPredistortedWaveformSplit': {
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
                'name': 'predistortedWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'predistortedWaveformQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'gain',
                'type': 'float64'
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
    'IDPDFetchProcessedMeanAcquiredWaveform': {
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
                'name': 'processedMeanAcquiredWaveform',
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
    'IDPDFetchProcessedMeanAcquiredWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDFetchProcessedMeanAcquiredWaveform',
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
                'name': 'processedMeanAcquiredWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedMeanAcquiredWaveform)'
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
    'IDPDFetchProcessedMeanAcquiredWaveformSplit': {
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
                'name': 'processedMeanAcquiredWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedMeanAcquiredWaveformQ',
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
    'IDPDFetchProcessedReferenceWaveform': {
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
                'name': 'processedReferenceWaveform',
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
    'IDPDFetchProcessedReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDFetchProcessedReferenceWaveform',
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
                'name': 'processedReferenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(processedReferenceWaveform)'
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
    'IDPDFetchProcessedReferenceWaveformSplit': {
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
                'name': 'processedReferenceWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'processedReferenceWaveformQ',
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
    'IDPDGetEqualizerReferenceWaveform': {
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
                'name': 'equalizerReferenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
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
    'IDPDGetEqualizerReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxSpecAn_IDPDGetEqualizerReferenceWaveform',
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
                'name': 'equalizerReferenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerReferenceWaveform)'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
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
    'IDPDGetEqualizerReferenceWaveformSplit': {
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
                'name': 'equalizerReferenceWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'equalizerReferenceWaveformQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'papr',
                'type': 'float64'
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
    'IMCfgAutoIntermodsSetup': {
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
                'enum': 'IMAutoIntermodsSetupEnabled',
                'name': 'autoIntermodsSetupEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'maximumIntermodOrder',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgAveraging': {
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
                'enum': 'IMAveragingEnabled',
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
                'enum': 'IMAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgFFT': {
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
                'enum': 'IMFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgFrequencyDefinition': {
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
                'enum': 'IMFrequencyDefinition',
                'name': 'frequencyDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgFundamentalTones': {
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
                'name': 'lowerToneFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'upperToneFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgIntermod': {
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
                'name': 'intermodOrder',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'lowerIntermodFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'upperIntermodFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'IMIntermodSide',
                'name': 'intermodSide',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IMIntermodEnabled',
                'name': 'intermodEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgIntermodArray': {
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
                'name': 'intermodOrder',
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
                'name': 'lowerIntermodFrequency',
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
                'name': 'upperIntermodFrequency',
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
                'enum': 'IMIntermodSide',
                'name': 'intermodSide',
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
                'enum': 'IMIntermodEnabled',
                'name': 'intermodEnabled',
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
    'IMCfgMeasurementMethod': {
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
                'enum': 'IMMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgNumberOfIntermods': {
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
                'name': 'numberOfIntermods',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgRBWFilter': {
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
                'enum': 'IMRbwFilterAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'IMRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IMCfgSweepTime': {
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
                'enum': 'IMSweepTimeAuto',
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
    'IMFetchFundamentalMeasurement': {
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
                'name': 'lowerTonePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperTonePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IMFetchInterceptPower': {
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
                'name': 'intermodOrder',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'worstCaseOutputInterceptPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerOutputInterceptPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperOutputInterceptPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IMFetchInterceptPowerArray': {
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
                'name': 'intermodOrder',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'worstCaseOutputInterceptPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'lowerOutputInterceptPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperOutputInterceptPower',
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
    'IMFetchIntermodMeasurement': {
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
                'name': 'intermodOrder',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'lowerIntermodPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperIntermodPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IMFetchIntermodMeasurementArray': {
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
                'name': 'intermodOrder',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'lowerIntermodPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperIntermodPower',
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
    'IMFetchSpectrum': {
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
                'name': 'spectrumIndex',
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
                'name': 'spectrum',
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
    'IQCfgAcquisition': {
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
                'name': 'sampleRate',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'numberOfRecords',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'acquisitionTime',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'pretriggerTime',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IQCfgBandwidth': {
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
                'enum': 'IQBandwidthAuto',
                'name': 'bandwidthAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'bandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'IQFetchData': {
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
                'name': 'recordToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
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
                'name': 'data',
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
    'IQFetchDataInterleavedIQ': {
        'cname': 'RFmxSpecAn_IQFetchData',
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
                'name': 'recordToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
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
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(data)'
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
    'IQFetchDataSplit': {
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
                'name': 'recordToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
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
                'name': 'dataI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dataQ',
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
    'IQGetRecordsDone': {
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
                'name': 'recordsDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'Initialize': {
        'custom_close': 'Close(id, RFMXSPECAN_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXSPECAN_VAL_FALSE)',
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
    'MarkerCfgBandSpan': {
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
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgFunctionType': {
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
                'enum': 'MarkerFunctionType',
                'name': 'functionType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgNumberOfMarkers': {
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
                'name': 'numberOfMarkers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgPeakExcursion': {
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
                'enum': 'MarkerPeakExcursionEnabled',
                'name': 'peakExcursionEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'peakExcursion',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgReferenceMarker': {
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
                'name': 'referenceMarker',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgThreshold': {
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
                'enum': 'MarkerThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'threshold',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgTrace': {
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
                'enum': 'MarkerTrace',
                'name': 'trace',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgType': {
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
                'enum': 'MarkerType',
                'name': 'markerType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgXLocation': {
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
                'name': 'markerXLocation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgYLocation': {
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
                'name': 'markerYLocation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerFetchFunctionValue': {
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
                'name': 'functionValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerFetchXY': {
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
                'name': 'markerXLocation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'markerYLocation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerNextPeak': {
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
                'enum': 'MarkerNextPeak',
                'name': 'nextPeak',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'nextPeakFound',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'MarkerPeakSearch': {
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
                'name': 'numberOfPeaks',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgAveraging': {
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
                'enum': 'NFAveragingEnabled',
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
    'NFCfgCalibrationLoss': {
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
                'enum': 'NFCalibrationLossCompensationEnabled',
                'name': 'calibrationLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'calibrationLossFrequency',
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
                'name': 'calibrationLoss',
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
                'name': 'calibrationLossTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgColdSourceDUTSParameters': {
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
                'grpc_name': 'dut_s_parameters_frequency',
                'name': 'dutsParametersFrequency',
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
                'grpc_name': 'dut_s21',
                'name': 'duts21',
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
                'grpc_name': 'dut_s12',
                'name': 'duts12',
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
                'grpc_name': 'dut_s11',
                'name': 'duts11',
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
                'grpc_name': 'dut_s22',
                'name': 'duts22',
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
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgColdSourceInputTermination': {
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
                'name': 'terminationVSWR',
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
                'name': 'terminationVSWRFrequency',
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
                'name': 'terminationTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgColdSourceMode': {
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
                'enum': 'NFColdSourceMode',
                'name': 'coldSourceMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgDUTInputLoss': {
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
                'enum': 'NFDutInputLossCompensationEnabled',
                'name': 'dutInputLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutInputLossFrequency',
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
                'name': 'dutInputLoss',
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
                'name': 'dutInputLossTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgDUTOutputLoss': {
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
                'enum': 'NFDutOutputLossCompensationEnabled',
                'name': 'dutOutputLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutOutputLossFrequency',
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
                'name': 'dutOutputLoss',
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
                'name': 'dutOutputLossTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgFrequencyList': {
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
                'name': 'frequencyList',
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
    'NFCfgFrequencyListStartStopPoints': {
        'cname': 'RFmxSpecAn_NFCfgFrequencyList_StartStopPoints',
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
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'numberOfPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgFrequencyListStartStopStep': {
        'cname': 'RFmxSpecAn_NFCfgFrequencyList_StartStopStep',
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
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stepSize',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgMeasurementBandwidth': {
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
                'name': 'measurementBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgMeasurementInterval': {
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
    'NFCfgMeasurementMethod': {
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
                'enum': 'NFMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgYFactorMode': {
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
                'enum': 'NFYFactorMode',
                'name': 'yFactorMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgYFactorNoiseSourceENR': {
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
                'name': 'enrFrequency',
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
                'name': 'enr',
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
                'name': 'coldTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'offTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgYFactorNoiseSourceLoss': {
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
                'enum': 'NFYFactorNoiseSourceLossCompensationEnabled',
                'name': 'noiseSourceLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'noiseSourceLossFrequency',
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
                'name': 'noiseSourceLoss',
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
                'name': 'noiseSourceLossTemperature',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFCfgYFactorNoiseSourceSettlingTime': {
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
                'name': 'settlingTime',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFClearCalibrationDatabase': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'calibrationSetupID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'NFFetchAnalyzerNoiseFigure': {
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
                'name': 'analyzerNoiseFigure',
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
    'NFFetchColdSourcePower': {
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
                'name': 'coldSourcePower',
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
    'NFFetchDUTNoiseFigureAndGain': {
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
                'name': 'dutNoiseFigure',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'dutNoiseTemperature',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'dutGain',
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
    'NFFetchYFactorPowers': {
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
                'name': 'hotPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'coldPower',
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
    'NFFetchYFactors': {
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
                'name': 'measurementYFactor',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'calibrationYFactor',
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
    'NFLoadCalibrationLossFromS2p': {
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
                'enum': 'NFCalibrationLossCompensationEnabled',
                'name': 'calibrationLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'calibrationLossS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFCalibrationLossS2pSParameterOrientation',
                'name': 'calibrationLossSParameterOrientation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'calibrationLossTemperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadColdSourceDUTSParametersFromS2p': {
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
                'grpc_name': 'dut_s_parameters_s2p_file_path',
                'name': 'dutsParametersS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFColdSourceDutS2pSParameterOrientation',
                'grpc_name': 'dut_s_parameter_orientation',
                'name': 'dutsParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadColdSourceInputTerminationFromS1p': {
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
                'name': 'terminationS1pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'terminationTemperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadDUTInputLossFromS2p': {
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
                'enum': 'NFDutInputLossCompensationEnabled',
                'name': 'dutInputLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutInputLossS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFDutInputLossS2pSParameterOrientation',
                'name': 'dutInputLossSParameterOrientation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutInputLossTemperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadDUTOutputLossFromS2p': {
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
                'enum': 'NFDutOutputLossCompensationEnabled',
                'name': 'dutOutputLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutOutputLossS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFDutOutputLossS2pSParameterOrientation',
                'name': 'dutOutputLossSParameterOrientation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'dutOutputLossTemperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadExternalPreampGainFromS2p': {
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
                'enum': 'NFExternalPreampPresent',
                'name': 'externalPreampPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'externalPreampGainS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFExternalPreampGainS2pSParameterOrientation',
                'name': 'externalPreampGainSParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'NFLoadYFactorNoiseSourceLossFromS2p': {
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
                'enum': 'NFYFactorNoiseSourceLossCompensationEnabled',
                'name': 'noiseSourceLossCompensationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'noiseSourceLossS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NFYFactorNoiseSourceLossS2pSParameterOrientation',
                'name': 'noiseSourceLossSParameterOrientation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'noiseSourceLossTemperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFRecommendReferenceLevel': {
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
                'name': 'dutMaxGain',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dutMaxNoiseFigure',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'NFValidateCalibrationData': {
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
                'enum': 'NFCalibrationDataValid',
                'name': 'calibrationDataValid',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgAveraging': {
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
                'enum': 'ObwAveragingEnabled',
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
                'enum': 'ObwAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgBandwidthPercentage': {
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
                'name': 'bandwidthPercentage',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgFFT': {
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
                'enum': 'ObwFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgPowerUnits': {
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
                'enum': 'ObwPowerUnits',
                'name': 'powerUnits',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgRBWFilter': {
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
                'enum': 'ObwRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'ObwRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgSpan': {
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
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OBWCfgSweepTime': {
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
                'enum': 'ObwSweepTimeAuto',
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
    'OBWFetchMeasurement': {
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
                'name': 'occupiedBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyResolution',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'stopFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'OBWFetchSpectrumTrace': {
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
    'OBWRead': {
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
                'name': 'occupiedBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyResolution',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'stopFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgMeasurementBandwidth': {
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
                'name': 'measurementBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgMeasurementInterval': {
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
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'measurementLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgMeasurementIntervalMode': {
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
                'enum': 'PavtMeasurementIntervalMode',
                'name': 'measurementIntervalMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgMeasurementLocationType': {
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
                'enum': 'PavtMeasurementLocationType',
                'name': 'measurementLocationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgNumberOfSegments': {
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
                'name': 'numberOfSegments',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgSegmentMeasurementInterval': {
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
                'name': 'segmentMeasurementOffset',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'segmentMeasurementLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgSegmentMeasurementIntervalArray': {
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
                'name': 'segmentMeasurementOffset',
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
                'name': 'segmentMeasurementLength',
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
    'PAVTCfgSegmentStartTimeList': {
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
                'name': 'segmentStartTime',
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
    'PAVTCfgSegmentStartTimeStep': {
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
                'name': 'numberOfSegments',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'segment0StartTime',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'segmentInterval',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgSegmentType': {
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
                'enum': 'PavtSegmentType',
                'name': 'segmentType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PAVTCfgSegmentTypeArray': {
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
                'enum': 'PavtSegmentType',
                'name': 'segmentType',
                'size': {
                    'mechanism': 'len',
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
    'PAVTFetchAmplitudeTrace': {
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
                'name': 'traceIndex',
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
                'name': 'amplitude',
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
    'PAVTFetchPhaseAndAmplitude': {
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
                'name': 'meanRelativePhase',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRelativeAmplitude',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsolutePhase',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteAmplitude',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PAVTFetchPhaseAndAmplitudeArray': {
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
                'name': 'meanRelativePhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanRelativeAmplitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanAbsolutePhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteAmplitude',
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
    'PAVTFetchPhaseTrace': {
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
                'name': 'traceIndex',
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
                'name': 'phase',
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
    'PhaseNoiseCfgAutoRange': {
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
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'rbwPercentage',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgAveragingMultiplier': {
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
                'name': 'averagingMultiplier',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgCancellation': {
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
                'enum': 'PhaseNoiseCancellationEnabled',
                'name': 'cancellationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'cancellationThreshold',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'frequency',
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
                'name': 'referencePhaseNoise',
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
    'PhaseNoiseCfgIntegratedNoise': {
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
                'enum': 'PhaseNoiseIntegratedNoiseRangeDefinition',
                'name': 'integratedNoiseRangeDefinition',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'integratedNoiseStartFrequency',
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
                'name': 'integratedNoiseStopFrequency',
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
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgNumberOfRanges': {
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
                'name': 'numberOfRanges',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgRangeArray': {
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
                'name': 'rangeStartFrequency',
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
                'name': 'rangeStopFrequency',
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
                'name': 'rangeRBWPercentage',
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
                'name': 'rangeAveragingCount',
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
    'PhaseNoiseCfgRangeDefinition': {
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
                'enum': 'PhaseNoiseRangeDefinition',
                'name': 'rangeDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgSmoothing': {
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
                'enum': 'PhaseNoiseSmoothingType',
                'name': 'smoothingType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'smoothingPercentage',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseCfgSpotNoiseFrequencyList': {
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
                'name': 'frequencyList',
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
    'PhaseNoiseCfgSpurRemoval': {
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
                'enum': 'PhaseNoiseSpurRemovalEnabled',
                'name': 'spurRemovalEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'peakExcursion',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseFetchCarrierMeasurement': {
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
                'name': 'carrierFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'carrierPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PhaseNoiseFetchIntegratedNoise': {
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
                'name': 'integratedPhaseNoise',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'residualPMInRadian',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'residualPMInDegree',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'residualFM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'jitter',
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
    'PhaseNoiseFetchMeasuredLogPlotTrace': {
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
                'name': 'frequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'measuredPhaseNoise',
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
    'PhaseNoiseFetchSmoothedLogPlotTrace': {
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
                'name': 'frequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'smoothedPhaseNoise',
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
    'PhaseNoiseFetchSpotNoise': {
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
                'name': 'spotPhaseNoise',
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
    'PowerListCfgRBWFilterArray': {
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
                'name': 'rbw',
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
                'name': 'rbwFilterType',
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
                'name': 'rrcAlpha',
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
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerListFetchMaximumPowerArray': {
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
                'name': 'maximumPower',
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
    'PowerListFetchMeanAbsolutePowerArray': {
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
                'name': 'meanAbsolutePower',
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
    'PowerListFetchMinimumPowerArray': {
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
                'name': 'minimumPower',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
    'SEMCfgCarrierChannelBandwidth': {
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
                'name': 'carrierChannelBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgCarrierEnabled': {
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
                'enum': 'SemCarrierEnabled',
                'name': 'carrierEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgCarrierFrequency': {
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
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgCarrierIntegrationBandwidth': {
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
                'name': 'integrationBandwidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgCarrierRBWFilter': {
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
                'enum': 'SemCarrierRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SemCarrierRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgCarrierRRCFilter': {
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
                'enum': 'SemCarrierRrcFilterEnabled',
                'name': 'rrcFilterEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgFFT': {
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
                'enum': 'SemFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgNumberOfCarriers': {
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
                'name': 'numberOfCarriers',
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
    'SEMCfgOffsetAbsoluteLimit': {
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
                'enum': 'SemOffsetAbsoluteLimitMode',
                'name': 'absoluteLimitMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'absoluteLimitStart',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'absoluteLimitStop',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetAbsoluteLimitArray': {
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
                'enum': 'SemOffsetAbsoluteLimitMode',
                'name': 'absoluteLimitMode',
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
                'name': 'absoluteLimitStart',
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
                'name': 'absoluteLimitStop',
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
    'SEMCfgOffsetBandwidthIntegral': {
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
                'name': 'bandwidthIntegral',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetFrequency': {
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
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'offsetStopFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetEnabled',
                'name': 'offsetEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetSideband',
                'name': 'offsetSideband',
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
                'enum': 'SemOffsetEnabled',
                'name': 'offsetEnabled',
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
    'SEMCfgOffsetFrequencyDefinition': {
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
                'enum': 'SemOffsetFrequencyDefinition',
                'name': 'offsetFrequencyDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetLimitFailMask': {
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
                'enum': 'SemOffsetLimitFailMask',
                'name': 'limitFailMask',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetRBWFilter': {
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
                'enum': 'SemOffsetRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetRBWFilterArray': {
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
                'enum': 'SemOffsetRbwAutoBandwidth',
                'name': 'rbwAuto',
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
                'name': 'rbw',
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
                'enum': 'SemOffsetRbwFilterType',
                'name': 'rbwFilterType',
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
    'SEMCfgOffsetRelativeAttenuation': {
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
                'name': 'relativeAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetRelativeAttenuationArray': {
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
                'name': 'relativeAttenuation',
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
    'SEMCfgOffsetRelativeLimit': {
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
                'enum': 'SemOffsetRelativeLimitMode',
                'name': 'relativeLimitMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'relativeLimitStart',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'relativeLimitStop',
                'type': 'float64'
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
                'enum': 'SemOffsetRelativeLimitMode',
                'name': 'relativeLimitMode',
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
    'SEMCfgPowerUnits': {
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
                'enum': 'SemPowerUnits',
                'name': 'powerUnits',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgReferenceType': {
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
                'enum': 'SemReferenceType',
                'name': 'referenceType',
                'type': 'int32'
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
    'SEMFetchAbsoluteMaskTrace': {
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
                'name': 'absoluteMask',
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
                'name': 'totalRelativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchCompositeMeasurementStatus': {
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
                'enum': 'SemCompositeMeasurementStatus',
                'name': 'compositeMeasurementStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchFrequencyResolution': {
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
                'name': 'frequencyResolution',
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
    'SEMFetchRelativeMaskTrace': {
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
                'name': 'relativeMask',
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
    'SEMFetchTotalCarrierPower': {
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
                'name': 'totalCarrierPower',
                'type': 'float64'
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
                'grpc_type': 'NiRFmxSpecAnAttribute',
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
    'SpectrumCfgAveraging': {
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
                'enum': 'SpectrumAveragingEnabled',
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
                'enum': 'SpectrumAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgDetector': {
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
                'enum': 'SpectrumDetectorType',
                'name': 'detectorType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'detectorPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgFFT': {
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
                'enum': 'SpectrumFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftPadding',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgFrequencyStartStop': {
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
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgMeasurementMethod': {
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
                'enum': 'SpectrumMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgNoiseCompensationEnabled': {
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
                'enum': 'SpectrumNoiseCompensationEnabled',
                'name': 'noiseCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgPowerUnits': {
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
                'enum': 'SpectrumPowerUnits',
                'name': 'spectrumPowerUnits',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgRBWFilter': {
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
                'enum': 'SpectrumRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SpectrumRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgSpan': {
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
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumCfgSweepTime': {
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
                'enum': 'SpectrumSweepTimeAuto',
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
    'SpectrumCfgVBWFilter': {
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
                'enum': 'SpectrumVbwFilterAutoBandwidth',
                'name': 'vbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'vbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'vbwToRBWRatio',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumFetchMeasurement': {
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
                'name': 'peakAmplitude',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyResolution',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpectrumFetchPowerTrace': {
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
    'SpectrumFetchSpectrum': {
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
    'SpectrumRead': {
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
    'SpectrumValidateNoiseCalibrationData': {
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
                'enum': 'SpectrumNoiseCalibrationDataValid',
                'name': 'noiseCalibrationDataValid',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgAveraging': {
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
                'enum': 'SpurAveragingEnabled',
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
                'enum': 'SpurAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgFFTWindowType': {
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
                'enum': 'SpurFftWindow',
                'name': 'fftWindow',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgNumberOfRanges': {
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
                'name': 'numberOfRanges',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeAbsoluteLimit': {
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
                'enum': 'SpurAbsoluteLimitMode',
                'name': 'absoluteLimitMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'absoluteLimitStart',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'absoluteLimitStop',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeAbsoluteLimitArray': {
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
                'enum': 'SpurAbsoluteLimitMode',
                'name': 'absoluteLimitMode',
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
                'name': 'absoluteLimitStart',
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
                'name': 'absoluteLimitStop',
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
    'SpurCfgRangeDetector': {
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
                'enum': 'SpurRangeDetectorType',
                'name': 'detectorType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'detectorPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeDetectorArray': {
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
                'enum': 'SpurRangeDetectorType',
                'name': 'detectorType',
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
                'name': 'detectorPoints',
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
    'SpurCfgRangeFrequency': {
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
                'name': 'startFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'stopFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SpurRangeEnabled',
                'name': 'rangeEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeFrequencyArray': {
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
                'name': 'startFrequency',
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
                'name': 'stopFrequency',
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
                'enum': 'SpurRangeEnabled',
                'name': 'rangeEnabled',
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
    'SpurCfgRangeNumberOfSpursToReport': {
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
                'name': 'numberOfSpursToReport',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeNumberOfSpursToReportArray': {
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
                'name': 'numberOfSpursToReport',
                'size': {
                    'mechanism': 'len',
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
    'SpurCfgRangePeakCriteria': {
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
                'name': 'threshold',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'excursion',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangePeakCriteriaArray': {
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
                'name': 'threshold',
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
                'name': 'excursion',
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
    'SpurCfgRangeRBWArray': {
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
                'enum': 'SpurRbwAutoBandwidth',
                'name': 'rbwAuto',
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
                'name': 'rbw',
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
                'enum': 'SpurRbwFilterType',
                'name': 'rbwFilterType',
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
    'SpurCfgRangeRBWFilter': {
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
                'enum': 'SpurRbwAutoBandwidth',
                'name': 'rbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SpurRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeRelativeAttenuation': {
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
                'name': 'relativeAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeRelativeAttenuationArray': {
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
                'name': 'relativeAttenuation',
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
    'SpurCfgRangeSweepTime': {
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
                'enum': 'SpurSweepTimeAuto',
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
    'SpurCfgRangeSweepTimeArray': {
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
                'enum': 'SpurSweepTimeAuto',
                'name': 'sweepTimeAuto',
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
                'name': 'sweepTimeInterval',
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
    'SpurCfgRangeVBWFilter': {
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
                'enum': 'SpurRangeVbwFilterAutoBandwidth',
                'name': 'vbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'vbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'vbwToRBWRatio',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpurCfgRangeVBWFilterArray': {
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
                'enum': 'SpurRangeVbwFilterAutoBandwidth',
                'name': 'vbwAuto',
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
                'name': 'vbw',
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
                'name': 'vbwToRBWRatio',
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
    'SpurCfgTraceRangeIndex': {
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
                'name': 'traceRangeIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurFetchAllSpurs': {
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
                'name': 'spurFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurAmplitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurMargin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurAbsoluteLimit',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurRangeIndex',
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
    'SpurFetchMeasurementStatus': {
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
                'enum': 'SpurMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurFetchRangeAbsoluteLimitTrace': {
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
                'name': 'absoluteLimit',
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
    'SpurFetchRangeSpectrumTrace': {
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
                'name': 'rangeSpectrum',
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
    'SpurFetchRangeStatus': {
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
                'enum': 'SpurRangeStatus',
                'name': 'rangeStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'detectedSpurs',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SpurFetchRangeStatusArray': {
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
                'enum': 'SpurRangeStatus',
                'name': 'rangeStatus',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'numberOfDetectedSpurs',
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
    'SpurFetchSpurMeasurement': {
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
                'name': 'spurFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spurAmplitude',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spurMargin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spurAbsoluteLimit',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SpurFetchSpurMeasurementArray': {
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
                'name': 'spurFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurAmplitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurAbsoluteLimit',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'spurMargin',
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
            },
            {
                'direction': 'in',
                'enum': 'TxpAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgMeasurementInterval': {
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
    'TXPCfgRBWFilter': {
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
                'name': 'rbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'TxpRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgThreshold': {
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
                'enum': 'TxpThresholdEnabled',
                'name': 'thresholdEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'thresholdLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'TxpThresholdType',
                'name': 'thresholdType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgVBWFilter': {
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
                'enum': 'TxpVbwFilterAutoBandwidth',
                'name': 'vbwAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'vbw',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'vbwToRBWRatio',
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
                'name': 'averageMeanPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakToAverageRatio',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'minimumPower',
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
    'TXPRead': {
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
                'name': 'averageMeanPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakToAverageRatio',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'minimumPower',
                'type': 'float64'
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan/functions_addon.py sha256=3613f100da88fa33308ac74c5ad1526c7672a7b897b402c1db0de0ac9ab54ccc bytes=3379 -->
## FILE: source/codegen/metadata/nirfmxspecan/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan/functions_addon.py`
- sha256: `3613f100da88fa33308ac74c5ad1526c7672a7b897b402c1db0de0ac9ab54ccc`
- bytes: 3379

````python
functions_override_metadata = {
    'IDPDCfgReferenceWaveform': {
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
            },
            {
                'direction': 'in',
                'enum': 'IdpdReferenceWaveformIdleDurationPresent',
                'grpc_raw_field_number': '6',
                'grpc_field_number': '8',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IdpdSignalType',
                'grpc_raw_field_number': '7',
                'grpc_field_number': '9',
                'name': 'signalType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DPDCfgApplyDPDUserLookupTableInterleavedIQ': {
        'cname': 'RFmxSpecAn_DPDCfgApplyDPDUserLookupTable',
        'codegen_method': 'CustomCode',
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
                'name': 'lutInputPowers',
                'size': {
                    'mechanism': 'custom-code',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'lutComplexGains',
                'size': {
                    'mechanism': 'custom-code',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(lutComplexGains)'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'name': 'arraySize',
                'type': 'int32',
            }
        ],
        'returns': 'int32'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/config.py sha256=a7182cbdbfe399fa8a0c849136ec459c16ecb0a119e18e0d732965f182e43f9b bytes=1991 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/config.py`
- sha256: `a7182cbdbfe399fa8a0c849136ec459c16ecb0a119e18e0d732965f182e43f9b`
- bytes: 1991

````python
# -*- coding: utf-8 -*-
config = {
    "code_readiness": "Release",
    "is_restricted": True,
    "api_version": "26.0.0",
    "c_header": "niRFmxSpecAn.h",
    "c_function_prefix": "RFmxSpecAn_",
    "service_class_prefix": "NiRFmxSpecAnRestricted",
    "java_package": "com.ni.grpc.nirfmxspecanrestricted",
    "csharp_namespace": "NationalInstruments.Grpc.NiRFmxSpecAnRestricted",
    "namespace_component": "nirfmxspecan_restricted",
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
    "driver_name": "NI-RFMXSPECAN-RESTRICTED",
    "resource_handle_type": "niRFmxInstrHandle",
    "status_ok": "status >= 0",
    "windows_only": True,
    "library_info": {
        "Linux": {
            "64bit": {
                "name": "nirfmxspecan",
                "type": "cdll",
                "abi_version": "1"
            }
        },
        "Windows": {
            "32bit": {
                "name": "niRFmxSpecAn.dll",
                "type": "windll"
            },
            "64bit": {
                "name": "niRFmxSpecAn.dll",
                "type": "cdll"
            }
        },
    },
    "linux_rt_support": False,
    "metadata_version": "0.1",
    "module_name": "nirfmxspecan_restricted",
    "session_class_description": "An NI-RFmxSpecAn instrument handle",
    'session_handle_parameter_name': 'instrumentHandle',
    "duplicate_resource_handles_allowed": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/enums.py sha256=a5295ee19bbb7fae0faad9dcd62b7ecb117753cc850b08516d0a511d009b7a0e bytes=1943 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/enums.py`
- sha256: `a5295ee19bbb7fae0faad9dcd62b7ecb117753cc850b08516d0a511d009b7a0e`
- bytes: 1943

````python
enums = {
    'IQDeleteOnFetch': {
        'values': [
            {
                'name': 'DEFAULT',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            },
            {
                'name': 'FALSE',
                'value': 2
            }
        ]
    },
    'AmpmReferenceWaveformIdleDurationPresent': {
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
    'AmpmSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
                'value': 1
            }
        ]
    },
    'DpdReferenceWaveformIdleDurationPresent': {
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
    'DpdSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
                'value': 1
            }
        ]
    },
    'IdpdReferenceWaveformIdleDurationPresent': {
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
    'IdpdSignalType': {
        'values': [
            {
                'name': 'MODULATED',
                'value': 0
            },
            {
                'name': 'TONES',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/functions.py sha256=04fe1aee23ba413a57853420642e4632f727a8f4fca31a47dbbc309eb636ad94 bytes=12548 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/functions.py`
- sha256: `04fe1aee23ba413a57853420642e4632f727a8f4fca31a47dbbc309eb636ad94`
- bytes: 12548

````python
functions = {
    'AMPMLoadReferenceWaveformFromTDMSFile': {
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
                'enum': 'AmpmReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AmpmSignalType',
                'name': 'signalType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CacheResult': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle',
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'selectorStringOutSize'
                },
                'type': 'char[]',
            },
        ],
        'returns': 'int32',
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
    'IQFetchDataOverrideBehavior': {
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
                'name': 'recordToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'enum': 'IQDeleteOnFetch',
                'name': 'deleteOnFetch',
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
                'name': 'data',
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
    'DPDApplyDigitalPredistortionToWaveformFromTDMSFile': {
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
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementTimeout',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'PAPR',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'powerOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDApplyPreDPDSignalConditioningToWaveformFromTDMSFile': {
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
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'x0Out',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dxOut',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveformOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySizeOut',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySizeOut',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'PAPR',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DPDLoadReferenceWaveformFromTDMSFile': {
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
                'enum': 'DpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'IDPDLoadReferenceWaveformFromTDMSFile': {
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
                'enum': 'IdpdReferenceWaveformIdleDurationPresent',
                'name': 'idleDurationPresent',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'IdpdSignalType',
                'name': 'signalType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxspecan_restricted/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxspecan_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxspecan_restricted/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/__init__.py`
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
