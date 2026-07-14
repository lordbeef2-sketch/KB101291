# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/functions.py sha256=5935a0c83da9936ec00fe4ac100670dd6f9eb53e2de0cf255be4e4f4365b4122 bytes=183655 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/functions.py`
- sha256: `5935a0c83da9936ec00fe4ac100670dd6f9eb53e2de0cf255be4e4f4365b4122`
- bytes: 183655

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
    'ACPFetchCarrierAbsolutePower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
        'cname': 'RFmxCDMA2k_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'BuildChannelString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
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
    'CDACfgMeasurementChannel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'walshCodeLength',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'walshCodeNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'CdaMeasurementChannelBranch',
                'name': 'branch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CDACfgPowerUnit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CdaPowerUnit',
                'name': 'powerUnit',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CDACfgSynchronizationModeAndInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CdaSynchronizationMode',
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
    'CDAFetchCodeDomainIAndQPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iMeanActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qMeanActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iPeakInactivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'qPeakInactivePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CDAFetchCodeDomainIAndQPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iCodeDomainPowers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'qCodeDomainPowers',
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
    'CDAFetchCodeDomainPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'totalActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanInactivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakInactivePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CDAFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CDAFetchSymbolConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolConstellation',
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
    'CDAFetchSymbolConstellationTraceInterleavedIQ': {
        'cname': 'RFmxCDMA2k_CDAFetchSymbolConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolConstellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(symbolConstellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CDAFetchSymbolConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolConstellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'symbolConstellationQ',
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
    'CDAFetchSymbolEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsSymbolEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakSymbolEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsSymbolMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsSymbolPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSymbolPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'chipRateError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CDAFetchSymbolEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolEVM',
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
    'CDAFetchSymbolMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolMagnitudeError',
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
    'CDAFetchSymbolPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolPhaseError',
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
    'CDAFetchSymbolPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'symbolPowers',
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
    'CHPFetchCarrierAbsolutePower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CfgBandClass': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bandClass',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgChannelConfigurationMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ChannelConfigurationMode',
                'name': 'channelConfigurationMode',
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
    'CfgFrequencyChannelNumber': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'bandClass',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
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
                'name': 'minimumQuietTimeMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'minimumQuietTime',
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
    'CfgNumberOfChannels': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfChannels',
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
    'CfgRadioConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'RadioConfiguration',
                'name': 'radioConfiguration',
                'type': 'int32'
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
    'CfgUplinkSpreading': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'uplinkSpreadingLongCodeMask',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'CfgUserDefinedChannel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'walshCodeLength',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'walshCodeNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'Branch',
                'name': 'branch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgUserDefinedChannelArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'walshCodeLength',
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
                'name': 'walshCodeNumber',
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
                'enum': 'Branch',
                'name': 'branch',
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
                'name': 'done',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
        'custom_close': 'Close(id, RFMXCDMA2K_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXCDMA2K_VAL_FALSE)',
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
    'ModAccFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxCDMA2k_ModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchDetectedChannel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'detectedWalshCodeLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'detectedWalshCodeNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedBranch',
                'name': 'detectedBranch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDetectedChannelArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'detectedWalshCodeLength',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'detectedWalshCodeNumber',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedBranch',
                'name': 'detectedBranch',
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
    'ModAccFetchEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rms_evm',
                'name': 'rmsevm',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rho',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'chipRateError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsPhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evm',
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
                'name': 'iqOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'magnitudeError',
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
    'ModAccFetchNumberOfDetectedChannels': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberOfDetectedChannels',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPeakActiveCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDEWalshCodeLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDEWalshCodeNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccPeakActiveCdeBranch',
                'name': 'peakActiveCDEBranch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPeakCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakCDEWalshCodeNumber',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccPeakCdeBranch',
                'name': 'peakCDEBranch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'phaseError',
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
    'QEVMCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'QevmAveragingEnabled',
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
    'QEVMCfgMeasurementLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'QEVMFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'QEVMFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxCDMA2k_QEVMFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'QEVMFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'QEVMFetchEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumPeakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanChipRateError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'QEVMFetchEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evm',
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
    'QEVMFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
            },
            {
                'direction': 'out',
                'name': 'maximumIQOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumIQQuadratureError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'QEVMFetchMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'magnitudeError',
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
    'QEVMFetchPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'phaseError',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
    'SEMFetchCarrierAbsoluteIntegratedPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'carrierAbsoluteIntegratedPower',
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
                'name': 'relativeMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
                'bitfield_as_enum_array': 'MeasurementTypes',
                'direction': 'in',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
                'grpc_type': 'NiRFmxCDMA2kAttribute',
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
    'SlotPhaseFetchChipPhaseErrorLinearFitTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'chipPhaseErrorLinearFit',
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
    'SlotPhaseFetchChipPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'chipPhaseError',
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
    'SlotPowerCfgSynchronizationModeAndInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SlotPowerSynchronizationMode',
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
                'name': 'slotPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'slotPowerDelta',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxdemod/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/attributes.py sha256=825fc41e82febe3af1a68beceaeffd38bd8ac234f0fc24c77b9f31eeeaefef6b bytes=19894 -->
## FILE: source/codegen/metadata/nirfmxdemod/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/attributes.py`
- sha256: `825fc41e82febe3af1a68beceaeffd38bd8ac234f0fc24c77b9f31eeeaefef6b`
- bytes: 19894

````python
attributes = {
    2097154: {
        'access': 'read-write',
        'enum': 'ADemodAMCarrierSuppressedEnabled',
        'name': 'ADEMOD_AM_CARRIER_SUPPRESSED',
        'type': 'int32'
    },
    2097155: {
        'access': 'read-write',
        'enum': 'ADemodAudioFilterType',
        'name': 'ADEMOD_AUDIO_FILTER_TYPE',
        'type': 'int32'
    },
    2097156: {
        'access': 'read-write',
        'name': 'ADEMOD_AUDIO_FILTER_LOWER_CUTOFF_FREQUENCY',
        'type': 'float64'
    },
    2097157: {
        'access': 'read-write',
        'name': 'ADEMOD_AUDIO_FILTER_UPPER_CUTOFF_FREQUENCY',
        'type': 'float64'
    },
    2097158: {
        'access': 'read-write',
        'enum': 'ADemodAveragingEnabled',
        'name': 'ADEMOD_AVERAGING_ENABLED',
        'type': 'int32'
    },
    2097159: {
        'access': 'read-write',
        'name': 'ADEMOD_AVERAGING_COUNT',
        'type': 'int32'
    },
    2097161: {
        'access': 'read-write',
        'enum': 'ADemodAveragingType',
        'name': 'ADEMOD_AVERAGING_TYPE',
        'type': 'int32'
    },
    2097162: {
        'access': 'read-write',
        'enum': 'ADemodCarrierFrequencyCorrectionEnabled',
        'name': 'ADEMOD_CARRIER_CORRECTION_FREQUENCY_ENABLED',
        'type': 'int32'
    },
    2097163: {
        'access': 'read-write',
        'enum': 'ADemodCarrierPhaseCorrectionEnabled',
        'name': 'ADEMOD_CARRIER_CORRECTION_PHASE_ENABLED',
        'type': 'int32'
    },
    2097164: {
        'access': 'read-write',
        'name': 'ADEMOD_FM_DEEMPHASIS',
        'type': 'float64'
    },
    2097165: {
        'access': 'read-write',
        'name': 'ADEMOD_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    2097166: {
        'access': 'read-write',
        'enum': 'ADemodModulationType',
        'name': 'ADEMOD_MODULATION_TYPE',
        'type': 'int32'
    },
    2097168: {
        'access': 'read-write',
        'enum': 'ADemodRbwFilterType',
        'name': 'ADEMOD_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    2097169: {
        'access': 'read-write',
        'name': 'ADEMOD_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    2097170: {
        'access': 'read-write',
        'name': 'ADEMOD_RBW_FILTER_ALPHA',
        'type': 'float64'
    },
    2097171: {
        'access': 'read-write',
        'name': 'ADEMOD_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    2097172: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_MEAN_CARRIER_FREQUENCY_ERROR',
        'type': 'float64'
    },
    2097173: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_MEAN_CARRIER_POWER',
        'type': 'float64'
    },
    2097174: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_MEAN_MODULATION_FREQUENCY',
        'type': 'float64'
    },
    2097175: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AVERAGE_SINAD',
        'type': 'float64'
    },
    2097176: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AVERAGE_THD_WITH_NOISE',
        'type': 'float64'
    },
    2097177: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AVERAGE_THD',
        'type': 'float64'
    },
    2097178: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AVERAGE_SNR',
        'type': 'float64'
    },
    2097179: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097180: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097181: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097182: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097183: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MEAN_RMS',
        'type': 'float64'
    },
    2097184: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097185: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097186: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097187: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097188: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_AM_MODULATION_DEPTH_MAXIMUM_RMS',
        'type': 'float64'
    },
    2097189: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MEAN_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097190: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097191: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MEAN_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097192: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MEAN_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097193: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MEAN_RMS',
        'type': 'float64'
    },
    2097194: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097195: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097196: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097197: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097198: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_FM_DEVIATION_MAXIMUM_RMS',
        'type': 'float64'
    },
    2097199: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MEAN_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097200: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MEAN_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097201: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MEAN_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097202: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MEAN_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097203: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MEAN_RMS',
        'type': 'float64'
    },
    2097204: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_STANDARD_DEVIATION',
        'type': 'float64'
    },
    2097205: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_HALF_PEAK_TO_PEAK',
        'type': 'float64'
    },
    2097206: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_POSITIVE_PEAK',
        'type': 'float64'
    },
    2097207: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_NEGATIVE_PEAK',
        'type': 'float64'
    },
    2097208: {
        'access': 'read-write',
        'name': 'ADEMOD_RESULTS_PM_DEVIATION_MAXIMUM_RMS',
        'type': 'float64'
    },
    2097209: {
        'access': 'read-write',
        'name': 'ADEMOD_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    2097216: {
        'access': 'read-write',
        'enum': 'ADemodAudioMeasurementEnabled',
        'name': 'ADEMOD_AUDIO_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    2101248: {
        'access': 'read-write',
        'name': 'DDEMOD_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    2101250: {
        'access': 'read-write',
        'enum': 'DDemodAveragingEnabled',
        'name': 'DDEMOD_AVERAGING_ENABLED',
        'type': 'int32'
    },
    2101251: {
        'access': 'read-write',
        'name': 'DDEMOD_AVERAGING_COUNT',
        'type': 'int32'
    },
    2101253: {
        'access': 'read-write',
        'enum': 'DDemodDifferentialEnabled',
        'name': 'DDEMOD_DIFFERENTIAL_ENABLED',
        'type': 'int32'
    },
    2101254: {
        'access': 'read-write',
        'enum': 'DDemodEqualizerMode',
        'name': 'DDEMOD_EQUALIZER_MODE',
        'type': 'int32'
    },
    2101255: {
        'access': 'read-write',
        'name': 'DDEMOD_EQUALIZER_CONVERGENCE_FACTOR',
        'type': 'float64'
    },
    2101256: {
        'access': 'read-write',
        'name': 'DDEMOD_FSK_DEVIATION',
        'type': 'float64'
    },
    2101257: {
        'access': 'read-write',
        'enum': 'DDemodM',
        'name': 'DDEMOD_M',
        'type': 'int32'
    },
    2101258: {
        'access': 'read-write',
        'enum': 'DDemodMeasurementFilterType',
        'name': 'DDEMOD_MEASUREMENT_FILTER_TYPE',
        'type': 'int32'
    },
    2101259: {
        'access': 'read-write',
        'enum': 'DDemodModulationType',
        'name': 'DDEMOD_MODULATION_TYPE',
        'type': 'int32'
    },
    2101261: {
        'access': 'read-write',
        'name': 'DDEMOD_NUMBER_OF_SYMBOLS',
        'type': 'int32'
    },
    2101262: {
        'access': 'read-write',
        'enum': 'DDemodPskFormat',
        'name': 'DDEMOD_PSK_FORMAT',
        'type': 'int32'
    },
    2101263: {
        'access': 'read-write',
        'enum': 'DDemodPulseShapingFilterType',
        'name': 'DDEMOD_PULSE_SHAPING_FILTER_TYPE',
        'type': 'int32'
    },
    2101264: {
        'access': 'read-write',
        'name': 'DDEMOD_PULSE_SHAPING_FILTER_PARAMETER',
        'type': 'float64'
    },
    2101265: {
        'access': 'read-write',
        'name': 'DDEMOD_SAMPLES_PER_SYMBOL',
        'type': 'int32'
    },
    2101266: {
        'access': 'read-write',
        'enum': 'DDemodSpectrumInverted',
        'name': 'DDEMOD_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    2101267: {
        'access': 'read-write',
        'name': 'DDEMOD_SYMBOL_RATE',
        'type': 'float64'
    },
    2101268: {
        'access': 'read-write',
        'enum': 'DDemodSynchronizationEnabled',
        'name': 'DDEMOD_SYNCHRONIZATION_ENABLED',
        'type': 'int32'
    },
    2101269: {
        'access': 'read-write',
        'name': 'DDEMOD_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    2101279: {
        'access': 'read-write',
        'name': 'DDEMOD_SYNCHRONIZATION_BITS',
        'type': 'int8[]'
    },
    2101281: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_CARRIER_MEAN_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    2101282: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_CARRIER_MEAN_FREQUENCY_DRIFT',
        'type': 'float64'
    },
    2101283: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_CARRIER_MEAN_PHASE_ERROR',
        'type': 'float64'
    },
    2101284: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_EVM_MEAN_RMS',
        'type': 'float64'
    },
    2101285: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_EVM_MAXIMUM_RMS',
        'type': 'float64'
    },
    2101286: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_EVM_MEAN_PEAK',
        'type': 'float64'
    },
    2101287: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_EVM_MAXIMUM_PEAK',
        'type': 'float64'
    },
    2101288: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_EVM_MEAN_MODULATION_ERROR_RATIO',
        'type': 'float64'
    },
    2101289: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_MAGNITUDE_ERROR_MEAN',
        'type': 'float64'
    },
    2101290: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_MAGNITUDE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    2101291: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_PHASE_ERROR_MEAN',
        'type': 'float64'
    },
    2101292: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_PHASE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    2101293: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_FSK_MEAN_DEVIATION',
        'type': 'float64'
    },
    2101294: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_FSK_MEAN_RMS_FSK_ERROR',
        'type': 'float64'
    },
    2101295: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_FSK_MAXIMUM_PEAK_FSK_ERROR',
        'type': 'float64'
    },
    2101296: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    2101297: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_QUADRATURE_SKEW',
        'type': 'float64'
    },
    2101298: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_IQ_IMPAIRMENTS_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    2101300: {
        'access': 'read-write',
        'name': 'DDEMOD_SYNCHRONIZATION_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    2101301: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_SYNC_FOUND',
        'type': 'int32'
    },
    2101302: {
        'access': 'read-write',
        'name': 'DDEMOD_EQUALIZER_FILTER_LENGTH',
        'type': 'int32'
    },
    2101303: {
        'access': 'read-write',
        'name': 'DDEMOD_EQUALIZER_TRAINING_COUNT',
        'type': 'int32'
    },
    2101304: {
        'access': 'read-write',
        'enum': 'DDemodFskReferenceCompensationEnabled',
        'name': 'DDEMOD_FSK_REFERENCE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    2101305: {
        'access': 'read-write',
        'enum': 'DDemodEvmNormalizationReference',
        'name': 'DDEMOD_EVM_NORMALIZATION_REFERENCE',
        'type': 'int32'
    },
    2101306: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_OFFSET_EVM_MEAN_RMS',
        'type': 'float64'
    },
    2101307: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_OFFSET_EVM_MEAN_PEAK',
        'type': 'float64'
    },
    2101308: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_RMS',
        'type': 'float64'
    },
    2101309: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_OFFSET_EVM_MAXIMUM_PEAK',
        'type': 'float64'
    },
    2101310: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_MEAN_RHO_FACTOR',
        'type': 'float64'
    },
    2101311: {
        'access': 'read-write',
        'name': 'DDEMOD_RESULTS_MEAN_AMPLITUDE_DROOP',
        'type': 'float64'
    },
    2101312: {
        'access': 'read-write',
        'enum': 'DDemodSymbolMapType',
        'name': 'DDEMOD_SYMBOL_MAP_TYPE',
        'type': 'int32'
    },
    2101313: {
        'access': 'read-write',
        'enum': 'DDemodSignalStructure',
        'name': 'DDEMOD_SIGNAL_STRUCTURE',
        'type': 'int32'
    },
    2101314: {
        'access': 'read-write',
        'name': 'DDEMOD_BURST_START_EXCLUSION_SYMBOLS',
        'type': 'int32'
    },
    2101315: {
        'access': 'read-write',
        'name': 'DDEMOD_BURST_END_EXCLUSION_SYMBOLS',
        'type': 'int32'
    },
    2101316: {
        'access': 'read-write',
        'enum': 'DDemodIQOffsetRemovalEnabled',
        'name': 'DDEMOD_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    2101317: {
        'access': 'read-write',
        'enum': 'DDemodCfoEstimationMode',
        'name': 'DDEMOD_CFO_ESTIMATION_MODE',
        'type': 'int32'
    },
    2101319: {
        'access': 'read-write',
        'enum': 'DDemodSearchLengthAuto',
        'name': 'DDEMOD_SEARCH_LENGTH_AUTO',
        'type': 'int32'
    },
    2101320: {
        'access': 'read-write',
        'name': 'DDEMOD_SEARCH_LENGTH',
        'type': 'float64'
    },
    2101321: {
        'access': 'read-write',
        'name': 'DDEMOD_APSK_R2_TO_R1_RATIO',
        'type': 'float64'
    },
    2101322: {
        'access': 'read-write',
        'name': 'DDEMOD_APSK_R3_TO_R1_RATIO',
        'type': 'float64'
    },
    2105345: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    2105346: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    2105347: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    2105348: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    2105349: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    2105350: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    2105351: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    2105352: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    2105353: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    2105354: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    2105355: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    2105356: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    2105357: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    2105358: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    2109436: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    2109437: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    2109439: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    2109440: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxdemod/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxdemod/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/config.py sha256=759f475b236bf49f5f123229fd5b061258747506efbf083178148740b429b489 bytes=1988 -->
## FILE: source/codegen/metadata/nirfmxdemod/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/config.py`
- sha256: `759f475b236bf49f5f123229fd5b061258747506efbf083178148740b429b489`
- bytes: 1988

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxDemod.h',
    'c_function_prefix': 'RFmxDemod_',
    'service_class_prefix': 'NiRFmxDemod',
    'java_package': 'com.ni.grpc.nirfmxdemod',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxDemod',
    'namespace_component': 'nirfmxdemod',
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
    'driver_name': 'NI-rfmxdemod',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxdemod',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxDemod.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxDemod.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxdemod',
    'session_class_description': 'An NI-RFmxDemod instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxdemod/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/enums.py sha256=16955c684d83a61efae211cfaf8d77c2de51b106619c351004ca66a683198bc9 bytes=16161 -->
## FILE: source/codegen/metadata/nirfmxdemod/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/enums.py`
- sha256: `16955c684d83a61efae211cfaf8d77c2de51b106619c351004ca66a683198bc9`
- bytes: 16161

````python
enums = {
    'ADemodAMCarrierSuppressedEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ADemodAudioFilterType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            },
            {
                'name': 'A_WEIGHT',
                'value': 2
            },
            {
                'name': 'B_WEIGHT',
                'value': 3
            },
            {
                'name': 'C_WEIGHT',
                'value': 4
            },
            {
                'name': 'CCITT',
                'value': 5
            },
            {
                'name': 'ITU_R_468_4',
                'value': 6
            }
        ]
    },
    'ADemodAudioMeasurementEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ADemodAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ADemodAveragingType': {
        'values': [
            {
                'name': 'LINEAR',
                'value': 0
            },
            {
                'name': 'MAXIMUM',
                'value': 1
            },
            {
                'name': 'MINIMUM',
                'value': 2
            }
        ]
    },
    'ADemodCarrierFrequencyCorrectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ADemodCarrierPhaseCorrectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ADemodModulationType': {
        'values': [
            {
                'name': 'AM',
                'value': 0
            },
            {
                'name': 'FM',
                'value': 1
            },
            {
                'name': 'PM',
                'value': 2
            }
        ]
    },
    'ADemodRbwFilterType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
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
                'name': 'SYNCH_TUNED_4',
                'value': 3
            },
            {
                'name': 'SYNCH_TUNED_5',
                'value': 4
            },
            {
                'name': 'RRC',
                'value': 5
            }
        ]
    },
    'DDemodAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodCfoEstimationMode': {
        'values': [
            {
                'name': 'NARROW',
                'value': 0
            },
            {
                'name': 'WIDE',
                'value': 1
            }
        ]
    },
    'DDemodDifferentialEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodEqualizerMode': {
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
    'DDemodEvmNormalizationReference': {
        'values': [
            {
                'name': 'PEAK',
                'value': 0
            },
            {
                'name': 'RMS',
                'value': 1
            }
        ]
    },
    'DDemodFskReferenceCompensationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodM': {
        'values': [
            {
                'name': '2',
                'value': 2
            },
            {
                'name': '4',
                'value': 4
            },
            {
                'name': '8',
                'value': 8
            },
            {
                'name': '16',
                'value': 16
            },
            {
                'name': '32',
                'value': 32
            },
            {
                'name': '64',
                'value': 64
            },
            {
                'name': '128',
                'value': 128
            },
            {
                'name': '256',
                'value': 256
            },
            {
                'name': '512',
                'value': 512
            },
            {
                'name': '1024',
                'value': 1024
            },
            {
                'name': '2048',
                'value': 2048
            },
            {
                'name': '4096',
                'value': 4096
            }
        ]
    },
    'DDemodMeasurementFilterType': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            }
        ]
    },
    'DDemodModulationType': {
        'values': [
            {
                'name': 'ASK',
                'value': 0
            },
            {
                'name': 'FSK',
                'value': 1
            },
            {
                'name': 'PSK',
                'value': 2
            },
            {
                'name': 'QAM',
                'value': 3
            },
            {
                'name': 'MSK',
                'value': 4
            },
            {
                'name': 'APSK',
                'value': 5
            }
        ]
    },
    'DDemodPskFormat': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'OFFSET_QPSK',
                'value': 1
            },
            {
                'name': 'PI_BY_4_QPSK',
                'value': 2
            },
            {
                'name': 'PI_BY_8_8PSK',
                'value': 3
            },
            {
                'name': '3PI_BY_8_8PSK',
                'value': 4
            },
            {
                'name': 'SHAPED_OFFSET_QPSK',
                'value': 5
            }
        ]
    },
    'DDemodPulseShapingFilterType': {
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
            },
            {
                'name': 'CUSTOM',
                'value': 4
            },
            {
                'name': 'HALF_SINE',
                'value': 5
            },
            {
                'name': 'LINEARIZED_GMSK_EDGE',
                'value': 6
            },
            {
                'name': 'SOQPSK_TG',
                'value': 7
            }
        ]
    },
    'DDemodSearchLengthAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodSignalStructure': {
        'values': [
            {
                'name': 'BURSTED',
                'value': 0
            },
            {
                'name': 'CONTINUOUS',
                'value': 1
            }
        ]
    },
    'DDemodSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DDemodSymbolMapType': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'CUSTOM',
                'value': 1
            }
        ]
    },
    'DDemodSynchronizationEnabled': {
        'values': [
            {
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
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
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
                'name': 'ADEMOD',
                'value': 1
            },
            {
                'name': 'DDEMOD',
                'value': 2
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxdemod/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/functions.py sha256=2914d5201cc883b46990c9101afff39b8772749394fe2015228081345c6c6739 bytes=180973 -->
## FILE: source/codegen/metadata/nirfmxdemod/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/functions.py`
- sha256: `2914d5201cc883b46990c9101afff39b8772749394fe2015228081345c6c6739`
- bytes: 180973

````python
functions = {
    'ADemodCfgAMCarrierSuppressed': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ADemodAMCarrierSuppressedEnabled',
                'name': 'amCarrierSuppressedEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgAudioFilter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ADemodAudioFilterType',
                'name': 'audioFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'audioFilterLowerCutoffFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'audioFilterUpperCutoffFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ADemodAveragingEnabled',
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
                'enum': 'ADemodAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgCarrierCorrection': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ADemodCarrierFrequencyCorrectionEnabled',
                'name': 'carrierFrequencyCorrectionEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ADemodCarrierPhaseCorrectionEnabled',
                'name': 'carrierPhaseCorrectionEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgFMDeEmphasis': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'deEmphasis',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgMeasurementInterval': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'ADemodCfgModulationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ADemodModulationType',
                'name': 'modulationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ADemodCfgRBWFilter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'enum': 'ADemodRbwFilterType',
                'name': 'rbwFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'grpc_name': 'rbw_rrc_alpha',
                'name': 'rbwrrcAlpha',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchAMMaximumModulationDepth': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumModulationDepth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchAMMeanModulationDepth': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanModulationDepth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCarrierFrequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCarrierPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchDemodSignalTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'demodulatedSignal',
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
    'ADemodFetchDemodSpectrumTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'demodulatedSpectrum',
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
    'ADemodFetchDistortions': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageSINAD',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageSNR',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageTHD',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageTHDWithNoise',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchFMMaximumDeviation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchFMMeanDeviation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchMeanModulationFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanModulationFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchPMMaximumDeviation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodFetchPMMeanDeviation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanHalfPeakToPeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMS',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPositivePeak',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanNegativePeak',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodReadAM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanModulationDepth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCarrierPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodReadFM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCarrierFrequencyError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ADemodReadPM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCarrierFrequencyError',
                'type': 'float64'
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
        'cname': 'RFmxDemod_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'DDemodCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodAveragingEnabled',
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
    'DDemodCfgEVMNormalizationReference': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodEvmNormalizationReference',
                'name': 'evmNormRef',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgEqualizer': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodEqualizerMode',
                'name': 'equalizerMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerFilterLength',
                'type': 'int32'
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
                'name': 'equalizerInitialCoefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'equalizerTrainingCount',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerConvergenceFactor',
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
    'DDemodCfgEqualizerInitialCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'equalizerInitialCoefficients',
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
    'DDemodCfgEqualizerInitialCoefficientsInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodCfgEqualizerInitialCoefficients',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'equalizerInitialCoefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerInitialCoefficients)'
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
    'DDemodCfgEqualizerInitialCoefficientsSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'equalizerInitialCoefficientsI',
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
                'name': 'equalizerInitialCoefficientsQ',
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
    'DDemodCfgEqualizerInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodCfgEqualizer',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodEqualizerMode',
                'name': 'equalizerMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerFilterLength',
                'type': 'int32'
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
                'name': 'equalizerInitialCoefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerInitialCoefficients)'
            },
            {
                'direction': 'in',
                'name': 'equalizerTrainingCount',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerConvergenceFactor',
                'type': 'float64'
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
    'DDemodCfgEqualizerSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodEqualizerMode',
                'name': 'equalizerMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerFilterLength',
                'type': 'int32'
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
                'name': 'equalizerInitialCoefficientsI',
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
                'name': 'equalizerInitialCoefficientsQ',
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
                'name': 'equalizerTrainingCount',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'equalizerConvergenceFactor',
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
    'DDemodCfgFSKDeviation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'fskDeviation',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'DDemodFskReferenceCompensationEnabled',
                'name': 'fskRefCompEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodM',
                'name': 'm',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgMeasurementFilter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodMeasurementFilterType',
                'name': 'measurementFilterType',
                'type': 'int32'
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
                'name': 'measurementFilterCustomCoefficients',
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
    'DDemodCfgMeasurementFilterCustomCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'measurementFilterCustomCoefficients',
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
    'DDemodCfgModulationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodModulationType',
                'name': 'modulationType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DDemodM',
                'name': 'm',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'DDemodDifferentialEnabled',
                'name': 'differentialEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgNumberOfSymbols': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfSymbols',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgPSKFormat': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodPskFormat',
                'name': 'pskFormat',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgPulseShapingFilter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodPulseShapingFilterType',
                'name': 'pulseShapingFilterType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'pulseShapingFilterParameter',
                'type': 'float64'
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
                'name': 'pulseShapingFilterCustomCoefficients',
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
    'DDemodCfgPulseShapingFilterCustomCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'pulseShapingFilterCustomCoefficients',
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
    'DDemodCfgSamplesPerSymbol': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'samplesPerSymbol',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgSignalStructure': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSignalStructure',
                'name': 'signalStructure',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgSpectrumInverted': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSpectrumInverted',
                'name': 'spectrumInverted',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgSymbolMap': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSymbolMapType',
                'name': 'symbolMapType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'symbolMap',
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
    'DDemodCfgSymbolMapInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodCfgSymbolMap',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSymbolMapType',
                'name': 'symbolMapType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'symbolMap',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(symbolMap)'
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
    'DDemodCfgSymbolMapSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSymbolMapType',
                'name': 'symbolMapType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'symbolMapI',
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
                'name': 'symbolMapQ',
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
    'DDemodCfgSymbolRate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'symbolRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodCfgSynchronization': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DDemodSynchronizationEnabled',
                'name': 'synchronizationEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'syncBits',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'measurementOffset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchCarrierMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyDrift',
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
    'DDemodFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTrace',
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
    'DDemodFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTrace',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(constellationTrace)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTraceI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'constellationTraceQ',
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
    'DDemodFetchDemodulatedBits': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'demodulatedBits',
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
    'DDemodFetchEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'maximum_rms_evm',
                'name': 'maximumRMSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanModulationErrorRatio',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPeakEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evm',
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
    'DDemodFetchEqualizerCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'DDemodFetchEqualizerCoefficientsInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodFetchEqualizerCoefficients',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'DDemodFetchEqualizerCoefficientsSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'DDemodFetchFSKDeviationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'fskError',
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
    'DDemodFetchFSKResults': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFSKDeviation',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'mean_rms_fsk_error',
                'name': 'meanRMSFSKError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakFSKError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanQuadratureSkew',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQOriginOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMagnitudeError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumMagnitudeError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'magnitudeError',
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
    'DDemodFetchMeanAmplitudeDroop': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAmplitudeDroop',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeanIQOriginOffset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeanQuadratureSkew': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanQuadratureSkew',
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeanRhoFactor': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRhoFactor',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeasurementWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'measurementWaveform',
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
            },
            {
                'direction': 'out',
                'name': 'samplesPerSymbol',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'symbolRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeasurementWaveformInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodFetchMeasurementWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'measurementWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(measurementWaveform)'
            },
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
            {
                'direction': 'out',
                'name': 'samplesPerSymbol',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'symbolRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchMeasurementWaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'measurementWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'measurementWaveformQ',
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
            },
            {
                'direction': 'out',
                'name': 'samplesPerSymbol',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'symbolRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchOffsetConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetConstellationTrace',
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
    'DDemodFetchOffsetConstellationTraceInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodFetchOffsetConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetConstellationTrace',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(offsetConstellationTrace)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchOffsetConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetConstellationTraceI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'offsetConstellationTraceQ',
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
    'DDemodFetchOffsetEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSOffsetEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumRMSOffsetEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakOffsetEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPeakOffsetEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchOffsetEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'offsetEVM',
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
    'DDemodFetchPhaseError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'phaseError',
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
    'DDemodFetchReferenceWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'referenceWaveform',
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
    'DDemodFetchReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodFetchReferenceWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'referenceWaveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(referenceWaveform)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodFetchReferenceWaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'referenceWaveformI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'referenceWaveformQ',
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
    'DDemodFetchSyncFound': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'syncFound',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodGetEqualizerInitialCoefficients': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'equalizerInitialCoefficients',
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
    'DDemodGetEqualizerInitialCoefficientsInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodGetEqualizerInitialCoefficients',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'equalizerInitialCoefficients',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(equalizerInitialCoefficients)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodGetEqualizerInitialCoefficientsSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'equalizerInitialCoefficientsI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'equalizerInitialCoefficientsQ',
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
    'DDemodGetSymbolMap': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'symbolMap',
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
    'DDemodGetSymbolMapInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodGetSymbolMap',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'symbolMap',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(symbolMap)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DDemodGetSymbolMapSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'symbolMapI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'symbolMapQ',
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
    'DDemodRead': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyOffset',
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
                'name': 'maximumPeakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanModulationErrorRatio',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DDemodSetSymbolMap': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
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
    'DDemodSetSymbolMapInterleavedIQ': {
        'cname': 'RFmxDemod_DDemodSetSymbolMap',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(attrVal)'
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
    'DDemodSetSymbolMapSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attrValI',
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
                'name': 'attrValQ',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
    'GetAttributeNIComplexDouble': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'NIComplexDouble'
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
    'GetAttributeNIComplexSingle': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'NIComplexSingle'
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
        'custom_close': 'Close(id, RFMXDEMOD_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXDEMOD_VAL_FALSE)',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'bitfield_as_enum_array': 'MeasurementTypes',
                'direction': 'in',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
    'SetAttributeNIComplexDouble': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'NIComplexDouble'
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
    'SetAttributeNIComplexSingle': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'NIComplexSingle'
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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
                'grpc_type': 'NiRFmxDemodAttribute',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxdemod/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxdemod/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxdemod/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxgsm/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/attributes.py sha256=f080ee983f39508bd04a6f36026029a4083dee5cfc5122e665bace88bf6dfeda bytes=15083 -->
## FILE: source/codegen/metadata/nirfmxgsm/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/attributes.py`
- sha256: `f080ee983f39508bd04a6f36026029a4083dee5cfc5122e665bace88bf6dfeda`
- bytes: 15083

````python
attributes = {
    4194305: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    4194306: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    4194307: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    4194308: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    4194309: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    4194310: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    4194311: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    4194312: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    4194313: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    4194314: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    4194315: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    4194316: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    4194317: {
        'access': 'read-write',
        'enum': 'LinkDirection',
        'name': 'LINK_DIRECTION',
        'type': 'int32'
    },
    4194318: {
        'access': 'read-write',
        'enum': 'Band',
        'name': 'BAND',
        'type': 'int32'
    },
    4194319: {
        'access': 'read-write',
        'name': 'NUMBER_OF_TIMESLOTS',
        'type': 'int32'
    },
    4194320: {
        'access': 'read-write',
        'enum': 'ModulationType',
        'name': 'MODULATION_TYPE',
        'type': 'int32'
    },
    4194321: {
        'access': 'read-write',
        'enum': 'BurstType',
        'name': 'BURST_TYPE',
        'type': 'int32'
    },
    4194322: {
        'access': 'read-write',
        'enum': 'HBFilterWidth',
        'name': 'HB_FILTER_WIDTH',
        'type': 'int32'
    },
    4194323: {
        'access': 'read-write',
        'enum': 'AutoTscDetectionEnabled',
        'name': 'AUTO_TSC_DETECTION_ENABLED',
        'type': 'int32'
    },
    4194324: {
        'access': 'read-write',
        'enum': 'Tsc',
        'name': 'TSC',
        'type': 'int32'
    },
    4194325: {
        'access': 'read-write',
        'name': 'POWER_CONTROL_LEVEL',
        'type': 'int32'
    },
    4194326: {
        'access': 'read-write',
        'enum': 'BurstSynchronizationType',
        'name': 'BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    4194327: {
        'access': 'read-write',
        'enum': 'SignalStructure',
        'name': 'SIGNAL_STRUCTURE',
        'type': 'int32'
    },
    4194328: {
        'access': 'read-write',
        'name': 'TIMING_ADVANCE',
        'type': 'int32'
    },
    4198396: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    4198397: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    4198399: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    4198400: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    4198402: {
        'access': 'read-write',
        'enum': 'ModAccAveragingEnabled',
        'name': 'MODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    4198404: {
        'access': 'read-write',
        'name': 'MODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    4198405: {
        'access': 'read-write',
        'enum': 'ModAccDroopCompensationEnabled',
        'name': 'MODACC_DROOP_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    4198406: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    4198407: {
        'access': 'read-write',
        'name': 'MODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    4198408: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_RMS_EVM',
        'type': 'float64'
    },
    4198409: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_RMS_EVM',
        'type': 'float64'
    },
    4198410: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_PEAK_EVM',
        'type': 'float64'
    },
    4198411: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_PEAK_EVM',
        'type': 'float64'
    },
    4198412: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_95TH_PERCENTILE_EVM',
        'type': 'float64'
    },
    4198413: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_PEAK_EVM_SYMBOL',
        'type': 'int32'
    },
    4198414: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    4198415: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    4198416: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_PHASE_ERROR',
        'type': 'float64'
    },
    4198417: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_PHASE_ERROR',
        'type': 'float64'
    },
    4198418: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_FREQUENCY_ERROR',
        'type': 'float64'
    },
    4198419: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_FREQUENCY_ERROR',
        'type': 'float64'
    },
    4198420: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_AMPLITUDE_DROOP',
        'type': 'float64'
    },
    4198421: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_AMPLITUDE_DROOP',
        'type': 'float64'
    },
    4198422: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MEAN_RMS_PHASE_ERROR',
        'type': 'float64'
    },
    4198423: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MAXIMUM_RMS_PHASE_ERROR',
        'type': 'float64'
    },
    4198424: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MEAN_PEAK_PHASE_ERROR',
        'type': 'float64'
    },
    4198425: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MAXIMUM_PEAK_PHASE_ERROR',
        'type': 'float64'
    },
    4198426: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_PEAK_PHASE_ERROR_SYMBOL',
        'type': 'int32'
    },
    4198427: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MEAN_FREQUENCY_ERROR',
        'type': 'float64'
    },
    4198428: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_MAXIMUM_FREQUENCY_ERROR',
        'type': 'float64'
    },
    4198429: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    4198430: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    4198431: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    4198432: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    4198433: {
        'access': 'read-write',
        'enum': 'ModAccDetectedTsc',
        'name': 'MODACC_RESULTS_DETECTED_TSC',
        'type': 'int32'
    },
    4198435: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_PEAK_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    4198436: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_PEAK_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    4198437: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_95TH_PERCENTILE_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    4198438: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MEAN_PEAK_PHASE_ERROR',
        'type': 'float64'
    },
    4198439: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_MAXIMUM_PEAK_PHASE_ERROR',
        'type': 'float64'
    },
    4198440: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EVM_95TH_PERCENTILE_PHASE_ERROR',
        'type': 'float64'
    },
    4198441: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PFER_95TH_PERCENTILE_PHASE_ERROR',
        'type': 'float64'
    },
    4202496: {
        'access': 'read-write',
        'name': 'ORFS_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    4202498: {
        'access': 'read-write',
        'enum': 'OrfsAveragingEnabled',
        'name': 'ORFS_AVERAGING_ENABLED',
        'type': 'int32'
    },
    4202499: {
        'access': 'read-write',
        'enum': 'OrfsAveragingType',
        'name': 'ORFS_AVERAGING_TYPE',
        'type': 'int32'
    },
    4202500: {
        'access': 'read-write',
        'name': 'ORFS_AVERAGING_COUNT',
        'type': 'int32'
    },
    4202501: {
        'access': 'read-write',
        'enum': 'OrfsMeasurementType',
        'name': 'ORFS_MEASUREMENT_TYPE',
        'type': 'int32'
    },
    4202502: {
        'access': 'read-write',
        'enum': 'OrfsNoiseCompensationEnabled',
        'name': 'ORFS_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    4202503: {
        'access': 'read-write',
        'enum': 'OrfsOffsetFrequencyMode',
        'name': 'ORFS_OFFSET_FREQUENCY_MODE',
        'type': 'int32'
    },
    4202507: {
        'access': 'read-write',
        'name': 'ORFS_MODULATION_CARRIER_RBW',
        'type': 'float64'
    },
    4202510: {
        'access': 'read-write',
        'name': 'ORFS_SWITCHING_CARRIER_RBW',
        'type': 'float64'
    },
    4202513: {
        'access': 'read-write',
        'name': 'ORFS_EVALUATION_SYMBOLS_START',
        'type': 'float64'
    },
    4202514: {
        'access': 'read-write',
        'enum': 'OrfsEvaluationSymbolsIncludeTsc',
        'name': 'ORFS_EVALUATION_SYMBOLS_INCLUDE_TSC',
        'type': 'int32'
    },
    4202515: {
        'access': 'read-write',
        'name': 'ORFS_EVALUATION_SYMBOLS_STOP',
        'type': 'float64'
    },
    4202516: {
        'access': 'read-write',
        'name': 'ORFS_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    4202517: {
        'access': 'read-write',
        'name': 'ORFS_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    4202525: {
        'access': 'read-write',
        'name': 'ORFS_MODULATION_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    4202526: {
        'access': 'read-write',
        'name': 'ORFS_MODULATION_OFFSET_FREQUENCY',
        'type': 'float32'
    },
    4202527: {
        'access': 'read-write',
        'name': 'ORFS_MODULATION_OFFSET_RBW',
        'type': 'float64'
    },
    4202528: {
        'access': 'read-write',
        'name': 'ORFS_SWITCHING_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    4202529: {
        'access': 'read-write',
        'name': 'ORFS_SWITCHING_OFFSET_FREQUENCY',
        'type': 'float32'
    },
    4202530: {
        'access': 'read-write',
        'name': 'ORFS_SWITCHING_OFFSET_RBW',
        'type': 'float64'
    },
    4202532: {
        'access': 'read-write',
        'enum': 'OrfsEvaluationSymbolsScope',
        'name': 'ORFS_EVALUATION_SYMBOLS_SCOPE',
        'type': 'int32'
    },
    4206592: {
        'access': 'read-write',
        'name': 'PVT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    4206594: {
        'access': 'read-write',
        'enum': 'PvtAveragingEnabled',
        'name': 'PVT_AVERAGING_ENABLED',
        'type': 'int32'
    },
    4206596: {
        'access': 'read-write',
        'enum': 'PvtAveragingType',
        'name': 'PVT_AVERAGING_TYPE',
        'type': 'int32'
    },
    4206597: {
        'access': 'read-write',
        'name': 'PVT_AVERAGING_COUNT',
        'type': 'int32'
    },
    4206599: {
        'access': 'read-write',
        'name': 'PVT_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    4206601: {
        'access': 'read-write',
        'name': 'PVT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    4206602: {
        'access': 'read-write',
        'name': 'PVT_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    4206603: {
        'access': 'read-write',
        'enum': 'PvtMeasurementStatus',
        'name': 'PVT_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    4206604: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SLOT_AVERAGE_POWER',
        'type': 'float64'
    },
    4206605: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SLOT_BURST_WIDTH',
        'type': 'float64'
    },
    4206606: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SLOT_MAXIMUM_POWER',
        'type': 'float64'
    },
    4206607: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SLOT_MINIMUM_POWER',
        'type': 'float64'
    },
    4206608: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SLOT_BURST_THRESHOLD',
        'type': 'float64'
    },
    4206609: {
        'access': 'read-write',
        'enum': 'PvtSlotMeasurementStatus',
        'name': 'PVT_RESULTS_SLOT_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    4243456: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    4247552: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    4247555: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxgsm/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxgsm/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/config.py sha256=8e54e6996b1a268aca00433e7dd0eca8f4363bbdcfe00cd0ae653933ec267420 bytes=1964 -->
## FILE: source/codegen/metadata/nirfmxgsm/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/config.py`
- sha256: `8e54e6996b1a268aca00433e7dd0eca8f4363bbdcfe00cd0ae653933ec267420`
- bytes: 1964

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.3.0',
    'c_header': 'niRFmxGSM.h',
    'c_function_prefix': 'RFmxGSM_',
    'service_class_prefix': 'NiRFmxGSM',
    'java_package': 'com.ni.grpc.nirfmxgsm',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxGSM',
    'namespace_component': 'nirfmxgsm',
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
    'driver_name': 'NI-RFMXGSM',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxgsm',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxGSM.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxGSM.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxgsm',
    'session_class_description': 'An NI-RFmxGSM instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxgsm/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/enums.py sha256=b1d5d59f5ffba68b4b7dd3e1d363504014edfda9cb9ec92ed955ee1752aa38bb bytes=14899 -->
## FILE: source/codegen/metadata/nirfmxgsm/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/enums.py`
- sha256: `b1d5d59f5ffba68b4b7dd3e1d363504014edfda9cb9ec92ed955ee1752aa38bb`
- bytes: 14899

````python
enums = {
    'AutoTscDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'Band': {
        'values': [
            {
                'name': 'PGSM',
                'value': 0
            },
            {
                'name': 'EGSM',
                'value': 1
            },
            {
                'name': 'RGSM',
                'value': 2
            },
            {
                'name': 'DCS1800',
                'value': 3
            },
            {
                'name': 'PCS1900',
                'value': 4
            },
            {
                'name': 'GSM450',
                'value': 5
            },
            {
                'name': 'GSM480',
                'value': 6
            },
            {
                'name': 'GSM850',
                'value': 7
            },
            {
                'name': 'GSM750',
                'value': 8
            },
            {
                'name': 'TGSM810',
                'value': 9
            }
        ]
    },
    'BurstSynchronizationType': {
        'values': [
            {
                'name': 'TSC',
                'value': 0
            },
            {
                'name': 'AMPLITUDE',
                'value': 1
            },
            {
                'name': 'NONE',
                'value': 2
            }
        ]
    },
    'BurstType': {
        'values': [
            {
                'name': 'NB',
                'value': 0
            },
            {
                'name': 'HB',
                'value': 1
            },
            {
                'name': 'AB',
                'value': 2
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
    'HBFilterWidth': {
        'values': [
            {
                'name': 'NARROW',
                'value': 0
            },
            {
                'name': 'WIDE',
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
    'MeasurementTypes': {
        'values': [
            {
                'name': 'MODACC',
                'value': 1
            },
            {
                'name': 'ORFS',
                'value': 2
            },
            {
                'name': 'PVT',
                'value': 4
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
    'ModAccDetectedTsc': {
        'enum-value-prefix': 'MODACC_DETECTED_TSC',
        'values': [
            {
                'name': 'UNKNOWN',
                'value': -1
            },
            {
                'name': 'TSC0',
                'value': 0
            },
            {
                'name': 'TSC1',
                'value': 1
            },
            {
                'name': 'TSC2',
                'value': 2
            },
            {
                'name': 'TSC3',
                'value': 3
            },
            {
                'name': 'TSC4',
                'value': 4
            },
            {
                'name': 'TSC5',
                'value': 5
            },
            {
                'name': 'TSC6',
                'value': 6
            },
            {
                'name': 'TSC7',
                'value': 7
            }
        ]
    },
    'ModAccDroopCompensationEnabled': {
        'enum-value-prefix': 'MODACC_DROOP_COMPENSATION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModulationType': {
        'values': [
            {
                'name': 'GMSK',
                'value': 0
            },
            {
                'name': '8PSK',
                'value': 1
            },
            {
                'name': 'QPSK',
                'value': 2
            },
            {
                'name': '16QAM',
                'value': 3
            },
            {
                'name': '32QAM',
                'value': 4
            }
        ]
    },
    'OrfsAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OrfsAveragingType': {
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
    'OrfsEvaluationSymbolsIncludeTsc': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OrfsEvaluationSymbolsScope': {
        'values': [
            {
                'name': 'OFFSET',
                'value': 0
            },
            {
                'name': 'OFFSET_AND_CARRIER',
                'value': 1
            }
        ]
    },
    'OrfsMeasurementType': {
        'values': [
            {
                'name': 'MODULATION_AND_SWITCHING',
                'value': 0
            },
            {
                'name': 'MODULATION',
                'value': 1
            },
            {
                'name': 'SWITCHING',
                'value': 2
            }
        ]
    },
    'OrfsNoiseCompensationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OrfsOffsetFrequencyMode': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'SHORT',
                'value': 1
            },
            {
                'name': 'CUSTOM',
                'value': 2
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
    'PvtSlotMeasurementStatus': {
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
    'SignalStructure': {
        'values': [
            {
                'name': 'BURSTED',
                'value': 0
            },
            {
                'name': 'CONTINUOUS',
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
    'Tsc': {
        'values': [
            {
                'name': 'TSC0',
                'value': 0
            },
            {
                'name': 'TSC1',
                'value': 1
            },
            {
                'name': 'TSC2',
                'value': 2
            },
            {
                'name': 'TSC3',
                'value': 3
            },
            {
                'name': 'TSC4',
                'value': 4
            },
            {
                'name': 'TSC5',
                'value': 5
            },
            {
                'name': 'TSC6',
                'value': 6
            },
            {
                'name': 'TSC7',
                'value': 7
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxgsm/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/functions.py sha256=ff2240b03e46d4da1dbc51f2145406428098db9e0b28434f51b13d014fbb1b07 bytes=120812 -->
## FILE: source/codegen/metadata/nirfmxgsm/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/functions.py`
- sha256: `ff2240b03e46d4da1dbc51f2145406428098db9e0b28434f51b13d014fbb1b07`
- bytes: 120812

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
        'cname': 'RFmxGSM_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'BuildSlotString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'slotNumber',
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
    'CfgAutoTSCDetectionEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AutoTscDetectionEnabled',
                'name': 'autoTSCDetectionEnabled',
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
                'enum': 'Band',
                'name': 'band',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'BurstSynchronizationType',
                'name': 'burstSynchronizationType',
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
    'CfgFrequencyARFCN': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'enum': 'Band',
                'name': 'band',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'arfcn',
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
                'name': 'minimumQuietTimeMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'minimumQuietTime',
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
    'CfgNumberOfTimeslots': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfTimeslots',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPowerControlLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'powerControlLevel',
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
    'CfgSignalType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModulationType',
                'name': 'modulationType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'BurstType',
                'name': 'burstType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'HBFilterWidth',
                'name': 'hbFilterWidth',
                'type': 'int32'
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
    'CfgTSC': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'Tsc',
                'name': 'tsc',
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
                'name': 'done',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
        'custom_close': 'Close(id, RFMXGSM_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXGSM_VAL_FALSE)',
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
    'ModAccCfgDroopCompensationEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccDroopCompensationEnabled',
                'name': 'droopCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTrace',
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
    'ModAccFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxGSM_ModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTrace',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(constellationTrace)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationTraceI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'constellationTraceQ',
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
    'ModAccFetchDemodulatedBits': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'demodulatedBits',
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
    'ModAccFetchDetectedTSC': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedTsc',
                'name': 'detectedTSC',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDetectedTSCArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedTsc',
                'name': 'detectedTSC',
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
    'ModAccFetchEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_name': 'maximum_rms_evm',
                'name': 'maximumRMSEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPeakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ninetyFifthPercentileEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakEVMSymbol',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMAmplitudeDroop': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAmplitudeDroop',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumAmplitudeDroop',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMMagnitudeError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumMagnitudeError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMPhaseError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'evm',
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
                'name': 'meanIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanIQOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumIQOriginOffset',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'magnitudeError',
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
    'ModAccFetchPFER': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumRMSPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanPeakPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanFrequencyError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakSymbol',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'phaseError',
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
    'ORFSCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OrfsAveragingEnabled',
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
                'enum': 'OrfsAveragingType',
                'name': 'averagingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ORFSCfgEvaluationSymbols': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'evaluationSymbolsStart',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'OrfsEvaluationSymbolsIncludeTsc',
                'name': 'evaluationSymbolsIncludeTSC',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'evaluationSymbolsStop',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ORFSCfgMeasurementType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OrfsMeasurementType',
                'name': 'measurementType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ORFSCfgModulationCustomOffsetFrequencyArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'modulationCustomOffsetFrequency',
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
    'ORFSCfgNoiseCompensationEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OrfsNoiseCompensationEnabled',
                'name': 'noiseCompensationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ORFSCfgOffsetFrequencyMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OrfsOffsetFrequencyMode',
                'name': 'offsetFrequencyMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ORFSCfgSwitchingCustomOffsetFrequencyArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'switchingCustomOffsetFrequency',
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
    'ORFSFetchModulationPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'absolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
    'ORFSFetchModulationResultsArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'modulationCarrierPower',
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
    'ORFSFetchSwitchingPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'offsetFrequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'absolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
    'ORFSFetchSwitchingResultsArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'switchingCarrierPower',
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
    'PVTFetchMeasurementStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'upperMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
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
                'name': 'lowerMask',
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
    'PVTFetchSlotMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotAveragePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotBurstWidth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtSlotMeasurementStatus',
                'name': 'slotMeasurementStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'slotMaximumPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotMinimumPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotBurstThreshold',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchSlotMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'slotAveragePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'slotBurstWidth',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'enum': 'PvtSlotMeasurementStatus',
                'name': 'slotMeasurementStatus',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'slotMaximumPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'slotMinimumPower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'slotBurstThreshold',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'bitfield_as_enum_array': 'MeasurementTypes',
                'direction': 'in',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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
                'grpc_type': 'NiRFmxGSMAttribute',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxgsm/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxgsm/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxgsm/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/__init__.py sha256=7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c bytes=371 -->
## FILE: source/codegen/metadata/nirfmxinstr/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/__init__.py`
- sha256: `7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c`
- bytes: 371

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/attributes.py sha256=9a2fb3147174e00bfef301d4a80f8aff1469547f0fa97358b354259fdb078658 bytes=14146 -->
## FILE: source/codegen/metadata/nirfmxinstr/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/attributes.py`
- sha256: `9a2fb3147174e00bfef301d4a80f8aff1469547f0fa97358b354259fdb078658`
- bytes: 14146

````python
attributes = {
    2: {
        'access': 'read-write',
        'enum': 'FrequencyReferenceSource',
        'name': 'FREQUENCY_REFERENCE_SOURCE',
        'type': 'char[]'
    },
    3: {
        'access': 'read-write',
        'name': 'FREQUENCY_REFERENCE_FREQUENCY',
        'type': 'float64'
    },
    4: {
        'access': 'read-write',
        'enum': 'RFAttenuationAuto',
        'name': 'RF_ATTENUATION_AUTO',
        'type': 'int32'
    },
    5: {
        'access': 'read-write',
        'name': 'RF_ATTENUATION_VALUE',
        'type': 'float64'
    },
    6: {
        'access': 'read-write',
        'enum': 'MechanicalAttenuationAuto',
        'name': 'MECHANICAL_ATTENUATION_AUTO',
        'type': 'int32'
    },
    7: {
        'access': 'read-write',
        'name': 'MECHANICAL_ATTENUATION_VALUE',
        'type': 'float64'
    },
    8: {
        'access': 'read-write',
        'enum': 'TuningSpeed',
        'name': 'TUNING_SPEED',
        'type': 'int32'
    },
    9: {
        'access': 'read-write',
        'enum': 'FrequencySettlingUnits',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'int32'
    },
    10: {
        'access': 'read-write',
        'name': 'FREQUENCY_SETTLING',
        'type': 'float64'
    },
    11: {
        'access': 'read-write',
        'enum': 'ChannelCoupling',
        'name': 'CHANNEL_COUPLING',
        'type': 'int32'
    },
    12: {
        'access': 'read-write',
        'enum': 'DownconverterPreselectorEnabled',
        'name': 'DOWNCONVERTER_PRESELECTOR_ENABLED',
        'type': 'int32'
    },
    13: {
        'access': 'read-write',
        'name': 'DOWNCONVERTER_CENTER_FREQUENCY',
        'type': 'float64'
    },
    14: {
        'access': 'read-write',
        'name': 'PREAMP_ENABLED',
        'type': 'int32'
    },
    15: {
        'access': 'read-write',
        'name': 'MIXER_LEVEL_OFFSET',
        'type': 'float64'
    },
    16: {
        'access': 'read-write',
        'name': 'MIXER_LEVEL',
        'type': 'float64'
    },
    17: {
        'access': 'read-write',
        'name': 'IF_OUTPUT_POWER_LEVEL_OFFSET',
        'type': 'float64'
    },
    18: {
        'access': 'read-write',
        'enum': 'LOInjectionSide',
        'name': 'LO_INJECTION_SIDE',
        'type': 'int32'
    },
    19: {
        'access': 'read-write',
        'name': 'PHASE_OFFSET',
        'type': 'float64'
    },
    21: {
        'access': 'read-write',
        'enum': 'DigitizerDitherEnabled',
        'name': 'DIGITIZER_DITHER_ENABLED',
        'type': 'int32'
    },
    22: {
        'access': 'read-write',
        'name': 'FFT_WIDTH',
        'type': 'float64'
    },
    23: {
        'access': 'read-write',
        'enum': 'OspDelayEnabled',
        'name': 'OSP_DELAY_ENABLED',
        'type': 'int32'
    },
    24: {
        'access': 'read-write',
        'name': 'DEVICE_TEMPERATURE',
        'type': 'float64'
    },
    25: {
        'access': 'read-write',
        'name': 'DIGITIZER_TEMPERATURE',
        'type': 'float64'
    },
    26: {
        'access': 'read-write',
        'name': 'LO_TEMPERATURE',
        'type': 'float64'
    },
    27: {
        'access': 'read-write',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'char[]'
    },
    28: {
        'access': 'read-write',
        'name': 'INSTRUMENT_MODEL',
        'type': 'char[]'
    },
    29: {
        'access': 'read-write',
        'name': 'MODULE_REVISION',
        'type': 'char[]'
    },
    30: {
        'access': 'read-write',
        'name': 'SERIAL_NUMBER',
        'type': 'char[]'
    },
    31: {
        'access': 'read-write',
        'name': 'PRESELECTOR_PRESENT',
        'type': 'int32'
    },
    32: {
        'access': 'read-write',
        'name': 'RF_PREAMP_PRESENT',
        'type': 'int32'
    },
    33: {
        'access': 'read-write',
        'enum': 'LOExportEnabled',
        'name': 'LO_EXPORT_ENABLED',
        'type': 'int32'
    },
    34: {
        'access': 'read-write',
        'enum': 'FrequencyReferenceExportedTerminal',
        'name': 'FREQUENCY_REFERENCE_EXPORTED_TERMINAL',
        'type': 'char[]'
    },
    35: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'TRIGGER_EXPORT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    36: {
        'access': 'read-write',
        'name': 'TRIGGER_TERMINAL_NAME',
        'type': 'char[]'
    },
    37: {
        'access': 'read-write',
        'enum': 'CleanerSpectrumEnabled',
        'name': 'CLEANER_SPECTRUM_ENABLED',
        'type': 'int32'
    },
    39: {
        'access': 'read-write',
        'enum': 'RecommendedAcquisitionType',
        'name': 'RECOMMENDED_ACQUISITION_TYPE',
        'type': 'int32'
    },
    40: {
        'access': 'read-write',
        'name': 'RECOMMENDED_NUMBER_OF_RECORDS',
        'type': 'int32'
    },
    41: {
        'access': 'read-write',
        'name': 'RECOMMENDED_TRIGGER_MINIMUM_QUIET_TIME',
        'type': 'float64'
    },
    42: {
        'access': 'read-write',
        'name': 'RECOMMENDED_IQ_ACQUISITION_TIME',
        'type': 'float64'
    },
    43: {
        'access': 'read-write',
        'name': 'RECOMMENDED_IQ_MINIMUM_SAMPLE_RATE',
        'type': 'float64'
    },
    44: {
        'access': 'read-write',
        'name': 'RECOMMENDED_IQ_PRE_TRIGGER_TIME',
        'type': 'float64'
    },
    45: {
        'access': 'read-write',
        'name': 'RECOMMENDED_SPECTRAL_ACQUISITION_SPAN',
        'type': 'float64'
    },
    46: {
        'access': 'read-write',
        'enum': 'RecommendedSpectralFftWindow',
        'name': 'RECOMMENDED_SPECTRAL_FFT_WINDOW',
        'type': 'int32'
    },
    47: {
        'access': 'read-write',
        'name': 'RECOMMENDED_SPECTRAL_RESOLUTION_BANDWIDTH',
        'type': 'float64'
    },
    48: {
        'access': 'read-write',
        'name': 'IF_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    49: {
        'access': 'read-write',
        'name': 'RF_HIGHPASS_FILTER_FREQUENCY',
        'type': 'float64'
    },
    50: {
        'access': 'read-write',
        'name': 'SUBSPAN_OVERLAP',
        'type': 'float64'
    },
    51: {
        'access': 'read-write',
        'name': 'RECOMMENDED_IQ_MEASUREMENT_BANDWIDTH',
        'type': 'float64'
    },
    52: {
        'access': 'read-write',
        'name': 'DOWNCONVERTER_GAIN',
        'type': 'float64'
    },
    53: {
        'access': 'read-write',
        'name': 'DOWNCONVERTER_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    54: {
        'access': 'read-write',
        'name': 'RF_ATTENUATION_STEP_SIZE',
        'type': 'float64'
    },
    55: {
        'access': 'read-write',
        'enum': 'LOLeakageAvoidanceEnabled',
        'name': 'LO_LEAKAGE_AVOIDANCE_ENABLED',
        'type': 'int32'
    },
    56: {
        'access': 'read-write',
        'name': 'AMPLITUDE_SETTLING',
        'type': 'float64'
    },
    57: {
        'access': 'read-write',
        'name': 'RECOMMENDED_CENTER_FREQUENCY',
        'type': 'float64'
    },
    58: {
        'access': 'read-write',
        'enum': 'LO2ExportEnabled',
        'name': 'LO2_EXPORT_ENABLED',
        'type': 'int32'
    },
    59: {
        'access': 'read-write',
        'enum': 'LOSource',
        'name': 'LO_SOURCE',
        'type': 'char[]'
    },
    60: {
        'access': 'read-write',
        'name': 'LO_FREQUENCY',
        'type': 'float64'
    },
    68: {
        'access': 'read-write',
        'enum': 'LOSharingMode',
        'name': 'LO_SHARING_MODE',
        'type': 'int32'
    },
    70: {
        'access': 'read-write',
        'name': 'COMMON_MODE_LEVEL',
        'type': 'float64'
    },
    71: {
        'access': 'read-write',
        'name': 'SMU_RESOURCE_NAME',
        'type': 'char[]'
    },
    72: {
        'access': 'read-write',
        'name': 'SMU_CHANNEL',
        'type': 'char[]'
    },
    74: {
        'access': 'read-write',
        'enum': 'AutomaticSGSASharedLOEnabled',
        'name': 'AUTOMATIC_SG_SA_SHARED_LO_ENABLED',
        'type': 'int32'
    },
    77: {
        'access': 'read-write',
        'enum': 'OverflowErrorReporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'int32'
    },
    78: {
        'access': 'read-write',
        'name': 'LO_IN_POWER',
        'type': 'float64'
    },
    79: {
        'access': 'read-write',
        'name': 'LO_OUT_POWER',
        'type': 'float64'
    },
    80: {
        'access': 'read-write',
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'float64'
    },
    84: {
        'access': 'read-write',
        'name': 'DIGITAL_GAIN',
        'type': 'float64'
    },
    90: {
        'access': 'read-write',
        'enum': 'LOPllFractionalModeEnabled',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'type': 'int32'
    },
    91: {
        'access': 'read-write',
        'enum': 'OptimizePathForSignalBandwidth',
        'name': 'OPTIMIZE_PATH_FOR_SIGNAL_BANDWIDTH',
        'type': 'int32'
    },
    92: {
        'access': 'read-write',
        'enum': 'InputIsolationEnabled',
        'name': 'INPUT_ISOLATION_ENABLED',
        'type': 'int32'
    },
    94: {
        'access': 'read-write',
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'float64'
    },
    95: {
        'access': 'read-write',
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'float64'
    },
    97: {
        'access': 'read-write',
        'name': 'NUMBER_OF_LO_SHARING_GROUPS',
        'type': 'int32'
    },
    98: {
        'access': 'read-write',
        'enum': 'StartTriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'int32'
    },
    99: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'START_TRIGGER_DIGITAL_EDGE_SOURCE',
        'type': 'char[]'
    },
    100: {
        'access': 'read-write',
        'enum': 'StartTriggerDigitalEdge',
        'name': 'START_TRIGGER_DIGITAL_EDGE',
        'type': 'int32'
    },
    101: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'START_TRIGGER_EXPORT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    102: {
        'access': 'read-write',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'char[]'
    },
    103: {
        'access': 'read-write',
        'enum': 'AdvanceTriggerType',
        'name': 'ADVANCE_TRIGGER_TYPE',
        'type': 'int32'
    },
    104: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'ADVANCE_TRIGGER_DIGITAL_EDGE_SOURCE',
        'type': 'char[]'
    },
    105: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'ADVANCE_TRIGGER_EXPORT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    106: {
        'access': 'read-write',
        'name': 'ADVANCE_TRIGGER_TERMINAL_NAME',
        'type': 'char[]'
    },
    107: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    108: {
        'access': 'read-write',
        'name': 'READY_FOR_START_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    109: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    110: {
        'access': 'read-write',
        'name': 'READY_FOR_ADVANCE_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    111: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'READY_FOR_REFERENCE_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    112: {
        'access': 'read-write',
        'name': 'READY_FOR_REFERENCE_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    113: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    114: {
        'access': 'read-write',
        'name': 'END_OF_RECORD_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    115: {
        'access': 'read-write',
        'enum': 'OutputTerminal',
        'name': 'DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    116: {
        'access': 'read-write',
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    117: {
        'access': 'read-write',
        'enum': 'SelfCalibrationValidityCheck',
        'name': 'SELF_CALIBRATION_VALIDITY_CHECK',
        'type': 'int32'
    },
    118: {
        'access': 'read-write',
        'name': 'SELF_CALIBRATION_VALIDITY_CHECK_TIME_INTERVAL',
        'type': 'float64'
    },
    119: {
        'access': 'read-write',
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'float64'
    },
    120: {
        'access': 'read-write',
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'float64'
    },
    128: {
        'access': 'read-write',
        'name': 'NUMBER_OF_RAW_IQ_RECORDS',
        'type': 'int32'
    },
    163: {
        'access': 'read-write',
        'enum': 'LoadOptions',
        'name': 'LOAD_OPTIONS',
        'type': 'int32[]'
    },
    184: {
        'access': 'read-write',
        'name': 'LO_SPLITTER_LOSS_FREQUENCY',
        'type': 'float64[]'
    },
    185: {
        'access': 'read-write',
        'name': 'LO_SPLITTER_LOSS',
        'type': 'float64[]'
    },
    188: {
        'access': 'read-write',
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'char[]'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfmxinstr/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/config.py sha256=2642f9fba14713096175ad3d70cce9074cd13ea7d0cae0cd44c030731e72611f bytes=2144 -->
## FILE: source/codegen/metadata/nirfmxinstr/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/config.py`
- sha256: `2642f9fba14713096175ad3d70cce9074cd13ea7d0cae0cd44c030731e72611f`
- bytes: 2144

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxInstr.h',
    'c_function_prefix': 'RFmxInstr_',
    'service_class_prefix': 'NiRFmxInstr',
    'java_package': 'com.ni.grpc.nirfmxinstr',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxInstr',
    'namespace_component': 'nirfmxinstr',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': { 'ivi.h': ['service.h'], 'custom/nirfmx_errors.h': ['service.cpp'] },
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
        "CVIAbsoluteTime": "google.protobuf.Timestamp",
    },
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-RFMXINSTR',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxinstr',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxInstr.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxInstr.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxinstr',
    'session_class_description': 'An NI-RFmxInstr instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxinstr/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/enums.py sha256=5a56283d9f28604ecf1e129567643c415d71334ed1035c7c4df9f25310b78f15 bytes=19215 -->
## FILE: source/codegen/metadata/nirfmxinstr/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/enums.py`
- sha256: `5a56283d9f28604ecf1e129567643c415d71334ed1035c7c4df9f25310b78f15`
- bytes: 19215

````python
enums = {
    'AdvanceTriggerType': {
        'values': [
            {
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SOFTWARE',
                'value': 3
            }
        ]
    },
    'AutomaticSGSASharedLOEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ChannelCoupling': {
        'values': [
            {
                'name': 'AC_COUPLED',
                'value': 0
            },
            {
                'name': 'DC_COUPLED',
                'value': 1
            }
        ]
    },
    'CleanerSpectrumEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
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
            }
        ]
    },
    'DigitizerDitherEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DownconverterPreselectorEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ExportSignalSource': {
        'values': [
            {
                'name': 'START_TRIGGER',
                'value': 0
            },
            {
                'name': 'REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'name': 'ADVANCE_TRIGGER',
                'value': 2
            },
            {
                'name': 'READY_FOR_START_EVENT',
                'value': 3
            },
            {
                'name': 'READY_FOR_REFERENCE_EVENT',
                'value': 4
            },
            {
                'name': 'READY_FOR_ADVANCE_EVENT',
                'value': 5
            },
            {
                'name': 'END_OF_RECORD_EVENT',
                'value': 6
            },
            {
                'name': 'DONE_EVENT',
                'value': 7
            },
            {
                'name': 'REFERENCE_CLOCK',
                'value': 8
            }
        ]
    },
    'FrequencyReferenceExportedTerminal': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'NONE',
                'value': ''
            },
            {
                'name': 'REF_OUT',
                'value': 'RefOut'
            },
            {
                'name': 'REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'name': 'CLK_OUT',
                'value': 'ClkOut'
            },
            {
                'name': 'DO_NOT_EXPORT',
                'value': ''
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
                'value': 'PXI_ClkMaster'
            }
        ]
    },
    'FrequencySettlingUnits': {
        'values': [
            {
                'name': 'PPM',
                'value': 0
            },
            {
                'name': 'SECONDS_AFTER_IO',
                'value': 2
            },
            {
                'name': 'SECONDS_AFTER_LOCK',
                'value': 1
            }
        ]
    },
    'InputIsolationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LO2ExportEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOExportEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOInjectionSide': {
        'values': [
            {
                'name': 'HIGH_SIDE',
                'value': 0
            },
            {
                'name': 'LOW_SIDE',
                'value': 1
            }
        ]
    },
    'LOLeakageAvoidanceEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOPllFractionalModeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LOSharingMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'EXTERNAL_DAISY_CHAIN',
                'value': 4
            },
            {
                'name': 'EXTERNAL_STAR',
                'value': 3
            },
            {
                'name': 'SPLITTER_AND_DAISY_CHAIN',
                'value': 5
            }
        ]
    },
    'LOSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'AUTOMATIC_SG_SA_SHARED',
                'value': 'Automatic_SG_SA_Shared'
            },
            {
                'name': 'LO_IN',
                'value': 'LO_In'
            },
            {
                'name': 'NONE',
                'value': 'None'
            },
            {
                'name': 'ONBOARD',
                'value': 'Onboard'
            },
            {
                'name': 'SECONDARY',
                'value': 'Secondary'
            },
            {
                'name': 'SG_SA_SHARED',
                'value': 'SG_SA_Shared'
            }
        ]
    },
    'LinearInterpolationFormat': {
        'values': [
            {
                'name': 'MAGNITUDE_AND_PHASE',
                'value': 1
            },
            {
                'name': 'MAGNITUDE_DB_AND_PHASE',
                'value': 2
            },
            {
                'name': 'REAL_AND_IMAGINARY',
                'value': 0
            }
        ]
    },
    'LoadOptions': {
        'values': [
            {
                'name': 'SKIP_NONE',
                'value': 0
            },
            {
                'name': 'SKIP_RFINSTR',
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
    'OptimizePathForSignalBandwidth': {
        'values': [
            {
                'name': 'AUTOMATIC',
                'value': 2
            },
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'ENABLED',
                'value': 1
            }
        ]
    },
    'OspDelayEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'OutputTerminal': {
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
                'name': 'PXIE_DSTARC',
                'value': 'PXIe_DStarC'
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
    'OverflowErrorReporting': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 1
            },
            {
                'name': 'WARNING',
                'value': 0
            }
        ]
    },
    'Personality': {
        'values': [
            {
                'name': 'ALL',
                'value': 2147483647
            },
            {
                'name': 'BT',
                'value': 1024
            },
            {
                'name': 'CDMA2K',
                'value': 32
            },
            {
                'name': 'DEMOD',
                'value': 2
            },
            {
                'name': 'EVDO',
                'value': 128
            },
            {
                'name': 'GSM',
                'value': 8
            },
            {
                'name': 'LTE',
                'value': 4
            },
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'NR',
                'value': 256
            },
            {
                'name': 'PULSE',
                'value': 2048
            },
            {
                'name': 'SPECAN',
                'value': 1
            },
            {
                'name': 'TDSCDMA',
                'value': 64
            },
            {
                'name': 'UWB',
                'value': 8192
            },
            {
                'name': 'VNA',
                'value': 4096
            },
            {
                'name': 'WCDMA',
                'value': 16
            },
            {
                'name': 'WLAN',
                'value': 512
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
    'RecommendedAcquisitionType': {
        'values': [
            {
                'name': 'IQ',
                'value': 0
            },
            {
                'name': 'IQ_OR_SPECTRAL',
                'value': 2
            },
            {
                'name': 'SPECTRAL',
                'value': 1
            }
        ]
    },
    'RecommendedSpectralFftWindow': {
        'values': [
            {
                'name': 'BLACKMAN',
                'value': 5
            },
            {
                'name': 'BLACKMAN_HARRIS',
                'value': 6
            },
            {
                'name': 'FLAT_TOP',
                'value': 1
            },
            {
                'name': 'GAUSSIAN',
                'value': 4
            },
            {
                'name': 'HAMMING',
                'value': 3
            },
            {
                'name': 'HANNING',
                'value': 2
            },
            {
                'name': 'KAISER_BESSEL',
                'value': 7
            },
            {
                'name': 'NONE',
                'value': 0
            }
        ]
    },
    'SParameterOrientation': {
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
    'SParameterType': {
        'values': [
            {
                'name': 'AMPLITUDE_AND_PHASE_FLATNESS',
                'value': 4
            },
            {
                'name': 'AMPLITUDE_FLATNESS',
                'value': 3
            },
            {
                'name': 'SCALAR',
                'value': 1
            },
            {
                'name': 'VECTOR',
                'value': 2
            }
        ]
    },
    'SelfCalStep': {
        'values': [
            {
                'name': 'AMPLITUDE_ACCURACY',
                'value': 32
            },
            {
                'name': 'DC_OFFSET',
                'value': 512
            },
            {
                'name': 'DIGITIZER_SELF_CAL',
                'value': 8
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
                'name': 'IMAGE_SUPPRESSION',
                'value': 128
            },
            {
                'name': 'LO_SELF_CAL',
                'value': 16
            },
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PRESELECTOR_ALIGNMENT',
                'value': 1
            },
            {
                'name': 'RESIDUAL_LO_POWER',
                'value': 64
            },
            {
                'name': 'SYNTHESIZER_ALIGNMENT',
                'value': 256
            }
        ]
    },
    'SelfCalibrationValidityCheck': {
        'values': [
            {
                'name': 'ENABLED',
                'value': 1
            },
            {
                'name': 'OFF',
                'value': 0
            }
        ]
    },
    'StartTriggerDigitalEdge': {
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
    'StartTriggerType': {
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
                'name': 'SOFTWARE',
                'value': 3
            }
        ]
    },
    'TuningSpeed': {
        'values': [
            {
                'name': 'FAST',
                'value': 2
            },
            {
                'name': 'MEDIUM',
                'value': 1
            },
            {
                'name': 'NORMAL',
                'value': 0
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/enums_addon.py sha256=73a5e3d360e5de4ef22b66235837bf967a61ee970592c5ea37e0375d65cdf722 bytes=316 -->
## FILE: source/codegen/metadata/nirfmxinstr/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/enums_addon.py`
- sha256: `73a5e3d360e5de4ef22b66235837bf967a61ee970592c5ea37e0375d65cdf722`
- bytes: 316

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "FrequencyReferenceExportedTerminal": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/functions.py sha256=7d6296d1e22c11f56a03ae1a440e67c74ff34c77ad608af61703ee0bdab5a107 bytes=94144 -->
## FILE: source/codegen/metadata/nirfmxinstr/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/functions.py`
- sha256: `7d6296d1e22c11f56a03ae1a440e67c74ff34c77ad608af61703ee0bdab5a107`
- bytes: 94144

````python
functions = {
    'BuildCalibrationPlaneString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'calibrationPlaneName',
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
    'BuildInstrumentString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'instrumentNumber',
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
    'BuildLOString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'loIndex',
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
    'BuildModuleString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'moduleName',
                'type': 'char[]'
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
    'BuildPortString': {
        'cname': 'RFmxInstr_BuildPortString2',
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'portName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'deviceName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
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
    'CfgExternalAttenuationInterpolationLinear': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'LinearInterpolationFormat',
                'name': 'format',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuationInterpolationNearest': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuationInterpolationSpline': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
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
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
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
    'CfgSParameterExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'frequencyArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sParameters',
                'size': {
                    'mechanism': 'len',
                    'value': 'sParameterTableSize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterTableSize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'SParameterOrientation',
                'name': 'sParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgSParameterExternalAttenuationTableInterleavedIQ': {
        'cname': 'RFmxInstr_CfgSParameterExternalAttenuationTable',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'frequencyArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sParameters',
                'size': {
                    'mechanism': 'len',
                    'value': 'sParameterTableSize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(sParameters)'
            },
            {
                'direction': 'in',
                'name': 'sParameterTableSize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'SParameterOrientation',
                'name': 'sParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgSParameterExternalAttenuationTableSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'frequencyArraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sParametersI',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'sParameterTableSize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'sParametersQ',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'sParameterTableSize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterTableSize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'SParameterOrientation',
                'name': 'sParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgSParameterExternalAttenuationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SParameterType',
                'name': 'sParameterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CheckAcquisitionStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'acquisitionDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CheckIfListExists': {
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
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'listExists',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'Personality',
                'name': 'personality',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CheckIfSignalConfigurationExists': {
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
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'signalConfigurationExists',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'Personality',
                'name': 'personality',
                'type': 'int32'
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
    'DeleteAllExternalAttenuationTables': {
        'parameters': [
            {
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
    'DeleteExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'DisableCalibrationPlane': {
        'parameters': [
            {
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
    'EnableCalibrationPlane': {
        'parameters': [
            {
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
    'ExportSignal': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'enum': 'ExportSignalSource',
                'name': 'exportSignalSource',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'OutputTerminal',
                'name': 'exportSignalOutputTerminal',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'FetchRawIQData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
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
                'name': 'recordsToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'int64'
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
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'void'
            }
        ],
        'returns': 'int32'
    },
    'FetchRawIQDataInterleavedIQ': {
        'cname': 'RFmxInstr_FetchRawIQData',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
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
                'name': 'recordsToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'int64'
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
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'void'
            }
        ],
        'returns': 'int32'
    },
    'FetchRawIQDataSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
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
                'name': 'recordsToFetch',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'int64'
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
            },
            {
                'direction': 'in',
                'hardcoded_value': 'nullptr',
                'include_in_proto': False,
                'name': 'reserved',
                'pointer': True,
                'type': 'void'
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
    'GetAvailablePaths': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'availablePaths',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAvailablePorts': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'availablePorts',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
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
    'GetExternalAttenuationTableActualValue': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'externalAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetListNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'Personality',
                'name': 'personalityFilter',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'listNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'listNamesSize',
                    'value_twist': 'actualListNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'listNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualListNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'Personality',
                'name': 'personality',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'personalityArraySize',
                    'value_twist': 'actualPersonalityArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'personalityArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualPersonalityArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetNIRFSASession': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'cross_driver_session': 'ViSession',
                'direction': 'out',
                'grpc_name': 'nirfsa_session',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'niRfsaSession',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetNIRFSASessionArray': {
        'codegen_method': 'CustomCode',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'cross_driver_session': 'ViSession',
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'nirfsaSessions',
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
    'GetSParameterExternalAttenuationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'SParameterType',
                'name': 'sParameterType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetSelfCalibrateLastDateAndTime': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalStep',
                'name': 'selfCalibrateStep',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 'timestamp',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'GetSelfCalibrateLastTemperature': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalStep',
                'name': 'selfCalibrateStep',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetSignalConfigurationNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'Personality',
                'name': 'personalityFilter',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'signalNamesSize',
                    'value_twist': 'actualSignalNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'signalNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualSignalNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'personality',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'personalityArraySize',
                    'value_twist': 'actualPersonalityArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'personalityArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualPersonalityArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'Initialize': {
        'custom_close': 'Close(id, RFMXINSTR_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXINSTR_VAL_FALSE)',
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
    'InitializeFromNIRFSASessionArray': {
        'custom_close': 'Close(id, RFMXINSTR_VAL_FALSE)',
        'init_method': True,
        'parameters': [
            {
                'cross_driver_session': 'ViSession',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'nirfsaSessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfNIRFSASessions'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfNIRFSASessions',
                'type': 'int32'
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
    'IsSelfCalibrateValid': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'selfCalibrateValid',
                'type': 'int32'
            },
            {
                'bitfield_as_enum_array': 'SelfCalStep',
                'direction': 'out',
                'name': 'validSteps',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadAllConfigurations': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'loadRFInstrConfiguration',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadConfigurations': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'LoadSParameterExternalAttenuationTableFromS2PFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_name': 's2p_file_path',
                'name': 's2PFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SParameterOrientation',
                'name': 'sParameterOrientation',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
                'name': 'attributeID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetDriver': {
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
    'ResetEntireSession': {
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
    'ResetToDefault': {
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
    'SaveAllConfigurations': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SelectActiveExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SelfCalibrate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalStep',
                'name': 'stepsToOmit',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SelfCalibrateRange': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalStep',
                'name': 'stepsToOmit',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'minimumFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'maximumFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'minimumReferenceLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'maximumReferenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SendSoftwareEdgeAdvanceTrigger': {
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
    'SendSoftwareEdgeStartTrigger': {
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxInstrAttribute',
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
    'TimestampFromValues': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'seconds_since_1970',
                'name': 'secondsSince1970',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'name': 'fractionalSeconds',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'timestamp',
                'type': 'CVIAbsoluteTime'
            }
        ],
        'returns': 'int32'
    },
    'ValuesFromTimestamp': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'timestamp',
                'type': 'CVIAbsoluteTime'
            },
            {
                'direction': 'out',
                'grpc_name': 'seconds_since_1970',
                'name': 'secondsSince1970',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 'fractionalSeconds',
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
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxinstr/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/attributes.py sha256=1ab47d472795c8110f0971d674cd366b799b84e1751230dbfcff51dace0c9fe7 bytes=17 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/attributes.py`
- sha256: `1ab47d472795c8110f0971d674cd366b799b84e1751230dbfcff51dace0c9fe7`
- bytes: 17

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/attributes_addon.py sha256=c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845 bytes=39 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/attributes_addon.py`
- sha256: `c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845`
- bytes: 39

````python
attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/config.py sha256=9cbf57334d9d68452bfc93de06de18d8514c4e305a7dd1557d7d1c2964910c68 bytes=1977 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/config.py`
- sha256: `9cbf57334d9d68452bfc93de06de18d8514c4e305a7dd1557d7d1c2964910c68`
- bytes: 1977

````python
# -*- coding: utf-8 -*-
config = {
    "code_readiness": "Release",
    "is_restricted": True,
    'api_version': '23.8.0',
    'c_header': 'niRFmxInstr.h',
    'c_function_prefix': 'RFmxInstr_',
    'service_class_prefix': 'NiRFmxInstrRestricted',
    'java_package': 'com.ni.grpc.nirfmxinstrrestricted',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxInstrRestricted',
    'namespace_component': 'nirfmxinstr_restricted',
    'close_function': None,
    'custom_types': [],
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
    'driver_name': 'NI-RFMXINSTR-RESTRICTED',
    "resource_handle_type": "niRFmxInstrHandle",
    'status_ok': 'status >= 0',
    "windows_only": True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxinstr',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxInstr.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxInstr.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxinstr_restricted',
    'session_class_description': 'An NI-RFmxInstr instrument handle.',
    'session_handle_parameter_name': 'instrument',
    "duplicate_resource_handles_allowed": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/enums.py sha256=b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc bytes=14 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/enums.py`
- sha256: `b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc`
- bytes: 14

````python
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/enums_addon.py sha256=2149957385bde3301473713f96ffe6fe7460abff296adc9beb38a209655aeefd bytes=34 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/enums_addon.py`
- sha256: `2149957385bde3301473713f96ffe6fe7460abff296adc9beb38a209655aeefd`
- bytes: 34

````python
enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/functions.py sha256=9e3ecdefc96235de9833ed7188752c20597221710ad64b47ca46c1f995bdae65 bytes=44570 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/functions.py`
- sha256: `9e3ecdefc96235de9833ed7188752c20597221710ad64b47ca46c1f995bdae65`
- bytes: 44570

````python
functions = {
    'ConvertForPowerUnitsUtility': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'referenceOrTriggerLevelIn',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'inputPowerUnits',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'outputPowerUnits',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'terminalConfiguration',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'bandwidth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceOrTriggerLevelOut',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'DeleteSnapshot': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'personality',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetActiveResultName': {
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
            },
            {
                'direction': 'in',
                'name': 'signalType',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'name': 'resultSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultName',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'resultSize',
                    'value_twist': 'actualResultSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'actualResultSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultState',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetActiveTableName': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'activeTableName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeAuthor': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
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
    'GetAttributeDesiredF32': {
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
    'GetAttributeDesiredF32Array': {
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
    'GetAttributeDesiredF64': {
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
    'GetAttributeDesiredF64Array': {
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
    'GetAttributeDesiredI32': {
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
    'GetAttributeDesiredI64': {
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
    'GetAttributeDesiredString': {
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
    'GetCalibrationPlaneEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'calibrationPlaneEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetCalibrationPlaneNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'calibrationPlaneNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
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
    'GetExternalAttenuationTableNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'externalAttenuationTableNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetForceAllTracesEnabled': {
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
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetInitiaitedSnapshotStrings': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'snapshotInfoCacheIndex',
                'type': 'uInt64'
            },
            {
                'direction': 'out',
                'name': 'personalityIDArray',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'personalityIDArraySize',
                    'value_twist': 'personalityIDArrayActualSize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'personalityIDArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'personalityIDArrayActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'signalNamesSize',
                    'value_twist': 'signalNamesActualSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'signalNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNamesActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'resultNamesSize',
                    'value_twist': 'resultNamesActualSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultNamesActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifiers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'snapshotIdentifiersSize',
                    'value_twist': 'snapshotIdentifiersActualSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'snapshotIdentifiersSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifiersActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotTimestampArray',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'snapshotTimestampArraySize',
                    'value_twist': 'snapshotTimestampArrayActualSize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'snapshotTimestampArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotTimestampArrayActualSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetLatestConfigurationSnapshot': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'snapshotInfoCacheIndex',
                'type': 'uInt64'
            },
            {
                'direction': 'out',
                'name': 'personalityID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalName',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'signalNameSize',
                    'value_twist': 'signalNameActualSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'signalNameSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNameActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifier',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'snapshotIdentifierSize',
                    'value_twist': 'snapshotIdentifierActualSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'snapshotIdentifierSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifierActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalConfigurationState',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalTimestamp',
                'type': 'uInt64'
            }
        ],
        'returns': 'int32'
    },
    'GetOpenSessionsInformation': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'infoJsonSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'infoJson',
                'size': {
                    'mechanism': 'ivi-dance',
                    'tags': [
                        'strlen-bug'
                    ],
                    'value': 'infoJsonSize'
                },
                'type': 'char[]'
            }            
        ],
        'returns': 'int32'
    },
    'GetPrivilegeLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'isConnectionAlive',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'privilegeLevel',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetRFmxVersion': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'grpc_name': 'version',
                'name': 'RFmxVersion',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetSessionUniqueIdentifier': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceNames',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sessionUniqueIdentifierSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'sessionUniqueIdentifier',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sessionUniqueIdentifierSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetSignalConfigurationState64': {
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
            },
            {
                'direction': 'in',
                'name': 'signalType',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'name': 'signalState',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'timeStamp',
                'type': 'uInt64'
            }
        ],
        'returns': 'int32'
    },
    'GetSnapshotInfoFromCache': {
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
                'name': 'snapshotInfoCacheIndex',
                'type': 'uInt64'
            },
            {
                'direction': 'out',
                'name': 'personalityIDArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'personalityIDArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'personalityIDArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'personalityIDArrayActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNames',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'signalNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'signalNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'signalNamesActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultNames',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'resultNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'resultNamesActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifiers',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'snapshotIdentifiersSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'snapshotIdentifiersSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotIdentifiersActualSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotTimestampArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'snapshotTimestampArraySize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'snapshotTimestampArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'snapshotTimestampArrayActualSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetSnapshotState': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'personality',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'snapshotState',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'GetTracesInfoForMonitorSnapshot': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'allTracesEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadAllForRevert': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'LoadConfigurationsFromJSON': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'jsonString',
                'type': 'char[]',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize',
                },
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RegisterSpecialClientSnapshotInterest': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RequestPrivilege': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'privilegeLevel',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'SaveAllForRevert': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SaveConfigurationsToJSON': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'signalNames',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'jsonStringOut',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetForceAllTracesEnabled': {
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
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetIOTraceStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'IOTraceStatus',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'UnregisterSpecialClientSnapshotInterest': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetSFPSessionAccessEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'isSFPSessionAccessEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateDefaultSignalConfiguration': {
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
            },
            {
                'direction': 'in',
                'name': 'personalityID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
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
    'DefineExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfPoints',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgSParameterExternalAttenuationTableFrequencies': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterFrequencies',
                'size': {
                    'mechanism': 'len',
                    'value': 'sParameterFrequenciesArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterFrequenciesArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgSParameterExternalAttenuationTableSParameter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sParameters',
                'size': {
                    'mechanism': 'len',
                    'value': 'sParameterTableSize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterTableSize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sParameterOrientation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'DefineSParameterExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfFrequencyPoints',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SaveExternalAttenuationTable': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'description',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuationTableFrequencies': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequency',
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
    'CfgExternalAttenuationTableLosses': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'tableName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
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
    'ReleaseLicense': {
        'parameters': [
            {
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
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxinstr_restricted/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxinstr_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxinstr_restricted/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/__init__.py sha256=9920240c02ae1184431703f37f87a58bae5e3b43309f9183292d0c3e1b8b6618 bytes=365 -->
## FILE: source/codegen/metadata/nirfmxlte/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/__init__.py`
- sha256: `9920240c02ae1184431703f37f87a58bae5e3b43309f9183292d0c3e1b8b6618`
- bytes: 365

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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/attributes.py sha256=a4ae467820a9e0268f2ff46b7d453552297488881616e74d82cd69493e95f381 bytes=60545 -->
## FILE: source/codegen/metadata/nirfmxlte/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/attributes.py`
- sha256: `a4ae467820a9e0268f2ff46b7d453552297488881616e74d82cd69493e95f381`
- bytes: 60545

````python
attributes = {
    3145729: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    3145730: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    3145731: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    3145732: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    3145733: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    3145734: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    3145735: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    3145736: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    3145737: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    3145738: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    3145739: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    3145740: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    3145741: {
        'access': 'read-write',
        'enum': 'DuplexScheme',
        'name': 'DUPLEX_SCHEME',
        'type': 'int32'
    },
    3145742: {
        'access': 'read-write',
        'enum': 'UplinkDownlinkConfiguration',
        'name': 'UPLINK_DOWNLINK_CONFIGURATION',
        'type': 'int32'
    },
    3145743: {
        'access': 'read-write',
        'name': 'NUMBER_OF_COMPONENT_CARRIERS',
        'type': 'int32'
    },
    3145744: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_BANDWIDTH',
        'type': 'float64'
    },
    3145745: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_FREQUENCY',
        'type': 'float64'
    },
    3145746: {
        'access': 'read-write',
        'name': 'CELL_ID',
        'type': 'int32'
    },
    3145747: {
        'access': 'read-write',
        'enum': 'ComponentCarrierSpacingType',
        'name': 'COMPONENT_CARRIER_SPACING_TYPE',
        'type': 'int32'
    },
    3145748: {
        'access': 'read-write',
        'name': 'COMPONENT_CARRIER_AT_CENTER_FREQUENCY',
        'type': 'int32'
    },
    3145749: {
        'access': 'read-write',
        'enum': 'CyclicPrefixMode',
        'name': 'CYCLIC_PREFIX_MODE',
        'type': 'int32'
    },
    3145751: {
        'access': 'read-write',
        'name': 'BAND',
        'type': 'int32'
    },
    3145753: {
        'access': 'read-write',
        'enum': 'UplinkGroupHoppingEnabled',
        'name': 'UPLINK_GROUP_HOPPING_ENABLED',
        'type': 'int32'
    },
    3145754: {
        'access': 'read-write',
        'enum': 'UplinkSequenceHoppingEnabled',
        'name': 'UPLINK_SEQUENCE_HOPPING_ENABLED',
        'type': 'int32'
    },
    3145755: {
        'access': 'read-write',
        'enum': 'PuschModulationType',
        'name': 'PUSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    3145756: {
        'access': 'read-write',
        'name': 'PUSCH_NUMBER_OF_RESOURCE_BLOCK_CLUSTERS',
        'type': 'int32'
    },
    3145758: {
        'access': 'read-write',
        'name': 'PUSCH_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    3145759: {
        'access': 'read-write',
        'name': 'PUSCH_N_DMRS_1',
        'type': 'int32'
    },
    3145760: {
        'access': 'read-write',
        'name': 'PUSCH_N_DMRS_2',
        'type': 'int32'
    },
    3145761: {
        'access': 'read-write',
        'name': 'PUSCH_DELTA_SEQUENCE_SHIFT',
        'type': 'int32'
    },
    3145762: {
        'access': 'read-write',
        'name': 'PUSCH_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    3145763: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SUBBLOCKS',
        'type': 'int32'
    },
    3145766: {
        'access': 'read-write',
        'enum': 'AutoResourceBlockDetectionEnabled',
        'name': 'AUTO_RESOURCE_BLOCK_DETECTION_ENABLED',
        'type': 'int32'
    },
    3145767: {
        'access': 'read-write',
        'name': 'PUSCH_POWER',
        'type': 'float64'
    },
    3145768: {
        'access': 'read-write',
        'enum': 'AutoDmrsDetectionEnabled',
        'name': 'AUTO_DMRS_DETECTION_ENABLED',
        'type': 'int32'
    },
    3145769: {
        'access': 'read-write',
        'enum': 'LinkDirection',
        'name': 'LINK_DIRECTION',
        'type': 'int32'
    },
    3145770: {
        'access': 'read-write',
        'name': 'SPECIAL_SUBFRAME_CONFIGURATION',
        'type': 'int32'
    },
    3145771: {
        'access': 'read-write',
        'name': 'NUMBER_OF_DUT_ANTENNAS',
        'type': 'int32'
    },
    3145772: {
        'access': 'read-write',
        'name': 'TRANSMIT_ANTENNA_TO_ANALYZE',
        'type': 'int32'
    },
    3145773: {
        'access': 'read-write',
        'enum': 'SrsEnabled',
        'name': 'SRS_ENABLED',
        'type': 'int32'
    },
    3145774: {
        'access': 'read-write',
        'name': 'SRS_SUBFRAME_CONFIGURATION',
        'type': 'int32'
    },
    3145775: {
        'access': 'read-write',
        'name': 'SRS_C_SRS',
        'type': 'int32'
    },
    3145776: {
        'access': 'read-write',
        'name': 'SRS_B_SRS',
        'type': 'int32'
    },
    3145777: {
        'access': 'read-write',
        'name': 'SRS_I_SRS',
        'type': 'int32'
    },
    3145778: {
        'access': 'read-write',
        'name': 'SRS_N_RRC',
        'type': 'int32'
    },
    3145779: {
        'access': 'read-write',
        'name': 'SRS_N_SRS_CS',
        'type': 'int32'
    },
    3145780: {
        'access': 'read-write',
        'name': 'SRS_B_HOP',
        'type': 'int32'
    },
    3145781: {
        'access': 'read-write',
        'name': 'SRS_K_TC',
        'type': 'int32'
    },
    3145782: {
        'access': 'read-write',
        'enum': 'SrsMaximumUpPtsEnabled',
        'name': 'SRS_MAXIMUM_UP_PTS_ENABLED',
        'type': 'int32'
    },
    3145783: {
        'access': 'read-write',
        'name': 'SRS_SUBFRAME1_N_RA',
        'type': 'int32'
    },
    3145784: {
        'access': 'read-write',
        'name': 'SRS_SUBFRAME6_N_RA',
        'type': 'int32'
    },
    3145785: {
        'access': 'read-write',
        'name': 'SRS_POWER',
        'type': 'float64'
    },
    3145788: {
        'access': 'read-write',
        'enum': 'DownlinkAutoCellIDDetectionEnabled',
        'name': 'DOWNLINK_AUTO_CELL_ID_DETECTION_ENABLED',
        'type': 'int32'
    },
    3145789: {
        'access': 'read-write',
        'enum': 'DownlinkChannelConfigurationMode',
        'name': 'DOWNLINK_CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    3145790: {
        'access': 'read-write',
        'enum': 'DownlinkUserDefinedRatio',
        'name': 'DOWNLINK_USER_DEFINED_CELL_SPECIFIC_RATIO',
        'type': 'int32'
    },
    3145791: {
        'access': 'read-write',
        'name': 'PSS_POWER',
        'type': 'float64'
    },
    3145792: {
        'access': 'read-write',
        'name': 'SSS_POWER',
        'type': 'float64'
    },
    3145793: {
        'access': 'read-write',
        'name': 'PBCH_POWER',
        'type': 'float64'
    },
    3145794: {
        'access': 'read-write',
        'name': 'PDCCH_POWER',
        'type': 'float64'
    },
    3145795: {
        'access': 'read-write',
        'name': 'DOWNLINK_NUMBER_OF_SUBFRAMES',
        'type': 'int32'
    },
    3145796: {
        'access': 'read-write',
        'name': 'PCFICH_CFI',
        'type': 'int32'
    },
    3145797: {
        'access': 'read-write',
        'name': 'PCFICH_POWER',
        'type': 'float64'
    },
    3145798: {
        'access': 'read-write',
        'enum': 'DownlinkUserDefinedPhichResource',
        'name': 'PHICH_RESOURCE',
        'type': 'int32'
    },
    3145799: {
        'access': 'read-write',
        'enum': 'DownlinkUserDefinedPhichDuration',
        'name': 'PHICH_DURATION',
        'type': 'int32'
    },
    3145800: {
        'access': 'read-write',
        'name': 'PHICH_POWER',
        'type': 'float64'
    },
    3145801: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PDSCH_CHANNELS',
        'type': 'int32'
    },
    3145802: {
        'access': 'read-write',
        'enum': 'UserDefinedPdschCW0ModulationType',
        'name': 'PDSCH_CW0_MODULATION_TYPE',
        'type': 'int32'
    },
    3145803: {
        'access': 'read-write',
        'name': 'PDSCH_RESOURCE_BLOCK_ALLOCATION',
        'type': 'char[]'
    },
    3145804: {
        'access': 'read-write',
        'name': 'PDSCH_POWER',
        'type': 'float64'
    },
    3145805: {
        'access': 'read-write',
        'enum': 'DownlinkTestModel',
        'name': 'DOWNLINK_TEST_MODEL',
        'type': 'int32'
    },
    3145808: {
        'access': 'read-write',
        'enum': 'ENodeBCategory',
        'name': 'ENODEB_CATEGORY',
        'type': 'int32'
    },
    3145809: {
        'access': 'read-write',
        'enum': 'DmrsOccEnabled',
        'name': 'DMRS_OCC_ENABLED',
        'type': 'int32'
    },
    3145810: {
        'access': 'read-write',
        'name': 'PUSCH_CYCLIC_SHIFT_FIELD',
        'type': 'int32'
    },
    3145811: {
        'access': 'read-write',
        'enum': 'MiConfiguration',
        'name': 'MI_CONFIGURATION',
        'type': 'int32'
    },
    3145813: {
        'access': 'read-write',
        'enum': 'PsschModulationType',
        'name': 'PSSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    3145814: {
        'access': 'read-write',
        'name': 'PSSCH_RESOURCE_BLOCK_OFFSET',
        'type': 'int32'
    },
    3145815: {
        'access': 'read-write',
        'name': 'PSSCH_NUMBER_OF_RESOURCE_BLOCKS',
        'type': 'int32'
    },
    3145816: {
        'access': 'read-write',
        'name': 'PSSCH_POWER',
        'type': 'float64'
    },
    3145817: {
        'access': 'read-write',
        'name': 'SUBBLOCK_FREQUENCY',
        'type': 'float64'
    },
    3149814: {
        'access': 'read-write',
        'enum': 'ListStepTimerUnit',
        'name': 'LIST_STEP_TIMER_UNIT',
        'type': 'int32'
    },
    3149815: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_OFFSET',
        'type': 'float64'
    },
    3149816: {
        'access': 'read-write',
        'name': 'NUMBER_OF_STEPS',
        'type': 'int32'
    },
    3149817: {
        'access': 'read-write',
        'name': 'LIST_STEP_TIMER_DURATION',
        'type': 'float64'
    },
    3149820: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    3149821: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    3149823: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    3149824: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3149829: {
        'access': 'read-write',
        'name': 'ACP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3149834: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    3149838: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3149842: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    3149843: {
        'access': 'read-write',
        'enum': 'AcpPowerUnits',
        'name': 'ACP_POWER_UNITS',
        'type': 'int32'
    },
    3149844: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3149845: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    3149846: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3149848: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    3149851: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    3149852: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    3149853: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    3149854: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    3149855: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    3149856: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    3149857: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3149858: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    3149862: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3149863: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    3149868: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3149869: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    3149874: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3149875: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    3149876: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    3149877: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    3149878: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    3149879: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3149880: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    3149881: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_SUBBLOCK_CENTER_FREQUENCY',
        'type': 'float64'
    },
    3149882: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_UTRA_OFFSETS',
        'type': 'int32'
    },
    3149883: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_EUTRA_OFFSETS',
        'type': 'int32'
    },
    3149887: {
        'access': 'read-write',
        'name': 'ACP_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3149888: {
        'access': 'read-write',
        'enum': 'AcpAmplitudeCorrectionType',
        'name': 'ACP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    3149889: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    3149890: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_GSM_OFFSETS',
        'type': 'int32'
    },
    3149891: {
        'access': 'read-write',
        'enum': 'AcpEutraOffsetDefinition',
        'name': 'ACP_EUTRA_OFFSET_DEFINITION',
        'type': 'int32'
    },
    3149892: {
        'access': 'read-write',
        'enum': 'AcpConfigurableNumberOfOffsetsEnabled',
        'name': 'ACP_CONFIGURABLE_NUMBER_OF_OFFSETS_ENABLED',
        'type': 'int32'
    },
    3149893: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    3149894: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    3149895: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMode',
        'name': 'ACP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    3149896: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationType',
        'name': 'ACP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    3149897: {
        'access': 'read-write',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    3149898: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationAveragingAuto',
        'name': 'ACP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    3149899: {
        'access': 'read-write',
        'enum': 'AcpNoiseCalibrationMode',
        'name': 'ACP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    3149904: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_STANDALONE_NB_IOT_OFFSETS',
        'type': 'int32'
    },
    3158016: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3158018: {
        'access': 'read-write',
        'name': 'CHP_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3158019: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3158022: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    3158023: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3158025: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    3158028: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    3158029: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    3158030: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    3158033: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    3158034: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    3158036: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3158037: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_COMPONENT_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3158040: {
        'access': 'read-write',
        'enum': 'ChpIntegrationBandwidthType',
        'name': 'CHP_INTEGRATION_BANDWIDTH_TYPE',
        'type': 'int32'
    },
    3158041: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    3158043: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_SUBBLOCK_FREQUENCY',
        'type': 'float64'
    },
    3158044: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3158045: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    3158048: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_COMPONENT_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    3158050: {
        'access': 'read-write',
        'name': 'CHP_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3158051: {
        'access': 'read-write',
        'enum': 'ChpAmplitudeCorrectionType',
        'name': 'CHP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    3158052: {
        'access': 'read-write',
        'enum': 'ChpMeasurementMode',
        'name': 'CHP_MEASUREMENT_MODE',
        'type': 'int32'
    },
    3158053: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationEnabled',
        'name': 'CHP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    3158054: {
        'access': 'read-write',
        'enum': 'ChpNoiseCompensationType',
        'name': 'CHP_NOISE_COMPENSATION_TYPE',
        'type': 'int32'
    },
    3158055: {
        'access': 'read-write',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_COUNT',
        'type': 'int32'
    },
    3158056: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationAveragingAuto',
        'name': 'CHP_NOISE_CALIBRATION_AVERAGING_AUTO',
        'type': 'int32'
    },
    3158057: {
        'access': 'read-write',
        'enum': 'ChpNoiseCalibrationMode',
        'name': 'CHP_NOISE_CALIBRATION_MODE',
        'type': 'int32'
    },
    3162112: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3162114: {
        'access': 'read-write',
        'enum': 'ModAccMulticarrierFilterEnabled',
        'name': 'MODACC_MULTICARRIER_FILTER_ENABLED',
        'type': 'int32'
    },
    3162115: {
        'access': 'read-write',
        'enum': 'ModAccSynchronizationMode',
        'name': 'MODACC_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    3162116: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    3162117: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    3162118: {
        'access': 'read-write',
        'enum': 'ModAccEvmUnit',
        'name': 'MODACC_EVM_UNIT',
        'type': 'int32'
    },
    3162119: {
        'access': 'read-write',
        'name': 'MODACC_FFT_WINDOW_OFFSET',
        'type': 'float64'
    },
    3162120: {
        'access': 'read-write',
        'enum': 'ModAccSpectralFlatnessCondition',
        'name': 'MODACC_SPECTRAL_FLATNESS_CONDITION',
        'type': 'int32'
    },
    3162121: {
        'access': 'read-write',
        'enum': 'ModAccCommonClockSourceEnabled',
        'name': 'MODACC_COMMON_CLOCK_SOURCE_ENABLED',
        'type': 'int32'
    },
    3162122: {
        'access': 'read-write',
        'enum': 'ModAccAveragingEnabled',
        'name': 'MODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3162123: {
        'access': 'read-write',
        'name': 'MODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    3162125: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3162126: {
        'access': 'read-write',
        'name': 'MODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3162127: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_COMPOSITE_EVM',
        'type': 'float64'
    },
    3162128: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_EVM',
        'type': 'float64'
    },
    3162131: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_COMPOSITE_EVM_SLOT_INDEX',
        'type': 'int32'
    },
    3162132: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_COMPOSITE_EVM_SYMBOL_INDEX',
        'type': 'int32'
    },
    3162133: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_COMPOSITE_EVM_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    3162134: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MEAN_RMS_DATA_EVM',
        'type': 'float64'
    },
    3162135: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MAXIMUM_PEAK_DATA_EVM',
        'type': 'float64'
    },
    3162136: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MEAN_RMS_DMRS_EVM',
        'type': 'float64'
    },
    3162137: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MAXIMUM_PEAK_DMRS_EVM',
        'type': 'float64'
    },
    3162138: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MEAN_DATA_POWER',
        'type': 'float64'
    },
    3162139: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PUSCH_MEAN_DMRS_POWER',
        'type': 'float64'
    },
    3162146: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_FREQUENCY_ERROR',
        'type': 'float64'
    },
    3162147: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    3162148: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    3162149: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_QUADRATURE_ERROR',
        'type': 'float64'
    },
    3162150: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_IQ_TIMING_SKEW',
        'type': 'float64'
    },
    3162151: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_TIME_OFFSET',
        'type': 'float64'
    },
    3162152: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_SYMBOL_CLOCK_ERROR',
        'type': 'float64'
    },
    3162155: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IN_BAND_EMISSION_MARGIN',
        'type': 'float64'
    },
    3162156: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE1_MINIMUM',
        'type': 'float64'
    },
    3162157: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE2_MINIMUM',
        'type': 'float64'
    },
    3162158: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE1_MAXIMUM_TO_RANGE2_MINIMUM',
        'type': 'float64'
    },
    3162159: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SPECTRAL_FLATNESS_RANGE2_MAXIMUM_TO_RANGE1_MINIMUM',
        'type': 'float64'
    },
    3162160: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    3162162: {
        'access': 'read-write',
        'enum': 'ModAccEvmWithExclusionPeriodEnabled',
        'name': 'MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED',
        'type': 'int32'
    },
    3162166: {
        'access': 'read-write',
        'enum': 'ModAccSpectrumInverted',
        'name': 'MODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    3162167: {
        'access': 'read-write',
        'enum': 'ModAccChannelEstimationType',
        'name': 'MODACC_CHANNEL_ESTIMATION_TYPE',
        'type': 'int32'
    },
    3162168: {
        'access': 'read-write',
        'enum': 'ModAccFftWindowType',
        'name': 'MODACC_FFT_WINDOW_TYPE',
        'type': 'int32'
    },
    3162169: {
        'access': 'read-write',
        'name': 'MODACC_FFT_WINDOW_LENGTH',
        'type': 'float64'
    },
    3162170: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_COMPOSITE_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    3162171: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    3162172: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_COMPOSITE_PHASE_ERROR',
        'type': 'float64'
    },
    3162173: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_COMPOSITE_PHASE_ERROR',
        'type': 'float64'
    },
    3162174: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_IN_BAND_EMISSION_MARGIN',
        'type': 'float64'
    },
    3162175: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    3162176: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_MEAN_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    3162177: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SUBBLOCK_MEAN_QUADRATURE_ERROR',
        'type': 'float64'
    },
    3162178: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_SRS_EVM',
        'type': 'float64'
    },
    3162179: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_SRS_POWER',
        'type': 'float64'
    },
    3162180: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_EVM',
        'type': 'float64'
    },
    3162181: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_QPSK_EVM',
        'type': 'float64'
    },
    3162182: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_16QAM_EVM',
        'type': 'float64'
    },
    3162183: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_64QAM_EVM',
        'type': 'float64'
    },
    3162184: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_256QAM_EVM',
        'type': 'float64'
    },
    3162185: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_CSRS_EVM',
        'type': 'float64'
    },
    3162186: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_PSS_EVM',
        'type': 'float64'
    },
    3162187: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_SSS_EVM',
        'type': 'float64'
    },
    3162188: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_PBCH_EVM',
        'type': 'float64'
    },
    3162189: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_PCFICH_EVM',
        'type': 'float64'
    },
    3162190: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_PDCCH_EVM',
        'type': 'float64'
    },
    3162191: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_PHICH_EVM',
        'type': 'float64'
    },
    3162193: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DOWNLINK_RS_TRANSMIT_POWER',
        'type': 'float64'
    },
    3162194: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DOWNLINK_OFDM_SYMBOL_TRANSMIT_POWER',
        'type': 'float64'
    },
    3162195: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DOWNLINK_DETECTED_CELL_ID',
        'type': 'int32'
    },
    3162196: {
        'access': 'read-write',
        'enum': 'AutoPdschChannelDetectionEnabled',
        'name': 'AUTO_PDSCH_CHANNEL_DETECTION_ENABLED',
        'type': 'int32'
    },
    3162197: {
        'access': 'read-write',
        'enum': 'AutoControlChannelPowerDetectionEnabled',
        'name': 'AUTO_CONTROL_CHANNEL_POWER_DETECTION_ENABLED',
        'type': 'int32'
    },
    3162198: {
        'access': 'read-write',
        'enum': 'AutoPcfichCfiDetectionEnabled',
        'name': 'AUTO_PCFICH_CFI_DETECTION_ENABLED',
        'type': 'int32'
    },
    3162199: {
        'access': 'read-write',
        'name': 'LAA_STARTING_SUBFRAME',
        'type': 'int32'
    },
    3162200: {
        'access': 'read-write',
        'name': 'LAA_NUMBER_OF_SUBFRAMES',
        'type': 'int32'
    },
    3162201: {
        'access': 'read-write',
        'enum': 'LaaUplinkStartPosition',
        'name': 'LAA_UPLINK_START_POSITION',
        'type': 'int32'
    },
    3162202: {
        'access': 'read-write',
        'enum': 'LaaUplinkEndingSymbol',
        'name': 'LAA_UPLINK_ENDING_SYMBOL',
        'type': 'int32'
    },
    3162203: {
        'access': 'read-write',
        'enum': 'LaaDownlinkStartingSymbol',
        'name': 'LAA_DOWNLINK_STARTING_SYMBOL',
        'type': 'int32'
    },
    3162204: {
        'access': 'read-write',
        'enum': 'LaaDownlinkNumberOfEndingSymbols',
        'name': 'LAA_DOWNLINK_NUMBER_OF_ENDING_SYMBOLS',
        'type': 'int32'
    },
    3162205: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PDSCH_MEAN_RMS_1024QAM_EVM',
        'type': 'float64'
    },
    3162206: {
        'access': 'read-write',
        'name': 'NCELL_ID',
        'type': 'int32'
    },
    3162207: {
        'access': 'read-write',
        'enum': 'NBIoTUplinkSubcarrierSpacing',
        'name': 'NB_IOT_UPLINK_SUBCARRIER_SPACING',
        'type': 'int32'
    },
    3162208: {
        'access': 'read-write',
        'enum': 'AutoNPuschChannelDetectionEnabled',
        'name': 'AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED',
        'type': 'int32'
    },
    3162209: {
        'access': 'read-write',
        'name': 'NPUSCH_FORMAT',
        'type': 'int32'
    },
    3162210: {
        'access': 'read-write',
        'name': 'NPUSCH_TONE_OFFSET',
        'type': 'int32'
    },
    3162211: {
        'access': 'read-write',
        'name': 'NPUSCH_NUMBER_OF_TONES',
        'type': 'int32'
    },
    3162212: {
        'access': 'read-write',
        'enum': 'NPuschModulationType',
        'name': 'NPUSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    3162213: {
        'access': 'read-write',
        'enum': 'NPuschDmrsBaseSequenceMode',
        'name': 'NPUSCH_DMRS_BASE_SEQUENCE_MODE',
        'type': 'int32'
    },
    3162214: {
        'access': 'read-write',
        'name': 'NPUSCH_DMRS_BASE_SEQUENCE_INDEX',
        'type': 'int32'
    },
    3162215: {
        'access': 'read-write',
        'name': 'NPUSCH_DMRS_CYCLIC_SHIFT',
        'type': 'int32'
    },
    3162216: {
        'access': 'read-write',
        'name': 'NPUSCH_DMRS_DELTA_SEQUENCE_SHIFT',
        'type': 'int32'
    },
    3162217: {
        'access': 'read-write',
        'enum': 'NPuschDmrsGroupHoppingEnabled',
        'name': 'NPUSCH_DMRS_GROUP_HOPPING_ENABLED',
        'type': 'int32'
    },
    3162218: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MEAN_RMS_DATA_EVM',
        'type': 'float64'
    },
    3162219: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DATA_EVM',
        'type': 'float64'
    },
    3162220: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MEAN_RMS_DMRS_EVM',
        'type': 'float64'
    },
    3162221: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MAXIMUM_PEAK_DMRS_EVM',
        'type': 'float64'
    },
    3162222: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MEAN_DATA_POWER',
        'type': 'float64'
    },
    3162223: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPUSCH_MEAN_DMRS_POWER',
        'type': 'float64'
    },
    3162224: {
        'access': 'read-write',
        'enum': 'EmtcAnalysisEnabled',
        'name': 'EMTC_ANALYSIS_ENABLED',
        'type': 'int32'
    },
    3162225: {
        'access': 'read-write',
        'enum': 'ModAccInBandEmissionMaskType',
        'name': 'MODACC_IN_BAND_EMISSION_MASK_TYPE',
        'type': 'int32'
    },
    3162226: {
        'access': 'read-write',
        'name': 'NPUSCH_STARTING_SLOT',
        'type': 'int32'
    },
    3162227: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MEAN_RMS_DATA_EVM',
        'type': 'float64'
    },
    3162228: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MAXIMUM_PEAK_DATA_EVM',
        'type': 'float64'
    },
    3162229: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MEAN_RMS_DMRS_EVM',
        'type': 'float64'
    },
    3162230: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MAXIMUM_PEAK_DMRS_EVM',
        'type': 'float64'
    },
    3162231: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MEAN_DATA_POWER',
        'type': 'float64'
    },
    3162232: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSSCH_MEAN_DMRS_POWER',
        'type': 'float64'
    },
    3162233: {
        'access': 'read-write',
        'enum': 'ModAccIQOriginOffsetEstimationEnabled',
        'name': 'MODACC_IQ_ORIGIN_OFFSET_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    3162234: {
        'access': 'read-write',
        'enum': 'ModAccIQMismatchEstimationsEnabled',
        'name': 'MODACC_IQ_MISMATCH_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    3162235: {
        'access': 'read-write',
        'enum': 'ModAccIQGainImbalanceCorrectionEnabled',
        'name': 'MODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED',
        'type': 'int32'
    },
    3162236: {
        'access': 'read-write',
        'enum': 'ModAccIQQuadratureErrorCorrectionEnabled',
        'name': 'MODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    3162237: {
        'access': 'read-write',
        'enum': 'ModAccIQTimingSkewCorrectionEnabled',
        'name': 'MODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED',
        'type': 'int32'
    },
    3162238: {
        'access': 'read-write',
        'enum': 'ModAccMulticarrierTimeSynchronizationMode',
        'name': 'MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    3162239: {
        'access': 'read-write',
        'enum': 'ModAccPreFftErrorEstimationInterval',
        'name': 'MODACC_PRE_FFT_ERROR_ESTIMATION_INTERVAL',
        'type': 'int32'
    },
    3162240: {
        'access': 'read-write',
        'enum': 'ModAccSymbolClockErrorEstimationEnabled',
        'name': 'MODACC_SYMBOL_CLOCK_ERROR_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    3162241: {
        'access': 'read-write',
        'enum': 'ModAccTimingTrackingEnabled',
        'name': 'MODACC_TIMING_TRACKING_ENABLED',
        'type': 'int32'
    },
    3162242: {
        'access': 'read-write',
        'enum': 'ModAccPhaseTrackingEnabled',
        'name': 'MODACC_PHASE_TRACKING_ENABLED',
        'type': 'int32'
    },
    3162243: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_FREQUENCY_ERROR',
        'type': 'float64'
    },
    3162244: {
        'access': 'read-write',
        'enum': 'NBIoTDownlinkChannelConfigurationMode',
        'name': 'NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    3162247: {
        'access': 'read-write',
        'name': 'NPSS_POWER',
        'type': 'float64'
    },
    3162249: {
        'access': 'read-write',
        'name': 'NSSS_POWER',
        'type': 'float64'
    },
    3162250: {
        'access': 'read-write',
        'name': 'NPDSCH_POWER',
        'type': 'float64'
    },
    3162251: {
        'access': 'read-write',
        'enum': 'NpdschEnabled',
        'name': 'NPDSCH_ENABLED',
        'type': 'int32'
    },
    3162252: {
        'access': 'read-write',
        'enum': 'NpdschModulationType',
        'name': 'NPDSCH_MODULATION_TYPE',
        'type': 'int32'
    },
    3162254: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_NPSS_EVM',
        'type': 'float64'
    },
    3162255: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_NSSS_EVM',
        'type': 'float64'
    },
    3162256: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPDSCH_MEAN_RMS_EVM',
        'type': 'float64'
    },
    3162257: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPDSCH_MEAN_RMS_QPSK_EVM',
        'type': 'float64'
    },
    3162258: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NPDSCH_MEAN_RMS_16QAM_EVM',
        'type': 'float64'
    },
    3162259: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MEAN_RMS_NRS_EVM',
        'type': 'float64'
    },
    3162260: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DOWNLINK_NRS_TRANSMIT_POWER',
        'type': 'float64'
    },
    3170304: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3170307: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3170308: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    3170310: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    3170311: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3170313: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    3170316: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    3170317: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    3170318: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    3170319: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    3170320: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    3170322: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3170323: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    3170324: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3170325: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    3170326: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    3170331: {
        'access': 'read-write',
        'enum': 'ObwAmplitudeCorrectionType',
        'name': 'OBW_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    3178496: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3178501: {
        'access': 'read-write',
        'name': 'SEM_COMPONENT_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3178507: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    3178508: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    3178509: {
        'access': 'read-write',
        'enum': 'SemOffsetLimitFailMask',
        'name': 'SEM_OFFSET_LIMIT_FAIL_MASK',
        'type': 'int32'
    },
    3178512: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_START',
        'type': 'float64'
    },
    3178513: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_ABSOLUTE_LIMIT_STOP',
        'type': 'float64'
    },
    3178515: {
        'access': 'read-write',
        'enum': 'SemOffsetSideband',
        'name': 'SEM_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    3178516: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    3178517: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    3178519: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    3178520: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    3178522: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_START',
        'type': 'float64'
    },
    3178523: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_STOP',
        'type': 'float64'
    },
    3178525: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3178526: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    3178527: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3178529: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    3178533: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    3178534: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    3178535: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3178536: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_TOTAL_AGGREGATED_POWER',
        'type': 'float64'
    },
    3178537: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    3178541: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178542: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178543: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    3178544: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_COMPONENT_CARRIER_PEAK_FREQUENCY',
        'type': 'float64'
    },
    3178548: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178549: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178550: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    3178551: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    3178552: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    3178553: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    3178554: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3178555: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    3178556: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    3178557: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    3178561: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178562: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    3178563: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    3178564: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    3178565: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    3178566: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    3178567: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    3178568: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    3178569: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    3178570: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    3178572: {
        'access': 'read-write',
        'enum': 'SemUplinkMaskType',
        'name': 'SEM_UPLINK_MASK_TYPE',
        'type': 'int32'
    },
    3178573: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_SUBBLOCK_CENTER_FREQUENCY',
        'type': 'float64'
    },
    3178574: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3178575: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_SUBBLOCK_POWER',
        'type': 'float64'
    },
    3178577: {
        'access': 'read-write',
        'name': 'SEM_SUBBLOCK_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    3178578: {
        'access': 'read-write',
        'name': 'SEM_SUBBLOCK_AGGREGATED_CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    3178579: {
        'access': 'read-write',
        'enum': 'SemDownlinkMaskType',
        'name': 'SEM_DOWNLINK_MASK_TYPE',
        'type': 'int32'
    },
    3178580: {
        'access': 'read-write',
        'name': 'SEM_DELTA_F_MAXIMUM',
        'type': 'float64'
    },
    3178581: {
        'access': 'read-write',
        'name': 'SEM_AGGREGATED_MAXIMUM_POWER',
        'type': 'float64'
    },
    3178582: {
        'access': 'read-write',
        'name': 'SEM_COMPONENT_CARRIER_MAXIMUM_OUTPUT_POWER',
        'type': 'float64'
    },
    3178583: {
        'access': 'read-write',
        'enum': 'SemAmplitudeCorrectionType',
        'name': 'SEM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    3178584: {
        'access': 'read-write',
        'enum': 'SemSidelinkMaskType',
        'name': 'SEM_SIDELINK_MASK_TYPE',
        'type': 'int32'
    },
    3178585: {
        'access': 'read-write',
        'enum': 'SemComponentCarrierOutputPowerType',
        'name': 'SEM_COMPONENT_CARRIER_OUTPUT_POWER_TYPE',
        'type': 'int32'
    },
    3182592: {
        'access': 'read-write',
        'name': 'PVT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3182594: {
        'access': 'read-write',
        'enum': 'PvtMeasurementMethod',
        'name': 'PVT_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    3182599: {
        'access': 'read-write',
        'enum': 'PvtAveragingEnabled',
        'name': 'PVT_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3182601: {
        'access': 'read-write',
        'name': 'PVT_AVERAGING_COUNT',
        'type': 'int32'
    },
    3182602: {
        'access': 'read-write',
        'enum': 'PvtAveragingType',
        'name': 'PVT_AVERAGING_TYPE',
        'type': 'int32'
    },
    3182603: {
        'access': 'read-write',
        'name': 'PVT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3182604: {
        'access': 'read-write',
        'name': 'PVT_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3182606: {
        'access': 'read-write',
        'enum': 'PvtMeasurementStatus',
        'name': 'PVT_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    3182608: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_BEFORE',
        'type': 'float64'
    },
    3182609: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER_AFTER',
        'type': 'float64'
    },
    3182610: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER',
        'type': 'float64'
    },
    3182612: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_BURST_WIDTH',
        'type': 'float64'
    },
    3182613: {
        'access': 'read-write',
        'name': 'PVT_OFF_POWER_EXCLUSION_BEFORE',
        'type': 'float64'
    },
    3182614: {
        'access': 'read-write',
        'name': 'PVT_OFF_POWER_EXCLUSION_AFTER',
        'type': 'float64'
    },
    3186688: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3186690: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    3186691: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    3186694: {
        'access': 'read-write',
        'enum': 'SlotPhaseSynchronizationMode',
        'name': 'SLOTPHASE_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    3186695: {
        'access': 'read-write',
        'enum': 'SlotPhaseExclusionPeriodEnabled',
        'name': 'SLOTPHASE_EXCLUSION_PERIOD_ENABLED',
        'type': 'int32'
    },
    3186696: {
        'access': 'read-write',
        'enum': 'SlotPhaseCommonClockSourceEnabled',
        'name': 'SLOTPHASE_COMMON_CLOCK_SOURCE_ENABLED',
        'type': 'int32'
    },
    3186697: {
        'access': 'read-write',
        'enum': 'SlotPhaseSpectrumInverted',
        'name': 'SLOTPHASE_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    3186699: {
        'access': 'read-write',
        'name': 'SLOTPHASE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3186708: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY',
        'type': 'float64'
    },
    3190784: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3190786: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    3190787: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    3190789: {
        'access': 'read-write',
        'enum': 'SlotPowerCommonClockSourceEnabled',
        'name': 'SLOTPOWER_COMMON_CLOCK_SOURCE_ENABLED',
        'type': 'int32'
    },
    3190790: {
        'access': 'read-write',
        'enum': 'SlotPowerSpectrumInverted',
        'name': 'SLOTPOWER_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    3190794: {
        'access': 'read-write',
        'name': 'SLOTPOWER_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3194880: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    3198976: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    3198977: {
        'access': 'read-write',
        'enum': 'AcquisitionBandwidthOptimizationEnabled',
        'name': 'ACQUISITION_BANDWIDTH_OPTIMIZATION_ENABLED',
        'type': 'int32'
    },
    3198978: {
        'access': 'read-write',
        'enum': 'TransmitterArchitecture',
        'name': 'TRANSMITTER_ARCHITECTURE',
        'type': 'int32'
    },
    3198979: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    3198980: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY_FOR_LIMITS',
        'type': 'float64'
    },
    3203072: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    3203074: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_OFFSET',
        'type': 'float64'
    },
    3203075: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    3203076: {
        'access': 'read-write',
        'enum': 'TxpAveragingEnabled',
        'name': 'TXP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    3203077: {
        'access': 'read-write',
        'name': 'TXP_AVERAGING_COUNT',
        'type': 'int32'
    },
    3203079: {
        'access': 'read-write',
        'name': 'TXP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    3203080: {
        'access': 'read-write',
        'name': 'TXP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    3203082: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    3203083: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    3203084: {
        'access': 'read-write',
        'enum': 'ModAccFrequencyErrorEstimation',
        'name': 'MODACC_FREQUENCY_ERROR_ESTIMATION',
        'type': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxlte/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/config.py sha256=a13340558f41f9e63402b018fb44002c1abc23631c364951c79d5304852047dd bytes=2037 -->
## FILE: source/codegen/metadata/nirfmxlte/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/config.py`
- sha256: `a13340558f41f9e63402b018fb44002c1abc23631c364951c79d5304852047dd`
- bytes: 2037

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxLTE.h',
    'c_function_prefix': 'RFmxLTE_',
    'service_class_prefix': 'NiRFmxLTE',
    'java_package': 'com.ni.grpc.nirfmxlte',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxLTE',
    'namespace_component': 'nirfmxlte',
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
    'driver_name': 'NI-RFMXLTE',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxlte',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxLTE.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxLTE.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxlte',
    'session_class_description': 'An NI-RFmxLTE instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxlte/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/enums.py sha256=69aed92d6f45e8d9b0b1470f33456f900d0d26d1e2c20ca43d99fe18c196dac5 bytes=48845 -->
## FILE: source/codegen/metadata/nirfmxlte/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/enums.py`
- sha256: `69aed92d6f45e8d9b0b1470f33456f900d0d26d1e2c20ca43d99fe18c196dac5`
- bytes: 48845

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
    'AcpConfigurableNumberOfOffsetsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpEutraOffsetDefinition': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'CLOSEST',
                'value': 1
            },
            {
                'name': 'COMPOSITE',
                'value': 2
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
    'AutoControlChannelPowerDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoDmrsDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoNPuschChannelDetectionEnabled': {
        'enum-value-prefix': 'AUTO_NPUSCH_CHANNEL_DETECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoPcfichCfiDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoPdschChannelDetectionEnabled': {
        'values': [
            {
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
    'ComponentCarrierSpacingType': {
        'values': [
            {
                'name': 'NOMINAL',
                'value': 0
            },
            {
                'name': 'MINIMUM',
                'value': 1
            },
            {
                'name': 'USER',
                'value': 2
            }
        ]
    },
    'CyclicPrefixMode': {
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
    'DmrsOccEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DownlinkAutoCellIDDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
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
                'name': 'TM3_2',
                'value': 5
            },
            {
                'name': 'TM3_3',
                'value': 6
            },
            {
                'name': 'TM3_1A',
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
    'DownlinkUserDefinedPhichDuration': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            }
        ]
    },
    'DownlinkUserDefinedPhichResource': {
        'values': [
            {
                'name': 'ONE_SIXTH',
                'value': 0
            },
            {
                'name': 'HALF',
                'value': 1
            },
            {
                'name': 'ONE',
                'value': 2
            },
            {
                'name': 'TWO',
                'value': 3
            }
        ]
    },
    'DownlinkUserDefinedRatio': {
        'values': [
            {
                'name': 'P_B0',
                'value': 0
            },
            {
                'name': 'P_B1',
                'value': 1
            },
            {
                'name': 'P_B2',
                'value': 2
            },
            {
                'name': 'P_B3',
                'value': 3
            }
        ]
    },
    'DuplexScheme': {
        'values': [
            {
                'name': 'FDD',
                'value': 0
            },
            {
                'name': 'TDD',
                'value': 1
            },
            {
                'name': 'LAA',
                'value': 2
            }
        ]
    },
    'ENodeBCategory': {
        'enum-value-prefix': 'ENODEB_CATEGORY',
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
                'name': 'HOME_BASE_STATION',
                'value': 4
            },
            {
                'name': 'MEDIUM_RANGE_BASE_STATION',
                'value': 5
            }
        ]
    },
    'EmtcAnalysisEnabled': {
        'values': [
            {
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
    'LaaDownlinkNumberOfEndingSymbols': {
        'values': [
            {
                'name': '3',
                'value': 3
            },
            {
                'name': '6',
                'value': 6
            },
            {
                'name': '9',
                'value': 9
            },
            {
                'name': '10',
                'value': 10
            },
            {
                'name': '11',
                'value': 11
            },
            {
                'name': '12',
                'value': 12
            },
            {
                'name': '14',
                'value': 14
            }
        ]
    },
    'LaaDownlinkStartingSymbol': {
        'values': [
            {
                'name': '0',
                'value': 0
            },
            {
                'name': '7',
                'value': 7
            }
        ]
    },
    'LaaUplinkEndingSymbol': {
        'values': [
            {
                'name': '12',
                'value': 12
            },
            {
                'name': '13',
                'value': 13
            }
        ]
    },
    'LaaUplinkStartPosition': {
        'values': [
            {
                'name': '00',
                'value': 0
            },
            {
                'name': '01',
                'value': 1
            },
            {
                'name': '10',
                'value': 2
            },
            {
                'name': '11',
                'value': 3
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
            },
            {
                'name': 'SIDELINK',
                'value': 2
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
                'name': 'ACP',
                'value': 1
            },
            {
                'name': 'CHP',
                'value': 2
            },
            {
                'name': 'MODACC',
                'value': 4
            },
            {
                'name': 'OBW',
                'value': 8
            },
            {
                'name': 'SEM',
                'value': 16
            },
            {
                'name': 'PVT',
                'value': 32
            },
            {
                'name': 'SLOTPHASE',
                'value': 64
            },
            {
                'name': 'SLOTPOWER',
                'value': 128
            },
            {
                'name': 'TXP',
                'value': 256
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
    'MiConfiguration': {
        'values': [
            {
                'name': 'TEST_MODEL',
                'value': 0
            },
            {
                'name': 'STANDARD',
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
    'ModAccEvmWithExclusionPeriodEnabled': {
        'enum-value-prefix': 'MODACC_EVM_WITH_EXCLUSION_PERIOD_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
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
    'ModAccIQMismatchEstimationsEnabled': {
        'enum-value-prefix': 'MODACC_IQ_MISMATCH_ESTIMATIONS_ENABLED',
        'values': [
            {
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
    'ModAccInBandEmissionMaskType': {
        'enum-value-prefix': 'MODACC_IN_BAND_EMISSION_MASK_TYPE',
        'values': [
            {
                'name': 'RELEASE_8_10',
                'value': 0
            },
            {
                'name': 'RELEASE_11_ONWARDS',
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
    'ModAccMulticarrierTimeSynchronizationMode': {
        'enum-value-prefix': 'MODACC_MULTICARRIER_TIME_SYNCHRONIZATION_MODE',
        'values': [
            {
                'name': 'COMMON',
                'value': 0
            },
            {
                'name': 'PER_CARRIER',
                'value': 1
            }
        ]
    },
    'ModAccPhaseTrackingEnabled': {
        'enum-value-prefix': 'MODACC_PHASE_TRACKING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
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
                'name': 'SUBFRAME',
                'value': 1
            },
            {
                'name': 'MEASUREMENT_LENGTH',
                'value': 2
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
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'MARKER',
                'value': 2
            }
        ]
    },
    'ModAccTimingTrackingEnabled': {
        'enum-value-prefix': 'MODACC_TIMING_TRACKING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'NBIoTDownlinkChannelConfigurationMode': {
        'enum-value-prefix': 'NB_IOT_DOWNLINK_CHANNEL_CONFIGURATION_MODE',
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
    'NBIoTUplinkSubcarrierSpacing': {
        'enum-value-prefix': 'NB_IOT_UPLINK_SUBCARRIER_SPACING',
        'values': [
            {
                'name': '15KHZ',
                'value': 0
            },
            {
                'name': '3_75KHZ',
                'value': 1
            }
        ]
    },
    'NPuschDmrsBaseSequenceMode': {
        'enum-value-prefix': 'NPUSCH_DMRS_BASE_SEQUENCE_MODE',
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
    'NPuschDmrsGroupHoppingEnabled': {
        'enum-value-prefix': 'NPUSCH_DMRS_GROUP_HOPPING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'NPuschModulationType': {
        'enum-value-prefix': 'NPUSCH_MODULATION_TYPE',
        'values': [
            {
                'name': 'BPSK',
                'value': 0
            },
            {
                'name': 'QPSK',
                'value': 1
            }
        ]
    },
    'NpdschEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'NpdschModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': 'QAM16',
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
    'PsschModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': 'QAM16',
                'value': 1
            },
            {
                'name': 'QAM64',
                'value': 2
            }
        ]
    },
    'PuschModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': '16_QAM',
                'value': 1
            },
            {
                'name': '64_QAM',
                'value': 2
            },
            {
                'name': '256_QAM',
                'value': 3
            },
            {
                'name': '1024_QAM',
                'value': 4
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
    'SemComponentCarrierOutputPowerType': {
        'values': [
            {
                'name': 'MAXIMUM_OUTPUT_POWER',
                'value': 0
            },
            {
                'name': 'RATED_OUTPUT_POWER',
                'value': 1
            }
        ]
    },
    'SemDownlinkMaskType': {
        'values': [
            {
                'name': 'ENODEB_CATEGORY_BASED',
                'value': 0
            },
            {
                'name': 'BAND46',
                'value': 1
            },
            {
                'name': 'CUSTOM',
                'value': 5
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
    'SemSidelinkMaskType': {
        'values': [
            {
                'name': 'GENERAL_NS01',
                'value': 0
            },
            {
                'name': 'NS33_OR_NS34',
                'value': 1
            },
            {
                'name': 'CUSTOM',
                'value': 5
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
                'name': 'GENERAL_NS01',
                'value': 0
            },
            {
                'name': 'NS03_OR_NS11_OR_NS20_OR_NS21',
                'value': 1
            },
            {
                'name': 'NS04',
                'value': 2
            },
            {
                'name': 'NS06_OR_NS07',
                'value': 3
            },
            {
                'name': 'CANS04',
                'value': 4
            },
            {
                'name': 'CUSTOM',
                'value': 5
            },
            {
                'name': 'GENERAL_CACLASSB',
                'value': 6
            },
            {
                'name': 'CANCNS01',
                'value': 7
            },
            {
                'name': 'NS27_OR_NS43',
                'value': 8
            },
            {
                'name': 'NS35',
                'value': 9
            },
            {
                'name': 'NS28',
                'value': 10
            },
            {
                'name': 'CANS09',
                'value': 11
            },
            {
                'name': 'CANS10',
                'value': 12
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
    'SlotPhaseCommonClockSourceEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPhaseExclusionPeriodEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPhaseSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPhaseSynchronizationMode': {
        'values': [
            {
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            }
        ]
    },
    'SlotPowerCommonClockSourceEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPowerSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SrsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SrsMaximumUpPtsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
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
    },
    'UplinkDownlinkConfiguration': {
        'values': [
            {
                'name': '0',
                'value': 0
            },
            {
                'name': '1',
                'value': 1
            },
            {
                'name': '2',
                'value': 2
            },
            {
                'name': '3',
                'value': 3
            },
            {
                'name': '4',
                'value': 4
            },
            {
                'name': '5',
                'value': 5
            },
            {
                'name': '6',
                'value': 6
            }
        ]
    },
    'UplinkGroupHoppingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'UplinkSequenceHoppingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'UserDefinedPdschCW0ModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': 'QAM16',
                'value': 1
            },
            {
                'name': 'QAM64',
                'value': 2
            },
            {
                'name': 'QAM256',
                'value': 3
            },
            {
                'name': 'QAM1024',
                'value': 4
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxlte/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxlte/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxlte/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````
