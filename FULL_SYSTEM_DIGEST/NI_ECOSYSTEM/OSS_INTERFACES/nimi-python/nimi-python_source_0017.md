# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/attributes.py sha256=518846df3fab659be669c48cf515c8358d3b29d0f300fcf3912752be8c5c17d7 bytes=64891 -->
## FILE: src/nifgen/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/attributes.py`
- sha256: `518846df3fab659be669c48cf515c8358d3b29d0f300fcf3912752be8c5c17d7`
- bytes: 64891

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 25.0.0f114
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  functions perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  functions return calculated values.\nDefault Value: VI_FALSE\nUse niFgen_InitWithOptions to override default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the driver setup portion of the option string that was passed into the niFgen_InitWithOptions function.'
        },
        'lv_property': '',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument  driver supports.\nFor each attribute for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'NUM_CHANNELS',
        'python_name': 'channel_count',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the resource descriptor that NI-FGEN uses to identify the physical device.\nIf you initialize NI-FGEN with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.\nIf you initialize NI-FGEN with the resource  descriptor, this attribute contains that value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name that you specified when opening the  current IVI session.\nYou may pass a logical name to niFgen_init or  niFgen_InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns a model code of the device. For NI-FGEN versions that support more than one device, this  attribute contains a comma-separated list of supported device  models.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050503: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the major version number of NI-FGEN.'
        },
        'lv_property': 'Instrument:Obsolete:Major Version',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'python_name': 'major_version',
        'type': 'ViInt32'
    },
    1050504: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minor version number of NI-FGEN.'
        },
        'lv_property': 'Instrument:Obsolete:Minor Version',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'python_name': 'minor_version',
        'type': 'ViInt32'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the firmware revision information  for the device that you are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the device manufacturer you are currently  using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the model number or name of the device that you  are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns a brief description of NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about  NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150101: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls whether the signal generator generates a digital pattern of the output signal.'
        },
        'lv_property': 'Output:Advanced:Digital Pattern Enabled',
        'name': 'DIGITAL_PATTERN_ENABLED',
        'type': 'ViBoolean'
    },
    1150102: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls whether the signal generator applies a digital filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.'
        },
        'lv_property': 'Output:Filters:Digital Filter Enabled',
        'name': 'DIGITAL_FILTER_ENABLED',
        'type': 'ViBoolean'
    },
    1150103: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls whether the signal generator applies to an analog filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.'
        },
        'lv_property': 'Output:Filters:Analog Filter Enabled',
        'name': 'ANALOG_FILTER_ENABLED',
        'type': 'ViBoolean'
    },
    1150104: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls the filter correction frequency of the analog filter. This attribute corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this attribute to 0 Hz.'
        },
        'lv_property': 'Instrument:5401/5411/5431:Filter Correction Frequency',
        'name': 'FILTER_CORRECTION_FREQUENCY',
        'type': 'ViReal64'
    },
    1150107: {
        'access': 'read-write',
        'documentation': {
            'description': 'Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.'
        },
        'lv_property': 'Clocks:Reference Clock:Frequency',
        'name': 'REF_CLOCK_FREQUENCY',
        'type': 'ViReal64'
    },
    1150108: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls the trigger mode.'
        },
        'enum': 'TriggerMode',
        'lv_property': 'Triggers:Trigger Mode',
        'name': 'TRIGGER_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150110: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls which clock mode is used for the signal generator.\nFor signal generators that support it, this attribute allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.\n'
        },
        'enum': 'ClockMode',
        'lv_property': 'Clocks:Sample Clock:Mode',
        'name': 'CLOCK_MODE',
        'type': 'ViInt32'
    },
    1150112: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Sample clock source. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR  attribute, the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'SampleClockSource',
        'lv_property': 'Clocks:Sample Clock:Source',
        'name': 'SAMPLE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150113: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the reference clock source used by the signal generator.\nThe signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this attribute to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'ReferenceClockSource',
        'lv_property': 'Clocks:Reference Clock:Source',
        'name': 'REFERENCE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150208: {
        'access': 'read-write',
        'documentation': {
            'description': 'Sets which frequency list the signal generator  produces. Create a frequency list using niFgen_CreateFreqList.  niFgen_CreateFreqList returns a handle that you can  use to identify the list.'
        },
        'grpc_enum': 'FrequencyListHandle',
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Handle',
        'name': 'FREQ_LIST_HANDLE',
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of frequency lists the signal generator allows.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists',
        'name': 'MAX_NUM_FREQ_LISTS',
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minimum number of frequency lists that the signal generator allows.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Length',
        'name': 'MIN_FREQ_LIST_LENGTH',
        'type': 'ViInt32'
    },
    1150211: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of steps that can be in a frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Length',
        'name': 'MAX_FREQ_LIST_LENGTH',
        'type': 'ViInt32'
    },
    1150212: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minimum number of steps that can be in a frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Duration',
        'name': 'MIN_FREQ_LIST_DURATION',
        'type': 'ViReal64'
    },
    1150213: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum duration of any one step in the frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Duration',
        'name': 'MAX_FREQ_LIST_DURATION',
        'type': 'ViReal64'
    },
    1150214: {
        'access': 'read-write',
        'documentation': {
            'description': 'Returns the quantum of which all durations must be a multiple in a  frequency list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Duration Quantum',
        'name': 'FREQ_LIST_DURATION_QUANTUM',
        'type': 'ViReal64'
    },
    1150215: {
        'access': 'read only',
        'documentation': {
            'description': 'The bus type of the signal generator.'
        },
        'enum': 'BusType',
        'lv_property': 'Instrument:Bus Type',
        'name': 'BUS_TYPE',
        'type': 'ViInt32'
    },
    1150218: {
        'access': 'read-write',
        'documentation': {
            'description': 'This attribute only affects the device when NIFGEN_ATTR_DIGITAL_FILTER_ENABLED is set to VI_TRUE. If you do not set this attribute directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.'
        },
        'lv_property': 'Output:Filters:Digital Filter Interpolation Factor',
        'name': 'DIGITAL_FILTER_INTERPOLATION_FACTOR',
        'type': 'ViReal64'
    },
    1150219: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute.'
        },
        'lv_property': 'Clocks:Sample Clock:Exported Sample Clock Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_DIVISOR',
        'type': 'ViInt32'
    },
    1150220: {
        'access': 'read-write',
        'documentation': {
            'description': 'This channel-based attribute specifies the load impedance connected to the analog output of the channel. If you set this attribute to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).'
        },
        'grpc_enum': 'LoadImpedance',
        'lv_property': 'Output:Load Impedance',
        'name': 'LOAD_IMPEDANCE',
        'type': 'ViReal64'
    },
    1150222: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.\nThe direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.\n'
        },
        'enum': 'AnalogPath',
        'lv_property': 'Output:Analog Path',
        'name': 'ANALOG_PATH',
        'type': 'ViInt32'
    },
    1150230: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR',
        'type': 'ViInt32'
    },
    1150233: {
        'access': 'read-write',
        'documentation': {
            'description': 'Binary value of the external clock delay.'
        },
        'lv_property': 'Clocks:Advanced:External Clock Delay Binary Value',
        'name': 'EXTERNAL_CLOCK_DELAY_BINARY_VALUE',
        'type': 'ViInt32'
    },
    1150234: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the mask to apply to the analog output. The masked data is replaced with the data in NIFGEN_ATTR_ANALOG_STATIC_VALUE.'
        },
        'lv_property': 'Output:Data Mask:Analog Data Mask',
        'name': 'ANALOG_DATA_MASK',
        'type': 'ViInt32'
    },
    1150235: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the static value that replaces data masked by NIFGEN_ATTR_ANALOG_DATA_MASK.'
        },
        'lv_property': 'Output:Data Mask:Analog Static Value',
        'name': 'ANALOG_STATIC_VALUE',
        'type': 'ViInt32'
    },
    1150236: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in NIFGEN_ATTR_DIGITAL_STATIC_VALUE.'
        },
        'lv_property': 'Output:Data Mask:Digital Data Mask',
        'name': 'DIGITAL_DATA_MASK',
        'type': 'ViInt32'
    },
    1150237: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the static value that replaces data masked by NIFGEN_ATTR_DIGITAL_DATA_MASK.'
        },
        'lv_property': 'Output:Data Mask:Digital Static Value',
        'name': 'DIGITAL_STATIC_VALUE',
        'type': 'ViInt32'
    },
    1150238: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute contains the number of samples used in the standard function waveform  buffer. This attribute is only valid on devices that implement standard function mode  in software, and is read-only for all other devices.\nimplementation of Standard Function Mode on your device.\n',
            'note': 'Refer to the Standard Function Mode topic for more information on the'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Buffer Size',
        'name': 'FUNC_BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150239: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute sets the maximum number of samples that can be used in the standard  function waveform buffer. Increasing this value may increase the quality of  the waveform. This attribute is only valid on devices that implement standard  function mode in software, and is read-only for all other devices.\nimplementation of Standard Function Mode on your device.\n',
            'note': 'Refer to the Standard Function Mode topic for more information on the'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Maximum Buffer Size',
        'name': 'FUNC_MAX_BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150240: {
        'access': 'read-write',
        'documentation': {
            'description': 'The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File functions.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:File Transfer Block Size',
        'name': 'FILE_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150241: {
        'access': 'read-write',
        'documentation': {
            'description': 'The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150242: {
        'access': 'read only',
        'documentation': {
            'description': 'The total amount of memory, in bytes, on the signal generator.'
        },
        'lv_property': 'Instrument:Memory Size',
        'name': 'MEMORY_SIZE',
        'type': 'ViInt32'
    },
    1150243: {
        'access': 'read only',
        'documentation': {
            'description': "\nThe signal generator's serial number.\n"
        },
        'lv_property': 'Instrument:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150254: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.\nSome signal generators support both digital gain and an analog gain (analog gain is specified with the NIFGEN_ATTR_FUNC_AMPLITUDE attribute or the NIFGEN_ATTR_ARB_GAIN attribute). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a function of analog gain, so only analog gain makes full use of the resolution of the DAC.\n'
        },
        'lv_property': 'Output:Digital Gain',
        'name': 'DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150270: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies which script the generator produces. To configure the generator to run a particular script, set this attribute to the name of the script. Use niFgen_WriteScript to create multiple scripts. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.'
        },
        'lv_property': 'Arbitrary Waveform:Script Mode:Script to Generate',
        'name': 'SCRIPT_TO_GENERATE',
        'type': 'ViString'
    },
    1150271: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of markers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.'
        },
        'lv_property': 'Instrument:Marker Events Count',
        'name': 'MARKER_EVENTS_COUNT',
        'type': 'ViInt32'
    },
    1150272: {
        'access': 'read only',
        'documentation': {
            'description': 'Specifies the number of Script triggers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.'
        },
        'lv_property': 'Instrument:Script Triggers Count',
        'name': 'SCRIPT_TRIGGERS_COUNT',
        'type': 'ViInt32'
    },
    1150273: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of Data Marker Events supported by the device.'
        },
        'lv_property': 'Instrument:Data Marker Events Count',
        'name': 'DATA_MARKER_EVENTS_COUNT',
        'type': 'ViInt32'
    },
    1150280: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this attribute.'
        },
        'enum': 'StartTriggerType',
        'lv_property': 'Triggers:Start:Trigger Type',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150281: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the source terminal for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.'
        },
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150282: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the active edge for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.'
        },
        'enum': 'StartTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150283: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Start trigger.'
        },
        'lv_property': 'Triggers:Start:Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150290: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the Script trigger type. Depending upon the value of this attribute, additional attributes may need to be configured to fully configure the trigger.'
        },
        'enum': 'ScriptTriggerType',
        'lv_property': 'Triggers:Script:Trigger Type',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.'
        },
        'lv_property': 'Triggers:Script:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150292: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the active edge for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.'
        },
        'enum': 'ScriptTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Script:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150295: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for the exported Script trigger.\nSetting this attribute to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.\n'
        },
        'lv_property': 'Triggers:Script:Output Terminal',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150310: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for the Ready for Start Event.'
        },
        'lv_property': 'Events:Ready For Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150312: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for the Marker Event.'
        },
        'lv_property': 'Events:Marker:Output Terminal',
        'name': 'MARKER_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViString'
    },
    1150314: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for the Started Event.'
        },
        'lv_property': 'Events:Started:Output Terminal',
        'name': 'STARTED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150315: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for the Done Event.'
        },
        'lv_property': 'Events:Done:Output Terminal',
        'name': 'DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150320: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the terminal to which to export the Sample Clock.'
        },
        'lv_property': 'Clocks:Sample Clock:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150321: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the terminal to which to export the Reference Clock.'
        },
        'lv_property': 'Clocks:Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150322: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the terminal to which to export the Onboard Reference Clock.'
        },
        'lv_property': 'Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150323: {
        'access': 'read-write',
        'documentation': {
            'description': '\nWhen VI_TRUE, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.\nThis attribute should be set to VI_FALSE when performing Flatness Calibration.\n'
        },
        'lv_property': 'Output:Filters:Flatness Correction Enabled',
        'name': 'FLATNESS_CORRECTION_ENABLED',
        'type': 'ViBoolean'
    },
    1150324: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the waveform handle of the waveform used to continuously stream data during generation. This attribute defaults to -1 when no streaming waveform is specified.\nUsed in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle',
        'name': 'STREAMING_WAVEFORM_HANDLE',
        'type': 'ViInt32'
    },
    1150325: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.\nTo avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.\nUsed in conjunction with the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE or NIFGEN_ATTR_STREAMING_WAVEFORM_NAME attributes.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'type': 'ViInt32'
    },
    1150326: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the name of the waveform used to continuously stream data during generation. This attribute defaults to // when no streaming waveform is specified.\nUse in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name',
        'name': 'STREAMING_WAVEFORM_NAME',
        'type': 'ViString'
    },
    1150327: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the position for a marker to be asserted in the arbitrary waveform. This attribute defaults to -1 when no marker position is specified. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\nUse niFgen_ExportSignal to export the marker signal.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position',
        'name': 'ARB_MARKER_POSITION',
        'type': 'ViInt32'
    },
    1150328: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies number of times to repeat the arbitrary waveform when the triggerMode parameter of nifgen_ConfigureTriggerMode is set to NIFGEN_VAL_SINGLE or NIFGEN_VAL_STEPPED. This attribute is ignored if the triggerMode parameter is set to NIFGEN_VAL_CONTINUOUS or NIFGEN_VAL_BURST. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\nWhen used during streaming, this attribute specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count',
        'name': 'ARB_REPEAT_COUNT',
        'type': 'ViInt32'
    },
    1150329: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute,   the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL  attribute is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150333: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width units for the Started Event.'
        },
        'enum': 'EventPulseWidthUnits',
        'lv_property': 'Events:Started:Pulse:Width Units',
        'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS',
        'type': 'ViInt32'
    },
    1150334: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width units for the Done Event.'
        },
        'enum': 'EventPulseWidthUnits',
        'lv_property': 'Events:Done:Pulse:Width Units',
        'name': 'DONE_EVENT_PULSE_WIDTH_UNITS',
        'type': 'ViInt32'
    },
    1150335: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width for the Started Event.'
        },
        'lv_property': 'Events:Started:Pulse:Width Value',
        'name': 'STARTED_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150336: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width for the Done Event.'
        },
        'lv_property': 'Events:Done:Pulse:Width Value',
        'name': 'DONE_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150337: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the bit number to assign to the Data Marker Event.'
        },
        'lv_property': 'Events:Data Marker:Data Bit Number',
        'name': 'DATA_MARKER_EVENT_DATA_BIT_NUMBER',
        'supported_rep_caps': [
            'data_markers'
        ],
        'type': 'ViInt32'
    },
    1150338: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the output polarity of the Data marker event.'
        },
        'enum': 'DataMarkerEventLevelPolarity',
        'lv_property': 'Events:Data Marker:Level:Active Level',
        'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY',
        'supported_rep_caps': [
            'data_markers'
        ],
        'type': 'ViInt32'
    },
    1150339: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the destination terminal for the Data Marker Event.'
        },
        'lv_property': 'Events:Data Marker:Output Terminal',
        'name': 'DATA_MARKER_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'data_markers'
        ],
        'type': 'ViString'
    },
    1150340: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width for the Marker Event.'
        },
        'lv_property': 'Events:Marker:Pulse:Width Value',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViReal64'
    },
    1150341: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the pulse width units for the Marker Event.'
        },
        'enum': 'EventPulseWidthUnits',
        'lv_property': 'Events:Marker:Pulse:Width Units',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150344: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns a bit field of the live status of all Marker Events.'
        },
        'lv_property': 'Events:Marker:Advanced:All Marker Events Live Status',
        'name': 'ALL_MARKER_EVENTS_LIVE_STATUS',
        'type': 'ViInt32'
    },
    1150349: {
        'access': 'read-write',
        'documentation': {
            'description': 'Returns a bit field of the latched status of all Marker Events.  Write 0 to this attribute to clear the latched status of all Marker Events.'
        },
        'lv_property': 'Events:Marker:Advanced:All Marker Events Latched Status',
        'name': 'ALL_MARKER_EVENTS_LATCHED_STATUS',
        'type': 'ViInt32'
    },
    1150365: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.'
        },
        'enum': 'TerminalConfiguration',
        'lv_property': 'Output:Terminal Configuration',
        'name': 'TERMINAL_CONFIGURATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150366: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This attribute applies only when you set the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute to NIFGEN_VAL_DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.'
        },
        'lv_property': 'Output:Common Mode Offset',
        'name': 'COMMON_MODE_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150367: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Sample Clock Timebase source.\nTo change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'SampleClockTimebaseSource',
        'lv_property': 'Clocks:Sample Clock Timebase:Source',
        'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'type': 'ViString'
    },
    1150368: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Sample clock timebase rate. This attribute applies only to external Sample clock timebases.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Rate',
        'name': 'SAMPLE_CLOCK_TIMEBASE_RATE',
        'type': 'ViReal64'
    },
    1150369: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this attribute can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.'
        },
        'lv_property': 'Output:Channel Delay',
        'name': 'CHANNEL_DELAY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150373: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this attribute. Set this attribute to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150374: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.\nRecommended values for this attribute are powers of two between 64 and 512.\nIn some cases, the signal generator generates packets smaller than  the preferred size you set with this attribute.\nYou cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.\n',
            'note': '\n:\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'type': 'ViInt32'
    },
    1150375: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum number of concurrent PCI Express read requests the signal generator can issue.\nWhen transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the signal generator supports.\nIf other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests',
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'type': 'ViInt32'
    },
    1150376: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this attribute to generate samples at a rate higher than your external clock rate.  When using this attribute, you do not need to explicitly set the external clock rate.'
        },
        'lv_property': 'Clocks:Advanced:External Sample Clock Multiplier',
        'name': 'EXTERNAL_SAMPLE_CLOCK_MULTIPLIER',
        'type': 'ViReal64'
    },
    1150377: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.'
        },
        'enum': 'IdleBehavior',
        'lv_property': 'Output:Advanced:Idle Behavior',
        'name': 'IDLE_BEHAVIOR',
        'type': 'ViInt32'
    },
    1150378: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.'
        },
        'lv_property': 'Output:Advanced:Idle Value',
        'name': 'IDLE_VALUE',
        'type': 'ViInt32'
    },
    1150379: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.'
        },
        'enum': 'WaitBehavior',
        'lv_property': 'Output:Advanced:Wait Behavior',
        'name': 'WAIT_BEHAVIOR',
        'type': 'ViInt32'
    },
    1150380: {
        'access': 'read-write',
        'documentation': {
            'description': 'Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.'
        },
        'lv_property': 'Output:Advanced:Wait Value',
        'name': 'WAIT_VALUE',
        'type': 'ViInt32'
    },
    1150390: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the module revision  for the device that you are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision',
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150409: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': 'Specifies the maximum amount of time allowed to complete a streaming write operation.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150411: {
        'access': 'read-write',
        'documentation': {
            'description': 'Controls the specified auxiliary power pin. Setting this attribute to TRUE energizes the auxiliary power when the session is committed. When this attribute is FALSE, the power pin of the connector outputs no power.'
        },
        'lv_property': 'Output:Advanced:AUX Power Enabled',
        'name': 'AUX_POWER_ENABLED',
        'type': 'ViBoolean'
    },
    1150412: {
        'access': 'read only',
        'documentation': {
            'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.'
        },
        'lv_property': 'Instrument:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150413: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the sub-Sample Clock delay, in seconds, to apply to the\nwaveform. Use this property to reduce the trigger jitter when\nsynchronizing multiple devices with NI-TClk. This property can also help\nmaintain synchronization repeatability by writing the absolute delay\nvalue of a previous measurement to the current session.\nTo set this property, the waveform generator must be in the Idle\n(Configuration) state.\n**Units**: seconds (s)\n**Valid Values**: Plus or minus half of one Sample Clock period\n**Default Value**: 0.0\n**Supported Waveform Generators**: PXIe-5413/5423/5433\n',
            'note': '\nIf this property is set, NI-TClk cannot perform any sub-Sample Clock\nadjustment.\n'
        },
        'lv_property': 'Output:Absolute Delay',
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': 'Sets which output mode the signal generator will use. The value you specify determines which functions and attributes you use to configure the waveform the signal generator produces.',
            'note': 'The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.'
        },
        'enum': 'OutputMode',
        'lv_property': 'Output:Output Mode',
        'name': 'OUTPUT_MODE',
        'type': 'ViInt32'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': 'This channel-based attribute specifies whether the signal that the signal generator produces appears at the output connector.'
        },
        'lv_property': 'Output:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250004: {
        'access': 'read-write',
        'documentation': {
            'description': 'This channel-based attribute specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.'
        },
        'grpc_enum': 'OutputImpedance',
        'lv_property': 'Output:Output Impedance',
        'name': 'OUTPUT_IMPEDANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis channel-based attribute specifies which standard waveform the signal generator produces.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to  NIFGEN_VAL_OUTPUT_FUNC.\nNIFGEN_VAL_WFM_SINE      - Sinusoid waveform\nNIFGEN_VAL_WFM_SQUARE    - Square waveform\nNIFGEN_VAL_WFM_TRIANGLE  - Triangle waveform\nNIFGEN_VAL_WFM_RAMP_UP   - Positive ramp waveform\nNIFGEN_VAL_WFM_RAMP_DOWN - Negative ramp waveform\nNIFGEN_VAL_WFM_DC        - Constant voltage\nNIFGEN_VAL_WFM_NOISE     - White noise\nNIFGEN_VAL_WFM_USER      - User-defined waveform as defined with\nniFgen_DefineUserStandardWaveform\n'
        },
        'enum': 'Waveform',
        'lv_property': 'Standard Function:Waveform',
        'name': 'FUNC_WAVEFORM',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250102: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.\nFor example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.\nset the Waveform parameter to NIFGEN_VAL_WFM_DC.\nUnits: Vpk-pk\n',
            'note': 'This parameter does not affect signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Amplitude',
        'name': 'FUNC_AMPLITUDE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250103: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.\nFor example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.\nUnits: volts\n'
        },
        'lv_property': 'Standard Function:DC Offset',
        'name': 'FUNC_DC_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250104: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls the frequency of the standard waveform that the  signal generator produces.\nUnits: hertz\n(1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the niFgen_ConfigureStandardWaveform function  to NIFGEN_VAL_WFM_DC.\n(2) For NIFGEN_VAL_WFM_SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.\n',
            'note': '\n:\n'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Frequency',
        'name': 'FUNC_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250105: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls horizontal offset of the standard waveform the  signal generator produces. Specify this attribute in degrees of  one waveform cycle.\nA start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.\nset the Waveform parameter to NIFGEN_VAL_WFM_DC.\nUnits: Degrees of one cycle\n',
            'note': 'This parameter does not affect signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Start Phase',
        'name': 'FUNC_START_PHASE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250106: {
        'access': 'read-write',
        'documentation': {
            'description': '\nControls the duty cycle of the square wave the signal generator  produces. Specify this attribute as a percentage of  the time the square wave is high in a cycle.\nset the Waveform parameter to NIFGEN_VAL_WFM_SQUARE.\nUnits: Percentage of time the waveform is high\n',
            'note': 'This parameter only affects signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Duty Cycle High',
        'name': 'FUNC_DUTY_CYCLE_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250201: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSelects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform functions:\nniFgen_CreateWaveformF64\nniFgen_CreateWaveformI16\nniFgen_CreateWaveformFromFileI16\nniFgen_CreateWaveformFromFileF64\nThese functions return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this attribute to the waveform handle.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\n'
        },
        'grpc_enum': 'ArbitraryWaveformHandle',
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle',
        'name': 'ARB_WAVEFORM_HANDLE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250202: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to scale the arbitrary waveform to other ranges.\nFor example, when you set this attribute to 2.0, the output signal ranges from -2.0 V to +2.0 V.\nUse this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\n'
        },
        'lv_property': 'Arbitrary Waveform:Gain',
        'name': 'ARB_GAIN',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250203: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to shift the arbitrary waveform range.\nFor example, when you set this attribute to 1.0, the output signal ranges from 2.0 V to 0.0 V.\nUse this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\nUnits: Volts\n'
        },
        'lv_property': 'Arbitrary Waveform:Offset',
        'name': 'ARB_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250204: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set  to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\nUnits: Samples/s\n'
        },
        'grpc_enum': 'SampleRate',
        'lv_property': 'Clocks:Sample Clock:Rate',
        'name': 'ARB_SAMPLE_RATE',
        'type': 'ViReal64'
    },
    1250205: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Number of Waveforms',
        'name': 'MAX_NUM_WAVEFORMS',
        'type': 'ViInt32'
    },
    1250206: {
        'access': 'read only',
        'documentation': {
            'description': '\nThe size of each arbitrary waveform must be a multiple of a quantum value. This attribute returns the quantum value that the signal generator allows.\nFor example, when this attribute returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.\n'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Waveform Quantum',
        'name': 'WAVEFORM_QUANTUM',
        'type': 'ViInt32'
    },
    1250207: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Min Waveform Size',
        'name': 'MIN_WAVEFORM_SIZE',
        'type': 'ViInt32'
    },
    1250208: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the size, in samples, of the largest waveform that can be created. This attribute reflects the space currently available, taking into account previously allocated waveforms and instructions.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Waveform Size',
        'name': 'MAX_WAVEFORM_SIZE',
        'type': 'ViInt32'
    },
    1250211: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis channel-based attribute identifies which sequence the signal generator produces. You can create multiple sequences using niFgen_CreateArbSequence. niFgen_CreateArbSequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this attribute to the sequence handle.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SEQ.\n'
        },
        'grpc_enum': 'ArbitrarySequenceHandle',
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle',
        'name': 'ARB_SEQUENCE_HANDLE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250212: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences',
        'name': 'MAX_NUM_SEQUENCES',
        'type': 'ViInt32'
    },
    1250213: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length',
        'name': 'MIN_SEQUENCE_LENGTH',
        'type': 'ViInt32'
    },
    1250214: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length',
        'name': 'MAX_SEQUENCE_LENGTH',
        'type': 'ViInt32'
    },
    1250215: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count',
        'name': 'MAX_LOOP_COUNT',
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nifgen/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/config.py sha256=e5dc3bbae170e5717386392089918bb2ebe705929244fb815578dfe1ee9ca578 bytes=1625 -->
## FILE: src/nifgen/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/config.py`
- sha256: `e5dc3bbae170e5717386392089918bb2ebe705929244fb815578dfe1ee9ca578`
- bytes: 1625

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 25.0.0f114
config = {
    'api_version': '25.0.0f114',
    'c_function_prefix': 'niFgen_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortGeneration',
        'initiate_function': 'InitiateGeneration',
        'task': 'generation'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-FGEN',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiFgen',
    'init_function': 'InitializeWithChannels',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifgen',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niFgen_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niFgen_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nifgen',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': 'ScriptTrigger',
            'python_name': 'script_triggers'
        },
        {
            'prefix': 'Marker',
            'python_name': 'markers'
        },
        {
            'prefix': 'DataMarker',
            'python_name': 'data_markers'
        }
    ],
    'session_class_description': 'An NI-FGEN session to an NI signal generator.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/config_addon.py sha256=7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2 bytes=259 -->
## FILE: src/nifgen/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/config_addon.py`
- sha256: `7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2017',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/enums.py sha256=49ad5eae1ef57b4924a814d1ef60eebb77a24ca0160b41e82f4911fc1be9d305 bytes=53299 -->
## FILE: src/nifgen/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/enums.py`
- sha256: `49ad5eae1ef57b4924a814d1ef60eebb77a24ca0160b41e82f4911fc1be9d305`
- bytes: 53299

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 25.0.0f114
enums = {
    'AnalogPath': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.'
                },
                'name': 'NIFGEN_VAL_MAIN_ANALOG_PATH',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies use of the direct path.'
                },
                'name': 'NIFGEN_VAL_DIRECT_ANALOG_PATH',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.'
                },
                'name': 'NIFGEN_VAL_FIXED_LOW_GAIN_ANALOG_PATH',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Specifies use of the high-gain amplifier in the main path.'
                },
                'name': 'NIFGEN_VAL_FIXED_HIGH_GAIN_ANALOG_PATH',
                'value': 3
            }
        ]
    },
    'BusType': {
        'values': [
            {
                'documentation': {
                    'description': 'Indicates an invalid bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_INVALID',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the AT bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_AT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PCI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PCI',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PXI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PXI',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the VXI bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_VXI',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PCI-CMA bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PCMCIA',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Indicates the signal generator is the PXI Express bus type.'
                },
                'name': 'NIFGEN_VAL_BUS_PXIE',
                'value': 6
            }
        ]
    },
    'ByteOrder': {
        'values': [
            {
                'name': 'NIFGEN_VAL_LITTLE_ENDIAN',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_BIG_ENDIAN',
                'value': 1
            }
        ]
    },
    'ClockMode': {
        'values': [
            {
                'documentation': {
                    'description': 'High resolution sampling—Sample rate is generated by a high–resolution clock source.'
                },
                'name': 'NIFGEN_VAL_HIGH_RESOLUTION',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Divide down sampling—Sample rates are generated by dividing the source frequency.'
                },
                'name': 'NIFGEN_VAL_DIVIDE_DOWN',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.'
                },
                'name': 'NIFGEN_VAL_AUTOMATIC',
                'value': 2
            }
        ]
    },
    'DataMarkerEventLevelPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DataProcessingMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The waveform data points are real numbers (I data).'
                },
                'name': 'NIFGEN_VAL_OSP_REAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The waveform data points are complex numbers (I/Q data).'
                },
                'name': 'NIFGEN_VAL_OSP_COMPLEX',
                'value': 1
            }
        ]
    },
    'DoneEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DoneEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'DoneEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'DoneEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'EventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'python_name': 'SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'python_name': 'SECONDS',
                'value': 102
            }
        ]
    },
    'FilterType': {
        'values': [
            {
                'documentation': {
                    'description': 'Applies a flat filter to the data with the passband value specified  in the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_FLAT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Applies a raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_RAISED_COSINE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Applies a root raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Applies a Gaussian filter to the data with the BT value specified in the  NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT attribute.'
                },
                'name': 'NIFGEN_VAL_OSP_GAUSSIAN',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Applies a custom filter to the data. If NIFGEN_VAL_OSP_CUSTOM is selected,  you must provide a set of FIR filter coefficients with the  niFgen_ConfigureCustomFIRFilterCoefficients function.'
                },
                'name': 'NIFGEN_VAL_OSP_CUSTOM',
                'value': 4
            }
        ]
    },
    'HardwareState': {
        'values': [
            {
                'name': 'NIFGEN_VAL_IDLE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                'value': 100
            },
            {
                'name': 'NIFGEN_VAL_RUNNING',
                'value': 200
            },
            {
                'name': 'NIFGEN_VAL_DONE',
                'value': 600
            },
            {
                'name': 'NIFGEN_VAL_HARDWARE_ERROR',
                'value': 1000
            }
        ]
    },
    'IdleBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.'
                },
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.'
                },
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'MarkerEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            },
            {
                'documentation': {
                    'description': '\nChanges to high or low while the event is active, depending on the\nactive state you specify.\n'
                },
                'name': 'NIFGEN_VAL_TOGGLE',
                'value': 103
            }
        ]
    },
    'MarkerEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the initial state of the Marker event to high.'
                },
                'name': 'NIFGEN_VAL_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Sets the initial state of the Marker event to low.'
                },
                'name': 'NIFGEN_VAL_LOW',
                'value': 102
            }
        ]
    },
    'OperationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Continuous Operation'
                },
                'name': 'NIFGEN_VAL_OPERATE_CONTINUOUS',
                'value': 0
            }
        ]
    },
    'OspMode': {
        'values': [
            {
                'documentation': {
                    'description': 'The OSP block generates intermediate frequency (IF) data.'
                },
                'name': 'NIFGEN_VAL_OSP_IF',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The OSP block generates baseband data.'
                },
                'name': 'NIFGEN_VAL_OSP_BASEBAND',
                'value': 1
            }
        ]
    },
    'OspOverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-FGEN returns errors whenever an overflow has occurred in the OSP block.'
                },
                'name': 'NIFGEN_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-FGEN does not return errors when an overflow occurs in the OSP block.'
                },
                'name': 'NIFGEN_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'OutputMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Standard Function mode—  Generates standard function waveforms  such as sine, square, triangle, and so on.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_FUNC',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_ARB',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_SEQ',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Frequency List mode—Generates a  standard function using a list of  frequencies you define.'
                },
                'name': 'NIFGEN_VAL_OUTPUT_FREQ_LIST',
                'value': 101
            },
            {
                'documentation': {
                    'description': '\n**Script mode—**\\ Allows you to use scripting to link and loop multiple\nwaveforms in complex combinations.\n'
                },
                'name': 'NIFGEN_VAL_OUTPUT_SCRIPT',
                'value': 102
            }
        ]
    },
    'P2PAddressType': {
        'values': [
            {
                'documentation': {
                    'description': 'Physical'
                },
                'name': 'NIFGEN_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Physical'
                },
                'name': 'NIFGEN_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'ReadyForStartEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ReferenceClockSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the CLK IN input signal from the front panel connector is\nused as the Reference Clock source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN_COLLISION_AVOIDANCE',
                'python_name': 'CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that a Reference Clock is not used.'
                },
                'name': 'NIFGEN_VAL_NONE_COLLISION_AVOIDANCE',
                'python_name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the onboard Reference Clock is used as the Reference\nClock source.\n'
                },
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE',
                'python_name': 'ONBOARD_REFERENCE_CLOCK',
                'value': 'OnboardRefClk'
            },
            {
                'documentation': {
                    'description': 'Specifies that the PXI Clock is used as the Reference Clock source.'
                },
                'name': 'NIFGEN_VAL_PXI_CLOCK_COLLISION_AVOIDANCE',
                'python_name': 'PXI_CLOCK',
                'value': 'PXI_Clk'
            },
            {
                'documentation': {
                    'description': 'Specifies that the RTSI line 7 is used as the Reference Clock source.'
                },
                'name': 'NIFGEN_VAL_RTSI_7_COLLISION_AVOIDANCE',
                'python_name': 'RTSI_7',
                'value': 'RTSI7'
            }
        ]
    },
    'RelativeTo': {
        'values': [
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_START',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT',
                'value': 1
            }
        ]
    },
    'SampleClockSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the signal at the CLK IN front panel connector is used as\nthe Sample Clock source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the Sample Clock from the DDC connector is used as the Sample\nClock source.\n'
                },
                'name': 'NIFGEN_VAL_DDC_CLOCK_IN',
                'value': 'DDC_ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that the onboard clock is used as the Sample Clock source.'
                },
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI\\_STAR trigger line is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_STAR_LINE',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 0 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_0_RTSI_0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 1 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_1_RTSI_1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 2 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_2_RTSI_2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 3 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_3_RTSI_3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 4 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_4_RTSI_4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 5 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_5_RTSI_5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 6 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_6_RTSI_6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': '\nSpecifies that the PXI or RTSI line 7 is used as the Sample Clock\nsource.\n'
                },
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_7_RTSI_7',
                'value': 'PXI_Trig7'
            }
        ]
    },
    'SampleClockTimebaseSource': {
        'values': [
            {
                'documentation': {
                    'description': '\nSpecifies that the external signal on the CLK IN front panel connector\nis used as the source.\n'
                },
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'Specifies that the onboard Sample Clock timebase is used as the source.'
                },
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            }
        ]
    },
    'ScriptTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edge'
                },
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'ScriptTriggerDigitalLevelActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'High Level'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Low Level'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ScriptTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured. Signal generation starts immediately.'
                },
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a digital edge is detected.'
                },
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a digital level is detected.'
                },
                'name': 'NIFGEN_VAL_DIGITAL_LEVEL',
                'value': 103
            },
            {
                'documentation': {
                    'description': 'Trigger is asserted when a software edge is detected.'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002
            },
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_MARKER_EVENT',
                'value': 1001
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                'value': 1006
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_REFERENCE_CLOCK',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            },
            {
                'name': 'NIFGEN_VAL_READY_FOR_START_EVENT',
                'value': 105
            },
            {
                'name': 'NIFGEN_VAL_STARTED_EVENT',
                'value': 106
            },
            {
                'name': 'NIFGEN_VAL_DONE_EVENT',
                'value': 107
            },
            {
                'name': 'NIFGEN_VAL_DATA_MARKER_EVENT',
                'value': 108
            }
        ]
    },
    'StartTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Rising Edge'
                },
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Falling Edge'
                },
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'StartTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'None'
                },
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Digital Edge'
                },
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'documentation': {
                    'description': 'Software Edge'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            },
            {
                'documentation': {
                    'description': 'P2P Endpoint Fullness'
                },
                'name': 'NIFGEN_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 106
            }
        ]
    },
    'StartedEventActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'StartedEventDelayUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the pulse width in Sample clock periods.'
                },
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Specifies the pulse width in seconds.'
                },
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'StartedEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Triggers a pulse for a specified period of time.'
                },
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'Shifts high or low while the event is active, depending  on the active state you specify.'
                },
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'StartedEventPulsePolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is high.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'When the operation is ready to start, the Ready for Start  event level is low.'
                },
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'SynchronizationSource': {
        'values': [
            {
                'documentation': {
                    'description': 'PXI TRIG0 or VXI TTL0'
                },
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI TRIG1 or VXI TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI TRIG2 or VXI TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI TRIG3 or VXI TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI TRIG4 or VXI TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI TRIG5 or VXI TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI TRIG6 or VXI TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'RTSI 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'No Synchronization Source'
                },
                'name': 'NIFGEN_VAL_NONE',
                'value': 1000
            }
        ]
    },
    'TerminalConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': 'Single-ended operation'
                },
                'name': 'NIFGEN_VAL_SINGLE_ENDED',
                'value': 300
            },
            {
                'documentation': {
                    'description': 'Differential operation'
                },
                'name': 'NIFGEN_VAL_DIFFERENTIAL',
                'value': 301
            }
        ]
    },
    'Trigger': {
        'values': [
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            }
        ]
    },
    'TriggerMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.'
                },
                'name': 'NIFGEN_VAL_SINGLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.'
                },
                'name': 'NIFGEN_VAL_CONTINUOUS',
                'value': 2
            },
            {
                'documentation': {
                    'description': '\nStepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.\ntrigger mode.\n',
                    'note': 'In Frequency List mode, Stepped trigger mode is the same as Burst'
                },
                'name': 'NIFGEN_VAL_STEPPED',
                'value': 3
            },
            {
                'documentation': {
                    'description': '\nBurst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.\ntrigger mode.\n',
                    'note': 'In Frequency List mode, Stepped trigger mode is the same as Burst'
                },
                'name': 'NIFGEN_VAL_BURST',
                'value': 4
            }
        ]
    },
    'TriggerSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Immediate-The signal generator does not wait for a trigger of any kind.'
                },
                'name': 'NIFGEN_VAL_IMMEDIATE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External-The signal generator waits for a trigger on the external trigger input'
                },
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Software Trigger-The signal generator waits until you call niFgen_SendSWTrigger.'
                },
                'name': 'NIFGEN_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PXI TRIG0 or VXI TTL0'
                },
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'PXI TRIG1 or VXI TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'PXI TRIG2 or VXI TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'PXI TRIG3 or VXI TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'PXI TRIG4 or VXI TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'PXI TRIG5 or VXI TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'PXI TRIG6 or VXI TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI star'
                },
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'RTSI line 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI line 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI line 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI line 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI line 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI line 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI line 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'RTSI line 7'
                },
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'documentation': {
                    'description': 'PFI 0'
                },
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'documentation': {
                    'description': 'PFI 1'
                },
                'name': 'NIFGEN_VAL_PFI_1',
                'value': 1012
            },
            {
                'documentation': {
                    'description': 'PFI 2'
                },
                'name': 'NIFGEN_VAL_PFI_2',
                'value': 1013
            },
            {
                'documentation': {
                    'description': 'PFI 3'
                },
                'name': 'NIFGEN_VAL_PFI_3',
                'value': 1014
            },
            {
                'documentation': {
                    'description': 'Specifies that another terminal is used.'
                },
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            }
        ]
    },
    'TriggerWhen': {
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'UpdateClockSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Internal Update Clock'
                },
                'name': 'NIFGEN_VAL_INTERNAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External update clock given on the IO front panel connector'
                },
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'TTL1'
                },
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'TTL2'
                },
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'TTL3'
                },
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'TTL4'
                },
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'TTL5'
                },
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'TTL6'
                },
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'PXI Star Trigger Line'
                },
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'documentation': {
                    'description': 'RTSI 0'
                },
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'documentation': {
                    'description': 'RTSI 1'
                },
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'documentation': {
                    'description': 'RTSI 2'
                },
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'documentation': {
                    'description': 'RTSI 3'
                },
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'documentation': {
                    'description': 'RTSI 4'
                },
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'documentation': {
                    'description': 'RTSI 5'
                },
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'documentation': {
                    'description': 'RTSI 6'
                },
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'documentation': {
                    'description': 'RTSI 7'
                },
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'documentation': {
                    'description': 'Uses another device terminal.'
                },
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            },
            {
                'documentation': {
                    'description': 'CLK IN front panel connector'
                },
                'name': 'NIFGEN_VAL_CLK_IN',
                'value': 1202
            },
            {
                'documentation': {
                    'description': 'DDC CLK IN line of the Digital Data & Control front panel connector'
                },
                'name': 'NIFGEN_VAL_DDC_CLK_IN',
                'value': 1203
            }
        ]
    },
    'VideoWaveformType': {
        'values': [
            {
                'documentation': {
                    'description': 'PAL B Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_B',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'PAL D Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_D',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'PAL G Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_G',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'PAL H Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_H',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'PAL I Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_I',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'PAL M Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_M',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'PAL N Video Type'
                },
                'name': 'NIFGEN_VAL_PAL_N',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'NTSC M Video Type'
                },
                'name': 'NIFGEN_VAL_NTSC_M',
                'value': 7
            }
        ]
    },
    'WaitBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.'
                },
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'documentation': {
                    'description': 'While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.'
                },
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'Waveform': {
        'values': [
            {
                'documentation': {
                    'description': 'Sinusoid waveform'
                },
                'name': 'NIFGEN_VAL_WFM_SINE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Square waveform'
                },
                'name': 'NIFGEN_VAL_WFM_SQUARE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Triange waveform'
                },
                'name': 'NIFGEN_VAL_WFM_TRIANGLE',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Positive ramp waveform'
                },
                'name': 'NIFGEN_VAL_WFM_RAMP_UP',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Negative ramp waveform'
                },
                'name': 'NIFGEN_VAL_WFM_RAMP_DOWN',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Constant voltage'
                },
                'name': 'NIFGEN_VAL_WFM_DC',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'White noise'
                },
                'name': 'NIFGEN_VAL_WFM_NOISE',
                'value': 101
            },
            {
                'documentation': {
                    'description': 'User-defined waveform as defined by the niFgen_DefineUserStandardWaveform function.'
                },
                'name': 'NIFGEN_VAL_WFM_USER',
                'value': 102
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nifgen/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/functions.py sha256=3f0be76875af6b97f148d21d977a7f789772cba50611ad4049ab378aaae3786d bytes=197656 -->
## FILE: src/nifgen/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/functions.py`
- sha256: `3f0be76875af6b97f148d21d977a7f789772cba50611ad4049ab378aaae3786d`
- bytes: 197656

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 25.0.0f114
functions = {
    'AbortGeneration': {
        'documentation': {
            'description': '\nAborts any previously initiated signal generation. Call the\nnifgen_InitiateGeneration function to cause the signal generator to\nproduce a signal again.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'abort',
        'returns': 'ViStatus'
    },
    'AllocateNamedWaveform': {
        'documentation': {
            'description': '\nSpecifies the size of a named waveform up front so that it can be\nallocated in onboard memory before loading the associated data. Data can\nthen be loaded in smaller blocks with the niFgen Write (Binary16)\nWaveform functions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to allocate the named\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the waveform to allocate in samples.\n\n**Default Value**: "4096"\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateWaveform': {
        'documentation': {
            'description': '\nSpecifies the size of a waveform so that it can be allocated in onboard\nmemory before loading the associated data. Data can then be loaded in\nsmaller blocks with the Write Binary 16 Waveform functions.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to allocate the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies, in samples, the size of the waveform to allocate.'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbMemory': {
        'documentation': {
            'description': '\nRemoves all previously created arbitrary waveforms, sequences, and\nscripts from the signal generator memory and invalidates all waveform\nhandles, sequence handles, and waveform names.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbSequence': {
        'documentation': {
            'description': '\nRemoves a previously created arbitrary sequence from the signal\ngenerator memory and invalidates the sequence handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary sequence that you want the signal\ngenerator to remove. You can create an arbitrary sequence using the\nnifgen_CreateArbSequence or nifgen_CreateAdvancedArbSequence function.\nThese functions return a handle that you use to identify the sequence.\n\n| **Defined Value**:\n| NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal\n  generator\n\n**Default Value**: None\n'
                },
                'grpc_enum': 'SequenceHandle',
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRemoves a previously created arbitrary waveform from the signal\ngenerator memory and invalidates the waveform handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'delete_waveform',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform that you want the signal\ngenerator to remove.\n\nYou can create multiple arbitrary waveforms using one of the following\nniFgen Create Waveform functions:\n\n-  niFgen_CreateWaveformF64\n-  niFgen_CreateWaveformI16\n-  niFgen_CreateWaveformFromFileI16\n-  niFgen_CreateWaveformFromFileF64\n\n**Defined Value**:\n\nNIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal\ngenerator.\n\n**Default Value**: None\n'
                },
                'grpc_enum': 'WaveformHandle',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearFreqList': {
        'documentation': {
            'description': '\nRemoves a previously created frequency list from the signal generator\nmemory and invalidates the frequency list handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the frequency list you want the signal generator\nto remove. You create multiple frequency lists using\nniFgen_CreateFreqList. niFgen_CreateFreqList returns a handle that you\nuse to identify each list. Specify a value of -1 to clear all frequency\nlists.\n\n**Defined Value**\n\nNIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal\ngenerator.\n\n**Default Value**: None\n'
                },
                'grpc_enum': 'FrequencyListOptions',
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearUserStandardWaveform': {
        'documentation': {
            'description': '\nClears the user-defined waveform created by the\nnifgen_DefineUserStandardWaveform function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name from which you want to clear a user standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nCauses a transition to the Committed state. This function verifies\nattribute values, reserves the device, and commits the attribute values\nto the device. If the attribute values are all valid, NI-FGEN sets the\ndevice hardware configuration to match the session configuration. This\nfunction does not support the NI 5401/5404/5411/5431 signal generators.\n\nIn the Committed state, you can load waveforms, scripts, and sequences\ninto memory. If any attributes are changed, NI-FGEN implicitly\ntransitions back to the Idle state, where you can program all session\nproperties before applying them to the device. This function has no\neffect if the device is already in the Committed or Generating state and\nreturns a successful status value.\n\nCalling this VI before the niFgen Initiate Generation VI is optional but\nhas the following benefits:\n\n-  Routes are committed, so signals are exported or imported.\n-  Any Reference Clock and external clock circuits are phase-locked.\n-  A subsequent niFgen_InitiateGeneration function can run faster\n   because the device is already configured.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbSequence': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the signal generator attributes that affect arbitrary\nsequence generation. Sets the NIFGEN_ATTR_ARB_SEQUENCE_HANDLE,\nNIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name from which you want to configure an arbitrary\nsequence.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary sequence that you want the signal\ngenerator to produce. NI-FGEN sets the\nNIFGEN_ATTR_ARB_SEQUENCE_HANDLE attribute to this value. You can\ncreate an arbitrary sequence using the niFgen_CreateArbSequence or\nniFgen_CreateAdvancedArbSequence function. These functions return a\nhandle that you use to identify the sequence.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the factor by which the signal generator scales the arbitrary\nwaveforms in the sequence. When you create an arbitrary waveform, you\nmust first normalize the data points to a range of –1.00 to +1.00. You\ncan use this parameter to scale the waveform to other ranges. The gain\nis applied before the offset is added.\n\nFor example, to configure the output signal to range from –2.00 to\n+2.00 V, set **gain** to 2.00.\n\n**Units**: unitless\n\n**Default Value**: None\n'
                },
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value the signal generator adds to the arbitrary waveform\ndata. When you create arbitrary waveforms, you must first normalize the\ndata points to a range of –1.00 to +1.00 V. You can use this parameter\nto shift the range of the arbitrary waveform. NI-FGEN sets the\nNIFGEN_ATTR_ARB_OFFSET attribute to this value.\n\nFor example, to configure the output signal to range from 0.00 to 2.00 V\ninstead of –1.00 to 1.00 V, set the offset to 1.00.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the attributes of the signal generator that affect arbitrary\nwaveform generation. Sets the NIFGEN_ATTR_ARB_WAVEFORM_HANDLE,\nNIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure an arbitrary\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform you want the signal\ngenerator to produce. NI-FGEN sets the\nNIFGEN_ATTR_ARB_WAVEFORM_HANDLE attribute to this value. You can\ncreate an arbitrary waveform using one of the following niFgen Create\nWaveform functions:\n\n-  niFgen_CreateWaveformF64\n-  niFgen_CreateWaveformI16\n-  niFgen_CreateWaveformFromFileI16\n-  niFgen_CreateWaveformFromFileF64\n\nThese functions return a handle that you use to identify the waveform.\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the factor by which the signal generator scales the arbitrary\nwaveforms in the sequence. When you create an arbitrary waveform, you\nmust first normalize the data points to a range of –1.00 to +1.00. You\ncan use this parameter to scale the waveform to other ranges. The gain\nis applied before the offset is added.\n\nFor example, to configure the output signal to range from –2.00 to\n+2.00 V, set **gain** to 2.00.\n\n**Units**: unitless\n\n**Default Value**: None\n'
                },
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value the signal generator adds to the arbitrary waveform\ndata. When you create arbitrary waveforms, you must first normalize the\ndata points to a range of –1.00 to +1.00 V. You can use this parameter\nto shift the range of the arbitrary waveform. NI-FGEN sets the\nNIFGEN_ATTR_ARB_OFFSET attribute to this value.\n\nFor example, to configure the output signal to range from 0.00 to 2.00 V\ninstead of –1.00 to 1.00 V, set the offset to 1.00.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFreqList': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the attributes of the signal generator that affect frequency\nlist generation (the NIFGEN_ATTR_FREQ_LIST_HANDLE,\nNIFGEN_ATTR_FUNC_AMPLITUDE, NIFGEN_ATTR_FUNC_DC_OFFSET, and\nNIFGEN_ATTR_FUNC_START_PHASE attributes).\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the frequency\nlist.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the frequency list that you want the signal\ngenerator to produce. NI-FGEN sets the NIFGEN_ATTR_FREQ_LIST_HANDLE\nattribute to this value. You can create a frequency list using the\nniFgen_CreateFreqList function, which returns a handle that you use to\nidentify the list.\n**Default Value**: None\n'
                },
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude of the standard waveform that you want the\nsignal generator to produce. This value is the amplitude at the output\nterminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to\nthis value.\n\nFor example, to produce a waveform ranging from –5.00 V to +5.00 V, set\nthe amplitude to 10.00 V.\n\n**Units**: peak-to-peak voltage\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the DC offset of the standard waveform that you want the\nsignal generator to produce. The value is the offset from ground to the\ncenter of the waveform you specify with the **waveform** parameter,\nobserved at the output terminal. For example, to configure a waveform\nwith an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the\n**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET\nattribute to this value.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the horizontal offset of the standard waveform you want the\nsignal generator to produce. Specify this attribute in degrees of one\nwaveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE\nattribute to this value. A start phase of 180 degrees means output\ngeneration begins halfway through the waveform. A start phase of 360\ndegrees offsets the output by an entire waveform cycle, which is\nidentical to a start phase of 0 degrees.\n\n**Units**: degrees of one cycle\n\n**Default Value**: None degrees\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureStandardWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the following attributes of the signal generator that affect\nstandard waveform generation:\n\n-  NIFGEN_ATTR_FUNC_WAVEFORM\n-  NIFGEN_ATTR_FUNC_AMPLITUDE\n-  NIFGEN_ATTR_FUNC_DC_OFFSET\n-  NIFGEN_ATTR_FUNC_FREQUENCY\n-  NIFGEN_ATTR_FUNC_START_PHASE\n',
            'note': '\nYou must call the niFgen_ConfigureOutputMode function with the\n**outputMode** parameter set to NIFGEN_VAL_OUTPUT_FUNC before calling\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure a standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the standard waveform that you want the signal generator to\nproduce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this\nvalue.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_WFM_SINE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WFM_SINE',
                            'Specifies that the signal generator produces a sinusoid waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_SQUARE',
                            'Specifies that the signal generator produces a square waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_TRIANGLE',
                            'Specifies that the signal generator produces a triangle waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_UP',
                            'Specifies that the signal generator produces a positive ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_DOWN',
                            'Specifies that the signal generator produces a negative ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_DC',
                            'Specifies that the signal generator produces a constant voltage.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_NOISE',
                            'Specifies that the signal generator produces white noise.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_USER',
                            'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.'
                        ]
                    ]
                },
                'enum': 'Waveform',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude of the standard waveform that you want the\nsignal generator to produce. This value is the amplitude at the output\nterminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to\nthis value.\n\nFor example, to produce a waveform ranging from –5.00 V to +5.00 V, set\nthe amplitude to 10.00 V.\n\n**Units**: peak-to-peak voltage\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the DC offset of the standard waveform that you want the\nsignal generator to produce. The value is the offset from ground to the\ncenter of the waveform you specify with the **waveform** parameter,\nobserved at the output terminal. For example, to configure a waveform\nwith an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the\n**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET\nattribute to this value.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the frequency of the standard waveform that you want the\n  signal generator to produce. NI-FGEN sets the\n  NIFGEN_ATTR_FUNC_FREQUENCY attribute to this value.\n\n**Units**: hertz\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the horizontal offset of the standard waveform that you want\nthe signal generator to produce. Specify this parameter in degrees of\none waveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE\nattribute to this value. A start phase of 180 degrees means output\ngeneration begins halfway through the waveform. A start phase of 360\ndegrees offsets the output by an entire waveform cycle, which is\nidentical to a start phase of 0 degrees.\n\n**Units**: degrees of one cycle\n\n**Default Value**: 0.00\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedArbSequence': {
        'documentation': {
            'description': '\nCreates an arbitrary sequence from an array of waveform handles and an\narray of corresponding loop counts. This function returns a handle that\nidentifies the sequence. You pass this handle to the\nniFgen_ConfigureArbSequence function to specify what arbitrary sequence\nyou want the signal generator to produce.\n\nThe niFgen_CreateAdvancedArbSequence function extends on the\nniFgen_CreateArbSequence function by adding the ability to set the\nnumber of samples in each sequence step and to set marker locations.\n\nAn arbitrary sequence consists of multiple waveforms. For each waveform,\nyou specify the number of times the signal generator produces the\nwaveform before proceeding to the next waveform. The number of times to\nrepeat a specific waveform is called the loop count.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this\nfunction.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveforms in the new arbitrary sequence that you\nwant to create. The value you pass must be between the minimum and\nmaximum sequence lengths that the signal generator allows. You can\nobtain the minimum and maximum sequence lengths from\n**minimumSequenceLength** and **maximumSequenceLength** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of waveform handles from which you want to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value that you specify in **sequenceLength**. Each\n**waveformHandlesArray** element has a corresponding **loopCountsArray**\nelement that indicates how many times that waveform is repeated. You\nobtain waveform handles when you create arbitrary waveforms with the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of loop counts you want to use to create a new\narbitrary sequence. The array must have at least as many elements as the\nvalue that you specify in the **sequenceLength** parameter. Each\n**loopCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates how many times to repeat that waveform. Each\nelement of the **loopCountsArray** must be less than or equal to the\nmaximum number of loop counts that the signal generator allows. You can\nobtain the maximum loop count from **maximumLoopCount** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of sample counts that you want to use to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value you specify in the **sequenceLength** parameter. Each\n**sampleCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates the subset, in samples, of the given waveform to\ngenerate. Each element of the **sampleCountsArray** must be larger than\nthe minimum waveform size, a multiple of the waveform quantum and no\nlarger than the number of samples in the corresponding waveform. You can\nobtain these values by calling the nifgen_QueryArbWfmCapabilities\nfunction.\n\n**Default Value**: None\n'
                },
                'name': 'sampleCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of marker locations to where you want a marker to be\ngenerated in the sequence. The array must have at least as many elements\nas the value you specify in the **sequenceLength** parameter. Each\n**markerLocationArray** element corresponds to a\n**waveformHandlesArray** element and indicates where in the waveform a\nmarker is to generate. The marker location must be less than the size of\nthe waveform the marker is in. The markers are coerced to the nearest\nmarker quantum and the coerced values are returned in the\n**coercedMarkersArray** parameter.\n\nIf you do not want a marker generated for a particular sequence stage,\nset this parameter to NIFGEN_VAL_NO_MARKER.\n\n**Defined Value**: NIFGEN_VAL_NO_MARKER\n\n**Default Value**: None\n'
                },
                'name': 'markerLocationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of all given markers that are coerced (rounded) to the\nnearest marker quantum. Not all devices coerce markers.\n\n**Default Value**: None\n'
                },
                'name': 'coercedMarkersArray',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(0 if marker_location_array is None else len(marker_location_array))'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new arbitrary sequence. You can\npass this handle to nifgen_ConfigureArbSequence to generate the\narbitrary sequence.\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateArbSequence': {
        'documentation': {
            'description': '\nCreates an arbitrary sequence from an array of waveform handles and an\narray of corresponding loop counts. This function returns a handle that\nidentifies the sequence. You pass this handle to the\nnifgen_ConfigureArbSequence function to specify what arbitrary sequence\nyou want the signal generator to produce.\n\nAn arbitrary sequence consists of multiple waveforms. For each waveform,\nyou can specify the number of times that the signal generator produces\nthe waveform before proceeding to the next waveform. The number of times\nto repeat a specific waveform is called the loop count.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this\nfunction.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveforms in the new arbitrary sequence that you\nwant to create. The value you pass must be between the minimum and\nmaximum sequence lengths that the signal generator allows. You can\nobtain the minimum and maximum sequence lengths from\n**minimumSequenceLength** and **maximumSequenceLength** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of waveform handles from which you want to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value that you specify in **sequenceLength**. Each\n**waveformHandlesArray** element has a corresponding **loopCountsArray**\nelement that indicates how many times that waveform is repeated. You\nobtain waveform handles when you create arbitrary waveforms with the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of loop counts you want to use to create a new\narbitrary sequence. The array must have at least as many elements as the\nvalue that you specify in the **sequenceLength** parameter. Each\n**loopCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates how many times to repeat that waveform. Each\nelement of the **loopCountsArray** must be less than or equal to the\nmaximum number of loop counts that the signal generator allows. You can\nobtain the maximum loop count from **maximumLoopCount** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new arbitrary sequence. You can\npass this handle to nifgen_ConfigureArbSequence to generate the\narbitrary sequence.\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateFreqList': {
        'documentation': {
            'description': '\nCreates a frequency list from an array of frequencies\n(**frequencyArray**) and an array of durations (**durationArray**). The\ntwo arrays should have the same number of elements, and this value must\nalso be the size of the **frequencyListLength**. The function returns a\nhandle that identifies the frequency list (the **frequencyListHandle**).\nYou can pass this handle to nifgen_ConfigureFreqList to specify what\nfrequency list you want the signal generator to produce.\n\nA frequency list consists of a list of frequencies and durations. The\nsignal generator generates each frequency for the given amount of time\nand then proceeds to the next frequency. When the end of the list is\nreached, the signal generator starts over at the beginning of the list.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the standard waveform that you want the signal generator to\nproduce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this\nvalue.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_WFM_SINE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WFM_SINE',
                            'Specifies that the signal generator produces a sinusoid waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_SQUARE',
                            'Specifies that the signal generator produces a square waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_TRIANGLE',
                            'Specifies that the signal generator produces a triangle waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_UP',
                            'Specifies that the signal generator produces a positive ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_DOWN',
                            'Specifies that the signal generator produces a negative ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_DC',
                            'Specifies that the signal generator produces a constant voltage.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_NOISE',
                            'Specifies that the signal generator produces white noise.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_USER',
                            'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.'
                        ]
                    ]
                },
                'enum': 'Waveform',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of steps in the frequency list you want to create.\nThe value must be between the minimum and maximum frequency list lengths\nthat the signal generator allows. You can obtain the minimum and maximum\nfrequency list lengths from the **minimumFrequencyListLength** and\n**maximumFrequencyListLength** parameters in the\nnifgen_QueryFreqListCapabilities function.\n\n**frequency** and **duration** must each be at least as long as this\nfrequency list length.\n\n**Default Value**: None\n'
                },
                'name': 'frequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of frequencies to form the frequency list. The array\nmust have at least as many elements as the value you specify in\n**frequencyListLength**. Each **frequencyArray** element has a\ncorresponding **durationArray** element that indicates how long that\nfrequency is repeated.\n\n**Units**: hertz\n\n**Default Value**: None\n'
                },
                'name': 'frequencyArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of durations to form the frequency list. The array\nmust have at least as many elements as the value that you specify in\n**frequencyListLength**. Each **durationArray** element has a\ncorresponding **frequencyArray** element and indicates how long in\nseconds to generate the corresponding frequency.\n\n**Units**: seconds\n\n**Default Value**: None\n'
                },
                'name': 'durationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new frequency list. You can pass\nthis handle to nifgen_ConfigureFreqList to generate the arbitrary\nsequence.\n'
                },
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.',
            'note': 'You must set NIFGEN_ATTR_OUTPUT_MODE to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ before calling this function.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'create_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.'
                },
                'name': 'waveformDataArray',
                'type': 'ViReal64',
                'type_in_documentation': 'iterable of float or int16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'create_waveform',
        'returns': 'ViStatus'
    },
    'CreateWaveformF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an onboard waveform from binary F64 (floating point double) data\nfor use in Arbitrary Waveform output mode or Arbitrary Sequence output\nmode. The **waveformHandle** returned can later be used for setting the\nactive waveform, changing the data in the waveform, building sequences\nof waveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'create_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want to create.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\nYou can obtain these values from the **maximumWaveformSize**,\n**minimumWaveformSize**, and **waveformQuantum** parameters of the\nnifgen_QueryArbWfmCapabilities function.\n\n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileF64': {
        'documentation': {
            'description': '\nThis function takes the floating point double (F64) data from the\nspecified file and creates an onboard waveform for use in Arbitrary\nWaveform or Arbitrary Sequence output mode. The **waveformHandle**\nreturned by this function can later be used for setting the active\nwaveform, changing the data in the waveform, building sequences of\nwaveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nThe F64 data must be between –1.0 and +1.0 V. Use the\nNIFGEN_ATTR_DIGITAL_GAIN attribute to generate different voltage\noutputs.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Defined Value**: "0"\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The full path and name of the file where the waveform data resides.'
                },
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte order of the data in the file.\n\n****Defined Values****\n\n| \n| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN\n',
                    'note': '\nData written by most applications in Windows (including\nLabWindows™/CVI™) is in Little Endian format. Data written to a file\nfrom LabVIEW is in Big Endian format by default on all platforms. Big\nEndian and Little Endian refer to the way data is stored in memory,\nwhich can differ on different processors.\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_LITTLE_ENDIAN',
                            'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'
                        ],
                        [
                            'NIFGEN_VAL_BIG_ENDIAN',
                            'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.'
                        ]
                    ]
                },
                'enum': 'ByteOrder',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileI16': {
        'documentation': {
            'description': '\nTakes the binary 16-bit signed integer (I16) data from the specified\nfile and creates an onboard waveform for use in Arbitrary Waveform or\nArbitrary Sequence output mode. The **waveformHandle** returned by this\nfunction can later be used for setting the active waveform, changing the\ndata in the waveform, building sequences of waveforms, or deleting the\nwaveform when it is no longer needed.\n',
            'note': '\nThe I16 data (values between –32768 and +32767) is assumed to\nrepresent –1 to +1 V. Use the NIFGEN_ATTR_DIGITAL_GAIN attribute to\ngenerate different voltage outputs.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The full path and name of the file where the waveform data resides.'
                },
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte order of the data in the file.\n\n****Defined Values****\n\n| \n| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN\n',
                    'note': '\nData written by most applications in Windows (including\nLabWindows™/CVI™) is in Little Endian format. Data written to a file\nfrom LabVIEW is in Big Endian format by default on all platforms. Big\nEndian and Little Endian refer to the way data is stored in memory,\nwhich can differ on different processors.\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_LITTLE_ENDIAN',
                            'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'
                        ],
                        [
                            'NIFGEN_VAL_BIG_ENDIAN',
                            'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.'
                        ]
                    ]
                },
                'enum': 'ByteOrder',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an onboard waveform from binary 16-bit signed integer (I16) data\nfor use in Arbitrary Waveform or Arbitrary Sequence output mode. The\n**waveformHandle** returned can later be used for setting the active\nwaveform, changing the data in the waveform, building sequences of\nwaveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'create_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want to create.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\nYou can obtain these values from the **maximumWaveformSize**,\n**minimumWaveformSize**, and **waveformQuantum** parameters of the\nnifgen_QueryArbWfmCapabilities function.\n\n| \n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify the array of data that you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in the Waveform Size parameter.\nYou must normalize the data points in the array to be between -32768 and\n+32767.\n****Default Value**:** None\n'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViInt16[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'DefineUserStandardWaveform': {
        'documentation': {
            'description': '\nDefines a user waveform for use in either Standard Function or Frequency\nList output mode.\n\nTo select the waveform, set the **waveform** parameter to\nNIFGEN_VAL_WFM_USER with either the nifgen_ConfigureStandardWaveform\nor the nifgen_CreateFreqList function.\n\nThe waveform data must be scaled between –1.0 and 1.0. Use the\n**amplitude** parameter in the niFgen_ConfigureStandardWaveform\nfunction to generate different output voltages.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_FUNC or\nNIFGEN_VAL_OUTPUT_FREQ_LIST before calling this function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to define a user standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the waveform in samples.\n**Default Value**: 16384\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteNamedWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRemoves a previously created arbitrary waveform from the signal\ngenerator memory and invalidates the waveform handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'delete_waveform',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the named waveform is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteScript': {
        'documentation': {
            'description': 'Deletes the specified script from onboard memory.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the script is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the script you want to delete. The script name\nappears in the text of the script following the script keyword.\n'
                },
                'name': 'scriptName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteWaveformDispatch': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Removes a previously created arbitrary waveform from the signal generator memory.',
            'note': 'The signal generator must not be in the Generating state when you call this function.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'delete_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from niFgen_InitializeWithChannels function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel onto which the named waveform is loaded.'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            }
        ],
        'python_name': 'delete_waveform',
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. The analog output and all\nexported signals are disabled.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to a configuration\nbuffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑FGEN returns an\nerror.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑FGEN returns an\nerror.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .nifgenconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n\nYou must provide a ViChar array to serve as a buffer for the value. You\npass the number of bytes in the buffer as the **arraySize** parameter.\nIf the current value of the attribute, including the terminating NUL\nbyte, is larger than the size you indicate in the **arraySize**\nparameter, the function copies **arraySize** – 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the array\nsize you must pass to get the entire value. For example, if the value is\n123456 and **arraySize** is 4, the function places 123 into the buffer\nand returns 7.\n\nIf you want to call this function just to get the required array size,\nyou can pass 0 for **arraySize** and VI_NULL for the **attributeValue**\nbuffer.\n\nIf you want the function to fill in the buffer regardless of the number\nof bytes in the value, pass a negative number for the **arraySize**\nparameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for the\n**attributeValue** parameter.\n\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes than you indicate in this parameter, the\nfunction copies **arraySize** – 1 bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the array size you must\npass to get the entire value. For example, if the value is 123456 and\n**arraySize** is 4, the function places 123 into the buffer and returns\n7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **attributeValue** buffer\nparameter.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be a ViChar data type and have at least as\nmany bytes as indicated in the **arraySize** parameter.\n\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes than you indicate in this parameter, the\nfunction copies **arraySize** – 1 bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the array size you must\npass to get the entire value. For example, if the value is 123456 and\n**arraySize** is 4, the function places 123 into the buffer and returns\n7.\n\nIf you specify 0 for the **arraySize** parameter, you can pass VI_NULL\nfor this parameter.\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'documentation': {
            'description': '\nReturns the channel string that is in the channel table at an index you\nspecify.\n',
            'note': '\nThis function is included for compliance with the IviFgen Class\nSpecification.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A 1-based index into the channel table.'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**description** parameter.\n\nIf the error description, including the terminating NULL byte, contains\nmore bytes than you indicate in this parameter, the function copies\nBufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the\nend of the buffer, and returns the buffer size you must pass to get the\nentire value. For example, if the value is "123456" and the Buffer Size\nis 4, the function places "123" into the buffer and returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the channel string that is in the channel table at the index you\nspecify. Do not modify the contents of the channel string.\n'
                },
                'name': 'channelString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with an IVI session or with the\ncurrent execution thread. If you specify a valid IVI session for the\n**vi** parameter, this function retrieves and then clears the error\ninformation for the session. If you pass VI_NULL for the **vi**\nparameter, this function retrieves and then clears the error information\nfor the current execution thread.\n\nThe IVI Engine also maintains this error information separately for each\nthread. This feature is useful if you do not have a session handle to\npass to the niFgen_GetError or nifgen_ClearError functions. This\nsituation occurs when a call to the nifgen_init or\nnifgen_InitWithOptions function fails.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the nifgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fail.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error code for the session or execution thread.\n\nA value of VI_SUCCESS (0) indicates that no error occurred. A positive\nvalue indicates a warning. A negative value indicates an error.\n\nYou can call nifgen_error_message to get a text description of the\nvalue.\n\nIf you are not interested in this value, you can pass VI_NULL.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the **errorDescription** array.\n\nYou can determine the array size needed to store the entire error\ndescription by setting this parameter to 0. The function then ignores\nthe **errorDescription** buffer, which may be set to VI_NULL, and gives\nas its return value the required buffer size. You can then call the\nfunction a second time using the correct buffer size.\n'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error description string for the session or execution thread. If the\nerror code is nonzero, the description string can further describe the\nerror or warning condition.\n\nIf you are not interested in this value, you can pass VI_NULL.\nOtherwise, you must pass a ViChar array of a size specified with the\n**errorDescriptionBufferSize** parameter.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\nThe time returned is 24-hour (military) local time; for example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hour** parameter and 30 for the **minute** parameter.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'documentation': {
            'description': '\nReturns the temperature at the last successful external calibration. The\ntemperature is returned in degrees Celsius.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the temperature at the last successful calibration in degrees\nCelsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'documentation': {
            'description': '\nReturns the recommended interval between external calibrations in\nmonths.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the recommended interval between external calibrations in\nmonths.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHardwareState': {
        'documentation': {
            'description': '\nReturns the current hardware state of the device and, if the device is\nin the hardware error state, the current hardware error.\n',
            'note': 'Hardware states do not necessarily correspond to NI-FGEN states.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the hardware state of the signal generator.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_IDLE',
                            'The device is in the Idle state.'
                        ],
                        [
                            'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                            'The device is waiting for Start Trigger.'
                        ],
                        [
                            'NIFGEN_VAL_RUNNING',
                            'The device is in the Running state.'
                        ],
                        [
                            'NIFGEN_VAL_DONE',
                            'The generation has completed successfully.'
                        ],
                        [
                            'NIFGEN_VAL_HARDWARE_ERROR',
                            'There is a hardware error.'
                        ]
                    ]
                },
                'enum': 'HardwareState',
                'name': 'state',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this function returns 14 for the **hour** parameter and 30 for the **minute** parameter.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last successful self-calibration.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.'
                },
                'name': 'lastCalDatetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nAll values are returned as separate parameters. Each parameter is\nreturned as an integer, including the year, month, day, hour, minute,\nand second. For example, if the device is calibrated in September 2013,\nthis function returns 9 for the **month** parameter and 2013 for the\n**year** parameter.\n\nThe time returned is 24-hour (military) local time. For example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hours** parameter and 30 for the **minutes** parameter.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'get_self_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'documentation': {
            'description': '\nReturns the temperature at the last successful self-calibration. The\ntemperature is returned in degrees Celsius.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the temperature at the last successful calibration in degrees\nCelsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'documentation': {
            'description': 'Returns whether the device supports self–calibration.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitWithOptions function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the device supports self-calibration.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Self–calibration is supported.'
                        ],
                        [
                            'VI_FALSE',
                            'Self–calibration is not supported.'
                        ]
                    ]
                },
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n\n\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while generating a signal.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'python_api_converter_name': 'convert_to_bytes',
                'python_type': 'bytes',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViAddr[]',
                'type_in_documentation': 'bytes'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers, channel counts, and onboard memory\nsizes.\n',
            'note': '\nYou cannot call this function while the session is in a running state,\nsuch as while generating a signal.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niFgen_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .nifgenconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates and returns a new NI-FGEN session to the specified channel of a\nwaveform generator that is used in all subsequent NI-FGEN function\ncalls.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must ensure that the name you use matches the name in the\nIVI Configuration Store file exactly, without any variations in the case\nof the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize.\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::\\ *1*',
                            '(*1* = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            '*myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::\\ *myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::\\ *2*',
                            '(*2* = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            '*myLogicalName*',
                            '(*myLogicalName* = name)'
                        ]
                    ],
                    'table_header': [
                        'Example #',
                        'Device Type',
                        'Syntax',
                        'Variable'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel that this VI uses.\n\n**Default Value**: "0"\n'
                },
                'is_repeated_capability': False,
                'name': 'channelName',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'str, list, range, tuple'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want to reset the device during the initialization\nprocedure. VI_TRUE specifies that the device is reset and performs the\nsame function as the nifgen_Reset function.\n\n****Defined Values****\n\n**Default Value**: VI_FALSE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Reset device'
                        ],
                        [
                            'VI_FALSE',
                            'Do not reset device'
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the initial value of certain session attributes.\n\nThe syntax for **optionString** is\n\n<*attributeName*> = <*value*>\n\nwhere\n\n*attributeName* is the name of the attribute and *value* is the value to\nwhich the attribute is set\n\nTo set multiple attributes, separate them with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for these attributes. You can override the default\nvalues by assigning a value explicitly in a string that you pass for\nthis parameter.\n\nYou do not have to specify all of the attributes and may leave any of\nthem out. However, if you do not specify one of the attributes, its\ndefault value is used.\n\nIf simulation is enabled (Simulate=1), you may specify the device that\nyou want to simulate. To specify a device, enter the following syntax in\n**optionString**.\n\nDriverSetup=Model:<*driver model number*>;Channels:<*channel\nnames*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in\nbytes*>\n\n**Syntax Examples**\n\n**Attributes and **Defined Values****\n\n**Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n',
                    'table_body': [
                        [
                            'RangeCheck',
                            'NIFGEN_ATTR_RANGE_CHECK',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Cache',
                            'NIFGEN_ATTR_CACHE',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Simulate',
                            'NIFGEN_ATTR_SIMULATE',
                            'VI_TRUE, VI_FALSE'
                        ]
                    ],
                    'table_header': [
                        'Attribute Name',
                        'Attribute',
                        'Values'
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-FGEN function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateGeneration': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates signal generation. If you want to abort signal generation,\ncall the nifgen_AbortGeneration function. After the signal generation\nis aborted, you can call the niFgen_InitiateGeneration function to\ncause the signal generator to produce a signal again.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': '\nDetermines whether the current generation is complete. This function\nsets the **done** parameter to VI_TRUE if the session is in the Idle or\nCommitted states.\n',
            'note': '\nNI-FGEN only reports the **done** parameter as VI_TRUE after the\ncurrent generation is complete in Single trigger mode.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns information about the completion of waveform generation.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Generation is complete.'
                        ],
                        [
                            'VI_FALSE',
                            'Generation is not complete.'
                        ]
                    ]
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session. Before it does so,\nthis function waits until all other execution threads have released\ntheir locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the\nfollowing ways:\n\n-  Your application called the niFgen_LockSession function.\n-  A call to the NI-FGEN locked the session.\n-  A call to the IVI Engine locked the session.\n\nAfter your call to the niFgen_LockSession function returns\nsuccessfully, no other threads can access the instrument session until\nyou call the nifgen_UnlockSession function.\n\nUse the niFgen_LockSession function and the niFgen_UnlockSession\nfunction around a sequence of calls to NI-FGEN functions if you require\nthat the instrument retain its settings through the end of the sequence.\n\nYou can safely make nested calls to the niFgen_LockSession function\nwithin the same thread. To completely unlock the session, you must\nbalance each call to the niFgen_LockSession function with a call to the\nniFgen_UnlockSession function. If, however, you use the\n**callerHasLock** parameter in all calls to the niFgen_LockSession\nfunction and the niFgen_UnlockSession function within a function, the\nIVI Engine locks the session only once within the function regardless of\nthe number of calls you make to the niFgen_LockSession function. This\nconfiguration allows you to call the niFgen_UnlockSession function just\nonce at the end of the function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nKeeps track of whether you obtained a lock and therefore need to unlock\nthe session. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to the\nniFgen_LockSession function or the nifgen_UnlockSession function in\nthe same function.\n\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nThis parameter is an input/output parameter. The niFgen_LockSession\nfunction and the niFgen_UnlockSession function each inspect the current\nvalue and take the following actions:\n\n-  If the value is VI_TRUE, the niFgen_LockSession function does not\n   lock the session again. If the value is VI_FALSE, the\n   niFgen_LockSession function obtains the lock and sets the value of\n   the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niFgen_UnlockSession function does\n   not attempt to unlock the session. If the value is VI_TRUE, the\n   niFgen_UnlockSession function releases the lock and sets the value\n   of the parameter to VI_FALSE.\n\nThus, you can call the niFgen_UnlockSession function at the end of your\nfunction without worrying about whether you actually have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\n\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\nif (flags & BIT_1)\n{\n\nviCheckErr( niFgen_LockSession(vi, &haveLock;));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\n\n viCheckErr( niFgen_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi));\nviCheckErr( niFgen_LockSession(vi, &haveLock;);\n\n}\nif (flags & BIT_3)\n\n viCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n| \n\n/\\*\nAt this point, you cannot really be sure that\nyou have the lock. Fortunately, the haveLock\nvariable takes care of that for you.\n\\*/\nniFgen_UnlockSession(vi, &haveLock;);\nreturn error;\n\n| }\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'QueryArbSeqCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating arbitrary sequences (the NIFGEN_ATTR_MAX_NUM_SEQUENCES,\nNIFGEN_ATTR_MIN_SEQUENCE_LENGTH,\nNIFGEN_ATTR_MAX_SEQUENCE_LENGTH, and NIFGEN_ATTR_MAX_LOOP_COUNT\nattributes).\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveform sequences that the\nsignal generator allows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_SEQUENCES attribute.\n'
                },
                'name': 'maximumNumberOfSequences',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of arbitrary waveforms the signal generator\nallows in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_SEQUENCE_LENGTH attribute.\n'
                },
                'name': 'minimumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveforms the signal generator\nallows in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_SEQUENCE_LENGTH attribute.\n'
                },
                'name': 'maximumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of times the signal generator can repeat an\narbitrary waveform in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_LOOP_COUNT attribute.\n'
                },
                'name': 'maximumLoopCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbWfmCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating arbitrary waveforms. These attributes are the maximum number of\nwaveforms, waveform quantum, minimum waveform size, and maximum waveform\nsize.\n',
            'note': '\nIf you do not want to obtain the waveform quantum, pass a value of\nVI_NULL for this parameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveforms that the signal\ngenerator allows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_WAVEFORMS attribute.\n'
                },
                'name': 'maximumNumberOfWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe size (number of points) of each waveform must be a multiple of a\nconstant quantum value. This parameter obtains the quantum value that\nthe signal generator uses. NI-FGEN returns this value from the\nNIFGEN_ATTR_WAVEFORM_QUANTUM attribute.\n\nFor example, when this attribute returns a value of 8, all waveform\nsizes must be a multiple of 8.\n'
                },
                'name': 'waveformQuantum',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of points that the signal generator allows in\na waveform. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_WAVEFORM_SIZE attribute.\n'
                },
                'name': 'minimumWaveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of points that the signal generator allows in\na waveform. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_WAVEFORM_SIZE attribute.\n'
                },
                'name': 'maximumWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryFreqListCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating frequency lists. These attributes are\nNIFGEN_ATTR_MAX_NUM_FREQ_LISTS,\nNIFGEN_ATTR_MIN_FREQ_LIST_LENGTH,\nNIFGEN_ATTR_MAX_FREQ_LIST_LENGTH,\nNIFGEN_ATTR_MIN_FREQ_LIST_DURATION,\nNIFGEN_ATTR_MAX_FREQ_LIST_DURATION, and\nNIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of frequency lists that the signal generator\nallows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_FREQ_LISTS attribute.\n'
                },
                'name': 'maximumNumberOfFreqLists',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of steps that the signal generator allows in\na frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_FREQ_LIST_LENGTH attribute.\n'
                },
                'name': 'minimumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of steps that the signal generator allows in\na frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_FREQ_LIST_LENGTH attribute.\n'
                },
                'name': 'maximumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum duration that the signal generator allows in a step\nof a frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_FREQ_LIST_DURATION attribute.\n'
                },
                'name': 'minimumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum duration that the signal generator allows in a step\nof a frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_FREQ_LIST_DURATION attribute.\n'
                },
                'name': 'maximumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the quantum of which all durations must be a multiple in a\nfrequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM attribute.\n'
                },
                'name': 'frequencyListDurationQuantum',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'documentation': {
            'description': '\nReads the current onboard temperature of the device. The temperature is\nreturned in degrees Celsius.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current temperature read from onboard temperature sensors,\nin degrees Celsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nPerforms a hard reset on the device. Generation is stopped, all routes\nare released, external bidirectional terminals are tristated, FPGAs are\nreset, hardware is configured to its default state, and all session\nattributes are reset to their default states.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the instrument and reapplies initial user–specified settings from\nthe logical name that was used to initialize the session. If the session\nwas created without a logical name, this function is equivalent to the\nnifgen_reset function.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'documentation': {
            'description': '\nPerforms a full internal self-calibration on the device. If the\ncalibration is successful, new calibration data and constants are stored\nin the onboard EEPROM.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the nifgen_InitWithOptions functions and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'documentation': {
            'description': '\nSends a command to trigger the signal generator. This VI can act as an\noverride for an external edge trigger.\n',
            'note': '\nThis VI does not override external digital edge triggers of the\nNI 5401/5411/5431.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'send_software_edge_trigger'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Trigger specifies the type of software trigger to send',
                    'table_body': [
                        [
                            'NIFGEN_VAL_START_TRIGGER'
                        ],
                        [
                            'NIFGEN_VAL_SCRIPT_TRIGGER'
                        ]
                    ],
                    'table_header': [
                        'Defined Values'
                    ]
                },
                'enum': 'Trigger',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Trigger ID specifies the Script Trigger to use for triggering.'
                },
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt32 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'grpc_enum': 'NiFgenInt32AttributeValues',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViReal64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'grpc_enum': 'NiFgenReal64AttributeValues',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'grpc_mapped_enum': 'NiFgenStringAttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetNamedWaveformNextWritePosition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the position in the waveform to which data is written at the next\nwrite. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the **waveformHandle** parameter. Subsequent\nwrites to that waveform begin where the last write left off, unless this\nfunction is called again. The **waveformHandle** passed in must have\nbeen created with a call to one of the following functions:\n\n-  nifgen_AllocateWaveform\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'set_next_write_position',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from the **relativeTo** parameter at which to start\nloading the data into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetNextWritePositionDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nSets the position in the waveform at which the next waveform data is\nwritten. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the waveformHandle parameter. Subsequent writes to\nthat waveform begin where the last write left off, unless this function\nis called again. The waveformHandle passed in must have been created by\na call to the nifgen_AllocateWaveform function or one of the following\nniFgen_CreateWaveformF64 function.\n'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'set_next_write_position'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the niFgen_InitializeWithChannels function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel on which to the waveform data should be loaded.'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'grpc_enum': None,
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from **relativeTo** at which to start loading the\ndata into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'set_next_write_position',
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformNextWritePosition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the position in the waveform at which the next waveform data is\nwritten. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the waveformHandle parameter. Subsequent writes to\nthat waveform begin where the last write left off, unless this function\nis called again. The waveformHandle passed in must have been created by\na call to the nifgen_AllocateWaveform function or one of the following\nniFgen CreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'set_next_write_position',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which to the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from **relativeTo** at which to start loading the\ndata into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an instrument session using the\nnifgen_LockSession function.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nKeeps track of whether you obtain a lock and therefore need to unlock\nthe session.\n\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nPass the address of a local ViBoolean variable. In the declaration of\nthe local variable, initialize it to VI_FALSE. Pass the address of the\nsame local variable to any other calls you make to the\nniFgen_LockSession function or the niFgen_UnlockSession function in\nthe same function.\n\nThe parameter is an input/output parameter. The niFgen_LockSession\nfunction and the niFgen_UnlockSession function each inspect the current\nvalue and take the following actions:\n\n-  If the value is VI_TRUE, the niFgen_LockSession function does not\n   lock the session again. If the value is VI_FALSE, the\n   niFgen_LockSession function obtains the lock and sets the value of\n   the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niFgen_UnlockSession function does\n   not attempt to unlock the session. If the value is VI_TRUE, the\n   niFgen_UnlockSession function releases the lock and sets the value\n   of the parameter to VI_FALSE.\n\nThus, you can, call the niFgen_UnlockSession function at the end of\nyour function without worrying about whether you actually have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\n\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\nif (flags & BIT_1)\n{\n\nviCheckErr(niFgen_LockSession(vi, &haveLock;));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\n\nviCheckErr( niFgen_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi));\nviCheckErr( niFgen_LockSession(vi, &haveLock;);\n\n}\nif (flags & BIT_3)\n\n viCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n| \n\n/\\*\nAt this point, you cannot really be sure that\nyou have the lock. Fortunately, the haveLock\nvariable takes care of that for you.\n\\*/\nniFgen_UnlockSession(vi, &haveLock;);\nreturn error;\n\n}\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitUntilDone': {
        'documentation': {
            'description': '\nWaits until the device is done generating or until the maximum time has\nexpired.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the timeout value in milliseconds.'
                },
                'name': 'maxTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteBinary16Waveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites binary data to the waveform in onboard memory. The waveform\nhandle passed must have been created by a call to the\nnifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.\n\nBy default, the subsequent call to the niFgen_WriteBinary16Waveform\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetWaveformNextWritePosition function. If streaming is enabled,\nyou can write more data than the allocated waveform size in onboard\nmemory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which to the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**. The binary data\nis left-justified.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites floating-point data to the waveform in onboard memory. The\nwaveform handle passed in must have been created by a call to the\nnifgen_AllocateWaveform function or to one of the following niFgen\nCreate Waveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n\nBy default, the subsequent call to the niFgen_WriteNamedWaveformF64\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites binary data to the named waveform in onboard memory.\n\nBy default, the subsequent call to the niFgen_WriteNamedWaveformI16\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteScript': {
        'documentation': {
            'description': '\nWrites a string containing one or more scripts that govern the\ngeneration of waveforms.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which the script is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nContains the text of the script you want to use for your generation\noperation. Refer to `scripting\nInstructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__\nfor more information about writing scripts.\n"
                },
                'name': 'script',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites floating-point data to the waveform in onboard memory. The\nwaveform handle passed in must have been created by a call to the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n\nBy default, the subsequent call to the niFgen_WriteWaveform function\ncontinues writing data from the position of the last sample written. You\ncan set the write position and offset by calling the\nnifgen_SetWaveformNextWritePosition function. If streaming is enabled,\nyou can write more data than the allocated waveform size in onboard\nmemory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'library_interpreter_filename': 'numpy_write_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Writes data to the waveform in onboard memory.\n\nBy default, subsequent calls to this function\ncontinue writing data from the position of the last sample written. You\ncan set the write position and offset by calling the nifgen_SetNamedWaveformNextWritePosition\nnifgen_SetWaveformNextWritePosition function.'
        },
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'write_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.'
                },
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'write_waveform',
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the following operations:\n\n-  Closes the instrument I/O session.\n-  Destroys the NI-FGEN session and all of its attributes.\n-  Deallocates any memory resources NI-FGEN uses.\n\nNot all signal routes established by calling the nifgen_ExportSignal\nand nifgen_RouteSignalOut functions are released when the NI-FGEN\nsession is closed. The following table shows what happens to a signal\nroute on your device when you call the niFgen_close function.\n',
            'note': '\nAfter calling niFgen_close, you cannot use NI-FGEN again until you\ncall the nifgen_init or nifgen_InitWithOptions functions.\n',
            'table_body': [
                [
                    'Front Panel',
                    'Remain connected',
                    'Remain connected'
                ],
                [
                    'RTSI/PXI Backplane',
                    'Remain connected',
                    'Disconnected'
                ]
            ],
            'table_header': [
                'Routes To',
                'NI 5401/5411/5431',
                'Other Devices'
            ]
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nConverts a status code returned by an NI-FGEN function into a\nuser-readable string.\n'
        },
        'grpc_name': 'ErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the niFgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fails.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-FGEN functions.\n\n**Default Value**: 0 (VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error message string read from the instrument error message\nqueue.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nRuns the instrument self-test routine and returns the test result(s).\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'note': '\nWhen used on some signal generators, the device is reset after the\nniFgen_self_test function runs. If you use the niFgen_self_test\nfunction, your device may not be in its previously configured state\nafter the function runs.\n',
            'table_body': [
                [
                    '0',
                    'Passed self-test'
                ],
                [
                    '1',
                    'Self-test failed'
                ]
            ],
            'table_header': [
                'Self-Test Code',
                'Description'
            ]
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels functions and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the instrument to a known state. This function aborts the\ngeneration, clears all routes, and resets session attributes to the\ndefault values. This function does not, however, commit the session\nproperties or configure the device hardware to its default state.\n',
            'note': '\nFor the NI 5401/5404/5411/5431, this function exhibits the same\nbehavior as the nifgen_ResetDevice function.\n'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Runs the instrument self-test routine and returns the test result(s).',
            'note': '\nWhen used on some signal generators, the device is reset after the\nniFgen_self_test function runs. If you use the niFgen_self_test\nfunction, your device may not be in its previously configured state\nafter the function runs.\n'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the value returned from the instrument self-test. A value of 0\nindicates success.\n',
                    'table_body': [
                        [
                            '0',
                            'Passed self-test'
                        ],
                        [
                            '1',
                            'Self-test failed'
                        ]
                    ],
                    'table_header': [
                        'Self-Test Code',
                        'Description'
                    ]
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test response string from the instrument.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/nifgen/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/metadata/nifgen.proto sha256=c6e1dd9acbb95b82c922ed2fc12d7d72f51b1945ecf681427c2be5281a76ed2e bytes=72399 -->
## FILE: src/nifgen/metadata/nifgen.proto

- repository: `ni/nimi-python`
- source_path: `src/nifgen/metadata/nifgen.proto`
- sha256: `c6e1dd9acbb95b82c922ed2fc12d7d72f51b1945ecf681427c2be5281a76ed2e`
- bytes: 72399

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-FGEN API metadata version 25.0.0f114
//---------------------------------------------------------------------
// Proto file for the NI-FGEN Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.fgen";
option java_outer_classname = "NiFgen";
option csharp_namespace = "NationalInstruments.Grpc.Fgen";

package nifgen_grpc;

import "nidevice.proto";
import "session.proto";

service NiFgen {
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitializeWithChannels(InitializeWithChannelsRequest) returns (InitializeWithChannelsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ErrorHandler(ErrorHandlerRequest) returns (ErrorHandlerResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc GetHardwareState(GetHardwareStateRequest) returns (GetHardwareStateResponse);
  rpc WaitUntilDone(WaitUntilDoneRequest) returns (WaitUntilDoneResponse);
  rpc IsDone(IsDoneRequest) returns (IsDoneResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc ConfigureOperationMode(ConfigureOperationModeRequest) returns (ConfigureOperationModeResponse);
  rpc ConfigureOutputMode(ConfigureOutputModeRequest) returns (ConfigureOutputModeResponse);
  rpc ConfigureReferenceClock(ConfigureReferenceClockRequest) returns (ConfigureReferenceClockResponse);
  rpc ConfigureOutputImpedance(ConfigureOutputImpedanceRequest) returns (ConfigureOutputImpedanceResponse);
  rpc ConfigureOutputEnabled(ConfigureOutputEnabledRequest) returns (ConfigureOutputEnabledResponse);
  rpc ConfigureChannels(ConfigureChannelsRequest) returns (ConfigureChannelsResponse);
  rpc InitiateGeneration(InitiateGenerationRequest) returns (InitiateGenerationResponse);
  rpc AbortGeneration(AbortGenerationRequest) returns (AbortGenerationResponse);
  rpc ConfigureStandardWaveform(ConfigureStandardWaveformRequest) returns (ConfigureStandardWaveformResponse);
  rpc DefineUserStandardWaveform(DefineUserStandardWaveformRequest) returns (DefineUserStandardWaveformResponse);
  rpc ClearUserStandardWaveform(ClearUserStandardWaveformRequest) returns (ClearUserStandardWaveformResponse);
  rpc ConfigureFrequency(ConfigureFrequencyRequest) returns (ConfigureFrequencyResponse);
  rpc ConfigureAmplitude(ConfigureAmplitudeRequest) returns (ConfigureAmplitudeResponse);
  rpc QueryArbWfmCapabilities(QueryArbWfmCapabilitiesRequest) returns (QueryArbWfmCapabilitiesResponse);
  rpc CreateWaveformF64(CreateWaveformF64Request) returns (CreateWaveformF64Response);
  rpc CreateWaveformI16(CreateWaveformI16Request) returns (CreateWaveformI16Response);
  rpc CreateWaveformComplexF64(CreateWaveformComplexF64Request) returns (CreateWaveformComplexF64Response);
  rpc CreateWaveformFromFileI16(CreateWaveformFromFileI16Request) returns (CreateWaveformFromFileI16Response);
  rpc CreateWaveformFromFileF64(CreateWaveformFromFileF64Request) returns (CreateWaveformFromFileF64Response);
  rpc ConfigureSampleRate(ConfigureSampleRateRequest) returns (ConfigureSampleRateResponse);
  rpc ConfigureArbWaveform(ConfigureArbWaveformRequest) returns (ConfigureArbWaveformResponse);
  rpc ClearArbWaveform(ClearArbWaveformRequest) returns (ClearArbWaveformResponse);
  rpc AllocateNamedWaveform(AllocateNamedWaveformRequest) returns (AllocateNamedWaveformResponse);
  rpc SetNamedWaveformNextWritePosition(SetNamedWaveformNextWritePositionRequest) returns (SetNamedWaveformNextWritePositionResponse);
  rpc WriteNamedWaveformF64(WriteNamedWaveformF64Request) returns (WriteNamedWaveformF64Response);
  rpc WriteNamedWaveformI16(WriteNamedWaveformI16Request) returns (WriteNamedWaveformI16Response);
  rpc WriteNamedWaveformComplexF64(WriteNamedWaveformComplexF64Request) returns (WriteNamedWaveformComplexF64Response);
  rpc WriteNamedWaveformComplexI16(WriteNamedWaveformComplexI16Request) returns (WriteNamedWaveformComplexI16Response);
  rpc DeleteNamedWaveform(DeleteNamedWaveformRequest) returns (DeleteNamedWaveformResponse);
  rpc QueryArbSeqCapabilities(QueryArbSeqCapabilitiesRequest) returns (QueryArbSeqCapabilitiesResponse);
  rpc CreateArbSequence(CreateArbSequenceRequest) returns (CreateArbSequenceResponse);
  rpc CreateAdvancedArbSequence(CreateAdvancedArbSequenceRequest) returns (CreateAdvancedArbSequenceResponse);
  rpc ConfigureArbSequence(ConfigureArbSequenceRequest) returns (ConfigureArbSequenceResponse);
  rpc ClearArbSequence(ClearArbSequenceRequest) returns (ClearArbSequenceResponse);
  rpc ClearArbMemory(ClearArbMemoryRequest) returns (ClearArbMemoryResponse);
  rpc QueryFreqListCapabilities(QueryFreqListCapabilitiesRequest) returns (QueryFreqListCapabilitiesResponse);
  rpc CreateFreqList(CreateFreqListRequest) returns (CreateFreqListResponse);
  rpc ConfigureFreqList(ConfigureFreqListRequest) returns (ConfigureFreqListResponse);
  rpc ClearFreqList(ClearFreqListRequest) returns (ClearFreqListResponse);
  rpc WriteScript(WriteScriptRequest) returns (WriteScriptResponse);
  rpc DeleteScript(DeleteScriptRequest) returns (DeleteScriptResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc RouteSignalOut(RouteSignalOutRequest) returns (RouteSignalOutResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc ConfigureP2PEndpointFullnessStartTrigger(ConfigureP2PEndpointFullnessStartTriggerRequest) returns (ConfigureP2PEndpointFullnessStartTriggerResponse);
  rpc ConfigureDigitalEdgeScriptTrigger(ConfigureDigitalEdgeScriptTriggerRequest) returns (ConfigureDigitalEdgeScriptTriggerResponse);
  rpc ConfigureDigitalLevelScriptTrigger(ConfigureDigitalLevelScriptTriggerRequest) returns (ConfigureDigitalLevelScriptTriggerResponse);
  rpc ConfigureSoftwareEdgeScriptTrigger(ConfigureSoftwareEdgeScriptTriggerRequest) returns (ConfigureSoftwareEdgeScriptTriggerResponse);
  rpc DisableScriptTrigger(DisableScriptTriggerRequest) returns (DisableScriptTriggerResponse);
  rpc ConfigureClockMode(ConfigureClockModeRequest) returns (ConfigureClockModeResponse);
  rpc AdjustSampleClockRelativeDelay(AdjustSampleClockRelativeDelayRequest) returns (AdjustSampleClockRelativeDelayResponse);
  rpc AllocateWaveform(AllocateWaveformRequest) returns (AllocateWaveformResponse);
  rpc SetWaveformNextWritePosition(SetWaveformNextWritePositionRequest) returns (SetWaveformNextWritePositionResponse);
  rpc WriteWaveform(WriteWaveformRequest) returns (WriteWaveformResponse);
  rpc WriteBinary16Waveform(WriteBinary16WaveformRequest) returns (WriteBinary16WaveformResponse);
  rpc WriteWaveformComplexF64(WriteWaveformComplexF64Request) returns (WriteWaveformComplexF64Response);
  rpc WriteComplexBinary16Waveform(WriteComplexBinary16WaveformRequest) returns (WriteComplexBinary16WaveformResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc GetSelfCalSupported(GetSelfCalSupportedRequest) returns (GetSelfCalSupportedResponse);
  rpc GetSelfCalLastDateAndTime(GetSelfCalLastDateAndTimeRequest) returns (GetSelfCalLastDateAndTimeResponse);
  rpc GetExtCalLastDateAndTime(GetExtCalLastDateAndTimeRequest) returns (GetExtCalLastDateAndTimeResponse);
  rpc GetSelfCalLastTemp(GetSelfCalLastTempRequest) returns (GetSelfCalLastTempResponse);
  rpc GetExtCalLastTemp(GetExtCalLastTempRequest) returns (GetExtCalLastTempResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc ReadCurrentTemperature(ReadCurrentTemperatureRequest) returns (ReadCurrentTemperatureResponse);
  rpc ConfigureCustomFIRFilterCoefficients(ConfigureCustomFIRFilterCoefficientsRequest) returns (ConfigureCustomFIRFilterCoefficientsResponse);
  rpc GetFIRFilterCoefficients(GetFIRFilterCoefficientsRequest) returns (GetFIRFilterCoefficientsResponse);
  rpc GetStreamEndpointHandle(GetStreamEndpointHandleRequest) returns (GetStreamEndpointHandleResponse);
  rpc WriteP2PEndpointI16(WriteP2PEndpointI16Request) returns (WriteP2PEndpointI16Response);
  rpc ConfigureSynchronization(ConfigureSynchronizationRequest) returns (ConfigureSynchronizationResponse);
  rpc EnableDigitalPatterning(EnableDigitalPatterningRequest) returns (EnableDigitalPatterningResponse);
  rpc DisableDigitalPatterning(DisableDigitalPatterningRequest) returns (DisableDigitalPatterningResponse);
  rpc EnableDigitalFilter(EnableDigitalFilterRequest) returns (EnableDigitalFilterResponse);
  rpc DisableDigitalFilter(DisableDigitalFilterRequest) returns (DisableDigitalFilterResponse);
  rpc EnableAnalogFilter(EnableAnalogFilterRequest) returns (EnableAnalogFilterResponse);
  rpc DisableAnalogFilter(DisableAnalogFilterRequest) returns (DisableAnalogFilterResponse);
  rpc ConfigureSampleClockSource(ConfigureSampleClockSourceRequest) returns (ConfigureSampleClockSourceResponse);
  rpc ConfigureTriggerMode(ConfigureTriggerModeRequest) returns (ConfigureTriggerModeResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc CheckAttributeViInt64(CheckAttributeViInt64Request) returns (CheckAttributeViInt64Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ManualEnableP2PStream(ManualEnableP2PStreamRequest) returns (ManualEnableP2PStreamResponse);
  rpc CreateWaveformFromFileHWS(CreateWaveformFromFileHWSRequest) returns (CreateWaveformFromFileHWSResponse);
}

enum NiFgenAttribute {
  NIFGEN_ATTRIBUTE_UNSPECIFIED = 0;
  NIFGEN_ATTRIBUTE_OUTPUT_MODE = 1250001;
  NIFGEN_ATTRIBUTE_OUTPUT_ENABLED = 1250003;
  NIFGEN_ATTRIBUTE_DIGITAL_GAIN = 1150254;
  NIFGEN_ATTRIBUTE_ANALOG_PATH = 1150222;
  NIFGEN_ATTRIBUTE_LOAD_IMPEDANCE = 1150220;
  NIFGEN_ATTRIBUTE_OUTPUT_IMPEDANCE = 1250004;
  NIFGEN_ATTRIBUTE_TERMINAL_CONFIGURATION = 1150365;
  NIFGEN_ATTRIBUTE_COMMON_MODE_OFFSET = 1150366;
  NIFGEN_ATTRIBUTE_CHANNEL_DELAY = 1150369;
  NIFGEN_ATTRIBUTE_ABSOLUTE_DELAY = 1150413;
  NIFGEN_ATTRIBUTE_ANALOG_FILTER_ENABLED = 1150103;
  NIFGEN_ATTRIBUTE_DIGITAL_FILTER_ENABLED = 1150102;
  NIFGEN_ATTRIBUTE_DIGITAL_FILTER_INTERPOLATION_FACTOR = 1150218;
  NIFGEN_ATTRIBUTE_FLATNESS_CORRECTION_ENABLED = 1150323;
  NIFGEN_ATTRIBUTE_ANALOG_DATA_MASK = 1150234;
  NIFGEN_ATTRIBUTE_ANALOG_STATIC_VALUE = 1150235;
  NIFGEN_ATTRIBUTE_DIGITAL_DATA_MASK = 1150236;
  NIFGEN_ATTRIBUTE_DIGITAL_STATIC_VALUE = 1150237;
  NIFGEN_ATTRIBUTE_DIGITAL_PATTERN_ENABLED = 1150101;
  NIFGEN_ATTRIBUTE_AUX_POWER_ENABLED = 1150411;
  NIFGEN_ATTRIBUTE_IDLE_BEHAVIOR = 1150377;
  NIFGEN_ATTRIBUTE_IDLE_VALUE = 1150378;
  NIFGEN_ATTRIBUTE_WAIT_BEHAVIOR = 1150379;
  NIFGEN_ATTRIBUTE_WAIT_VALUE = 1150380;
  NIFGEN_ATTRIBUTE_ARB_GAIN = 1250202;
  NIFGEN_ATTRIBUTE_ARB_OFFSET = 1250203;
  NIFGEN_ATTRIBUTE_WAVEFORM_QUANTUM = 1250206;
  NIFGEN_ATTRIBUTE_MAX_NUM_WAVEFORMS = 1250205;
  NIFGEN_ATTRIBUTE_MIN_WAVEFORM_SIZE = 1250207;
  NIFGEN_ATTRIBUTE_MAX_WAVEFORM_SIZE = 1250208;
  NIFGEN_ATTRIBUTE_ARB_WAVEFORM_HANDLE = 1250201;
  NIFGEN_ATTRIBUTE_ARB_MARKER_POSITION = 1150327;
  NIFGEN_ATTRIBUTE_ARB_REPEAT_COUNT = 1150328;
  NIFGEN_ATTRIBUTE_ARB_SEQUENCE_HANDLE = 1250211;
  NIFGEN_ATTRIBUTE_MAX_NUM_SEQUENCES = 1250212;
  NIFGEN_ATTRIBUTE_MIN_SEQUENCE_LENGTH = 1250213;
  NIFGEN_ATTRIBUTE_MAX_SEQUENCE_LENGTH = 1250214;
  NIFGEN_ATTRIBUTE_MAX_LOOP_COUNT = 1250215;
  NIFGEN_ATTRIBUTE_SCRIPT_TO_GENERATE = 1150270;
  NIFGEN_ATTRIBUTE_FILE_TRANSFER_BLOCK_SIZE = 1150240;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE = 1150241;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH = 1150373;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_ENABLED = 1150244;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_SIZE = 1150245;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_ADDRESS = 1150274;
  NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_NAME = 1150326;
  NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_HANDLE = 1150324;
  NIFGEN_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM = 1150325;
  NIFGEN_ATTRIBUTE_STREAMING_WRITE_TIMEOUT = 1150409;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE = 1150374;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS = 1150375;
  NIFGEN_ATTRIBUTE_PCI_DMA_OPTIMIZATIONS_ENABLED = 1150362;
  NIFGEN_ATTRIBUTE_OSP_ENABLED = 1150246;
  NIFGEN_ATTRIBUTE_OSP_IQ_RATE = 1150248;
  NIFGEN_ATTRIBUTE_OSP_DATA_PROCESSING_MODE = 1150247;
  NIFGEN_ATTRIBUTE_OSP_MODE = 1150370;
  NIFGEN_ATTRIBUTE_OSP_FREQUENCY_SHIFT = 1150371;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_ENABLED = 1150249;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_FREQUENCY = 1150250;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_I = 1150251;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_Q = 1150252;
  NIFGEN_ATTRIBUTE_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY = 1150389;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_TYPE = 1150253;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ENABLED = 1150255;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_INTERPOLATION = 1150256;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_ENABLED = 1150257;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_INTERPOLATION = 1150258;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA = 1150259;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_RAISED_COSINE_ALPHA = 1150260;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_FLAT_PASSBAND = 1150261;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_GAUSSIAN_BT = 1150262;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_GAIN = 1150263;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_I = 1150264;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_Q = 1150265;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_I = 1150266;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_Q = 1150267;
  NIFGEN_ATTRIBUTE_OSP_OVERFLOW_ERROR_REPORTING = 1150268;
  NIFGEN_ATTRIBUTE_OSP_OVERFLOW_STATUS = 1150269;
  NIFGEN_ATTRIBUTE_P2P_ENABLED = 1150391;
  NIFGEN_ATTRIBUTE_P2P_DESTINATION_CHANNELS = 1150392;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_SIZE = 1150393;
  NIFGEN_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT = 1150394;
  NIFGEN_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT = 1150395;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_COUNT = 1150396;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL = 1150400;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS = 1150408;
  NIFGEN_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED = 1150397;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS = 1150398;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE = 1150399;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS = 1150401;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE = 1150402;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_SIZE = 1150403;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL = 1150410;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS = 1150405;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS_TYPE = 1150406;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_VALUE = 1150407;
  NIFGEN_ATTRIBUTE_FUNC_WAVEFORM = 1250101;
  NIFGEN_ATTRIBUTE_FUNC_AMPLITUDE = 1250102;
  NIFGEN_ATTRIBUTE_FUNC_DC_OFFSET = 1250103;
  NIFGEN_ATTRIBUTE_FUNC_START_PHASE = 1250105;
  NIFGEN_ATTRIBUTE_FUNC_DUTY_CYCLE_HIGH = 1250106;
  NIFGEN_ATTRIBUTE_SYNC_DUTY_CYCLE_HIGH = 1150105;
  NIFGEN_ATTRIBUTE_SYNC_OUT_OUTPUT_TERMINAL = 1150330;
  NIFGEN_ATTRIBUTE_FUNC_FREQUENCY = 1250104;
  NIFGEN_ATTRIBUTE_FUNC_BUFFER_SIZE = 1150238;
  NIFGEN_ATTRIBUTE_FUNC_MAX_BUFFER_SIZE = 1150239;
  NIFGEN_ATTRIBUTE_FREQ_LIST_HANDLE = 1150208;
  NIFGEN_ATTRIBUTE_MAX_NUM_FREQ_LISTS = 1150209;
  NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_LENGTH = 1150210;
  NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_LENGTH = 1150211;
  NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_DURATION = 1150212;
  NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_DURATION = 1150213;
  NIFGEN_ATTRIBUTE_FREQ_LIST_DURATION_QUANTUM = 1150214;
  NIFGEN_ATTRIBUTE_REFERENCE_CLOCK_SOURCE = 1150113;
  NIFGEN_ATTRIBUTE_REF_CLOCK_FREQUENCY = 1150107;
  NIFGEN_ATTRIBUTE_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL = 1150321;
  NIFGEN_ATTRIBUTE_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL = 1150322;
  NIFGEN_ATTRIBUTE_ARB_SAMPLE_RATE = 1250204;
  NIFGEN_ATTRIBUTE_CLOCK_MODE = 1150110;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_SOURCE = 1150112;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL = 1150320;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_DIVISOR = 1150219;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_SOURCE = 1150367;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_RATE = 1150368;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL = 1150329;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR = 1150230;
  NIFGEN_ATTRIBUTE_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER = 1150376;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_ABSOLUTE_DELAY = 1150231;
  NIFGEN_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE = 1150232;
  NIFGEN_ATTRIBUTE_EXTERNAL_CLOCK_DELAY_BINARY_VALUE = 1150233;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_TERMINAL = 1150312;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR = 1150342;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_POLARITY = 1150313;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH = 1150340;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS = 1150341;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE = 1150343;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY = 1150354;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY_UNITS = 1150355;
  NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LIVE_STATUS = 1150344;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_LIVE_STATUS = 1150345;
  NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LATCHED_STATUS = 1150349;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_LATCHED_STATUS = 1150350;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_DATA_BIT_NUMBER = 1150337;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_LEVEL_POLARITY = 1150338;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_OUTPUT_TERMINAL = 1150339;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL = 1150310;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL = 1150311;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LIVE_STATUS = 1150348;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_TERMINAL = 1150314;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_BEHAVIOR = 1150331;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_LEVEL_ACTIVE_LEVEL = 1150316;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_POLARITY = 1150318;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH_UNITS = 1150333;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH = 1150335;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY = 1150356;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY_UNITS = 1150357;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_LATCHED_STATUS = 1150352;
  NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_TERMINAL = 1150315;
  NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_BEHAVIOR = 1150332;
  NIFGEN_ATTRIBUTE_DONE_EVENT_LEVEL_ACTIVE_LEVEL = 1150317;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_POLARITY = 1150319;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH_UNITS = 1150334;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH = 1150336;
  NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY = 1150358;
  NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY_UNITS = 1150359;
  NIFGEN_ATTRIBUTE_DONE_EVENT_LATCHED_STATUS = 1150351;
  NIFGEN_ATTRIBUTE_TRIGGER_MODE = 1150108;
  NIFGEN_ATTRIBUTE_BURST_COUNT = 1250350;
  NIFGEN_ATTRIBUTE_START_TRIGGER_TYPE = 1150280;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE = 1150281;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1150282;
  NIFGEN_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150283;
  NIFGEN_ATTRIBUTE_SCRIPT_TRIGGER_TYPE = 1150290;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE = 1150291;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE = 1150292;
  NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE = 1150293;
  NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL = 1150294;
  NIFGEN_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL = 1150295;
  NIFGEN_ATTRIBUTE_BUS_TYPE = 1150215;
  NIFGEN_ATTRIBUTE_MEMORY_SIZE = 1150242;
  NIFGEN_ATTRIBUTE_SERIAL_NUMBER = 1150243;
  NIFGEN_ATTRIBUTE_MARKER_EVENTS_COUNT = 1150271;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENTS_COUNT = 1150273;
  NIFGEN_ATTRIBUTE_SCRIPT_TRIGGERS_COUNT = 1150272;
  NIFGEN_ATTRIBUTE_VIDEO_WAVEFORM_TYPE = 1150216;
  NIFGEN_ATTRIBUTE_FPGA_BITFILE_PATH = 1150412;
  NIFGEN_ATTRIBUTE_FILTER_CORRECTION_FREQUENCY = 1150104;
  NIFGEN_ATTRIBUTE_TRIGGER_SOURCE = 1250302;
  NIFGEN_ATTRIBUTE_SYNCHRONIZATION = 1150111;
  NIFGEN_ATTRIBUTE_ID_QUERY_RESPONSE = 1150001;
  NIFGEN_ATTRIBUTE_GAIN_DAC_VALUE = 1150223;
  NIFGEN_ATTRIBUTE_OFFSET_DAC_VALUE = 1150224;
  NIFGEN_ATTRIBUTE_OSCILLATOR_FREQ_DAC_VALUE = 1150225;
  NIFGEN_ATTRIBUTE_PRE_AMPLIFIER_ATTENUATION = 1150228;
  NIFGEN_ATTRIBUTE_POST_AMPLIFIER_ATTENUATION = 1150229;
  NIFGEN_ATTRIBUTE_CACHE = 1050004;
  NIFGEN_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIFGEN_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIFGEN_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIFGEN_ATTRIBUTE_SIMULATE = 1050005;
  NIFGEN_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIFGEN_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIFGEN_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIFGEN_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIFGEN_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIFGEN_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIFGEN_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIFGEN_ATTRIBUTE_MODULE_REVISION = 1150390;
  NIFGEN_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIFGEN_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIFGEN_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION = 1050503;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION = 1050504;
  NIFGEN_ATTRIBUTE_UPDATE_CLOCK_SOURCE = 1150106;
}

enum OutputMode {
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FUNC = 0;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB = 1;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SEQ = 2;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FREQ_LIST = 101;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SCRIPT = 102;
}

enum Waveform {
  WAVEFORM_UNSPECIFIED = 0;
  WAVEFORM_NIFGEN_VAL_WFM_SINE = 1;
  WAVEFORM_NIFGEN_VAL_WFM_SQUARE = 2;
  WAVEFORM_NIFGEN_VAL_WFM_TRIANGLE = 3;
  WAVEFORM_NIFGEN_VAL_WFM_RAMP_UP = 4;
  WAVEFORM_NIFGEN_VAL_WFM_RAMP_DOWN = 5;
  WAVEFORM_NIFGEN_VAL_WFM_DC = 6;
  WAVEFORM_NIFGEN_VAL_WFM_NOISE = 101;
  WAVEFORM_NIFGEN_VAL_WFM_USER = 102;
}

enum Signal {
  SIGNAL_UNSPECIFIED = 0;
  SIGNAL_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK = 1019;
  SIGNAL_NIFGEN_VAL_SYNC_OUT = 1002;
  SIGNAL_NIFGEN_VAL_START_TRIGGER = 1004;
  SIGNAL_NIFGEN_VAL_MARKER_EVENT = 1001;
  SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE = 1006;
  SIGNAL_NIFGEN_VAL_SYNCHRONIZATION = 1007;
  SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK = 101;
  SIGNAL_NIFGEN_VAL_REFERENCE_CLOCK = 102;
  SIGNAL_NIFGEN_VAL_SCRIPT_TRIGGER = 103;
  SIGNAL_NIFGEN_VAL_READY_FOR_START_EVENT = 105;
  SIGNAL_NIFGEN_VAL_STARTED_EVENT = 106;
  SIGNAL_NIFGEN_VAL_DONE_EVENT = 107;
  SIGNAL_NIFGEN_VAL_DATA_MARKER_EVENT = 108;
}

enum TriggerMode {
  TRIGGER_MODE_UNSPECIFIED = 0;
  TRIGGER_MODE_NIFGEN_VAL_SINGLE = 1;
  TRIGGER_MODE_NIFGEN_VAL_CONTINUOUS = 2;
  TRIGGER_MODE_NIFGEN_VAL_STEPPED = 3;
  TRIGGER_MODE_NIFGEN_VAL_BURST = 4;
}

enum ClockMode {
  CLOCK_MODE_NIFGEN_VAL_HIGH_RESOLUTION = 0;
  CLOCK_MODE_NIFGEN_VAL_DIVIDE_DOWN = 1;
  CLOCK_MODE_NIFGEN_VAL_AUTOMATIC = 2;
}

enum RelativeTo {
  RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_START = 0;
  RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_CURRENT = 1;
}

enum HardwareState {
  HARDWARE_STATE_NIFGEN_VAL_IDLE = 0;
  HARDWARE_STATE_NIFGEN_VAL_WAITING_FOR_START_TRIGGER = 100;
  HARDWARE_STATE_NIFGEN_VAL_RUNNING = 200;
  HARDWARE_STATE_NIFGEN_VAL_DONE = 600;
  HARDWARE_STATE_NIFGEN_VAL_HARDWARE_ERROR = 1000;
}

enum ByteOrder {
  BYTE_ORDER_NIFGEN_VAL_LITTLE_ENDIAN = 0;
  BYTE_ORDER_NIFGEN_VAL_BIG_ENDIAN = 1;
}

enum TriggerWhen {
  TRIGGER_WHEN_UNSPECIFIED = 0;
  TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_HIGH = 101;
  TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_LOW = 102;
}

enum Trigger {
  TRIGGER_UNSPECIFIED = 0;
  TRIGGER_NIFGEN_VAL_START_TRIGGER = 1004;
  TRIGGER_NIFGEN_VAL_SCRIPT_TRIGGER = 103;
}

enum FrequencyListOptions {
  FREQUENCY_LIST_OPTIONS_UNSPECIFIED = 0;
  FREQUENCY_LIST_OPTIONS_NIFGEN_VAL_ALL_FLISTS = -1;
}

enum RouteSignalFrom {
  ROUTE_SIGNAL_FROM_UNSPECIFIED = 0;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_MARKER = 1001;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNC_OUT = 1002;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_OUT_START_TRIGGER = 1004;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_BOARD_CLOCK = 1006;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNCHRONIZATION = 1007;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SOFTWARE_TRIG = 2;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_REF_OUT = 1008;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_CLOCK_OUT = 1009;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_PXI_STAR = 131;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_PFI_0 = 1011;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_0 = 141;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_1 = 142;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_2 = 143;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_3 = 144;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_4 = 145;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_5 = 146;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_6 = 147;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_7 = 1010;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK = 1019;
}

enum RouteSignalTo {
  ROUTE_SIGNAL_TO_UNSPECIFIED = 0;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_0 = 141;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_1 = 142;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_2 = 143;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_3 = 144;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_4 = 145;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_5 = 146;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_6 = 147;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_7 = 1010;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_REF_OUT = 1008;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_0 = 1011;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_1 = 1012;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PXI_STAR = 131;
}

enum SequenceHandle {
  SEQUENCE_HANDLE_UNSPECIFIED = 0;
  SEQUENCE_HANDLE_NIFGEN_VAL_ALL_SEQUENCES = -1;
}

enum WaveformHandle {
  WAVEFORM_HANDLE_UNSPECIFIED = 0;
  WAVEFORM_HANDLE_NIFGEN_VAL_ALL_WAVEFORMS = -1;
}

enum NiFgenInt32AttributeValues {
  option allow_alias = true;
  NIFGEN_INT32_UNSPECIFIED = 0;
  NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL = 0;
  NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL = 1;
  NIFGEN_INT32_ANALOG_PATH_VAL_MAIN_ANALOG_PATH = 0;
  NIFGEN_INT32_ANALOG_PATH_VAL_DIRECT_ANALOG_PATH = 1;
  NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_LOW_GAIN_ANALOG_PATH = 2;
  NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_HIGH_GAIN_ANALOG_PATH = 3;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_FIRST_SEQUENCE_HANDLE = 100000;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_LAST_SEQUENCE_HANDLE = 109999;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_NO_SEQUENCE = -1;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_FIRST_WAVEFORM_HANDLE = 10000;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_LAST_WAVEFORM_HANDLE = 10999;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_NO_WAVEFORM = -1;
  NIFGEN_INT32_BURST_COUNT_VAL_GENERATE_CONTINUOUS = -1;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_INVALID = 0;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_AT = 1;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCI = 2;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXI = 3;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_VXI = 4;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCMCIA = 5;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXIE = 6;
  NIFGEN_INT32_CLOCK_MODE_VAL_HIGH_RESOLUTION = 0;
  NIFGEN_INT32_CLOCK_MODE_VAL_DIVIDE_DOWN = 1;
  NIFGEN_INT32_CLOCK_MODE_VAL_AUTOMATIC = 2;
  NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_REAL = 0;
  NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_COMPLEX = 1;
  NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_FLAT = 0;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_RAISED_COSINE = 1;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_ROOT_RAISED_COSINE = 2;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_GAUSSIAN = 3;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_CUSTOM = 4;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_FIRST_FREQ_LIST_HANDLE = 200000;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_LAST_FREQ_LIST_HANDLE = 209999;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_NO_FREQ_LIST = -1;
  NIFGEN_INT32_IDLE_BEHAVIOR_VAL_HOLD_LAST_VALUE = 400;
  NIFGEN_INT32_IDLE_BEHAVIOR_VAL_JUMP_TO_VALUE = 401;
  NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_TOGGLE = 103;
  NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_HIGH = 101;
  NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_LOW = 102;
  NIFGEN_INT32_OSP_MODE_VAL_OSP_IF = 0;
  NIFGEN_INT32_OSP_MODE_VAL_OSP_BASEBAND = 1;
  NIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR = 0;
  NIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED = 2;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_NONE = 0;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I = 1;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q = 2;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I = 4;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q = 8;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_I = 16;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_I = 16;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_Q = 32;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_Q = 32;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_I = 64;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_Q = 128;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_COMPLEX_DATA = 256;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_I = 512;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_Q = 1024;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_EQUALIZER = 2048;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FUNC = 0;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_ARB = 1;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SEQ = 2;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FREQ_LIST = 101;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SCRIPT = 102;
  NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_TRIG_NONE = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_LEVEL = 103;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_SOFTWARE_EDGE = 104;
  NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE = 101;
  NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE = 102;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_TRIG_NONE = 101;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 102;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_SOFTWARE_EDGE = 104;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_P2P_ENDPOINT_FULLNESS = 106;
  NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL0 = 111;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_NONE = 1000;
  NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED = 300;
  NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL = 301;
  NIFGEN_INT32_TRIGGER_MODE_VAL_SINGLE = 1;
  NIFGEN_INT32_TRIGGER_MODE_VAL_CONTINUOUS = 2;
  NIFGEN_INT32_TRIGGER_MODE_VAL_STEPPED = 3;
  NIFGEN_INT32_TRIGGER_MODE_VAL_BURST = 4;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE = 0;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_EXTERNAL = 1;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG = 2;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL0 = 111;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PXI_STAR = 131;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_7 = 1010;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_0 = 1011;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_1 = 1012;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_2 = 1013;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_3 = 1014;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_OTHER_TERMINAL = 1018;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_INTERNAL = 0;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_EXTERNAL = 1;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_PXI_STAR = 131;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_7 = 1010;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_OTHER_TERMINAL = 1018;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_CLK_IN = 1202;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_DDC_CLK_IN = 1203;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_B = 0;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_D = 1;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_G = 2;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_H = 3;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_I = 4;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_M = 5;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_N = 6;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_NTSC_M = 7;
  NIFGEN_INT32_WAIT_BEHAVIOR_VAL_HOLD_LAST_VALUE = 400;
  NIFGEN_INT32_WAIT_BEHAVIOR_VAL_JUMP_TO_VALUE = 401;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_SINE = 1;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_SQUARE = 2;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_TRIANGLE = 3;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_UP = 4;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_DOWN = 5;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_DC = 6;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_NOISE = 101;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_USER = 102;
}

enum NiFgenReal64AttributeValues {
  option allow_alias = true;
  NIFGEN_REAL64_UNSPECIFIED = 0;
  NIFGEN_REAL64_LOAD_IMPEDANCE_VAL_MATCHED_LOAD_IMPEDANCE = -1;
  NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_50_OHMS = 50;
  NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_75_OHMS = 75;
  NIFGEN_REAL64_SAMPLE_RATE_VAL_EXTERNAL_SAMPLE_RATE = -1;
}

enum NiFgenStringAttributeValuesMapped {
  NIFGEN_STRING_MAPPED_UNSPECIFIED = 0;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_CLOCK_IN_COLLISION_AVOIDANCE = 1;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_NONE_COLLISION_AVOIDANCE = 2;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE = 3;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_PXI_CLOCK_COLLISION_AVOIDANCE = 4;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_RTSI_7_COLLISION_AVOIDANCE = 5;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_CLOCK_IN = 6;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_DDC_CLOCK_IN = 7;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_ONBOARD_CLOCK = 8;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_STAR_LINE = 9;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_0_RTSI_0 = 10;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_1_RTSI_1 = 11;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_2_RTSI_2 = 12;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_3_RTSI_3 = 13;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_4_RTSI_4 = 14;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_5_RTSI_5 = 15;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_6_RTSI_6 = 16;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_7_RTSI_7 = 17;
  NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_CLOCK_IN = 18;
  NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_ONBOARD_CLOCK = 19;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitializeWithChannelsRequest {
  string session_name = 1;
  string resource_name = 2;
  string channel_name = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitializeWithChannelsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_description = 3;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ErrorHandlerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorHandlerResponse {
  int32 status = 1;
  string error_message = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message GetHardwareStateRequest {
  nidevice_grpc.Session vi = 1;
}

message GetHardwareStateResponse {
  int32 status = 1;
  HardwareState state = 2;
  sint32 state_raw = 3;
}

message WaitUntilDoneRequest {
  nidevice_grpc.Session vi = 1;
  sint32 max_time = 2;
}

message WaitUntilDoneResponse {
  int32 status = 1;
}

message IsDoneRequest {
  nidevice_grpc.Session vi = 1;
}

message IsDoneResponse {
  int32 status = 1;
  bool done = 2;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message ConfigureOperationModeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 operation_mode = 3;
}

message ConfigureOperationModeResponse {
  int32 status = 1;
}

message ConfigureOutputModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof output_mode_enum {
    OutputMode output_mode = 2;
    sint32 output_mode_raw = 3;
  }
}

message ConfigureOutputModeResponse {
  int32 status = 1;
}

message ConfigureReferenceClockRequest {
  nidevice_grpc.Session vi = 1;
  string reference_clock_source = 2;
  double reference_clock_frequency = 3;
}

message ConfigureReferenceClockResponse {
  int32 status = 1;
}

message ConfigureOutputImpedanceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double impedance = 3;
}

message ConfigureOutputImpedanceResponse {
  int32 status = 1;
}

message ConfigureOutputEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool enabled = 3;
}

message ConfigureOutputEnabledResponse {
  int32 status = 1;
}

message ConfigureChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channels = 2;
}

message ConfigureChannelsResponse {
  int32 status = 1;
}

message InitiateGenerationRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateGenerationResponse {
  int32 status = 1;
}

message AbortGenerationRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortGenerationResponse {
  int32 status = 1;
}

message ConfigureStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof waveform_enum {
    Waveform waveform = 3;
    sint32 waveform_raw = 4;
  }
  double amplitude = 5;
  double dc_offset = 6;
  double frequency = 7;
  double start_phase = 8;
}

message ConfigureStandardWaveformResponse {
  int32 status = 1;
}

message DefineUserStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double waveform_data_array = 3;
}

message DefineUserStandardWaveformResponse {
  int32 status = 1;
}

message ClearUserStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ClearUserStandardWaveformResponse {
  int32 status = 1;
}

message ConfigureFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double frequency = 3;
}

message ConfigureFrequencyResponse {
  int32 status = 1;
}

message ConfigureAmplitudeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double amplitude = 3;
}

message ConfigureAmplitudeResponse {
  int32 status = 1;
}

message QueryArbWfmCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryArbWfmCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_waveforms = 2;
  sint32 waveform_quantum = 3;
  sint32 minimum_waveform_size = 4;
  sint32 maximum_waveform_size = 5;
}

message CreateWaveformF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double waveform_data_array = 3;
}

message CreateWaveformF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated sint32 waveform_data_array = 3;
}

message CreateWaveformI16Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated nidevice_grpc.NIComplexNumber waveform_data_array = 3;
}

message CreateWaveformComplexF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformFromFileI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  oneof byte_order_enum {
    ByteOrder byte_order = 4;
    sint32 byte_order_raw = 5;
  }
}

message CreateWaveformFromFileI16Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformFromFileF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  oneof byte_order_enum {
    ByteOrder byte_order = 4;
    sint32 byte_order_raw = 5;
  }
}

message CreateWaveformFromFileF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message ConfigureSampleRateRequest {
  nidevice_grpc.Session vi = 1;
  double sample_rate = 2;
}

message ConfigureSampleRateResponse {
  int32 status = 1;
}

message ConfigureArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  double gain = 4;
  double offset = 5;
}

message ConfigureArbWaveformResponse {
  int32 status = 1;
}

message ClearArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof waveform_handle_enum {
    WaveformHandle waveform_handle = 2;
    sint32 waveform_handle_raw = 3;
  }
}

message ClearArbWaveformResponse {
  int32 status = 1;
}

message AllocateNamedWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  sint32 waveform_size = 4;
}

message AllocateNamedWaveformResponse {
  int32 status = 1;
}

message SetNamedWaveformNextWritePositionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  oneof relative_to_enum {
    RelativeTo relative_to = 4;
    sint32 relative_to_raw = 5;
  }
  sint32 offset = 6;
}

message SetNamedWaveformNextWritePositionResponse {
  int32 status = 1;
}

message WriteNamedWaveformF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated double data = 4;
}

message WriteNamedWaveformF64Response {
  int32 status = 1;
}

message WriteNamedWaveformI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated sint32 data = 4;
}

message WriteNamedWaveformI16Response {
  int32 status = 1;
}

message WriteNamedWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated nidevice_grpc.NIComplexNumber data = 4;
}

message WriteNamedWaveformComplexF64Response {
  int32 status = 1;
}

message WriteNamedWaveformComplexI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated nidevice_grpc.NIComplexI16 data = 4;
}

message WriteNamedWaveformComplexI16Response {
  int32 status = 1;
}

message DeleteNamedWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
}

message DeleteNamedWaveformResponse {
  int32 status = 1;
}

message QueryArbSeqCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryArbSeqCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_sequences = 2;
  sint32 minimum_sequence_length = 3;
  sint32 maximum_sequence_length = 4;
  sint32 maximum_loop_count = 5;
}

message CreateArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 waveform_handles_array = 2;
  repeated sint32 loop_counts_array = 3;
}

message CreateArbSequenceResponse {
  int32 status = 1;
  sint32 sequence_handle = 2;
}

message CreateAdvancedArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 waveform_handles_array = 2;
  repeated sint32 loop_counts_array = 3;
  repeated sint32 sample_counts_array = 4;
  repeated sint32 marker_location_array = 5;
}

message CreateAdvancedArbSequenceResponse {
  int32 status = 1;
  repeated sint32 coerced_markers_array = 2;
  sint32 sequence_handle = 3;
}

message ConfigureArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 sequence_handle = 3;
  double gain = 4;
  double offset = 5;
}

message ConfigureArbSequenceResponse {
  int32 status = 1;
}

message ClearArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  oneof sequence_handle_enum {
    SequenceHandle sequence_handle = 2;
    sint32 sequence_handle_raw = 3;
  }
}

message ClearArbSequenceResponse {
  int32 status = 1;
}

message ClearArbMemoryRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearArbMemoryResponse {
  int32 status = 1;
}

message QueryFreqListCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryFreqListCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_freq_lists = 2;
  sint32 minimum_frequency_list_length = 3;
  sint32 maximum_frequency_list_length = 4;
  double minimum_frequency_list_duration = 5;
  double maximum_frequency_list_duration = 6;
  double frequency_list_duration_quantum = 7;
}

message CreateFreqListRequest {
  nidevice_grpc.Session vi = 1;
  oneof waveform_enum {
    Waveform waveform = 2;
    sint32 waveform_raw = 3;
  }
  repeated double frequency_array = 4;
  repeated double duration_array = 5;
}

message CreateFreqListResponse {
  int32 status = 1;
  sint32 frequency_list_handle = 2;
}

message ConfigureFreqListRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 frequency_list_handle = 3;
  double amplitude = 4;
  double dc_offset = 5;
  double start_phase = 6;
}

message ConfigureFreqListResponse {
  int32 status = 1;
}

message ClearFreqListRequest {
  nidevice_grpc.Session vi = 1;
  oneof frequency_list_handle_enum {
    FrequencyListOptions frequency_list_handle = 2;
    sint32 frequency_list_handle_raw = 3;
  }
}

message ClearFreqListResponse {
  int32 status = 1;
}

message WriteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string script = 3;
}

message WriteScriptResponse {
  int32 status = 1;
}

message DeleteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string script_name = 3;
}

message DeleteScriptResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    Signal signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  string output_terminal = 5;
}

message ExportSignalResponse {
  int32 status = 1;
}

message RouteSignalOutRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof route_signal_from_enum {
    RouteSignalFrom route_signal_from = 3;
    sint32 route_signal_from_raw = 4;
  }
  oneof route_signal_to_enum {
    RouteSignalTo route_signal_to = 5;
    sint32 route_signal_to_raw = 6;
  }
}

message RouteSignalOutResponse {
  int32 status = 1;
}

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_enum {
    Trigger trigger = 2;
    sint32 trigger_raw = 3;
  }
  string trigger_id = 4;
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string source = 2;
  sint32 edge = 3;
}

message ConfigureDigitalEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
  int32 status = 1;
}

message ConfigureP2PEndpointFullnessStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 p2p_endpoint_fullness_level = 2;
}

message ConfigureP2PEndpointFullnessStartTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
  string source = 3;
  sint32 edge = 4;
}

message ConfigureDigitalEdgeScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalLevelScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
  string source = 3;
  oneof trigger_when_enum {
    TriggerWhen trigger_when = 4;
    sint32 trigger_when_raw = 5;
  }
}

message ConfigureDigitalLevelScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
}

message ConfigureSoftwareEdgeScriptTriggerResponse {
  int32 status = 1;
}

message DisableScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
}

message DisableScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureClockModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof clock_mode_enum {
    ClockMode clock_mode = 2;
    sint32 clock_mode_raw = 3;
  }
}

message ConfigureClockModeResponse {
  int32 status = 1;
}

message AdjustSampleClockRelativeDelayRequest {
  nidevice_grpc.Session vi = 1;
  double adjustment_time = 2;
}

message AdjustSampleClockRelativeDelayResponse {
  int32 status = 1;
}

message AllocateWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_size = 3;
}

message AllocateWaveformResponse {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message SetWaveformNextWritePositionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  oneof relative_to_enum {
    RelativeTo relative_to = 4;
    sint32 relative_to_raw = 5;
  }
  sint32 offset = 6;
}

message SetWaveformNextWritePositionResponse {
  int32 status = 1;
}

message WriteWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated double data = 4;
}

message WriteWaveformResponse {
  int32 status = 1;
}

message WriteBinary16WaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated sint32 data = 4;
}

message WriteBinary16WaveformResponse {
  int32 status = 1;
}

message WriteWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated nidevice_grpc.NIComplexNumber data = 3;
  sint32 waveform_handle = 4;
}

message WriteWaveformComplexF64Response {
  int32 status = 1;
}

message WriteComplexBinary16WaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated nidevice_grpc.NIComplexI16 data = 4;
}

message WriteComplexBinary16WaveformResponse {
  int32 status = 1;
}

message SelfCalRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message GetSelfCalSupportedRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalSupportedResponse {
  int32 status = 1;
  bool self_cal_supported = 2;
}

message GetSelfCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetExtCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetSelfCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetExtCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message ReadCurrentTemperatureRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadCurrentTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message ConfigureCustomFIRFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double coefficients_array = 3;
}

message ConfigureCustomFIRFilterCoefficientsResponse {
  int32 status = 1;
}

message GetFIRFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetFIRFilterCoefficientsResponse {
  int32 status = 1;
  repeated double coefficients_array = 2;
  sint32 number_of_coefficients_read = 3;
}

message GetStreamEndpointHandleRequest {
  nidevice_grpc.Session vi = 1;
  string stream_endpoint = 2;
}

message GetStreamEndpointHandleResponse {
  int32 status = 1;
  uint32 reader_handle = 2;
}

message WriteP2PEndpointI16Request {
  nidevice_grpc.Session vi = 1;
  string endpoint_name = 2;
  repeated sint32 endpoint_data = 3;
}

message WriteP2PEndpointI16Response {
  int32 status = 1;
}

message ConfigureSynchronizationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 synchronization_source = 3;
}

message ConfigureSynchronizationResponse {
  int32 status = 1;
}

message EnableDigitalPatterningRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message EnableDigitalPatterningResponse {
  int32 status = 1;
}

message DisableDigitalPatterningRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableDigitalPatterningResponse {
  int32 status = 1;
}

message EnableDigitalFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message EnableDigitalFilterResponse {
  int32 status = 1;
}

message DisableDigitalFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableDigitalFilterResponse {
  int32 status = 1;
}

message EnableAnalogFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double filter_correction_frequency = 3;
}

message EnableAnalogFilterResponse {
  int32 status = 1;
}

message DisableAnalogFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableAnalogFilterResponse {
  int32 status = 1;
}

message ConfigureSampleClockSourceRequest {
  nidevice_grpc.Session vi = 1;
  string sample_clock_source = 2;
}

message ConfigureSampleClockSourceResponse {
  int32 status = 1;
}

message ConfigureTriggerModeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof trigger_mode_enum {
    TriggerMode trigger_mode = 3;
    sint32 trigger_mode_raw = 4;
  }
}

message ConfigureTriggerModeResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message CheckAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message CheckAttributeViInt64Response {
  int32 status = 1;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 attribute_value = 2;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    string attribute_value_raw = 4;
    NiFgenStringAttributeValuesMapped attribute_value_mapped = 5;
  }
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    string attribute_value_raw = 4;
    NiFgenStringAttributeValuesMapped attribute_value_mapped = 5;
  }
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message ResetAttributeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message ResetAttributeResponse {
  int32 status = 1;
}

message ManualEnableP2PStreamRequest {
  nidevice_grpc.Session vi = 1;
  string endpoint_name = 2;
}

message ManualEnableP2PStreamResponse {
  int32 status = 1;
}

message CreateWaveformFromFileHWSRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  bool use_rate_from_waveform = 4;
  bool use_gain_and_offset_from_waveform = 5;
}

message CreateWaveformFromFileHWSResponse {
  int32 status = 1;
  sint32 waveform_handle = 2;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/nifgen.mak sha256=5ea7de782af9ede80d0a095945ab98d2067502770ce68c69d91211a0e216fc75 bytes=352 -->
## FILE: src/nifgen/nifgen.mak

- repository: `ni/nimi-python`
- source_path: `src/nifgen/nifgen.mak`
- sha256: `5ea7de782af9ede80d0a095945ab98d2067502770ce68c69d91211a0e216fc75`
- bytes: 352

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/system_tests/grpc_server_config.json sha256=27fa7af2151b6aa1b045964dd3195ce469dd40525fe0137aba750c9c3d83b591 bytes=156 -->
## FILE: src/nifgen/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/nifgen/system_tests/grpc_server_config.json`
- sha256: `27fa7af2151b6aa1b045964dd3195ce469dd40525fe0137aba750c9c3d83b591`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31763,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/system_tests/test_system_nifgen.py sha256=3e2b05f3476c0339d482c98a1608ff8ce40bda3d13252ddfc422e2e1952507d5 bytes=26629 -->
## FILE: src/nifgen/system_tests/test_system_nifgen.py

- repository: `ni/nimi-python`
- source_path: `src/nifgen/system_tests/test_system_nifgen.py`
- sha256: `3e2b05f3476c0339d482c98a1608ff8ce40bda3d13252ddfc422e2e1952507d5`
- bytes: 26629

````python
import os
import pathlib
import sys
import tempfile
import warnings

import grpc
import hightime
import numpy
import pytest

import nifgen

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


# Set up global information we need
test_files_base_dir = os.path.join(os.path.dirname(__file__))


def get_test_file_path(file_name):
    return os.path.join(test_files_base_dir, file_name)


invalid_waveforms = ['Not waveform data',
                     numpy.zeros(100, dtype=numpy.uint16),
                     numpy.zeros(100, dtype=numpy.float32),
                     42,
                     3.14159, ]


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, session_creation_kwargs):
        with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    def test_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_get_attribute_string(self, session):
        model = session.instrument_model
        assert model == 'NI PXIe-5433 (2CH)'

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:invalid_model (2CH);BoardType:PXIe', **session_creation_kwargs):
                assert False
        except nifgen.Error as e:
            # The returned error has changed over time, so accept multiple error codes, descriptions.
            # Users should generally not look for specific error codes and should instead correct their code if they hit an error.
            assert e.code in [-1074134944, -1074134964]
            assert any(
                [
                    e.description.find('Insufficient location information or resource not present in the system.') != -1,
                    e.description.find('The option string parameter contains an entry with an unknown option value.') != -1,
                ]
            )

    def test_get_error(self, session):
        try:
            session.instrument_model = ''
            assert False
        except nifgen.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.
            assert e.description.find('Attribute is read-only.') != -1

    def test_method_get_self_cal_supported(self, session):
        assert session.get_self_cal_supported() in [True, False]

    def test_get_self_cal_last_date_and_time(self, session):
        before = hightime.datetime.now()
        # Returned cal time does not have sub-minute info
        before = before.replace(second=0, microsecond=0)
        last_cal_time = session.get_self_cal_last_date_and_time()
        after = hightime.datetime.now()
        assert before <= last_cal_time <= after

    def test_self_cal(self, session):
        session.self_cal()

    def test_channels_rep_cap(self):
        with nifgen.Session('', '', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe') as session:
            session.func_amplitude = 0.5
            assert session.channels[0:1].func_amplitude == 0.5

            session.channels[0].func_amplitude = 1
            assert session.channels[0].func_amplitude == 1
            assert session.channels[1].func_amplitude == 0.5

    def test_markers_rep_cap(self, session):
        assert '' == session.markers[0].marker_event_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        session.markers[0].marker_event_output_terminal = requested_terminal_name
        assert requested_terminal_name == session.markers[0].marker_event_output_terminal

    def test_data_markers_rep_cap(self, session):
        assert nifgen.DataMarkerEventLevelPolarity.HIGH == session.data_markers[0].data_marker_event_level_polarity

        requested_polarity = nifgen.DataMarkerEventLevelPolarity.LOW
        session.data_markers[0].data_marker_event_level_polarity = requested_polarity
        assert requested_polarity == session.data_markers[0].data_marker_event_level_polarity

    def test_script_triggers_rep_cap(self, session):
        assert '' == session.script_triggers[0].exported_script_trigger_output_terminal

        requested_terminal_name = '/Dev1/PXI_Trig0'
        session.script_triggers[0].exported_script_trigger_output_terminal = requested_terminal_name
        assert requested_terminal_name == session.script_triggers[0].exported_script_trigger_output_terminal

    def test_standard_waveform(self, session):
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 2000000, 1.0, 0.0)
        expected_frequency = 2000000
        with session.initiate():
            assert session.func_amplitude == 2.0
            assert session.func_waveform == nifgen.Waveform.SINE
            actual_frequency = session.func_frequency
            in_range = abs(actual_frequency - expected_frequency) <= max(1e-09 * max(abs(actual_frequency), abs(expected_frequency)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
            assert in_range is True
            assert session.func_dc_offset == 1.0
            assert session.func_start_phase == 0.0
            assert session.is_done() is False

    def test_frequency_list(self, session):
        session.output_mode = nifgen.OutputMode.FREQ_LIST
        duration_array = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        frequency_array = [1000, 100900, 200800, 300700, 400600, 500500, 600400, 700300, 800200, 900100]
        waveform_handle = session.create_freq_list(nifgen.Waveform.SQUARE, frequency_array, duration_array)
        session.configure_freq_list(waveform_handle, 2.0, 0, 0)
        session.trigger_mode = nifgen.TriggerMode.CONTINUOUS
        session.output_enabled = True
        assert session.func_waveform == nifgen.Waveform.SQUARE
        assert session.func_amplitude == 2.0

    def test_clear_freq_list(self, session):
        session.clear_freq_list(-1)

    def test_create_waveform_from_list(self, session):
        data = [0.1] * 10000
        assert type(session.create_waveform(data)) is int

    def test_configure_arb_waveform(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.output_mode = nifgen.OutputMode.ARB
        session.configure_arb_waveform(session.create_waveform(waveform_data), 1.0, 0.0)

    def test_disable(self, session):
        channel = session.channels['0']
        assert channel.output_enabled is True
        session.disable()
        assert channel.output_enabled is False

    def test_get_ext_cal_last_date_and_time(self, session):
        try:
            session.get_ext_cal_last_date_and_time()
            assert False, "If we hit this, it means a simulated 5433 now works properly for this. You can now remove the check for -1074135040"
        except nifgen.Error as e:
            assert e.code == -1074118632 or e.code == -1074135040  # This operation is not supported for simulated device or Unrecoverable Failure

    def test_get_ext_cal_last_temp(self, session):
        try:
            session.get_ext_cal_last_temp()
        except nifgen.Error as e:
            assert e.code == -1074135023  # Function or method not supported for 5413/23/33 and not supported on any other FGen when simulated

    def test_get_ext_cal_recommended_interval(self, session):
        interval = session.get_ext_cal_recommended_interval()
        assert interval.days == 730  # recommended external cal interval is 24 months

    def test_get_hardware_state(self, session):
        assert session.get_hardware_state() == nifgen.HardwareState.IDLE

    def test_get_self_cal_last_temp(self, session):
        assert session.get_self_cal_last_temp() == 0.0  # returns 0.0 for a simulated 5433

    def test_query_arb_wfm_capabilities(self, session):
        max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size = session.query_arb_wfm_capabilities()
        assert max_number_of_waveform == 4194304  # default values for max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size for a simulated 5433 is 4194304, 1, 4, 268435456 respectively
        assert waveform_quantum == 1
        assert minimum_waveform_size == 4
        assert maximum_waveform_size == 268435456

    def test_query_freq_list_capabilities(self, session):
        maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum = session.query_freq_list_capabilities()  # comparing with default values for simulated 5433
        assert maximum_number_of_freq_lists == 9999
        assert minimum_frequency_list_length == 1
        assert maximum_frequency_list_length == 1024
        assert minimum_frequency_list_duration == 1e-08
        assert maximum_frequency_list_duration == 2814749.76711
        assert frequency_list_duration_quantum == 1e-08

    def test_read_current_temperature(self, session):
        assert session.read_current_temperature() > 25.0

    def test_allocate_waveform(self, session):
        handles = [session.allocate_waveform(100) in range(10)]
        assert len(handles) == len(set(handles)), "Failed, waveform handles aren't unique."
        try:
            session.allocate_waveform(2000000000)
            assert False
        except nifgen.Error as e:
            assert e.code == -1074101596  # Such a big waveform doesn't fit!

    def test_clear_waveform_memory(self, session):
        session.clear_arb_memory()
        session.clear_user_standard_waveform()
        session.configure_arb_sequence(0, 1.0, 0)
        session.clear_arb_sequence(-1)
        session.delete_waveform(-1)

    def test_query_arb_seq_capabilities(self, session):
        maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count = session.query_arb_seq_capabilities()
        assert maximum_number_of_sequences == 65535
        assert minimum_sequence_length == 1
        assert maximum_sequence_length >= minimum_sequence_length
        assert maximum_loop_count == 16777215

    def test_create_arb_sequence(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data)]
        # This relies on value of sequence handles starting at 0 and incrementing, not ideal but true for now.
        assert 0 == session.create_arb_sequence(waveform_handles_array, [10])
        assert 1 == session.create_arb_sequence(waveform_handles_array, [10])

    def test_create_advanced_arb_sequence(self, session):
        seq_handle_base = 0  # On 5433, handles start at 0.
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data), session.create_waveform(waveform_data), session.create_waveform(waveform_data)]
        marker_location_array = [0, 16, 32]
        sample_counts_array = [256, 128, 64]
        loop_counts_array = [10, 20, 30]
        session.output_mode = nifgen.OutputMode.SEQ
        # Test relies on value of sequence handles starting at a known value and incrementing sequentially. Hardly ideal.
        assert ([], seq_handle_base + 0) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array)
        assert ([], seq_handle_base + 1) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array)
        assert (marker_location_array, seq_handle_base + 2) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, marker_location_array=marker_location_array)
        assert (marker_location_array, seq_handle_base + 3) == session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array, marker_location_array=marker_location_array)

    def test_arb_script(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        session.write_waveform('wfmSine', waveform_data)
        session.arb_sample_rate = 10000000
        script = '''script myScript0
        repeat 3
        Generate wfmSine
        end repeat
        end script'''
        session.write_script(script)
        session.script_to_generate = 'myScript0'
        session.commit()
        session.delete_script('myScript0')
        actual_sample_rate = session.arb_sample_rate
        in_range = abs(actual_sample_rate - 10000000) <= max(1e-09 * max(abs(actual_sample_rate), abs(10000000)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert in_range is True

    def test_reset(self, session):
        default_output_mode = session.output_mode
        assert default_output_mode == nifgen.OutputMode.ARB
        session.output_mode = nifgen.OutputMode.SEQ
        assert session.output_mode == nifgen.OutputMode.SEQ
        session.reset()
        assert session.output_mode == nifgen.OutputMode.ARB

    def test_reset_device(self, session):
        default_trigger_mode = session.trigger_mode
        assert default_trigger_mode == nifgen.TriggerMode.CONTINUOUS
        session.trigger_mode = nifgen.TriggerMode.STEPPED
        non_default_trigger_mode = nifgen.TriggerMode.STEPPED
        assert non_default_trigger_mode == nifgen.TriggerMode.STEPPED
        session.reset_device()
        assert session.trigger_mode == nifgen.TriggerMode.CONTINUOUS

    def test_reset_with_default(self, session):
        default_sample_rate = session.arb_sample_rate
        assert default_sample_rate == 250000000.0
        session.arb_sample_rate = 100000000.0
        non_default_arb_sample_rate = session.arb_sample_rate
        assert non_default_arb_sample_rate == 100000000.0
        session.reset_with_defaults()
        assert session.arb_sample_rate == 250000000.0

    def test_write_waveform_from_list(self, session):
        data = [0.1] * 10000
        session.write_waveform(session.allocate_waveform(len(data)), data)

    def test_write_named_waveform_from_list(self, session):
        data = [0.1] * 10000
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)

    def test_write_waveform_wrong_type(self, session):
        waveform_handle = session.allocate_waveform(100)
        for data in invalid_waveforms:
            try:
                session.write_waveform(waveform_handle, data)
                assert False
            except (TypeError, ValueError):
                pass

    def test_set_waveform_next_write_position(self, session):
        session.set_next_write_position(session.allocate_waveform(10), nifgen.RelativeTo.START, 5)

    def test_write_waveform_from_filei64(self, session):
        session.create_waveform_from_file_i16(get_test_file_path('SineI16BigEndian_1000.bin'), nifgen.ByteOrder.BIG)

    def test_named_waveform_operations(self, session):
        waveform_name = 'Waveform'
        waveform_size = 4096
        write_offset = 0
        waveform_data_1 = [x * (1.0 / 256.0) for x in range(256)]
        waveform_data_2 = [x * (-1.0 / 256.0) for x in range(256)]
        session.allocate_named_waveform(waveform_name, waveform_size)
        session.set_next_write_position(waveform_name, nifgen.RelativeTo.START, write_offset)
        session.write_waveform(waveform_name, waveform_data_1)
        session.write_waveform(waveform_name, waveform_data_2)
        session.delete_waveform(waveform_name)

    def test_handle_waveform_operations(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handle = session.create_waveform(waveform_data_array=waveform_data)
        session.delete_waveform(waveform_handle)

    def test_write_waveform_from_file_f64(self, session):
        try:
            session.create_waveform_from_file_f64(get_test_file_path('SineI16BigEndian_1000.bin'), nifgen.ByteOrder.BIG)
        except nifgen.Error as e:
            assert e.code == -1074135024  # Expecting error since loading an I16 file when f64 is expected.

    def test_wait_until_done(self, session):
        session.wait_until_done(hightime.timedelta(milliseconds=20))

    def test_user_standard_waveform(self, session):
        wfm_points = [1] * 8192
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(nifgen.Waveform.USER, 1.0, 2000000, 1.0, 0.0)
        session.define_user_standard_waveform(wfm_points)
        session.clear_user_standard_waveform()

    ''' Removed due to OSP disabled - #891
    def test_fir_filter_coefficients(self, session_creation_kwargs):
        with nifgen.Session('', '0', False, 'Simulate=1, DriverSetup=Model:5441;BoardType:PXI', **session_creation_kwargs) as session:
            coeff_array = [0 for i in range(95)]
            coeff_array[0] = -1.0
            coeff_array[2] = 1.0
            session.configure_custom_fir_filter_coefficients(coeff_array)
            session.commit()
            array = session.get_fir_filter_coefficients()
            assert len(array) == len(coeff_array)
            assert array == coeff_array
    '''

    def test_send_software_edge_trigger_start_deprecated(self, session):
        warnings.filterwarnings("always", category=DeprecationWarning)

        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        with session.initiate():
            with warnings.catch_warnings(record=True) as w:
                session.send_software_edge_trigger()
                assert len(w) == 1
                assert issubclass(w[0].category, DeprecationWarning)

    def test_send_software_edge_trigger_script_deprecated(self, session):
        warnings.filterwarnings("always", category=DeprecationWarning)

        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        with session.initiate():
            with warnings.catch_warnings(record=True) as w:
                session.script_triggers[0].send_software_edge_trigger()
                assert len(w) == 1
                assert issubclass(w[0].category, DeprecationWarning)

    def test_send_software_edge_trigger_start(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        with session.initiate():
            session.send_software_edge_trigger(nifgen.Trigger.START, 'None')

    def test_send_software_edge_trigger_script(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        session.create_waveform(waveform_data)
        session.output_mode = nifgen.OutputMode.SCRIPT
        session.script_triggers[0].digital_edge_script_trigger_source = 'PFI0'
        session.script_triggers[0].digital_edge_script_trigger_edge = nifgen.ScriptTriggerDigitalEdgeEdge.RISING
        with session.initiate():
            session.send_software_edge_trigger(nifgen.Trigger.SCRIPT, 'ScriptTrigger0')

    def test_channel_format_types(self, session_creation_kwargs):
        with nifgen.Session('', [0, 1], False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', range(2), False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', '0,1', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session('', None, False, 'Simulate=1, DriverSetup=Model:5433 (2CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2
        with nifgen.Session(resource_name='', reset_device=False, options='Simulate=1, DriverSetup=Model:5433 (2CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            assert simulated_session.channel_count == 2

    def test_import_export_buffer(self, session):
        test_value_1 = 1.0
        test_value_2 = 2.0
        session.arb_gain = test_value_1
        assert session.arb_gain == test_value_1
        buffer = session.export_attribute_configuration_buffer()
        session.arb_gain = test_value_2
        assert session.arb_gain == test_value_2
        session.import_attribute_configuration_buffer(buffer)
        assert session.arb_gain == test_value_1

    def test_import_export_file(self, session):
        test_value_1 = 2.0
        test_value_2 = 3.0
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        session.arb_gain = test_value_1
        assert session.arb_gain == test_value_1
        session.export_attribute_configuration_file(path)
        session.arb_gain = test_value_2
        assert session.arb_gain == test_value_2
        session.import_attribute_configuration_file(path)
        assert session.arb_gain == test_value_1
        os.remove(path)

    def test_get_channel_name(self, session):
        name = session.get_channel_name(1)
        assert name == '0'

    def test_create_waveform_wrong_type(self, session):
        for data in invalid_waveforms:
            try:
                session.create_waveform(data)
                assert False
            except (TypeError, ValueError):
                pass

    def test_create_advanced_arb_sequence_wrong_size(self, session):
        waveform_data = [x * (1.0 / 256.0) for x in range(256)]
        waveform_handles_array = [session.create_waveform(waveform_data), session.create_waveform(waveform_data), session.create_waveform(waveform_data)]
        marker_location_array = [0, 16]
        loop_counts_array = [10, 20, 30]
        session.output_mode = nifgen.OutputMode.SEQ
        # Test relies on value of sequence handles starting at a known value and incrementing sequentially. Hardly ideal.
        with pytest.raises(ValueError) as exc_info:
            session.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array=loop_counts_array, marker_location_array=marker_location_array)
        assert exc_info.value.args[0] == 'Length of marker_location_array and waveform_handles_array parameters do not match.'
        assert str(exc_info.value) == 'Length of marker_location_array and waveform_handles_array parameters do not match.'

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_create_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        assert type(session.create_waveform(data)) is int

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_create_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        assert type(session.create_waveform(data)) is int

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        session.write_waveform(session.allocate_waveform(len(data)), data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        session.write_waveform(session.allocate_waveform(len(data)), data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_named_waveform_from_numpy_array_float64(self, session):
        data = numpy.ndarray(10000, dtype=numpy.float64)
        data.fill(0.5)
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)

    # Test doesn't run over gRPC because numpy isn't supported by gRPC.
    def test_write_named_waveform_numpy_array_int16(self, session):
        data = numpy.ndarray(10000, dtype=numpy.int16)
        data.fill(256)
        session.allocate_named_waveform('foo', len(data))
        session.write_waveform('foo', data)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = nifgen.GrpcSessionOptions(grpc_channel, '')
        return {'grpc_options': grpc_options}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/templates/session.py/create_waveform.py.mako sha256=473bb2255dd56b47266fa6c06d3ee60361b3ce249f8ef1790b42ea296acc0a8b bytes=1551 -->
## FILE: src/nifgen/templates/session.py/create_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nifgen/templates/session.py/create_waveform.py.mako`
- sha256: `473bb2255dd56b47266fa6c06d3ee60361b3ce249f8ef1790b42ea296acc0a8b`
- bytes: 1551

````mako
<%page args="f, config"/>\
<%
    '''Dispatches to the appropriate "create waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            import numpy
            if waveform_data_array.dtype == numpy.float64:
                return self._create_waveform_f64_numpy(waveform_data_array)
            elif waveform_data_array.dtype == numpy.int16:
                return self._create_waveform_i16_numpy(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(waveform_data_array.dtype, numpy.float64, numpy.int16))
        elif isinstance(waveform_data_array, array.array):
            if waveform_data_array.typecode == 'd':
                return self._create_waveform_f64(waveform_data_array)
            elif waveform_data_array.typecode == 'h':
                return self._create_waveform_i16(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(waveform_data_array.typecode, 'd (double)', 'h (16 bit int)'))

        return self._create_waveform_f64(waveform_data_array)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/templates/session.py/delete_waveform.py.mako sha256=e0ad1143391ffd46b4ab432f8f5fe88f314c7785ff38446e3e1ed989185b6870 bytes=617 -->
## FILE: src/nifgen/templates/session.py/delete_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nifgen/templates/session.py/delete_waveform.py.mako`
- sha256: `e0ad1143391ffd46b4ab432f8f5fe88f314c7785ff38446e3e1ed989185b6870`
- bytes: 617

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if isinstance(waveform_name_or_handle, str):
            return self._delete_named_waveform(waveform_name_or_handle)
        else:
            return self._clear_arb_waveform(waveform_name_or_handle)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/templates/session.py/send_software_edge_trigger.py.mako sha256=48cbe1fd8a97432bbf5f2fd0bbe8e5e480bda51345b6ed27c7c4efa7f9f2f69b bytes=1434 -->
## FILE: src/nifgen/templates/session.py/send_software_edge_trigger.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nifgen/templates/session.py/send_software_edge_trigger.py.mako`
- sha256: `48cbe1fd8a97432bbf5f2fd0bbe8e5e480bda51345b6ed27c7c4efa7f9f2f69b`
- bytes: 1434

````mako
<%page args="f, config"/>\
<%
    '''Need different behavior depending on whether we are called on a rep cap container or not'''
    import build.helper as helper
%>\
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if trigger is None or trigger_id is None:
            import warnings
            warnings.warn('trigger and trigger_id should now always be passed in to the method', category=DeprecationWarning)

            # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
            if len(self._repeated_capability) > 0:
                trigger_id = self._repeated_capability
                trigger = enums.Trigger.SCRIPT
            else:
                trigger_id = "None"
                trigger = enums.Trigger.START

        elif trigger is not None and trigger_id is not None:
            pass  # This is how the function should be called

        else:
            raise ValueError('Both trigger ({}) and trigger_id ({}) should be passed in to the method'.format(str(trigger), str(trigger_id)))

        if type(trigger) is not enums.Trigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.Trigger))
        self._interpreter.send_software_edge_trigger(trigger, trigger_id)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/templates/session.py/set_next_write_position.py.mako sha256=1a439f53d2a7c17c9f1ff0d7f69df362b0bdd44e2dd5814e921a0d3391e2fb3a bytes=690 -->
## FILE: src/nifgen/templates/session.py/set_next_write_position.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nifgen/templates/session.py/set_next_write_position.py.mako`
- sha256: `1a439f53d2a7c17c9f1ff0d7f69df362b0bdd44e2dd5814e921a0d3391e2fb3a`
- bytes: 690

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if isinstance(waveform_name_or_handle, str):
            return self._set_named_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
        else:
            return self._set_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nifgen/templates/session.py/write_waveform.py.mako sha256=34eb38c4cefbad5497b4a36ae9e5d36d07d6a7747d359d1904eb97615b0514f2 bytes=1963 -->
## FILE: src/nifgen/templates/session.py/write_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nifgen/templates/session.py/write_waveform.py.mako`
- sha256: `34eb38c4cefbad5497b4a36ae9e5d36d07d6a7747d359d1904eb97615b0514f2`
- bytes: 1963

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "write waveform" method based on the waveform type.'''
    import build.helper as helper
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        use_named = isinstance(waveform_name_or_handle, str)
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(data)).find("'numpy.ndarray'") != -1:
            import numpy
            if data.dtype == numpy.float64:
                return self._write_named_waveform_f64_numpy(waveform_name_or_handle, data) if use_named else self._write_waveform_numpy(waveform_name_or_handle, data)
            elif data.dtype == numpy.int16:
                return self._write_named_waveform_i16_numpy(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform_numpy(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(data.dtype, numpy.float64, numpy.int16))
        elif isinstance(data, array.array):
            if data.typecode == 'd':
                return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
            elif data.typecode == 'h':
                return self._write_named_waveform_i16(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(data.typecode, 'd (double)', 'h (16 bit int)'))

        return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/examples/nimodinst_all_devices.py sha256=f69e6c699373e730fe55f607d7f11eb47568ffd8da4bd6ddc021853d2a18554f bytes=468 -->
## FILE: src/nimodinst/examples/nimodinst_all_devices.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/examples/nimodinst_all_devices.py`
- sha256: `f69e6c699373e730fe55f607d7f11eb47568ffd8da4bd6ddc021853d2a18554f`
- bytes: 468

````python
#!/usr/bin/python

import nimodinst


def example():
    with nimodinst.Session('') as session:
        if len(session) > 0:
            print("%d items" % len(session))
            print("{: >20} {: >15} {: >10}".format('Name', 'Model', 'S/N'))
        for d in session:
            print(f"{d.device_name: >20} {d.device_model: >15} {d.serial_number: >10}")


def _main():
    example()


def test_example():
    example()


if __name__ == '__main__':
    _main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nimodinst/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nimodinst/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/attributes.py sha256=7b4b7236b0bf743a5347b439570437dd3fe4e049000fc92e0a7d37ea88f48988 bytes=2399 -->
## FILE: src/nimodinst/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/attributes.py`
- sha256: `7b4b7236b0bf743a5347b439570437dd3fe4e049000fc92e0a7d37ea88f48988`
- bytes: 2399

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 25.0.0f85
attributes = {
    0: {
        'access': 'read only',
        'documentation': {
            'description': 'The name of the device, which can be used to open an instrument driver session for that device'
        },
        'name': 'DEVICE_NAME',
        'type': 'ViString'
    },
    1: {
        'access': 'read only',
        'documentation': {
            'description': 'The model of the device (for example, NI PXI-5122)'
        },
        'name': 'DEVICE_MODEL',
        'type': 'ViString'
    },
    2: {
        'access': 'read only',
        'documentation': {
            'description': 'The serial number of the device'
        },
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    10: {
        'access': 'read only',
        'documentation': {
            'description': 'The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'SLOT_NUMBER',
        'type': 'ViInt32'
    },
    11: {
        'access': 'read only',
        'documentation': {
            'description': 'The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.'
        },
        'name': 'CHASSIS_NUMBER',
        'type': 'ViInt32'
    },
    12: {
        'access': 'read only',
        'documentation': {
            'description': 'The bus on which the device has been enumerated.'
        },
        'name': 'BUS_NUMBER',
        'type': 'ViInt32'
    },
    13: {
        'access': 'read only',
        'documentation': {
            'description': 'The socket number on which the device has been enumerated'
        },
        'name': 'SOCKET_NUMBER',
        'type': 'ViInt32'
    },
    17: {
        'access': 'read only',
        'documentation': {
            'description': '**PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32'
    },
    18: {
        'access': 'read only',
        'documentation': {
            'description': '**MAX_PCIEXPRESS_LINK_WIDTH**'
        },
        'name': 'MAX_PCIEXPRESS_LINK_WIDTH',
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nimodinst/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/config.py sha256=cea3149eaeb7e5b44a39c8796f68f2a6c0b3d082c05edd362c4dfe8a9e29dca7 bytes=1083 -->
## FILE: src/nimodinst/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/config.py`
- sha256: `cea3149eaeb7e5b44a39c8796f68f2a6c0b3d082c05edd362c4dfe8a9e29dca7`
- bytes: 1083

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 25.0.0f85
config = {
    'api_version': '25.0.0f85',
    'c_function_prefix': 'niModInst_',
    'close_function': 'CloseInstalledDevicesSession',
    'context_manager_name': {
    },
    'custom_types': [
    ],
    'driver_name': 'NI-ModInst',
    'extra_errors_used': [
    ],
    'grpc_service_class_prefix': 'NiModInst',
    'init_function': 'OpenInstalledDevicesSession',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nimodinst',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niModInst.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niModInst_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nimodinst',
    'repeated_capabilities': [
    ],
    'session_class_description': 'A NI-ModInst session to get device information',
    'session_handle_parameter_name': 'handle'
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/config_addon.py sha256=7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2 bytes=259 -->
## FILE: src/nimodinst/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/config_addon.py`
- sha256: `7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2017',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/enums.py sha256=9f01f24d26d0f376239c6a3e1b90a1e312b300238b86fab8a98d01b8e01cb483 bytes=108 -->
## FILE: src/nimodinst/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/enums.py`
- sha256: `9f01f24d26d0f376239c6a3e1b90a1e312b300238b86fab8a98d01b8e01cb483`
- bytes: 108

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 25.0.0f85
enums = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nimodinst/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/functions.py sha256=bdfe85803eb053a3130708921beb92c07f372033be031687220c9e9b8667c6b4 bytes=12351 -->
## FILE: src/nimodinst/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/functions.py`
- sha256: `bdfe85803eb053a3130708921beb92c07f372033be031687220c9e9b8667c6b4`
- bytes: 12351

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-ModInst API metadata version 25.0.0f85
functions = {
    'CloseInstalledDevicesSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCleans up the NI-ModInst session created by a call to\nniModInst_OpenInstalledDevicesSession. Call this function when you are\nfinished using the session handle and do not use this handle again.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtendedErrorInfo': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns detailed information about the last error that occurred in the\ncurrent thread during a call to one of the NI-ModInst functions. When\none of the other functions returns a negative value as its return value,\nimmediately call this function to get detailed information about the\nerror. Because error information is stored on a thread-by-thread basis,\nbe sure to call this function in the same thread that called the\nfunction that returned an error. The extended error information is\nreturned as a string. To find out the length of the error information\nstring before you allocate a buffer for it, call this function and pass\n0 as the errorInfoBufferSize parameter or NULL as the errorInfo\nparameter. When you do this, the function returns the size of the buffer\nrequired to hold the error information string as its return value. You\ncan then allocate an appropriately sized string character buffer and\ncall this function again.\n'
        },
        'included_in_proto': False,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the buffer allocated and passed in as the errorInfo\nparameter. The buffer should be large enough to hold the errorInfo\nstring (including a NULL terminating character). The size of the buffer\nallocated and passed in as the errorInfo parameter. The buffer should be\nlarge enough to hold the errorInfo string (including a NULL terminating\ncharacter). Refer to the function help to find out how to determine the\nexact buffer size required.\n'
                },
                'name': 'errorInfoBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The character buffer into which the error information string is copied.'
                },
                'name': 'errorInfo',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorInfoBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetInstalledDeviceAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns an integer attribute specified by the attributeID parameter for\na device specified by the handle and index parameters. The handle\nparameter is expected to be a valid handle returned by\nniModInst_OpenInstalledDevicesSession. It therefore acts as a handle to\na list of installed devices. The index parameter specifies the device in\nthe list for which you want the attribute.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA zero-based index that specifies the device for which you want the\nattribute. This index parameter should be between 0 and (deviceCount -\n1), inclusive, where deviceCount is the number of installed devices\nreturned by niModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the integer attribute you want to query. Valid Values Slot\nNumber--the slot (for example, in a PXI chassis) in which the device is\ninstalled. This attribute can only be queried for PXI devices installed\nin a chassis that has been properly identified in MAX. Chassis\nNumber--the number of the chassis in which the device is installed. This\nattribute can only be queried for PXI devices installed in a chassis\nthat has been properly identified in MAX. Bus Number--the bus on which\nthe device has been enumerated. Socket Number--the socket number on\nwhich the device has been enumerated. Notes The bus number and socket\nnumber can be used to form a VISA resource string for this device, of\nthe form "PXI::::INSTR". Traditional NI-DAQ devices do not support the\nchassis number, bus number, and socket number attributes.\n'
                },
                'name': 'attributeId',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to a signed 32-bit integer variable that receives the value of\nthe requested attribute.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetInstalledDeviceAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a string attribute specified by the attributeID parameter for a\ndevice specified by the handle and index parameters. The handle\nparameter is expected to be a valid handle returned by\nniModInst_OpenInstalledDevicesSession. Therefore, it acts as a handle\nto a list of installed devices. The index parameter specifies for which\ndevice in the list you want the attribute. To find out the length of the\ndevice name string before you allocate a buffer for it, simply call this\nfunction and pass 0 as the attributeValueBufferSize parameter or NULL as\nthe attributeValue parameter. When you do this, the function returns the\nsize of the buffer required to hold the attribute value string as its\nreturn value. You can then allocate an appropriately sized character\nbuffer and call this function again.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe NI-ModInst session handle created by\nniModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA zero-based index that specifies the device for which you want the\nattribute. This index parameter should be between 0 and (deviceCount -\n1), inclusive, where deviceCount is the number of installed devices\nreturned by niModInst_OpenInstalledDevicesSession.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the string attribute you want to query. Valid Values\nNIMODINST_ATTR_DEVICE_NAME--the name of the device, which can be used\nto open an instrument driver session for that device\nNIMODINST_ATTR_DEVICE_MODEL--the model of the device (for example, NI\nPXI-5122) NIMODINST_ATTR_SERIAL_NUMBER--the serial number of the\ndevice\n'
                },
                'name': 'attributeId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe size of the buffer allocated and passed in as the attributeValue\nparameter. The buffer should be large enough to hold the attribute value\nstring (including a NULL terminating character). Refer to the\nDescription section for information on how to determine the exact buffer\nsize required.\n'
                },
                'name': 'attributeValueBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The character buffer into which the attribute value string is copied.'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'attributeValueBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'OpenInstalledDevicesSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates a handle to a list of installed devices supported by the\nspecified driver. Call this function and pass in the name of an NI \ninstrument driver, such as "NI-SCOPE". This function\nsearches the system and constructs a list of all the installed devices\nthat are supported by that driver, and then returns both a handle to\nthis list and the number of devices found. The handle is used with other\nfunctions to query for attributes such as device name and model, and to\nsafely discard the list when finished. Note This handle reflects the\nsystem state when the handle is created (that is, when you call this\nfunction. If you remove devices from the system or rename them in\nMeasurement & Automation Explorer (MAX), this handle may not refer to an\naccurate list of devices. You should destroy the handle using\nniModInst_CloseInstalledDevicesSession and create a new handle using\nthis function.\n'
        },
        'included_in_proto': False,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA string specifying the driver whose supported devices you want to find.\nThis string is not case-sensitive. Some examples are: NI-SCOPE niScope\nNI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If\nyou use the empty string for this parameter, NI-ModInst creates a list\nof all Modular Instruments devices installed in the system.\n'
                },
                'name': 'driver',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to a ViSession variable that receives the value of the\nNI-ModInst session handle. This value acts as a handle to the list of\ninstalled devices and is used in other NI-ModInst functions.\n'
                },
                'name': 'handle',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA pointer to an integer variable that receives the number of devices\nfound in the system that are supported by the driver specified in the\ndriver parameter.\n'
                },
                'name': 'deviceCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/nimodinst/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/nimodinst.mak sha256=80e0246326346deb648c101886d9e8ae53a2e18528e7ba57b35d3c100a28333a bytes=932 -->
## FILE: src/nimodinst/nimodinst.mak

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/nimodinst.mak`
- sha256: `80e0246326346deb648c101886d9e8ae53a2e18528e7ba57b35d3c100a28333a`
- bytes: 932

````makefile
include $(BUILD_HELPER_DIR)/defines.mak
include $(BUILD_HELPER_DIR)/tools.mak

# We want everything but enums.py
MODULE_FILES_TO_GENERATE := $(filter-out enums.py _attributes.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out rep_caps.rst enums.rst,$(DEFAULT_RST_FILES_TO_GENERATE))

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for ModInst
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))
# Need to signal the top level makefile to run tests again
	$(_hide_cmds)$(call trigger_unit_tests)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/system_tests/test_system_nimodinst.py sha256=1163a9aff9ac72fe76b259f508ed27563f91b2a7a88814ff51f0e5b3735ff8b7 bytes=4141 -->
## FILE: src/nimodinst/system_tests/test_system_nimodinst.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/system_tests/test_system_nimodinst.py`
- sha256: `1163a9aff9ac72fe76b259f508ed27563f91b2a7a88814ff51f0e5b3735ff8b7`
- bytes: 4141

````python
#!/usr/bin/python

import nimodinst
import re


def test_bad_device_family():
    with nimodinst.Session('FAKE') as session:
        assert len(session) == 0


def test_no_device_family():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'


def test_device_family_string_with_dashes():
    with nimodinst.Session('NI-SCOPE') as session:
        assert len(session) > 0, 'This test expects a device supported by NI-SCOPE in the system (real or simulated).'


def test_device_family_string_without_dashes():
    with nimodinst.Session('niscope') as session:
        assert len(session) > 0, 'This test expects a device supported by NI-SCOPE in the system (real or simulated).'


def test_int_attribute_error_on_non_existant_device():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.devices[device].slot_number
            assert False
        except IndexError:
            pass


def test_string_attribute_error_on_non_existant_device():
    with nimodinst.Session('') as session:
        device = len(session) + 1
        try:
            session.devices[device].slot_number
            assert False
        except IndexError:
            pass


def test_device_name_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].device_name, str)
        assert len(session.devices[0].device_name) > 0  # device name must be at least 1 character


def test_device_model_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert len(session.devices[0].device_model) > 0
        assert isinstance(session.devices[0].device_model, str)
        pattern = r'(NI )?[A-Z]+e?-\d\d\d\d'
        assert re.search(pattern, session.devices[0].device_model) is not None  # NI Model numbers are generally "NI PXIe-2532", but might also be "USB-2532"


def test_serial_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        pattern = r'^[0-9A-F]+$'
        assert isinstance(session.devices[0].serial_number, str)
        assert (len(session.devices[0].serial_number) == 0) or (re.search(pattern, session.devices[0].serial_number) is not None)  # NI Serial numbers hex unless it is simulated than it is 0


def test_bus_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].bus_number, int)


def test_chassis_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].chassis_number, int)


def test_max_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].max_pciexpress_link_width, int)


def test_pciexpress_link_width_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].pciexpress_link_width, int)


def test_slot_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].slot_number, int)


def test_socket_number_attribute():
    with nimodinst.Session('') as session:
        assert len(session) > 0, 'This test expects an instrument in the system (real or simulated).'
        assert isinstance(session.devices[0].socket_number, int)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/templates/_library_interpreter.py/_get_error_description.py.mako sha256=583b995619233d183ca995fad14181d5b4b36f54876a8137fb6dd1febe1c0b0f bytes=1185 -->
## FILE: src/nimodinst/templates/_library_interpreter.py/_get_error_description.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/templates/_library_interpreter.py/_get_error_description.py.mako`
- sha256: `583b995619233d183ca995fad14181d5b4b36f54876a8137fb6dd1febe1c0b0f`
- bytes: 1185

````mako
    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into the cfunc rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return 'Failed to retrieve error description.'
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/templates/session.py.mako sha256=658a67099f0cb37a79831b649b694a3cdffe7cd75b7054a86ab2e426e611d35f bytes=6325 -->
## FILE: src/nimodinst/templates/session.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/templates/session.py.mako`
- sha256: `658a67099f0cb37a79831b649b694a3cdffe7cd75b7054a86ab2e426e611d35f`
- bytes: 6325

````mako
# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = helper.filter_codegen_attributes(config['attributes'])
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.filter_codegen_functions(functions)

    close_function_name = helper.camelcase_to_snakecase(config['close_function'])
%>\

import ${module_name}._library_interpreter as _library_interpreter
import ${module_name}.errors as errors

# Used for __repr__ and __str__
import pprint

pp = pprint.PrettyPrinter(indent=4)


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id)


class _Device(object):

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, owner, index):
        self._index = index
% for attribute in helper.sorted_attrs(attributes):
        self.${attributes[attribute]['name'].lower()} = Attribute${attributes[attribute]['type']}(owner, ${attribute}, index=index)
%   if 'documentation' in attributes[attribute]:
        '''
        ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
        '''
%   endif
% endfor
        self._param_list = 'owner=' + pp.pformat(owner) + ', index=' + pp.pformat(index)
        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
% for attribute in helper.sorted_attrs(attributes):
        ret_str += '    ${attributes[attribute]['name'].lower()} = ' + pp.pformat(self.${attributes[attribute]['name'].lower()}) + '\n'
% endfor
        return ret_str

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index', '_param_list', '__class__', '__name__', '__repr__', '__str__', '__setattr__', ]:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class _DeviceIterable(object):
    def __init__(self, owner, count):
        self._current_index = 0
        self._owner = owner
        self._count = count
        self._param_list = 'owner=' + pp.pformat(owner) + ', count=' + pp.pformat(count)
        self._is_frozen = True

    def _get_next(self):
        if self._current_index + 1 > self._count:
            raise StopIteration
        else:
            dev = _Device(self._owner, self._current_index)
            self._current_index += 1
            return dev

    def next(self):
        return self._get_next()

    def __next__(self):
        return self._get_next()

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    current index = {0}'.format(self._current_index)
        return ret_str


class Session(object):
    '''${config['session_class_description']}'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._item_count = 0
        self._current_item = 0
        self._interpreter = _library_interpreter.LibraryInterpreter('windows-1251')
        # Note that _library_interpreter clears the session handle in its constructor, so that if
        # _open_installed_devices_session fails, the error handler can reference it.
        # And then once _open_installed_devices_session succeeds, we can call this again with the
        # actual session handle.
        ${config['session_handle_parameter_name']}, self._item_count = self._open_installed_devices_session(driver)
        self._interpreter.set_session_handle(${config['session_handle_parameter_name']})
        self._param_list = "driver=" + pp.pformat(driver)

        self.devices = []
        for i in range(self._item_count):
            self.devices.append(_Device(self, i))

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        for i in range(self._item_count):
            ret_str += str(_Device(self, i)) + '\n'
        return ret_str

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        return _DeviceIterable(self, self._item_count)

    def close(self):
        try:
            self._${close_function_name}()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''
% for func_name in sorted(functions):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nimodinst/unit_tests/test_modinst.py sha256=a0715b3738fed5dc867810fcd3c9f4cbef5a7067783cd73769795d82f6063f4c bytes=14928 -->
## FILE: src/nimodinst/unit_tests/test_modinst.py

- repository: `ni/nimi-python`
- source_path: `src/nimodinst/unit_tests/test_modinst.py`
- sha256: `a0715b3738fed5dc867810fcd3c9f4cbef5a7067783cd73769795d82f6063f4c`
- bytes: 14928

````python
import _matchers
import _mock_helper

import nimodinst
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession:
    class PatchedLibrary(nimodinst._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niModInst_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nimodinst._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niModInst_OpenInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_OpenInstalledDevicesSession
        self.disallow_close = self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_CloseInstalledDevicesSession

        self.side_effects_helper['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1

        self.iteration_device_looping = 0
        self.num_int_devices_looping = 3
        self.int_vals_device_looping = [123, 456, 789]
        self.num_string_devices_looping = 4
        self.string_vals_device_looping = ["Life", "liberty", "and", "happiness"]

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViString_looping(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if attribute_value_buffer_size.value == 0:
            # TODO(marcoskirsch): What about the byte for the NULL character? Issue #526
            return (len(self.string_vals_device_looping[self.iteration_device_looping]))
        bytes_to_copy = self.string_vals_device_looping[self.iteration_device_looping].encode('ascii')
        for i in range(0, len(bytes_to_copy)):
            attribute_value[i] = bytes_to_copy[i]
        self.iteration_device_looping += 1
        return 0

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViInt32_looping(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        attribute_value.contents.value = self.int_vals_device_looping[self.iteration_device_looping]
        self.iteration_device_looping += 1
        return 0

    # API Tests

    def test_open_and_close(self):
        session = nimodinst.Session('')
        self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(_matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher(), _matchers.ViInt32PointerMatcher())
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert isinstance(session, nimodinst.Session)
            self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(_matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher(), _matchers.ViInt32PointerMatcher())
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_iterating_for(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        with nimodinst.Session('') as session:
            assert len(session) == 2
            count = 0
            for d in session:
                count += 1
            assert count == len(session)

    def test_iterating_for_empty(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 0
        with nimodinst.Session('') as session:
            assert len(session) == 0
            count = 0
            for d in session:
                count += 1
            assert count == len(session)

    def test_get_extended_error_info(self):
        error_string = 'Error'
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            # Calling the internal function directly, as get_extended_error_info() functions differently than other IVI Dance functions.
            # As a result, it cannot be used directly during error handling.
            result = session._interpreter.get_extended_error_info()
            assert result == error_string

    def test_get_error_description_fails(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = -1
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number
            except nimodinst.Error as e:
                assert e.code == -1  # we want the original error code from getting the attribute.
                assert e.description == "Failed to retrieve error description."

    def test_get_attribute_session(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            attr_int = session.devices[0].chassis_number
            assert attr_int == val

    def test_get_attribute_vi_int32_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session.devices[index].chassis_number
            index += 1
            assert attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session.devices[index].device_name
            index += 1
            assert attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_session_no_index(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            try:
                session.chassis_number
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'chassis_number'"

    def test_get_attribute_vi_int32_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.chassis_number
                assert attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.device_name
                assert attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    # Error Tests
    def test_cannot_add_properties_to_session_set(self):
        with nimodinst.Session('') as session:
            try:
                session.non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_cannot_add_properties_to_session_get(self):
        with nimodinst.Session('') as session:
            try:
                session.non_existent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_cannot_add_properties_to_device_set(self):
        with nimodinst.Session('') as session:
            try:
                session.devices[0].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_cannot_add_properties_to_device_get(self):
        with nimodinst.Session('') as session:
            try:
                session.devices[0].non_existent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'_Device' object has no attribute 'non_existent_property'"

    def test_vi_int32_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_vi_string_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session.devices[0].device_name = "Not Possible"
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_int_attribute_error(self):
        error_code = -1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = error_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number
                assert False
            except nimodinst.Error as e:
                assert e.code == error_code
                assert e.description == error_string

    def test_int_attribute_warning(self):
        warning_code = 1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = warning_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            with warnings.catch_warnings(record=True) as w:
                session.devices[0].chassis_number
                assert len(w) == 1
                assert issubclass(w[0].category, nimodinst.DriverWarning)
                assert error_string in str(w[0].message)

    def test_repr_and_str(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViString
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = 42
        self.side_effects_helper['GetInstalledDeviceAttributeViString']['attributeValue'] = 'fourty two'
        with nimodinst.Session('') as session:
            session
            print(session)
            for d in session:
                d
                print(d)


# not a session test per se
def test_diagnostic_information():
    info = nimodinst.print_diagnostic_information()
    assert isinstance(info, dict)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/examples/nirfsg_arb_waveform.py sha256=7724654f52acafa9d14ff2dd08efdeeba3fc8ee20e285c13c48de53e8b4bc550 bytes=1957 -->
## FILE: src/nirfsg/examples/nirfsg_arb_waveform.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/examples/nirfsg_arb_waveform.py`
- sha256: `7724654f52acafa9d14ff2dd08efdeeba3fc8ee20e285c13c48de53e8b4bc550`
- bytes: 1957

````python
import argparse
import nirfsg
import numpy as np
import sys


def example(resource_name, options, frequency, power_level, number_of_samples):
    waveform_data = np.full(number_of_samples, 1 + 0j, dtype=np.complex128)
    with nirfsg.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as session:
        session.configure_rf(
            frequency,
            power_level
        )
        session.generation_mode = nirfsg.GenerationMode.ARB_WAVEFORM
        session.write_arb_waveform('wfm', waveform_data, False)
        with session.initiate():
            session.check_generation_status()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Continuously generates an arbitrary waveform using NI-RFSG.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal generator.')
    parser.add_argument('-f', '--frequency', default=1e9, type=float, help='Frequency in Hz.')
    parser.add_argument('-p', '--power-level', default=-10.0, type=float, help='Power level in dBm.')
    parser.add_argument('-s', '--number-of-samples', default=1000, type=int, help='Number of samples.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.frequency, args.power_level, args.number_of_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, -10.0, 1000)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--frequency', '1e9', '--power-level', '-10', '--number-of-samples', '1000', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/examples/nirfsg_cw.py sha256=8c8456f2d1dc1c114b0c378af68e914e1b0dccb6b867610826df370b38912fda bytes=1700 -->
## FILE: src/nirfsg/examples/nirfsg_cw.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/examples/nirfsg_cw.py`
- sha256: `8c8456f2d1dc1c114b0c378af68e914e1b0dccb6b867610826df370b38912fda`
- bytes: 1700

````python
import argparse
import nirfsg
import sys


def example(resource_name, options, frequency, power_level):
    with nirfsg.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as session:
        # Configure RF settings
        session.configure_rf(
            frequency,  # Frequency in Hz
            power_level  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start generation
        with session.initiate():
            session.check_generation_status()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generates a continuous wave (CW) signal using NI-RFSG.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal generator.')
    parser.add_argument('-f', '--frequency', default=1e9, type=float, help='Frequency in Hz.')
    parser.add_argument('-p', '--power-level', default=-10.0, type=float, help='Power level in dBm.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.frequency, args.power_level)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, -10.0)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--frequency', '1e9', '--power-level', '-10', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/examples/nirfsg_script.py sha256=acf3315b1219f95da76ac28a0b958005e78035ac6f4ffe71e25a44106a3137f2 bytes=2100 -->
## FILE: src/nirfsg/examples/nirfsg_script.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/examples/nirfsg_script.py`
- sha256: `acf3315b1219f95da76ac28a0b958005e78035ac6f4ffe71e25a44106a3137f2`
- bytes: 2100

````python
import argparse
import nirfsg
import numpy as np
import sys

SAMPLE_SCRIPT = '''
script continuousWaveform
    repeat forever
        generate wfm
    end repeat
end script
'''


def example(resource_name, options, frequency, power_level, number_of_samples):
    waveform_data = np.full(number_of_samples, 1 + 0j, dtype=np.complex64)
    with nirfsg.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as session:
        session.configure_rf(
            frequency,
            power_level
        )
        session.generation_mode = nirfsg.GenerationMode.SCRIPT
        session.write_arb_waveform('wfm', waveform_data, False)
        session.write_script(SAMPLE_SCRIPT)
        with session.initiate():
            session.check_generation_status()


def _main(argsv):
    parser = argparse.ArgumentParser(description='Generates a signal based on the script provided.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of the NI RF signal generator.')
    parser.add_argument('-f', '--frequency', default=1e9, type=float, help='Frequency in Hz.')
    parser.add_argument('-p', '--power-level', default=-10.0, type=float, help='Power level in dBm.')
    parser.add_argument('-s', '--number-of-samples', default=1000, type=int, help='Number of samples.')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string for the session.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.option_string, args.frequency, args.power_level, args.number_of_samples)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5841', }, }
    example('simulated5841', options, 1e9, -10.0, 1000)


def test_main():
    cmd_line = ['--resource-name', 'simulated5841', '--frequency', '1e9', '--power-level', '-10', '--number-of-samples', '1000', '--option-string', 'Simulate=1, DriverSetup=Model:5841']
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/LATEST_RELEASE sha256=6ca2e3356014241331fb2b399428fca23c558e3f3d428edcf4f56eb0fe907069 bytes=7 -->
## FILE: src/nirfsg/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/LATEST_RELEASE`
- sha256: `6ca2e3356014241331fb2b399428fca23c558e3f3d428edcf4f56eb0fe907069`
- bytes: 7

````text
1.1.0
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nirfsg/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/attributes.py sha256=add812733cf92dc4b29f67df11b0474d0a613d2ed53a955386f8200ddf26ee24 bytes=275994 -->
## FILE: src/nirfsg/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/attributes.py`
- sha256: `add812733cf92dc4b29f67df11b0474d0a613d2ed53a955386f8200ddf26ee24`
- bytes: 275994

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 26.3.0d9999
attributes = {
    1050302: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the prefix for NI-RFSG. The name of each user-callable function in NI-RFSG starts with this prefix. This attribute returns\n\nniRFSG.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the resource name NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this attribute contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this attribute contains that value.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the nirfsg_Init function or the nirfsg_InitWithOptions function. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a list of supported devices.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString',
        'type_in_documentation': 'list of str'
    },
    1050401: {
        'access': 'read only',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a list of class-extension groups that NI-RFSG implements.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString',
        'type_in_documentation': 'list of str'
    },
    1050510: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the name of the manufacturer of the NI-RFSG device you are currently using.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the model number or name of the NI-RFSG device that you are currently using. For drivers that support more than one device, this attribute returns a comma-separated list of supported devices.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the name of the vendor that supplies NI-RFSG. This attribute returns\n\nNational Instruments.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains a brief description of NI-RFSG. This attribute returns\n\nNational Instruments RF Signal Generator Instrument Driver.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the major version number of the class specification with which NI-RFSG is compliant.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the minor version number of the class specification with which NI-RFSG is compliant.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return\n\nDriver: NI-RFSG14.5.0, Compiler: MSVC9.00, Components: IVI Engine4.00, VISA-Spec4.00 as the value of this attribute.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock source. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** OnboardClock\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureRefClock\n\n**Possible Values**:',
            'table_body': [
                [
                    '"OnboardClock"',
                    'Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. ** PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.'
                ],
                [
                    '"ClkIn"',
                    'Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.'
                ],
                [
                    '"RefIn"',
                    'Uses the clock signal present at the front panel REF IN connector as the Reference Clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector. **PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector.'
                ],
                [
                    '"PXI_CLK"',
                    'Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.'
                ],
                [
                    '"RefIn2"',
                    'This value is not valid on any supported devices.'
                ],
                [
                    '"PXI_ClkMaster"',
                    'This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653** —NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_CLK as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'enum': 'ReferenceClockSource',
        'lv_property': 'Clock:Reference Clock Source',
        'name': 'REF_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the Start Trigger. This attribute is used when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to digital edge. The NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute is not case-sensitive. To set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, the NI-RFSG device must be in the Configuration state.\n\nPXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeStartTrigger\n\n **Possible Values**:',
            'table_body': [
                [
                    '"PFI0"',
                    'The trigger is received on PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The trigger is received on PFI 1.'
                ],
                [
                    '"PFI2"',
                    'The trigger is received on PFI 2.'
                ],
                [
                    '"PFI3"',
                    'The trigger is received on PFI 3.'
                ],
                [
                    '"PXI_Star"',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXI_Trig7"',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    '"PXIe_DStarB"',
                    'The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    '"TrigIn"',
                    'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ],
                [
                    '"Sync_Script"',
                    'The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150003: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Start Trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nPXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PFI0"',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    '"PFI4"',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    '"PFI5"',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    '"TrigOut"',
                    'The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Triggers:Start:Export Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150005: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this attribute is set to NIRFSG_VAL_ENABLE, NI-RFSG may increase the waveform size. To set the NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED attribute, the NI-RFSG device must be in the Configuration state. NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT.\n\nPXI-5671: When using the PXI-5671 with I/Q rates less than or equal to 8.33MS/s, an input phase-continuous signal is always phase-continuous upon output, and this attribute has no effect.\n\nPXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Phase continuity is *always* enabled on this device.\n\n**Default Value:** NIRFSG_VAL_AUTO\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_\n\n`Arb Waveform Mode Tuning Speed Factors <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_arb_waveform_mode_tuning_speed_factors.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_AUTO',
                    '-1 (-0x1)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase. When the Generation Mode property is set to Script, the Phase Continuity Enabled property indicates a warning condition. NI-RFSG cannot guarantee a phase-continuous output signal in Script mode. Phase continuity is automatically disabled in script mode, and the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform is played back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED Attribute Setting',
                'Value',
                'With I/Q Rates > 8.33 MS/s.'
            ]
        },
        'enum': 'PhaseContinuityEnabled',
        'lv_property': 'Arb:Phase Continuity Enabled',
        'name': 'PHASE_CONTINUITY_ENABLED',
        'type': 'ViInt32'
    },
    1150007: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': "Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× NIRFSG_ATTR_IQ_RATE).\n\nNI-RFSG defines *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* :sub:`max` - *f* :sub:`min` .\n\nThis attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT, except for when using the PXIe-5830/5831/5832/5840/5841, which supports setting this attribute in all supported generation modes. To set the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute, the NI-RFSG device must be in the Configuration state.\n\nPXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to configure the upconverter center frequency in increments of 1MHz or 5MHz. Failure to configure this attribute may result in the signal being placed outside the upconverter passband.\n\nPXIe-5644/5645/5646, PXIe-5673/5673E: This attribute is used only for error-checking purposes. Otherwise, this attribute is ignored.\n\nPXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this attribute is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.\n\n**Units**: hertz (Hz)\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n\n`Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_"
        },
        'lv_property': 'Arb:Signal Bandwidth (Hz)',
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables automatic thermal correction. When this attribute is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjusts the settings as needed. When this attribute is disabled, you must explicitly call the nirfsg_PerformThermalCorrection function to adjust the device for temperature changes.\n\n**Default Value:** NIRFSG_VAL_ENABLE\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_\n\n`Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Automatic thermal correction is disabled.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Automatic thermal correction is enabled.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticThermalCorrection',
        'lv_property': 'RF:Automatic Thermal Correction',
        'name': 'AUTOMATIC_THERMAL_CORRECTION',
        'type': 'ViInt32'
    },
    1150011: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the maximum instantaneous power of the RF output signal.\n\n**Units**: dBm\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': '- This attribute is valid only when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_AVERAGE_POWER.\n\n - The NIRFSG_ATTR_ARB_DIGITAL_GAIN attribute is not included in the calculation of the NIRFSG_ATTR_PEAK_ENVELOPE_POWER attribute.'
        },
        'lv_property': 'RF:Peak Envelope Power (dBm)',
        'name': 'PEAK_ENVELOPE_POWER',
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'When this attribute is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error rates (MER) and error vector magnitude (EVM) for signals with large bandwidths (>500 kHz), but it increases tuning times.\n\nOn the PXI-5670/5671, equalization is performed in the software, so tuning time is increased. On the PXIe-5672, equalization is performed in the hardware so that there is no compromise in performance.\n\nThis attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nPXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_ENABLE is the only supported value for this device.\n\n**Default Value:**\n\nPXI-5670/5671: NIRFSG_VAL_DISABLE\n\nPXIe-5644/5645/5646, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_ENABLE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Response and Software Equalization <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/if_response_and_equalizer.html>`_—Refer to this topic for more information about equalization performed in software.\n\n`Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Filter is not applied'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Filter is applied.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DigitalEqualizationEnabled',
        'lv_property': 'Arb:Digital Equalization Enabled',
        'name': 'DIGITAL_EQUALIZATION_ENABLED',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this attribute is set to VI_FALSE, even if the NIRFSG_ATTR_OUTPUT_ENABLED attribute is set to VI_FALSE, the nirfsg_Abort function is called, or the NI-RFSG session is closed.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViBoolean function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'The local oscillator signal is present at the LO OUT front panel connector.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'The local oscillator signal is not present at the LO OUT front panel connector.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'lv_property': 'RF:LO Out Enabled',
        'name': 'LO_OUT_ENABLED',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViBoolean'
    },
    1150014: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables warnings or errors when you set the frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable the NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS attribute, the driver does not report out-of-specification warnings or errors.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices:** PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'note': 'Accuracy cannot be guaranteed outside of device specifications, and results may vary by module.',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables out-of-specification user settings.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables out-of-specification user settings.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AllowOutOfSpecificationUserSettings',
        'lv_property': 'RF:Allow Out Of Specification User Settings',
        'name': 'ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '**Units**: hertz (Hz)\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate a carrier frequency with a waveform.\nIndicates the carrier frequency generated by the arbitrary waveform generator (AWG) module. The specified carrier frequency is related to the RF output as shown in the following equations:',
            'note': '- Use this attribute to associate a carrier frequency with a waveform.\n\n - This attribute is read-only on the PXI-5670/5671 and PXIe-5672.',
            'table_body': [
                [
                    'PXI-5610, PXI-5670/5671, PXIe-5672',
                    'RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency* – 25 MHz'
                ],
                [
                    'PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860',
                    'RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency*.Note that - the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute and the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute cannot be set at the same time. The only time the carrier frequency is nonzero on these devices is when in-band retuning is used. '
                ]
            ],
            'table_header': [
                'Device',
                'Equations'
            ]
        },
        'lv_property': 'Arb:Arb Carrier Frequency (Hz)',
        'name': 'ARB_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this attribute returns the temperature of the primary NI RF device. The NI-RFSG session is opened using the primary RF device name.\n\nSerial signals between the sensor and the system control unit could modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.\n\nPXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\nPXIe-5830/5831/5832: To use this attribute, you must first set the channelName parameter of the nirfsg_SetAttributeViReal64 function to using the appropriate string for your instrument configuration. Setting the nirfsg_SetAttributeViReal64 function is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.\n\n**Units**: degrees Celsius (°C)\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_\n\n`Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_',
            'table_body': [
                [
                    'PXIe-3621/3622',
                    '—',
                    'if or "" (empty string)'
                ],
                [
                    'PXIe-5820',
                    '—',
                    'fpga'
                ],
                [
                    'First connected mmRH-5582',
                    'DIRECT TRX PORTS Only',
                    'rf0'
                ],
                [
                    'First connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf0switch0'
                ],
                [
                    'First connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf0switch1'
                ],
                [
                    'Second connected mmRH-5582',
                    'DIRECT TRX PORTS Only',
                    'rf1'
                ],
                [
                    'Second connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf1switch0'
                ],
                [
                    'Second connected mmRH-5582',
                    'SWITCHED TRX PORTS [0-7]',
                    'rf1switch1'
                ]
            ],
            'table_header': [
                'Hardware Module',
                'TRX Port Type',
                'Active Channel String'
            ]
        },
        'lv_property': 'Device Characteristics:Device Temperature (Degrees C)',
        'name': 'DEVICE_TEMPERATURE',
        'supported_rep_caps': [
            'device_temperatures'
        ],
        'type': 'ViReal64'
    },
    1150018: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute, or the script specified by the NIRFSG_ATTR_SELECTED_SCRIPT attribute, upon calling the nirfsg_Initiate function.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_CW\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696 (CW support only), PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n\n`Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_—Refer to this topic for more information about scripting.\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ARB_WAVEFORM',
                    '1001 (0x3e9)',
                    'Configures the RF signal generator to generate the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute.'
                ],
                [
                    'NIRFSG_VAL_CW',
                    '1000 (0x3e8)',
                    'Configures the RF signal generator to generate a CW signal.'
                ],
                [
                    'NIRFSG_VAL_SCRIPT',
                    '1002 (0x3ea)',
                    'Configures the RF signal generator to generate arbitrary waveforms as directed by the NIRFSG_ATTR_SELECTED_SCRIPT attribute..'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'GenerationMode',
        'lv_property': 'Arb:Generation Mode',
        'name': 'GENERATION_MODE',
        'type': 'ViInt32'
    },
    1150019: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Script Trigger type. Depending upon the value of this attribute, more attributes may be needed to fully configure the trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_NONE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeScriptTrigger\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE',
                    'No trigger is configured. Signal generation starts immediately.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_EDGE',
                    'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_LEVEL',
                    'The data operation does not start until the digital level is detected. The source of the digital level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, and the active level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute.'
                ],
                [
                    'NIRFSG_VAL_SOFTWARE',
                    'The data operation does not start until a software trigger occurs. You can create a software event by calling the niRFSG_SendSoftwareEdgeTrigger function.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTriggerType',
        'lv_property': 'Triggers:Script:Type',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150020: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to digital edge. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeScriptTrigger\n\n**Possible Values**:',
            'table_body': [
                [
                    '"PFI0"',
                    'The trigger is received on PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The trigger is received on PFI 1.'
                ],
                [
                    '"PFI2"',
                    'The trigger is received on PFI 2.'
                ],
                [
                    '"PFI3"',
                    'The trigger is received on PFI 3.'
                ],
                [
                    '"PXI_Star"',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXI_Trig7"',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    '"PXIe_DStarB"',
                    'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    '"PulseIn"',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ],
                [
                    '"Sync_Script"',
                    'The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Triggers:Script:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150021: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active edge for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to digital edge. To set the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_RISING_EDGE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeScriptTrigger\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_FALLING_EDGE',
                    '1 (0x1)',
                    'Asserts the trigger when the signal transitions from high level to low level.'
                ],
                [
                    'NIRFSG_VAL_RISING_EDGE',
                    '0 (0x0)',
                    'Asserts the trigger when the signal transitions from low level to high level.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Script:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Script Trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_ —Refer to this topic for information about trigger delay.\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PFI0"',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    '"PFI4"',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    '"PFI5"',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Triggers:Script:Export Output Terminal',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150023: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the script in onboard memory to generate upon calling the nirfsg_Initiate function when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_SCRIPT.\n\nThe NIRFSG_ATTR_SELECTED_SCRIPT attribute is ignored when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_CW. To set the NIRFSG_ATTR_SELECTED_SCRIPT attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n\n`Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_'
        },
        'lv_property': 'Arb:Selected Script',
        'name': 'SELECTED_SCRIPT',
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the phase of the RF output signal. Use this attribute to align the phase of the RF output with the phase of the RF output of another device, as long as the two devices are phase-coherent.\n\n**Units**: degrees (°)\n\n**Default Value:** 0\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Phase Synchronization and Phase Coherency <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phase_synchronization_and_phase_coherency.html>`_'
        },
        'lv_property': 'RF:Phase Offset (Degrees)',
        'name': 'PHASE_OFFSET',
        'type': 'ViReal64'
    },
    1150025: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this attribute. PXIe-5860 can only be in the Configuration state to use this attribute.\n\nOn the PXI-5671, this attribute applies only when the NIRFSG_ATTR_IQ_RATE attribute is set to a value less than or equal to 8.33MS/s. On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this attribute is always applicable.\n\n**Units**: dB\n\n**Default Value:** 0dB\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Pre-filter Gain (dB)',
        'name': 'ARB_PRE_FILTER_GAIN',
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this attribute returns the serial number of the primary RF module.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150027: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the loop bandwidth of the tuning PLLs. This attribute is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10MHz. This attribute is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50MHz.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Default Value:**\n\nPXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: NIRFSG_VAL_MEDIUM\n\nPXI/PXIe-5650/5651/5652, PXIe-5673/5673E: NIRFSG_VAL_NARROW\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n\n`Modulation Implementation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5650_5651_5652_modulation_implementation.html>`_\n\n`Sinusoidal Tone Versus Modulation Operation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sinusoidal_tone_versus_modulation_implementation.html>`_\n\n**Defined Values**:',
            'note': 'Setting this attribute to NIRFSG_VAL_WIDE on the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, or the PXIe-5673/5673E allows the frequency to settle significantly faster at the expense of increased phase noise. Setting this attribute to NIRFSG_VAL_MEDIUM is not a valid option on the PXI/PXIe-5650/5651/5652 or PXIe-5673/5673E. NIRFSG_VAL_MEDIUM is the only supported value for the PXIe-5840/5841/5842.',
            'table_body': [
                [
                    'NIRFSG_VAL_MEDIUM',
                    '1 (0x1)',
                    'Uses the medium loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_NARROW',
                    '0 (0x0)',
                    'Uses the narrowest loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_WIDE',
                    '2 (0x2)',
                    'Uses the widest loop bandwidth setting for the PLL.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoopBandwidth',
        'lv_property': 'RF:Loop Bandwidth',
        'name': 'LOOP_BANDWIDTH',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViInt32'
    },
    1150029: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Sample Clock mode on the device. To set this attribute, the device must be in the Configuration state.\n\nPXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_DIVIDE_DOWN is the only supported value for this device.\n\n**Default Values:**\n\nPXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_DIVIDE_DOWN\n\nPXIe-5673/5673E: NIRFSG_VAL_HIGH_RESOLUTION\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Clocking Modes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/clocking.html>`_\n\n**Valid Values**:',
            'note': 'Using the high resolution clock may result in increased phase noise.',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_RESOLUTION',
                    'Sample rates are generated by a high-resolution clock.'
                ],
                [
                    'NIRFSG_VAL_DIVIDE_DOWN',
                    'Sample rates are generated by dividing the source frequency.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'ArbOnboardSampleClockMode',
        'lv_property': 'Clock:Arb Onboard Sample Clock Mode',
        'name': 'ARB_ONBOARD_SAMPLE_CLOCK_MODE',
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Sample Clock source for the device. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nPXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: OnboardClock is the only supported value for this device.\n\n**Default Value:** OnboardClock\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '"ClkIn"',
                    'Uses the external clock as the Sample Clock source.'
                ],
                [
                    '"OnboardClock"',
                    'Uses the AWG module onboard clock as the Sample Clock source.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'enum': 'ArbSampleClockSource',
        'lv_property': 'Clock:Arb Sample Clock Source',
        'name': 'ARB_SAMPLE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150031: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the rate of the Sample Clock on the device.\n\n**Units**: hertz (Hz)\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Clock:Arb Sample Clock Rate (Hz)',
        'name': 'ARB_SAMPLE_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the analog modulation format to use.\n\n**Default Value:** NIRFSG_VAL_NONE\n\n**Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation.html>`_\n\n`PXI/PXIe-5650/5651/5652 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_\n\n`PXIe-5654/5654 with PXIe-5696 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_modulation_modes.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_AM',
                    '2002 (0x7d2)',
                    'Specifies that the analog modulation type is AM.'
                ],
                [
                    'NIRFSG_VAL_FM',
                    '2000 (0x7d0)',
                    'Specifies that the analog modulation type is FM.'
                ],
                [
                    'NIRFSG_VAL_NONE',
                    '0 (0x0)',
                    'Disables analog modulation.'
                ],
                [
                    'NIRFSG_VAL_PM',
                    '2001 (0x7d1)',
                    'Specifies that the analog modulation type is PM.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnalogModulationType',
        'lv_property': 'Modulation:Analog:Modulation Type',
        'name': 'ANALOG_MODULATION_TYPE',
        'type': 'ViInt32'
    },
    1150042: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the nirfsg_WriteArbWaveform function immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this attribute when an arbitrary waveform is first allocated.\n\nFor the PXI-5670, direct download is always disabled. For all other devices, direct download is always enabled.\n\nPXI-5671: To increase performance when using large waveforms, enable direct download. To maximize reconfigurability, disable direct download.\n\nPerform the following steps to enable direct download:\n\n1. Set the I/Q rate to less than or equal to 8.33MS/s with the NIRFSG_ATTR_IQ_RATE attribute.\n\n2. Set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\n3. Disable the NIRFSG_ATTR_IQ_SWAP_ENABLED attribute.\n\n4. Disable the NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED attribute.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_UNSPECIFIED',
                    '-2 (-0x2)',
                    'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DirectDownload',
        'lv_property': 'Arb:Data Transfer:Direct Download',
        'name': 'DIRECT_DOWNLOAD',
        'type': 'ViInt32'
    },
    1150043: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies how NI-RFSG interprets the value of the NIRFSG_ATTR_POWER_LEVEL attribute. The NIRFSG_ATTR_POWER_LEVEL_TYPE attribute also affects how waveforms are scaled.\n\nPXI-5670/5671: While in Script generation mode, if this attribute is set to NIRFSG_VAL_AVERAGE_POWER, NI-RFSG scales each waveform so that all waveforms have the same average power. The average power level of each waveform matches the value set with the NIRFSG_ATTR_POWER_LEVEL attribute. You can disable this scaling operation by setting the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\nPXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: While in Script generation mode, this attribute must be set to NIRFSG_VAL_PEAK_POWER.\n\nConverting from Average Power to Peak Power\n\nTypically, this attribute is set to NIRFSG_VAL_AVERAGE_POWER. However, some instrument modes require this attribute to be set to NIRFSG_VAL_PEAK_POWER. Use the following equations to calculate the equivalent peak power given the desired average power for your waveform:\n\nWhere 1 is the highest possible magnitude in the waveform.\n\n**Default Value:**\n\nPXIe-5820: NIRFSG_VAL_PEAK_POWER\n\nAll other devices: NIRFSG_VAL_AVERAGE_POWER\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_\n\n`Optimizing for Low Power Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/optimizing_for_low_power_generation.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_AVERAGE_POWER',
                    'Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.'
                ],
                [
                    'NIRFSG_VAL_PEAK_POWER',
                    'Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR attribute. You can use the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute in conjunction with the NIRFSG_ATTR_POWER_LEVEL attribute when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'PowerLevelType',
        'lv_property': 'RF:Power Level Type',
        'name': 'POWER_LEVEL_TYPE',
        'type': 'ViInt32'
    },
    1150045: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables and disables continuous streaming of waveform data.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'Streaming is enabled.'
                ],
                [
                    'VI_FALSE',
                    'Streaming is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Enabled',
        'name': 'STREAMING_ENABLED',
        'type': 'ViBoolean'
    },
    1150046: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the name of the waveform used to continually stream data during generation.\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n`Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_'
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Waveform Name',
        'name': 'STREAMING_WAVEFORM_NAME',
        'type': 'ViString'
    },
    1150047: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.\n\nTo read this attribute, the NI-RFSG device must be in the Committed state.\n\n**Units**: samples\n\n**Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_'
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'type': 'ViInt64'
    },
    1150052: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies how much to scale the data before writing it with the nirfsg_WriteArbWaveform function. The resulting waveform must be smaller than 1.0 in complex magnitude. This attribute is supported only if you set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n\n**Default Value:** 1.0\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_'
        },
        'lv_property': 'Arb:Software Scaling Factor',
        'name': 'ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR',
        'type': 'ViReal64'
    },
    1150053: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Possible Values**:\n\nPossible Value: Description\n\n"" :The Reference Clock signal is not exported.\n\n"RefOut" :Exports the Reference Clock signal to the REF OUT connector of the device.\n\n"RefOut2" :Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.\n\n"ClkOut" :Exports the Reference Clock signal to the CLK OUT connector of the device.\n\n**Default Value:** \'""\'\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Interconnecting Multiple NI 5673E Modules <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/interconnecting_multiple_ni_5673_modules.html>`_',
            'note': 'The RefOut2 output terminal value is valid for only the PXIe-5650/5651/5652, not the PXI-5650/5651/5652.',
            'table_body': [
                [
                    '"ClkOut"',
                    'Exports the Reference Clock signal to the CLK OUT connector of the device.',
                    'Supported on PXIe-5673, 5673E'
                ],
                [
                    '""',
                    'The Reference Clock signal is not exported.',
                    'Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5652, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5652 (See Note)'
                ],
                [
                    '"RefOut"',
                    'Exports the Reference Clock signal to the REF OUT connector of the device.',
                    'Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5653, 5653, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5653, '
                ],
                [
                    '"RefOut2"',
                    'Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.',
                    'Supported on PXIe-5650/5651/5652, 5654, 5673E, PXIe-5654 with PXIe-5696'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description',
                'Supported devices'
            ]
        },
        'enum': 'ReferenceClockExportOutputTerminal',
        'lv_property': 'Clock:Reference Clock Export Output Terminal',
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150054: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source terminal for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to NIRFSG_VAL_DIGITAL_LEVEL. The NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute is not case-sensitive.\n\nTo set the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '"PFI0"',
                    'The trigger is received on PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The trigger is received on PFI 1.'
                ],
                [
                    '"PFI2"',
                    'The trigger is received on PFI 2.'
                ],
                [
                    '"PFI3"',
                    'The trigger is received on PFI 3.'
                ],
                [
                    '"PXI_Star"',
                    'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXI_Trig7"',
                    'The trigger is received on PXI trigger line 7.'
                ],
                [
                    '"PXIe_DStarB"',
                    'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    '"PulseIn"',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Triggers:Script:Digital Level:Source',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active level for the Script Trigger. This attribute is used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to NIRFSG_VAL_DIGITAL_LEVEL.\n\n**Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'lv_property': 'Triggers:Script:Digital Level:Active Level',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViInt32'
    },
    1150061: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'The total amount of memory on the signal generator in bytes.\n\n**Units:** bytes\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Memory Options <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/memory_options.html>`_\n\n`Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_',
            'note': 'Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.'
        },
        'lv_property': 'Arb:Memory Size',
        'name': 'MEMORY_SIZE',
        'type': 'ViInt64'
    },
    1150062: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the `deviation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/glossary.html>`_ to use in phase modulation, in degrees.\n\n**Units**: degrees (°)\n\n**Default Value:** 90°\n\n**Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653\n\n**Related Topics**\n\n`Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_'
        },
        'lv_property': 'Modulation:Analog:PM Deviation (Degrees)',
        'name': 'ANALOG_MODULATION_PM_DEVIATION',
        'type': 'ViReal64'
    },
    1150063: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Done event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PFI0"',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    '"PFI4"',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    '"PFI5"',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Posible Value',
                'Description'
            ]
        },
        'lv_property': 'Events:Done Event Export Output Terminal',
        'name': 'EXPORTED_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150064: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Marker Event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PFI0"',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    '"PFI4"',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    '"PFI5"',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Events:Marker:Output Terminal',
        'name': 'EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViString'
    },
    1150065: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Started event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PFI0"',
                    'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                ],
                [
                    '"PFI1"',
                    'The signal is exported to the PFI 1 connector.'
                ],
                [
                    '"PFI4"',
                    'The signal is exported to the PFI 4 connector.'
                ],
                [
                    '"PFI5"',
                    'The signal is exported to the PFI 5 connector.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                ],
                [
                    '"DIO/PFI0"',
                    'The trigger is received on PFI0 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI1"',
                    'The trigger is received on PFI1 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI2"',
                    'The trigger is received on PFI2 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI3"',
                    'The trigger is received on PFI3 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI4"',
                    'The trigger is received on PFI4 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI5"',
                    'The trigger is received on PFI5 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI6"',
                    'The trigger is received on PFI6 from the front panel DIO terminal.'
                ],
                [
                    '"DIO/PFI7"',
                    'The trigger is received on PFI7 from the front panel DIO terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Events:Started Event Export Output Terminal',
        'name': 'EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150066: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the power level of the signal at the LO OUT front panel connector.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Units**: dBm\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_',
            'note': 'For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this attribute is always read-only.'
        },
        'lv_property': 'RF:LO Out Power (dBm)',
        'name': 'LO_OUT_POWER',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViReal64'
    },
    1150067: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the power level of the signal at the LO IN front panel connector.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Units**: dBm\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_',
            'note': '- This attribute is read/write if you are using an external LO. Otherwise, this attribute is read-only.\n\n - For the PXIe-5644/5645/5646, this attribute is always read-only.'
        },
        'lv_property': 'RF:LO In Power (dBm)',
        'name': 'LO_IN_POWER',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViReal64'
    },
    1150068: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the AWG module temperature in degrees Celsius.\n\nPXIe-5820/5840/5841/5842: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n**Units**: degrees Celsius (°C)\n\n**Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:AWG Temperature (Degrees C)',
        'name': 'ARB_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables I/Q impairment. The NIRFSG_ATTR_IQ_I_OFFSET, NIRFSG_ATTR_IQ_Q_OFFSET, NIRFSG_ATTR_IQ_GAIN_IMBALANCE, and NIRFSG_ATTR_IQ_SKEW attributes are ignored when the NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED attribute is disabled.\n\n**Default Value:** VI_TRUE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'I/Q impairment is enabled.'
                ],
                [
                    'VI_FALSE',
                    'I/Q impairment is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'IQ Impairment:Enabled',
        'name': 'IQ_IMPAIRMENT_ENABLED',
        'type': 'ViBoolean'
    },
    1150070: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'When using a National Instruments AWG module or vector signal transceiver (VST), this attribute specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute setting.\n\nPXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this attribute. When using an external AWG (non–National Instruments AWG), this attribute is read-only and indicates the I/Q modulator I-offset. Units are volts, as specified by the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute.\n\n**Valid Values:**-100 to 100% or -0.2V to 0.2V\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_'
        },
        'lv_property': 'IQ Impairment:I Offset',
        'name': 'IQ_I_OFFSET',
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'When using a National Instruments AWG module or VST device, this attribute specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute setting.\nPXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this attribute. When using an external AWG (non–National Instruments AWG), the NIRFSG_ATTR_IQ_Q_OFFSET attribute is read-only and indicates the I/Q modulator Q-offset. Units are volts, as indicated by the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute.\n**Valid Values**: -100% to 100% or -0.2V to 0.2V\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n**Related Topics**\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_'
        },
        'lv_property': 'IQ Impairment:Q Offset',
        'name': 'IQ_Q_OFFSET',
        'type': 'ViReal64'
    },
    1150072: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the gain imbalance of the I/Q modulator (I versus Q).\n\nGain imbalance is calculated with the following equation:\n\n**Units**: dB\n\n**Valid Values:**-6dB to 6dB\n\n**Default Value:** 0dB\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_\n\n`Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_'
        },
        'lv_property': 'IQ Impairment:Gain Imbalance (dB)',
        'name': 'IQ_GAIN_IMBALANCE',
        'type': 'ViReal64'
    },
    1150073: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the adjustment of the phase angle between the I and Q vectors. If the skew is zero, the phase angle is 90 degrees.\n\nThis attribute is ignored when the NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED attribute is disabled.\n\n**Units**: degrees (°)\n\n**Valid Values:**-30° to 30°\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_'
        },
        'lv_property': 'IQ Impairment:IQ Skew (Degrees)',
        'name': 'IQ_SKEW',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the LO module temperature in degrees Celsius.\n\nPXIe-5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution.\n\n**Units**: degrees Celsius (°C)\n\n**Supported Devices:** PXIe-5673/5673E, PXIe-5840/5841/5842'
        },
        'lv_property': 'Device Characteristics:LO Temperature (Degrees C)',
        'name': 'LO_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150076: {
        'access': 'read only',
        'attribute_class': 'AttributeViInt32TimeDeltaMonths',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the recommended interval between each external calibration of the device.\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'External Calibration:Recommended Interval',
        'name': 'EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL',
        'type': 'ViInt32',
        'type_in_documentation': 'hightime.timedelta'
    },
    1150077: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature of the device at the time of the last external calibration.\n\n**Units**: degrees Celsius (°C)\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E'
        },
        'lv_property': 'External Calibration:Last External Calibration Temperature',
        'name': 'EXTERNAL_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150081: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the units of the NIRFSG_ATTR_IQ_I_OFFSET attribute and NIRFSG_ATTR_IQ_Q_OFFSET attribute. Offset units are either percent or volts.\n\nThe AWG or VST offset is the specified percentage of the AWG or VST peak power level when the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT. Given perfect carrier leakage suppression, the following equation is satisfied\n\n\nor equivalently\n\nIf the NIRFSG_ATTR_IQ_I_OFFSET attribute is set to 100%, NIRFSG_ATTR_IQ_Q_OFFSET attribute is set to 0%, and NIRFSG_ATTR_POWER_LEVEL attribute set to 0 dBm, the desired RF signal is at 0 dBm and the carrier leakage is also at 0 dBm.\n\nThe AWG or VST peak power level changes when settings change in other attributes such as the NIRFSG_ATTR_POWER_LEVEL, NIRFSG_ATTR_FREQUENCY, NIRFSG_ATTR_IQ_SKEW, NIRFSG_ATTR_IQ_GAIN_IMBALANCE and NIRFSG_ATTR_ARB_PRE_FILTER_GAIN attributes. When the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT, the actual AWG or VST offset changes as the AWG or VST peak power level changes to satisfy the preceding equations. These changes are useful if you are intentionally adding carrier leakage to test the tolerance of a receiver. When the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_PERCENT, the carrier leakage, in dBc, remains at a consistent level.\n\nIf you are trying to eliminate residual carrier leakage due to calibration inaccuracies or drift, set the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute to NIRFSG_VAL_VOLTS. Offset correction voltage is applied to the I/Q modulator or VST, regardless of changes to the AWG or VST peak power level.\n\n**Default Value**: NIRFSG_VAL_PERCENT\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Defined Values**:',
            'note': 'For any devices except PXIe-5820, if the NIRFSG_ATTR_IQ_OFFSET_UNITS attribute is set to NIRFSG_VAL_VOLTS, a 0.1 I offset results in a 0.1 V offset in the output. For PXIe-5820 devices, 0.1 I offset results in a 10% offset in the output.',
            'table_body': [
                [
                    'NIRFSG_VAL_PERCENT',
                    'Specifies the NIRFSG_ATTR_IQ_I_OFFSET and NIRFSG_ATTR_IQ_Q_OFFSET attribute units as percent.'
                ],
                [
                    'NIRFSG_VAL_VOLTS',
                    'Specifies the NIRFSG_ATTR_IQ_I_OFFSET and NIRFSG_ATTR_IQ_Q_OFFSET attribute units as volts.'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'OffsetUnits',
        'lv_property': 'IQ Impairment:Offset Units',
        'name': 'IQ_OFFSET_UNITS',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the interpretation of the value passed to the NIRFSG_ATTR_FREQUENCY_SETTLING attribute.\n\nPXIe-5650/5651/5652/5653, PXIe-5673E: When the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set to a valid list name, the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO as a valid value.\n\nPXIe-5654/5654 with PXIe-5696: The NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO and NIRFSG_VAL_PPM as valid values.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Default Value**: NIRFSG_VAL_PPM\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n**Defined Values**:',
            'note': 'If you set this attribute to NIRFSG_VAL_TIME_AFTER_IO, the definition of settled for the Configuration Settled event changes.',
            'table_body': [
                [
                    'NIRFSG_VAL_TIME_AFTER_LOCK',
                    'Specifies the time to wait after the frequency PLL locks.'
                ],
                [
                    'NIRFSG_VAL_TIME_AFTER_IO',
                    'Specifies the time to wait after all writes occur to change the frequency.'
                ],
                [
                    'NIRFSG_VAL_PPM',
                    'Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6).'
                ]
            ],
            'table_header': [
                'Name',
                'Description'
            ]
        },
        'enum': 'FrequencySettlingUnits',
        'lv_property': 'RF:Frequency Settling Units',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'ViInt32'
    },
    1150083: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency settling time. Interpretation of this value depends on the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute.\n\n**Valid Values:**\n\nThe valid values for this attribute depend on the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute.\n\n\n\n**Default Value**: 1.0\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_'
        },
        'lv_property': 'RF:Frequency Settling',
        'name': 'FREQUENCY_SETTLING',
        'type': 'ViReal64'
    },
    1150084: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this attribute returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF device name.\n\n**Supported Devices:** PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/identifying_device_revision.html>`_'
        },
        'lv_property': 'Device Characteristics:Module Revision',
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150085: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.\n\nPositive values for this attribute represent amplification, and negative values for this attribute represent attenuation.\n\n**Valid Values:** -INF dB to +INF dB\n\n**Default Value:** 0dB\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': '- Setting this attribute adjusts the actual device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:External Gain (dB)',
        'name': 'EXTERNAL_GAIN',
        'type': 'ViReal64'
    },
    1150100: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the time before the timer emits an event after the task is started and specifies the time interval between Timer events after the first event.\n\n**Units**: seconds (s)\n\n**Default Value:** 0\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_',
            'note': 'For the PXIe-5820/5840/5841/5842/5860, this attribute must be set for the timer to start. If you do not set this attribute, the timer is disabled.'
        },
        'lv_property': 'Events:Timer:Interval',
        'name': 'TIMER_EVENT_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150104: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this attribute, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this attribute, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this attribute.\n\nPXIe-5820/5830/5831/5832/5840/5841/5842/5860: This attribute is read only.\n\n**Units**: Degrees Celsius\n\n**Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': '- Resetting this attribute reverts back to the default unset behavior.\n\n - Use this attribute only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, it is best to ensure that the temperature does not vary too much.'
        },
        'lv_property': 'RF:Advanced:Correction Temperature',
        'name': 'CORRECTION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150112: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Default Values**:\n\nPXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartedEvent, where *AWGName* is the name of your associated AWG module in MAX.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartedEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\nPXIe-5820/5840/5841: /*ModuleName*/ao/0/StartedEvent, where *ModuleName* is the name of your device in MAX.\n\nPXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartedEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_GetTerminalName'
        },
        'lv_property': 'Events:Started Event Terminal Name',
        'name': 'STARTED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150113: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Default Values**:\n\nPXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/DoneEvent, where *AWGName* is the name of your associated AWG module in MAX.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/DoneEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\nPXIe-5820/5840/5841: /*ModuleName*/ao/0/DoneEvent, where *ModuleName* is the name of your device in MAX.\n\nPXIe-5860: /*ModuleName*/ao/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_GetTerminalName'
        },
        'lv_property': 'Events:Done Event Terminal Name',
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150114: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Default Values**:\n\nPXIe-5654/5654 with PXIe-5696: /*ModuleName*/StartTrigger, where *ModuleName* is the name of your device in MAX.\n\nPXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartTrigger, where *ModuleName* is the name of your associated AWG module in MAX.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartTrigger, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\nPXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/StartTrigger, where *ModuleName* is the name of your device in MAX.\n\nPXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_GetTerminalName'
        },
        'lv_property': 'Triggers:Start:Terminal Name',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150115: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Default Values**:\n\nPXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/Marker *X* Event, where *AWGName* is the name of your associated AWG module in MAX and *X* is Marker Event 0 through 3.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/Marker *X* Event, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Marker Event 0 through 3.\n\nPXIe-5820/5840/5841: /*ModuleName*/ao/0/Marker *X* Event, where *ModuleName* is the name of your device in MAX and *X* is Marker Event 0 through 3.\n\n**Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_GetTerminalName'
        },
        'lv_property': 'Events:Marker:Terminal Name',
        'name': 'MARKER_EVENT_TERMINAL_NAME',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViString'
    },
    1150116: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Default Values**:\n\nPXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/ScriptTrigger *X*, where *AWGName* is the name of your associated AWG module in MAX and *X* is Script Trigger 0 through 3.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/ScriptTrigger *X*, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Script Trigger 0 through 3.\n\nPXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX and *X* is Script Trigger 0 through 3.\n\nPXIe-5860: /*ModuleName*/ao/*ChannelNumber*/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX, *ChannelNumber* is the channel number (0 or 1), and *X* is Script Trigger 0 through 3.\n\n**Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_GetTerminalName'
        },
        'lv_property': 'Triggers:Script:Terminal Name',
        'name': 'SCRIPT_TRIGGER_TERMINAL_NAME',
        'supported_rep_caps': [
            'script_triggers'
        ],
        'type': 'ViString'
    },
    1150118: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Adjusts the dynamics of the current driving the YIG main coil.\n\n**Default Value:** NIRFSG_VAL_MANUAL\n\n**Supported Devices:** PXIe-5653\n\n**Defined Values**:',
            'note': 'Setting this attribute to NIRFSG_VAL_FAST on the PXIe-5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.',
            'table_body': [
                [
                    'NIRFSG_VAL_SLOW',
                    'Adjusts the YIG main coil for an underdamped response.'
                ],
                [
                    'NIRFSG_VAL_FAST',
                    'Adjusts the YIG main coil for an overdamped response.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'YigMainCoilDrive',
        'lv_property': 'RF:Advanced:YIG Main Coil Drive',
        'name': 'YIG_MAIN_COIL_DRIVE',
        'type': 'ViInt32'
    },
    1150129: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Configuration Settled event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_\n\n`PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'The signal is not exported.'
                ],
                [
                    '"PXI_Trig0"',
                    'The trigger is received on PXI trigger line 0.'
                ],
                [
                    '"PXI_Trig1"',
                    'The trigger is received on PXI trigger line 1.'
                ],
                [
                    '"PXI_Trig2"',
                    'The trigger is received on PXI trigger line 2.'
                ],
                [
                    '"PXI_Trig3"',
                    'The trigger is received on PXI trigger line 3.'
                ],
                [
                    '"PXI_Trig4"',
                    'The trigger is received on PXI trigger line 4.'
                ],
                [
                    '"PXI_Trig5"',
                    'The trigger is received on PXI trigger line 5.'
                ],
                [
                    '"PXI_Trig6"',
                    'The trigger is received on PXI trigger line 6.'
                ],
                [
                    '"PXIe_DStarC"',
                    'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                ],
                [
                    '"TrigOut"',
                    'TRIG IN/OUT terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'lv_property': 'Events:Configuration Settled Event Export Output Terminal',
        'name': 'EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150132: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the adjustment for the NIRFSG_ATTR_POWER_LEVEL attribute. This attribute is valid only when you set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER. The value of the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute adds to the NIRFSG_ATTR_POWER_LEVEL attribute. The NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate a peak power adjustment with a waveform.',
            'note': '- For the PXIe-5673/5673E only, use this attribute to associate a peak power adjustment with a waveform.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Peak Power Adjustment (dB)',
        'name': 'PEAK_POWER_ADJUSTMENT',
        'type': 'ViReal64'
    },
    1150133: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the loop bandwidth of the reference PLL.\n\n**Default Value:** NIRFSG_VAL_NARROW\n\n**Supported Devices:** PXIe-5653\n\n**Related Topics**\n\n`Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_NARROW',
                    'Uses the narrowest loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_MEDIUM',
                    'Uses the medium loop bandwidth setting for the PLL.'
                ],
                [
                    'NIRFSG_VAL_WIDE',
                    'Uses the widest loop bandwidth setting for the PLL.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'ReferencePllBandwidth',
        'lv_property': 'RF:Advanced:Ref PLL Bandwidth',
        'name': 'REF_PLL_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150136: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Self Calibration:Last Self Calibration Temperature',
        'name': 'SELF_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150137: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the nirfsg_Initiate function or nirfsg_WaitUntilSettled function or prior to advancing to next step if using RF list mode.\n\nAny specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.\n\nPXI/PXIe-5650/5651/5652: This attribute is for NI internal use only.\n\n**Units**: dB\n\n**Default Value:**\n\nPXIe-5654: 4\n\nPXIe-5654 with PXIe-5696 (ALC disabled): 4\n\nPXIe-5654 with PXIe-5696 (ALC enabled): 0.2\n\nPXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5\n\n**Valid Values:**\n\nPXIe-5654: 1.5, 2, 4\n\nPXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4\n\nPXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5\n\nPXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Amplitude Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_amplitude_settling_times.html>`_'
        },
        'lv_property': 'RF:Amplitude Settling',
        'name': 'AMPLITUDE_SETTLING',
        'type': 'ViReal64'
    },
    1150140: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates the maximum amount of time allowed to complete a streaming write operation.\n\n**Default Value:** 10.0seconds\n\n**Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n`Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_'
        },
        'lv_property': 'Arb:Data Transfer:Streaming:Streaming Write Timeout',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150142: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master device when synchronizing the Script Trigger.\n\nThe master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.\n\nWhen synchronizing the Script trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute to digital edge, and set the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute to sync_script.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_\n\nRefer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Script Trigger.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Script Trigger.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master',
        'name': 'SYNC_SCRIPT_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150143: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the synchronized Script Trigger signal. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646\n\n**Related Topics**\n\n`Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_\n\n`Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_\n\nRefer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line',
        'name': 'SYNC_SCRIPT_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150144: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the connector(s) to use to generate the signal. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nYou must write complex I and Q data for all options. The Q data has no effect if you set this attribute to I Only and set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY attribute to 0. If you set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY attribute to a value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex value and outputs the real portion of the result on the I connector(s) of the device.\n\nIf you set the NIRFSG_ATTR_OUTPUT_PORT attribute to NIRFSG_VAL_I_ONLY or NIRFSG_VAL_IQ_OUT, the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute applies.\n\n**Default Value:**\n\nPXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860: NIRFSG_VAL_RF_OUT\n\nPXIe-5820: NIRFSG_VAL_IQ_OUT\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_CAL_OUT',
                    '14002 (0x36b2)',
                    'Enables the CAL OUT port.'
                ],
                [
                    'NIRFSG_VAL_I_ONLY',
                    '14003 (0x36b3)',
                    'Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645.'
                ],
                [
                    'NIRFSG_VAL_IQ_OUT',
                    '14001 (0x36b1)',
                    'Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.'
                ],
                [
                    'NIRFSG_VAL_RF_OUT',
                    '14000 (0x36b0)',
                    'Enables the RF OUT port. This value is not valid for the PXIe-5820.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'OutputPort',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Output Port',
        'name': 'OUTPUT_PORT',
        'type': 'ViInt32'
    },
    1150145: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Units:** hertz (Hz)\n\n**Valid Values:**\n\nPXIe-5645: -60MHz to 60MHz\n\nPXIe-5820: -500MHz to 500MHz\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': '- For the PXIe-5820, NI recommends using the NIRFSG_ATTR_FREQUENCY attribute.\n\n - For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Carrier Frequency',
        'name': 'IQ_OUT_PORT_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150146: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to use the I/Q OUT port for differential configuration or single-ended configuration. If you set this attribute to NIRFSG_VAL_SINGLE_ENDED, you must terminate the negative I and Q output connectors with a 50 Ohm termination.\n\nIf you set this attribute to NIRFSG_VAL_SINGLE_ENDED, the positive I and Q connectors generate the resulting waveform. If you set this attribute to NIRFSG_VAL_DIFFERENTIAL, both the positive and negative I and Q connectors generate the resulting waveform.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_DIFFERENTIAL\n\nPXIe-5820: The only valid value for this attribute is NIRFSG_VAL_DIFFERENTIAL.\n\n**Supported Devices:** PXIe-5645, PXIe-5820\n\n**Related Topics**\n\n`Differential and Single-Ended Operation (I/O Interface) <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/differential_single_ended_operation.html>`_\n\n**Defined Values**:',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.',
            'table_body': [
                [
                    'NIRFSG_VAL_DIFFERENTIAL',
                    '15000 (0x3a98)',
                    'Sets the terminal configuration to differential.'
                ],
                [
                    'NIRFSG_VAL_SINGLE_ENDED',
                    '15001 (0x3a99)',
                    'Sets the terminal configuration to single-ended.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'IQOutPortTerminalConfiguration',
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration',
        'name': 'IQ_OUT_PORT_TERMINAL_CONFIGURATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150147: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the amplitude of the generated signal in volts, peak-to-peak (V). For example, if you set this attribute to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\nRefer to the specifications document for your device for allowable output levels.\n\n**Units:** Volts, peak-to-peak (V :sub:`pk-pk` )\n\n**Valid Values:**\n\nPXIe-5645: 1V :sub:`pk-pk`  maximum if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL, and 0.5V :sub:`pk-pk` \n\nmaximum if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_SINGLE_ENDED.\n\nPXIe-5820: 3.4V :sub:`pk-pk` maximum for signal bandwidth less than 160MHz, and 2V :sub:`pk-pk` \n\nmaximum for signal bandwidth greater than 160MHz.\n\n**Default Value:** 0.5volts\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': '- For the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n - The valid values are only applicable when you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 50 Ω and when you set the NIRFSG_ATTR_IQ_OUT_PORT_OFFSET attribute to 0.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Level',
        'name': 'IQ_OUT_PORT_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150148: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the common-mode offset applied to the signals generated at each differential output terminal. This attribute applies only when you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL. Common-mode offset shifts both positive and negative terminals in the same direction.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Units:** Volts\n\n**Valid Values:**\n\nPXIe-5645: -0.8V to 0.8V if you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 50 Ω. The valid values are -1.2V to 1.2V if you set the NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE attribute to 100 Ω.\n\nPXIe-5820: -0.25V to 1.5V\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': '- For the PXIe-5645, this attribute is ignored if you are using the RF ports.\n\n - The valid range is dependent on the load impedance.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Common Mode Offset',
        'name': 'IQ_OUT_PORT_COMMON_MODE_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150149: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the value, in volts, that the signal generator adds to the arbitrary waveform data. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\nPXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.\n\nPXIe-5820: The waveform is not automatically scaled in DSP. To prevent DSP overflows, use the NIRFSG_ATTR_ARB_PRE_FILTER_GAIN attribute to scale the waveform to provide additional headroom for offsets.\n\n**Units:** Volts\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Offset',
        'name': 'IQ_OUT_PORT_OFFSET',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150150: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to use the internal or external local oscillator (LO) source. If the NIRFSG_ATTR_LO_SOURCE attribute is set to "" (empty string), NI-RFSG uses the internal LO source. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViString function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Default Value:** Onboard\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_\n\n`PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_\n\n**Possible Values**:',
            'note': 'For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to SG_SA_Shared.',
            'table_body': [
                [
                    '"Automatic_SG_SA_Shared"',
                    'NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.'
                ],
                [
                    '"LO_In"',
                    'Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to specify the LO frequency.'
                ],
                [
                    '"Onboard"',
                    'Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.'
                ],
                [
                    '"SG_SA_Shared"',
                    'Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842.'
                ],
                [
                    '"Secondary"',
                    'Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'enum': 'LoSource',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Source',
        'name': 'LO_SOURCE',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViString'
    },
    1150151: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).\n\nWhen the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is enabled, the specified step size affects the fractional spur performance of the device. When the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is disabled, the specified step size affects the phase noise performance of the device.\n\nThe valid values for this attribute depend on the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute.\n\n**PXIe-5644/5645/5646**—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is coerced to the nearest valid value.\n\n**PXIe-5840/5841**—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.\n\n**Units:** hertz (Hz)\n\n**Default Values:**\n\nPXIe-5644/5645/5646: 200kHz\n\nPXIe-5830: 2MHz\n\nPXIe-5831/5832 (RF port): 8MHz\n\nPXIe-5831/5832 (IF port): 2MHz, 4MHz\n\nPXIe-5840/5841:\n\n- Fractional mode: 500 kHz\n- Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.\n\nPXIe-5841 with PXIe-5655: 500kHz\n\nPXIe-5842: 1Hz\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842',
            'note': 'Values up to 100 MHz are coerced to 50 MHz.',
            'table_body': [
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5644/5645',
                    '50 kHz to 24 MHz',
                    '4 MHz, 5 MHz, 6 MHz, 12 MHz, or 24 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5646',
                    '50 kHz to 25 MHz',
                    '2 MHz, 5 MHz, 10 MHz, or 25 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5840/5841',
                    '50 kHz to 100 MHz',
                    '1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, or 100 MHz'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5830/5831/ 5832 LO1',
                    '8 Hz to 400 MHz',
                    '—'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5830/5831/ 5832 LO2',
                    '4 Hz to 400 MHz',
                    '—'
                ],
                [
                    'NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE Attribute Valid Values on PXIe-5841 with PXIe-5655/NI PXIe-5842 (See note)',
                    '1 nHz to 100 MHz',
                    '1 nHz to 50 MHz'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED Attribute Setting',
                'NIRFSG_VAL_ENABLE',
                'NIRFSG_VAL_DISABLE'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)',
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150152: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This attribute enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE attribute. However, fractional mode may introduce non-harmonic spurs.\n\nThis attribute applies only if you set the NIRFSG_ATTR_LO_SOURCE attribute to Onboard.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" .\n\n**Default Value:** NIRFSG_VAL_ENABLE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\nRefer to the local oscillators topic appropriate to your device for more information about using fractional mode.\n\n**Defined Values**:',
            'note': 'For the PXIe-5841 with PXIe-5655, this attribute is ignored if the PXIe-5655 is used as the LO source.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    '0 (0x0)',
                    'Disables fractional mode for the LO PLL.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '1 (0x1)',
                    'Enables fractional mode for the LO PLL.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoPllFractionalModeEnabled',
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViInt32'
    },
    1150153: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the delay, in seconds, to apply to the I/Q waveform. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Units:** Seconds\n\n**Valid Values:** Plus or minus half of one I/Q sample period\n\n**Supported Devices:** PXIe-5644/5645/5646'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Interpolation Delay',
        'name': 'INTERPOLATION_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150154: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\nBy default, markers and events are delayed to align with the waveform data generated from the device. This attribute adds an additional delay to markers and events. Use this attribute to adjust the time delay between events and the corresponding data.\n\n**Units:** Seconds\n\n**Valid Values:**\n\nPXIe-5644/5645: -1.217 μs to 67.050 μs\n\nPXIe-5646: -0.896 μs to 64.640 μs\n\nPXIe-5820/5830/5831/5832/5840/5841/5842: 0 μs to 3.276 μs\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_',
            'note': 'If you decrease the event delay during generation, some markers may be dropped.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Events:Events Delay',
        'name': 'EVENTS_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150155: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master device when synchronizing the Start Trigger. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.\n\nWhen synchronizing the Start Trigger, one device must always be designated as the master. The master device actively drives the Start Trigger distribution line. For slave devices, set the NIRFSG_ATTR_START_TRIGGER_TYPE attribute to digital edge, and set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to sync_script.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\nRefer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Start Trigger.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Start Trigger.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Master',
        'name': 'SYNC_START_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150156: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\nRefer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Dist Line',
        'name': 'SYNC_START_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150157: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the repetition mode of a waveform when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM. If you set this attribute to VI_TRUE, the number of repetitions is determined by the NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT attribute. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'Repeats the waveform a finite number of times.'
                ],
                [
                    'VI_FALSE',
                    'Repeats the waveform continuously until you abort the generation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Arb:Waveform Repeat Count Is Finite',
        'name': 'ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150158: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the repeat count of a waveform when you set the NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE attribute to VI_TRUE. This attribute is valid only when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** 1\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Waveform Repeat Count',
        'name': 'ARB_WAVEFORM_REPEAT_COUNT',
        'type': 'ViInt32'
    },
    1150160: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute offsets the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY from the RF frequency. Use this attribute to keep the local oscillator (LO) leakage at a determined offset from the RF signal.\n\n**Valid Values:**\n\nPXIe-5644/5645: -42MHz to +42MHz\n\nPXIe-5646: -100MHz to +100MHz\n\nPXIe-5830/5831/5832/5840/5841: -500MHz to +500MHz\n\nPXI-5842 (500 MHz bandwidth option): -250MHz to +250MHz\n\nPXI-5842 (1 GHz bandwidth option): -500MHz to +500MHz\n\nPXI-5842 (2 GHz bandwidth option): -1GHz to +1GHz\n\nPXIe-5842 (4 GHz bandwidth option) using the Standard personality: -1GHz to +1GHz\n\nPXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2GHz to +2GHz\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_',
            'note': '- You cannot set the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute or the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute at the same time as the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.\n\n - Resetting this attribute disables the upconverter frequency offset.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)',
        'name': 'UPCONVERTER_FREQUENCY_OFFSET',
        'type': 'ViReal64'
    },
    1150161: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.\n\n**Units:** Degrees Celsius\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Temperature (Degrees C)',
        'name': 'IQ_OUT_PORT_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150162: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\nYou can specify Marker Events by using scripts to trigger blanking at a certain point in a waveform. For example, if you set this attribute to marker0 str}, and marker0 occurs on samples 1,000 and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000.\n\nPXIe-5645: This attribute is ignored if you are using the I/Q ports.\n\nPXIe-5840/5841: RF blanking does not occur for frequencies below 120MHz.\n\nFor PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n**Valid Values**:',
            'note': 'The shortest supported blanking interval is eight microseconds.',
            'table_body': [
                [
                    '""',
                    'RF blanking is disabled.'
                ],
                [
                    '"Marker0"',
                    'RF blanking is tied to marker0.'
                ],
                [
                    '"Marker1"',
                    'RF blanking is tied to marker1.'
                ],
                [
                    '"Marker2"',
                    'RF blanking is tied to marker2.'
                ],
                [
                    '"Marker3"',
                    'RF blanking is tied to marker3.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:RF Blanking Source',
        'name': 'RF_BLANKING_SOURCE',
        'type': 'ViString'
    },
    1150163: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the load impedance connected to the I/Q OUT port. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).\n\n**Units:** Ohms\n\n**Valid Values:** Any value greater than 0. Values greater than or equal to 1 megaohms (MΩ) are interpreted as high impedance.\n\n**Default Value:** 50 Ω if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_SINGLE_ENDED, and 100 Ω if you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL.\n\n**Supported Devices:** PXIe-5645, PXIe-5820',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the RF ports.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:IQ Out Port:Load Impedance',
        'name': 'IQ_OUT_PORT_LOAD_IMPEDANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150165: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.\n\nThis attribute is valid only when you set the NIRFSG_ATTR_ANALOG_MODULATION_TYPE attribute to NIRFSG_VAL_FM and the NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND attribute to NIRFSG_VAL_NARROWBAND.\n\n**Default Value:** NIRFSG_VAL_100HZ_TO_1KHZ\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_100HZ_TO_1KHZ',
                    '18000 (0x4650)',
                    'Specifies a range from 100Â Hz to 1Â kHz.'
                ],
                [
                    'NIRFSG_VAL_10KHZ_TO_100KHZ',
                    '18002 (0x4652)',
                    'Specifies a range from 10Â kHz to 100Â kHz.'
                ],
                [
                    'NIRFSG_VAL_1KHZ_TO_10KHZ',
                    '18001 (0x4651)',
                    'Specifies a range from 1Â kHz to 10Â kHz.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnalogModulationFmNarrowbandIntegrator',
        'lv_property': 'Modulation:Analog:FM Narrowband Integrator',
        'name': 'ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR',
        'type': 'ViInt32'
    },
    1150166: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\n**Default Value:** 100\n\n**Valid Values:** 0 to 100\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_'
        },
        'lv_property': 'Modulation:Analog:FM Sensitivity',
        'name': 'ANALOG_MODULATION_FM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150167: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\nWhen using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this attribute to determine the coerced value.\n\n**Default Value:** 100\n\n**Valid Values:** 0 to 100\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Amplitude Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_amplitude_modulation.html>`_'
        },
        'lv_property': 'Modulation:Analog:AM Sensitivity',
        'name': 'ANALOG_MODULATION_AM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150168: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n\n**Default Value:** 100\n\n**Valid Values:** 0 to 100\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_'
        },
        'lv_property': 'Modulation:Analog:PM Sensitivity',
        'name': 'ANALOG_MODULATION_PM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150173: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the level of attenuation in the attenuator path. Setting this attribute overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this attribute.\n\n**Units**: dB\n\n**Valid Values**: 0dB to 110dB in steps of 10\n\n**Supported Devices:** PXIe-5654 with PXIe-5696',
            'note': 'Resetting this attribute reverts back to the default unset behavior.'
        },
        'lv_property': 'RF:Attenuator Setting (dB)',
        'name': 'ATTENUATOR_SETTING',
        'type': 'ViReal64'
    },
    1150180: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.\n\nWhen synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5646\n\n**Related Topics**\n\n`Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'The device is the master device for synchronizing the Sample Clock.'
                ],
                [
                    'VI_FALSE',
                    'The device is not the master for synchronizing the Sample Clock.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master',
        'name': 'SYNC_SAMPLE_CLOCK_MASTER',
        'type': 'ViBoolean'
    },
    1150181: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5646\n\n**Related Topics**\n\n`Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Dist Line',
        'name': 'SYNC_SAMPLE_CLOCK_DIST_LINE',
        'type': 'ViString'
    },
    1150182: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the amplitude extender module temperature in degrees Celsius.\n\n**Units**: degrees Celsius (°C)\n\n**Supported Devices:** PXIe-5654 with PXIe-5696'
        },
        'lv_property': 'Device Characteristics:AE Temperature (Degrees C)',
        'name': 'AE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150185: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.\n\nNI-RFSG automatically sets the value of this attribute based on power and frequency settings. Setting this attribute overrides the value chosen by NI-RFSG.\n\n**Default Value:** NIRFSG_VAL_LOW_HARMONIC\n\n**Supported Devices:** PXIe-5654 with PXIe-5696\n\n**Related Topics**\n\n`Low Harmonic Path Versus High Power Path <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/low_harmonic_path_vs_high_power_path.html>`_\n\n**Defined Values**:',
            'note': 'Resetting this attribute reverts back to the default unset behavior.',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_POWER',
                    '16000 (0x3e80)',
                    'Sets the amplification path to use the high power path.'
                ],
                [
                    'NIRFSG_VAL_LOW_HARMONIC',
                    '16001 (0x3e81)',
                    'Sets the amplification path to use the low harmonic path.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AmpPath',
        'lv_property': 'RF:Advanced:Amp Path',
        'name': 'AMP_PATH',
        'type': 'ViInt32'
    },
    1150186: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the nirfsg_InitWithOptions function.\n\nNI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the vector signal transceiver FPGA while maintaining the functionality of the NI-RFSG instrument driver.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/fpga_extensions.html>`_'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Device Characteristics:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150188: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns whether the NI RF signal generator has the fast tuning option available.\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Frequency Tuning Times for 5654 <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.5654.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'The RF signal generator has the fast 100 µs tuning option.'
                ],
                [
                    'VI_FALSE',
                    'The RF signal generator has the 1 ms tuning option.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Device Characteristics:Options:Fast Tuning Option',
        'name': 'FAST_TUNING_OPTION',
        'type': 'ViBoolean'
    },
    1150190: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'PXIe-5654/5654 with PXIe-5696: Specifies the pulse modulation mode to use.\n\nPXIe-5842: This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.\n\n**Default Value:** NIRFSG_VAL_ANALOG\n\n**Supported Devices:** PXIe-5842/5654/5654 with PXIe-5696\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_OPTIMAL_MATCH',
                    'Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION',
                    'Allows for the best on/off power ratio of the pulsed signal.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_ANALOG',
                    'Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.'
                ],
                [
                    'NIRFSG_VAL_PULSE_MODULATION_DIGITAL',
                    'Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationMode',
        'lv_property': 'RF:Advanced:Pulse Modulation Mode',
        'name': 'PULSE_MODULATION_MODE',
        'type': 'ViInt32'
    },
    1150191: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100kHz. Narrowband FM allows for modulating lower frequency signals.\n\n**Default Value:** NIRFSG_VAL_WIDEBAND\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_NARROWBAND',
                    '17000 (0x4268)',
                    'Specifies narrowband frequency modulation.'
                ],
                [
                    'NIRFSG_VAL_WIDEBAND',
                    '17001 (0x4269)',
                    'Specifies wideband frequency modulation.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnalogModulationFmBand',
        'lv_property': 'Modulation:Analog:FM Band',
        'name': 'ANALOG_MODULATION_FM_BAND',
        'type': 'ViInt32'
    },
    1150192: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the phase modulation (PM) mode to use.\n\n**Default Value:** NIRFSG_VAL_LOW_PHASE_NOISE\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_HIGH_DEVIATION',
                    '19000 (0x4a38)',
                    'Specifies high deviation. High deviation comes at the expense of a higher phase noise.'
                ],
                [
                    'NIRFSG_VAL_LOW_PHASE_NOISE',
                    '19001 (0x4a39)',
                    'Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AnalogModulationPmMode',
        'lv_property': 'Modulation:Analog:PM Mode',
        'name': 'ANALOG_MODULATION_PM_MODE',
        'type': 'ViInt32'
    },
    1150194: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the name of the fully qualified signal name as a string.\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Default Values**:\n\nPXIe-5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.\n\nPXIe-5830/5831/5832: /*BasebandModule*/ao/0/ConfigurationSettledEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.\n\nPXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.\n\n**Related Topics**\n\n`Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_\n\n`Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_'
        },
        'lv_property': 'Events:Configuration Settled Event Terminal Name',
        'name': 'CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150195: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables the automatic leveling control (ALC).\n\nPXIe-5654 with PXIe-5696: If this attribute is enabled, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If this attribute is disabled, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the NIRFSG_ATTR_ALC_CONTROL attribute also allows for NI-RFSG to perform an automatic power search.\n\nPXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device. The PXIe-5654 does not support the ALC when used as a stand-alone device.\n\n**Default Value:**\n\nPXIe-5654: NIRFSG_VAL_DISABLE\n\nPXIe-5654 with PXIe-5696: NIRFSG_VAL_ENABLE\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Power Level Adjustment <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_level_adjustment.html>`_\n\n`ALC Closed Loop Versus Open Loop <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_alc_closed_loop_vs_open_loop.html>`_\n\n`Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables ALC.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables the ALC.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticLevelControl',
        'lv_property': 'RF:ALC Control',
        'name': 'ALC_CONTROL',
        'type': 'ViInt32'
    },
    1150196: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables automatic power search. When this attribute is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this attribute is disabled, NI-RFSG does not perform a power search unless you call the nirfsg_PerformPowerSearch function.\n\nThis attribute is ignored when the NIRFSG_ATTR_ALC_CONTROL attribute is enabled.\n\nPXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device.\n\n**Default Value:**\n\nPXIe-5654: NIRFSG_VAL_DISABLE\n\nPXIe-5654 with PXIe-5696: NIRFSG_VAL_ENABLE\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696\n\n**Related Topics**\n\n`Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    '0 (0x0)',
                    'Disables automatic power search.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    '1 (0x1)',
                    'Enables automatic power search.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'AutomaticPowerSearch',
        'lv_property': 'RF:Automatic Power Search',
        'name': 'AUTO_POWER_SEARCH',
        'type': 'ViInt32'
    },
    1150199: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency of the LO source.\n\nTo use this attribute for the PXIe-5830/5831/5832, you must use the channelName parameter of the nirfsg_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_',
            'note': 'This attribute is read/write if you are using an external LO. Otherwise, this attribute is read-only.'
        },
        'lv_property': 'RF:LO Frequency (Hz)',
        'name': 'LO_FREQUENCY',
        'supported_rep_caps': [
            'los'
        ],
        'type': 'ViReal64'
    },
    1150204: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this attribute to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\n**Default Value:** 0 dB\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'name': 'ARB_DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the output behavior for the Marker Event. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_PULSE\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_PULSE',
                    '23000 (0x59d8)',
                    'Specifies the Marker Event output behavior as pulse.'
                ],
                [
                    'NIRFSG_VAL_TOGGLE',
                    '23001 (0x59d9)',
                    'Specifies the Marker Event output behavior as toggle.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventOutputBehavior',
        'lv_property': 'Events:Marker:Output Behavior',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150207: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the pulse width value for the Marker Event. Use the NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS attribute to set the units for the pulse width value. This attribute is valid only when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** 200 ns\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_'
        },
        'lv_property': 'Events:Marker:Pulse:Width Value',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViReal64'
    },
    1150208: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the pulse width units for the Marker Event. This attribute is valid only when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_SECONDS\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_PULSE',
                    '23000 (0x59d8)',
                    'Specifies the Marker Event output behavior as pulse.'
                ],
                [
                    'NIRFSG_VAL_TOGGLE',
                    '23001 (0x59d9)',
                    'Specifies the Marker Event output behavior as toggle.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventPulseWidthUnits',
        'lv_property': 'Events:Marker:Pulse:Width Units',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the initial state for the Marker Event when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_TOGGLE.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_DIGITAL_LOW\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DIGITAL_HIGH',
                    '21001 (0x5209)',
                    'Specifies the initial state of the Marker Event toggle behavior as digital high.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_LOW',
                    '21000 (0x5208)',
                    'Specifies the initial state of the Marker Event toggle behavior as digital low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'MarkerEventToggleInitialState',
        'lv_property': 'Events:Marker:Toggle:Initial State',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'supported_rep_caps': [
            'markers'
        ],
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the total power consumption of the device.\n\n**Units:** watts\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Characteristics:Module Power Consumption (W)',
        'name': 'MODULE_POWER_CONSUMPTION',
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the FPGA temperature in degrees Celsius.\n\nSerial signals between the sensor and the system control unit can potentially modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'If you query this attribute during RF list mode, list steps may take longer to complete during list execution.'
        },
        'lv_property': 'Device Characteristics:FPGA Temperature (Degrees C)',
        'name': 'FPGA_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150212: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the minimum time between temperature sensor readings.\n\n**Units:** Seconds\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:Temperature Read Interval',
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150220: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the delay, in seconds, to apply to the I/Q waveform.\n\nRelative delay allows for delaying the generated signal from one device relative to the generated signal of another device after those devices have been synchronized. You can achieve a negative relative delay by delaying both synchronized devices by the same value (1 μs) before generation begins and then changing the relative delay to a smaller amount than the initial value on only one of the devices.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration or Generation state.\n\n**Units:** Seconds\n\n**Valid Values:**\n\nPXIe-PXIe-5820/5830/5831/5832/5840/5841: 0 μs to 3.2 μs\n\nPXIe-5842: 0 μs to 6.5 μs\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_',
            'note': '- To obtain a negative relative delay when synchronizing the PXIe-5840/5841 with a module that does not support this attribute, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY attribute.\n\n - The resolution of this attribute is a function of the I/Q sample period at 15E(-6) of the sample period but not worse than one Sample Clock period.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Relative Delay',
        'name': 'RELATIVE_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150225: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This attribute can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Units:** Seconds\n\n**Valid Values:** Plus or minus half of one Sample Clock period\n\n**Supported Devices:** PXIe-5820/5840/5841/5842',
            'note': '- The resolution of this attribute is a function of the I/Q sample period at 15E(-6) times that sample period.\n\n - If this attribute is set, NI-TClk cannot perform any sub-Sample Clock adjustment.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay',
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150226: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.\n\nThe NIRFSG_ATTR_SIGNAL_BANDWIDTH centered at the NIRFSG_ATTR_FREQUENCY must fit within the device instantaneous bandwidth, which is centered at the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY.\n\n**Units**: Hz\n\n**Default Value**: N/A\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_\n\n`PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_'
        },
        'lv_property': 'Arb:Device Instantaneous Bandwidth (Hz)',
        'name': 'DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150228: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.\n\n**Default Value:** NIRFSG_VAL_ERROR_REPORTING_WARNING\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ERROR_REPORTING_DISABLED',
                    '1302 (0x516)',
                    'NI-RFSG does not return an error or a warning when an OSP overflow occurs.'
                ],
                [
                    'NIRFSG_VAL_ERROR_REPORTING_WARNING',
                    '1301 (0x515)',
                    'NI-RFSG returns a warning when an OSP overflow occurs.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'OverflowErrorReporting',
        'lv_property': 'Arb:Advanced:Overflow Error Reporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'ViInt32'
    },
    1150239: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the size of the DMA buffer in computer memory, in bytes. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\nA sufficiently large host DMA buffer improves performance by allowing large writes to be transferred more efficiently.\n\n**Units:** bytes\n\n**Default Value:** 8MB\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Data Transfer:Advanced:Host DMA Buffer Size',
        'name': 'HOST_DMA_BUFFER_SIZE',
        'type': 'ViInt64'
    },
    1150241: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the port to configure.\n\n**Valid Values**:\n\nPXIe-5644/5645/5646, PXIe-5820/5840/5841: "" (empty string)\n\nPXIe-5830: if0, if1\n\nPXIe-5831/5832: if0, if1, rf*0-1*/port*x*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.\n\n**Default Value:**\n\nPXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)\n\nPXIe-5830/5831/5832: if0\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\nNIRFSG_ATTR_AVAILABLE_PORTS',
            'note': 'When using RF list mode, ports cannot be shared with NI-RFSA.'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports',
        'name': 'SELECTED_PORTS',
        'type': 'ViString'
    },
    1150242: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.\n\nSet this attribute to NIRFSG_VAL_ENABLE to allow NI-RFSA to control the LO out export. Use the RF OUT LO EXPORT ENABLED attribute to control the LO out export from NI-RFSA.\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices**: PXIe-5840/5841/5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    '0 (0x0)',
                    'Do not allow NI-RFSA to control the NI-RFSG local oscillator export.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    '1 (0x1)',
                    'Allow NI-RFSA to control the NI-RFSG local oscillator export.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'LoOutExportConfigureFromRfsaEnable',
        'lv_property': 'RF:LO Out Export Configure From RFSA',
        'name': 'LO_OUT_EXPORT_CONFIGURE_FROM_RFSA',
        'type': 'ViInt32'
    },
    1150243: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.\n\nSet this attribute to NIRFSG_VAL_ENABLE to export the LO signal from the RF IN LO OUT terminal.\n\nWhen this attribute is enabled, if the NIRFSG_ATTR_LO_SOURCE attribute is set to LO_In and you do not set the NIRFSG_ATTR_LO_FREQUENCY or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes, NI-RFSG rounds the LO frequency to approximately an LO step size as if the source was OnboardClock. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.\n\n**Default Value:** NIRFSG_VAL_UNSPECIFIED\n\n**Supported Devices**: PXIe-5840/5841/5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DISABLE',
                    'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_ENABLE',
                    'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                ],
                [
                    'NIRFSG_VAL_UNSPECIFIED',
                    'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'RFInLoExportEnabled',
        'lv_property': 'RF:RF In LO Export Enabled',
        'name': 'RF_IN_LO_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150244: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.\n\n**Units:** degrees Celsius (°C)\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Default Values:**\n\nPXIe-5830/5831/5832/5842/5860: 0.2\n\nPXIe-5840/5841: 1.0'
        },
        'lv_property': 'RF:Advanced:Thermal Correction Temperature Resolution (Degrees C)',
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'ViReal64'
    },
    1150248: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.\n\nPlacing the upconverter center frequency outside the bandwidth of your waveform can help avoid issues such as LO leakage.\n\nTo set an offset yourself, set this attribute to NIRFSG_VAL_AUTO or NIRFSG_VAL_USER_DEFINED, and set either the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute.\n\nTo allow NI-RFSG to automatically select the upconverter frequency offset, set this attribute to NIRFSG_VAL_AUTO or NIRFSG_VAL_ENABLE and set the NIRFSG_ATTR_SIGNAL_BANDWIDTH to describe the bandwidth of your waveform. The signal bandwidth must be no greater than half the value of the NIRFSG_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH attribute, minus a device-specific guard band. Do not set the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attributes. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal bandwidth. Set this attribute to NIRFSG_VAL_ENABLE if you want to receive an error any time NI-RFSG is unable to apply automatic offset.\n\nWhen you set an offset yourself or do not use an offset, the reference frequency for gain is near the upconverter center frequency, and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSG_VAL_USER_DEFINED. When NI-RFSG automatically sets an offset, the reference frequency for gain is near the NIRFSG_ATTR_FREQUENCY and NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE returns NIRFSG_VAL_ENABLE.\n\n**Default Value:** NIRFSG_VAL_AUTO\n\n**Supported Devices**: PXIe-5830/5831/5832/5841/5842\n\n**Related Topics**\n\n`PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n\n`PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n\n`PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_\n\n**Defined Values**:',
            'note': 'Below 120 MHz, the PXIe-5841 does not use an LO and NIRFSG_VAL_ENABLE is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSG returns an error if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large.'
                ],
                [
                    'NIRFSG_VAL_AUTO',
                    'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided.'
                ],
                [
                    'NIRFSG_VAL_USER_DEFINED',
                    'NI-RFSG uses the offset that you specified with the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'UpconverterFrequencyOffsetMode',
        'lv_property': 'RF:Upconverter:Frequency Offset Mode',
        'name': 'UPCONVERTER_FREQUENCY_OFFSET_MODE',
        'type': 'ViInt32'
    },
    1150249: {
        'access': 'read only',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a list of the ports available for use based on your instrument configuration.\n\n**Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Available Ports',
        'name': 'AVAILABLE_PORTS',
        'type': 'ViString',
        'type_in_documentation': 'list of str'
    },
    1150251: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a string that contains the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.\n\nThis attribute is channel dependent if multiple FPGA targets are supported.\n\n**Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Device Characteristics:FPGA Target Name',
        'name': 'FPGA_TARGET_NAME',
        'type': 'ViString'
    },
    1150252: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the type of de-embedding to apply to measurements on the specified port.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViInt32 function to specify the name of the port to configure for de-embedding.\n\nIf you set this attribute to NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.\n\n**Default Value**: NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR\n\n**Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSG_VAL_DEEMBEDDING_TYPE_NONE\n\n**Valid Values for PXIe-5831** NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR, NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, or NIRFSG_VAL_DEEMBEDDING_TYPE_NONE. NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_NONE',
                    '25000 (0x61a8)',
                    'De-embedding is not applied to the measurement.'
                ],
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR',
                    '25001 (0x61a9)',
                    'De-embeds the measurement using only the gain term.'
                ],
                [
                    'NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR',
                    '25002 (0x61aa)',
                    'De-embeds the measurement using the gain term and the reflection term.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'DeembeddingType',
        'lv_property': 'De-embedding:Type',
        'name': 'DEEMBEDDING_TYPE',
        'supported_rep_caps': [
            'ports'
        ],
        'type': 'ViInt32'
    },
    1150253: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Selects the de-embedding table to apply to the measurements on the specified port.\n\nTo use this attribute, you must use the channelName parameter of the nirfsg_SetAttributeViString function to specify the name of the port to configure for de-embedding.\n\nIf de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT.\n\nUse the create deembedding sparameter table array function to create tables.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'De-embedding:Selected Table',
        'name': 'DEEMBEDDING_SELECTED_TABLE',
        'supported_rep_caps': [
            'ports'
        ],
        'type': 'ViString'
    },
    1150257: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.\n\n**Valid Values**:\n\nLO1: 1 Hz to 50 MHz\n\nLO2: 1 Hz to 100 MHz\n\n**Default Value**: 1 MHz\n\n**Supported Devices**: PXIe-5830/5831/5832'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)',
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150258: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the NIRFSG_ATTR_DEVICE_TEMPERATURE attribute.\n\nFor example, if this property is set to 5.0, and the device is self-calibrated at 35°C, then you can expect to run the device from 30°C to 40°C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.\n\n**Units:** degrees Celsius (°C)\n\n**Default Value**:\n\n**PXIe-5830/5831/5832/5842/5860**: 5\n\n**PXIe-5840/5841**: 10\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'RF:Advanced:Thermal Correction Headroom Range (Degrees C)',
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'ViReal64'
    },
    1150263: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the I/Q rate of the waveform. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate an I/Q rate with a waveform.\n\n`Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_'
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform IQ Rate (S/s)',
        'name': 'WAVEFORM_IQ_RATE',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViReal64'
    },
    1150264: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× NIRFSG_ATTR_IQ_RATE).\n\n**Units**: hertz (Hz)\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Signal Bandwidth (Hz)',
        'name': 'WAVEFORM_SIGNAL_BANDWIDTH',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViReal64'
    },
    1150265: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.\n\n**Units**: dB\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5841 with PXIe-5655'
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Runtime Scaling',
        'name': 'WAVEFORM_RUNTIME_SCALING',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViReal64'
    },
    1150266: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the peak-to-average power ratio (PAPR).\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform PAPR (dB)',
        'name': 'WAVEFORM_PAPR',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies a list of ports for which to fix the group delay.\n\n\n**Supported Devices:** PXIe-5831/5832'
        },
        'lv_property': 'Device Specific:Vector Signal Transceiver:Signal Path:Fixed Group Delay Across Ports',
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'ViString',
        'type_in_documentation': 'list of str'
    },
    1150273: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables the detection of burst start and burst stop locations in the waveform. You can read the detected burst start and burst stop locations using nirfsg_GetWaveformBurstStartLocations and nirfsg_GetWaveformBurstStopLocations functions respectively.\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'note': '- When you download a waveform using nirfsg_ReadAndDownloadWaveformFromFileTdms function and if NIRFSG_ATTR_WAVEFORM_RF_BLANKING attribute is enabled, you must set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute to NIRFSG_VAL_DISABLE.\n\n - For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'Burst detection is enabled.'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'Burst detection is disabled.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformBurstDetection',
        'lv_property': 'Arb:Write Waveform Burst Detection:Enabled',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION',
        'type': 'ViInt32'
    },
    1150274: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute. When you set NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE to NIRFSG_VAL_AUTO, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this attribute to NIRFSG_VAL_MANUAL and specify the burst detection parameters using the write waveform burst detection minimum quiet time, NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD, write waveform burst detection minimum burst time attributes.\n\n**Default Value:** NIRFSG_VAL_AUTO\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_AUTO',
                    'NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.'
                ],
                [
                    'NIRFSG_VAL_MANUAL',
                    'User sets the burst detection parameters.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformBurstDetectionMode',
        'lv_property': 'Arb:Write Waveform Burst Detection:Mode',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_MODE',
        'type': 'ViInt32'
    },
    1150276: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this attribute. This attribute is ignored when you disable the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION attribute or when you set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE attribute to NIRFSG_VAL_AUTO.\n\n**Units:** dB\n\n**Default Value:** 0\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'Arb:Write Waveform Burst Detection:Power Threshold',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD',
        'type': 'ViReal64'
    },
    1150278: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': '\n**Defined Values**:\n\nName (Value): Description\n\nNIRFSG_VAL_DISABLE (0):\tRF blanking is disabled.\n\nNIRFSG_VAL_ENABLE (1):\tRF blanking is enabled.\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Related Topics**\n\n`Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_\n\nEnables or disables RF blanking.',
            'note': 'For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any nirfsg_Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking attributes. Alternatively, you can call nirfsg_ResetWithOptions or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.',
            'table_body': [
                [
                    '"" (empty string)',
                    'NIRFSG_VAL_DISABLE',
                    'No blanking performed.'
                ],
                [
                    '"" (empty string)',
                    'NIRFSG_VAL_ENABLE',
                    'Blanking performed based on burst start and stop values and blanking source set to private marker.'
                ],
                [
                    'NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3',
                    'NIRFSG_VAL_DISABLE',
                    'Blanking performed based on the marker locations for the marker that the user set in the blanking source.'
                ],
                [
                    'NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3',
                    'NIRFSG_VAL_ENABLE',
                    'Error is shown.'
                ]
            ],
            'table_header': [
                'NIRFSG_ATTR_RF_BLANKING_SOURCE',
                'NIRFSG_ATTR_WAVEFORM_RF_BLANKING',
                'Behaviour'
            ]
        },
        'enum': 'RFBlanking',
        'lv_property': 'Arb:Waveform Attributes:Waveform RF Blanking',
        'name': 'WAVEFORM_RF_BLANKING',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViInt32'
    },
    1150289: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the de-embedding gain applied to compensate for the mismatch on the specified port. If de-embedding is enabled, NI-RFSG uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.\n\n**Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860'
        },
        'lv_property': 'De-embedding:Compensation Gain',
        'name': 'DEEMBEDDING_COMPENSATION_GAIN',
        'supported_rep_caps': [
            'ports'
        ],
        'type': 'ViReal64'
    },
    1150290: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the configurations to skip while loading from a file.\n\n**Default Value:**  NIRFSG_VAL_SKIP_NONE\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE',
                    'NI-RFSG loads all the configurations to the session.'
                ],
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS',
                    'NI-RFSG skips loading the waveform configurations to the session.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'LoadOptions',
        'lv_property': 'Load Configurations:Load Options',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS',
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the configurations to skip to reset while loading configurations from a file.\n\n**Default Value:**  NIRFSG_VAL_SKIP_NONE\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE',
                    'NI-RFSG resets all configurations.'
                ],
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS',
                    'NI-RFSG skips resetting the waveform configurations.'
                ],
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS',
                    'NI-RFSG skips resetting the scripts.'
                ],
                [
                    'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES',
                    'NI-RFSG skips resetting the de-embedding tables.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'LoadConfigurationResetOptions',
        'lv_property': 'Load Configurations:Reset Options',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS',
        'type': 'ViInt32'
    },
    1150292: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** 10MHz\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'table_body': [
                [
                    '10000000.0',
                    'Uses a 10MHz Reference Clock rate.'
                ],
                [
                    '100000000.0',
                    'Uses a 100MHz Reference Clock rate.'
                ],
                [
                    '1000000000.0',
                    'Uses a 1GHz Reference Clock rate.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Clock:Reference Clock Exported Rate (Hz)',
        'name': 'EXPORTED_REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150293: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether to perform the normalization on a waveform.\n\n**Default Value:** NIRFSG_VAL_DISABLE\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Defined Values**:',
            'note': 'You can not set NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION and NIRFSG_ATTR_POWER_LEVEL_TYPE attributes at the same time.',
            'table_body': [
                [
                    'NIRFSG_VAL_ENABLE',
                    'Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00'
                ],
                [
                    'NIRFSG_VAL_DISABLE',
                    'Disables normalization on the waveform.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'WriteWaveformNormalization',
        'lv_property': 'Arb:Write Waveform Normalization',
        'name': 'WRITE_WAVEFORM_NORMALIZATION',
        'type': 'ViInt32'
    },
    1150297: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the size of the waveform specified by an active channel.\n\n**Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860'
        },
        'lv_property': 'Arb:Waveform Attributes:Waveform Size',
        'name': 'WAVEFORM_WAVEFORM_SIZE',
        'supported_rep_caps': [
            'waveforms'
        ],
        'type': 'ViInt32'
    },
    1150307: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n**Supported Devices:**  PXIe-5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'lv_property': 'RF:Advanced:Pulse Modulation Active Level',
        'name': 'PULSE_MODULATION_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150308: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** PulseIn\n\n**Supported Devices:**  PXIe-5842\n\n **Possible Values**:',
            'table_body': [
                [
                    '"PulseIn"',
                    'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                ],
                [
                    '"Marker0"',
                    'The trigger is received from the Marker 0.'
                ],
                [
                    '"Marker1"',
                    'The trigger is received from the Marker 1.'
                ],
                [
                    '"Marker2"',
                    'The trigger is received from the Marker 2.'
                ],
                [
                    '"Marker3"',
                    'The trigger is received from the Marker 3.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationSource',
        'lv_property': 'Modulation:Pulse:Pulse Modulation Source',
        'name': 'PULSE_MODULATION_SOURCE',
        'type': 'ViString'
    },
    1150309: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `do not export str`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `exported pulse modulation event active level`. You can tri-state this terminal by setting this property to `do not export str` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** PulseOut\n\n**Supported Devices:**  PXIe-5842\n\n**Possible Values**:',
            'table_body': [
                [
                    '""',
                    'Pulse modulation video signal is not exported.'
                ],
                [
                    '"PulseOut"',
                    'Export the pulse modulation video signal on the pulse out terminal.'
                ]
            ],
            'table_header': [
                'Possible Value',
                'Description'
            ]
        },
        'enum': 'PulseModulationOutputTerminal',
        'lv_property': 'Events:Pulse Modulation:Exported Pulse Modulation Event Output Terminal',
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150310: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active level of the exported Pulse Modulation Event. When `attribute pulse modulation enabled` is Enabled, `pulse modulation active level` is `active high`, `exported pulse modulation event output terminal` is `PulseOut`, and this property is `active high`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_ACTIVE_HIGH\n\n**Supported Devices:**  PXIe-5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_ACTIVE_HIGH',
                    '9000 (0x2328)',
                    'Trigger when the digital trigger signal is high.'
                ],
                [
                    'NIRFSG_VAL_ACTIVE_LOW',
                    '9001 (0x2329)',
                    'Trigger when the digital trigger signal is low.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'lv_property': 'Events:Pulse Modulation:Exported Pulse Modulation Event Active Level',
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150311: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies which path to configure to generate a signal.'
        },
        'lv_property': 'Signal Path:Advanced:Selected Path',
        'name': 'SELECTED_PATH',
        'type': 'ViString'
    },
    1150312: {
        'access': 'read only',
        'attribute_class': 'AttributeViStringCommaSeparated',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns a list of the configurable paths available for use based on your instrument configuration.'
        },
        'lv_property': 'Signal Path:Advanced:Available Paths',
        'name': 'AVAILABLE_PATHS',
        'type': 'ViString',
        'type_in_documentation': 'list of str'
    },
    1154097: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the gain the upconverter applies to the signal.\n\n**Units**: dB\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860',
            'note': 'This attribute is read/write on the PXI-5610 and PXIe-5611 and is read-only on the PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
        },
        'lv_property': 'RF:Upconverter:Gain (dB)',
        'name': 'UPCONVERTER_GAIN',
        'type': 'ViReal64'
    },
    1154098: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this attribute while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841 device enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.\n\n**Units**: hertz (Hz)\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842',
            'note': '- This attribute is read/write on the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, and is read-only on the PXI-5670/5671.\n\n - Resetting this attribute disables in-band retuning, however, for the PXIe-5820, in-band retuning is always enabled.\n\n - For the PXIe-5820, the only valid value for this attribute is 0.\n\n - Setting this attribute while the PXIe-5644/5645/5646, PXIe-5673/5673E, or PXIe-5820/5830/5831/5832/5840/5841/5842 device is generating has no effect until a dynamic attribute is set.'
        },
        'lv_property': 'RF:Upconverter:Center Frequency (Hz)',
        'name': 'UPCONVERTER_CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this attribute specifies the center frequency of the signal.\n\nThe PXI-5670/5671, PXIe-5672, PXIe-5820, and PXIe-5860 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this attribute.\n\n**Units**: hertz (Hz)\n\n**Defined Values**:\nRefer to the specifications document for your device allowable frequency settings.\n\n**Default Value:**\n\nPXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E: 100MHz\n\nPXIe-5653: 4GHz\n\nPXIe-5820: 0Hz\n\nPXIe-5830/5831/5832: 6.5 GHz\n\nPXIe-5840/5841/5860, PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options): 1GHz\n\nPXIe-5842 (4 GHz bandwidth option) using the Standard personality: 1GHz\n\nPXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: 6.5GHz\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureRf',
            'note': 'For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Frequency (Hz)',
        'name': 'FREQUENCY',
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies either the average power level or peak power level of the generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute setting.\n\nThe PXI-5670/5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this attribute. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this attribute.\n\nRefer to the specifications document for your device for allowable power level settings.\n\n**Units**: dBm\n\n**Default Values:**\n\nPXIe-5644/5645/5646, PXIe-5673/5673E: -100\n\nPXI/PXIe-5650/5651/5652: -90\n\nPXIe-5654: -7\n\nPXIe-5654 with PXIe-5696: -110\n\nPXI-5670/5671, PXIe-5672: -145\n\nPXIe-5830/5831/5832/5840/5841/5842/5860: -174\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860\n**High-Level Functions**:\n\n- nirfsg_ConfigureRf',
            'note': '- For the PXIe-5653, this attribute is read-only.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.'
        },
        'lv_property': 'RF:Power Level (dBm)',
        'name': 'POWER_LEVEL',
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies whether signal output is enabled. Setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute to VI_FALSE while in the Generation state stops signal output, although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute while in the Committed state does not transition the device to the Configuration state, but output changes immediately.\n\n**Default Value:** VI_TRUE\n\n**Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Output Enabled <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/outputenable.html>`_\n\n`NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_\n\n**Defined Values**:',
            'note': '- For the PXIe-5653, this attribute controls only the LO1 terminal.\n\n - For the PXIe-5645, this attribute is ignored if you are using the I/Q ports.\n\n - When the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set to a valid list name, setting the NIRFSG_ATTR_OUTPUT_ENABLED attribute transitions the device to the Configuration state.',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables signal output.'
                ],
                [
                    'VI_FALSE',
                    'Disables signal output.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'RF:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'type': 'ViBoolean'
    },
    1250051: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables pulse modulation.\n\nPXIe-5654/5654 with PXIe-5696: If this attribute is enabled and the signal at the PULSEIN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.\n\nPXIe-5673/5673E: If this attribute is enabled and the signal at the PLSMOD front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.\n\nPXIe-5842: If this attribute is enabled and the signal at the PULSE IN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled. This behavior can be modified by setting pulse modulation active level.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E\n\n**Related Topics**\n\n`Pulse Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/pulse_modulation.html>`_\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'Enables pulse modulation.'
                ],
                [
                    'VI_FALSE',
                    'Disables pulse modulation.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Modulation:Pulse:Pulse Modulation Enabled',
        'name': 'PULSE_MODULATION_ENABLED',
        'type': 'ViBoolean'
    },
    1250322: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute is set to ClkIn, RefIn, or RefIn2\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696, the NI-RFSG device must be in the Committed state to read this attribute. When you read this attribute, it returns the frequency the device is locked to during the Committed state.\n\nIf you set this attribute to Auto, NI-RFSG uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.\n\n**Valid Values:**\n\nPXIe-5654/5654 with PXIe-5696: Values between 1MHz to 20MHz in 1MHz steps are supported in addition to the Auto and 10MHz values.\n\nPXIe-5841 with PXIe-5655, PXIe-5842: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz \n\ny, where\n\ny is 4, 8, 16, 24, 25, or 32.\n\nPXIe-5860: 10 MHz, 100 MHz\n\n**Units**: hertz (Hz)\n\n**Default Value:** Auto\n\n**Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureRefClock\n\n**Defined Values**:',
            'note': 'Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10MHz.',
            'table_body': [
                [
                    'Auto',
                    '-1.0',
                    'Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it.'
                ],
                [
                    '10MHz',
                    '10000000.0',
                    'Uses a 10 MHz Reference Clock rate.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'lv_property': 'Clock:Reference Clock Rate (Hz)',
        'name': 'REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1250404: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** VI_FALSE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842\n\n**Defined Values**:',
            'table_body': [
                [
                    'VI_TRUE',
                    'NI-RFSG device applies noninverse phase rotation of the I/Q signal.'
                ],
                [
                    'VI_FALSE',
                    'NI-RFSG device applies inverse phase rotation of the I/Q signal.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'name': 'IQ_SWAP_ENABLED',
        'type': 'ViBoolean'
    },
    1250451: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the waveform in onboard memory to generate upon calling the nirfsg_Init function when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM. The NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute is ignored when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_SCRIPT or NIRFSG_VAL_CW. To set the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** "" (empty string)\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_SelectArbWaveform'
        },
        'lv_property': 'Arb:Waveform Capabilities:Selected Waveform',
        'name': 'ARB_SELECTED_WAVEFORM',
        'type': 'ViString'
    },
    1250452: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'This attribute specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 × IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to ( *f*/0.4).\n\nThis attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT.\n\nTo set this attribute, the NI-RFSG device must be in the Configuration state.\n\nSetting this attribute to 50 MS/s on the PXI-5670/5671 and PXIe-5672 has the following implications:\n- NI-RFSG is forced to place the carrier frequency at 18 MHz ± 1 MHz to avoid aliasing. This means that NI-RFSG cannot select a carrier frequency that could optimize waveform size if phase continuity is enabled.  \n- Output signal bandwidth must be <5 MHz to avoid aliasing.  \n- Close-in phase noise is higher.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_\n\n`Assigning Properties or Attributes to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this attribute to associate an I/Q rate with a waveform.\n\n`Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_\n\n**Valid Values**:',
            'note': 'Use this attribute to associate an I/Q rate with a waveform.',
            'table_body': [
                [
                    'PXIe-5644/5645',
                    'Up to 120 MS/s.'
                ],
                [
                    'PXIe-5646',
                    'Up to 250 MS/s.'
                ],
                [
                    'PXI-5670',
                    '50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)'
                ],
                [
                    '',
                    '100 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)'
                ],
                [
                    'PXI-5671',
                    '50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)'
                ],
                [
                    '',
                    '100 MS/s'
                ],
                [
                    'PXIe-5672 ',
                    'Up to 100 MS/s.'
                ],
                [
                    'PXIe-5673/5673E',
                    'Up to 200 MS/s. Note that -  If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN NIFGEN_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY attribute is disabled if the requested I/Q rate is less than 1.5 MS/s.'
                ],
                [
                    'PXIe-5820/5830/5831/5832/5840/5841/5860',
                    'Up to 1.25 GS/s.'
                ],
                [
                    'PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)',
                    'Up to 2.5 GS/s'
                ],
                [
                    ' PXIe-5842 (4 GHz bandwidth option) using the Standard personality',
                    'Up to 2.5 GS/s'
                ],
                [
                    'PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality',
                    '5 GS/s only.'
                ]
            ],
            'table_header': [
                'Device',
                'I/Q Rates'
            ]
        },
        'lv_property': 'Acquisition:IQ',
        'name': 'IQ_RATE',
        'type': 'ViReal64'
    },
    1250454: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the maximum number of waveforms the device can hold in memory.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Max Number Waveforms',
        'name': 'ARB_MAX_NUMBER_WAVEFORMS',
        'type': 'ViInt32'
    },
    1250455: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN and NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX arbitrary waveform sizes.\n\nPXI-5671, PXIe-5672: The value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE attribute before reading this attribute.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Waveform Quantum',
        'name': 'ARB_WAVEFORM_QUANTUM',
        'type': 'ViInt32'
    },
    1250456: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the smallest allowable waveform size. For the PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE attribute before reading this attribute.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsg_QueryArbWaveformCapabilities'
        },
        'lv_property': 'Arb:Waveform Capabilities:Min Waveform Size',
        'name': 'ARB_WAVEFORM_SIZE_MIN',
        'type': 'ViInt32'
    },
    1250457: {
        'access': 'read only',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the size of the largest waveform that is allowed.\n\nTo read this attribute, the NI-RFSG device must be in the Configuration state.\n\nFor the PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE before reading this attribute. For the PXIe-5673/5673E, the maximum waveform size is reduced to account for the amount of device memory currently used.\n\n**Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**High-Level Functions**:\n\n- nirfsg_QueryArbWaveformCapabilities',
            'note': 'Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.'
        },
        'lv_property': 'Arb:Waveform Capabilities:Max Waveform Size',
        'name': 'ARB_WAVEFORM_SIZE_MAX',
        'type': 'ViInt32'
    },
    1250458: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the Start Trigger type. Depending upon the value of this attribute, more attributes may be needed to fully configure the trigger. To set this attribute, the NI-RFSG device must be in the Configuration state.\n\n**Default Value:** NIRFSG_VAL_NONE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeStartTrigger\n- nirfsg_ConfigureSoftwareStartTrigger\n- nirfsg_DisableStartTrigger\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_NONE',
                    'No trigger is configured.'
                ],
                [
                    'NIRFSG_VAL_DIGITAL_EDGE',
                    'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                ],
                [
                    'NIRFSG_VAL_SOFTWARE',
                    'The data operation does not start until a software event occurs. You may create a software trigger by calling the niRFSG_SendSoftwareEdgeTrigger function.'
                ]
            ],
            'table_header': [
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTriggerType',
        'lv_property': 'Triggers:Start:Type',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1250459: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {
            'description': 'Specifies the active edge for the Start Trigger. This attribute is used when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to digital edge. To set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute, the NI-RFSG device must be in the Configuration state.\n\nPXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.\n\n**Default Value:** NIRFSG_VAL_RISING_EDGE\n\n**Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n\n**Related Topics**\n\n`Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_\n\n`Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_\n\n**High-Level Functions**:\n\n- nirfsg_ConfigureDigitalEdgeStartTrigger\n\n**Defined Values**:',
            'table_body': [
                [
                    'NIRFSG_VAL_FALLING_EDGE',
                    '1 (0x1)',
                    'Occurs when the signal transitions from high level to low level.'
                ],
                [
                    'NIRFSG_VAL_RISING_EDGE',
                    '0 (0x0)',
                    'Occurs when the signal transitions from low level to high level.'
                ]
            ],
            'table_header': [
                'Name',
                'Value',
                'Description'
            ]
        },
        'enum': 'StartTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nirfsg/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/config.py sha256=831339cd4fdc4cd03d66de4ba38bd2cda4dff52361f9916a5644b579c071084e bytes=2072 -->
## FILE: src/nirfsg/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/config.py`
- sha256: `831339cd4fdc4cd03d66de4ba38bd2cda4dff52361f9916a5644b579c071084e`
- bytes: 2072

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 26.3.0d9999
config = {
    'api_version': '26.3.0d9999',
    'c_function_prefix': 'niRFSG_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'generation'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-RFSG',
    'enum_whitelist_prefix': [
        'RANGE_',
        'CLOCK_RATE_'
    ],
    'enum_whitelist_suffix': [
        '_HERTZ',
        '_KILOHERTZ',
        '_MEGAHERTZ',
        '_GIGAHERTZ',
        '_TOWARDS_DUT'
    ],
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiRFSG',
    'init_function': 'InitWithOptions',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsg',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSG.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSG_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nirfsg',
    'repeated_capabilities': [
        {
            'prefix': 'marker',
            'python_name': 'markers'
        },
        {
            'prefix': 'scripttrigger',
            'python_name': 'script_triggers'
        },
        {
            'prefix': 'waveform::',
            'python_name': 'waveforms'
        },
        {
            'prefix': '',
            'python_name': 'ports'
        },
        {
            'prefix': 'LO',
            'python_name': 'los'
        },
        {
            'prefix': '',
            'python_name': 'device_temperatures'
        },
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-RFSG session to the NI-RFSG driver',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': True
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/config_addon.py sha256=9ede360d14430b6e5377e86c2903093fbf1c3c170d6ba4292c57060e4b07aa06 bytes=332 -->
## FILE: src/nirfsg/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/config_addon.py`
- sha256: `9ede360d14430b6e5377e86c2903093fbf1c3c170d6ba4292c57060e4b07aa06`
- bytes: 332

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.1.1.dev0',
    'development_status': '4 - Beta',
    'latest_runtime_version_tested_against': '2025 Q4 Patch 1',
    'initial_release_year': '2025',
    'custom_types': [
    ]
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/enums.py sha256=8f088c8318449c05aaa9b5f0f7e0265cfb88a88336ac53bbf076dfb329744cac bytes=52991 -->
## FILE: src/nirfsg/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/enums.py`
- sha256: `8f088c8318449c05aaa9b5f0f7e0265cfb88a88336ac53bbf076dfb329744cac`
- bytes: 52991

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 26.3.0d9999
enums = {
    'AllowOutOfSpecificationUserSettings': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables out-of-specification user settings.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables out-of-specification user settings.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AmpPath': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the amplification path to use the high power path.'
                },
                'name': 'NIRFSG_VAL_HIGH_POWER',
                'value': 16000
            },
            {
                'documentation': {
                    'description': 'Sets the amplification path to use the low harmonic path.'
                },
                'name': 'NIRFSG_VAL_LOW_HARMONIC',
                'value': 16001
            }
        ]
    },
    'AnalogModulationFmBand': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies narrowband frequency modulation.'
                },
                'name': 'NIRFSG_VAL_NARROWBAND',
                'value': 17000
            },
            {
                'documentation': {
                    'description': 'Specifies wideband frequency modulation.'
                },
                'name': 'NIRFSG_VAL_WIDEBAND',
                'value': 17001
            }
        ]
    },
    'AnalogModulationFmNarrowbandIntegrator': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies a range from 100Hz to 1kHz.'
                },
                'name': 'NIRFSG_VAL_100HZ_TO_1KHZ',
                'python_name': 'RANGE_100_HERTZ_TO_1_KILOHERTZ',
                'value': 18000
            },
            {
                'documentation': {
                    'description': 'Specifies a range from 1kHz to 10kHz.'
                },
                'name': 'NIRFSG_VAL_1KHZ_TO_10KHZ',
                'python_name': 'RANGE_1_KILOHERTZ_TO_10_KILOHERTZ',
                'value': 18001
            },
            {
                'documentation': {
                    'description': 'Specifies a range from 10kHz to 100kHz.'
                },
                'name': 'NIRFSG_VAL_10KHZ_TO_100KHZ',
                'python_name': 'RANGE_10_KILOHERTZ_TO_100_KILOHERTZ',
                'value': 18002
            }
        ]
    },
    'AnalogModulationPmMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies high deviation. High deviation comes at the expense of a higher phase noise.'
                },
                'name': 'NIRFSG_VAL_HIGH_DEVIATION',
                'value': 19000
            },
            {
                'documentation': {
                    'description': 'Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.'
                },
                'name': 'NIRFSG_VAL_LOW_PHASE_NOISE',
                'value': 19001
            }
        ]
    },
    'AnalogModulationType': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables analog modulation.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is FM.'
                },
                'name': 'NIRFSG_VAL_FM',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is PM.'
                },
                'name': 'NIRFSG_VAL_PM',
                'value': 2001
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is AM.'
                },
                'name': 'NIRFSG_VAL_AM',
                'value': 2002
            }
        ]
    },
    'ArbOnboardSampleClockMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Sample rates are generated by a high-resolution clock.'
                },
                'name': 'NIRFSG_VAL_HIGH_RESOLUTION',
                'value': 6000
            },
            {
                'documentation': {
                    'description': 'Sample rates are generated by dividing the source frequency.'
                },
                'name': 'NIRFSG_VAL_DIVIDE_DOWN',
                'value': 6001
            }
        ]
    },
    'ArbSampleClockSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the AWG module onboard clock as the Sample Clock source.'
                },
                'name': 'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'Uses the external clock as the Sample Clock source.'
                },
                'name': 'NIRFSG_VAL_CLK_IN_STR',
                'value': 'ClkIn'
            }
        ]
    },
    'AutomaticLevelControl': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables ALC.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables the ALC.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AutomaticPowerSearch': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables automatic power search.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables automatic power search.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AutomaticThermalCorrection': {
        'values': [
            {
                'documentation': {
                    'description': 'Automatic thermal correction is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Automatic thermal correction is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'DeembeddingType': {
        'values': [
            {
                'documentation': {
                    'description': 'De-embedding is not applied to the measurement.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_NONE',
                'value': 25000
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using only the gain term.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR',
                'value': 25001
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using the gain term and the reflection term.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR',
                'value': 25002
            }
        ]
    },
    'DigitalEqualizationEnabled': {
        'values': [
            {
                'documentation': {
                    'description': 'Filter is not applied'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Filter is applied.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'DirectDownload': {
        'values': [
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                },
                'name': 'NIRFSG_VAL_UNSPECIFIED',
                'value': -2
            }
        ]
    },
    'Format': {
        'values': [
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                'value': 26001
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                'value': 26002
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                'value': 26000
            }
        ]
    },
    'FrequencySettlingUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the time to wait after the frequency PLL locks.'
                },
                'name': 'NIRFSG_VAL_TIME_AFTER_LOCK',
                'value': 12000
            },
            {
                'documentation': {
                    'description': 'Specifies the time to wait after all writes occur to change the frequency'
                },
                'name': 'NIRFSG_VAL_TIME_AFTER_IO',
                'value': 12001
            },
            {
                'documentation': {
                    'description': 'Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6).'
                },
                'name': 'NIRFSG_VAL_PPM',
                'value': 12002
            }
        ]
    },
    'GenerationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate a CW signal.'
                },
                'name': 'NIRFSG_VAL_CW',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_WAVEFORM',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate arbitrary waveforms as directed by the NIRFSG_ATTR_SELECTED_SCRIPT attribute.'
                },
                'name': 'NIRFSG_VAL_SCRIPT',
                'value': 1002
            }
        ]
    },
    'IQOutPortTerminalConfiguration': {
        'values': [
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to differential.'
                },
                'name': 'NIRFSG_VAL_DIFFERENTIAL',
                'value': 15000
            },
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to single-ended.'
                },
                'name': 'NIRFSG_VAL_SINGLE_ENDED',
                'value': 15001
            }
        ]
    },
    'LoOutEnabled': {
        'values': [
            {
                'documentation': {
                    'description': 'The local oscillator signal is present at the LO OUT front panel connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The local oscillator signal is  not present at the LO OUT front panel connector..'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'LoOutExportConfigureFromRfsaEnable': {
        'values': [
            {
                'documentation': {
                    'description': 'Do not allow NI-RFSA to control the NI-RFSG local oscillator export.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Allow NI-RFSA to control the NI-RFSG local oscillator export.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'LoPllFractionalModeEnabled': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'LoSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_ONBOARD_STR',
                'value': 'Onboard'
            },
            {
                'documentation': {
                    'description': 'Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the UPCONVERTER_CENTER_FREQUENCY attribute to specify the LO frequency.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_LO_IN_STR',
                'value': 'LO_In'
            },
            {
                'documentation': {
                    'description': 'Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_SECONDARY_STR',
                'value': 'Secondary'
            },
            {
                'documentation': {
                    'description': 'Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR',
                'value': 'SG_SA_Shared'
            },
            {
                'documentation': {
                    'description': 'NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED_STR',
                'value': 'Automatic_SG_SA_Shared'
            }
        ]
    },
    'LoadConfigurationResetOptions': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the waveform configurations.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the de-embedding tables.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the scripts.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'NI-RFSG resets all configurations.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE',
                'value': 0
            }
        ]
    },
    'LoadOptions': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG loads all the configurations to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips loading the waveform configurations to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips loading the scripts to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_SCRIPTS',
                'value': 2
            }
        ]
    },
    'LoopBandwidth': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the narrowest loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_NARROW',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses the medium loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_MEDIUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Uses the widest loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_WIDE',
                'value': 2
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Marker Event output behavior as pulse.'
                },
                'name': 'NIRFSG_VAL_PULSE',
                'value': 23000
            },
            {
                'documentation': {
                    'description': 'Specifies the Marker Event output behavior as toggle.'
                },
                'name': 'NIRFSG_VAL_TOGGLE',
                'value': 23001
            }
        ]
    },
    'MarkerEventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Marker Event pulse width units as seconds.'
                },
                'name': 'NIRFSG_VAL_SECONDS',
                'value': 22000
            },
            {
                'documentation': {
                    'description': 'Specifies the Marker Event pulse width units as Sample Clock periods.'
                },
                'name': 'NIRFSG_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 22001
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the initial state of the Marker Event toggle behavior as digital low.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_LOW',
                'value': 21000
            },
            {
                'documentation': {
                    'description': 'Specifies the initial state of the Marker Event toggle behavior as digital high.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_HIGH',
                'value': 21001
            }
        ]
    },
    'Module': {
        'values': [
            {
                'documentation': {
                    'description': 'The AWG associated with the primary module.'
                },
                'name': 'NIRFSG_VAL_AWG',
                'value': 13001
            },
            {
                'documentation': {
                    'description': 'The LO associated with the primary module.'
                },
                'name': 'NIRFSG_VAL_LO',
                'value': 13002
            },
            {
                'documentation': {
                    'description': 'The stand-alone device or the main module in a multi-module device.'
                },
                'name': 'NIRFSG_VAL_PRIMARY_MODULE',
                'value': 13000
            }
        ]
    },
    'OffsetUnits': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the unit in percentage.'
                },
                'name': 'NIRFSG_VAL_PERCENT',
                'value': 11000
            },
            {
                'documentation': {
                    'description': 'Specifies the unit in volts.'
                },
                'name': 'NIRFSG_VAL_VOLTS',
                'value': 11001
            }
        ]
    },
    'OutputPort': {
        'values': [
            {
                'documentation': {
                    'description': 'Enables the RF OUT port. This value is not valid for the PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_RF_OUT',
                'value': 14000
            },
            {
                'documentation': {
                    'description': 'Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_IQ_OUT',
                'value': 14001
            },
            {
                'documentation': {
                    'description': 'Enables the CAL OUT port.'
                },
                'name': 'NIRFSG_VAL_CAL_OUT',
                'value': 14002
            },
            {
                'documentation': {
                    'description': 'Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645.'
                },
                'name': 'NIRFSG_VAL_I_ONLY',
                'value': 14003
            }
        ]
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG returns a warning when an OSP overflow occurs.'
                },
                'name': 'NIRFSG_VAL_ERROR_REPORTING_WARNING',
                'value': 1301
            },
            {
                'documentation': {
                    'description': 'NI-RFSG does not return an error or a warning when an OSP overflow occurs.'
                },
                'name': 'NIRFSG_VAL_ERROR_REPORTING_DISABLED',
                'value': 1302
            }
        ]
    },
    'PhaseContinuityEnabled': {
        'values': [
            {
                'documentation': {
                    'description': 'The arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'The arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this attribute could cause waveform size to increase.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'PowerLevelType': {
        'values': [
            {
                'documentation': {
                    'description': 'Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_AVERAGE_POWER',
                'value': 7000
            },
            {
                'documentation': {
                    'description': 'Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR attribute. You can use the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute in conjunction with the NIRFSG_ATTR_POWER_LEVEL attribute when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.'
                },
                'name': 'NIRFSG_VAL_PEAK_POWER',
                'value': 7001
            }
        ]
    },
    'PulseModulationMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842'
                },
                'name': 'NIRFSG_VAL_OPTIMAL_MATCH',
                'value': 20000
            },
            {
                'documentation': {
                    'description': 'Allows for the best on/off power ratio of the pulsed signal.'
                },
                'name': 'NIRFSG_VAL_HIGH_ISOLATION',
                'value': 20001
            },
            {
                'documentation': {
                    'description': 'Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.'
                },
                'name': 'NIRFSG_VAL_ANALOG',
                'value': 20002
            },
            {
                'documentation': {
                    'description': 'Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.'
                },
                'name': 'NIRFSG_VAL_DIGITAL',
                'value': 20003
            }
        ]
    },
    'PulseModulationOutputTerminal': {
        'values': [
            {
                'documentation': {
                    'description': 'Pulse modulation video signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Export the pulse modulation video signal on the pulse out terminal.'
                },
                'name': 'NIRFSG_VAL_PULSE_OUT_STR',
                'value': 'PulseOut'
            }
        ]
    },
    'PulseModulationSource': {
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                },
                'name': 'NIRFSG_VAL_PULSE_IN_STR',
                'python_name': 'PULSE_IN',
                'value': 'PulseIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 0.'
                },
                'name': 'NIRFSG_VAL_MARKER0_STR',
                'python_name': 'MARKER0',
                'value': 'Marker0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 1.'
                },
                'name': 'NIRFSG_VAL_MARKER1_STR',
                'python_name': 'MARKER1',
                'value': 'Marker1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 2.'
                },
                'name': 'NIRFSG_VAL_MARKER2_STR',
                'python_name': 'MARKER2',
                'value': 'Marker2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 3.'
                },
                'name': 'NIRFSG_VAL_MARKER3_STR',
                'python_name': 'MARKER3',
                'value': 'Marker3'
            },
            {
                'documentation': {
                    'description': 'Do not drive pulse modulation.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_DRIVE_SIGNAL',
                'value': ''
            }
        ]
    },
    'RFBlanking': {
        'values': [
            {
                'documentation': {
                    'description': 'RF blanking is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'RF blanking is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'RFInLoExportEnabled': {
        'values': [
            {
                'documentation': {
                    'description': 'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may'
                },
                'name': 'NIRFSG_VAL_UNSPECIFIED',
                'value': -2
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'ReferenceClockExportOutputTerminal': {
        'values': [
            {
                'documentation': {
                    'description': 'The Reference Clock signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the REF OUT connector of the device.'
                },
                'name': 'NIRFSG_VAL_REF_OUT_STR',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.'
                },
                'name': 'NIRFSG_VAL_REF_OUT2_STR',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the CLK OUT connector of the device.'
                },
                'name': 'NIRFSG_VAL_CLK_OUT_STR',
                'value': 'ClkOut'
            }
        ]
    },
    'ReferenceClockSource': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the onboard Reference Clock as the clock source.'
                },
                'name': 'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'Uses the clock signal present at the front panel REF IN connector as the Reference Clock source.'
                },
                'name': 'NIRFSG_VAL_REF_IN_STR',
                'value': 'RefIn'
            },
            {
                'documentation': {
                    'description': 'Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.'
                },
                'name': 'NIRFSG_VAL_PXI_CLK_STR',
                'value': 'PXI_CLK'
            },
            {
                'documentation': {
                    'description': 'Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.'
                },
                'name': 'NIRFSG_VAL_CLK_IN_STR',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'This value is not valid on any supported devices.'
                },
                'name': 'NIRFSG_VAL_REF_IN_2_STR',
                'value': 'RefIn2'
            },
            {
                'documentation': {
                    'description': 'This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653 -** NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use NIRFSG_VAL_PXI_CLK_STR as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                },
                'name': 'NIRFSG_VAL_PXI_CLK_MASTER_STR',
                'value': 'PXI_ClkMaster'
            }
        ]
    },
    'ReferencePllBandwidth': {
        'values': [
            {
                'documentation': {
                    'description': 'Uses the narrowest loop bandwidth setting for the PLL. Setting this attribute to NIRFSG_VAL_NARROW allows the PXIe-5653 to lock to a reference with worse phase noise than the PXIe-5653 and utilize the better phase noise of the PXIe-5653.'
                },
                'name': 'NIRFSG_VAL_NARROW',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses the medium loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_MEDIUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Uses the widest loop bandwidth setting for the PLL. Setting this attribute to NIRFSG_VAL_WIDE on the PXIe-5653 allows the reference PLL to lock to a better reference with better phase noise than the PXIe-5653 and utilize the better phase noise of the reference.'
                },
                'name': 'NIRFSG_VAL_WIDE',
                'value': 2
            }
        ]
    },
    'RelativeTo': {
        'values': [
            {
                'documentation': {
                    'description': 'The reference position is relative to the current position.'
                },
                'name': 'NIRFSG_VAL_CURRENT_POSITION',
                'value': 8001
            },
            {
                'documentation': {
                    'description': 'The reference position is relative to the start of the waveform.'
                },
                'name': 'NIRFSG_VAL_START_OF_WAVEFORM',
                'value': 8000
            }
        ]
    },
    'ResetWithOptionsStepsToOmit': {
        'class': 'IntFlag',
        'values': [
            {
                'documentation': {
                    'description': 'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'No step is omitted during reset.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits clearing scripts.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits clearing waveforms.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS',
                'value': 1
            }
        ]
    },
    'ScriptTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from low level to high level.'
                },
                'name': 'NIRFSG_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from high level to low level.'
                },
                'name': 'NIRFSG_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'ScriptTriggerDigitalLevelActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the digital trigger signal is high.'
                },
                'name': 'NIRFSG_VAL_ACTIVE_HIGH',
                'value': 9000
            },
            {
                'documentation': {
                    'description': 'Trigger when the digital trigger signal is low.'
                },
                'name': 'NIRFSG_VAL_ACTIVE_LOW',
                'value': 9001
            }
        ]
    },
    'ScriptTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured. Signal generation starts immediately.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until the digital level is detected. The source of the digital level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, and the active level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_LEVEL',
                'value': 8000
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software trigger occurs. You can create a software event by calling the nirfsg_SendSoftwareEdgeTrigger function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            }
        ]
    },
    'SelfCalibrateRangeStepsToOmit': {
        'class': 'IntFlag',
        'values': [
            {
                'documentation': {
                    'description': 'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_LO_SELF_CAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'No calibration steps are omitted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_OMIT_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                'value': 16
            }
        ]
    },
    'Signal': {
        'values': [
            {
                'documentation': {
                    'description': 'Exports a Start Trigger.'
                },
                'name': 'NIRFSG_VAL_START_TRIGGER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Exports a Script Trigger.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Exports a Marker Event.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock.'
                },
                'name': 'NIRFSG_VAL_REF_CLOCK',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Exports a Started Event.'
                },
                'name': 'NIRFSG_VAL_STARTED_EVENT',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Exports a Done Event.'
                },
                'name': 'NIRFSG_VAL_DONE_EVENT',
                'value': 5
            }
        ]
    },
    'SoftwareTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Script Trigger.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies the Start Trigger.'
                },
                'name': 'NIRFSG_VAL_START_TRIGGER',
                'value': 0
            }
        ]
    },
    'SparameterOrientation': {
        'values': [
            {
                'documentation': {
                    'description': 'Port 1 of the S2P is oriented towards the DUT port.'
                },
                'name': 'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                'value': 24000
            },
            {
                'documentation': {
                    'description': 'Port 2 of the S2P is oriented towards the DUT port.'
                },
                'name': 'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                'value': 24001
            }
        ]
    },
    'StartTriggerDigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': 'Occurs when the signal transitions from low level to high level.'
                },
                'name': 'NIRFSG_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Occurs when the signal transitions from high level to low level.'
                },
                'name': 'NIRFSG_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'StartTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software event occurs. You may create a software trigger by calling the nirfsg_SendSoftwareEdgeTrigger function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            }
        ]
    },
    'TriggerIdentifier': {
        'values': [
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 0.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER0',
                'value': 'scriptTrigger0'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 1.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER1',
                'value': 'scriptTrigger1'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 2.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER2',
                'value': 'scriptTrigger2'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 3.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER3',
                'value': 'scriptTrigger3'
            },
            {
                'documentation': {
                    'description': 'None (no signal to export)'
                },
                'name': 'NIRFSG_VAL_NONE_EMPTY_STRING',
                'python_name': 'NONE',
                'value': ''
            }
        ]
    },
    'UpconverterFrequencyOffsetMode': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSG returns an error if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG uses the offset that you specified with the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes.'
                },
                'name': 'NIRFSG_VAL_USER_DEFINED',
                'value': 5001
            }
        ]
    },
    'WriteWaveformBurstDetection': {
        'values': [
            {
                'documentation': {
                    'description': 'Burst detection is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Burst detection is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'WriteWaveformBurstDetectionMode': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'User sets the burst detection parameters.'
                },
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            }
        ]
    },
    'WriteWaveformNormalization': {
        'values': [
            {
                'documentation': {
                    'description': 'Disables normalization on the waveform.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'YigMainCoilDrive': {
        'values': [
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil for an underdamped response.'
                },
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil for an overdamped response.'
                },
                'name': 'NIRFSG_VAL_FAST',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nirfsg/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nirfsg/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nirfsg/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````
