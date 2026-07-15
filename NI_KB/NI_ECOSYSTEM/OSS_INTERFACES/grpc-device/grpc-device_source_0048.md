# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/functions.py sha256=da923bf2188b7bfdd339d54c08c4261b20cc6906792a0d74d936000fc42c70b0 bytes=395718 -->
## FILE: source/codegen/metadata/nirfmxlte/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/functions.py`
- sha256: `da923bf2188b7bfdd339d54c08c4261b20cc6906792a0d74d936000fc42c70b0`
- bytes: 395718

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
    'ACPCfgConfigurableNumberOfOffsetsEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AcpConfigurableNumberOfOffsetsEnabled',
                'name': 'configurableNumberOfOffsetsEnabled',
                'type': 'int32'
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
    'ACPCfgNumberOfEUTRAOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfEUTRAOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfGSMOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfGSMOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfUTRAOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfUTRAOffsets',
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
    'ACPCfgUTRAAndEUTRAOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfUTRAOffsets',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfEUTRAOffsets',
                'type': 'int32'
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
    'ACPFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ACPFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativePower',
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
    'ACPFetchSubblockMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
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
    'ACPFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
        'cname': 'RFmxLTE_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'BuildClusterString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'clusterNumber',
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
    'BuildPDSCHString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pdschNumber',
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
    'BuildSubblockString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'subblockNumber',
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
    'BuildSubframeString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'subframeNumber',
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
    'CHPCfgIntegrationBandwidthType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ChpIntegrationBandwidthType',
                'name': 'integrationBandwidthType',
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
    'CHPFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CHPFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativePower',
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
    'CHPFetchSubblockMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
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
    'CHPFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
    'CfgAutoDMRSDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AutoDmrsDetectionEnabled',
                'name': 'autoDMRSDetectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgAutoNPUSCHChannelDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AutoNPuschChannelDetectionEnabled',
                'name': 'autoNPUSCHChannelDetectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgAutoResourceBlockDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AutoResourceBlockDetectionEnabled',
                'name': 'autoResourceBlockDetectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgBand': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'band',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgCellSpecificRatio': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkUserDefinedRatio',
                'name': 'cellSpecificRatio',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgComponentCarrier': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierBandwidth',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'cellID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgComponentCarrierArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierBandwidth',
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
                'name': 'componentCarrierFrequency',
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
                'name': 'cellID',
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
    'CfgComponentCarrierSpacing': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ComponentCarrierSpacingType',
                'name': 'componentCarrierSpacingType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierAtCenterFrequency',
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
    'CfgDownlinkAutoCellIDDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkAutoCellIDDetectionEnabled',
                'name': 'autoCellIDDetectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkAutoChannelDetection': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AutoPdschChannelDetectionEnabled',
                'name': 'autoPDSCHChannelDetectionEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AutoControlChannelPowerDetectionEnabled',
                'name': 'autoControlChannelPowerDetectionEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'AutoPcfichCfiDetectionEnabled',
                'grpc_name': 'auto_pcfich_cfi_detection_enabled',
                'name': 'autoPCFICHCFIDetectionEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkChannelConfigurationMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkChannelConfigurationMode',
                'name': 'channelConfigurationMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkNumberOfSubframes': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfSubframes',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkSynchronizationSignal': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pssPower',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'sssPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkTestModel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkTestModel',
                'name': 'downlinkTestModel',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDownlinkTestModelArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkTestModel',
                'name': 'downlinkTestModel',
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
    'CfgDuplexScheme': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DuplexScheme',
                'name': 'duplexScheme',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'UplinkDownlinkConfiguration',
                'name': 'uplinkDownlinkConfiguration',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgEMTCAnalysisEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'EmtcAnalysisEnabled',
                'name': 'emtcAnalysisEnabled',
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
    'CfgFrequencyEARFCN': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'LinkDirection',
                'name': 'linkDirection',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'band',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'earfcn',
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
    'CfgLinkDirection': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'LinkDirection',
                'name': 'linkDirection',
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
    'CfgNBIoTComponentCarrier': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'nCellID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'NBIoTUplinkSubcarrierSpacing',
                'name': 'uplinkSubcarrierSpacing',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNPUSCHDMRS': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'NPuschDmrsBaseSequenceMode',
                'grpc_name': 'npusch_dmrs_base_sequence_mode',
                'name': 'npuschdmrsBaseSequenceMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_name': 'npusch_dmrs_base_sequence_index',
                'name': 'npuschdmrsBaseSequenceIndex',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_name': 'npusch_dmrs_cyclic_shift',
                'name': 'npuschdmrsCyclicShift',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'NPuschDmrsGroupHoppingEnabled',
                'grpc_name': 'npusch_dmrs_group_hopping_enabled',
                'name': 'npuschdmrsGroupHoppingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_name': 'npusch_dmrs_delta_ss',
                'name': 'npuschdmrsDeltaSS',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNPUSCHFormat': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'format',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNPUSCHStartingSlot': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'startingSlot',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNPUSCHTones': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'toneOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfTones',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'NPuschModulationType',
                'name': 'modulationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfComponentCarriers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfComponentCarriers',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfDUTAntennas': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfDUTAntennas',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfPDSCHChannels': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfPDSCHChannels',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfPUSCHResourceBlockClusters': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfResourceBlockClusters',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgNumberOfSubblocks': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfSubblocks',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPBCH': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pbchPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPCFICH': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'cfi',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'power',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPDCCH': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pdcchPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPDSCH': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'UserDefinedPdschCW0ModulationType',
                'name': 'cw0ModulationType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'resourceBlockAllocation',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'power',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPHICH': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkUserDefinedPhichResource',
                'name': 'resource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DownlinkUserDefinedPhichDuration',
                'name': 'duration',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'power',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPSSCHModulationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PsschModulationType',
                'name': 'modulationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPSSCHResourceBlocks': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resourceBlockOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfResourceBlocks',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPUSCHModulationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PuschModulationType',
                'name': 'modulationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPUSCHResourceBlocks': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resourceBlockOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfResourceBlocks',
                'type': 'int32'
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
    'CfgTransmitAntennaToAnalyze': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'transmitAntennaToAnalyze',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgeNodeBCategory': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ENodeBCategory',
                'grpc_name': 'enodeb_category',
                'name': 'eNodeBCategory',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
        'custom_close': 'Close(id, RFMXLTE_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXLTE_VAL_FALSE)',
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
    'ModAccCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccAveragingEnabled',
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
    'ModAccCfgCommonClockSourceEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccCommonClockSourceEnabled',
                'name': 'commonClockSourceEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgEVMUnit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccEvmUnit',
                'name': 'evmUnit',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgFFTWindowOffset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'fftWindowOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgFFTWindowPosition': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccFftWindowType',
                'name': 'fftWindowType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'fftWindowOffset',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'fftWindowLength',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgInBandEmissionMaskType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccInBandEmissionMaskType',
                'name': 'inBandEmissionMaskType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgSynchronizationModeAndInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccSynchronizationMode',
                'name': 'synchronizationMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCSRSConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'csrsConstellation',
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
    'ModAccFetchCSRSConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchCSRSConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'csrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(csrsConstellation)'
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
    'ModAccFetchCSRSConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'csrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'csrsConstellationQ',
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
    'ModAccFetchCSRSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_csrs_evm',
                'name': 'meanRMSCSRSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCSRSEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_csrs_evm',
                'name': 'meanRMSCSRSEVM',
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
    'ModAccFetchCompositeEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositeEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakCompositeEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSymbolIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSubcarrierIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSlotIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCompositeEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositeEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakCompositeEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSymbolIndex',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSubcarrierIndex',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVMSlotIndex',
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
    'ModAccFetchCompositeMagnitudeAndPhaseError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositeMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maxPeakCompositeMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositePhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maxPeakCompositePhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCompositeMagnitudeAndPhaseErrorArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositeMagnitudeError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakCompositeMagnitudeError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanRMSCompositePhaseError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakCompositePhaseError',
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
    'ModAccFetchDownlinkDetectedCellID': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'detectedCellID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDownlinkDetectedCellIDArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'detectedCellID',
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
    'ModAccFetchDownlinkPBCHConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchConstellation',
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
    'ModAccFetchDownlinkPBCHConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchDownlinkPBCHConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pbchConstellation)'
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
    'ModAccFetchDownlinkPBCHConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pbchConstellationQ',
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
    'ModAccFetchDownlinkPCFICHConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pcfichConstellation',
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
    'ModAccFetchDownlinkPCFICHConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchDownlinkPCFICHConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pcfichConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pcfichConstellation)'
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
    'ModAccFetchDownlinkPCFICHConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pcfichConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pcfichConstellationQ',
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
    'ModAccFetchDownlinkPDCCHConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdcchConstellation',
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
    'ModAccFetchDownlinkPDCCHConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchDownlinkPDCCHConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdcchConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pdcchConstellation)'
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
    'ModAccFetchDownlinkPDCCHConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdcchConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pdcchConstellationQ',
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
    'ModAccFetchDownlinkPHICHConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'phichConstellation',
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
    'ModAccFetchDownlinkPHICHConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchDownlinkPHICHConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'phichConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(phichConstellation)'
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
    'ModAccFetchDownlinkPHICHConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'phichConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'phichConstellationQ',
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
    'ModAccFetchDownlinkTransmitPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rsTransmitPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ofdmSymbolTransmitPower',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved1',
                'pointer': True,
                'type': 'float64'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved2',
                'pointer': True,
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDownlinkTransmitPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rsTransmitPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'ofdmSymbolTransmitPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved1',
                'pointer': True,
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
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved2',
                'pointer': True,
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
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMHighPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evmHighPerSymbol',
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
    'ModAccFetchEVMLowPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evmLowPerSymbol',
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
    'ModAccFetchEVMPerSlotTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_per_slot',
                'name': 'rmsevmPerSlot',
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
    'ModAccFetchEVMPerSubcarrierTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'mean_rms_evm_per_subcarrier',
                'name': 'meanRMSEVMPerSubcarrier',
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
    'ModAccFetchEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_per_symbol',
                'name': 'rmsevmPerSymbol',
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
    'ModAccFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQQuadratureError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchIQImpairmentsArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQOriginOffset',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanIQGainImbalance',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanIQQuadratureError',
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
    'ModAccFetchInBandEmissionMargin': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'inBandEmissionMargin',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchInBandEmissionMarginArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'inBandEmissionMargin',
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
    'ModAccFetchInBandEmissionTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'inBandEmission',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'inBandEmissionMask',
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
    'ModAccFetchMaximumEVMHighPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVMHighPerSymbol',
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
    'ModAccFetchMaximumEVMLowPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVMLowPerSymbol',
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
    'ModAccFetchMaximumEVMPerSlotTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVMPerSlot',
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
    'ModAccFetchMaximumEVMPerSubcarrierTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVMPerSubcarrier',
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
    'ModAccFetchMaximumEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVMPerSymbol',
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
    'ModAccFetchMaximumFrequencyErrorPerSlotTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumFrequencyErrorPerSlot',
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
    'ModAccFetchMaximumMagnitudeErrorPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumMagnitudeErrorPerSymbol',
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
    'ModAccFetchMaximumPhaseErrorPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumPhaseErrorPerSymbol',
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
    'ModAccFetchNBSynchronizationSignalConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'nsssConstellationArraySize',
                    'value_twist': 'nsssConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'nsssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'npssConstellationArraySize',
                    'value_twist': 'npssConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'npssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNBSynchronizationSignalConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchNBSynchronizationSignalConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'nsssConstellationArraySize',
                    'value_twist': 'nsssConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(nsssConstellation)'
            },
            {
                'direction': 'in',
                'name': 'nsssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'npssConstellationArraySize',
                    'value_twist': 'npssConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(npssConstellation)'
            },
            {
                'direction': 'in',
                'name': 'npssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNBSynchronizationSignalConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'nsssConstellationArraySize',
                    'value_twist': 'nsssConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'nsssConstellationArraySize',
                    'value_twist': 'nsssConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'nsssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'nsssConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'npssConstellationArraySize',
                    'value_twist': 'npssConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'npssConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'npssConstellationArraySize',
                    'value_twist': 'npssConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'npssConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'npssConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPDSCH16QAMConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
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
    'ModAccFetchNPDSCH16QAMConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchNPDSCH16QAMConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam16Constellation)'
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
    'ModAccFetchNPDSCH16QAMConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationQ',
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
    'ModAccFetchNPDSCHQPSKConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
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
    'ModAccFetchNPDSCHQPSKConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchNPDSCHQPSKConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qpskConstellation)'
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
    'ModAccFetchNPDSCHQPSKConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationQ',
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
    'ModAccFetchNPUSCHConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPUSCHConstellationTraceInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchNPUSCHConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dmrsConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPUSCHConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPUSCHDMRSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'npusch_mean_rms_dmrs_evm',
                'name': 'npuschMeanRMSDMRSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'npusch_maximum_peak_dmrs_evm',
                'name': 'npuschMaximumPeakDMRSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPUSCHDataEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'npuschMeanRMSDataEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'npuschMaximumPeakDataEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNPUSCHSymbolPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'npuschMeanDataPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'npuschMeanDMRSPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchNRSConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nrsConstellation',
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
    'ModAccFetchNRSConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchNRSConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(nrsConstellation)'
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
    'ModAccFetchNRSConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'nrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'nrsConstellationQ',
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
    'ModAccFetchPDSCH1024QAMConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024Constellation',
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
    'ModAccFetchPDSCH1024QAMConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPDSCH1024QAMConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam1024Constellation)'
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
    'ModAccFetchPDSCH1024QAMConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam1024ConstellationQ',
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
    'ModAccFetchPDSCH1024QAMEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_1024qam_evm',
                'name': 'meanRMS1024QAMEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPDSCH1024QAMEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_1024qam_evm',
                'name': 'meanRMS1024QAMEVM',
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
    'ModAccFetchPDSCH16QAMConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
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
    'ModAccFetchPDSCH16QAMConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPDSCH16QAMConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam16Constellation)'
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
    'ModAccFetchPDSCH16QAMConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationQ',
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
    'ModAccFetchPDSCH256QAMConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256Constellation',
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
    'ModAccFetchPDSCH256QAMConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPDSCH256QAMConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam256Constellation)'
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
    'ModAccFetchPDSCH256QAMConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam256ConstellationQ',
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
    'ModAccFetchPDSCH64QAMConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64Constellation',
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
    'ModAccFetchPDSCH64QAMConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPDSCH64QAMConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam64Constellation)'
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
    'ModAccFetchPDSCH64QAMConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam64ConstellationQ',
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
    'ModAccFetchPDSCHEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_evm',
                'name': 'meanRMSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_qpsk_evm',
                'name': 'meanRMSQPSKEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_16qam_evm',
                'name': 'meanRMS16QAMEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_64qam_evm',
                'name': 'meanRMS64QAMEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_256qam_evm',
                'name': 'meanRMS256QAMEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPDSCHEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_evm',
                'name': 'meanRMSEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_qpsk_evm',
                'name': 'meanRMSQPSKEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_16qam_evm',
                'name': 'meanRMS16QAMEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_64qam_evm',
                'name': 'meanRMS64QAMEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_256qam_evm',
                'name': 'meanRMS256QAMEVM',
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
    'ModAccFetchPDSCHQPSKConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
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
    'ModAccFetchPDSCHQPSKConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPDSCHQPSKConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qpskConstellation)'
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
    'ModAccFetchPDSCHQPSKConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationQ',
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
    'ModAccFetchPSSCHConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHConstellationTraceInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPSSCHConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dmrsConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHDMRSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pssch_mean_rms_dmrs_evm',
                'name': 'psschMeanRMSDMRSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pssch_maximum_peak_dmrs_evm',
                'name': 'psschMaximumPeakDMRSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHDMRSEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pssch_mean_rms_dmrs_evm',
                'name': 'psschMeanRMSDMRSEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pssch_maximum_peak_dmrs_evm',
                'name': 'psschMaximumPeakDMRSEVM',
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
    'ModAccFetchPSSCHDataEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMeanRMSDataEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMaximumPeakDataEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHDataEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMeanRMSDataEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'psschMaximumPeakDataEVM',
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
    'ModAccFetchPSSCHSymbolPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMeanDataPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMeanDMRSPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPSSCHSymbolPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psschMeanDataPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'psschMeanDMRSPower',
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
    'ModAccFetchPUSCHConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHConstellationTraceInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchPUSCHConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dataConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(dmrsConstellation)'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataConstellationArraySize',
                    'value_twist': 'dataConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dataConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dataConstellationActualArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dmrsConstellationArraySize',
                    'value_twist': 'dmrsConstellationActualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'dmrsConstellationArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'dmrsConstellationActualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHDMRSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_dmrs_evm',
                'name': 'meanRMSDMRSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'maximum_peak_dmrs_evm',
                'name': 'maximumPeakDMRSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHDMRSEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_dmrs_evm',
                'name': 'meanRMSDMRSEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'maximum_peak_dmrs_evm',
                'name': 'maximumPeakDMRSEVM',
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
    'ModAccFetchPUSCHDataEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSDataEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakDataEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHDataEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSDataEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakDataEVM',
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
    'ModAccFetchPUSCHDemodulatedBits': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'bits',
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
    'ModAccFetchPUSCHSymbolPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschMeanDataPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschMeanDMRSPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPUSCHSymbolPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschMeanDataPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'puschMeanDMRSPower',
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
    'ModAccFetchRMSMagnitudeErrorPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'rmsMagnitudeErrorPerSymbol',
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
    'ModAccFetchRMSPhaseErrorPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'rmsPhaseErrorPerSymbol',
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
    'ModAccFetchSRSConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'srsConstellation',
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
    'ModAccFetchSRSConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchSRSConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'srsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(srsConstellation)'
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
    'ModAccFetchSRSConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'srsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'srsConstellationQ',
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
    'ModAccFetchSRSEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_srs_evm',
                'name': 'meanRMSSRSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSRSPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchSRSEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_srs_evm',
                'name': 'meanRMSSRSEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanSRSPower',
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
    'ModAccFetchSpectralFlatness': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'range1MaximumToRange1Minimum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'range2MaximumToRange2Minimum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'range1MaximumToRange2Minimum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'range2MaximumToRange1Minimum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchSpectralFlatnessArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'range1MaximumToRange1Minimum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'range2MaximumToRange2Minimum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'range1MaximumToRange2Minimum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'range2MaximumToRange1Minimum',
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
    'ModAccFetchSpectralFlatnessTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'spectralFlatness',
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
    'ModAccFetchSubblockIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockMeanIQOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockMeanIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockMeanIQQuadratureError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchSubblockInBandEmissionMargin': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmissionMargin',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchSubblockInBandEmissionTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmission',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmissionMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmissionRBIndices',
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
    'ModAccFetchSynchronizationSignalConstellation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'out',
                'name': 'pssConstellation',
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
    'ModAccFetchSynchronizationSignalConstellationInterleavedIQ': {
        'cname': 'RFmxLTE_ModAccFetchSynchronizationSignalConstellation',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(sssConstellation)'
            },
            {
                'direction': 'out',
                'name': 'pssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pssConstellation)'
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
    'ModAccFetchSynchronizationSignalConstellationSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'sssConstellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pssConstellationQ',
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
    'ModAccFetchSynchronizationSignalEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_pss_evm',
                'name': 'meanRMSPSSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_sss_evm',
                'name': 'meanRMSSSSEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchSynchronizationSignalEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_pss_evm',
                'name': 'meanRMSPSSEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_sss_evm',
                'name': 'meanRMSSSSEVM',
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
                'name': 'absolutePower',
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
    'OBWFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'PVTCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PvtAveragingEnabled',
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
                'enum': 'PvtAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PVTCfgMeasurementMethod': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PvtMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PVTCfgOFFPowerExclusionPeriods': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offPowerExclusionBefore',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'offPowerExclusionAfter',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteOFFPowerBefore',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteOFFPowerAfter',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteONPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'burstWidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtMeasurementStatus',
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
                'name': 'meanAbsoluteOFFPowerBefore',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteOFFPowerAfter',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteONPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'burstWidth',
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
    'PVTFetchSignalPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'signalPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
    'SEMCfgComponentCarrierMaximumOutputPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierMaximumOutputPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgComponentCarrierMaximumOutputPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierMaximumOutputPower',
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
    'SEMCfgDownlinkMask': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemDownlinkMaskType',
                'name': 'downlinkMaskType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'deltaFMaximum',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'aggregatedMaximumPower',
                'type': 'float64'
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
                'name': 'offsetAbsoluteLimitStart',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'offsetAbsoluteLimitStop',
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
                'name': 'offsetAbsoluteLimitStart',
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
                'name': 'offsetAbsoluteLimitStop',
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
                'name': 'offsetBandwidthIntegral',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgOffsetBandwidthIntegralArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetBandwidthIntegral',
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
    'SEMCfgOffsetLimitFailMaskArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'offsetRBW',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetRbwFilterType',
                'name': 'offsetRBWFilterType',
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
                'name': 'offsetRBW',
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
                'name': 'offsetRBWFilterType',
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
    'SEMCfgUplinkMaskType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemUplinkMaskType',
                'name': 'uplinkMaskType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absoluteIntegratedPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absoluteIntegratedPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
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
                'name': 'absoluteIntegratedPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absolutePeakPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativePeakPower',
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
                'name': 'absoluteIntegratedPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'absolutePeakPower',
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
                'name': 'relativePeakPower',
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
    'SEMFetchSubblockMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
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
    'SEMFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
                'name': 'absoluteIntegratedPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absolutePeakPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'relativePeakPower',
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
                'name': 'absoluteIntegratedPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativeIntegratedPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'absolutePeakPower',
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
                'name': 'relativePeakPower',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
                'grpc_type': 'NiRFmxLTEAttribute',
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
    'SlotPhaseCfgSynchronizationModeAndInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SlotPhaseSynchronizationMode',
                'name': 'synchronizationMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SlotPhaseFetchMaximumPhaseDiscontinuity': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPhaseDiscontinuity',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SlotPhaseFetchMaximumPhaseDiscontinuityArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPhaseDiscontinuity',
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
    'SlotPhaseFetchPhaseDiscontinuities': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotPhaseDiscontinuity',
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
    'SlotPhaseFetchSamplePhaseError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'samplePhaseError',
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
    'SlotPhaseFetchSamplePhaseErrorLinearFitTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'samplePhaseErrorLinearFit',
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
    'SlotPowerCfgMeasurementInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'measurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SlotPowerFetchPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subframePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'subframePowerDelta',
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
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgMeasurementOffsetAndInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'measurementInterval',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/functions_addon.py sha256=eb07baf08a6590f4d83d2915b0cc6d13dec69627e517b0360f05b410c552bb40 bytes=767 -->
## FILE: source/codegen/metadata/nirfmxlte/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/functions_addon.py`
- sha256: `eb07baf08a6590f4d83d2915b0cc6d13dec69627e517b0360f05b410c552bb40`
- bytes: 767

````python
functions_override_metadata = {
    'CfgPSSCHModulationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PsschModulationType',
                'grpc_field_number': '4',
                'grpc_raw_field_number': '3',
                'name': 'modulationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxnr/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/attributes.py sha256=c43e71f0e2c3001447748bca907ba99d612dc03b65504acb2424a6b1813d980d bytes=69825 -->
## FILE: source/codegen/metadata/nirfmxnr/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/attributes.py`
- sha256: `c43e71f0e2c3001447748bca907ba99d612dc03b65504acb2424a6b1813d980d`
- bytes: 69825

````python
attributes = {
    9437185: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    9437186: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    9437187: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    9437188: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    9437189: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    9437190: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    9437191: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    9437192: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    9437193: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    9437194: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    9437195: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    9437196: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    9437198: {
        'access': 'read-write',
        'enum': 'LinkDirection',
        'name': 'LINK_DIRECTION',
        'type': 'int32'
    },
    9437200: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SUBBLOCKS',
        'type': 'int32'
    },
    9437202: {
        'access': 'read-write',
        'name': 'BAND',
        'type': 'int32'
    },
    9437203: {
        'access': 'read-write',
        'enum': 'ComponentCarrierSpacingType',
        'name': 'COMPONENT_CARRIER_SPACING_TYPE',
        'type': 'int32'
    },
    9437204: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_AT_CENTER_FREQUENCY',
        'type': 'int32'
    },
    9437205: {
        'access': 'read-write',
        'name': 'NUMBER_OF_COMPONENT_CARRIERS',
        'type': 'int32'
    },
    9437206: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_BANDWIDTH',
        'type': 'float64'
    },
    9437207: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    9437209: {
        'access': 'read-write',
        'name': 'CELL_ID',
        'type': 'int32'
    },
    9437210: {
        'access': 'read-write',
        'enum': 'BandwidthPartCyclicPrefixMode',
        'name': 'BANDWIDTH_PART_CYCLIC_PREFIX_MODE',
        'type': 'int32'
    },
    9437211: {
        'access': 'read-write',
        'name': 'BANDWIDTH_PART_SUBCARRIER_SPACING',
        'type': 'float64'
    },
    9437214: {
        'access': 'read-write',
        'enum': 'PuschTransformPrecodingEnabled',
        'name': 'PUSCH_TRANSFORM_PRECODING_ENABLED',
        'type': 'int32'
    },
    9437215: {
        'access': 'read-write',
        'enum': 'AutoResourceBlockDetectionEnabled',
        'name': 'AUTO_RESOURCE_BLOCK_DETECTION_ENABLED',
        'type': 'int32'
    },
    9437217: {
        'access': 'read-write',
        'enum': 'PuschDmrsGroupHoppingEnabled',
        'name': 'PUSCH_DMRS_GROUP_HOPPING_ENABLED',
        'type': 'int32'
    },
    9437218: {
        'access': 'read-write',
        'enum': 'PuschDmrsSequenceHoppingEnabled',
        'name': 'PUSCH_DMRS_SEQUENCE_HOPPING_ENABLED',
        'type': 'int32'
    },
    9437222: {
        'access': 'read-write',
        'enum': 'PuschModulationType',
        'name': 'PUSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    9437223: {
        'access': 'read-write',
        'name': 'PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS',
        'type': 'int32'
    },
    9437224: {
        'access': 'read-write',
        'name': 'PUSCH_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    9437225: {
        'access': 'read-write',
        'name': 'PUSCH_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    9437231: {
        'access': 'read-write',
        'enum': 'ModAccDCSubcarrierRemovalEnabled',
        'name': 'MODACC_DC_SUBCARRIER_REMOVAL_ENABLED',
        'type': 'int32'
    },
    9437232: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_POWER',
        'type': 'float64'
    },
    9437233: {
        'access': 'read-write',
        'enum': 'PuschDmrsConfigurationType',
        'name': 'PUSCH_DMRS_CONFIGURATION_TYPE',
        'type': 'int32'
    },
    9437234: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_ADDITIONAL_POSITIONS',
        'type': 'int32'
    },
    9437235: {
        'access': 'read-write',
        'enum': 'PuschDmrsDuration',
        'name': 'PUSCH_DMRS_DURATION',
        'type': 'int32'
    },
    9437236: {
        'access': 'read-write',
        'enum': 'PuschMappingType',
        'name': 'PUSCH_MAPPING_TYPE',
        'type': 'int32'
    },
    9437237: {
        'access': 'read-write',
        'enum': 'FrequencyRange',
        'name': 'FREQUENCY_RANGE',
        'type': 'int32'
    },
    9437239: {
        'access': 'read-write',
        'enum': 'ReferenceGridAlignmentMode',
        'name': 'REFERENCE_GRID_ALIGNMENT_MODE',
        'type': 'int32'
    },
    9437240: {
        'access': 'read-write',
        'enum': 'ModAccCompositeResultsIncludeDmrs',
        'name': 'MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS',
        'type': 'int32'
    },
    9437241: {
        'access': 'read-write',
        'enum': 'ModAccCompositeResultsIncludePtrs',
        'name': 'MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS',
        'type': 'int32'
    },
    9437244: {
        'access': 'read-write',
        'name': 'SUB_BAND_ALLOCATION',
        'type': 'char[]'
    },
    9437245: {
        'access': 'read-write',
        'name': 'NUMBER_OF_BANDWIDTH_PARTS',
        'type': 'int32'
    },
    9437246: {
        'access': 'read-write',
        'name': 'BANDWIDTH_PART_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    9437247: {
        'access': 'read-write',
        'name': 'BANDWIDTH_PART_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    9437249: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_ANTENNA_PORTS',
        'type': 'char[]'
    },
    9437250: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_NUMBER_OF_CDM_GROUPS',
        'type': 'int32'
    },
    9437252: {
        'access': 'read-write',
        'enum': 'PuschDmrsScramblingIDMode',
        'name': 'PUSCH_DMRS_SCRAMBLING_ID_MODE',
        'type': 'int32'
    },
    9437253: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_SCRAMBLING_ID',
        'type': 'int32'
    },
    9437254: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_NSCID',
        'type': 'int32'
    },
    9437255: {
        'access': 'read-write',
        'enum': 'PuschDmrsPuschIDMode',
        'name': 'PUSCH_DMRS_PUSCH_ID_MODE',
        'type': 'int32'
    },
    9437256: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_PUSCH_ID',
        'type': 'int32'
    },
    9437258: {
        'access': 'read-write',
        'name': 'PUSCH_DMRS_TYPE_A_POSITION',
        'type': 'int32'
    },
    9437259: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PUSCH_CONFIGURATIONS',
        'type': 'int32'
    },
    9437260: {
        'access': 'read-write',
        'name': 'PUSCH_SLOT_ALLOCATION',
        'type': 'char[]'
    },
    9437261: {
        'access': 'read-write',
        'name': 'PUSCH_SYMBOL_ALLOCATION',
        'type': 'char[]'
    },
    9437265: {
        'access': 'read-write',
        'enum': 'PuschDmrsPowerMode',
        'name': 'PUSCH_DMRS_POWER_MODE',
        'type': 'int32'
    },
    9437269: {
        'access': 'read-write',
        'enum': 'PuschPtrsEnabled',
        'name': 'PUSCH_PTRS_ENABLED',
        'type': 'int32'
    },
    9437270: {
        'access': 'read-write',
        'name': 'PUSCH_PTRS_ANTENNA_PORTS',
        'type': 'char[]'
    },
    9437271: {
        'access': 'read-write',
        'enum': 'PuschPtrsPowerMode',
        'name': 'PUSCH_PTRS_POWER_MODE',
        'type': 'int32'
    },
    9437272: {
        'access': 'read-write',
        'name': 'PUSCH_PTRS_POWER',
        'type': 'float64'
    },
    9437274: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PTRS_GROUPS',
        'type': 'int32'
    },
    9437275: {
        'access': 'read-write',
        'name': 'SAMPLES_PER_PTRS_GROUP',
        'type': 'int32'
    },
    9437276: {
        'access': 'read-write',
        'name': 'PUSCH_PTRS_TIME_DENSITY',
        'type': 'int32'
    },
    9437277: {
        'access': 'read-write',
        'name': 'PUSCH_PTRS_FREQUENCY_DENSITY',
        'type': 'int32'
    },
    9437278: {
        'access': 'read-write',
        'name': 'PUSCH_PTRS_RE_OFFSET',
        'type': 'int32'
    },
    9437279: {
        'access': 'read-write',
        'enum': 'GNodeBCategory',
        'name': 'GNODEB_CATEGORY',
        'type': 'int32'
    },
    9437280: {
        'access': 'read-write',
        'name': 'SUBBLOCK_TRANSMIT_LO_FREQUENCY',
        'type': 'float64'
    },
    9437281: {
        'access': 'read-write',
        'name': 'PHASE_COMPENSATION_FREQUENCY',
        'type': 'float64'
    },
    9437282: {
        'access': 'read-write',
        'name': 'REFERENCE_GRID_SUBCARRIER_SPACING',
        'type': 'float64'
    },
    9437283: {
        'access': 'read-write',
        'name': 'REFERENCE_GRID_START',
        'type': 'int32'
    },
    9437284: {
        'access': 'read-write',
        'name': 'NUMBER_OF_USERS',
        'type': 'int32'
    },
    9437285: {
        'access': 'read-write',
        'name': 'RNTI',
        'type': 'int32'
    },
    9437287: {
        'access': 'read-write',
        'name': 'PDSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS',
        'type': 'int32'
    },
    9437288: {
        'access': 'read-write',
        'name': 'PDSCH_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    9437289: {
        'access': 'read-write',
        'name': 'PDSCH_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    9437290: {
        'access': 'read-write',
        'enum': 'PdschModulationType',
        'name': 'PDSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    9437291: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_ANTENNA_PORTS',
        'type': 'char[]'
    },
    9437292: {
        'access': 'read-write',
        'enum': 'PdschDmrsPowerMode',
        'name': 'PDSCH_DMRS_POWER_MODE',
        'type': 'int32'
    },
    9437293: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_POWER',
        'type': 'float64'
    },
    9437294: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_NUMBER_OF_CDM_GROUPS',
        'type': 'int32'
    },
    9437295: {
        'access': 'read-write',
        'enum': 'PdschDmrsScramblingIDMode',
        'name': 'PDSCH_DMRS_SCRAMBLING_ID_MODE',
        'type': 'int32'
    },
    9437296: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_SCRAMBLING_ID',
        'type': 'int32'
    },
    9437297: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_NSCID',
        'type': 'int32'
    },
    9437300: {
        'access': 'read-write',
        'enum': 'PdschDmrsConfigurationType',
        'name': 'PDSCH_DMRS_CONFIGURATION_TYPE',
        'type': 'int32'
    },
    9437301: {
        'access': 'read-write',
        'enum': 'PdschMappingType',
        'name': 'PDSCH_MAPPING_TYPE',
        'type': 'int32'
    },
    9437302: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_TYPE_A_POSITION',
        'type': 'int32'
    },
    9437303: {
        'access': 'read-write',
        'enum': 'PdschDmrsDuration',
        'name': 'PDSCH_DMRS_DURATION',
        'type': 'int32'
    },
    9437304: {
        'access': 'read-write',
        'name': 'PDSCH_DMRS_ADDITIONAL_POSITIONS',
        'type': 'int32'
    },
    9437305: {
        'access': 'read-write',
        'enum': 'PdschPtrsEnabled',
        'name': 'PDSCH_PTRS_ENABLED',
        'type': 'int32'
    },
    9437306: {
        'access': 'read-write',
        'name': 'PDSCH_PTRS_ANTENNA_PORTS',
        'type': 'char[]'
    },
    9437307: {
        'access': 'read-write',
        'enum': 'PdschPtrsPowerMode',
        'name': 'PDSCH_PTRS_POWER_MODE',
        'type': 'int32'
    },
    9437308: {
        'access': 'read-write',
        'name': 'PDSCH_PTRS_POWER',
        'type': 'float64'
    },
    9437309: {
        'access': 'read-write',
        'name': 'PDSCH_PTRS_TIME_DENSITY',
        'type': 'int32'
    },
    9437310: {
        'access': 'read-write',
        'name': 'PDSCH_PTRS_FREQUENCY_DENSITY',
        'type': 'int32'
    },
    9437311: {
        'access': 'read-write',
        'name': 'PDSCH_PTRS_RE_OFFSET',
        'type': 'int32'
    },
    9437312: {
        'access': 'read-write',
        'name': 'PDSCH_SLOT_ALLOCATION',
        'type': 'char[]'
    },
    9437313: {
        'access': 'read-write',
        'name': 'PDSCH_SYMBOL_ALLOCATION',
        'type': 'char[]'
    },
    9437314: {
        'access': 'read-write',
        'enum': 'SsbEnabled',
        'name': 'SSB_ENABLED',
        'type': 'int32'
    },
    9437315: {
        'access': 'read-write',
        'name': 'SSB_CRB_OFFSET',
        'type': 'int32'
    },
    9437316: {
        'access': 'read-write',
        'name': 'SSB_SUBCARRIER_OFFSET',
        'type': 'int32'
    },
    9437317: {
        'access': 'read-write',
        'enum': 'SsbPattern',
        'name': 'SSB_PATTERN',
        'type': 'int32'
    },
    9437318: {
        'access': 'read-write',
        'name': 'PSS_POWER',
        'type': 'float64'
    },
    9437319: {
        'access': 'read-write',
        'name': 'SSS_POWER',
        'type': 'float64'
    },
    9437320: {
        'access': 'read-write',
        'name': 'PBCH_POWER',
        'type': 'float64'
    },
    9437321: {
        'access': 'read-write',
        'name': 'PBCH_DMRS_POWER',
        'type': 'float64'
    },
    9437324: {
        'access': 'read-write',
        'enum': 'AutoCellIDDetectionEnabled',
        'name': 'AUTO_CELL_ID_DETECTION_ENABLED',
        'type': 'int32'
    },
    9437326: {
        'access': 'read-write',
        'enum': 'DownlinkChannelConfigurationMode',
        'name': 'DOWNLINK_CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    9437328: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PDSCH_CONFIGURATIONS',
        'type': 'int32'
    },
    9437330: {
        'access': 'read-write',
        'name': 'EPRE_RATIO_PORT',
        'type': 'int32'
    },
    9437332: {
        'access': 'read-write',
        'name': 'SSB_PERIODICITY',
        'type': 'float64'
    },
    9437333: {
        'access': 'read-write',
        'name': 'SSB_ACTIVE_BLOCKS',
        'type': 'char[]'
    },
    9437334: {
        'access': 'read-write',
        'name': 'GRID_START',
        'type': 'int32'
    },
    9437336: {
        'access': 'read-write',
        'name': 'CHANNEL_RASTER',
        'type': 'float64'
    },
    9437337: {
        'access': 'read-write',
        'name': 'SUBCARRIER_SPACING_COMMON',
        'type': 'float64'
    },
    9437338: {
        'access': 'read-write',
        'name': 'GRID_SIZE',
        'type': 'int32'
    },
    9437339: {
        'access': 'read-write',
        'name': 'TRANSMIT_ANTENNA_TO_ANALYZE',
        'type': 'int32'
    },
    9437340: {
        'access': 'read-write',
        'name': 'POWER_CLASS',
        'type': 'int32'
    },
    9437342: {
        'access': 'read-write',
        'enum': 'PiBy2BpskPowerBoostEnabled',
        'name': 'PIBY2BPSK_POWER_BOOST_ENABLED',
        'type': 'int32'
    },
    9437343: {
        'access': 'read-write',
        'enum': 'AutoIncrementCellIDEnabled',
        'name': 'AUTO_INCREMENT_CELL_ID_ENABLED',
        'type': 'int32'
    },
    9437344: {
        'access': 'read-write',
        'enum': 'GNodeBType',
        'name': 'GNODEB_TYPE',
        'type': 'int32'
    },
    9437345: {
        'access': 'read-write',
        'name': 'RATED_TRP',
        'type': 'float64'
    },
    9437346: {
        'access': 'read-write',
        'name': 'RATED_EIRP',
        'type': 'float64'
    },
    9437347: {
        'access': 'read-write',
        'enum': 'SatelliteAccessNodeClass',
        'name': 'SATELLITE_ACCESS_NODE_CLASS',
        'type': 'int32'
    },
    9437348: {
        'access': 'read-write',
        'enum': 'SatelliteAccessNodeType',
        'name': 'SATELLITE_ACCESS_NODE_TYPE',
        'type': 'int32'
    },
    9437440: {
        'access': 'read-write',
        'enum': 'DownlinkTestModel',
        'name': 'DOWNLINK_TEST_MODEL',
        'type': 'int32'
    },
    9437441: {
        'access': 'read-write',
        'enum': 'DownlinkTestModelDuplexScheme',
        'name': 'DOWNLINK_TEST_MODEL_DUPLEX_SCHEME',
        'type': 'int32'
    },
    9437442: {
        'access': 'read-write',
        'enum': 'ComponentCarrierRadioAccessType',
        'name': 'COMPONENT_CARRIER_RADIO_ACCESS_TYPE',
        'type': 'int32'
    },
    9437443: {
        'access': 'read-write',
        'name': 'SUBBLOCK_ENDC_NOMINAL_SPACING_ADJUSTMENT',
        'type': 'float64'
    },
    9437446: {
        'access': 'read-write',
        'name': 'NUMBER_OF_CORESETS',
        'type': 'int32'
    },
    9437447: {
        'access': 'read-write',
        'name': 'CORESET_SYMBOL_OFFSET',
        'type': 'int32'
    },
    9437448: {
        'access': 'read-write',
        'name': 'CORESET_NUMBER_OF_SYMBOLS',
        'type': 'int32'
    },
    9437449: {
        'access': 'read-write',
        'name': 'CORESET_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS',
        'type': 'int32'
    },
    9437450: {
        'access': 'read-write',
        'name': 'CORESET_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    9437451: {
        'access': 'read-write',
        'name': 'CORESET_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    9437452: {
        'access': 'read-write',
        'enum': 'CoresetPrecodingGranularity',
        'name': 'CORESET_PRECODING_GRANULARITY',
        'type': 'int32'
    },
    9437453: {
        'access': 'read-write',
        'enum': 'CoresetCceToRegMappingType',
        'name': 'CORESET_CCE_TO_REG_MAPPING_TYPE',
        'type': 'int32'
    },
    9437454: {
        'access': 'read-write',
        'name': 'CORESET_REG_BUNDLE_SIZE',
        'type': 'int32'
    },
    9437455: {
        'access': 'read-write',
        'name': 'CORESET_INTERLEAVER_SIZE',
        'type': 'int32'
    },
    9437456: {
        'access': 'read-write',
        'name': 'CORESET_SHIFT_INDEX',
        'type': 'int32'
    },
    9437458: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PDCCH_CONFIGURATIONS',
        'type': 'int32'
    },
    9437459: {
        'access': 'read-write',
        'name': 'PDCCH_CCE_AGGREGATION_LEVEL',
        'type': 'int32'
    },
    9437460: {
        'access': 'read-write',
        'name': 'PDCCH_CCE_OFFSET',
        'type': 'int32'
    },
    9437461: {
        'access': 'read-write',
        'name': 'PDCCH_SLOT_ALLOCATION',
        'type': 'char[]'
    },
    9437462: {
        'access': 'read-write',
        'enum': 'PuschDmrsReleaseVersion',
        'name': 'PUSCH_DMRS_RELEASE_VERSION',
        'type': 'int32'
    },
    9437463: {
        'access': 'read-write',
        'enum': 'PdschDmrsReleaseVersion',
        'name': 'PDSCH_DMRS_RELEASE_VERSION',
        'type': 'int32'
    },
    9437464: {
        'access': 'read-write',
        'enum': 'ComponentCarrierAllocated',
        'name': 'COMPONENT_CARRIER_ALLOCATED',
        'type': 'int32'
    },
    9437465: {
        'access': 'read-write',
        'name': 'REFERENCE_GRID_SIZE',
        'type': 'int32'
    },
    9437466: {
        'access': 'read-write',
        'name': 'SSB_GRID_START',
        'type': 'int32'
    },
    9437467: {
        'access': 'read-write',
        'name': 'SSB_GRID_SIZE',
        'type': 'int32'
    },
    9437468: {
        'access': 'read-write',
        'enum': 'GridSizeMode',
        'name': 'GRID_SIZE_MODE',
        'type': 'int32'
    },
    9437469: {
        'access': 'read-write',
        'enum': 'DownlinkTestModelModulationType',
        'name': 'DOWNLINK_TEST_MODEL_MODULATION_TYPE',
        'type': 'int32'
    },
    9437470: {
        'access': 'read-write',
        'enum': 'DownlinkTestModelCellIDMode',
        'name': 'DOWNLINK_TEST_MODEL_CELL_ID_MODE',
        'type': 'int32'
    },
    9437471: {
        'access': 'read-write',
        'name': 'SUBBLOCK_FREQUENCY',
        'type': 'float64'
    },
    9437472: {
        'access': 'read-write',
        'name': 'SSB_HRF_INDEX',
        'type': 'int32'
    },
    9437473: {
        'access': 'read-write',
        'enum': 'BandwidthPartDCLocationKnown',
        'name': 'BANDWIDTH_PART_DC_LOCATION_KNOWN',
        'type': 'int32'
    },
    9438267: {
        'access': 'read-write',
        'enum': 'TransmitterArchitecture',
        'name': 'TRANSMITTER_ARCHITECTURE',
        'type': 'int32'
    },
    9438269: {
        'access': 'read-write',
        'enum': 'PhaseCompensation',
        'name': 'PHASE_COMPENSATION',
        'type': 'int32'
    },
    9441270: {
        'access': 'read-write',
        'enum': 'ListStepTimerUnit',
        'name': 'LIST_STEP_TIMER_UNIT',
        'type': 'int32'
    },
    9441271: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_OFFSET',
        'type': 'float64'
    },
    9441272: {
        'access': 'read-write',
        'name': 'NUMBER_OF_STEPS',
        'type': 'int32'
    },
    9441273: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_DURATION',
        'type': 'float64'
    },
    9441276: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    9441277: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    9441279: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    9441280: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9441282: {
        'access': 'read-write',
        'name': 'ACP_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9441286: {
        'access': 'read-write',
        'name': 'ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9441289: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_UTRA_OFFSETS',
        'type': 'int32'
    },
    9441290: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_EUTRA_OFFSETS',
        'type': 'int32'
    },
    9441291: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_NR_OFFSETS',
        'type': 'int32'
    },
    9441292: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    9441294: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    9441295: {
        'access': 'read-write',
        'enum': 'AcpOffsetSideband',
        'name': 'ACP_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    9441298: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9441302: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    9441303: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    9441304: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    9441305: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    9441306: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    9441307: {
        'access': 'read-write',
        'enum': 'AcpPowerUnits',
        'name': 'ACP_POWER_UNITS',
        'type': 'int32'
    },
    9441308: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    9441309: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    9441310: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9441311: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    9441313: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    9441314: {
        'access': 'read-write',
        'enum': 'AcpFftWindow',
        'name': 'ACP_FFT_WINDOW',
        'type': 'int32'
    },
    9441316: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    9441317: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    9441318: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    9441319: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    9441320: {
        'access': 'read-write',
        'enum': 'AcpAmplitudeCorrectionType',
        'name': 'ACP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    9441321: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9441322: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9441324: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    9441328: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    9441331: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9441332: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    9441338: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9441339: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    9441345: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9441346: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    9441347: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ENDC_OFFSETS',
        'type': 'int32'
    },
    9441349: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_CHANNEL_SPACING_ADJUSTMENT',
        'type': 'float64'
    },
    9441350: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    9441351: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    9441352: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMode',
        'name': 'ACP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    9441353: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationType',
        'name': 'ACP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    9441354: {
        'access': 'read-write',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    9441355: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationAveragingAuto',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    9441356: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationMode',
        'name': 'ACP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    9441357: {
        'access': 'read-write',
        'enum': 'AcpChannelConfigurationType',
        'name': 'ACP_CHANNEL_CONFIGURATION_TYPE',
        'type': 'int32'
    },
    9441358: {
        'access': 'read-write',
        'name': 'ACP_SUBBLOCK_OFFSET',
        'type': 'float64'
    },
    9449472: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9449474: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    9449475: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    9449476: {
        'access': 'read-write',
        'enum': 'ChpIntegrationBandwidthType',
        'name': 'CHP_INTEGRATION_BANDWIDTH_TYPE',
        'type': 'int32'
    },
    9449477: {
        'access': 'read-write',
        'name': 'CHP_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9449478: {
        'access': 'read-write',
        'name': 'CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9449481: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    9449482: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    9449483: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    9449485: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9449486: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    9449488: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    9449489: {
        'access': 'read-write',
        'enum': 'ChpFftWindow',
        'name': 'CHP_FFT_WINDOW',
        'type': 'int32'
    },
    9449490: {
        'access': 'read-write',
        'enum': 'ChpAmplitudeCorrectionType',
        'name': 'CHP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    9449491: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9449492: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9449494: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    9449498: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    9449501: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9449503: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    9449505: {
        'access': 'read-write',
        'enum': 'ChpMeasurementMode',
        'name': 'CHP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    9449506: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationEnabled',
        'name': 'CHP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    9449507: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationType',
        'name': 'CHP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    9449508: {
        'access': 'read-write',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    9449509: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationAveragingAuto',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    9449510: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationMode',
        'name': 'CHP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    9453568: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9453570: {
        'access': 'read-write',
        'enum': 'ModAccMulticarrierFilterEnabled',
        'name': 'MODACC_MULTICARRIER_FILTER_ENABLED',
        'type': 'int32'
    },
    9453572: {
        'access': 'read-write',
        'enum': 'ModAccSynchronizationMode',
        'name': 'MODACC_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    9453573: {
        'access': 'read-write',
        'enum': 'ModAccMeasurementLengthUnit',
        'name': 'MODACC_MEASUREMENT_LENGTH_UNIT',
        'type': 'int32'
    },
    9453574: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_OFFSET',
        'type': 'float64'
    },
    9453575: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_LENGTH',
        'type': 'float64'
    },
    9453576: {
        'access': 'read-write',
        'enum': 'ModAccSpectrumInverted',
        'name': 'MODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    9453577: {
        'access': 'read-write',
        'enum': 'ModAccChannelEstimationType',
        'name': 'MODACC_CHANNEL_ESTIMATION_TYPE',
        'type': 'int32'
    },
    9453578: {
        'access': 'read-write',
        'enum': 'ModAccEvmUnit',
        'name': 'MODACC_EVM_UNIT',
        'type': 'int32'
    },
    9453579: {
        'access': 'read-write',
        'enum': 'ModAccFftWindowType',
        'name': 'MODACC_FFT_WINDOW_TYPE',
        'type': 'int32'
    },
    9453580: {
        'access': 'read-write',
        'name': 'MODACC_FFT_WINDOW_OFFSET',
        'type': 'float64'
    },
    9453581: {
        'access': 'read-write',
        'name': 'MODACC_FFT_WINDOW_LENGTH',
        'type': 'float64'
    },
    9453582: {
        'access': 'read-write',
        'enum': 'ModAccCommonClockSourceEnabled',
        'name': 'MODACC_COMMON_CLOCK_SOURCE_ENABLED',
        'type': 'int32'
    },
    9453584: {
        'access': 'read-write',
        'enum': 'ModAccSpectralFlatnessCondition',
        'name': 'MODACC_SPECTRAL_FLATNESS_CONDITION',
        'type': 'int32'
    },
    9453585: {
        'access': 'read-write',
        'enum': 'ModAccAveragingEnabled',
        'name': 'MODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9453586: {
        'access': 'read-write',
        'name': 'MODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    9453587: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9453588: {
        'access': 'read-write',
        'name': 'MODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9453590: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453591: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453592: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_RMS_MAGNITUDE_ERROR_MEAN',
        'type': 'float64'
    },
    9453593: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_MAGNITUDE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    9453594: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_RMS_PHASE_ERROR_MEAN',
        'type': 'float64'
    },
    9453595: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_PHASE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    9453596: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_EVM_SLOT_INDEX',
        'type': 'int32'
    },
    9453597: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_EVM_SYMBOL_INDEX',
        'type': 'int32'
    },
    9453598: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_EVM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453599: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453600: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DATA_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453603: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DMRS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453604: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DMRS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453607: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IN_BAND_EMISSION_MARGIN',
        'type': 'float64'
    },
    9453608: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM',
        'type': 'float64'
    },
    9453609: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM',
        'type': 'float64'
    },
    9453610: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM',
        'type': 'float64'
    },
    9453611: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM',
        'type': 'float64'
    },
    9453612: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN',
        'type': 'float64'
    },
    9453613: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_FREQUENCY_ERROR_MEAN',
        'type': 'float64'
    },
    9453614: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    9453615: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_IQ_GAIN_IMBALANCE_MEAN',
        'type': 'float64'
    },
    9453616: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_QUADRATURE_ERROR_MEAN',
        'type': 'float64'
    },
    9453617: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_IQ_TIMING_SKEW_MEAN',
        'type': 'float64'
    },
    9453618: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_TIME_OFFSET_MEAN',
        'type': 'float64'
    },
    9453619: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_SYMBOL_CLOCK_ERROR_MEAN',
        'type': 'float64'
    },
    9453622: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    9453626: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_CELL_ID',
        'type': 'int32'
    },
    9453640: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_PTRS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453641: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_PTRS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453649: {
        'access': 'read-write',
        'enum': 'ModAccPhaseTrackingMode',
        'name': 'MODACC_PHASE_TRACKING_MODE',
        'type': 'int32'
    },
    9453650: {
        'access': 'read-write',
        'enum': 'ModAccTimingTrackingMode',
        'name': 'MODACC_TIMING_TRACKING_MODE',
        'type': 'int32'
    },
    9453652: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_PEAK_EVM_BWP_INDEX',
        'type': 'int32'
    },
    9453653: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_QPSK_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453654: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_16QAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453655: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_64QAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453656: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_256QAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453657: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453658: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DATA_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453659: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DMRS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453660: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DMRS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453661: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_PTRS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453662: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_PTRS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453666: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_LO_COMPONENT_CARRIER_INDEX',
        'type': 'int32'
    },
    9453667: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_LO_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453679: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SCH_SYMBOL_POWER_MEAN',
        'type': 'float64'
    },
    9453680: {
        'access': 'read-write',
        'enum': 'SchDetectedModulationType',
        'name': 'MODACC_RESULTS_SCH_DETECTED_MODULATION_TYPE',
        'type': 'int32'
    },
    9453681: {
        'access': 'read-write',
        'enum': 'ModAccFrequencyErrorEstimation',
        'name': 'MODACC_FREQUENCY_ERROR_ESTIMATION',
        'type': 'int32'
    },
    9453683: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_1024QAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453685: {
        'access': 'read-write',
        'enum': 'ModAccSymbolClockErrorEstimationEnabled',
        'name': 'MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    9453686: {
        'access': 'read-write',
        'enum': 'ModAccIQOriginOffsetEstimationEnabled',
        'name': 'MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    9453687: {
        'access': 'read-write',
        'enum': 'ModAccIQMismatchEstimationEnabled',
        'name': 'MODACC_IQ_MISMATCH_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    9453688: {
        'access': 'read-write',
        'enum': 'ModAccMagnitudeAndPhaseErrorEnabled',
        'name': 'MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED',
        'type': 'int32'
    },
    9453689: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453690: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453691: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SSS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453692: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SSS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453693: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PBCH_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453694: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PBCH_DATA_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453695: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PBCH_DMRS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453696: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PBCH_DMRS_PEAK_EVM_MAXIMUM',
        'type': 'float64'
    },
    9453697: {
        'access': 'read-write',
        'enum': 'ModAccEvmReferenceDataSymbolsMode',
        'name': 'MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE',
        'type': 'int32'
    },
    9453698: {
        'access': 'read-write',
        'enum': 'ModAccIQImpairmentsModel',
        'name': 'MODACC_IQ_IMPAIRMENTS_MODEL',
        'type': 'int32'
    },
    9453699: {
        'access': 'read-write',
        'enum': 'ModAccIQGainImbalanceCorrectionEnabled',
        'name': 'MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED',
        'type': 'int32'
    },
    9453700: {
        'access': 'read-write',
        'enum': 'ModAccIQQuadratureErrorCorrectionEnabled',
        'name': 'MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    9453701: {
        'access': 'read-write',
        'enum': 'ModAccIQTimingSkewCorrectionEnabled',
        'name': 'MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED',
        'type': 'int32'
    },
    9453702: {
        'access': 'read-write',
        'enum': 'ModAccIQImpairmentsPerSubcarrierEnabled',
        'name': 'MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED',
        'type': 'int32'
    },
    9453704: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SLOT_INDEX',
        'type': 'int32'
    },
    9453705: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM',
        'type': 'float64'
    },
    9453706: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM',
        'type': 'float64'
    },
    9453707: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM',
        'type': 'float64'
    },
    9453708: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM',
        'type': 'float64'
    },
    9453709: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453710: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MINIMUM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453711: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453712: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MINIMUM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    9453713: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_8PSK_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453714: {
        'access': 'read-write',
        'enum': 'ModAccNoiseCompensationEnabled',
        'name': 'MODACC_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    9453715: {
        'access': 'read-write',
        'enum': 'ModAccNoiseCompensationInputPowerCheckEnabled',
        'name': 'MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED',
        'type': 'int32'
    },
    9453716: {
        'access': 'read-write',
        'name': 'MODACC_NOISE_COMPENSATION_REFERENCE_LEVEL_COERCION_LIMIT',
        'type': 'float64'
    },
    9453717: {
        'access': 'read-write',
        'enum': 'ModAccMeasurementMode',
        'name': 'MODACC_MEASUREMENT_MODE',
        'type': 'int32'
    },
    9453718: {
        'access': 'read-write',
        'enum': 'ModAccNoiseCompensationApplied',
        'name': 'MODACC_RESULTS_NOISE_COMPENSATION_APPLIED',
        'type': 'int32'
    },
    9453719: {
        'access': 'read-write',
        'enum': 'ModAccAutoLevelAllowOverflow',
        'name': 'MODACC_AUTO_LEVEL_ALLOW_OVERFLOW',
        'type': 'int32'
    },
    9453725: {
        'access': 'read-write',
        'enum': 'ModAccShortFrameEnabled',
        'name': 'MODACC_SHORT_FRAME_ENABLED',
        'type': 'int32'
    },
    9453726: {
        'access': 'read-write',
        'name': 'MODACC_SHORT_FRAME_LENGTH',
        'type': 'float64'
    },
    9453727: {
        'access': 'read-write',
        'enum': 'ModAccShortFrameLengthUnit',
        'name': 'MODACC_SHORT_FRAME_LENGTH_UNIT',
        'type': 'int32'
    },
    9453728: {
        'access': 'read-write',
        'enum': 'ModAccPreFftErrorEstimationInterval',
        'name': 'MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL',
        'type': 'int32'
    },
    9453729: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_SLOT_FREQUENCY_ERROR_MAXIMUM',
        'type': 'float64'
    },
    9453730: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_SLOT_IQ_ORIGIN_OFFSET_MAXIMUM',
        'type': 'float64'
    },
    9453731: {
        'access': 'read-write',
        'enum': 'ModAccTransientPeriodEvmMode',
        'name': 'MODACC_TRANSIENT_PERIOD_EVM_MODE',
        'type': 'int32'
    },
    9453732: {
        'access': 'read-write',
        'name': 'MODACC_TRANSIENT_PERIOD',
        'type': 'float64'
    },
    9453733: {
        'access': 'read-write',
        'name': 'MODACC_TRANSIENT_POWER_CHANGE_THRESHOLD',
        'type': 'float64'
    },
    9453734: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DATA_TRANSIENT_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9453735: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_MAXIMUM',
        'type': 'float64'
    },
    9453736: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_PEAK_PHASE_OFFSET_SLOT_INDEX',
        'type': 'int32'
    },
    9453737: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DATA_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453738: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_DMRS_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453739: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_PTRS_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453740: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DATA_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453741: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_DMRS_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453742: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_PTRS_RE_POWER_MEAN',
        'type': 'float64'
    },
    9453743: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_CROSS_POWER_MEAN',
        'type': 'float64'
    },
    9453744: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPONENT_CARRIER_TIME_ALIGNMENT_ERROR_MEAN',
        'type': 'float64'
    },
    9453746: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_4096QAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    9461760: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9461763: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    9461766: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    9461767: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    9461768: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    9461769: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    9461770: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    9461771: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9461772: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    9461774: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    9461775: {
        'access': 'read-write',
        'enum': 'ObwFftWindow',
        'name': 'OBW_FFT_WINDOW',
        'type': 'int32'
    },
    9461777: {
        'access': 'read-write',
        'enum': 'ObwAmplitudeCorrectionType',
        'name': 'OBW_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    9461778: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9461779: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9461781: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    9461782: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9461783: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    9461784: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    9461786: {
        'access': 'read-write',
        'enum': 'ObwSpanAuto',
        'name': 'OBW_SPAN_AUTO',
        'type': 'int32'
    },
    9461792: {
        'access': 'read-write',
        'enum': 'ObwPowerIntegrationMethod',
        'name': 'OBW_POWER_INTEGRATION_METHOD',
        'type': 'int32'
    },
    9465856: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9465858: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_OFFSET',
        'type': 'float64'
    },
    9465859: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    9465860: {
        'access': 'read-write',
        'enum': 'TxpAveragingEnabled',
        'name': 'TXP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9465861: {
        'access': 'read-write',
        'name': 'TXP_AVERAGING_COUNT',
        'type': 'int32'
    },
    9465863: {
        'access': 'read-write',
        'name': 'TXP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9465864: {
        'access': 'read-write',
        'name': 'TXP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9465866: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    9465867: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    9469952: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9469954: {
        'access': 'read-write',
        'enum': 'SemUplinkMaskType',
        'name': 'SEM_UPLINK_MASK_TYPE',
        'type': 'int32'
    },
    9469955: {
        'access': 'read-write',
        'name': 'SEM_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9469956: {
        'access': 'read-write',
        'name': 'SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    9469957: {
        'access': 'read-write',
        'name': 'SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    9469958: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    9469959: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    9469960: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    9469961: {
        'access': 'read-write',
        'enum': 'SemOffsetSideband',
        'name': 'SEM_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    9469962: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    9469963: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    9469964: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    9469965: {
        'access': 'read-write',
        'enum': 'SemOffsetLimitFailMask',
        'name': 'SEM_OFFSET_LIMIT_FAIL_MASK',
        'type': 'int32'
    },
    9469966: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_START',
        'type': 'float64'
    },
    9469967: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_STOP',
        'type': 'float64'
    },
    9469968: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_START',
        'type': 'float64'
    },
    9469969: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_STOP',
        'type': 'float64'
    },
    9469970: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    9469971: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    9469972: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9469973: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    9469974: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    9469975: {
        'access': 'read-write',
        'enum': 'SemAmplitudeCorrectionType',
        'name': 'SEM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    9469976: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9469977: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9469979: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    9469980: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    9469983: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    9469984: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9469985: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9469986: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    9469987: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY',
        'type': 'float64'
    },
    9469988: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    9469989: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9469990: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9469991: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    9469992: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    9469993: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    9469994: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    9469995: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9469996: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    9469997: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    9469998: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    9469999: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9470000: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    9470001: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    9470002: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    9470003: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    9470004: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    9470005: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    9470006: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    9470007: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    9470008: {
        'access': 'read-write',
        'enum': 'SemDownlinkMaskType',
        'name': 'SEM_DOWNLINK_MASK_TYPE',
        'type': 'int32'
    },
    9470009: {
        'access': 'read-write',
        'name': 'SEM_DELTA_F_MAXIMUM',
        'type': 'float64'
    },
    9470010: {
        'access': 'read-write',
        'name': 'SEM_COMPONENT_CARRIER_RATED_OUTPUT_POWER',
        'type': 'float64'
    },
    9470016: {
        'access': 'read-write',
        'enum': 'SemFftWindow',
        'name': 'SEM_FFT_WINDOW',
        'type': 'int32'
    },
    9470018: {
        'access': 'read-write',
        'enum': 'SemOffsetFrequencyDefinition',
        'name': 'SEM_OFFSET_FREQUENCY_DEFINITION',
        'type': 'int32'
    },
    9474048: {
        'access': 'read-write',
        'name': 'PVT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    9474050: {
        'access': 'read-write',
        'enum': 'PvtMeasurementMethod',
        'name': 'PVT_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    9474051: {
        'access': 'read-write',
        'enum': 'PvtAveragingEnabled',
        'name': 'PVT_AVERAGING_ENABLED',
        'type': 'int32'
    },
    9474052: {
        'access': 'read-write',
        'name': 'PVT_AVERAGING_COUNT',
        'type': 'int32'
    },
    9474053: {
        'access': 'read-write',
        'enum': 'PvtAveragingType',
        'name': 'PVT_AVERAGING_TYPE',
        'type': 'int32'
    },
    9474055: {
        'access': 'read-write',
        'name': 'PVT_OFF_POWER_EXCLUSION_BEFORE',
        'type': 'float64'
    },
    9474056: {
        'access': 'read-write',
        'name': 'PVT_OFF_POWER_EXCLUSION_AFTER',
        'type': 'float64'
    },
    9474057: {
        'access': 'read-write',
        'name': 'PVT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    9474059: {
        'access': 'read-write',
        'name': 'PVT_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    9474060: {
        'access': 'read-write',
        'enum': 'PvtMeasurementStatus',
        'name': 'PVT_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    9474061: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_ABSOLUTE_OFF_POWER_BEFORE',
        'type': 'float64'
    },
    9474062: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_ABSOLUTE_OFF_POWER_AFTER',
        'type': 'float64'
    },
    9474063: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_ABSOLUTE_ON_POWER',
        'type': 'float64'
    },
    9474064: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_BURST_WIDTH',
        'type': 'float64'
    },
    9474068: {
        'access': 'read-write',
        'enum': 'PvtMeasurementIntervalAuto',
        'name': 'PVT_MEASUREMENT_INTERVAL_AUTO',
        'type': 'int32'
    },
    9474069: {
        'access': 'read-write',
        'name': 'PVT_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    9474070: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_PEAK_WINDOWED_OFF_POWER',
        'type': 'float64'
    },
    9474071: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_MARGIN',
        'type': 'float64'
    },
    9474072: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_PEAK_WINDOWED_OFF_POWER_TIME',
        'type': 'float64'
    },
    9486336: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    9490433: {
        'access': 'read-write',
        'enum': 'AcquisitionBandwidthOptimizationEnabled',
        'name': 'ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED',
        'type': 'int32'
    },
    9490434: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    9490435: {
        'access': 'read-write',
        'name': 'NUMBER_OF_RECEIVE_CHAINS',
        'type': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxnr/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/config.py sha256=49e2ee4c44d0e0369add4eb1b0da020b6095c56ec3f67d1d5b29568b43a62309 bytes=2027 -->
## FILE: source/codegen/metadata/nirfmxnr/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/config.py`
- sha256: `49e2ee4c44d0e0369add4eb1b0da020b6095c56ec3f67d1d5b29568b43a62309`
- bytes: 2027

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxNR.h',
    'c_function_prefix': 'RFmxNR_',
    'service_class_prefix': 'NiRFmxNR',
    'java_package': 'com.ni.grpc.nirfmxnr',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxNR',
    'namespace_component': 'nirfmxnr',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': {'custom/nirfmx_errors.h': ['service.cpp']},
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
    'driver_name': 'NI-RFMXNR',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxnr',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxNR.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxNR.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxnr',
    'session_class_description': 'An NI-RFmxNR instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxnr/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/enums.py sha256=b51c9abfd17cc5f7a8e64de304a99005ac41cbe520bb4eaf5509b1dca8152256 bytes=61044 -->
## FILE: source/codegen/metadata/nirfmxnr/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/enums.py`
- sha256: `b51c9abfd17cc5f7a8e64de304a99005ac41cbe520bb4eaf5509b1dca8152256`
- bytes: 61044

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
    'AcpChannelConfigurationType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            },
            {
                'name': 'NS_29',
                'value': 2
            },
            {
                'name': 'STANDARD_REL_16',
                'value': 3
            },
            {
                'name': 'STANDARD_REL_18',
                'value': 4
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
                'name': 'DBM_BY_HZ',
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
    'AcquisitionBandwidthOptimizationEnabled': {
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
    'AutoCellIDDetectionEnabled': {
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
    'AutoIncrementCellIDEnabled': {
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
    'AutoResourceBlockDetectionEnabled': {
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
    'BandwidthPartCyclicPrefixMode': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'EXTENDED',
                'value': 1
            }
        ]
    },
    'BandwidthPartDCLocationKnown': {
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
    'ChpIntegrationBandwidthType': {
        'values': [
            {
                'name': 'SIGNAL_BANDWIDTH',
                'value': 0
            },
            {
                'name': 'CHANNEL_BANDWIDTH',
                'value': 1
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
    'ComponentCarrierAllocated': {
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
    'ComponentCarrierRadioAccessType': {
        'values': [
            {
                'name': 'NR',
                'value': 0
            },
            {
                'name': 'EUTRA',
                'value': 1
            }
        ]
    },
    'ComponentCarrierSpacingType': {
        'values': [
            {
                'name': 'NOMINAL',
                'value': 0
            },
            {
                'name': 'USER',
                'value': 2
            }
        ]
    },
    'CoresetCceToRegMappingType': {
        'values': [
            {
                'name': 'NON_INTERLEAVED',
                'value': 0
            },
            {
                'name': 'INTERLEAVED',
                'value': 1
            }
        ]
    },
    'CoresetPrecodingGranularity': {
        'values': [
            {
                'name': 'SAME_AS_REG_BUNDLE',
                'value': 0
            },
            {
                'name': 'ALL_CONTIGUOUS_RESOURCE_BLOCKS',
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
    'DownlinkChannelConfigurationMode': {
        'values': [
            {
                'name': 'USER_DEFINED',
                'value': 1
            },
            {
                'name': 'TEST_MODEL',
                'value': 2
            }
        ]
    },
    'DownlinkTestModel': {
        'values': [
            {
                'name': 'TM1_1',
                'value': 0
            },
            {
                'name': 'TM1_2',
                'value': 1
            },
            {
                'name': 'TM2',
                'value': 2
            },
            {
                'name': 'TM2A',
                'value': 3
            },
            {
                'name': 'TM3_1',
                'value': 4
            },
            {
                'name': 'TM3_1A',
                'value': 5
            },
            {
                'name': 'TM3_2',
                'value': 6
            },
            {
                'name': 'TM3_3',
                'value': 7
            },
            {
                'name': 'TM2B',
                'value': 8
            },
            {
                'name': 'TM3_1B',
                'value': 9
            }
        ]
    },
    'DownlinkTestModelCellIDMode': {
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
    'DownlinkTestModelDuplexScheme': {
        'values': [
            {
                'name': 'FDD',
                'value': 0
            },
            {
                'name': 'TDD',
                'value': 1
            }
        ]
    },
    'DownlinkTestModelModulationType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'QPSK',
                'value': 1
            },
            {
                'name': 'QAM16',
                'value': 2
            },
            {
                'name': 'QAM64',
                'value': 3
            }
        ]
    },
    'FrequencyRange': {
        'values': [
            {
                'name': 'RANGE1',
                'value': 0
            },
            {
                'name': 'RANGE2_1',
                'value': 1
            },
            {
                'name': 'RANGE2_2',
                'value': 2
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
    'GNodeBCategory': {
        'enum-value-prefix': 'GNODEB_CATEGORY',
        'values': [
            {
                'name': 'WIDE_AREA_BASE_STATION_CATEGORY_A',
                'value': 0
            },
            {
                'name': 'WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION1',
                'value': 1
            },
            {
                'name': 'WIDE_AREA_BASE_STATION_CATEGORY_B_OPTION2',
                'value': 2
            },
            {
                'name': 'LOCAL_AREA_BASE_STATION',
                'value': 3
            },
            {
                'name': 'MEDIUM_RANGE_BASE_STATION',
                'value': 5
            },
            {
                'name': 'FR2_CATEGORY_A',
                'value': 6
            },
            {
                'name': 'FR2_CATEGORY_B',
                'value': 7
            }
        ]
    },
    'GNodeBType': {
        'enum-value-prefix': 'GNODEB_TYPE',
        'values': [
            {
                'name': '1C',
                'value': 0
            },
            {
                'name': '1H',
                'value': 1
            },
            {
                'name': '1O',
                'value': 2
            },
            {
                'name': '2O',
                'value': 3
            }
        ]
    },
    'GridSizeMode': {
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
    'LinkDirection': {
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
    'ListStepTimerUnit': {
        'values': [
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'TIME',
                'value': 6
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'MODACC',
                'value': 1
            },
            {
                'name': 'SEM',
                'value': 2
            },
            {
                'name': 'ACP',
                'value': 4
            },
            {
                'name': 'CHP',
                'value': 8
            },
            {
                'name': 'OBW',
                'value': 16
            },
            {
                'name': 'PVT',
                'value': 32
            },
            {
                'name': 'TXP',
                'value': 64
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
    'ModAccAutoLevelAllowOverflow': {
        'enum-value-prefix': 'MODACC_AUTO_LEVEL_ALLOW_OVERFLOW',
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
    'ModAccAveragingEnabled': {
        'enum-value-prefix': 'MODACC_AVERAGING_ENABLED',
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
    'ModAccCalibrationDataValid': {
        'enum-value-prefix': 'MODACC_CALIBRATION_DATA_VALID',
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
    'ModAccChannelEstimationType': {
        'enum-value-prefix': 'MODACC_CHANNEL_ESTIMATION_TYPE',
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
    'ModAccCommonClockSourceEnabled': {
        'enum-value-prefix': 'MODACC_COMMON_CLOCK_SOURCE_ENABLED',
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
    'ModAccCompositeResultsIncludeDmrs': {
        'enum-value-prefix': 'MODACC_COMPOSITE_RESULTS_INCLUDE_DMRS',
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
    'ModAccCompositeResultsIncludePtrs': {
        'enum-value-prefix': 'MODACC_COMPOSITE_RESULTS_INCLUDE_PTRS',
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
    'ModAccDCSubcarrierRemovalEnabled': {
        'enum-value-prefix': 'MODACC_DC_SUBCARRIER_REMOVAL_ENABLED',
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
    'ModAccEvmReferenceDataSymbolsMode': {
        'enum-value-prefix': 'MODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE',
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
    'ModAccEvmUnit': {
        'enum-value-prefix': 'MODACC_EVM_UNIT',
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
    'ModAccFftWindowType': {
        'enum-value-prefix': 'MODACC_FFT_WINDOW_TYPE',
        'values': [
            {
                'name': '3GPP',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            }
        ]
    },
    'ModAccFrequencyErrorEstimation': {
        'enum-value-prefix': 'MODACC_FREQUENCY_ERROR_ESTIMATION',
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'NORMAL',
                'value': 1
            },
            {
                'name': 'WIDE',
                'value': 2
            }
        ]
    },
    'ModAccIQGainImbalanceCorrectionEnabled': {
        'enum-value-prefix': 'MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED',
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
    'ModAccIQImpairmentsModel': {
        'enum-value-prefix': 'MODACC_IQ_IMPAIRMENTS_MODEL',
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
    'ModAccIQImpairmentsPerSubcarrierEnabled': {
        'enum-value-prefix': 'MODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED',
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
    'ModAccIQMismatchEstimationEnabled': {
        'enum-value-prefix': 'MODACC_IQ_MISMATCH_ESTIMATION_ENABLED',
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
    'ModAccIQOriginOffsetEstimationEnabled': {
        'enum-value-prefix': 'MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED',
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
    'ModAccIQQuadratureErrorCorrectionEnabled': {
        'enum-value-prefix': 'MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED',
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
    'ModAccIQTimingSkewCorrectionEnabled': {
        'enum-value-prefix': 'MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED',
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
    'ModAccMagnitudeAndPhaseErrorEnabled': {
        'enum-value-prefix': 'MODACC_MAGNITUDE_AND_PHASE_ERROR_ENABLED',
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
    'ModAccMeasurementLengthUnit': {
        'enum-value-prefix': 'MODACC_MEASUREMENT_LENGTH_UNIT',
        'values': [
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'SUBFRAME',
                'value': 3
            },
            {
                'name': 'TIME',
                'value': 6
            }
        ]
    },
    'ModAccMeasurementMode': {
        'enum-value-prefix': 'MODACC_MEASUREMENT_MODE',
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
    'ModAccMulticarrierFilterEnabled': {
        'enum-value-prefix': 'MODACC_MULTICARRIER_FILTER_ENABLED',
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
    'ModAccNoiseCompensationApplied': {
        'enum-value-prefix': 'MODACC_NOISE_COMPENSATION_APPLIED',
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
    'ModAccNoiseCompensationEnabled': {
        'enum-value-prefix': 'MODACC_NOISE_COMPENSATION_ENABLED',
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
    'ModAccNoiseCompensationInputPowerCheckEnabled': {
        'enum-value-prefix': 'MODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED',
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
    'ModAccPhaseTrackingMode': {
        'enum-value-prefix': 'MODACC_PHASE_TRACKING_MODE',
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'REFERENCE_AND_DATA',
                'value': 1
            },
            {
                'name': 'PTRS',
                'value': 2
            }
        ]
    },
    'ModAccPreFftErrorEstimationInterval': {
        'enum-value-prefix': 'MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL',
        'values': [
            {
                'name': 'SLOT',
                'value': 0
            },
            {
                'name': 'MEASUREMENT_LENGTH',
                'value': 1
            }
        ]
    },
    'ModAccShortFrameEnabled': {
        'enum-value-prefix': 'MODACC_SHORT_FRAME_ENABLED',
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
    'ModAccShortFrameLengthUnit': {
        'enum-value-prefix': 'MODACC_SHORT_FRAME_LENGTH_UNIT',
        'values': [
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'SUBFRAME',
                'value': 3
            },
            {
                'name': 'TIME',
                'value': 6
            }
        ]
    },
    'ModAccSpectralFlatnessCondition': {
        'enum-value-prefix': 'MODACC_SPECTRAL_FLATNESS_CONDITION',
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'EXTREME',
                'value': 1
            }
        ]
    },
    'ModAccSpectrumInverted': {
        'enum-value-prefix': 'MODACC_SPECTRUM_INVERTED',
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
    'ModAccSymbolClockErrorEstimationEnabled': {
        'enum-value-prefix': 'MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED',
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
    'ModAccSynchronizationMode': {
        'enum-value-prefix': 'MODACC_SYNCHRONIZATION_MODE',
        'values': [
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'FRAME',
                'value': 5
            },
            {
                'name': 'SSB_START_FRAME',
                'value': 7
            }
        ]
    },
    'ModAccTimingTrackingMode': {
        'enum-value-prefix': 'MODACC_TIMING_TRACKING_MODE',
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'REFERENCE_AND_DATA',
                'value': 1
            }
        ]
    },
    'ModAccTransientPeriodEvmMode': {
        'enum-value-prefix': 'MODACC_TRANSIENT_PERIOD_EVM_MODE',
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'EXCLUDE',
                'value': 1
            },
            {
                'name': 'INCLUDE',
                'value': 2
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
    'ObwPowerIntegrationMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'FROM_CENTER',
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
    'ObwSpanAuto': {
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
    'PdschDmrsConfigurationType': {
        'values': [
            {
                'name': '1',
                'value': 0
            },
            {
                'name': '2',
                'value': 1
            }
        ]
    },
    'PdschDmrsDuration': {
        'values': [
            {
                'name': 'SINGLE_SYMBOL',
                'value': 1
            },
            {
                'name': 'DOUBLE_SYMBOL',
                'value': 2
            }
        ]
    },
    'PdschDmrsPowerMode': {
        'values': [
            {
                'name': 'CDM_GROUPS',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PdschDmrsReleaseVersion': {
        'values': [
            {
                'name': 'RELEASE15',
                'value': 0
            },
            {
                'name': 'RELEASE16',
                'value': 1
            }
        ]
    },
    'PdschDmrsScramblingIDMode': {
        'values': [
            {
                'name': 'CELL_ID',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PdschMappingType': {
        'values': [
            {
                'name': 'A',
                'value': 0
            },
            {
                'name': 'B',
                'value': 1
            }
        ]
    },
    'PdschModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 1
            },
            {
                'name': 'QAM16',
                'value': 2
            },
            {
                'name': 'QAM64',
                'value': 3
            },
            {
                'name': 'QAM256',
                'value': 4
            },
            {
                'name': 'QAM1024',
                'value': 5
            },
            {
                'name': 'PSK8',
                'value': 100
            },
            {
                'name': 'QAM4096',
                'value': 6
            }
        ]
    },
    'PdschPtrsEnabled': {
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
    'PdschPtrsPowerMode': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PhaseCompensation': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            },
            {
                'name': 'USER_DEFINED',
                'value': 2
            }
        ]
    },
    'PiBy2BpskPowerBoostEnabled': {
        'enum-value-prefix': 'PI_BY_2_BPSK_POWER_BOOST_ENABLED',
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
    'PuschDmrsConfigurationType': {
        'values': [
            {
                'name': '1',
                'value': 0
            },
            {
                'name': '2',
                'value': 1
            }
        ]
    },
    'PuschDmrsDuration': {
        'values': [
            {
                'name': 'SINGLE_SYMBOL',
                'value': 1
            },
            {
                'name': 'DOUBLE_SYMBOL',
                'value': 2
            }
        ]
    },
    'PuschDmrsGroupHoppingEnabled': {
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
    'PuschDmrsPowerMode': {
        'values': [
            {
                'name': 'CDM_GROUPS',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PuschDmrsPuschIDMode': {
        'values': [
            {
                'name': 'CELL_ID',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PuschDmrsReleaseVersion': {
        'values': [
            {
                'name': 'RELEASE15',
                'value': 0
            },
            {
                'name': 'RELEASE16',
                'value': 1
            }
        ]
    },
    'PuschDmrsScramblingIDMode': {
        'values': [
            {
                'name': 'CELL_ID',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PuschDmrsSequenceHoppingEnabled': {
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
    'PuschMappingType': {
        'values': [
            {
                'name': 'A',
                'value': 0
            },
            {
                'name': 'B',
                'value': 1
            }
        ]
    },
    'PuschModulationType': {
        'values': [
            {
                'name': 'PI_BY_2_BPSK',
                'value': 0
            },
            {
                'name': 'QPSK',
                'value': 1
            },
            {
                'name': 'QAM16',
                'value': 2
            },
            {
                'name': 'QAM64',
                'value': 3
            },
            {
                'name': 'QAM256',
                'value': 4
            },
            {
                'name': 'QAM1024',
                'value': 5
            },
            {
                'name': 'PSK8',
                'value': 100
            },
            {
                'name': 'QAM4096',
                'value': 6
            }
        ]
    },
    'PuschPtrsEnabled': {
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
    'PuschPtrsPowerMode': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'PuschTransformPrecodingEnabled': {
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
    'PvtAveragingEnabled': {
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
    'PvtAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            }
        ]
    },
    'PvtMeasurementIntervalAuto': {
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
    'PvtMeasurementMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'DYNAMIC_RANGE',
                'value': 1
            }
        ]
    },
    'PvtMeasurementStatus': {
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
    'ReferenceGridAlignmentMode': {
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
    'SatelliteAccessNodeClass': {
        'values': [
            {
                'name': 'GEO',
                'value': 0
            },
            {
                'name': 'LEO',
                'value': 1
            }
        ]
    },
    'SatelliteAccessNodeType': {
        'values': [
            {
                'name': '1H',
                'value': 0
            },
            {
                'name': '1O',
                'value': 1
            },
            {
                'name': '2O',
                'value': 2
            }
        ]
    },
    'SchDetectedModulationType': {
        'values': [
            {
                'name': 'PI_BY_2_BPSK',
                'value': 0
            },
            {
                'name': 'QPSK',
                'value': 1
            },
            {
                'name': 'QAM16',
                'value': 2
            },
            {
                'name': 'QAM64',
                'value': 3
            },
            {
                'name': 'QAM256',
                'value': 4
            },
            {
                'name': 'QAM1024',
                'value': 5
            },
            {
                'name': 'PSK8',
                'value': 100
            },
            {
                'name': 'QAM4096',
                'value': 6
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
    'SemDownlinkMaskType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 2
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
    'SemOffsetFrequencyDefinition': {
        'values': [
            {
                'name': 'CARRIER_CENTER_TO_MEAS_BW_CENTER',
                'value': 0
            },
            {
                'name': 'CARRIER_EDGE_TO_MEAS_BW_CENTER',
                'value': 2
            },
            {
                'name': 'SUBBLOCK_EDGE_TO_MEAS_BW_CENTER',
                'value': 6
            }
        ]
    },
    'SemOffsetLimitFailMask': {
        'values': [
            {
                'name': 'ABS_AND_REL',
                'value': 0
            },
            {
                'name': 'ABS_OR_REL',
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
    'SemUplinkMaskType': {
        'values': [
            {
                'name': 'GENERAL',
                'value': 0
            },
            {
                'name': 'NS35',
                'value': 1
            },
            {
                'name': 'CUSTOM',
                'value': 2
            },
            {
                'name': 'NS03',
                'value': 3
            },
            {
                'name': 'NS04',
                'value': 4
            },
            {
                'name': 'NS06',
                'value': 5
            },
            {
                'name': 'NS21',
                'value': 6
            },
            {
                'name': 'NS27',
                'value': 7
            },
            {
                'name': 'NS07',
                'value': 8
            },
            {
                'name': 'NS03U',
                'value': 9
            },
            {
                'name': 'NS21_REL_17_ONWARDS',
                'value': 10
            },
            {
                'name': 'NS04N',
                'value': 11
            },
            {
                'name': 'NS05N',
                'value': 12
            },
            {
                'name': 'NS09N',
                'value': 13
            },
            {
                'name': 'NS10N',
                'value': 14
            },
            {
                'name': 'NS11N',
                'value': 15
            },
            {
                'name': 'NS12N',
                'value': 16
            },
            {
                'name': 'NS203N',
                'value': 17
            },
            {
                'name': 'NS204N',
                'value': 18
            },
            {
                'name': 'NS207N',
                'value': 19
            },
            {
                'name': 'NS208N',
                'value': 20
            },
            {
                'name': 'NS02N',
                'value': 21
            },
            {
                'name': 'NS03N',
                'value': 22
            },
            {
                'name': 'NS06N',
                'value': 23
            },
            {
                'name': 'NS07N',
                'value': 24
            },
            {
                'name': 'NS08N',
                'value': 25
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
    'SsbEnabled': {
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
    'SsbPattern': {
        'values': [
            {
                'name': 'A_UP_TO_3GHZ',
                'value': 0
            },
            {
                'name': 'A_3GHZ_TO_6GHZ',
                'value': 1
            },
            {
                'name': 'B_UP_TO_3GHZ',
                'value': 2
            },
            {
                'name': 'B_3GHZ_TO_6GHZ',
                'value': 3
            },
            {
                'name': 'C_UP_TO_3GHZ',
                'value': 4
            },
            {
                'name': 'C_3GHZ_TO_6GHZ',
                'value': 5
            },
            {
                'name': 'D',
                'value': 6
            },
            {
                'name': 'E',
                'value': 7
            },
            {
                'name': 'F',
                'value': 8
            },
            {
                'name': 'G',
                'value': 9
            }
        ]
    },
    'TransmitterArchitecture': {
        'values': [
            {
                'name': 'LO_PER_COMPONENT_CARRIER',
                'value': 0
            },
            {
                'name': 'LO_PER_SUBBLOCK',
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
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxnr/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/functions.py sha256=57da57bcfb8d34778324aa1470beb281f50bca819ceed4db83429cc8de7c80f8 bytes=310228 -->
## FILE: source/codegen/metadata/nirfmxnr/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/functions.py`
- sha256: `57da57bcfb8d34778324aa1470beb281f50bca819ceed4db83429cc8de7c80f8`
- bytes: 310228

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
    'ACPCfgNumberOfENDCOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfENDCOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfEUTRAOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfEUTRAOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfNROffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfNROffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfUTRAOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfUTRAOffsets',
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
    'ACPFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ACPFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativePower',
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
    'ACPFetchSubblockMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
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
    'ACPFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
        'cname': 'RFmxNR_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
        'cname': 'RFmxNR_AnalyzeNWaveformsIQ',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
            },
            {
                'direction': 'out',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'BuildBandwidthPartString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bandwidthPartNumber',
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
    'BuildCORESETClusterString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'coresetClusterNumber',
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
    'BuildCORESETString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'coresetNumber',
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
    'BuildCarrierString': {
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
    'BuildPDCCHString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pdcchNumber',
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
    'BuildPDSCHClusterString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pdschClusterNumber',
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
    'BuildPDSCHString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pdschNumber',
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
    'BuildPUSCHClusterString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'puschClusterNumber',
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
    'BuildPUSCHString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'puschNumber',
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
    'BuildSubblockString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'subblockNumber',
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
    'CHPFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CHPFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'relativePower',
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
    'CHPFetchSubblockPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
    'CfggNodeBCategory': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'GNodeBCategory',
                'grpc_name': 'gnodeb_category',
                'name': 'gNodeBCategory',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
        'custom_close': 'Close(id, RFMXNR_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXNR_VAL_FALSE)',
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
    'LoadFromGenerationConfigurationFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'configurationIndex',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccAutoLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
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
    'ModAccCfgMeasurementMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccMeasurementMode',
                'name': 'measurementMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgNoiseCompensationEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccNoiseCompensationEnabled',
                'name': 'noiseCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgReferenceWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'ModAccCfgReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxNR_ModAccCfgReferenceWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'ModAccCfgReferenceWaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'ModAccClearNoiseCalibrationDatabase': {
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
    'ModAccFetchCompositeEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'compositePeakEVMMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorMean': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchFrequencyErrorPerSlotMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'frequencyErrorPerSlotMaximum',
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
    'ModAccFetchIQGainImbalancePerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchIQQuadratureErrorPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchInBandEmissionTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'inBandEmission',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'inBandEmissionMask',
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
    'ModAccFetchPBCHDMRSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pbch_dmrs_constellation',
                'name': 'pbchdmrsConstellation',
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
    'ModAccFetchPBCHDMRSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPBCHDMRSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pbch_dmrs_constellation',
                'name': 'pbchdmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pbchdmrsConstellation)'
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
    'ModAccFetchPBCHDMRSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pbch_dmrs_constellation_i',
                'name': 'pbchdmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pbch_dmrs_constellation_q',
                'name': 'pbchdmrsConstellationQ',
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
    'ModAccFetchPBCHDMRSRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pbch_dmrs_rms_evm_per_subcarrier_mean',
                'name': 'pbchdmrsrmsevmPerSubcarrierMean',
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
    'ModAccFetchPBCHDMRSRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pbch_dmrs_rms_evm_per_symbol_mean',
                'name': 'pbchdmrsrmsevmPerSymbolMean',
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
    'ModAccFetchPBCHDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchDataConstellation',
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
    'ModAccFetchPBCHDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPBCHDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pbchDataConstellation)'
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
    'ModAccFetchPBCHDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pbchDataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pbchDataConstellationQ',
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
    'ModAccFetchPBCHDataRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pbch_data_rms_evm_per_subcarrier_mean',
                'name': 'pbchDataRMSEVMPerSubcarrierMean',
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
    'ModAccFetchPBCHDataRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pbch_data_rms_evm_per_symbol_mean',
                'name': 'pbchDataRMSEVMPerSymbolMean',
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
    'ModAccFetchPDSCH1024QAMConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024Constellation',
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
    'ModAccFetchPDSCH1024QAMConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH1024QAMConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam1024Constellation)'
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
    'ModAccFetchPDSCH1024QAMConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam1024ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam1024ConstellationQ',
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
    'ModAccFetchPDSCH16QAMConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
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
    'ModAccFetchPDSCH16QAMConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH16QAMConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam16Constellation)'
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
    'ModAccFetchPDSCH16QAMConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam16ConstellationQ',
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
    'ModAccFetchPDSCH256QAMConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256Constellation',
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
    'ModAccFetchPDSCH256QAMConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH256QAMConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam256Constellation)'
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
    'ModAccFetchPDSCH256QAMConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam256ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam256ConstellationQ',
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
    'ModAccFetchPDSCH4096QAMConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam4096Constellation',
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
    'ModAccFetchPDSCH4096QAMConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH4096QAMConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam4096Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam4096Constellation)'
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
    'ModAccFetchPDSCH4096QAMConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam4096ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam4096ConstellationQ',
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
    'ModAccFetchPDSCH64QAMConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64Constellation',
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
    'ModAccFetchPDSCH64QAMConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH64QAMConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qam64Constellation)'
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
    'ModAccFetchPDSCH64QAMConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qam64ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qam64ConstellationQ',
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
    'ModAccFetchPDSCH8PSKConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psk8Constellation',
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
    'ModAccFetchPDSCH8PSKConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCH8PSKConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psk8Constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(psk8Constellation)'
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
    'ModAccFetchPDSCH8PSKConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'psk8ConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'psk8ConstellationQ',
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
    'ModAccFetchPDSCHDMRSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_dmrs_constellation',
                'name': 'pdschdmrsConstellation',
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
    'ModAccFetchPDSCHDMRSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCHDMRSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_dmrs_constellation',
                'name': 'pdschdmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pdschdmrsConstellation)'
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
    'ModAccFetchPDSCHDMRSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_dmrs_constellation_i',
                'name': 'pdschdmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_dmrs_constellation_q',
                'name': 'pdschdmrsConstellationQ',
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
    'ModAccFetchPDSCHDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdschDataConstellation',
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
    'ModAccFetchPDSCHDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCHDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdschDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pdschDataConstellation)'
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
    'ModAccFetchPDSCHDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pdschDataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pdschDataConstellationQ',
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
    'ModAccFetchPDSCHDemodulatedBits': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'bits',
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
    'ModAccFetchPDSCHPTRSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_ptrs_constellation',
                'name': 'pdschptrsConstellation',
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
    'ModAccFetchPDSCHPTRSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCHPTRSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_ptrs_constellation',
                'name': 'pdschptrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pdschptrsConstellation)'
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
    'ModAccFetchPDSCHPTRSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_ptrs_constellation_i',
                'name': 'pdschptrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pdsch_ptrs_constellation_q',
                'name': 'pdschptrsConstellationQ',
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
    'ModAccFetchPDSCHQPSKConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
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
    'ModAccFetchPDSCHQPSKConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPDSCHQPSKConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(qpskConstellation)'
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
    'ModAccFetchPDSCHQPSKConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qpskConstellationQ',
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
    'ModAccFetchPSSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pssConstellation',
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
    'ModAccFetchPSSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPSSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(pssConstellation)'
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
    'ModAccFetchPSSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'pssConstellationQ',
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
    'ModAccFetchPSSRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pss_rms_evm_per_subcarrier_mean',
                'name': 'pssrmsevmPerSubcarrierMean',
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
    'ModAccFetchPSSRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'pss_rms_evm_per_symbol_mean',
                'name': 'pssrmsevmPerSymbolMean',
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
    'ModAccFetchPUSCHDMRSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_dmrs_constellation',
                'name': 'puschdmrsConstellation',
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
    'ModAccFetchPUSCHDMRSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPUSCHDMRSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_dmrs_constellation',
                'name': 'puschdmrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(puschdmrsConstellation)'
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
    'ModAccFetchPUSCHDMRSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_dmrs_constellation_i',
                'name': 'puschdmrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_dmrs_constellation_q',
                'name': 'puschdmrsConstellationQ',
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
    'ModAccFetchPUSCHDataConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschDataConstellation',
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
    'ModAccFetchPUSCHDataConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPUSCHDataConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschDataConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(puschDataConstellation)'
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
    'ModAccFetchPUSCHDataConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'puschDataConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'puschDataConstellationQ',
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
    'ModAccFetchPUSCHDemodulatedBits': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'bits',
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
    'ModAccFetchPUSCHPTRSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_ptrs_constellation',
                'name': 'puschptrsConstellation',
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
    'ModAccFetchPUSCHPTRSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchPUSCHPTRSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_ptrs_constellation',
                'name': 'puschptrsConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(puschptrsConstellation)'
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
    'ModAccFetchPUSCHPTRSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_ptrs_constellation_i',
                'name': 'puschptrsConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'pusch_ptrs_constellation_q',
                'name': 'puschptrsConstellationQ',
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
    'ModAccFetchPUSCHPhaseOffsetTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'puschPhaseOffset',
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
    'ModAccFetchPeakEVMHighPerSymbolMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'peakEVMHighPerSymbolMaximum',
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
    'ModAccFetchPeakEVMLowPerSymbolMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'peakEVMLowPerSymbolMaximum',
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
    'ModAccFetchPeakEVMPerSlotMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'peakEVMPerSlotMaximum',
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
    'ModAccFetchPeakEVMPerSubcarrierMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'peakEVMPerSubcarrierMaximum',
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
    'ModAccFetchPeakEVMPerSymbolMaximumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'peakEVMPerSymbolMaximum',
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
    'ModAccFetchRMSEVMHighPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_high_per_symbol_mean',
                'name': 'rmsevmHighPerSymbolMean',
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
    'ModAccFetchRMSEVMLowPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_low_per_symbol_mean',
                'name': 'rmsevmLowPerSymbolMean',
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
    'ModAccFetchRMSEVMPerSlotMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_per_slot_mean',
                'name': 'rmsevmPerSlotMean',
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
    'ModAccFetchRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_per_subcarrier_mean',
                'name': 'rmsevmPerSubcarrierMean',
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
    'ModAccFetchRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'rms_evm_per_symbol_mean',
                'name': 'rmsevmPerSymbolMean',
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
    'ModAccFetchSSSConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellation',
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
    'ModAccFetchSSSConstellationTraceInterleavedIQ': {
        'cname': 'RFmxNR_ModAccFetchSSSConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(sssConstellation)'
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
    'ModAccFetchSSSConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'sssConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'sssConstellationQ',
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
    'ModAccFetchSSSRMSEVMPerSubcarrierMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'sss_rms_evm_per_subcarrier_mean',
                'name': 'sssrmsevmPerSubcarrierMean',
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
    'ModAccFetchSSSRMSEVMPerSymbolMeanTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'sss_rms_evm_per_symbol_mean',
                'name': 'sssrmsevmPerSymbolMean',
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
    'ModAccFetchSpectralFlatnessTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'spectralFlatness',
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
    'ModAccFetchSubblockInBandEmissionTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmission',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmissionMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'subblockInBandEmissionRBIndices',
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
    'ModAccFetchTransientPeriodLocationsTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'transientPeriodLocations',
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
    'ModAccValidateCalibrationData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'ModAccCalibrationDataValid',
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
                'name': 'absolutePower',
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
    'OBWFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'PVTCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PvtAveragingEnabled',
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
                'enum': 'PvtAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PVTCfgMeasurementMethod': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PvtMeasurementMethod',
                'name': 'measurementMethod',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PVTCfgOFFPowerExclusionPeriods': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offPowerExclusionBefore',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'offPowerExclusionAfter',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'absoluteOFFPowerBefore',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absoluteOFFPowerAfter',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absoluteONPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'burstWidth',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtMeasurementStatus',
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
                'name': 'absoluteOFFPowerBefore',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'absoluteOFFPowerAfter',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'absoluteONPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'burstWidth',
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
    'PVTFetchSignalPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'signalPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
    'PVTFetchWindowedSignalPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'windowedSignalPower',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
    'SEMCfgComponentCarrierRatedOutputPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierRatedOutputPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMCfgComponentCarrierRatedOutputPowerArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'componentCarrierRatedOutputPower',
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
    'SEMCfgOffsetBandwidthIntegralArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'SEMCfgOffsetLimitFailMaskArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'offsetRBW',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'SemOffsetRbwFilterType',
                'name': 'offsetRBWFilterType',
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
                'name': 'offsetRBW',
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
                'name': 'offsetRBWFilterType',
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
    'SEMCfgUplinkMaskType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SemUplinkMaskType',
                'name': 'uplinkMaskType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchComponentCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'relativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SEMFetchComponentCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'relativePower',
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
    'SEMFetchSubblockMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'subblockPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'integrationBandwidth',
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
    'SEMFetchTotalAggregatedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalAggregatedPower',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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
                'grpc_type': 'NiRFmxNRAttribute',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxnr/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxnr/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxnr/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/__init__.py sha256=9f2093ddaaf188e3d37c1fccce6ee28dbb56756ec05683fd6d89597b24b732f8 bytes=244 -->
## FILE: source/codegen/metadata/nirfmxpulse/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/__init__.py`
- sha256: `9f2093ddaaf188e3d37c1fccce6ee28dbb56756ec05683fd6d89597b24b732f8`
- bytes: 244

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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/attributes.py sha256=4da3bb62d2055c29b49b530bc8d662f2fc222cb803dc3caf3deb0239a83e80b6 bytes=41127 -->
## FILE: source/codegen/metadata/nirfmxpulse/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/attributes.py`
- sha256: `4da3bb62d2055c29b49b530bc8d662f2fc222cb803dc3caf3deb0239a83e80b6`
- bytes: 41127

````python
attributes = {
    12582913: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    12582914: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    12582915: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    12582916: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    12582917: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    12582918: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    12582919: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    12582920: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    12582921: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    12582922: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    12582923: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    12582924: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    12582925: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    12582929: {
        'access': 'read-write',
        'name': 'ACQUISITION_LENGTH',
        'type': 'float64'
    },
    12582930: {
        'access': 'read-write',
        'enum': 'MaximumPulseCountEnabled',
        'name': 'MAXIMUM_PULSE_COUNT_ENABLED',
        'type': 'int32'
    },
    12582931: {
        'access': 'read-write',
        'name': 'MAXIMUM_PULSE_COUNT',
        'type': 'int32'
    },
    12582932: {
        'access': 'read-write',
        'enum': 'SegmentedAcquisitionEnabled',
        'name': 'SEGMENTED_ACQUISITION_ENABLED',
        'type': 'int32'
    },
    12582933: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    12582934: {
        'access': 'read-write',
        'name': 'SEGMENT_ACQUISITION_LENGTH',
        'type': 'float64'
    },
    12582935: {
        'access': 'read-write',
        'name': 'MEASUREMENT_BANDWIDTH',
        'type': 'float64'
    },
    12582936: {
        'access': 'read-write',
        'enum': 'MeasurementFilterType',
        'name': 'MEASUREMENT_FILTER_TYPE',
        'type': 'int32'
    },
    12587004: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    12587005: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    12587007: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    12587008: {
        'access': 'read-write',
        'name': 'PULSE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    12587010: {
        'access': 'read-write',
        'enum': 'PulseDetectionReference',
        'name': 'PULSE_DETECTION_REFERENCE',
        'type': 'int32'
    },
    12587011: {
        'access': 'read-write',
        'name': 'PULSE_DETECTION_THRESHOLD',
        'type': 'float64'
    },
    12587012: {
        'access': 'read-write',
        'name': 'PULSE_DETECTION_HYSTERESIS',
        'type': 'float64'
    },
    12587013: {
        'access': 'read-write',
        'name': 'PULSE_DETECTION_MINIMUM_OFF_DURATION',
        'type': 'float64'
    },
    12587014: {
        'access': 'read-write',
        'name': 'PULSE_DETECTION_MINIMUM_WIDTH',
        'type': 'float64'
    },
    12587015: {
        'access': 'read-write',
        'name': 'PULSE_DETECTION_MAXIMUM_WIDTH',
        'type': 'float64'
    },
    12587016: {
        'access': 'read-write',
        'enum': 'PulseLevelComputationMethod',
        'name': 'PULSE_LEVEL_COMPUTATION_METHOD',
        'type': 'int32'
    },
    12587017: {
        'access': 'read-write',
        'enum': 'PulseAmplitudeLevelDomain',
        'name': 'PULSE_AMPLITUDE_LEVEL_DOMAIN',
        'type': 'int32'
    },
    12587018: {
        'access': 'read-write',
        'name': 'PULSE_UPPER_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    12587019: {
        'access': 'read-write',
        'name': 'PULSE_WIDTH_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    12587020: {
        'access': 'read-write',
        'name': 'PULSE_LOWER_THRESHOLD_LEVEL',
        'type': 'float64'
    },
    12587021: {
        'access': 'read-write',
        'enum': 'PulseDroopCompensationEnabled',
        'name': 'PULSE_DROOP_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    12587022: {
        'access': 'read-write',
        'name': 'PULSE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    12587023: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_COUNT',
        'type': 'int32'
    },
    12587024: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOP_LEVEL',
        'type': 'float64[]'
    },
    12587025: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOP_LEVEL_MEAN',
        'type': 'float64'
    },
    12587026: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOP_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587027: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOP_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587028: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOP_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587029: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BASE_LEVEL',
        'type': 'float64[]'
    },
    12587030: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BASE_LEVEL_MEAN',
        'type': 'float64'
    },
    12587031: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BASE_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587032: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BASE_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587033: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BASE_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587034: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_ON_LEVEL',
        'type': 'float64[]'
    },
    12587035: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_ON_LEVEL_MEAN',
        'type': 'float64'
    },
    12587036: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_ON_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587037: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_ON_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587038: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_ON_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587039: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PEAK_LEVEL',
        'type': 'float64[]'
    },
    12587040: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PEAK_LEVEL_MEAN',
        'type': 'float64'
    },
    12587041: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PEAK_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587042: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PEAK_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587043: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PEAK_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587044: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_LEVEL',
        'type': 'float64[]'
    },
    12587045: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_LEVEL_MEAN',
        'type': 'float64'
    },
    12587046: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587047: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587048: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587049: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_OVERSHOOT',
        'type': 'float64[]'
    },
    12587050: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_OVERSHOOT_MEAN',
        'type': 'float64'
    },
    12587051: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_OVERSHOOT_MAXIMUM',
        'type': 'float64'
    },
    12587052: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_OVERSHOOT_MINIMUM',
        'type': 'float64'
    },
    12587053: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_OVERSHOOT_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587054: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DROOP',
        'type': 'float64[]'
    },
    12587055: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DROOP_MEAN',
        'type': 'float64'
    },
    12587056: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DROOP_MAXIMUM',
        'type': 'float64'
    },
    12587057: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DROOP_MINIMUM',
        'type': 'float64'
    },
    12587058: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DROOP_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587059: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RIPPLE',
        'type': 'float64[]'
    },
    12587060: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RIPPLE_MEAN',
        'type': 'float64'
    },
    12587061: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RIPPLE_MAXIMUM',
        'type': 'float64'
    },
    12587062: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RIPPLE_MINIMUM',
        'type': 'float64'
    },
    12587063: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RIPPLE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587064: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_TIME',
        'type': 'float64[]'
    },
    12587065: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_TIME_MEAN',
        'type': 'float64'
    },
    12587066: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_TIME_MAXIMUM',
        'type': 'float64'
    },
    12587067: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_TIME_MINIMUM',
        'type': 'float64'
    },
    12587068: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_TIME_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587069: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_TIME',
        'type': 'float64[]'
    },
    12587070: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_TIME_MEAN',
        'type': 'float64'
    },
    12587071: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_TIME_MAXIMUM',
        'type': 'float64'
    },
    12587072: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_TIME_MINIMUM',
        'type': 'float64'
    },
    12587073: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_TIME_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587074: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_WIDTH',
        'type': 'float64[]'
    },
    12587075: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_WIDTH_MEAN',
        'type': 'float64'
    },
    12587076: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_WIDTH_MAXIMUM',
        'type': 'float64'
    },
    12587077: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_WIDTH_MINIMUM',
        'type': 'float64'
    },
    12587078: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_WIDTH_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587079: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_OFF_DURATION',
        'type': 'float64[]'
    },
    12587080: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_OFF_DURATION_MEAN',
        'type': 'float64'
    },
    12587081: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_OFF_DURATION_MAXIMUM',
        'type': 'float64'
    },
    12587082: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_OFF_DURATION_MINIMUM',
        'type': 'float64'
    },
    12587083: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_OFF_DURATION_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587084: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DUTY_CYCLE',
        'type': 'float64[]'
    },
    12587085: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DUTY_CYCLE_MEAN',
        'type': 'float64'
    },
    12587086: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DUTY_CYCLE_MAXIMUM',
        'type': 'float64'
    },
    12587087: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DUTY_CYCLE_MINIMUM',
        'type': 'float64'
    },
    12587088: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_DUTY_CYCLE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587089: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_REPETITION_INTERVAL',
        'type': 'float64[]'
    },
    12587090: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MEAN',
        'type': 'float64'
    },
    12587091: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MAXIMUM',
        'type': 'float64'
    },
    12587092: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_REPETITION_INTERVAL_MINIMUM',
        'type': 'float64'
    },
    12587093: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_REPETITION_INTERVAL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587099: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE',
        'type': 'float64[]'
    },
    12587100: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE_MEAN',
        'type': 'float64'
    },
    12587101: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE_MAXIMUM',
        'type': 'float64'
    },
    12587102: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE_MINIMUM',
        'type': 'float64'
    },
    12587103: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587105: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MEAN',
        'type': 'float64'
    },
    12587106: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MAXIMUM',
        'type': 'float64'
    },
    12587107: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_MINIMUM',
        'type': 'float64'
    },
    12587108: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587109: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_DEVIATION',
        'type': 'float64[]'
    },
    12587110: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_DEVIATION_MEAN',
        'type': 'float64'
    },
    12587111: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_DEVIATION_MAXIMUM',
        'type': 'float64'
    },
    12587112: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_DEVIATION_MINIMUM',
        'type': 'float64'
    },
    12587113: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_DEVIATION_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587114: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_FREQUENCY',
        'type': 'float64[]'
    },
    12587115: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_FREQUENCY_MEAN',
        'type': 'float64'
    },
    12587116: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_FREQUENCY_MAXIMUM',
        'type': 'float64'
    },
    12587117: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_FREQUENCY_MINIMUM',
        'type': 'float64'
    },
    12587118: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_FREQUENCY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587119: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE',
        'type': 'float64[]'
    },
    12587120: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_MEAN',
        'type': 'float64'
    },
    12587121: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_MAXIMUM',
        'type': 'float64'
    },
    12587122: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_MINIMUM',
        'type': 'float64'
    },
    12587123: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_FREQUENCY_DIFFERENCE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587124: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_DEVIATION',
        'type': 'float64[]'
    },
    12587125: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_DEVIATION_MEAN',
        'type': 'float64'
    },
    12587126: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_DEVIATION_MAXIMUM',
        'type': 'float64'
    },
    12587127: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_DEVIATION_MINIMUM',
        'type': 'float64'
    },
    12587128: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_DEVIATION_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587129: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AMPLITUDE_STABILITY',
        'type': 'float64[]'
    },
    12587130: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AMPLITUDE_STABILITY_MEAN',
        'type': 'float64'
    },
    12587131: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AMPLITUDE_STABILITY_MAXIMUM',
        'type': 'float64'
    },
    12587132: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AMPLITUDE_STABILITY_MINIMUM',
        'type': 'float64'
    },
    12587133: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AMPLITUDE_STABILITY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587134: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_STABILITY',
        'type': 'float64[]'
    },
    12587135: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_STABILITY_MEAN',
        'type': 'float64'
    },
    12587136: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_STABILITY_MAXIMUM',
        'type': 'float64'
    },
    12587137: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_STABILITY_MINIMUM',
        'type': 'float64'
    },
    12587138: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_STABILITY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587139: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOTAL_STABILITY',
        'type': 'float64[]'
    },
    12587140: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOTAL_STABILITY_MEAN',
        'type': 'float64'
    },
    12587141: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOTAL_STABILITY_MAXIMUM',
        'type': 'float64'
    },
    12587142: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOTAL_STABILITY_MINIMUM',
        'type': 'float64'
    },
    12587143: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TOTAL_STABILITY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587144: {
        'access': 'read-write',
        'name': 'PULSE_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    12587145: {
        'access': 'read-write',
        'enum': 'PulseStabilityFrequencyErrorCompensation',
        'name': 'PULSE_STABILITY_FREQUENCY_ERROR_COMPENSATION',
        'type': 'int32'
    },
    12587146: {
        'access': 'read-write',
        'enum': 'PulseMeasurementPointReference',
        'name': 'PULSE_MEASUREMENT_POINT_REFERENCE',
        'type': 'int32'
    },
    12587147: {
        'access': 'read-write',
        'name': 'PULSE_MEASUREMENT_POINT_OFFSET',
        'type': 'float64'
    },
    12587148: {
        'access': 'read-write',
        'name': 'PULSE_MEASUREMENT_POINT_AVERAGING_DURATION',
        'type': 'float64'
    },
    12587149: {
        'access': 'read-write',
        'enum': 'PulseFrequencyAndPhaseDeviationRangeReference',
        'name': 'PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_REFERENCE',
        'type': 'int32'
    },
    12587150: {
        'access': 'read-write',
        'name': 'PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_LENGTH',
        'type': 'float64'
    },
    12587151: {
        'access': 'read-write',
        'name': 'PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_START',
        'type': 'float64'
    },
    12587152: {
        'access': 'read-write',
        'name': 'PULSE_FREQUENCY_AND_PHASE_DEVIATION_RANGE_EDGE_STOP',
        'type': 'float64'
    },
    12587153: {
        'access': 'read-write',
        'name': 'PULSE_SELECTED_PULSE_TRACE',
        'type': 'int32'
    },
    12587154: {
        'access': 'read-write',
        'name': 'PULSE_STABILITY_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    12587155: {
        'access': 'read-write',
        'name': 'PULSE_STABILITY_REFERENCE_OFFSET',
        'type': 'int32'
    },
    12587156: {
        'access': 'read-write',
        'name': 'PULSE_STABILITY_PULSE_TO_PULSE_OFFSET',
        'type': 'int32'
    },
    12587157: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_AMPLITUDE_STABILITY',
        'type': 'float64'
    },
    12587158: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_PHASE_STABILITY',
        'type': 'float64'
    },
    12587159: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_AVERAGE_TOTAL_STABILITY',
        'type': 'float64'
    },
    12587160: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_TO_PULSE_PHASE_DIFFERENCE',
        'type': 'float64[]'
    },
    12587161: {
        'access': 'read-write',
        'enum': 'PulseStabilityEnabled',
        'name': 'PULSE_STABILITY_ENABLED',
        'type': 'int32'
    },
    12587162: {
        'access': 'read-write',
        'enum': 'PulseMetricsEnabled',
        'name': 'PULSE_METRICS_ENABLED',
        'type': 'int32'
    },
    12587163: {
        'access': 'read-write',
        'enum': 'PulseModulationType',
        'name': 'PULSE_FREQUENCY_AND_PHASE_MODULATION_TYPE',
        'type': 'int32'
    },
    12587164: {
        'access': 'read-write',
        'enum': 'PulseCWFrequencyOffsetAuto',
        'name': 'PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET_AUTO',
        'type': 'int32'
    },
    12587165: {
        'access': 'read-write',
        'name': 'PULSE_FREQUENCY_AND_PHASE_CW_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    12587166: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_RMS',
        'type': 'float64[]'
    },
    12587167: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_RMS_MEAN',
        'type': 'float64'
    },
    12587168: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_RMS_MAXIMUM',
        'type': 'float64'
    },
    12587169: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_RMS_MINIMUM',
        'type': 'float64'
    },
    12587170: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_RMS_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587171: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK',
        'type': 'float64[]'
    },
    12587172: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK_MEAN',
        'type': 'float64'
    },
    12587173: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK_MAXIMUM',
        'type': 'float64'
    },
    12587174: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK_MINIMUM',
        'type': 'float64'
    },
    12587175: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587176: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PHASE_ERROR_PEAK_LOCATION',
        'type': 'float64[]'
    },
    12587177: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_RMS',
        'type': 'float64[]'
    },
    12587178: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_RMS_MEAN',
        'type': 'float64'
    },
    12587179: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_RMS_MAXIMUM',
        'type': 'float64'
    },
    12587180: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_RMS_MINIMUM',
        'type': 'float64'
    },
    12587181: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_RMS_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587182: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK',
        'type': 'float64[]'
    },
    12587183: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK_MEAN',
        'type': 'float64'
    },
    12587184: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK_MAXIMUM',
        'type': 'float64'
    },
    12587185: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK_MINIMUM',
        'type': 'float64'
    },
    12587186: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587187: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FREQUENCY_ERROR_PEAK_LOCATION',
        'type': 'float64[]'
    },
    12587188: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE',
        'type': 'float64[]'
    },
    12587189: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE_MEAN',
        'type': 'float64'
    },
    12587190: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE_MAXIMUM',
        'type': 'float64'
    },
    12587191: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE_MINIMUM',
        'type': 'float64'
    },
    12587192: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587193: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY',
        'type': 'float64[]'
    },
    12587194: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MEAN',
        'type': 'float64'
    },
    12587195: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MAXIMUM',
        'type': 'float64'
    },
    12587196: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_MINIMUM',
        'type': 'float64'
    },
    12587197: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587198: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY',
        'type': 'float64[]'
    },
    12587199: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MEAN',
        'type': 'float64'
    },
    12587200: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MAXIMUM',
        'type': 'float64'
    },
    12587201: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_MINIMUM',
        'type': 'float64'
    },
    12587202: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587213: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE2',
        'type': 'float64[]'
    },
    12587214: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE2_MEAN',
        'type': 'float64'
    },
    12587215: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE2_MAXIMUM',
        'type': 'float64'
    },
    12587216: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE2_MINIMUM',
        'type': 'float64'
    },
    12587217: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_RATE2_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587218: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2',
        'type': 'float64[]'
    },
    12587219: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MEAN',
        'type': 'float64'
    },
    12587220: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MAXIMUM',
        'type': 'float64'
    },
    12587221: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_MINIMUM',
        'type': 'float64'
    },
    12587222: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_START_FREQUENCY2_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587223: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2',
        'type': 'float64[]'
    },
    12587224: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MEAN',
        'type': 'float64'
    },
    12587225: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MAXIMUM',
        'type': 'float64'
    },
    12587226: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_MINIMUM',
        'type': 'float64'
    },
    12587227: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FM_CHIRP_STOP_FREQUENCY2_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587228: {
        'access': 'read-write',
        'enum': 'PulseAmplitudeTraceUnit',
        'name': 'PULSE_AMPLITUDE_TRACE_UNIT',
        'type': 'int32'
    },
    12587229: {
        'access': 'read-write',
        'enum': 'PulseMetricsAmplitudeDeviationUnit',
        'name': 'PULSE_METRICS_AMPLITUDE_DEVIATION_UNIT',
        'type': 'int32'
    },
    12587230: {
        'access': 'read-write',
        'enum': 'MultiburstEnabled',
        'name': 'PULSE_MULTIBURST_ENABLED',
        'type': 'int32'
    },
    12587231: {
        'access': 'read-write',
        'name': 'PULSE_MULTIBURST_LENGTH',
        'type': 'int32'
    },
    12587232: {
        'access': 'read-write',
        'name': 'PULSE_SELECTED_BURST_TRACE',
        'type': 'int32'
    },
    12587233: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_BURST_INDEX',
        'type': 'int32[]'
    },
    12587234: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_PULSE_POSITION_INDEX',
        'type': 'int32[]'
    },
    12587235: {
        'access': 'read-write',
        'enum': 'PulseMultipleMeasurementPointsEnabled',
        'name': 'PULSE_MULTIPLE_MEASUREMENT_POINTS_ENABLED',
        'type': 'int32'
    },
    12587236: {
        'access': 'read-write',
        'name': 'PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_START',
        'type': 'float64'
    },
    12587237: {
        'access': 'read-write',
        'name': 'PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STOP',
        'type': 'float64'
    },
    12587238: {
        'access': 'read-write',
        'name': 'PULSE_MULTIPLE_MEASUREMENT_POINTS_WINDOW_STEP_SIZE',
        'type': 'float64'
    },
    12587239: {
        'access': 'read-write',
        'enum': 'PulseTimeSidelobeEnabled',
        'name': 'PULSE_TIME_SIDELOBE_ENABLED',
        'type': 'int32'
    },
    12587240: {
        'access': 'read-write',
        'enum': 'PulseTimeSidelobeReferenceWindowType',
        'name': 'PULSE_TIME_SIDELOBE_REFERENCE_WINDOW_TYPE',
        'type': 'int32'
    },
    12587241: {
        'access': 'read-write',
        'enum': 'PulseTimeSidelobeKeepOutTimeAuto',
        'name': 'PULSE_TIME_SIDELOBE_KEEP_OUT_TIME_AUTO',
        'type': 'int32'
    },
    12587242: {
        'access': 'read-write',
        'name': 'PULSE_TIME_SIDELOBE_KEEP_OUT_TIME',
        'type': 'float64'
    },
    12587243: {
        'access': 'read-write',
        'name': 'PULSE_TIME_SIDELOBE_MINIMUM_CORRELATION',
        'type': 'float64'
    },
    12587244: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH',
        'type': 'float64[]'
    },
    12587245: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MEAN',
        'type': 'float64'
    },
    12587246: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MAXIMUM',
        'type': 'float64'
    },
    12587247: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_MINIMUM',
        'type': 'float64'
    },
    12587248: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_MAINLOBE_WIDTH_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587249: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_DELAY',
        'type': 'float64[]'
    },
    12587250: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_DELAY_MEAN',
        'type': 'float64'
    },
    12587251: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_DELAY_MAXIMUM',
        'type': 'float64'
    },
    12587252: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_DELAY_MINIMUM',
        'type': 'float64'
    },
    12587253: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_DELAY_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587254: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL',
        'type': 'float64[]'
    },
    12587255: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MEAN',
        'type': 'float64'
    },
    12587256: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MAXIMUM',
        'type': 'float64'
    },
    12587257: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_MINIMUM',
        'type': 'float64'
    },
    12587258: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_SIDELOBE_LEVEL_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587259: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO',
        'type': 'float64[]'
    },
    12587260: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MEAN',
        'type': 'float64'
    },
    12587261: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MAXIMUM',
        'type': 'float64'
    },
    12587262: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_MINIMUM',
        'type': 'float64'
    },
    12587263: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_COMPRESSION_RATIO_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587264: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION',
        'type': 'float64[]'
    },
    12587265: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MEAN',
        'type': 'float64'
    },
    12587266: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MAXIMUM',
        'type': 'float64'
    },
    12587267: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_MINIMUM',
        'type': 'float64'
    },
    12587268: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_TIME_SIDELOBE_PEAK_CORRELATION_STANDARD_DEVIATION',
        'type': 'float64'
    },
    12587272: {
        'access': 'read-write',
        'enum': 'PulseTraceRangeAuto',
        'name': 'PULSE_TRACE_RANGE_AUTO',
        'type': 'int32'
    },
    12587273: {
        'access': 'read-write',
        'enum': 'PulseTraceRangeReference',
        'name': 'PULSE_TRACE_RANGE_REFERENCE',
        'type': 'int32'
    },
    12587274: {
        'access': 'read-write',
        'name': 'PULSE_TRACE_RANGE_OFFSET',
        'type': 'float64'
    },
    12587275: {
        'access': 'read-write',
        'name': 'PULSE_TRACE_RANGE_LENGTH',
        'type': 'float64'
    },
    12587276: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_RISE_EDGE',
        'type': 'float64[]'
    },
    12587277: {
        'access': 'read-write',
        'name': 'PULSE_RESULTS_FALL_EDGE',
        'type': 'float64[]'
    },
    12587278: {
        'access': 'read-write',
        'enum': 'PulseAcquisitionTraceSelect',
        'name': 'PULSE_ACQUISITION_TRACE_SELECT',
        'type': 'int32'
    },
    12587279: {
        'access': 'read-write',
        'name': 'PULSE_ACQUISITION_TRACE_SUBSET_OFFSET',
        'type': 'int32'
    },
    12587280: {
        'access': 'read-write',
        'name': 'PULSE_ACQUISITION_TRACE_SUBSET_LENGTH',
        'type': 'int32'
    },
    12632064: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/attributes_addon.py sha256=2bf9a11cabca22e1871143e397bbd88deb958fbfdd9ea5b0918bfb2f9124a164 bytes=203 -->
## FILE: source/codegen/metadata/nirfmxpulse/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/attributes_addon.py`
- sha256: `2bf9a11cabca22e1871143e397bbd88deb958fbfdd9ea5b0918bfb2f9124a164`
- bytes: 203

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxpulse/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/config.py sha256=b74ca9b0dd32e10633f39265e7478f4335012fb41e538a7fdfd2109931f084cb bytes=1986 -->
## FILE: source/codegen/metadata/nirfmxpulse/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/config.py`
- sha256: `b74ca9b0dd32e10633f39265e7478f4335012fb41e538a7fdfd2109931f084cb`
- bytes: 1986

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxPulse.h',
    'c_function_prefix': 'RFmxPulse_',
    'service_class_prefix': 'NiRFmxPulse',
    'java_package': 'com.ni.grpc.nirfmxpulse',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxPulse',
    'namespace_component': 'nirfmxpulse',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': {},
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
    'driver_name': 'NI-rfmxpulse',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxpulse',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxPulse.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxPulse.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxpulse',
    'session_class_description': 'An NI-RFmxPulse instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxpulse/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxpulse/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxpulse/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````
