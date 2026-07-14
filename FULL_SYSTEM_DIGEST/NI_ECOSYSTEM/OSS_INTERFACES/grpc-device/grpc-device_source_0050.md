# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/attributes.py sha256=d758fb1cf8eaa524e89ca6cdfed107095871c998fa6487bd228ef5d237583469 bytes=35761 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/attributes.py`
- sha256: `d758fb1cf8eaa524e89ca6cdfed107095871c998fa6487bd228ef5d237583469`
- bytes: 35761

````python
attributes = {
    7340033: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    7340034: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    7340035: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    7340036: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    7340037: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    7340038: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    7340039: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    7340040: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    7340041: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    7340042: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    7340043: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    7340044: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    7340048: {
        'access': 'read-write',
        'enum': 'ChannelConfigurationMode',
        'name': 'CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    7340052: {
        'access': 'read-write',
        'name': 'NUMBER_OF_CHANNELS',
        'type': 'int32'
    },
    7340053: {
        'access': 'read-write',
        'name': 'SLOT_INDEX',
        'type': 'int32'
    },
    7340054: {
        'access': 'read-write',
        'enum': 'ChannelType',
        'name': 'CHANNEL_TYPE',
        'type': 'int32'
    },
    7340055: {
        'access': 'read-write',
        'enum': 'ModulationType',
        'name': 'MODULATION_TYPE',
        'type': 'int32'
    },
    7340056: {
        'access': 'read-write',
        'name': 'SLOT_FORMAT',
        'type': 'int32'
    },
    7340057: {
        'access': 'read-write',
        'name': 'CHANNELIZATION_CODE',
        'type': 'int32'
    },
    7340058: {
        'access': 'read-write',
        'name': 'UPLINK_SCRAMBLING_CODE',
        'type': 'int32'
    },
    7340059: {
        'access': 'read-write',
        'name': 'MAXIMUM_NUMBER_OF_USERS',
        'type': 'int32'
    },
    7340060: {
        'access': 'read-write',
        'name': 'PILOT_CODE',
        'type': 'int32'
    },
    7344124: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    7344125: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    7344127: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    7344128: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7344133: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    7344136: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    7344138: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    7344142: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    7344146: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    7344148: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7344149: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    7344150: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7344152: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    7344155: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    7344156: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    7344157: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    7344158: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    7344159: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    7344160: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    7344161: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7344166: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7344172: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7344173: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    7344178: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7344179: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    7344180: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    7344181: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    7344182: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    7344184: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    7344185: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    7344186: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    7352320: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7352322: {
        'access': 'read-write',
        'name': 'CHP_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    7352323: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7352326: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    7352327: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7352329: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    7352332: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    7352333: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    7352334: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    7352337: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    7352338: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    7352340: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7352341: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7364608: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7364611: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7364612: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    7364614: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    7364615: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7364617: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    7364620: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    7364621: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    7364622: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    7364623: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    7364624: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    7364626: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7364627: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    7364628: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7364629: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    7364630: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    7368704: {
        'access': 'read-write',
        'name': 'PVT_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7368706: {
        'access': 'read-write',
        'enum': 'PvtMeasurementMethod',
        'name': 'PVT_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    7368709: {
        'access': 'read-write',
        'enum': 'PvtRRCFilterEnabled',
        'name': 'PVT_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    7368710: {
        'access': 'read-write',
        'enum': 'PvtAveragingEnabled',
        'name': 'PVT_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7368711: {
        'access': 'read-write',
        'name': 'PVT_AVERAGING_COUNT',
        'type': 'int32'
    },
    7368712: {
        'access': 'read-write',
        'enum': 'PvtAveragingType',
        'name': 'PVT_AVERAGING_TYPE',
        'type': 'int32'
    },
    7368713: {
        'access': 'read-write',
        'name': 'PVT_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7368714: {
        'access': 'read-write',
        'name': 'PVT_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7368716: {
        'access': 'read-write',
        'name': 'PVT_NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    7368717: {
        'access': 'read-write',
        'name': 'PVT_SEGMENT_START',
        'type': 'float64'
    },
    7368718: {
        'access': 'read-write',
        'name': 'PVT_SEGMENT_STOP',
        'type': 'float64'
    },
    7368719: {
        'access': 'read-write',
        'enum': 'PvtMeasurementStatus',
        'name': 'PVT_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    7368720: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MEAN_ABSOLUTE_ON_POWER',
        'type': 'float64'
    },
    7368721: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MEAN_ABSOLUTE_OFF_POWER',
        'type': 'float64'
    },
    7368722: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MAXIMUM_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7368723: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MINIMUM_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7368724: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_BURST_WIDTH',
        'type': 'float64'
    },
    7368727: {
        'access': 'read-write',
        'enum': 'PvtSegmentStatus',
        'name': 'PVT_RESULTS_SEGMENT_STATUS',
        'type': 'int32'
    },
    7368728: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SEGMENT_MARGIN',
        'type': 'float64'
    },
    7368729: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SEGMENT_MARGIN_TIME',
        'type': 'float64'
    },
    7368731: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SEGMENT_MEAN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7368732: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SEGMENT_MAXIMUM_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7368733: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_SEGMENT_MINIMUM_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7368734: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MIDAMBLE_CODE',
        'type': 'int32'
    },
    7368735: {
        'access': 'read-write',
        'name': 'PVT_RESULTS_MIDAMBLE_SHIFT',
        'type': 'int32'
    },
    7372800: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7372805: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    7372811: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    7372812: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    7372820: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    7372821: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    7372823: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    7372824: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    7372829: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7372830: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    7372831: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7372833: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    7372837: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    7372838: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    7372839: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7372841: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    7372845: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    7372852: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    7372853: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    7372854: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    7372855: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    7372856: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    7372857: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    7372858: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7372859: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    7372860: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    7372861: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    7372865: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    7372866: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    7372867: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    7372868: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    7372869: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    7372870: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    7372871: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    7372872: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    7372873: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    7372874: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    7376896: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7376898: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    7376899: {
        'access': 'read-write',
        'enum': 'SlotPowerSpectrumInverted',
        'name': 'SLOTPOWER_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    7376900: {
        'access': 'read-write',
        'enum': 'SlotPowerRrcFilterEnabled',
        'name': 'SLOTPOWER_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    7389184: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    7393280: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    7393283: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    7409664: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7409666: {
        'access': 'read-write',
        'enum': 'ModAccSynchronizationMode',
        'name': 'MODACC_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    7409667: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    7409668: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    7409670: {
        'access': 'read-write',
        'enum': 'ModAccSlotType',
        'name': 'MODACC_SLOT_TYPE',
        'type': 'int32'
    },
    7409671: {
        'access': 'read-write',
        'enum': 'MidambleAutoDetectionMode',
        'name': 'MIDAMBLE_AUTO_DETECTION_MODE',
        'type': 'int32'
    },
    7409673: {
        'access': 'read-write',
        'name': 'MIDAMBLE_SHIFT',
        'type': 'int32'
    },
    7409674: {
        'access': 'read-write',
        'enum': 'ModAccSpectrumInverted',
        'name': 'MODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    7409675: {
        'access': 'read-write',
        'enum': 'ModAccAveragingEnabled',
        'name': 'MODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7409677: {
        'access': 'read-write',
        'name': 'MODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    7409681: {
        'access': 'read-write',
        'enum': 'ModAccIQGainImbalanceRemovalEnabled',
        'name': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7409682: {
        'access': 'read-write',
        'enum': 'ModAccIQQuadratureErrorRemovalEnabled',
        'name': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7409683: {
        'access': 'read-write',
        'enum': 'ModAccRrcFilterEnabled',
        'name': 'MODACC_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    7409691: {
        'access': 'read-write',
        'enum': 'ModAccIQOffsetRemovalEnabled',
        'name': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7409692: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7409792: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_COMPOSITE_EVM',
        'type': 'float64'
    },
    7409793: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_COMPOSITE_EVM',
        'type': 'float64'
    },
    7409794: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_COMPOSITE_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    7409795: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_COMPOSITE_PHASE_ERROR',
        'type': 'float64'
    },
    7409796: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    7409797: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    7409798: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    7409799: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_FREQUENCY_ERROR',
        'type': 'float64'
    },
    7409800: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_COMPOSITE_RHO',
        'type': 'float64'
    },
    7409802: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_MIDAMBLE_EVM',
        'type': 'float64'
    },
    7409803: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_MIDAMBLE_EVM',
        'type': 'float64'
    },
    7409804: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_MIDAMBLE_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    7409805: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_MIDAMBLE_PHASE_ERROR',
        'type': 'float64'
    },
    7409806: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MIDAMBLE_RHO',
        'type': 'float64'
    },
    7409807: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MIDAMBLE_POWER',
        'type': 'float64'
    },
    7409808: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MIDAMBLE_CODE',
        'type': 'int32'
    },
    7409809: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MIDAMBLE_SHIFT',
        'type': 'int32'
    },
    7409810: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_DATA_EVM',
        'type': 'float64'
    },
    7409811: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_EVM',
        'type': 'float64'
    },
    7409812: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_DATA_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    7409813: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_DATA_PHASE_ERROR',
        'type': 'float64'
    },
    7409814: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DATA_RHO',
        'type': 'float64'
    },
    7409815: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_CDE',
        'type': 'float64'
    },
    7409816: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_CDE_SPREADING_FACTOR',
        'type': 'int32'
    },
    7409817: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_CDE_CODE',
        'type': 'int32'
    },
    7409818: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE',
        'type': 'float64'
    },
    7409819: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_SPREADING_FACTOR',
        'type': 'int32'
    },
    7409820: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_CODE',
        'type': 'int32'
    },
    7409821: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_ACTIVE_CDE_NUMBER_OF_CHANNELS',
        'type': 'int32'
    },
    7409822: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DATA_FIELD_1_POWER',
        'type': 'float64'
    },
    7409823: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DATA_FIELD_2_POWER',
        'type': 'float64'
    },
    7409824: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_RCDE',
        'type': 'float64'
    },
    7409825: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_RCDE_SPREADING_FACTOR',
        'type': 'int32'
    },
    7409826: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DATA_RCDE_CODE',
        'type': 'int32'
    },
    7409827: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS',
        'type': 'int32'
    },
    7409828: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_SLOT_INDEX',
        'type': 'int32'
    },
    7409829: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_SPREADING_FACTOR',
        'type': 'int32'
    },
    7409830: {
        'access': 'read-write',
        'enum': 'ModAccDetectedModulationType',
        'name': 'MODACC_RESULTS_DETECTED_MODULATION_TYPE',
        'type': 'int32'
    },
    7409831: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_CHANNELIZATION_CODE',
        'type': 'int32'
    },
    7409833: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    7409838: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_PILOT_EVM',
        'type': 'float64'
    },
    7409839: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_PILOT_EVM',
        'type': 'float64'
    },
    7409840: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_PILOT_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    7409841: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_PILOT_PHASE_ERROR',
        'type': 'float64'
    },
    7409842: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PILOT_RHO',
        'type': 'float64'
    },
    7409843: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_COMPOSITE_RHO',
        'type': 'float64'
    },
    7409855: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_DATA_CDE',
        'type': 'float64'
    },
    7409856: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_DATA_ACTIVE_CDE',
        'type': 'float64'
    },
    7409857: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MAXIMUM_PEAK_DATA_RCDE',
        'type': 'float64'
    },
    7417856: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    7417858: {
        'access': 'read-write',
        'enum': 'CdaSynchronizationMode',
        'name': 'CDA_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    7417859: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    7417860: {
        'access': 'read-write',
        'name': 'CDA_BASE_SPREADING_FACTOR',
        'type': 'int32'
    },
    7417861: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR',
        'type': 'int32'
    },
    7417862: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_CHANNELIZATION_CODE',
        'type': 'int32'
    },
    7417863: {
        'access': 'read-write',
        'enum': 'CdaSpectrumInverted',
        'name': 'CDA_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    7417864: {
        'access': 'read-write',
        'enum': 'CdaIQOffsetRemovalEnabled',
        'name': 'CDA_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7417865: {
        'access': 'read-write',
        'enum': 'CdaIQGainImbalanceRemovalEnabled',
        'name': 'CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7417866: {
        'access': 'read-write',
        'enum': 'CdaIQQuadratureErrorRemovalEnabled',
        'name': 'CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    7417867: {
        'access': 'read-write',
        'enum': 'CdaPowerUnit',
        'name': 'CDA_POWER_UNIT',
        'type': 'int32'
    },
    7417868: {
        'access': 'read-write',
        'enum': 'CdaRrcFilterEnabled',
        'name': 'CDA_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    7417869: {
        'access': 'read-write',
        'name': 'CDA_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    7417870: {
        'access': 'read-write',
        'name': 'CDA_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    7417872: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_RMS_SYMBOL_EVM',
        'type': 'float64'
    },
    7417874: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_RMS_SYMBOL_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    7417875: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_RMS_SYMBOL_PHASE_ERROR',
        'type': 'float64'
    },
    7417876: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    7417877: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    7417878: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    7417879: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_FREQUENCY_ERROR',
        'type': 'float64'
    },
    7417880: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    7417881: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_TOTAL_POWER',
        'type': 'float64'
    },
    7417882: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_TOTAL_ACTIVE_POWER',
        'type': 'float64'
    },
    7417883: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    7417885: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_INACTIVE_POWER',
        'type': 'float64'
    },
    7417889: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MAXIMUM_PEAK_SYMBOL_EVM',
        'type': 'float64'
    },
    7417892: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MAXIMUM_TOTAL_POWER',
        'type': 'float64'
    },
    7417893: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MAXIMUM_TOTAL_ACTIVE_POWER',
        'type': 'float64'
    },
    7417895: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MAXIMUM_PEAK_ACTIVE_POWER',
        'type': 'float64'
    },
    7417897: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MAXIMUM_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    7417898: {
        'access': 'read-write',
        'enum': 'CdaAveragingEnabled',
        'name': 'CDA_AVERAGING_ENABLED',
        'type': 'int32'
    },
    7417900: {
        'access': 'read-write',
        'name': 'CDA_AVERAGING_COUNT',
        'type': 'int32'
    },
    7417901: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_SYMBOL_POWER',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/config.py sha256=8b27a8234d784ad8bd83e38a389fd2281404512ee41e77995cbe0ba07b10c565 bytes=2012 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/config.py`
- sha256: `8b27a8234d784ad8bd83e38a389fd2281404512ee41e77995cbe0ba07b10c565`
- bytes: 2012

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.3.0',
    'c_header': 'niRFmxTDSCDMA.h',
    'c_function_prefix': 'RFmxTDSCDMA_',
    'service_class_prefix': 'NiRFmxTDSCDMA',
    'java_package': 'com.ni.grpc.nirfmxtdscdma',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxTDSCDMA',
    'namespace_component': 'nirfmxtdscdma',
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
    'driver_name': 'NI-rfmxtdscdma',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxtdscdma',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxTDSCDMA.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxTDSCDMA.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxtdscdma',
    'session_class_description': 'An NI-RFmxTDSCDMA instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/enums.py sha256=9ec514d82722897ce238654d4a023738f9a032113beeb87113369089a4f88413 bytes=23630 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/enums.py`
- sha256: `9ec514d82722897ce238654d4a023738f9a032113beeb87113369089a4f88413`
- bytes: 23630

````python
enums = {
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
    'AcpFftOverlapMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'AUTOMATIC',
                'value': 1
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
    'CdaAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaIQGainImbalanceRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaIQQuadratureErrorRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaPowerUnit': {
        'values': [
            {
                'name': 'DB',
                'value': 0
            },
            {
                'name': 'DBM',
                'value': 1
            }
        ]
    },
    'CdaRrcFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSynchronizationMode': {
        'values': [
            {
                'name': 'SLOT',
                'value': 0
            }
        ]
    },
    'ChannelConfigurationMode': {
        'values': [
            {
                'name': 'AUTO_DETECT',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'ChannelType': {
        'values': [
            {
                'name': 'IDLE',
                'value': 0
            },
            {
                'name': 'DPCH',
                'value': 1
            },
            {
                'name': 'EDCH',
                'value': 2
            },
            {
                'name': 'HSSICH',
                'value': 3
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
                'name': 'MODACC',
                'value': 1
            },
            {
                'name': 'ACP',
                'value': 2
            },
            {
                'name': 'CHP',
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
                'name': 'CDA',
                'value': 32
            },
            {
                'name': 'PVT',
                'value': 64
            },
            {
                'name': 'SLOTPOWER',
                'value': 128
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
    'MidambleAutoDetectionMode': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'MIDAMBLE_SHIFT',
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
    'ModAccDetectedModulationType': {
        'enum-value-prefix': 'MODACC_DETECTED_MODULATION_TYPE',
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': '8PSK',
                'value': 1
            },
            {
                'name': '16QAM',
                'value': 2
            }
        ]
    },
    'ModAccIQGainImbalanceRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQOffsetRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQQuadratureErrorRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccMeasurementSlotType': {
        'enum-value-prefix': 'MODACC_MEASUREMENT_SLOT_TYPE',
        'values': [
            {
                'name': 'TRAFFIC',
                'value': 0
            },
            {
                'name': 'PILOT',
                'value': 1
            }
        ]
    },
    'ModAccRrcFilterEnabled': {
        'enum-value-prefix': 'MODACC_RRC_FILTER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccSlotType': {
        'enum-value-prefix': 'MODACC_SLOT_TYPE',
        'values': [
            {
                'name': 'TRAFFIC',
                'value': 0
            },
            {
                'name': 'PILOT',
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
    'ModAccSynchronizationMode': {
        'enum-value-prefix': 'MODACC_SYNCHRONIZATION_MODE',
        'values': [
            {
                'name': 'SLOT',
                'value': 0
            },
            {
                'name': 'SUBFRAME',
                'value': 1
            }
        ]
    },
    'ModulationType': {
        'values': [
            {
                'name': 'QPSK',
                'value': 0
            },
            {
                'name': '8PSK',
                'value': 1
            },
            {
                'name': '16QAM',
                'value': 2
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
    'PvtRRCFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PvtSegmentStatus': {
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
            },
            {
                'name': 'SYNCH_TUNED_4',
                'value': 3
            },
            {
                'name': 'SYNCH_TUNED_5',
                'value': 4
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
    'SlotPowerRrcFilterEnabled': {
        'values': [
            {
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/functions.py sha256=fdc19036adab7c3154d65e8c54ee48f76fc5039719df56992bf9e9c581feffef bytes=193590 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/functions.py`
- sha256: `fdc19036adab7c3154d65e8c54ee48f76fc5039719df56992bf9e9c581feffef`
- bytes: 193590

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
        'cname': 'RFmxTDSCDMA_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'CDACfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CdaAveragingEnabled',
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
                'name': 'spreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelizationCode',
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
    'CDACfgSynchronizationModeAndOffset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'meanTotalPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanTotalActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakActivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanInactivePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakInactivePower',
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
    'CDAFetchMaximumCodeDomainPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumCodeDomainPowers',
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
    'CDAFetchMaximumSymbolEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumSymbolEVM',
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
    'CDAFetchMaximumSymbolMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumSymbolMagnitudeError',
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
    'CDAFetchMaximumSymbolPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumSymbolPhaseError',
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
    'CDAFetchMeanCodeDomainPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanCodeDomainPowers',
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
    'CDAFetchMeanSymbolEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSymbolEVM',
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
    'CDAFetchMeanSymbolMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSymbolMagnitudeError',
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
    'CDAFetchMeanSymbolPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSymbolPhaseError',
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
        'cname': 'RFmxTDSCDMA_CDAFetchSymbolConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'meanRMSSymbolEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakSymbolEVM',
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
                'name': 'meanRMSSymbolMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanRMSSymbolPhaseError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanSymbolPower',
                'type': 'float64'
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
    'CfgMidambleShift': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MidambleAutoDetectionMode',
                'name': 'midambleAutoDetectionMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'maximumNumberOfUsers',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'midambleShift',
                'type': 'int32'
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
    'CfgPilot': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pilotCode',
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
    'CfgUplinkScramblingCode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'uplinkScramblingCode',
                'type': 'int32'
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
                'name': 'slotIndex',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ChannelType',
                'name': 'channelType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'slotFormat',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ModulationType',
                'name': 'modulationType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelizationCode',
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
                'name': 'slotIndex',
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
                'enum': 'ChannelType',
                'name': 'channelType',
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
                'name': 'slotFormat',
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
                'enum': 'ModulationType',
                'name': 'modulationType',
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
                'name': 'channelizationCode',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
        'custom_close': 'Close(id, RFMXTDSCDMA_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXTDSCDMA_VAL_FALSE)',
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
    'ModAccCfgSlotType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccMeasurementSlotType',
                'name': 'slotType',
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
    'ModAccFetchCodeDomainErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'codeDomainError',
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
                'name': 'rmsCompositeEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakCompositeEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'compositeRho',
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
                'name': 'rmsCompositeMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsCompositePhaseError',
                'type': 'float64'
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
        'cname': 'RFmxTDSCDMA_ModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchDataActiveCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakDataActiveCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakDataActiveCDESpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakDataActiveCDECode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakDataActiveCDENumberOfChannels',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDataCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakDataCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakDataCDESpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakDataCDECode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDataEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsDataEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakDataEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataRho',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsDataMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsDataPhaseError',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDataRCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumPeakDataRCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakDataRCDESpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakDataRCDECode',
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
                'name': 'detectedSlotIndex',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'detectedSpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedModulationType',
                'name': 'detectedModulationType',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'detectedChannelizationCode',
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
                'name': 'detectedSlotIndex',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'detectedSpreadingFactor',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedModulationType',
                'name': 'detectedModulationType',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'detectedChannelizationCode',
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
    'ModAccFetchMaximumCodeDomainErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'maximumCodeDomainError',
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
    'ModAccFetchMaximumEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumEVM',
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
    'ModAccFetchMaximumMagnitudeErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumMagnitudeError',
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
    'ModAccFetchMaximumPhaseErrorTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'maximumPhaseError',
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
    'ModAccFetchMidambleAndDataPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'midamblePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataField1Power',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dataField2Power',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchMidambleEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsMidambleEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakMidambleEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'midambleRho',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsMidambleMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsMidamblePhaseError',
                'type': 'float64'
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
    'ModAccFetchPilotEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsPilotEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakPilotEVM',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'pilotRho',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsPilotMagnitudeError',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rmsPilotPhaseError',
                'type': 'float64'
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
    'PVTFetchPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteONPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'meanAbsoluteOFFPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchSegmentMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtSegmentStatus',
                'name': 'segmentStatus',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'segmentMargin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'segmentMarginTime',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'segmentMeanAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'segmentMaximumAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'segmentMinimumAbsolutePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'PVTFetchSegmentMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'PvtSegmentStatus',
                'name': 'segmentStatus',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'segmentMargin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'segmentMarginTime',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'segmentMeanAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'segmentMaximumAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'segmentMinimumAbsolutePower',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
                'grpc_type': 'NiRFmxTDSCDMAAttribute',
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
    'SlotPowerCfgMeasurementLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxtdscdma/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxtdscdma/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxtdscdma/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/__init__.py sha256=9f2093ddaaf188e3d37c1fccce6ee28dbb56756ec05683fd6d89597b24b732f8 bytes=244 -->
## FILE: source/codegen/metadata/nirfmxvna/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/attributes.py sha256=9b94eca3bb429e50d1753f116abbdae8ccd48e1e11682f8a8d5be4e8fc032192 bytes=20037 -->
## FILE: source/codegen/metadata/nirfmxvna/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/attributes.py`
- sha256: `9b94eca3bb429e50d1753f116abbdae8ccd48e1e11682f8a8d5be4e8fc032192`
- bytes: 20037

````python
attributes = {
    13631489: {
        'access': 'read-write',
        'name': 'NUMBER_OF_SEGMENTS',
        'type': 'int32'
    },
    13631490: {
        'access': 'read-write',
        'name': 'FREQUENCY_LIST',
        'type': 'float64[]'
    },
    13631491: {
        'access': 'read-write',
        'name': 'POWER_LEVEL',
        'type': 'float64'
    },
    13631492: {
        'access': 'read-write',
        'name': 'IF_BANDWIDTH',
        'type': 'float64'
    },
    13631493: {
        'access': 'read-write',
        'name': 'SWEEP_DELAY',
        'type': 'float64'
    },
    13631494: {
        'access': 'read-write',
        'name': 'DWELL_TIME',
        'type': 'float64'
    },
    13631495: {
        'access': 'read-write',
        'enum': 'AveragingEnabled',
        'name': 'AVERAGING_ENABLED',
        'type': 'int32'
    },
    13631496: {
        'access': 'read-write',
        'name': 'AVERAGING_COUNT',
        'type': 'int32'
    },
    13631498: {
        'access': 'read-write',
        'name': 'TEST_RECEIVER_ATTENUATION',
        'type': 'float64'
    },
    13631499: {
        'access': 'read-write',
        'enum': 'CorrectionEnabled',
        'name': 'CORRECTION_ENABLED',
        'type': 'int32'
    },
    13631502: {
        'access': 'read-write',
        'enum': 'CorrectionPortSubsetEnabled',
        'name': 'CORRECTION_PORT_SUBSET_ENABLED',
        'type': 'int32'
    },
    13631503: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_SUBSET_FULL_PORTS',
        'type': 'char[]'
    },
    13631504: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_PORTS',
        'type': 'char[]'
    },
    13631505: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_CONNECTOR_TYPE',
        'type': 'char[]'
    },
    13631506: {
        'access': 'read-write',
        'enum': 'CorrectionCalibrationCalkitType',
        'name': 'CORRECTION_CALIBRATION_CALKIT_TYPE',
        'type': 'int32'
    },
    13631507: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_RESOURCE_NAME',
        'type': 'char[]'
    },
    13631508: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_CALKIT_MECHANICAL_NAME',
        'type': 'char[]'
    },
    13631509: {
        'access': 'read-write',
        'enum': 'CorrectionCalibrationMethod',
        'name': 'CORRECTION_CALIBRATION_METHOD',
        'type': 'int32'
    },
    13631511: {
        'access': 'read-write',
        'enum': 'CorrectionCalibrationThruMethod',
        'name': 'CORRECTION_CALIBRATION_THRU_METHOD',
        'type': 'int32'
    },
    13631512: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_THRU_COAX_DELAY',
        'type': 'float64'
    },
    13631513: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_STEP_COUNT',
        'type': 'int32'
    },
    13631514: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_STEP_DESCRIPTION',
        'type': 'char[]'
    },
    13631518: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_CALKIT_ELECTRONIC_ORIENTATION',
        'type': 'char[]'
    },
    13631526: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionEnabled',
        'name': 'CORRECTION_PORT_EXTENSION_ENABLED',
        'type': 'int32'
    },
    13631527: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_DELAY',
        'type': 'float64'
    },
    13631528: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionDCLossEnabled',
        'name': 'CORRECTION_PORT_EXTENSION_DC_LOSS_ENABLED',
        'type': 'int32'
    },
    13631529: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_DC_LOSS',
        'type': 'float64'
    },
    13631533: {
        'access': 'read-write',
        'enum': 'SweepSequence',
        'name': 'SWEEP_SEQUENCE',
        'type': 'int32'
    },
    13631534: {
        'access': 'read-write',
        'enum': 'SweepType',
        'name': 'SWEEP_TYPE',
        'type': 'int32'
    },
    13631535: {
        'access': 'read-write',
        'enum': 'SegmentEnabled',
        'name': 'SEGMENT_ENABLED',
        'type': 'int32'
    },
    13631537: {
        'access': 'read-write',
        'enum': 'PulseModeEnabled',
        'name': 'PULSE_MODE_ENABLED',
        'type': 'int32'
    },
    13631539: {
        'access': 'read-write',
        'enum': 'PulseTriggerType',
        'name': 'PULSE_TRIGGER_TYPE',
        'type': 'int32'
    },
    13631540: {
        'access': 'read-write',
        'enum': 'PulseDigitalEdgeTriggerSource',
        'name': 'PULSE_DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    13631541: {
        'access': 'read-write',
        'name': 'PULSE_PERIOD',
        'type': 'float64'
    },
    13631543: {
        'access': 'read-write',
        'name': 'PULSE_MODULATOR_DELAY',
        'type': 'float64'
    },
    13631544: {
        'access': 'read-write',
        'name': 'PULSE_MODULATOR_WIDTH',
        'type': 'float64'
    },
    13631545: {
        'access': 'read-write',
        'enum': 'PulseAcquisitionAuto',
        'name': 'PULSE_ACQUISITION_AUTO',
        'type': 'int32'
    },
    13631546: {
        'access': 'read-write',
        'name': 'PULSE_ACQUISITION_DELAY',
        'type': 'float64'
    },
    13631547: {
        'access': 'read-write',
        'name': 'PULSE_ACQUISITION_WIDTH',
        'type': 'float64'
    },
    13631550: {
        'access': 'read-write',
        'enum': 'PulseGeneratorEnabled',
        'name': 'PULSE_GENERATOR_ENABLED',
        'type': 'int32'
    },
    13631551: {
        'access': 'read-write',
        'name': 'PULSE_GENERATOR_EXPORT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    13631552: {
        'access': 'read-write',
        'name': 'PULSE_GENERATOR_DELAY',
        'type': 'float64'
    },
    13631553: {
        'access': 'read-write',
        'name': 'PULSE_GENERATOR_WIDTH',
        'type': 'float64'
    },
    13631554: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    13631555: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    13631556: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    13631557: {
        'access': 'read-write',
        'enum': 'TriggerMode',
        'name': 'TRIGGER_MODE',
        'type': 'int32'
    },
    13631558: {
        'access': 'read-write',
        'enum': 'AutoIFBandwidthScalingEnabled',
        'name': 'AUTO_IF_BANDWIDTH_SCALING_ENABLED',
        'type': 'int32'
    },
    13631559: {
        'access': 'read-write',
        'enum': 'CorrectionSwitchPortsMultipathCalibration',
        'name': 'CORRECTION_SWITCH_PORTS_MULTIPATH_CALIBRATION',
        'type': 'int32'
    },
    13631560: {
        'access': 'read-write',
        'enum': 'SegmentPowerLevelEnabled',
        'name': 'SEGMENT_POWER_LEVEL_ENABLED',
        'type': 'int32'
    },
    13631561: {
        'access': 'read-write',
        'name': 'SEGMENT_POWER_LEVEL',
        'type': 'float64'
    },
    13631562: {
        'access': 'read-write',
        'enum': 'SegmentIFBandwidthEnabled',
        'name': 'SEGMENT_IF_BANDWIDTH_ENABLED',
        'type': 'int32'
    },
    13631563: {
        'access': 'read-write',
        'name': 'SEGMENT_IF_BANDWIDTH',
        'type': 'float64'
    },
    13631564: {
        'access': 'read-write',
        'enum': 'SegmentTestReceiverAttenuationEnabled',
        'name': 'SEGMENT_TEST_RECEIVER_ATTENUATION_ENABLED',
        'type': 'int32'
    },
    13631565: {
        'access': 'read-write',
        'name': 'SEGMENT_TEST_RECEIVER_ATTENUATION',
        'type': 'float64'
    },
    13631566: {
        'access': 'read-write',
        'enum': 'SegmentDwellTimeEnabled',
        'name': 'SEGMENT_DWELL_TIME_ENABLED',
        'type': 'int32'
    },
    13631567: {
        'access': 'read-write',
        'name': 'SEGMENT_DWELL_TIME',
        'type': 'float64'
    },
    13631568: {
        'access': 'read-write',
        'name': 'PULSE_GENERATOR_TERMINAL_NAME',
        'type': 'char[]'
    },
    13631569: {
        'access': 'read-write',
        'name': 'START_FREQUENCY',
        'type': 'float64'
    },
    13631570: {
        'access': 'read-write',
        'name': 'STOP_FREQUENCY',
        'type': 'float64'
    },
    13631571: {
        'access': 'read-write',
        'name': 'NUMBER_OF_POINTS',
        'type': 'int32'
    },
    13631572: {
        'access': 'read-write',
        'name': 'SEGMENT_START_FREQUENCY',
        'type': 'float64'
    },
    13631573: {
        'access': 'read-write',
        'name': 'SEGMENT_STOP_FREQUENCY',
        'type': 'float64'
    },
    13631574: {
        'access': 'read-write',
        'name': 'SEGMENT_NUMBER_OF_FREQUENCY_POINTS',
        'type': 'int32'
    },
    13631575: {
        'access': 'read-write',
        'name': 'X_AXIS_VALUES',
        'type': 'float64[]'
    },
    13631576: {
        'access': 'read-write',
        'enum': 'CorrectionInterpolationEnabled',
        'name': 'CORRECTION_INTERPOLATION_ENABLED',
        'type': 'int32'
    },
    13631577: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionLoss1Enabled',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS1_ENABLED',
        'type': 'int32'
    },
    13631578: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS1_FREQUENCY',
        'type': 'float64'
    },
    13631579: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS1',
        'type': 'float64'
    },
    13631580: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionLoss2Enabled',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS2_ENABLED',
        'type': 'int32'
    },
    13631581: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS2_FREQUENCY',
        'type': 'float64'
    },
    13631582: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_LOSS2',
        'type': 'float64'
    },
    13631583: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionDelayDomain',
        'name': 'CORRECTION_PORT_EXTENSION_DELAY_DOMAIN',
        'type': 'int32'
    },
    13631584: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_DISTANCE',
        'type': 'float64'
    },
    13631585: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionDistanceUnit',
        'name': 'CORRECTION_PORT_EXTENSION_DISTANCE_UNIT',
        'type': 'int32'
    },
    13631586: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_VELOCITY_FACTOR',
        'type': 'float64'
    },
    13631587: {
        'access': 'read-write',
        'name': 'READY_FOR_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    13631588: {
        'access': 'read-write',
        'name': 'READY_FOR_TRIGGER_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    13631589: {
        'access': 'read-write',
        'enum': 'ReadyForTriggerEventLevel',
        'name': 'READY_FOR_TRIGGER_EVENT_LEVEL',
        'type': 'int32'
    },
    13631590: {
        'access': 'read-write',
        'name': 'INDEX_EVENT_OUTPUT_TERMINAL',
        'type': 'char[]'
    },
    13631591: {
        'access': 'read-write',
        'name': 'INDEX_EVENT_TERMINAL_NAME',
        'type': 'char[]'
    },
    13631592: {
        'access': 'read-write',
        'enum': 'IndexEventLevel',
        'name': 'INDEX_EVENT_LEVEL',
        'type': 'int32'
    },
    13631594: {
        'access': 'read-write',
        'name': 'CW_FREQUENCY',
        'type': 'float64'
    },
    13631600: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    13631609: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_SUBSET_RESPONSE_PORTS',
        'type': 'char[]'
    },
    13631610: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionAutoLossEnabled',
        'name': 'CORRECTION_PORT_EXTENSION_AUTO_LOSS_ENABLED',
        'type': 'int32'
    },
    13631611: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionAutoRegularizationEnabled',
        'name': 'CORRECTION_PORT_EXTENSION_AUTO_REGULARIZATION_ENABLED',
        'type': 'int32'
    },
    13631612: {
        'access': 'read-write',
        'enum': 'CorrectionPortExtensionAutoFrequencyMode',
        'name': 'CORRECTION_PORT_EXTENSION_AUTO_FREQUENCY_MODE',
        'type': 'int32'
    },
    13631613: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_AUTO_START_FREQUENCY',
        'type': 'float64'
    },
    13631614: {
        'access': 'read-write',
        'name': 'CORRECTION_PORT_EXTENSION_AUTO_STOP_FREQUENCY',
        'type': 'float64'
    },
    13633536: {
        'access': 'read-write',
        'name': 'CORRECTION_CALIBRATION_ESTIMATED_THRU_DELAY',
        'type': 'float64'
    },
    13635584: {
        'access': 'read-write',
        'name': 'SPARAMS_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    13635586: {
        'access': 'read-write',
        'name': 'SPARAMS_NUMBER_OF_SPARAMETERS',
        'type': 'int32'
    },
    13635587: {
        'access': 'read-write',
        'name': 'SPARAMS_RECEIVER_PORT',
        'type': 'char[]'
    },
    13635588: {
        'access': 'read-write',
        'name': 'SPARAMS_SOURCE_PORT',
        'type': 'char[]'
    },
    13635589: {
        'access': 'read-write',
        'enum': 'SParamsFormat',
        'name': 'SPARAMS_FORMAT',
        'type': 'int32'
    },
    13635590: {
        'access': 'read-write',
        'enum': 'SParamsMagnitudeUnits',
        'name': 'SPARAMS_MAGNITUDE_UNITS',
        'type': 'int32'
    },
    13635591: {
        'access': 'read-write',
        'enum': 'SParamsPhaseTraceType',
        'name': 'SPARAMS_PHASE_TRACE_TYPE',
        'type': 'int32'
    },
    13635594: {
        'access': 'read-write',
        'name': 'IQ_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    13635597: {
        'access': 'read-write',
        'name': 'IQ_ACQUISITION_TIME',
        'type': 'float64'
    },
    13635599: {
        'access': 'read-write',
        'name': 'IQ_RECEIVER_PORT',
        'type': 'char[]'
    },
    13635600: {
        'access': 'read-write',
        'name': 'IQ_SOURCE_PORT',
        'type': 'char[]'
    },
    13635603: {
        'access': 'read-write',
        'enum': 'SParamsSnPDataFormat',
        'name': 'SPARAMS_SNP_DATA_FORMAT',
        'type': 'int32'
    },
    13635604: {
        'access': 'read-write',
        'name': 'SPARAMS_SNP_USER_COMMENT',
        'type': 'char[]'
    },
    13635605: {
        'access': 'read-write',
        'name': 'SPARAMS_SNP_PORTS',
        'type': 'char[]'
    },
    13635607: {
        'access': 'read-write',
        'name': 'SPARAMS_PARAMETER',
        'type': 'char[]'
    },
    13635608: {
        'access': 'read-write',
        'enum': 'SParamsCorrectionState',
        'name': 'SPARAMS_RESULTS_CORRECTION_STATE',
        'type': 'int32'
    },
    13635609: {
        'access': 'read-write',
        'enum': 'IQCorrectionState',
        'name': 'IQ_RESULTS_CORRECTION_STATE',
        'type': 'int32'
    },
    13635610: {
        'access': 'read-write',
        'enum': 'SParamsMathFunction',
        'name': 'SPARAMS_MATH_FUNCTION',
        'type': 'int32'
    },
    13635611: {
        'access': 'read-write',
        'name': 'SPARAMS_MATH_ACTIVE_MEASUREMENT_MEMORY',
        'type': 'char[]'
    },
    13635612: {
        'access': 'read-write',
        'enum': 'SParamsGroupDelayApertureMode',
        'name': 'SPARAMS_GROUP_DELAY_APERTURE_MODE',
        'type': 'int32'
    },
    13635613: {
        'access': 'read-write',
        'name': 'SPARAMS_GROUP_DELAY_APERTURE_POINTS',
        'type': 'float64'
    },
    13635614: {
        'access': 'read-write',
        'name': 'SPARAMS_GROUP_DELAY_APERTURE_PERCENTAGE',
        'type': 'float64'
    },
    13635615: {
        'access': 'read-write',
        'name': 'SPARAMS_GROUP_DELAY_APERTURE_FREQUENCY_SPAN',
        'type': 'float64'
    },
    13635616: {
        'access': 'read-write',
        'name': 'SPARAMS_RESULTS_CORRECTION_LEVEL',
        'type': 'char[]'
    },
    13639680: {
        'access': 'read-write',
        'name': 'WAVES_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    13639682: {
        'access': 'read-write',
        'name': 'WAVES_NUMBER_OF_WAVES',
        'type': 'int32'
    },
    13639683: {
        'access': 'read-write',
        'enum': 'WavesReceiver',
        'name': 'WAVES_RECEIVER',
        'type': 'int32'
    },
    13639684: {
        'access': 'read-write',
        'name': 'WAVES_RECEIVER_PORT',
        'type': 'char[]'
    },
    13639685: {
        'access': 'read-write',
        'name': 'WAVES_SOURCE_PORT',
        'type': 'char[]'
    },
    13639686: {
        'access': 'read-write',
        'enum': 'WavesFormat',
        'name': 'WAVES_FORMAT',
        'type': 'int32'
    },
    13639687: {
        'access': 'read-write',
        'enum': 'WavesMagnitudeUnits',
        'name': 'WAVES_MAGNITUDE_UNITS',
        'type': 'int32'
    },
    13639688: {
        'access': 'read-write',
        'enum': 'WavesPhaseTraceType',
        'name': 'WAVES_PHASE_TRACE_TYPE',
        'type': 'int32'
    },
    13639691: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    13639692: {
        'access': 'read-write',
        'enum': 'SourcePowerMode',
        'name': 'SOURCE_POWER_MODE',
        'type': 'int32'
    },
    13639693: {
        'access': 'read-write',
        'name': 'GROUND_TERMINATED_PORTS',
        'type': 'char[]'
    },
    13639698: {
        'access': 'read-write',
        'name': 'WAVES_PARAMETER',
        'type': 'char[]'
    },
    13639699: {
        'access': 'read-write',
        'enum': 'WavesCorrectionState',
        'name': 'WAVES_RESULTS_CORRECTION_STATE',
        'type': 'int32'
    },
    13639701: {
        'access': 'read-write',
        'enum': 'WavesGroupDelayApertureMode',
        'name': 'WAVES_GROUP_DELAY_APERTURE_MODE',
        'type': 'int32'
    },
    13639702: {
        'access': 'read-write',
        'name': 'WAVES_GROUP_DELAY_APERTURE_POINTS',
        'type': 'float64'
    },
    13639703: {
        'access': 'read-write',
        'name': 'WAVES_GROUP_DELAY_APERTURE_PERCENTAGE',
        'type': 'float64'
    },
    13639704: {
        'access': 'read-write',
        'name': 'WAVES_GROUP_DELAY_APERTURE_FREQUENCY_SPAN',
        'type': 'float64'
    },
    13639705: {
        'access': 'read-write',
        'name': 'WAVES_RESULTS_CORRECTION_LEVEL',
        'type': 'char[]'
    },
    13680640: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/attributes_addon.py sha256=2bf9a11cabca22e1871143e397bbd88deb958fbfdd9ea5b0918bfb2f9124a164 bytes=203 -->
## FILE: source/codegen/metadata/nirfmxvna/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/attributes_addon.py`
- sha256: `2bf9a11cabca22e1871143e397bbd88deb958fbfdd9ea5b0918bfb2f9124a164`
- bytes: 203

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxvna/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/config.py sha256=637394dadd313244df498c4dc69c5abf2388be87c3e6c9cb21886fe62179982d bytes=1962 -->
## FILE: source/codegen/metadata/nirfmxvna/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/config.py`
- sha256: `637394dadd313244df498c4dc69c5abf2388be87c3e6c9cb21886fe62179982d`
- bytes: 1962

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxVNA.h',
    'c_function_prefix': 'RFmxVNA_',
    'service_class_prefix': 'NiRFmxVNA',
    'java_package': 'com.ni.grpc.nirfmxvna',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxVNA',
    'namespace_component': 'nirfmxvna',
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
    'driver_name': 'NI-rfmxvna',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxvna',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxVNA.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxVNA.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxvna',
    'session_class_description': 'An NI-RFmxVNA instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxvna/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/enums.py sha256=f213279ea678db5eb02dda26b1363d2bdcdf3974600a0bcd08112baa8446555a bytes=29904 -->
## FILE: source/codegen/metadata/nirfmxvna/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/enums.py`
- sha256: `f213279ea678db5eb02dda26b1363d2bdcdf3974600a0bcd08112baa8446555a`
- bytes: 29904

````python
enums = {
    'AutoIFBandwidthScalingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CalErrorTerm': {
        'values': [
            {
                'name': 'DIRECTIVITY',
                'value': 0
            },
            {
                'name': 'SOURCE_MATCH',
                'value': 1
            },
            {
                'name': 'REFLECTION_TRACKING',
                'value': 2
            },
            {
                'name': 'TRANSMISSION_TRACKING',
                'value': 3
            },
            {
                'name': 'LOAD_MATCH',
                'value': 4
            },
            {
                'name': 'K',
                'value': 5
            },
            {
                'name': 'ALPHA',
                'value': 6
            },
            {
                'name': 'BETA',
                'value': 7
            },
            {
                'name': 'GAMMA',
                'value': 8
            },
            {
                'name': 'DELTA',
                'value': 9
            },
            {
                'name': 'SWITCH_TERM',
                'value': 10
            }
        ]
    },
    'CalFrequencyGrid': {
        'values': [
            {
                'name': 'DIRECTIVITY',
                'value': 0
            },
            {
                'name': 'SOURCE_MATCH',
                'value': 1
            },
            {
                'name': 'REFLECTION_TRACKING',
                'value': 2
            },
            {
                'name': 'TRANSMISSION_TRACKING',
                'value': 3
            },
            {
                'name': 'LOAD_MATCH',
                'value': 4
            },
            {
                'name': 'K',
                'value': 5
            },
            {
                'name': 'ALPHA',
                'value': 6
            },
            {
                'name': 'BETA',
                'value': 7
            },
            {
                'name': 'GAMMA',
                'value': 8
            },
            {
                'name': 'DELTA',
                'value': 9
            },
            {
                'name': 'SWITCH_TERM',
                'value': 10
            }
        ]
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability': {
        'values': [
            {
                'name': 'ESTIMATE',
                'value': 0
            },
            {
                'name': 'KNOWN',
                'value': 1
            }
        ]
    },
    'CalkitManagerCalkitCalibrationElementReflectModelType': {
        'values': [
            {
                'name': 'REFLECT_OPEN',
                'value': 0
            },
            {
                'name': 'REFLECT_SHORT',
                'value': 1
            },
            {
                'name': 'LOAD',
                'value': 2
            }
        ]
    },
    'CalkitManagerCalkitCalibrationElementSParameterAvailability': {
        'values': [
            {
                'name': 'ESTIMATE',
                'value': 0
            },
            {
                'name': 'KNOWN',
                'value': 1
            }
        ]
    },
    'CalkitManagerCalkitCalibrationElementSParameterDefinition': {
        'values': [
            {
                'name': 'REFLECT_MODEL',
                'value': 0
            },
            {
                'name': 'SPARAMETER',
                'value': 1
            },
            {
                'name': 'DELAY_MODEL',
                'value': 2
            },
            {
                'name': 'UNKNOWN',
                'value': 3
            }
        ]
    },
    'CalkitManagerCalkitCalibrationElementType': {
        'values': [
            {
                'name': 'LOAD',
                'value': 0
            },
            {
                'name': 'OPEN',
                'value': 1
            },
            {
                'name': 'SHORT',
                'value': 2
            },
            {
                'name': 'THRU',
                'value': 3
            },
            {
                'name': 'LINE',
                'value': 4
            },
            {
                'name': 'REFLECT',
                'value': 5
            },
            {
                'name': 'TERMINATION',
                'value': 6
            }
        ]
    },
    'CalkitManagerCalkitConnectorGender': {
        'values': [
            {
                'name': 'MALE',
                'value': 0
            },
            {
                'name': 'FEMALE',
                'value': 1
            },
            {
                'name': 'NO_GENDER',
                'value': 2
            }
        ]
    },
    'CalkitManagerCalkitTrlReferencePlane': {
        'values': [
            {
                'name': 'THRU',
                'value': 0
            },
            {
                'name': 'REFLECT',
                'value': 1
            }
        ]
    },
    'CorrectionCalibrationCalkitType': {
        'values': [
            {
                'name': 'ELECTRONIC',
                'value': 0
            },
            {
                'name': 'MECHANICAL',
                'value': 1
            }
        ]
    },
    'CorrectionCalibrationMethod': {
        'values': [
            {
                'name': 'SOL',
                'value': 0
            },
            {
                'name': 'SOLT',
                'value': 1
            },
            {
                'name': 'TRL',
                'value': 2
            }
        ]
    },
    'CorrectionCalibrationThruMethod': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'DEFINED_THRU',
                'value': 1
            },
            {
                'name': 'FLUSH_THRU',
                'value': 2
            },
            {
                'name': 'UNDEFINED_THRU',
                'value': 3
            },
            {
                'name': 'VCAL_THRU_AS_UNKNOWN_THRU',
                'value': 5
            }
        ]
    },
    'CorrectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionInterpolationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionAutoFrequencyMode': {
        'values': [
            {
                'name': 'SWEEP',
                'value': 0
            },
            {
                'name': 'USER',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionAutoLossEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionAutoRegularizationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionAutoStandard': {
        'values': [
            {
                'name': 'OPEN',
                'value': 0
            },
            {
                'name': 'SHORT',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionDCLossEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionDelayDomain': {
        'values': [
            {
                'name': 'DELAY',
                'value': 0
            },
            {
                'name': 'DISTANCE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionDistanceUnit': {
        'values': [
            {
                'name': 'METERS',
                'value': 0
            },
            {
                'name': 'FEET',
                'value': 1
            },
            {
                'name': 'INCHES',
                'value': 2
            }
        ]
    },
    'CorrectionPortExtensionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionLoss1Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortExtensionLoss2Enabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionPortSubsetEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CorrectionSwitchPortsMultipathCalibration': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'DISABLED',
                'value': 1
            },
            {
                'name': 'ENABLED',
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
    'IQCorrectionState': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'CORRECTED',
                'value': 1
            },
            {
                'name': 'INTERPOLATED',
                'value': 2
            },
            {
                'name': 'SETTINGS_MODIFIED',
                'value': 3
            }
        ]
    },
    'IndexEventLevel': {
        'values': [
            {
                'name': 'ACTIVE_HIGH',
                'value': 0
            },
            {
                'name': 'ACTIVE_LOW',
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
            }
        ]
    },
    'MarkerMode': {
        'values': [
            {
                'name': 'CONTINUOUS',
                'value': 0
            },
            {
                'name': 'DISCRETE',
                'value': 1
            }
        ]
    },
    'MarkerPeakSearchExcursionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MarkerPeakSearchThresholdEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'MarkerSearchMode': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'MAX',
                'value': 1
            },
            {
                'name': 'MIN',
                'value': 2
            },
            {
                'name': 'PEAK',
                'value': 3
            },
            {
                'name': 'NEXT_PEAK',
                'value': 4
            },
            {
                'name': 'NEXT_LEFT_PEAK',
                'value': 5
            },
            {
                'name': 'NEXT_RIGHT_PEAK',
                'value': 6
            },
            {
                'name': 'TARGET',
                'value': 7
            },
            {
                'name': 'NEXT_LEFT_TARGET',
                'value': 8
            },
            {
                'name': 'NEXT_RIGHT_TARGET',
                'value': 9
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
                'value': 2
            },
            {
                'name': 'FIXED',
                'value': 3
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'SPARAMS',
                'value': 1
            },
            {
                'name': 'WAVES',
                'value': 2
            },
            {
                'name': 'IQ',
                'value': 4
            },
            {
                'name': 'INTEGRATEDPOWER',
                'value': 8
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
    'PulseAcquisitionAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PulseDigitalEdgeTriggerSource': {
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
            }
        ]
    },
    'PulseGeneratorEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PulseModeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PulseTriggerType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'DIGITAL_EDGE',
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
    'ReadyForTriggerEventLevel': {
        'values': [
            {
                'name': 'ACTIVE_HIGH',
                'value': 0
            },
            {
                'name': 'ACTIVE_LOW',
                'value': 1
            }
        ]
    },
    'RestoreConfiguration': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'STIMULUS',
                'value': 1
            }
        ]
    },
    'SParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_VNA',
                'value': 0
            },
            {
                'name': 'PORT2_TOWARDS_VNA',
                'value': 1
            }
        ]
    },
    'SParamsCorrectionState': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'CORRECTED',
                'value': 1
            },
            {
                'name': 'INTERPOLATED',
                'value': 2
            },
            {
                'name': 'SETTINGS_MODIFIED',
                'value': 3
            }
        ]
    },
    'SParamsFormat': {
        'values': [
            {
                'name': 'MAGNITUDE',
                'value': 0
            },
            {
                'name': 'PHASE',
                'value': 1
            },
            {
                'name': 'COMPLEX',
                'value': 2
            },
            {
                'name': 'SWR',
                'value': 3
            },
            {
                'name': 'SMITH_IMPEDANCE',
                'value': 4
            },
            {
                'name': 'SMITH_ADMITTANCE',
                'value': 5
            },
            {
                'name': 'POLAR',
                'value': 6
            },
            {
                'name': 'GROUP_DELAY',
                'value': 7
            }
        ]
    },
    'SParamsGroupDelayApertureMode': {
        'values': [
            {
                'name': 'POINTS',
                'value': 0
            },
            {
                'name': 'PERCENTAGE',
                'value': 1
            },
            {
                'name': 'FREQUENCY_SPAN',
                'value': 2
            }
        ]
    },
    'SParamsMagnitudeUnits': {
        'values': [
            {
                'name': 'DB',
                'value': 0
            },
            {
                'name': 'LINEAR',
                'value': 1
            }
        ]
    },
    'SParamsMathFunction': {
        'values': [
            {
                'name': 'OFF',
                'value': 0
            },
            {
                'name': 'ADD',
                'value': 1
            },
            {
                'name': 'SUBTRACT',
                'value': 2
            },
            {
                'name': 'MULTIPLY',
                'value': 3
            },
            {
                'name': 'DIVIDE',
                'value': 4
            }
        ]
    },
    'SParamsPhaseTraceType': {
        'values': [
            {
                'name': 'WRAPPED',
                'value': 0
            },
            {
                'name': 'UNWRAPPED',
                'value': 1
            }
        ]
    },
    'SParamsSnPDataFormat': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'LOG_MAGNITUDE_ANGLE',
                'value': 1
            },
            {
                'name': 'REAL_IMAGINARY',
                'value': 2
            },
            {
                'name': 'LINEAR_MAGNITUDE_ANGLE',
                'value': 3
            }
        ]
    },
    'SegmentDwellTimeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SegmentEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SegmentIFBandwidthEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SegmentPowerLevelEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SegmentTestReceiverAttenuationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SourcePowerMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'OFF',
                'value': 1
            }
        ]
    },
    'SweepSequence': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'POINT',
                'value': 1
            }
        ]
    },
    'SweepType': {
        'values': [
            {
                'name': 'LIST',
                'value': 0
            },
            {
                'name': 'LINEAR',
                'value': 1
            },
            {
                'name': 'SEGMENT',
                'value': 2
            },
            {
                'name': 'CW_TIME',
                'value': 4
            }
        ]
    },
    'TriggerMode': {
        'values': [
            {
                'name': 'SIGNAL',
                'value': 0
            },
            {
                'name': 'SWEEP',
                'value': 1
            },
            {
                'name': 'POINT',
                'value': 2
            },
            {
                'name': 'SEGMENT',
                'value': 3
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
                'name': 'SOFTWARE',
                'value': 2
            }
        ]
    },
    'WavesCorrectionState': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'CORRECTED',
                'value': 1
            },
            {
                'name': 'INTERPOLATED',
                'value': 2
            },
            {
                'name': 'SETTINGS_MODIFIED',
                'value': 3
            }
        ]
    },
    'WavesFormat': {
        'values': [
            {
                'name': 'MAGNITUDE',
                'value': 0
            },
            {
                'name': 'PHASE',
                'value': 1
            },
            {
                'name': 'COMPLEX',
                'value': 2
            },
            {
                'name': 'SWR',
                'value': 3
            },
            {
                'name': 'SMITH_IMPEDANCE',
                'value': 4
            },
            {
                'name': 'SMITH_ADMITTANCE',
                'value': 5
            },
            {
                'name': 'POLAR',
                'value': 6
            },
            {
                'name': 'GROUP_DELAY',
                'value': 7
            }
        ]
    },
    'WavesGroupDelayApertureMode': {
        'values': [
            {
                'name': 'POINTS',
                'value': 0
            },
            {
                'name': 'PERCENTAGE',
                'value': 1
            },
            {
                'name': 'FREQUENCY_SPAN',
                'value': 2
            }
        ]
    },
    'WavesMagnitudeUnits': {
        'values': [
            {
                'name': 'DBM',
                'value': 0
            },
            {
                'name': 'DBMV',
                'value': 1
            },
            {
                'name': 'DBUV',
                'value': 2
            },
            {
                'name': 'DBMA',
                'value': 3
            },
            {
                'name': 'W',
                'value': 4
            },
            {
                'name': 'V',
                'value': 5
            },
            {
                'name': 'A',
                'value': 6
            }
        ]
    },
    'WavesPhaseTraceType': {
        'values': [
            {
                'name': 'WRAPPED',
                'value': 0
            },
            {
                'name': 'UNWRAPPED',
                'value': 1
            }
        ]
    },
    'WavesReceiver': {
        'values': [
            {
                'name': 'TEST',
                'value': 0
            },
            {
                'name': 'REFERENCE',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/enums_addon.py sha256=67149519d49e2a7016bdc78ff16db650e492f9f02b68d8941d7876f3f3d43b18 bytes=188 -->
## FILE: source/codegen/metadata/nirfmxvna/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/enums_addon.py`
- sha256: `67149519d49e2a7016bdc78ff16db650e492f9f02b68d8941d7876f3f3d43b18`
- bytes: 188

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/functions.py sha256=a5de98e240170d4100b1568463d504f0a8e98e42897235d668ff268dc70cc89f bytes=188651 -->
## FILE: source/codegen/metadata/nirfmxvna/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/functions.py`
- sha256: `a5de98e240170d4100b1568463d504f0a8e98e42897235d668ff268dc70cc89f`
- bytes: 188651

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
    'AutoDetectvCalOrientation': {
        'parameters': [
            {
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
    'AutoPortExtensionMeasure': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CorrectionPortExtensionAutoStandard',
                'name': 'standard',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'port',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'AutoPortExtensionReset': {
        'parameters': [
            {
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
    'BuildCalibrationElementString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calibrationElementID',
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
    'BuildCalkitString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitID',
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
    'BuildCalstepString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calstepNumber',
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
    'BuildConnectorString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'connectorID',
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
    'BuildMarkerString': {
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
    'BuildPortString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'portString',
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
    'BuildPulseGeneratorString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'pulseGeneratorNumber',
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
    'BuildSParameterString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sParameterNumber',
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
    'BuildWaveString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveNumber',
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
    'CalibrationAbort': {
        'parameters': [
            {
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
    'CalibrationAcquire': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
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
    'CalibrationInitiate': {
        'parameters': [
            {
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
    'CalibrationSave': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitAddCalibrationElement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calibrationElementID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitAddConnector': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'connectorID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementDelayModelGetDelay': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'delay',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementDelayModelSetDelay': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'delay',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetMaximumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'maximumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetMinimumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'minimumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetPortConnectors': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'grpc_name': 'connector_ids',
                'name': 'connectorIDs',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetSParameterDefinition': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitCalibrationElementSParameterDefinition',
                'name': 'sParameterDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementGetTypes': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitCalibrationElementType',
                'name': 'calibrationElementTypes',
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
    'CalkitManagerCalkitCalibrationElementReflectModelGetC0': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'c0',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetC1': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'c1',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetC2': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'c2',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetC3': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'c3',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetModelType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitCalibrationElementReflectModelType',
                'name': 'modelType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetOffsetDelay': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'offsetDelay',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetOffsetLoss': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'offsetLoss',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetOffsetZ0': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'offsetZ0',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetReferenceImpedance': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'referenceImpedance',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelGetSParamAvailability': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability',
                'name': 'sParameterAvailability',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetC0': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'c0',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetC1': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'c1',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetC2': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'c2',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetC3': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'c3',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetModelType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitCalibrationElementReflectModelType',
                'name': 'modelType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetOffsetDelay': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetDelay',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetOffsetLoss': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetLoss',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetOffsetZ0': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetZ0',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetReferenceImpedance': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'referenceImpedance',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementReflectModelSetSParamAvailability': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitCalibrationElementReflectModelSParameterAvailability',
                'name': 'sParameterAvailability',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterGetFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS11': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's11',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS11InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS11',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's11',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s11)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterGetS11Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's11I',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 's11Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS12': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's12',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS12InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS12',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's12',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s12)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterGetS12Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's12I',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 's12Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS21': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's21',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS21InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS21',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's21',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s21)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterGetS21Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's21I',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 's21Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS22': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's22',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetS22InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterGetS22',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's22',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s22)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterGetS22Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 's22I',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 's22Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterGetSParamAvailability': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitCalibrationElementSParameterAvailability',
                'name': 'sParameterAvailability',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterSetFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'fileName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSParameterSetS11': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's11',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS11InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS11',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's11',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s11)'
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS11Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's11I',
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
                'name': 's11Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS12': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's12',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS12InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS12',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's12',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s12)'
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS12Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's12I',
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
                'name': 's12Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS21': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's21',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS21InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS21',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's21',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s21)'
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS21Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's21I',
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
                'name': 's21Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS22': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's22',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS22InterleavedIQ': {
        'cname': 'RFmxVNA_CalkitManagerCalkitCalibrationElementSParameterSetS22',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's22',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexDouble*>(s22)'
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
    'CalkitManagerCalkitCalibrationElementSParameterSetS22Split': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 's22I',
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
                'name': 's22Q',
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
    'CalkitManagerCalkitCalibrationElementSParameterSetSParamAvailability': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitCalibrationElementSParameterAvailability',
                'name': 'sParameterAvailability',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CalkitManagerCalkitCalibrationElementSetMaximumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'maximumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSetMinimumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'minimumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSetPortConnectors': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_name': 'connector_ids',
                'name': 'connectorIDs',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSetSParameterDefinition': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitCalibrationElementSParameterDefinition',
                'name': 'sParameterDefinition',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitCalibrationElementSetTypes': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitCalibrationElementType',
                'name': 'calibrationElementTypes',
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
    'CalkitManagerCalkitConnectorGetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorGetGender': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitConnectorGender',
                'name': 'connectorGender',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorGetImpedance': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'impedance',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorGetMaximumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'maximumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorGetMinimumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'minimumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorGetType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'connectorType',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorSetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CalkitManagerCalkitConnectorSetGender': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitConnectorGender',
                'name': 'connectorGender',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorSetImpedance': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'impedance',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorSetMaximumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'maximumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorSetMinimumFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'minimumFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitConnectorSetType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'connectorType',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetCalibrationElementIDs': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'grpc_name': 'calibration_element_ids',
                'name': 'calibrationElementIDs',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetConnectorIDs': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'grpc_name': 'connector_ids',
                'name': 'connectorIDs',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'calkitDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetLRLLineAutoChar': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'autoCharacterizationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetTRLReferencePlane': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'enum': 'CalkitManagerCalkitTrlReferencePlane',
                'name': 'referencePlane',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitGetVersion': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'calkitVersion',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitRemoveCalibrationElement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calibrationElementID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitRemoveConnector': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'connectorID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitSetDescription': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitDescription',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitSetLRLLineAutoChar': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'autoCharacterizationEnabled',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitSetTRLReferencePlane': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalkitManagerCalkitTrlReferencePlane',
                'name': 'referencePlane',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCalkitSetVersion': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitVersion',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerCreateCalkit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerExportCalkit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitID',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitFilePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerGetCalkitIDs': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'grpc_name': 'calkit_ids',
                'name': 'calkitIDs',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerImportCalkit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitFilePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerRemoveCalkit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalkitManagerValidateCalkit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calkitID',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalsetEmbedFixtureS2p': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'fixtureS2pFilePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'vnaPort',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'SParameterOrientation',
                'name': 'sParameterOrientation',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'newCalsetName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalsetGetErrorTerm': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalErrorTerm',
                'name': 'errorTermIdentifier',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementPort',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sourcePort',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'errorTerm',
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
    'CalsetGetErrorTermInterleavedIQ': {
        'cname': 'RFmxVNA_CalsetGetErrorTerm',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalErrorTerm',
                'name': 'errorTermIdentifier',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementPort',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sourcePort',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'errorTerm',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(errorTerm)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CalsetGetErrorTermSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalErrorTerm',
                'name': 'errorTermIdentifier',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'measurementPort',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sourcePort',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'errorTermI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'errorTermQ',
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
    'CalsetGetFrequencyGrid': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CalFrequencyGrid',
                'name': 'errorTermIdentifier',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'frequencyGrid',
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
    'CalsetLoadFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetFilePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CalsetSaveToFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetFilePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgCorrectionPortSubset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'portSubset',
                'type': 'char[]'
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
    'ClearCalset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'ClearMeasurementMemoryNames': {
        'parameters': [
            {
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
    'CopyCalset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sourceCalsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'newCalsetName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CopyDataToMeasurementMemory': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementMemoryName',
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
    'DeselectActiveCalset': {
        'parameters': [
            {
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
    'GetAllCalsetNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'calsetNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
    'GetMeasurementMemoryNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'measurementMemoryNames',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetMeasurementMemoryXData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'measurementMemoryX',
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
    'GetMeasurementMemoryYData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'measurementMemoryY1',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'measurementMemoryY2',
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
            }
        ],
        'returns': 'int32'
    },
    'IQFetchDataInterleavedIQ': {
        'cname': 'RFmxVNA_IQFetchData',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
            }
        ],
        'returns': 'int32'
    },
    'Initialize': {
        'custom_close': 'Close(id, RFMXVNA_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXVNA_VAL_FALSE)',
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
    'LoadDataToMeasurementMemoryFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'parameter',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementMemoryName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgDataSource': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'dataSource',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MarkerMode',
                'name': 'markerMode',
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
    'MarkerCfgPeakSearchExcursion': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MarkerPeakSearchExcursionEnabled',
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
    'MarkerCfgPeakSearchThreshold': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MarkerPeakSearchThresholdEnabled',
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
    'MarkerCfgTargetValue': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'targetValue',
                'type': 'float64'
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
    'MarkerCfgX': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'markerX',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerCfgY': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'markerY1',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'markerY2',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerFetchX': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'markerX',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerFetchY': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
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
                'name': 'markerY1',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'markerY2',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'MarkerSearch': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MarkerSearchMode',
                'name': 'searchMode',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
    'SParamsCfgSParameter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'sParameter',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SParamsExportToSnPFile': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'snpFilePath',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SParamsFetchXData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x',
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
    'SParamsFetchYData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'y1',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'y2',
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
    'SParamsGetSParameter': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'sParameter',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SelectActiveCalset': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'calsetName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'RestoreConfiguration',
                'name': 'restoreConfiguration',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
                'grpc_type': 'NiRFmxVNAAttribute',
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
    },
    'WavesCfgWave': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'wave',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'WavesFetchXData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x',
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
    'WavesFetchYData': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'y1',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'y2',
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
    'WavesGetWave': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'wave',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxvna/functions_addon.py sha256=2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679 bytes=34 -->
## FILE: source/codegen/metadata/nirfmxvna/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxvna/functions_addon.py`
- sha256: `2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679`
- bytes: 34

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxwcdma/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/attributes.py sha256=68419b874b1aa6834b32f59fb6eb4e0d6caa7145e9ae7ed4cb8e8305965bc3aa bytes=37461 -->
## FILE: source/codegen/metadata/nirfmxwcdma/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/attributes.py`
- sha256: `68419b874b1aa6834b32f59fb6eb4e0d6caa7145e9ae7ed4cb8e8305965bc3aa`
- bytes: 37461

````python
attributes = {
    5242881: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    5242882: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    5242883: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    5242884: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    5242885: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    5242886: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    5242887: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    5242888: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    5242889: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    5242890: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    5242891: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    5242892: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    5242893: {
        'access': 'read-write',
        'enum': 'LinkDirection',
        'name': 'LINK_DIRECTION',
        'type': 'int32'
    },
    5242894: {
        'access': 'read-write',
        'name': 'NUMBER_OF_CARRIERS',
        'type': 'int32'
    },
    5242895: {
        'access': 'read-write',
        'name': 'CARRIER_FREQUENCY',
        'type': 'float64'
    },
    5242896: {
        'access': 'read-write',
        'enum': 'ChannelConfigurationMode',
        'name': 'CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    5242900: {
        'access': 'read-write',
        'name': 'NUMBER_OF_CHANNELS',
        'type': 'int32'
    },
    5242901: {
        'access': 'read-write',
        'name': 'SPREADING_FACTOR',
        'type': 'int32'
    },
    5242902: {
        'access': 'read-write',
        'name': 'SPREADING_CODE',
        'type': 'int32'
    },
    5242903: {
        'access': 'read-write',
        'enum': 'ModulationType',
        'name': 'MODULATION_TYPE',
        'type': 'int32'
    },
    5242904: {
        'access': 'read-write',
        'enum': 'Branch',
        'name': 'BRANCH',
        'type': 'int32'
    },
    5242905: {
        'access': 'read-write',
        'enum': 'UplinkTestModel',
        'name': 'UPLINK_TEST_MODEL',
        'type': 'int32'
    },
    5242906: {
        'access': 'read-write',
        'enum': 'DownlinkTestModel',
        'name': 'DOWNLINK_TEST_MODEL',
        'type': 'int32'
    },
    5242907: {
        'access': 'read-write',
        'enum': 'UplinkScramblingType',
        'name': 'UPLINK_SCRAMBLING_TYPE',
        'type': 'int32'
    },
    5242908: {
        'access': 'read-write',
        'name': 'UPLINK_SCRAMBLING_CODE',
        'type': 'int32'
    },
    5242909: {
        'access': 'read-write',
        'enum': 'DownlinkScramblingType',
        'name': 'DOWNLINK_SCRAMBLING_TYPE',
        'type': 'int32'
    },
    5242910: {
        'access': 'read-write',
        'name': 'DOWNLINK_SCRAMBLING_PRIMARY_CODE',
        'type': 'int32'
    },
    5242911: {
        'access': 'read-write',
        'name': 'DOWNLINK_SCRAMBLING_SECONDARY_CODE',
        'type': 'int32'
    },
    5242912: {
        'access': 'read-write',
        'name': 'BAND',
        'type': 'int32'
    },
    5246972: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    5246973: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    5246975: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    5246976: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5246981: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    5246984: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    5246986: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    5246988: {
        'access': 'read-write',
        'enum': 'AcpOffsetPowerReferenceCarrier',
        'name': 'ACP_OFFSET_POWER_REFERENCE_CARRIER',
        'type': 'int32'
    },
    5246989: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_POWER_REFERENCE_SPECIFIC',
        'type': 'int32'
    },
    5246990: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    5246994: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    5246996: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    5246997: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    5246998: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    5247000: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    5247003: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    5247004: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    5247005: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    5247006: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    5247007: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    5247008: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    5247009: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5247010: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    5247014: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5247015: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    5247020: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5247021: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    5247026: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5247027: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    5247028: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    5247029: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    5247030: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    5247032: {
        'access': 'read-write',
        'enum': 'AcpAmplitudeCorrectionType',
        'name': 'ACP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    5247033: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    5247034: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    5247035: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    5255168: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5255170: {
        'access': 'read-write',
        'name': 'CHP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    5255171: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    5255174: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    5255175: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    5255177: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    5255180: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    5255181: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    5255182: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    5255185: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    5255186: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    5255188: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5255189: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5255192: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    5255193: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_RELATIVE_POWER',
        'type': 'float64'
    },
    5255195: {
        'access': 'read-write',
        'enum': 'ChpAmplitudeCorrectionType',
        'name': 'CHP_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    5267456: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5267459: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    5267460: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    5267462: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    5267463: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    5267465: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    5267468: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    5267469: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    5267470: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    5267471: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    5267472: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    5267474: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5267475: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    5267476: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5267477: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    5267478: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    5267482: {
        'access': 'read-write',
        'enum': 'ObwAmplitudeCorrectionType',
        'name': 'OBW_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    5275648: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5275653: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    5275659: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    5275660: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    5275668: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    5275669: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    5275671: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    5275672: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    5275677: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    5275678: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    5275679: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    5275681: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    5275685: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    5275686: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    5275687: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5275688: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_TOTAL_CARRIER_POWER',
        'type': 'float64'
    },
    5275689: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    5275693: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275694: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275695: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    5275696: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_PEAK_FREQUENCY',
        'type': 'float64'
    },
    5275700: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275701: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275702: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    5275703: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    5275704: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    5275705: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    5275706: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5275707: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    5275708: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    5275709: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    5275713: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275714: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    5275715: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    5275716: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    5275717: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    5275718: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    5275719: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    5275720: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    5275721: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    5275722: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    5275724: {
        'access': 'read-write',
        'enum': 'SemAmplitudeCorrectionType',
        'name': 'SEM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    5292032: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    5296128: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    5296129: {
        'access': 'read-write',
        'enum': 'TransmitterArchitecture',
        'name': 'TRANSMITTER_ARCHITECTURE',
        'type': 'int32'
    },
    5296131: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    5312512: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5312514: {
        'access': 'read-write',
        'enum': 'ModAccSynchronizationMode',
        'name': 'MODACC_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    5312515: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    5312516: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    5312517: {
        'access': 'read-write',
        'enum': 'ModAccSpectrumInverted',
        'name': 'MODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    5312518: {
        'access': 'read-write',
        'enum': 'ModAccIQOffsetRemovalEnabled',
        'name': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5312519: {
        'access': 'read-write',
        'enum': 'ModAccTransientRemovalEnabled',
        'name': 'MODACC_TRANSIENT_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5312520: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5312521: {
        'access': 'read-write',
        'name': 'MODACC_DOWNLINK_TIMING_CHANNEL_SPREADING_FACTOR',
        'type': 'int32'
    },
    5312522: {
        'access': 'read-write',
        'name': 'MODACC_DOWNLINK_TIMING_CHANNEL_CODE',
        'type': 'int32'
    },
    5312529: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_EVM',
        'type': 'float64'
    },
    5312530: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_EVM',
        'type': 'float64'
    },
    5312531: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    5312532: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_PHASE_ERROR',
        'type': 'float64'
    },
    5312533: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RHO',
        'type': 'float64'
    },
    5312534: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    5312535: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_FREQUENCY_ERROR',
        'type': 'float64'
    },
    5312536: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    5312537: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_CDE',
        'type': 'float64'
    },
    5312539: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_CDE_CODE',
        'type': 'int32'
    },
    5312540: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE',
        'type': 'float64'
    },
    5312541: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_SPREADING_FACTOR',
        'type': 'int32'
    },
    5312542: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_CODE',
        'type': 'int32'
    },
    5312543: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PSCH_POWER',
        'type': 'float64'
    },
    5312544: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SSCH_POWER',
        'type': 'float64'
    },
    5312545: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DPCH_TIMING_OFFSET',
        'type': 'float64'
    },
    5312546: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RCDE',
        'type': 'float64'
    },
    5312547: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RCDE_SPREADING_FACTOR',
        'type': 'int32'
    },
    5312548: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RCDE_CODE',
        'type': 'int32'
    },
    5312549: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS',
        'type': 'int32'
    },
    5312550: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_SPREADING_FACTOR',
        'type': 'int32'
    },
    5312551: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_SPREADING_CODE',
        'type': 'int32'
    },
    5312552: {
        'access': 'read-write',
        'enum': 'ModAccDetectedModulationType',
        'name': 'MODACC_RESULTS_DETECTED_MODULATION_TYPE',
        'type': 'int32'
    },
    5312553: {
        'access': 'read-write',
        'enum': 'ModAccDetectedBranch',
        'name': 'MODACC_RESULTS_DETECTED_BRANCH',
        'type': 'int32'
    },
    5312554: {
        'access': 'read-write',
        'enum': 'ModAccPeakCdeBranch',
        'name': 'MODACC_RESULTS_PEAK_CDE_BRANCH',
        'type': 'int32'
    },
    5312555: {
        'access': 'read-write',
        'enum': 'ModAccPeakActiveCdeBranch',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH',
        'type': 'int32'
    },
    5312556: {
        'access': 'read-write',
        'enum': 'ModAccPeakRcdeBranch',
        'name': 'MODACC_RESULTS_PEAK_RCDE_BRANCH',
        'type': 'int32'
    },
    5312557: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    5312558: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    5312559: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MULTI_CARRIER_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    5312571: {
        'access': 'read-write',
        'enum': 'ModAccRrcFilterEnabled',
        'name': 'MODACC_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    5312572: {
        'access': 'read-write',
        'enum': 'ModAccIQGainImbalanceRemovalEnabled',
        'name': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5312573: {
        'access': 'read-write',
        'enum': 'ModAccIQQuadratureErrorRemovalEnabled',
        'name': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5316608: {
        'access': 'read-write',
        'name': 'QEVM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5316611: {
        'access': 'read-write',
        'name': 'QEVM_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    5316613: {
        'access': 'read-write',
        'enum': 'QevmAveragingEnabled',
        'name': 'QEVM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    5316614: {
        'access': 'read-write',
        'name': 'QEVM_AVERAGING_COUNT',
        'type': 'int32'
    },
    5316615: {
        'access': 'read-write',
        'enum': 'QevmSpectrumInverted',
        'name': 'QEVM_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    5316616: {
        'access': 'read-write',
        'enum': 'QevmIQOffsetRemovalEnabled',
        'name': 'QEVM_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5316619: {
        'access': 'read-write',
        'enum': 'QevmRrcFilterEnabled',
        'name': 'QEVM_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    5316620: {
        'access': 'read-write',
        'name': 'QEVM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5316621: {
        'access': 'read-write',
        'name': 'QEVM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    5316622: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_RMS_EVM',
        'type': 'float64'
    },
    5316623: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_RMS_EVM',
        'type': 'float64'
    },
    5316624: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_PEAK_EVM',
        'type': 'float64'
    },
    5316625: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_PEAK_EVM',
        'type': 'float64'
    },
    5316626: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    5316627: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    5316628: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_PHASE_ERROR',
        'type': 'float64'
    },
    5316629: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_PHASE_ERROR',
        'type': 'float64'
    },
    5316630: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_FREQUENCY_ERROR',
        'type': 'float64'
    },
    5316631: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR',
        'type': 'float64'
    },
    5316632: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    5316633: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    5316634: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    5316635: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    5324800: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5324802: {
        'access': 'read-write',
        'enum': 'SlotPhaseSynchronizationMode',
        'name': 'SLOTPHASE_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    5324803: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    5324804: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    5324807: {
        'access': 'read-write',
        'enum': 'SlotPhaseSpectrumInverted',
        'name': 'SLOTPHASE_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    5324808: {
        'access': 'read-write',
        'enum': 'SlotPhaseTransientRemovalEnabled',
        'name': 'SLOTPHASE_TRANSIENT_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5324809: {
        'access': 'read-write',
        'enum': 'SlotPhaseRrcFilterEnabled',
        'name': 'SLOTPHASE_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    5324812: {
        'access': 'read-write',
        'name': 'SLOTPHASE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5324814: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY',
        'type': 'float64'
    },
    5324815: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT1',
        'type': 'int32'
    },
    5324816: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_DISCONTINUITY_COUNT_GREATER_THAN_LIMIT2',
        'type': 'int32'
    },
    5324817: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_DISCONTINUITY_MINIMUM_DISTANCE',
        'type': 'int32'
    },
    5328896: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5328898: {
        'access': 'read-write',
        'enum': 'CdaSynchronizationMode',
        'name': 'CDA_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    5328899: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    5328900: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    5328901: {
        'access': 'read-write',
        'enum': 'CdaSpectrumInverted',
        'name': 'CDA_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    5328902: {
        'access': 'read-write',
        'enum': 'CdaIQOffsetRemovalEnabled',
        'name': 'CDA_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    5328903: {
        'access': 'read-write',
        'enum': 'CdaRrcFilterEnabled',
        'name': 'CDA_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    5328905: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_SPREADING_FACTOR',
        'type': 'int32'
    },
    5328906: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_SPREADING_CODE',
        'type': 'int32'
    },
    5328907: {
        'access': 'read-write',
        'enum': 'CdaMeasurementChannelModulationType',
        'name': 'CDA_MEASUREMENT_CHANNEL_MODULATION_TYPE',
        'type': 'int32'
    },
    5328908: {
        'access': 'read-write',
        'enum': 'CdaMeasurementChannelBranch',
        'name': 'CDA_MEASUREMENT_CHANNEL_BRANCH',
        'type': 'int32'
    },
    5328909: {
        'access': 'read-write',
        'enum': 'CdaPowerUnit',
        'name': 'CDA_POWER_UNIT',
        'type': 'int32'
    },
    5328917: {
        'access': 'read-write',
        'name': 'CDA_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    5328919: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_EVM',
        'type': 'float64'
    },
    5328920: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_SYMBOL_EVM',
        'type': 'float64'
    },
    5328921: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    5328922: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR',
        'type': 'float64'
    },
    5328923: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_TOTAL_POWER',
        'type': 'float64'
    },
    5328924: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_SYMBOL_POWER',
        'type': 'float64'
    },
    5328927: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_TOTAL_ACTIVE_POWER',
        'type': 'float64'
    },
    5328929: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_ACTIVE_POWER',
        'type': 'float64'
    },
    5328930: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    5328931: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    5328932: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_INACTIVE_POWER',
        'type': 'float64'
    },
    5328937: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_I_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    5328938: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_Q_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    5328939: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_I_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    5328940: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_Q_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    5328941: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    5332992: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    5332994: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    5332995: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    5332996: {
        'access': 'read-write',
        'enum': 'SlotPowerSpectrumInverted',
        'name': 'SLOTPOWER_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    5332997: {
        'access': 'read-write',
        'enum': 'SlotPowerRrcFilterEnabled',
        'name': 'SLOTPOWER_RRC_FILTER_ENABLED',
        'type': 'int32'
    },
    5332999: {
        'access': 'read-write',
        'enum': 'SlotPowerSynchronizationMode',
        'name': 'SLOTPOWER_SYNCHRONIZATION_MODE',
        'type': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxwcdma/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxwcdma/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/config.py sha256=903e4ff7883d0f5dc4d6f4a4cbc962f7bdd59996bcae5d4d80d4eb74dc15c7b4 bytes=1988 -->
## FILE: source/codegen/metadata/nirfmxwcdma/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/config.py`
- sha256: `903e4ff7883d0f5dc4d6f4a4cbc962f7bdd59996bcae5d4d80d4eb74dc15c7b4`
- bytes: 1988

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.3.0',
    'c_header': 'niRFmxWCDMA.h',
    'c_function_prefix': 'RFmxWCDMA_',
    'service_class_prefix': 'NiRFmxWCDMA',
    'java_package': 'com.ni.grpc.nirfmxwcdma',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxWCDMA',
    'namespace_component': 'nirfmxwcdma',
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
    'driver_name': 'NI-rfmxwcdma',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxwcdma',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxWCDMA.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxWCDMA.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxwcdma',
    'session_class_description': 'An NI-RFmxWCDMA instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxwcdma/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/enums.py sha256=3e5c31f01b02af5f50f71e879b2c100914ec3a79e8a852e2cc3e68ef760c10ae bytes=33033 -->
## FILE: source/codegen/metadata/nirfmxwcdma/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/enums.py`
- sha256: `3e5c31f01b02af5f50f71e879b2c100914ec3a79e8a852e2cc3e68ef760c10ae`
- bytes: 33033

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
                'name': 'MAX',
                'value': 3
            },
            {
                'name': 'MIN',
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
    'Branch': {
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'CdaIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaMeasurementChannelBranch': {
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            }
        ]
    },
    'CdaMeasurementChannelModulationType': {
        'values': [
            {
                'name': 'BPSK_QPSK',
                'value': 0
            },
            {
                'name': '4PAM_16QAM',
                'value': 1
            }
        ]
    },
    'CdaPowerUnit': {
        'values': [
            {
                'name': 'DB',
                'value': 0
            },
            {
                'name': 'DBM',
                'value': 1
            }
        ]
    },
    'CdaRrcFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSynchronizationMode': {
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
                'name': 'ARBITRARY',
                'value': 2
            }
        ]
    },
    'ChannelConfigurationMode': {
        'values': [
            {
                'name': 'AUTO_DETECT',
                'value': 0
            },
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
                'name': 'MAX',
                'value': 3
            },
            {
                'name': 'MIN',
                'value': 4
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
    'DownlinkScramblingType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'LEFT',
                'value': 1
            },
            {
                'name': 'RIGHT',
                'value': 2
            }
        ]
    },
    'DownlinkTestModel': {
        'values': [
            {
                'name': '1_16DPCH',
                'value': 0
            },
            {
                'name': '1_32DPCH',
                'value': 1
            },
            {
                'name': '1_64DPCH',
                'value': 2
            },
            {
                'name': '1_16DPCH_SCCPCH',
                'value': 3
            },
            {
                'name': '1_32DPCH_SCCPCH',
                'value': 4
            },
            {
                'name': '1_64DPCH_SCCPCH',
                'value': 5
            },
            {
                'name': '2',
                'value': 6
            },
            {
                'name': '2_SCCPCH',
                'value': 7
            },
            {
                'name': '3_16DPCH',
                'value': 8
            },
            {
                'name': '3_32DPCH',
                'value': 9
            },
            {
                'name': '3_16DPCH_SCCPCH',
                'value': 10
            },
            {
                'name': '3_32DPCH_SCCPCH',
                'value': 11
            },
            {
                'name': '4',
                'value': 12
            },
            {
                'name': '4_PCPICH',
                'value': 13
            },
            {
                'name': '5_2HSPDSCH_16QAM',
                'value': 14
            },
            {
                'name': '5_4HSPDSCH_4DPCH_16QAM',
                'value': 15
            },
            {
                'name': '5_4HSPDSCH_14DPCH_16QAM',
                'value': 16
            },
            {
                'name': '5_8HSPDSCH_16QAM',
                'value': 17
            },
            {
                'name': '6_4HSPDSCH_64QAM',
                'value': 18
            },
            {
                'name': '6_8HSPDSCH_64QAM',
                'value': 19
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
                'name': 'ACP',
                'value': 2
            },
            {
                'name': 'CHP',
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
                'name': 'QEVM',
                'value': 32
            },
            {
                'name': 'SLOTPHASE',
                'value': 64
            },
            {
                'name': 'CDA',
                'value': 128
            },
            {
                'name': 'SLOTPOWER',
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
    'ModAccDetectedBranch': {
        'enum-value-prefix': 'MODACC_DETECTED_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccDetectedModulationType': {
        'enum-value-prefix': 'MODACC_DETECTED_MODULATION_TYPE',
        'values': [
            {
                'name': 'BPSK_QPSK',
                'value': 0
            },
            {
                'name': '4PAM_16QAM',
                'value': 1
            },
            {
                'name': '64QAM',
                'value': 2
            }
        ]
    },
    'ModAccIQGainImbalanceRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQOffsetRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQQuadratureErrorRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccPeakActiveCdeBranch': {
        'enum-value-prefix': 'MODACC_PEAK_ACTIVE_CDE_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccPeakCdeBranch': {
        'enum-value-prefix': 'MODACC_PEAK_CDE_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccPeakRcdeBranch': {
        'enum-value-prefix': 'MODACC_PEAK_RCDE_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccRrcFilterEnabled': {
        'enum-value-prefix': 'MODACC_RRC_FILTER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
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
                'name': 'ARBITRARY',
                'value': 2
            },
            {
                'name': 'MARKER',
                'value': 3
            }
        ]
    },
    'ModAccTransientRemovalEnabled': {
        'enum-value-prefix': 'MODACC_TRANSIENT_REMOVAL_ENABLED',
        'values': [
            {
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
                'name': 'BPSK_QPSK',
                'value': 0
            },
            {
                'name': '4PAM_16QAM',
                'value': 1
            },
            {
                'name': '64QAM',
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
                'name': 'MAX',
                'value': 3
            },
            {
                'name': 'MIN',
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
    'QevmAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmRrcFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmSpectrumInverted': {
        'values': [
            {
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
                'name': 'MAX',
                'value': 3
            },
            {
                'name': 'MIN',
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
            },
            {
                'name': 'SYNCH_TUNED_4',
                'value': 3
            },
            {
                'name': 'SYNCH_TUNED_5',
                'value': 4
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
    'SlotPhaseRrcFilterEnabled': {
        'values': [
            {
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
    'SlotPhaseTransientRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPowerRrcFilterEnabled': {
        'values': [
            {
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
    'SlotPowerSynchronizationMode': {
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
    'TransmitterArchitecture': {
        'values': [
            {
                'name': 'LO_PER_CARRIER',
                'value': 0
            },
            {
                'name': 'LO_PER_BAND',
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
    'UplinkScramblingType': {
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
    'UplinkTestModel': {
        'values': [
            {
                'name': 'R6C_2_1',
                'value': 0
            },
            {
                'name': 'R6C_2_2',
                'value': 1
            },
            {
                'name': 'R6C_2_3',
                'value': 2
            },
            {
                'name': 'R6C_2_4',
                'value': 3
            },
            {
                'name': 'R6C_2_5',
                'value': 4
            },
            {
                'name': 'R6C_10_1_4_SUBTEST1',
                'value': 5
            },
            {
                'name': 'R6C_10_1_4_SUBTEST2',
                'value': 6
            },
            {
                'name': 'R6C_10_1_4_SUBTEST3',
                'value': 7
            },
            {
                'name': 'R6C_10_1_4_SUBTEST4',
                'value': 8
            },
            {
                'name': 'R6C_10_1_4_SUBTEST5',
                'value': 9
            },
            {
                'name': 'R6C_10_1_4_SUBTEST6',
                'value': 10
            },
            {
                'name': 'R7C_10_1_4_SUBTEST1',
                'value': 11
            },
            {
                'name': 'R7C_10_1_4_SUBTEST2',
                'value': 12
            },
            {
                'name': 'R7C_10_1_4_SUBTEST3',
                'value': 13
            },
            {
                'name': 'R7C_10_1_4_SUBTEST4',
                'value': 14
            },
            {
                'name': 'R7C_11_1_3_SUBTEST1',
                'value': 15
            },
            {
                'name': 'R7C_11_1_3_SUBTEST2',
                'value': 16
            },
            {
                'name': 'R7C_11_1_3_SUBTEST3',
                'value': 17
            },
            {
                'name': 'R7C_11_1_3_SUBTEST4',
                'value': 18
            },
            {
                'name': 'R7C_11_1_3_SUBTEST5',
                'value': 19
            },
            {
                'name': 'R8C_11_1_3_SUBTEST1',
                'value': 20
            },
            {
                'name': 'R8C_11_1_3_SUBTEST2',
                'value': 21
            },
            {
                'name': 'R8C_11_1_3_SUBTEST3',
                'value': 22
            },
            {
                'name': 'R8C_11_1_3_SUBTEST4',
                'value': 23
            },
            {
                'name': 'R8C_11_1_3_SUBTEST5',
                'value': 24
            },
            {
                'name': 'R8C_11_1_4_SUBTEST1',
                'value': 25
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxwcdma/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/functions.py sha256=6a104df079edc0eb1a79405940d9864569eeeb6124046841ba8cce80b853798b bytes=222219 -->
## FILE: source/codegen/metadata/nirfmxwcdma/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/functions.py`
- sha256: `6a104df079edc0eb1a79405940d9864569eeeb6124046841ba8cce80b853798b`
- bytes: 222219

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
                'name': 'offsetPowerReferenceCarrier',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'offsetPowerReferenceSpecific',
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
                'name': 'relativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
        'cname': 'RFmxWCDMA_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'spreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'spreadingCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'CdaMeasurementChannelModulationType',
                'name': 'modulationType',
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
    'CDAFetchCodeDomainPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'codeDomainPowers',
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
                'name': 'relativePower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CHPFetchCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'CfgCarrierFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'CfgCarrierFrequencyArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'CfgContiguousCarriers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
            },
            {
                'direction': 'in',
                'name': 'carrierAtCenterFrequency',
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
    'CfgFrequencyUARFCN': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
                'name': 'uarfcn',
                'type': 'int32'
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
    'CfgNumberOfCarriers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'CfgNumberOfChannelsArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
    'CfgUplinkScrambling': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'uplinkScramblingCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'UplinkScramblingType',
                'name': 'uplinkScramblingType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgUplinkScramblingArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'UplinkScramblingType',
                'name': 'uplinkScramblingType',
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
                'name': 'uplinkScramblingCode',
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
    'CfgUplinkTestModel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'UplinkTestModel',
                'name': 'uplinkTestModel',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgUplinkTestModelArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'UplinkTestModel',
                'name': 'uplinkTestModel',
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
                'name': 'spreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'spreadingCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'enum': 'ModulationType',
                'name': 'modulationType',
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
                'name': 'spreadingFactor',
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
                'name': 'spreadingCode',
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
                'enum': 'ModulationType',
                'name': 'modulationType',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
        'custom_close': 'Close(id, RFMXWCDMA_VAL_FALSE)',
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
        'custom_close': 'Close(id, RFMXWCDMA_VAL_FALSE)',
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
        'cname': 'RFmxWCDMA_ModAccCfgReferenceWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
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
        'cname': 'RFmxWCDMA_ModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'name': 'detectedSpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'detectedSpreadingCode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedModulationType',
                'name': 'detectedModulationType',
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
                'name': 'detectedSpreadingFactor',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'detectedSpreadingCode',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'enum': 'ModAccDetectedModulationType',
                'name': 'detectedModulationType',
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
    'ModAccFetchEVMArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakEVM',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'rho',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'frequencyError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'chipRateError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'rmsMagnitudeError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'rmsPhaseError',
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
                'name': 'iqOriginOffset',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'iqGainImbalance',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'iqQuadratureError',
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
    'ModAccFetchMulticarrierIQImpairments': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'multicarrierIQOriginOffset',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'multicarrierIQGainImbalance',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'multicarrierIQQuadratureError',
                'type': 'float64'
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
    'ModAccFetchNumberOfDetectedChannelsArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'numberofDetectedChannels',
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
                'name': 'peakActiveCDESpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDECode',
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
    'ModAccFetchPeakActiveCDEArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDESpreadingFactor',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDECode',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakActiveCDEBranch',
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
                'name': 'peakCDECode',
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
    'ModAccFetchPeakCDEArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakCDECode',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakCDEBranch',
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
    'ModAccFetchRCDE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRCDE',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRCDESpreadingFactor',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'peakRCDECode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'enum': 'ModAccPeakRcdeBranch',
                'name': 'peakRCDEBranch',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchRCDEArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRCDE',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'peakRCDESpreadingFactor',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakRCDECode',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'peakRCDEBranch',
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
    'ModAccFetchRCDETrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'rcde',
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
    'ModAccFetchReferenceWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchReferenceWaveformInterleavedIQ': {
        'cname': 'RFmxWCDMA_ModAccFetchReferenceWaveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
    'ModAccFetchReferenceWaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
        'cname': 'RFmxWCDMA_QEVMFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
    'SEMFetchCarrierMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
                'grpc_type': 'NiRFmxWCDMAAttribute',
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
    'SlotPhaseFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
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
            },
            {
                'direction': 'out',
                'name': 'discontinuityCountGreaterThanLimit1',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'discontinuityCountGreaterThanLimit2',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'discontinuityMinimumDistance',
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwcdma/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfmxwcdma/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwcdma/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxwlan/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/attributes.py sha256=58481892c819ae8d1b2c77cbc40720a14d2cdde7930fcd689750d63005cfa5f1 bytes=60916 -->
## FILE: source/codegen/metadata/nirfmxwlan/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/attributes.py`
- sha256: `58481892c819ae8d1b2c77cbc40720a14d2cdde7930fcd689750d63005cfa5f1`
- bytes: 60916

````python
attributes = {
    10485761: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    10485762: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    10485763: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    10485764: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    10485765: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    10485766: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    10485767: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    10485768: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    10485769: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    10485770: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    10485771: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    10485772: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    10485773: {
        'access': 'read-write',
        'enum': 'Standard',
        'name': 'STANDARD',
        'type': 'int32'
    },
    10485774: {
        'access': 'read-write',
        'name': 'CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    10485775: {
        'access': 'read-write',
        'name': 'NUMBER_OF_FREQUENCY_SEGMENTS',
        'type': 'int32'
    },
    10485776: {
        'access': 'read-write',
        'name': 'NUMBER_OF_RECEIVE_CHAINS',
        'type': 'int32'
    },
    10485777: {
        'access': 'read-write',
        'enum': 'Standard',
        'name': 'AUTO_DETECT_SIGNAL_DETECTED_STANDARD',
        'type': 'int32'
    },
    10485778: {
        'access': 'read-write',
        'name': 'AUTO_DETECT_SIGNAL_DETECTED_CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    10485779: {
        'access': 'read-write',
        'name': 'AUTO_DETECT_SIGNAL_DETECTED_BURST_LENGTH',
        'type': 'float64'
    },
    10485780: {
        'access': 'read-write',
        'name': 'OFDM_FREQUENCY_SEGMENT_INDEX',
        'type': 'int32'
    },
    10485781: {
        'access': 'read-write',
        'enum': 'OfdmTransmitPowerClass',
        'name': 'OFDM_TRANSMIT_POWER_CLASS',
        'type': 'int32'
    },
    10485782: {
        'access': 'read-write',
        'enum': 'OfdmFrequencyBand',
        'name': 'OFDM_FREQUENCY_BAND',
        'type': 'int32'
    },
    10485783: {
        'access': 'read-write',
        'enum': 'OfdmPpduType',
        'name': 'OFDM_PPDU_TYPE',
        'type': 'int32'
    },
    10485784: {
        'access': 'read-write',
        'name': 'OFDM_NUMBER_OF_USERS',
        'type': 'int32'
    },
    10485785: {
        'access': 'read-write',
        'name': 'OFDM_MCS_INDEX',
        'type': 'int32'
    },
    10485786: {
        'access': 'read-write',
        'name': 'OFDM_RU_SIZE',
        'type': 'int32'
    },
    10485787: {
        'access': 'read-write',
        'name': 'OFDM_RU_OFFSET_MRU_INDEX',
        'type': 'int32'
    },
    10485788: {
        'access': 'read-write',
        'enum': 'OfdmGuardIntervalType',
        'name': 'OFDM_GUARD_INTERVAL_TYPE',
        'type': 'int32'
    },
    10485789: {
        'access': 'read-write',
        'enum': 'OfdmLtfSize',
        'name': 'OFDM_LTF_SIZE',
        'type': 'int32'
    },
    10485790: {
        'access': 'read-write',
        'name': 'OFDM_NUMBER_OF_SPACE_TIME_STREAMS',
        'type': 'int32'
    },
    10485791: {
        'access': 'read-write',
        'name': 'OFDM_SPACE_TIME_STREAM_OFFSET',
        'type': 'int32'
    },
    10485792: {
        'access': 'read-write',
        'name': 'OFDM_NUMBER_OF_HE_SIG_B_SYMBOLS',
        'type': 'int32'
    },
    10485793: {
        'access': 'read-write',
        'enum': 'OfdmDcmEnabled',
        'name': 'OFDM_DCM_ENABLED',
        'type': 'int32'
    },
    10485794: {
        'access': 'read-write',
        'name': 'OFDM_NUMBER_OF_LTF_SYMBOLS',
        'type': 'int32'
    },
    10485796: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    10485797: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    10485799: {
        'access': 'read-write',
        'enum': 'OfdmAutoPpduTypeDetectionEnabled',
        'name': 'OFDM_AUTO_PPDU_TYPE_DETECTION_ENABLED',
        'type': 'int32'
    },
    10485800: {
        'access': 'read-write',
        'enum': 'OfdmHeaderDecodingEnabled',
        'name': 'OFDM_HEADER_DECODING_ENABLED',
        'type': 'int32'
    },
    10485801: {
        'access': 'read-write',
        'enum': 'OfdmMUMimoLtfModeEnabled',
        'name': 'OFDM_MU_MIMO_LTF_MODE_ENABLED',
        'type': 'int32'
    },
    10485802: {
        'access': 'read-write',
        'enum': 'TriggerGateEnabled',
        'name': 'TRIGGER_GATE_ENABLED',
        'type': 'int32'
    },
    10485803: {
        'access': 'read-write',
        'name': 'TRIGGER_GATE_LENGTH',
        'type': 'float64'
    },
    10485807: {
        'access': 'read-write',
        'enum': 'OfdmPreamblePuncturingEnabled',
        'name': 'OFDM_PREAMBLE_PUNCTURING_ENABLED',
        'type': 'int32'
    },
    10485808: {
        'access': 'read-write',
        'name': 'OFDM_PREAMBLE_PUNCTURING_BITMAP',
        'type': 'int64'
    },
    10485809: {
        'access': 'read-write',
        'name': 'OFDM_PE_DISAMBIGUITY',
        'type': 'int32'
    },
    10485810: {
        'access': 'read-write',
        'enum': 'OfdmFecCodingType',
        'name': 'OFDM_FEC_CODING_TYPE',
        'type': 'int32'
    },
    10485811: {
        'access': 'read-write',
        'name': 'OFDM_PRE_FEC_PADDING_FACTOR',
        'type': 'int32'
    },
    10485812: {
        'access': 'read-write',
        'name': 'OFDM_LDPC_EXTRA_SYMBOL_SEGMENT',
        'type': 'int32'
    },
    10485813: {
        'access': 'read-write',
        'enum': 'OfdmStbcEnabled',
        'name': 'OFDM_STBC_ENABLED',
        'type': 'int32'
    },
    10485814: {
        'access': 'read-write',
        'name': 'SAMPLE_CLOCK_RATE_FACTOR',
        'type': 'float64'
    },
    10485815: {
        'access': 'read-write',
        'enum': 'OfdmPhaseRotationCoefficient1',
        'name': 'OFDM_PHASE_ROTATION_COEFFICIENT_1',
        'type': 'int32'
    },
    10485816: {
        'access': 'read-write',
        'enum': 'OfdmPhaseRotationCoefficient2',
        'name': 'OFDM_PHASE_ROTATION_COEFFICIENT_2',
        'type': 'int32'
    },
    10485817: {
        'access': 'read-write',
        'enum': 'OfdmPhaseRotationCoefficient3',
        'name': 'OFDM_PHASE_ROTATION_COEFFICIENT_3',
        'type': 'int32'
    },
    10485818: {
        'access': 'read-write',
        'enum': 'OfdmSigCompressionEnabled',
        'name': 'OFDM_SIG_COMPRESSION_ENABLED',
        'type': 'int32'
    },
    10485819: {
        'access': 'read-write',
        'name': 'OFDM_NUMBER_OF_SIG_SYMBOLS',
        'type': 'int32'
    },
    10485820: {
        'access': 'read-write',
        'enum': 'OfdmAutoPhaseRotationDetectionEnabled',
        'name': 'OFDM_AUTO_PHASE_ROTATION_DETECTION_ENABLED',
        'type': 'int32'
    },
    10485821: {
        'access': 'read-write',
        'name': 'OFDM_SCRAMBLER_SEED',
        'type': 'int32'
    },
    10485823: {
        'access': 'read-write',
        'enum': 'OfdmRUType',
        'name': 'OFDM_RU_TYPE',
        'type': 'int32'
    },
    10485824: {
        'access': 'read-write',
        'name': 'OFDM_DISTRIBUTION_BANDWIDTH',
        'type': 'float64'
    },
    10485825: {
        'access': 'read-write',
        'enum': 'Ofdm2xLdpcEnabled',
        'name': 'OFDM_2xLDPC_ENABLED',
        'type': 'int32'
    },
    10485826: {
        'access': 'read-write',
        'enum': 'OfdmIMPilotsEnabled',
        'name': 'OFDM_IM_PILOTS_ENABLED',
        'type': 'int32'
    },
    10485827: {
        'access': 'read-write',
        'enum': 'OfdmUnequalModulationEnabled',
        'name': 'OFDM_UNEQUAL_MODULATION_ENABLED',
        'type': 'int32'
    },
    10485828: {
        'access': 'read-write',
        'name': 'OFDM_UNEQUAL_MODULATION_PATTERN_INDEX',
        'type': 'int32'
    },
    10489852: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    10489853: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    10489855: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    10489856: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10489858: {
        'access': 'read-write',
        'name': 'TXP_MAXIMUM_MEASUREMENT_INTERVAL',
        'type': 'float64'
    },
    10489859: {
        'access': 'read-write',
        'enum': 'TxpBurstDetectionEnabled',
        'name': 'TXP_BURST_DETECTION_ENABLED',
        'type': 'int32'
    },
    10489860: {
        'access': 'read-write',
        'enum': 'TxpAveragingEnabled',
        'name': 'TXP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10489861: {
        'access': 'read-write',
        'name': 'TXP_AVERAGING_COUNT',
        'type': 'int32'
    },
    10489862: {
        'access': 'read-write',
        'name': 'TXP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    10489863: {
        'access': 'read-write',
        'name': 'TXP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    10489865: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10489873: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10489877: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MAXIMUM',
        'type': 'float64'
    },
    10489878: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MINIMUM',
        'type': 'float64'
    },
    10489879: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MEAN',
        'type': 'float64'
    },
    10489880: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MINIMUM',
        'type': 'float64'
    },
    10493962: {
        'access': 'read-write',
        'name': 'POWERRAMP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10493964: {
        'access': 'read-write',
        'name': 'POWERRAMP_ACQUISITION_LENGTH',
        'type': 'float64'
    },
    10493972: {
        'access': 'read-write',
        'enum': 'PowerRampAveragingEnabled',
        'name': 'POWERRAMP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10493973: {
        'access': 'read-write',
        'name': 'POWERRAMP_AVERAGING_COUNT',
        'type': 'int32'
    },
    10493974: {
        'access': 'read-write',
        'name': 'POWERRAMP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    10493975: {
        'access': 'read-write',
        'name': 'POWERRAMP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    10493976: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_RISE_TIME_MEAN',
        'type': 'float64'
    },
    10493977: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_FALL_TIME_MEAN',
        'type': 'float64'
    },
    10498058: {
        'access': 'read-write',
        'name': 'DSSSMODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10498059: {
        'access': 'read-write',
        'enum': 'DsssModAccAcquisitionLengthMode',
        'name': 'DSSSMODACC_ACQUISITION_LENGTH_MODE',
        'type': 'int32'
    },
    10498060: {
        'access': 'read-write',
        'name': 'DSSSMODACC_ACQUISITION_LENGTH',
        'type': 'float64'
    },
    10498061: {
        'access': 'read-write',
        'name': 'DSSSMODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    10498062: {
        'access': 'read-write',
        'name': 'DSSSMODACC_MAXIMUM_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    10498063: {
        'access': 'read-write',
        'enum': 'DsssModAccPulseShapingFilterType',
        'name': 'DSSSMODACC_PULSE_SHAPING_FILTER_TYPE',
        'type': 'int32'
    },
    10498064: {
        'access': 'read-write',
        'name': 'DSSSMODACC_PULSE_SHAPING_FILTER_PARAMETER',
        'type': 'float64'
    },
    10498065: {
        'access': 'read-write',
        'enum': 'DsssModAccEqualizationEnabled',
        'name': 'DSSSMODACC_EQUALIZATION_ENABLED',
        'type': 'int32'
    },
    10498066: {
        'access': 'read-write',
        'enum': 'DsssModAccEvmUnit',
        'name': 'DSSSMODACC_EVM_UNIT',
        'type': 'int32'
    },
    10498067: {
        'access': 'read-write',
        'enum': 'DsssModAccPowerMeasurementEnabled',
        'name': 'DSSSMODACC_POWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10498068: {
        'access': 'read-write',
        'name': 'DSSSMODACC_POWER_NUMBER_OF_CUSTOM_GATES',
        'type': 'int32'
    },
    10498069: {
        'access': 'read-write',
        'name': 'DSSSMODACC_POWER_CUSTOM_GATE_START_TIME',
        'type': 'float64'
    },
    10498070: {
        'access': 'read-write',
        'name': 'DSSSMODACC_POWER_CUSTOM_GATE_STOP_TIME',
        'type': 'float64'
    },
    10498092: {
        'access': 'read-write',
        'enum': 'DsssModAccFrequencyErrorCorrectionEnabled',
        'name': 'DSSSMODACC_FREQUENCY_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10498093: {
        'access': 'read-write',
        'enum': 'DsssModAccChipClockErrorCorrectionEnabled',
        'name': 'DSSSMODACC_CHIP_CLOCK_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10498094: {
        'access': 'read-write',
        'enum': 'DsssModAccIQOriginOffsetCorrectionEnabled',
        'name': 'DSSSMODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10498095: {
        'access': 'read-write',
        'enum': 'DsssModAccAveragingEnabled',
        'name': 'DSSSMODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10498096: {
        'access': 'read-write',
        'name': 'DSSSMODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    10498097: {
        'access': 'read-write',
        'name': 'DSSSMODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    10498098: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10498099: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MEAN',
        'type': 'float64'
    },
    10498100: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_1999_MAXIMUM',
        'type': 'float64'
    },
    10498101: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MEAN',
        'type': 'float64'
    },
    10498102: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_2007_MAXIMUM',
        'type': 'float64'
    },
    10498108: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MEAN',
        'type': 'float64'
    },
    10498109: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PEAK_EVM_802_11_2016_MAXIMUM',
        'type': 'float64'
    },
    10498110: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_CUSTOM_GATE_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10498111: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_CUSTOM_GATE_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10498125: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_NUMBER_OF_CHIPS_USED',
        'type': 'int32'
    },
    10498126: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_FREQUENCY_ERROR_MEAN',
        'type': 'float64'
    },
    10498130: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_CHIP_CLOCK_ERROR_MEAN',
        'type': 'float64'
    },
    10498131: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN',
        'type': 'float64'
    },
    10498135: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_IQ_QUADRATURE_ERROR_MEAN',
        'type': 'float64'
    },
    10498139: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    10498146: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_RMS_MAGNITUDE_ERROR_MEAN',
        'type': 'float64'
    },
    10498147: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_RMS_PHASE_ERROR_MEAN',
        'type': 'float64'
    },
    10498152: {
        'access': 'read-write',
        'enum': 'DsssModAccDataModulationFormat',
        'name': 'DSSSMODACC_RESULTS_DATA_MODULATION_FORMAT',
        'type': 'int32'
    },
    10498153: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PAYLOAD_LENGTH',
        'type': 'int32'
    },
    10498154: {
        'access': 'read-write',
        'enum': 'DsssModAccPreambleType',
        'name': 'DSSSMODACC_RESULTS_PREAMBLE_TYPE',
        'type': 'int32'
    },
    10498156: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_LOCKED_CLOCKS_BIT',
        'type': 'int32'
    },
    10498157: {
        'access': 'read-write',
        'enum': 'DsssModAccPayloadHeaderCrcStatus',
        'name': 'DSSSMODACC_RESULTS_HEADER_CRC_STATUS',
        'type': 'int32'
    },
    10498158: {
        'access': 'read-write',
        'enum': 'DsssModAccPsduCrcStatus',
        'name': 'DSSSMODACC_RESULTS_PSDU_CRC_STATUS',
        'type': 'int32'
    },
    10498161: {
        'access': 'read-write',
        'name': 'DSSSMODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    10498162: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PREAMBLE_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10498163: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PREAMBLE_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10498164: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_HEADER_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10498165: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_HEADER_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10498166: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_DATA_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10498167: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_DATA_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10498168: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PPDU_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10498169: {
        'access': 'read-write',
        'name': 'DSSSMODACC_RESULTS_PPDU_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10498170: {
        'access': 'read-write',
        'enum': 'DsssModAccBurstStartDetectionEnabled',
        'name': 'DSSSMODACC_BURST_START_DETECTION_ENABLED',
        'type': 'int32'
    },
    10498171: {
        'access': 'read-write',
        'enum': 'DsssModAccSpectrumInverted',
        'name': 'DSSSMODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    10498172: {
        'access': 'read-write',
        'enum': 'DsssModAccDataDecodingEnabled',
        'name': 'DSSSMODACC_DATA_DECODING_ENABLED',
        'type': 'int32'
    },
    10502144: {
        'access': 'read-write',
        'name': 'OFDMMODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10502146: {
        'access': 'read-write',
        'enum': 'OfdmModAccAveragingEnabled',
        'name': 'OFDMMODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10502147: {
        'access': 'read-write',
        'name': 'OFDMMODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    10502148: {
        'access': 'read-write',
        'name': 'OFDMMODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    10502149: {
        'access': 'read-write',
        'name': 'OFDMMODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    10502152: {
        'access': 'read-write',
        'enum': 'OfdmModAccEvmUnit',
        'name': 'OFDMMODACC_EVM_UNIT',
        'type': 'int32'
    },
    10502153: {
        'access': 'read-write',
        'enum': 'OfdmModAccAcquisitionLengthMode',
        'name': 'OFDMMODACC_ACQUISITION_LENGTH_MODE',
        'type': 'int32'
    },
    10502154: {
        'access': 'read-write',
        'name': 'OFDMMODACC_ACQUISITION_LENGTH',
        'type': 'float64'
    },
    10502155: {
        'access': 'read-write',
        'name': 'OFDMMODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    10502156: {
        'access': 'read-write',
        'name': 'OFDMMODACC_MAXIMUM_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    10502157: {
        'access': 'read-write',
        'enum': 'OfdmModAccCommonClockSourceEnabled',
        'name': 'OFDMMODACC_COMMON_CLOCK_SOURCE_ENABLED',
        'type': 'int32'
    },
    10502158: {
        'access': 'read-write',
        'enum': 'OfdmModAccAmplitudeTrackingEnabled',
        'name': 'OFDMMODACC_AMPLITUDE_TRACKING_ENABLED',
        'type': 'int32'
    },
    10502159: {
        'access': 'read-write',
        'enum': 'OfdmModAccPhaseTrackingEnabled',
        'name': 'OFDMMODACC_PHASE_TRACKING_ENABLED',
        'type': 'int32'
    },
    10502160: {
        'access': 'read-write',
        'enum': 'OfdmModAccSymbolClockErrorCorrectionEnabled',
        'name': 'OFDMMODACC_SYMBOL_CLOCK_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10502161: {
        'access': 'read-write',
        'enum': 'OfdmModAccChannelEstimationType',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_TYPE',
        'type': 'int32'
    },
    10502166: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_NUMBER_OF_SYMBOLS_USED',
        'type': 'int32'
    },
    10502167: {
        'access': 'read-write',
        'enum': 'OfdmModAccPowerMeasurementEnabled',
        'name': 'OFDMMODACC_POWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10502168: {
        'access': 'read-write',
        'name': 'OFDMMODACC_POWER_NUMBER_OF_CUSTOM_GATES',
        'type': 'int32'
    },
    10502169: {
        'access': 'read-write',
        'name': 'OFDMMODACC_POWER_CUSTOM_GATE_START_TIME',
        'type': 'float64'
    },
    10502170: {
        'access': 'read-write',
        'name': 'OFDMMODACC_POWER_CUSTOM_GATE_STOP_TIME',
        'type': 'float64'
    },
    10502171: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQImpairmentsModel',
        'name': 'OFDMMODACC_IQ_IMPAIRMENTS_MODEL',
        'type': 'int32'
    },
    10502172: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQGainImbalanceCorrectionEnabled',
        'name': 'OFDMMODACC_IQ_GAIN_IMBALANCE_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10502173: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQQuadratureErrorCorrectionEnabled',
        'name': 'OFDMMODACC_IQ_QUADRATURE_ERROR_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10502174: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQTimingSkewCorrectionEnabled',
        'name': 'OFDMMODACC_IQ_TIMING_SKEW_CORRECTION_ENABLED',
        'type': 'int32'
    },
    10502179: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN',
        'type': 'float64'
    },
    10502180: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_SUBCARRIER_INDEX',
        'type': 'int32'
    },
    10502181: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_UNUSED_TONE_ERROR_MARGIN',
        'type': 'float64'
    },
    10502182: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_UNUSED_TONE_ERROR_MARGIN_RU_INDEX',
        'type': 'int32'
    },
    10502183: {
        'access': 'read-write',
        'enum': 'OfdmModAccNoiseCompensationApplied',
        'name': 'OFDMMODACC_RESULTS_NOISE_COMPENSATION_APPLIED',
        'type': 'int32'
    },
    10502184: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_FREQUENCY_ERROR_MEAN',
        'type': 'float64'
    },
    10502185: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_FREQUENCY_ERROR_CCDF_10_PERCENT',
        'type': 'float64'
    },
    10502186: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MEAN',
        'type': 'float64'
    },
    10502187: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    10502188: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_ABSOLUTE_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    10502189: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN',
        'type': 'float64'
    },
    10502190: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MEAN',
        'type': 'float64'
    },
    10502191: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_TIMING_SKEW_MEAN',
        'type': 'float64'
    },
    10502192: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RMS_COMMON_PHASE_ERROR_MEAN',
        'type': 'float64'
    },
    10502193: {
        'access': 'read-write',
        'enum': 'OfdmPpduType',
        'name': 'OFDMMODACC_RESULTS_PPDU_TYPE',
        'type': 'int32'
    },
    10502194: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_MCS_INDEX',
        'type': 'int32'
    },
    10502195: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RU_SIZE',
        'type': 'int32'
    },
    10502196: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RU_OFFSET_MRU_INDEX',
        'type': 'int32'
    },
    10502197: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_NUMBER_OF_USERS',
        'type': 'int32'
    },
    10502198: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_NUMBER_OF_HE_SIG_B_SYMBOLS',
        'type': 'int32'
    },
    10502199: {
        'access': 'read-write',
        'enum': 'OfdmGuardIntervalType',
        'name': 'OFDMMODACC_RESULTS_GUARD_INTERVAL_TYPE',
        'type': 'int32'
    },
    10502200: {
        'access': 'read-write',
        'enum': 'OfdmLtfSize',
        'name': 'OFDMMODACC_RESULTS_LTF_SIZE',
        'type': 'int32'
    },
    10502201: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_NUMBER_OF_SPACE_TIME_STREAMS',
        'type': 'int32'
    },
    10502202: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502203: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502204: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_LTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502205: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_LTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502206: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502207: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_L_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502208: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_RL_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502209: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_RL_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502210: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502211: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502212: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_SIG_A_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502213: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_SIG_A_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502214: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_SIG_A_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502215: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_SIG_A_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502216: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_SIG_B_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502217: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_SIG_B_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502218: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_SIG_B_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502219: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_SIG_B_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502220: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502221: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502222: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_GF_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502223: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_GF_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502224: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502225: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502226: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502227: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502228: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_DLTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502229: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_DLTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502230: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_ELTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502231: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HT_ELTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502232: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_LTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502233: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_VHT_LTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502234: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_LTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502235: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_HE_LTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502236: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_DATA_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502237: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_DATA_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502238: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_PE_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502239: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_PE_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502240: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_PPDU_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502241: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_PPDU_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502242: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502243: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_CUSTOM_GATE_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502246: {
        'access': 'read-write',
        'enum': 'OfdmModAccMeasurementMode',
        'name': 'OFDMMODACC_MEASUREMENT_MODE',
        'type': 'int32'
    },
    10502247: {
        'access': 'read-write',
        'enum': 'OfdmModAccNoiseCompensationEnabled',
        'name': 'OFDMMODACC_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    10502248: {
        'access': 'read-write',
        'enum': 'OfdmModAccNoiseCompensationInputPowerCheckEnabled',
        'name': 'OFDMMODACC_NOISE_COMPENSATION_INPUT_POWER_CHECK_ENABLED',
        'type': 'int32'
    },
    10502249: {
        'access': 'read-write',
        'name': 'OFDMMODACC_NOISE_COMPENSATION_REFERENCE_LEVEL_COERCION_LIMIT',
        'type': 'float64'
    },
    10502250: {
        'access': 'read-write',
        'enum': 'OfdmModAccChannelEstimationInterpolationType',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_INTERPOLATION_TYPE',
        'type': 'int32'
    },
    10502251: {
        'access': 'read-write',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_SMOOTHING_LENGTH',
        'type': 'int32'
    },
    10502252: {
        'access': 'read-write',
        'enum': 'OfdmModAccUnusedToneErrorMaskReference',
        'name': 'OFDMMODACC_UNUSED_TONE_ERROR_MASK_REFERENCE',
        'type': 'int32'
    },
    10502253: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RMS_COMMON_PILOT_ERROR_MEAN',
        'type': 'float64'
    },
    10502254: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_COMPOSITE_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502255: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_COMPOSITE_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502256: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_COMPOSITE_PILOT_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502257: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502258: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502259: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_PILOT_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502260: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502261: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502262: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_PILOT_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502263: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502264: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_STREAM_DATA_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502265: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_STREAM_PILOT_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502266: {
        'access': 'read-write',
        'enum': 'OfdmModAccSpectrumInverted',
        'name': 'OFDMMODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    10502267: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQImpairmentsEstimationEnabled',
        'name': 'OFDMMODACC_IQ_IMPAIRMENTS_ESTIMATION_ENABLED',
        'type': 'int32'
    },
    10502268: {
        'access': 'read-write',
        'enum': 'OfdmModAccOptimizeDynamicRangeForEvmEnabled',
        'name': 'OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_ENABLED',
        'type': 'int32'
    },
    10502269: {
        'access': 'read-write',
        'name': 'OFDMMODACC_OPTIMIZE_DYNAMIC_RANGE_FOR_EVM_MARGIN',
        'type': 'float64'
    },
    10502270: {
        'access': 'read-write',
        'enum': 'OfdmModAccFrequencyErrorEstimationMethod',
        'name': 'OFDMMODACC_FREQUENCY_ERROR_ESTIMATION_METHOD',
        'type': 'int32'
    },
    10502271: {
        'access': 'read-write',
        'enum': 'OfdmModAccIQImpairmentsPerSubcarrierEnabled',
        'name': 'OFDMMODACC_IQ_IMPAIRMENTS_PER_SUBCARRIER_ENABLED',
        'type': 'int32'
    },
    10502277: {
        'access': 'read-write',
        'enum': 'OfdmModAccBurstStartDetectionEnabled',
        'name': 'OFDMMODACC_BURST_START_DETECTION_ENABLED',
        'type': 'int32'
    },
    10502279: {
        'access': 'read-write',
        'enum': 'OfdmModAccChannelEstimationLLtfEnabled',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_L_LTF_ENABLED',
        'type': 'int32'
    },
    10502280: {
        'access': 'read-write',
        'enum': 'OfdmModAccLSigParityCheckStatus',
        'name': 'OFDMMODACC_RESULTS_L_SIG_PARITY_CHECK_STATUS',
        'type': 'int32'
    },
    10502281: {
        'access': 'read-write',
        'enum': 'OfdmModAccSigCrcStatus',
        'name': 'OFDMMODACC_RESULTS_SIG_CRC_STATUS',
        'type': 'int32'
    },
    10502282: {
        'access': 'read-write',
        'enum': 'OfdmModAccSigBCrcStatus',
        'name': 'OFDMMODACC_RESULTS_SIG_B_CRC_STATUS',
        'type': 'int32'
    },
    10502283: {
        'access': 'read-write',
        'enum': 'OfdmModAccDataDecodingEnabled',
        'name': 'OFDMMODACC_DATA_DECODING_ENABLED',
        'type': 'int32'
    },
    10502284: {
        'access': 'read-write',
        'enum': 'OfdmModAccPsduCrcStatus',
        'name': 'OFDMMODACC_RESULTS_PSDU_CRC_STATUS',
        'type': 'int32'
    },
    10502285: {
        'access': 'read-write',
        'enum': 'OfdmModAccChannelMatrixPowerEnabled',
        'name': 'OFDMMODACC_CHANNEL_MATRIX_POWER_ENABLED',
        'type': 'int32'
    },
    10502286: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CROSS_POWER_MEAN',
        'type': 'float64'
    },
    10502287: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_POWER_MEAN',
        'type': 'float64'
    },
    10502288: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SPACE_TIME_STREAM_OFFSET',
        'type': 'int32'
    },
    10502289: {
        'access': 'read-write',
        'enum': 'OfdmModAccUSigCrcStatus',
        'name': 'OFDMMODACC_RESULTS_U_SIG_CRC_STATUS',
        'type': 'int32'
    },
    10502290: {
        'access': 'read-write',
        'enum': 'OfdmModAccEhtSigCrcStatus',
        'name': 'OFDMMODACC_RESULTS_EHT_SIG_CRC_STATUS',
        'type': 'int32'
    },
    10502291: {
        'access': 'read-write',
        'enum': 'OfdmModAccEvmReferenceDataSymbolsMode',
        'name': 'OFDMMODACC_EVM_REFERENCE_DATA_SYMBOLS_MODE',
        'type': 'int32'
    },
    10502293: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_PE_DURATION',
        'type': 'float64'
    },
    10502294: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_RMS_EVM_MAXIMUM',
        'type': 'float64'
    },
    10502295: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_RMS_EVM_MINIMUM',
        'type': 'float64'
    },
    10502296: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MAXIMUM',
        'type': 'float64'
    },
    10502297: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_RMS_EVM_MINIMUM',
        'type': 'float64'
    },
    10502298: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MAXIMUM',
        'type': 'float64'
    },
    10502299: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_STREAM_RMS_EVM_MINIMUM',
        'type': 'float64'
    },
    10502300: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502301: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_USER_POWER_MINIMUM',
        'type': 'float64'
    },
    10502302: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_MAXIMUM',
        'type': 'float64'
    },
    10502303: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SPECTRAL_FLATNESS_MARGIN_MINIMUM',
        'type': 'float64'
    },
    10502304: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_FREQUENCY_ERROR_MAXIMUM',
        'type': 'float64'
    },
    10502305: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_FREQUENCY_ERROR_MINIMUM',
        'type': 'float64'
    },
    10502306: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MAXIMUM',
        'type': 'float64'
    },
    10502307: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SYMBOL_CLOCK_ERROR_MINIMUM',
        'type': 'float64'
    },
    10502308: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MAXIMUM',
        'type': 'float64'
    },
    10502309: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_RELATIVE_IQ_ORIGIN_OFFSET_MINIMUM',
        'type': 'float64'
    },
    10502310: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MAXIMUM',
        'type': 'float64'
    },
    10502311: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_GAIN_IMBALANCE_MINIMUM',
        'type': 'float64'
    },
    10502312: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    10502313: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_IQ_QUADRATURE_ERROR_MINIMUM',
        'type': 'float64'
    },
    10502314: {
        'access': 'read-write',
        'enum': 'OfdmModAccFecCodingType',
        'name': 'OFDMMODACC_RESULTS_FEC_CODING_TYPE',
        'type': 'int32'
    },
    10502315: {
        'access': 'read-write',
        'enum': 'OfdmModAccDcmEnabled',
        'name': 'OFDMMODACC_RESULTS_DCM_ENABLED',
        'type': 'int32'
    },
    10502316: {
        'access': 'read-write',
        'enum': 'OfdmModAccAveragingType',
        'name': 'OFDMMODACC_AVERAGING_TYPE',
        'type': 'int32'
    },
    10502317: {
        'access': 'read-write',
        'enum': 'OfdmModAccVectorAveragingTimeAlignmentEnabled',
        'name': 'OFDMMODACC_VECTOR_AVERAGING_TIME_ALIGNMENT_ENABLED',
        'type': 'int32'
    },
    10502318: {
        'access': 'read-write',
        'enum': 'OfdmModAccVectorAveragingPhaseAlignmentEnabled',
        'name': 'OFDMMODACC_VECTOR_AVERAGING_PHASE_ALIGNMENT_ENABLED',
        'type': 'int32'
    },
    10502320: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_BURST_START_TIME_MEAN',
        'type': 'float64'
    },
    10502321: {
        'access': 'read-write',
        'enum': 'OfdmModAccAutoLevelAllowOverflow',
        'name': 'OFDMMODACC_AUTO_LEVEL_ALLOW_OVERFLOW',
        'type': 'int32'
    },
    10502327: {
        'access': 'read-write',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_RELATIVE_DELAY_SPREAD',
        'type': 'float64'
    },
    10502328: {
        'access': 'read-write',
        'enum': 'OfdmModAccPhaseRotationCoefficient1',
        'name': 'OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_1',
        'type': 'int32'
    },
    10502329: {
        'access': 'read-write',
        'enum': 'OfdmModAccPhaseRotationCoefficient2',
        'name': 'OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_2',
        'type': 'int32'
    },
    10502330: {
        'access': 'read-write',
        'enum': 'OfdmModAccPhaseRotationCoefficient3',
        'name': 'OFDMMODACC_RESULTS_PHASE_ROTATION_COEFFICIENT_3',
        'type': 'int32'
    },
    10502331: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_L_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502332: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502333: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SIG_B_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502334: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_U_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502335: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_EHT_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502336: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_U_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502337: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_U_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502338: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502339: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502340: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502341: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502342: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_LTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502343: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_EHT_LTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502344: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_SCRAMBLER_SEED',
        'type': 'int32'
    },
    10502345: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_AGGREGATION',
        'type': 'int32'
    },
    10502346: {
        'access': 'read-write',
        'enum': 'OfdmModAccCombinedSignalDemodulationEnabled',
        'name': 'OFDMMODACC_COMBINED_SIGNAL_DEMODULATION_ENABLED',
        'type': 'int32'
    },
    10502347: {
        'access': 'read-write',
        'name': 'OFDMMODACC_REFERENCE_DATA_CONSTELLATION_IDENTIFIER',
        'type': 'char[]'
    },
    10502348: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_STREAM_POWER_MEAN',
        'type': 'float64'
    },
    10502353: {
        'access': 'read-write',
        'enum': 'OfdmModAccCommonPilotErrorScalingReference',
        'name': 'OFDMMODACC_COMMON_PILOT_ERROR_SCALING_REFERENCE',
        'type': 'int32'
    },
    10502354: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_UHR_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502355: {
        'access': 'read-write',
        'enum': 'OfdmModAccUhrSigCrcStatus',
        'name': 'OFDMMODACC_RESULTS_UHR_SIG_CRC_STATUS',
        'type': 'int32'
    },
    10502356: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_ELR_SIG_RMS_EVM_MEAN',
        'type': 'float64'
    },
    10502357: {
        'access': 'read-write',
        'enum': 'OfdmModAccElrSigCrcStatus',
        'name': 'OFDMMODACC_RESULTS_ELR_SIG_CRC_STATUS',
        'type': 'int32'
    },
    10502358: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_STF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502359: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_STF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502360: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_LTF_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502361: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_LTF_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502362: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502363: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_UHR_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502364: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_ELR_SIG_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502365: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_ELR_SIG_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502366: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_ELR_MARK_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    10502367: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_POWER_ELR_MARK_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    10502368: {
        'access': 'read-write',
        'enum': 'OfdmModAccChannelEstimationLtfAveragingEnabled',
        'name': 'OFDMMODACC_CHANNEL_ESTIMATION_LTF_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10502369: {
        'access': 'read-write',
        'enum': 'OfdmModAccRUType',
        'name': 'OFDMMODACC_RESULTS_RU_TYPE',
        'type': 'int32'
    },
    10502370: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_DISTRIBUTION_BANDWIDTH',
        'type': 'float64'
    },
    10502371: {
        'access': 'read-write',
        'enum': 'OfdmModAcc2xLdpcEnabled',
        'name': 'OFDMMODACC_RESULTS_2xLDPC_ENABLED',
        'type': 'int32'
    },
    10502372: {
        'access': 'read-write',
        'enum': 'OfdmModAccIMPilotsEnabled',
        'name': 'OFDMMODACC_RESULTS_IM_PILOTS_ENABLED',
        'type': 'int32'
    },
    10502373: {
        'access': 'read-write',
        'enum': 'OfdmModAccUnequalModulationEnabled',
        'name': 'OFDMMODACC_RESULTS_UNEQUAL_MODULATION_ENABLED',
        'type': 'int32'
    },
    10502374: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_UNEQUAL_MODULATION_PATTERN_INDEX',
        'type': 'int32'
    },
    10502375: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_NUMBER_OF_SIG_SYMBOLS',
        'type': 'int32'
    },
    10502376: {
        'access': 'read-write',
        'name': 'OFDMMODACC_RESULTS_CHAIN_STREAM_CROSS_POWER_MEAN',
        'type': 'float64'
    },
    10506240: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    10506242: {
        'access': 'read-write',
        'enum': 'SemMaskType',
        'name': 'SEM_MASK_TYPE',
        'type': 'int32'
    },
    10506245: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    10506246: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    10506247: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    10506248: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    10506249: {
        'access': 'read-write',
        'enum': 'SemOffsetSideband',
        'name': 'SEM_OFFSET_SIDEBAND',
        'type': 'int32'
    },
    10506250: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_START',
        'type': 'float64'
    },
    10506251: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RELATIVE_LIMIT_STOP',
        'type': 'float64'
    },
    10506252: {
        'access': 'read-write',
        'enum': 'SemSpanAuto',
        'name': 'SEM_SPAN_AUTO',
        'type': 'int32'
    },
    10506253: {
        'access': 'read-write',
        'name': 'SEM_SPAN',
        'type': 'float64'
    },
    10506257: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    10506258: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    10506259: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    10506260: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    10506261: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    10506262: {
        'access': 'read-write',
        'enum': 'SemAmplitudeCorrectionType',
        'name': 'SEM_AMPLITUDE_CORRECTION_TYPE',
        'type': 'int32'
    },
    10506263: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    10506264: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    10506267: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    10506268: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    10506270: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    10506271: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_PEAK_FREQUENCY',
        'type': 'float64'
    },
    10506273: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    10506274: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    10506275: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    10506276: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    10506277: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    10506278: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    10506279: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    10506280: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    10506281: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    10506282: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    10506283: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    10506284: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    10506285: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    10506286: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    10506287: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    10506288: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    10506289: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    10506290: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    10506291: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    10506292: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    10534912: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfmxwlan/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/config.py sha256=5a21c6d2668d31865b42d2e86cad69fd69e64983e4b6d2af292abebdcede585b bytes=2051 -->
## FILE: source/codegen/metadata/nirfmxwlan/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/config.py`
- sha256: `5a21c6d2668d31865b42d2e86cad69fd69e64983e4b6d2af292abebdcede585b`
- bytes: 2051

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxWLAN.h',
    'c_function_prefix': 'RFmxWLAN_',
    'service_class_prefix': 'NiRFmxWLAN',
    'java_package': 'com.ni.grpc.nirfmxwlan',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxWLAN',
    'namespace_component': 'nirfmxwlan',
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
    'driver_name': 'NI-RFMXWLAN',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxwlan',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxWLAN.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxWLAN.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxwlan',
    'session_class_description': 'An NI-RFmxWLAN instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxwlan/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxwlan/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxwlan/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````
