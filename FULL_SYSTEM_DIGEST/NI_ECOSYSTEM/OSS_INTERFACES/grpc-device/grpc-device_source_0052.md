# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/attributes.py sha256=9f3b4ec265424957d0e8652e5613ee570282d5aae6d047c22f7611f3933307f6 bytes=140787 -->
## FILE: source/codegen/metadata/nirfsg/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/attributes.py`
- sha256: `9f3b4ec265424957d0e8652e5613ee570282d5aae6d047c22f7611f3933307f6`
- bytes: 140787

````python
attributes = {
    1050002: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to validate attribute values and function  parameters. Range checking parameters is very useful for debugging.  After you validate your program, set this attribute to VI_FALSE to disable  range checking and maximize performance. NI-RFSG can choose to ignore range  checking for particular attributes, regardless of the setting of this attribute.  Use the niRFSG_InitWithOptions function to override the default value. \n \n'
        },
        'name': 'RANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether NI-RFSG queries the NI-RFSG device status  after each operation. Querying the device status is useful  for debugging. After you validate your program, set this attribute  to VI_FALSE to disable status checking and maximize performance.  NI-RFSG can choose to ignore status checking for particular attributes,  regardless of the setting of this attribute. Use the niRFSG_InitWithOptions  function to override the default value. \n \n'
        },
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to cache the value of attributes. When caching is  enabled, NI-RFSG tracks the current NI-RFSG device settings and avoids  sending redundant commands to the device. \n \n NI-RFSG can always cache or never cache particular attributes, regardless  of the setting of this attribute.\n \n'
        },
        'name': 'CACHE',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns whether NI-RFSG simulates I/O operations. This attribute  is useful for debugging applications without using hardware.  After a session is opened, you cannot change the simulation state.  Use the niRFSG_InitWithOptions function to enable simulation.\n \n'
        },
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the IVI engine keeps a list of the value coercions it  makes for integer and real type attributes.\n \n This attribute is currently not supported.\n'
        },
        'name': 'RECORD_COERCIONS',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read-write',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings.\n \n',
            'note': ' This attribute is currently not supported. \n'
        },
        'name': 'INTERCHANGE_CHECK',
        'type': 'ViBoolean'
    },
    1050022: {
        'access': 'read-write',
        'name': 'SPY',
        'type': 'ViBoolean'
    },
    1050023: {
        'access': 'read-write',
        'name': 'USE_SPECIFIC_SIMULATION',
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
            'description': ' Returns a string that contains the prefix for NI-RFSG. The name of each  user-callable function in NI-RFSG starts with this prefix.  This attribute returns niRFSG.\n     '
        },
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the resource name NI-RFSG uses to identify the physical device.  If you initialize NI-RFSG with a logical name, this attribute contains the  resource name that corresponds to the entry in the IVI Configuration  Utility. If you initialize NI-RFSG with the resource name, this attribute  contains that value. \n     '
        },
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the logical name you specified when opening the current IVI session.  You can pass a logical name to the niRFSG_init  function or the niRFSG_InitWithOptions function. The IVI Configuration  Utility must contain an entry for the logical name. The logical name entry  refers to a driver session section in the IVI Configuration file. The  driver session section specifies a physical device and initial user  options.\n     '
        },
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains a model code of the NI-RFSG device.  For drivers that support more than one device,  this attribute contains a comma-separated list of supported devices. \n     '
        },
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains a comma-separated list of class-extension  groups that NI-RFSG implements.\n     '
        },
        'name': 'GROUP_CAPABILITIES',
        'type': 'ViString'
    },
    1050402: {
        'access': 'read-write',
        'name': 'FUNCTION_CAPABILITIES',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the firmware revision information for the  NI-RFSG device you are currently using.\n     '
        },
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the name of the manufacturer for the  NI-RFSG device you are currently using.\n     '
        },
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the model number or name of the NI-RFSG  device that you are currently using. For drivers that support more than  one device, this attribute returns a comma-separated list of  supported devices.\n'
        },
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains the name of the vendor that supplies  NI-RFSG. This attribute returns National Instruments.\n     '
        },
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains a brief description of NI-RFSG.  This attribute returns National Instruments RF Signal Generator Instrument Driver.\n     '
        },
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the major version number of the class specification with which  NI-RFSG is compliant.\n     '
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the minor version number of the class specification with which  NI-RFSG is compliant.\n     '
        },
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string that contains additional version information about  NI-RFSG. For example, NI-RFSG can return Driver: NI-RFSG 14.5.0,  Compiler: MSVC 9.00, Components: IVI Engine 4.00, VISA-Spec 4.00.\n     '
        },
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Reference Clock source. To set this attribute, the NI-RFSG  device must be in the Configuration state. Only certain combinations  of this attribute and the NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE  attribute are valid\n \n backplane clock on PXI chassis only using the  NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE attribute. \n \n  ',
            'note': ' PXI-5670/5671 and PXIe-5672 devices also allow you to drive the PXI 10 MHz '
        },
        'enum': 'RefClockSource',
        'name': 'REF_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150002: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Start Trigger. This attribute is  used when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_EDGE. This attribute is not case-sensitive. To set the  NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, the NI-RFSG device  must be in the Configuration state.\n \n'
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150003: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Start Trigger.  To set this attribute, the NI-RFSG device must be in the Configuration  state.\n \n'
        },
        'enum': 'AnySignalOutputTerm',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the clock source for driving the PXI 10 MHz backplane Reference  Clock. This attribute is configurable if the PXI-5610 upconverter  module is installed in only Slot 2 of a PXI chassis. To set this attribute, the  NI-RFSG device must be in the Configuration state.\n'
        },
        'enum': 'PXIChassisClk10',
        'name': 'PXI_CHASSIS_CLK10_SOURCE',
        'type': 'ViString'
    },
    1150005: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the driver maintains phase continuity in the  arbitrary waveforms. When this attribute is set to  NIRFSG_VAL_ENABLE, NI-RFSG may increase the waveform size. When  this attribute is set to NIRFSG_VAL_ENABLE, the  NIRFSG_ATTR_FREQUENCY_TOLERANCE attribute specifies the maximum  allowable frequency error that can be introduced when keeping the  signal phase-continuous. To set the NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED  attribute, the NI-RFSG device must be in the Configuration state.  NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED applies only when the  NIRFSG_ATTR_GENERATION_MODE attribute is set to  NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT. \n \n On the PXI-5671: When using the PXI-5671 with I/Q rates less than or equal  to 8.33 MS/s, an input phase-continuous signal is always phase-continuous  upon output, and this attribute has no effect. \n \n PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5840/5841: Phase continuity is always enabled on this device. \n \n'
        },
        'enum': 'PhaseContinuity',
        'name': 'PHASE_CONTINUITY_ENABLED',
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum frequency error allowed during the software  upconversion process. NI-RFSG may introduce a frequency error up to the  specified amount in order to optimize computational speed and onboard  memory usage while upconverting phase-continuous signals. \n \n If the NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED attribute is set to  NIRFSG_VAL_DISABLE, the NIRFSG_ATTR_FREQUENCY_TOLERANCE attribute is  ignored, and the driver does not introduce a frequency error. On devices  that do not use software upconversion, this attribute is ignored. The  PXI-5670 always uses software upconversion, and the PXI-5671 uses software  upconversion for I/Q rates greater than 8.33 MS/s. \n \n To set the  NIRFSG_ATTR_FREQUENCY_TOLERANCE attribute, the NI-RFSG device must be in  the Configuration state.\n \n Units: hertz (Hz) \n \n'
        },
        'name': 'FREQUENCY_TOLERANCE',
        'type': 'ViReal64'
    },
    1150007: {
        'access': 'read-write',
        'documentation': {
            'description': " Specifies the bandwidth of the arbitrary signal. \n \n This value must be less than or equal to (0.8 * I/Q rate). \n \n NI-RFSG defines signal bandwidth as twice the maximum baseband signal deviation  from 0 Hz. Usually, the baseband signal center frequency is 0 Hz.  In such cases, the signal bandwidth is simply the baseband signal's minimum frequency  subtracted from its maximum frequency. \n \n This attribute applies only when the NIRFSG_ATTR_GENERATION_MODE attribute  is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT,  except for when using the PXIe-5840/5841, which supports setting this attribute  in all supported generation modes. To set the NIRFSG_ATTR_SIGNAL_BANDWIDTH  attribute, the NI-RFSG device must be in the Configuration state. \n \n PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to  configure the upconverter center frequency in increments of 1 MHz or 5 MHz.  Failure to configure this attribute may result in the signal being placed outside  the upconverter passband. \n \n PXIe-5644/5645/5646, PXIe-5673/5673E: This attribute is used only for  error-checking purposes. Otherwise, this attribute is ignored. \n \n PXIe-5820/5830/5831/5840/5841: Based on your signal bandwidth, NI-RFSG decides the  equalized bandwidth. If this attribute is not set, NI-RFSG uses  the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal  bandwidth depends on the upconverter center frequency. Refer to the  specifications document for your device for more information about signal  bandwidth. The device specifications depend on the signal bandwidth. \n Units: hertz (Hz) \n \n"
        },
        'name': 'SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150008: {
        'access': 'read only',
        'documentation': {
            'description': ' Enables or disables automatic thermal correction. When enabled, changes to  settings cause NI-RFSG to check whether the device temperature has changed  and adjustd the settings as needed.When disabled, you must explicitly call  the niRFSG_PerformThermalCorrection function to adjust the device for  temperature changes. \n \n  '
        },
        'name': 'AUTOMATIC_THERMAL_CORRECTION',
        'type': 'ViInt32'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether attenuator hold is enabled. While this attribute is  set to VI_TRUE, changing the power level causes NI-RFSG to scale the  digital data sent to the AWG instead of adjusting the attenuators.  Changing power levels in this manner allows the device to increase or  decrease the power level in more accurate increments, but it may affect  signal-to-noise ratios (noise density).\n \n Setting this attribute to VI_TRUE limits the power levels that can be  attained. With attenuator hold enabled, the power level must satisfy the  following conditions:\n \n - Power level <= the maximum power level set with the  NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER attribute \n - Power level >= (the maximum power level set with  the  NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER attribute -70 dB)\n - Power level >= -145 dBm\n \n To set this attribute, the NI-RFSG device must be in the Configuration  state.\n \n'
        },
        'name': 'ATTENUATOR_HOLD_ENABLED',
        'type': 'ViBoolean'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum power level of the RF output signal whenthe  NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED attribute is set to VI_TRUE.\n \n To set this attribute, the NI-RFSG device must be in the Configuration  state.\n \n Units: dBm \n'
        },
        'name': 'ATTENUATOR_HOLD_MAX_POWER',
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read only',
        'documentation': {
            'description': ' Specifies the maximum instantaneous power of the current RF output signal.   \n attribute is set to NIRFSG_VAL_AVERAGE_POWER. \n  \n Units: dBm \n  \n',
            'note': ' This attribute is valid only when the NIRFSG_ATTR_POWER_LEVEL_TYPE '
        },
        'name': 'PEAK_ENVELOPE_POWER',
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': ' When this attribute is enabled, NI-RFSG equalizes the waveform  data to correct for variations in the response of the NI-RFSG device.  Enabling digital equalization improves  the modulation error rates (MER) and error vector magnitude (EVM) for  signals with large bandwidths (> 500 kHz). On the PXI-5670/5671, this  equalization is performed in the software so that tuning time is  increased. On the PXIe-5672, this is performed in the hardware so that it  has no performance penalties.\n \n This attribute only applies when the NIRFSG_ATTR_GENERATION_MODE attribute  is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT. To set this  attribute, the NI-RFSG device must be in the Configuration state.\n \n PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841: NIRFSG_VAL_ENABLE is the only supported value for this device.\n \n'
        },
        'enum': 'EnableValues',
        'name': 'DIGITAL_EQUALIZATION_ENABLED',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the local oscillator signal is present at the front  panel LO Out connector.\n The local oscillator signal remains at the LO OUT front panel connector  until this attribute is set to VI_FALSE even if the  NIRFSG_ATTR_OUTPUT_ENABLED attribute is set to VI FALSE,  the niRFSG_Abort function is called, or the NI-RFSG sesssion is closed.  To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViBoolean function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n'
        },
        'name': 'LO_OUT_ENABLED',
        'type': 'ViBoolean'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables warnings or errors when you set the frequency, power, or bandwidth values beyond the limits  of the NI-RFSG device specifications. When you enable the NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS attribute,  the driver does not report out-of-specification warnings or errors. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n \n',
            'note': ' Accuracy cannot be guaranteed outside of device specifications, and results may vary by unit. \n'
        },
        'name': 'ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'documentation': {
            'description': ' Indicates the carrier frequency generated by the arbitrary waveform  generator (AWG) module. The specified carrier frequency is related  to the RF output as shown in the following equations: \n \n PXI-5610, PXI-5670/5671, PXIe-5672 \n RF Frequency (MHz) = Upconverter Center Frequency + Arb Carrier Frequency - 25 MHz \n \n PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5840/5841 \n RF Frequency (MHz) = Upconverter Center Frequency + Arb Carrier Frequency \n \n and the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute cannot be set at the same time.  The only time the carrier frequency is nonzero on the PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5840/5841 is when in-band retuning is used.  \n \n Units: Hz \n \n',
            'note': ' This attribute is read-only on the PXI-5670/5671, PXIe-5672. \n'
        },
        'name': 'ARB_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150016: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates the average output power from the PXI-5421, PXI-5441, PXIe-5442, and PXIe-5450  AWG module. If an arbitrary waveform is being generated, this  attribute specifies either the average power or the peak power of the  signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE  attribute setting. \n \n  Units: dBm \n \n'
        },
        'name': 'ARB_POWER',
        'type': 'ViReal64'
    },
    1150017: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the device temperature. If the NI-RFSG session is controlling  multiple devices, this attribute returns the temperature of the primary  NI RF device.  The NI-RFSG session is opened using the primary RF device name. \n \n Serial signals between the sensor and the system control unit could  modulate the signal being generated, thus causing phase spurs. After the device  thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius)  and slowly, and it is not necessary to constantly poll this temperature sensor.  Refer to the thermal management topic appropriate to your device in the  NI RF Signal Generators Help for more information about device temperature. \n PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this attribute during RF  list mode, list steps may take longer to complete during list execution. \n PXIe-5830/5831: To use this attribute, you must first set the channelName parameter of the niRFSG_SetAttributeViReal64 function  to using the appropriate string for your instrument configuration. Refer to the NI-RFSG C Function Reference for more information about  the applicable string to use for your instrument configuration. \n\n Units: desgrees Celsius (°C) \n \n'
        },
        'name': 'DEVICE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to generate a continuous wave (CW) signal, the arb  waveform specified by the NIRFSG_ATTR_SELECTED_WAVEFORM attribute, or the  script specified by the NIRFSG_ATTR_SELECTED_SCRIPT attribute, upon  calling the niRFSG_Initiate function. \n  '
        },
        'enum': 'GenerationMode',
        'name': 'GENERATION_MODE',
        'type': 'ViInt32'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Script Trigger type. Depending upon the value of this  attribute, more attributes may be needed to fully configure the trigger.  To set this attribute, the NI-RFSG device must be in the Configuration  state.\n \n'
        },
        'enum': 'ScriptTriggerType',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150020: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Script Trigger. This attribute is  used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_EDGE. This attribute is not case-sensitive. To set this  attribute, the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150021: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active edge for the Script Trigger. This attribute is used  when NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE is set to NIRFSG_VAL_DIGITAL_EDGE. To  set the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute,  the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'enum': 'DigitalEdgeEdge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Script Trigger. To  set this attribute, the NI-RFSG device must be in the Configuration state.  For trigger delay information, refer to the triggering section in the NI  RF Signal Generators Help. \n \n'
        },
        'enum': 'AnySignalOutputTerm',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the script in onboard memory to generate upon calling the  niRFSG_Initiate function when NIRFSG_ATTR_GENERATION_MODE is set to  NIRFSG_VAL_SCRIPT.  \n \n The NIRFSG_ATTR_SELECTED_SCRIPT attribute is ignored  when the NIRFSG_ATTR_GENERATION_MODE attribute is set to  NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_CW. To set the  NIRFSG_ATTR_SELECTED_SCRIPT attribute, the NI-RFSG device must be in the  Configuration state.\n'
        },
        'name': 'SELECTED_SCRIPT',
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the phase of the RF output signal. Use this attribute  to align the phase of the RF output with the phase of the RF output of  another device, as long as the two devices are phase-coherent. \n \n Units: degrees (º) \n \n'
        },
        'name': 'PHASE_OFFSET',
        'type': 'ViReal64'
    },
    1150025: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the AWG prefilter gain. The prefilter gain is  applied to the waveform data before any other signal processing.  Reduce this value to prevent overflow in the AWG interpolation filters.  Other gains on the NI-RFSG device are automatically adjusted to  compensate for nonunity AWG prefilter gain. The PXI-5671 and  the PXIe-5672 must be in the Configuration state to use this attribute.  However, the PXIe5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5840/5841 can be in either the Configuration  or the Generation state to use this attribute. \n \n On the PXI-5671, this attribute applies only when the  NIRFSG_ATTR_IQ_RATE attribute is set to a value  less than or equal to 8.33 MS/s. On the PXIe-5644/5645/5646,  PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5840/5841, this attribute is always applicable.\n \n Units: dB \n \n'
        },
        'name': 'ARB_PRE_FILTER_GAIN',
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the serial number of the RF module.\n'
        },
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150027: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the loop bandwidth of the tuning PLLs. This attribute is ignored on the  PXI-5610, PXI-5670/5671, PXIe-5672 for signal bandwidths greater than or equal to 10 MHz.  This attribute is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50 MHz. \n \n PXIe-5644/5645/5646/5650/5651/5652/5673/5673E allows the frequency to settle  significantly faster at the expense of increased phase noise.  Setting this attribute to NIRFSG_VAL_MEDIUM is not a valid  option on the PXI/PXIe-5650/5651/5652, PXIe-5673/5673E. NIRFSG_VAL_MEDIUM is the only  supported value for the PXIe-5830/5831/5840/5841. \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n',
            'note': ' Setting this attribute to NIRFSG_VAL_WIDE on the '
        },
        'enum': 'LoopBandwidth',
        'name': 'LOOP_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Sample Clock mode on the device.  To set this attribute, the device must be in the Configuration state. \n \n PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841: NIRFSG_VAL_DIVIDE_DOWN is the only supported value for this device. \n \n',
            'note': ' Using the high resolution clock may result in increased phase noise. /n'
        },
        'enum': 'ArbOnboardSampleClockMode',
        'name': 'ARB_ONBOARD_SAMPLE_CLOCK_MODE',
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Sample Clock source for the device.  To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841: NIRFSG_VAL_ONBOARD_CLK_STR is the only supported value for this device. \n \n'
        },
        'enum': 'ArbSampleClockSource',
        'name': 'ARB_SAMPLE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    1150031: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the rate of the Sample Clock on the device. \n \n Units: hertz (Hz) \n \n'
        },
        'name': 'ARB_SAMPLE_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the analog modulation format to use. \n \n'
        },
        'enum': 'AnalogModulationType',
        'name': 'ANALOG_MODULATION_TYPE',
        'type': 'ViInt32'
    },
    1150033: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the type of waveform to use as the message signal for analog  modulation. \n \n'
        },
        'enum': 'AnalogModulationWaveformType',
        'name': 'ANALOG_MODULATION_WAVEFORM_TYPE',
        'type': 'ViInt32'
    },
    1150034: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the waveform to use as the message signal in  analog modulation. \n Units: hertz (Hz) \n \n  '
        },
        'name': 'ANALOG_MODULATION_WAVEFORM_FREQUENCY',
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency deviation to use in frequency modulation. \n'
        },
        'name': 'ANALOG_MODULATION_FM_DEVIATION',
        'type': 'ViReal64'
    },
    1150036: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the digital modulation format to use.\n \n'
        },
        'enum': 'DigitalModulationType',
        'name': 'DIGITAL_MODULATION_TYPE',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the symbol rate of the bit stream for FSK modulation.\n'
        },
        'name': 'DIGITAL_MODULATION_SYMBOL_RATE',
        'type': 'ViReal64'
    },
    1150038: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the type of waveform to use as the message signal in digital  modulation.\n \n'
        },
        'enum': 'DigitalModulationWaveformType',
        'name': 'DIGITAL_MODULATION_WAVEFORM_TYPE',
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the order of the pseudorandom bit sequence (PRBS)  sequence internally generated by hardware  and used as the message signal in digital modulation. \n'
        },
        'name': 'DIGITAL_MODULATION_PRBS_ORDER',
        'type': 'ViInt32'
    },
    1150040: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the seed of the internally generated  pseudorandom bit sequence (PRBS) sequence.\n'
        },
        'name': 'DIGITAL_MODULATION_PRBS_SEED',
        'type': 'ViInt32'
    },
    1150041: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the deviation to use in FSK modulation. \n'
        },
        'name': 'DIGITAL_MODULATION_FSK_DEVIATION',
        'type': 'ViReal64'
    },
    1150042: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the niRFSG_WriteArbWaveform function writes waveforms  immediately to the device or copies the waveform to host memory for  download later. NI-RFSG reads and validates this attribute when an  arbitrary waveform is first allocated.\n \n PXI-5670: Direct download is always disabled. \n \n PXI-5671: To increase performance when using large waveforms,  enable direct download.  To maximize reconfigurability, disable direct  download.\n \n  Perform the following steps to enable direct download:\n -Set the IQ rate to less than or equal to 8.33 MS/s with the  NIRFSG_ATTR_IQ_RATE attribute. \n -Set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER. \n -Disable the NIRFSG_ATTR_IQ_SWAP_ENABLED attribute. \n -Disable the NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED attribute. \n \n PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5840/5841: Direct download is always enabled. \n \n  '
        },
        'enum': 'EnableValues',
        'name': 'DIRECT_DOWNLOAD',
        'type': 'ViInt32'
    },
    1150043: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies how NI-RFSG interprets the value of the  NIRFSG_ATTR_POWER_LEVEL attribute.  The NIRFSG_ATTR_POWER_LEVEL_TYPE  attribute also affects how waveforms are scaled.\n \n PXI-5670/5671: While in Script generation mode, if this attribute is set to NIRFSG_VAL_AVERAGE_POWER,  NI-RFSG scales each waveform so that all waveforms have the same average power.  The average power level of each waveform matches the value set with the NIRFSG_ATTR_POWER_LEVEL attribute.  You can disable this scaling operation by setting the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to NIRFSG_VAL_PEAK_POWER.\n \n PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5840/5841: While in Script generation mode, this attribute must be set to NIRFSG_VAL_PEAK_POWER. \n \n'
        },
        'enum': 'PowerLevelType',
        'name': 'POWER_LEVEL_TYPE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables digital pattern on the PXI-5421/5441 AWG module. This  attribute must be set to VI_TRUE to enable signal routing to and from the  Digital Data &amp; Control connector. To set this attribute, the NI-RFSG  device must be in the Configuration state.\n \n'
        },
        'name': 'DIGITAL_PATTERN',
        'type': 'ViBoolean'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables streaming of waveform data.\n \n'
        },
        'name': 'STREAMING_ENABLED',
        'type': 'ViBoolean'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the name of the waveform used to continuously stream data during  generation.\n \n'
        },
        'name': 'STREAMING_WAVEFORM_NAME',
        'type': 'ViString'
    },
    1150047: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates the space available, in samples, in the streaming  waveform for writing new data. For optimal performance, write  new data to the waveform in a fixed size that is an integer  divisor of the total size of the streaming waveform.  This waveform size ensures that writes do not have to wrap  around from the end to the beginning of the waveform buffer. \n \n To read this attribute, the NI-RFSG device must be in  the Committed state. \n  \n Units: Samples \n \n  '
        },
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'type': 'ViInt64'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': ' Indicates the number of samples download to onboard memory at one time. This  attribute is useful when the total data to be transferred to onboard  memory is large. \n Units: Samples \n \n'
        },
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'type': 'ViInt32'
    },
    1150052: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies how much to scale the data before writing it with the  niRFSG_WriteArbWaveform function. The resulting waveform must be  smaller than 1.0 in complex magnitude. This attribute is supported only  if you set the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute to  NIRFSG_VAL_PEAK_POWER. \n \n'
        },
        'name': 'ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR',
        'type': 'ViReal64'
    },
    1150053: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Reference Clock on  the NI RF signal generators. To set this attribute,  the NI-RFSG device must be in the Configuration state. \n'
        },
        'enum': 'RefClockOutputTerm',
        'name': 'EXPORTED_REF_CLOCK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150054: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Script Trigger. This attribute is  used when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_LEVEL. This attribute is not case-sensitive. To set  the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute,  the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'enum': 'TriggerSource',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active level for the Script Trigger. This attribute is used  when the NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_LEVEL. \n \n'
        },
        'enum': 'DigitalLevelActiveLevel',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150056: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse-shaping filter type for the FIR filter. You can use this attribute  only with signal generators that support onboard signal processing (OSP).  NI-RFSG returns an error if you use this attribute with a device that  does not support OSP. \n'
        },
        'enum': 'ArbFilterType',
        'name': 'ARB_FILTER_TYPE',
        'type': 'ViInt32'
    },
    1150057: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients.  You can use this attribute when the NIRFSG_ATTR_ARB_FILTER_TYPE  attribute is set to NIRFSG_VAL_ARB_ROOT_RAISED_COSINE and with signal  generators that support onboard signal processing (OSP).  NI-RFSG returns an error if you use this attribute with a device  that does not support OSP. \n'
        },
        'name': 'ARB_FILTER_ROOT_RAISED_COSINE_ALPHA',
        'type': 'ViReal64'
    },
    1150058: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which upconverter center frequencies are used. This attribute  can be used to increase the speed of frequency sweeps by reducing the  number of times the upconverter is retuned. \n This attribute is obsolete and should not be used. \n \n  '
        },
        'name': 'UPCONVERTER_CENTER_FREQUENCY_INCREMENT',
        'type': 'ViReal64'
    },
    1150059: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the reference point for the upconverter center frequencies to  use.This attribute can be used to speed up frequency sweeps by reducing  the number of times the upconverter is retuned. \n This attribute is obsolete and should not be used. \n \n  '
        },
        'name': 'UPCONVERTER_CENTER_FREQUENCY_INCREMENT_ANCHOR',
        'type': 'ViReal64'
    },
    1150060: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the alpha value to use when calculating the pulse-shaping filter coefficients.  You can use this attribute when the NIRFSG_ATTR_ARB_FILTER_TYPE  attribute is set to NIRFSG_VAL_ARB_RAISED_COSINE and with signal  generators that support onboard signal processing (OSP).  NI-RFSG returns an error if you use this attribute with a device  that does not support OSP. \n \n'
        },
        'name': 'ARB_FILTER_RAISED_COSINE_ALPHA',
        'type': 'ViReal64'
    },
    1150061: {
        'access': 'read only',
        'documentation': {
            'description': ' The total amount of memory on the signal generator in bytes. \n \n of onboard memory stores scripts that specify how the waveforms are  generated. These scripts typically require less than 1 KB of  onboard memory. \n',
            'note': ' Not all onboard memory can be used for waveform storage. A portion '
        },
        'name': 'MEMORY_SIZE',
        'type': 'ViInt64'
    },
    1150062: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the deviation to use in phase modulation, in degrees. \n'
        },
        'name': 'ANALOG_MODULATION_PM_DEVIATION',
        'type': 'ViReal64'
    },
    1150063: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Done event. To set  this attribute, the NI-RFSG device must be in the Configuration state.\n'
        },
        'enum': 'AnySignalOutputTerm',
        'name': 'EXPORTED_DONE_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150064: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the marker event. To set  this attribute, the NI-RFSG device must be in the Configuration state.\n'
        },
        'enum': 'AnySignalOutputTerm',
        'name': 'EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150065: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the started event. To set  this attribute, the NI-RFSG device must be in the Configuration state.\n'
        },
        'enum': 'AnySignalOutputTerm',
        'name': 'EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150066: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the power level of the signal at the LO OUT front panel connector. \n For the PXIe-5644/5645/5646/5673/5673E, this attribute is always read-only. \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n Units: dBm \n \n'
        },
        'name': 'LO_OUT_POWER',
        'type': 'ViReal64'
    },
    1150067: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the power level of the signal at the front panel LO IN  connector. \n \n Otherwise, this attribute is read-only. \n \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n Units: dBm \n \n',
            'note': ' For the PXIe-5644/5645/5646, this attribute is always read-only. \n'
        },
        'name': 'LO_IN_POWER',
        'type': 'ViReal64'
    },
    1150068: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the AWG module temperature in degrees Celsius. \n PXIe-5820/5840/5841: If you query this attribute during RF list mode, list steps may  take longer to complete during list execution. \n \n Units: degrees Celsius (°C) \n \n'
        },
        'name': 'ARB_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables/disables I/Q impairment.  The NIRFSG_ATTR_IQ_I_OFFSET,  NIRFSG_ATTR_IQ_Q_OFFSET, NIRFSG_ATTR_IQ_GAIN_IMBALANCE, and  NIRFSG_ATTR_IQ_SKEW attributes are ignored when the  NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED attribute is disabled. \n \n  '
        },
        'name': 'IQ_IMPAIRMENT_ENABLED',
        'type': 'ViBoolean'
    },
    1150070: {
        'access': 'read-write',
        'documentation': {
            'description': ' When using a National Instruments AWG module or vector  signal transceiver (VST), this attribute specifies the  I-signal DC offset. Units are either percent or volts,  depending on the NIRFSG_ATTR_OFFSET_UNITS attribute setting. \n \n PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q  modulator offset correction plus the value specified by this attribute.  When using an external AWG, this attribute is read-only  and indicates the I/Q modulator I-offset.  Units are volts, as indicated  by the NIRFSG_ATTR_OFFSET_UNITS attribute. \n \n'
        },
        'name': 'IQ_I_OFFSET',
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': ' When using a National Instruments AWG or VST device, this attribute  specifies the Q-signal DC offset. Units are either percent or volts,  depending on the NIRFSG_ATTR_OFFSET_UNITS attribute. \n \n PXIe-5673/5673E: Actual AWG signal offset is equal to the  I/Q modulator offset correction plus the value specified by this  attribute. When using an external AWG (non-National Instruments AWG),  this attribute is read-only, and indicates the IQ modulator Q offset.  Units are volts, as indicated by the NIRFSG_ATTR_OFFSET_UNITS attribute. \n \n'
        },
        'name': 'IQ_Q_OFFSET',
        'type': 'ViReal64'
    },
    1150072: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the gain imbalance of the I/Q modulator (I versus Q). \n \n Units: dB \n \n'
        },
        'name': 'IQ_GAIN_IMBALANCE',
        'type': 'ViReal64'
    },
    1150073: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the adjustment of the phase angle between the I and Q vectors.  If this skew is zero, the phase angle is 90 degrees. \n'
        },
        'name': 'IQ_SKEW',
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the LO module temperature in degrees Celsius. \n PXIe-5840/5841: If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n \n Units: degrees Celsius (°C) \n \n'
        },
        'name': 'LO_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150076: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the recommended interval between each external calibration of the device. \n \n Units: months \n'
        },
        'name': 'EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL',
        'type': 'ViInt32'
    },
    1150077: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates in degrees Celsius the temperature of the device at the time of  the last external calibration. \n'
        },
        'name': 'EXTERNAL_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150078: {
        'access': 'read only',
        'documentation': {
            'description': ' Specifies a string that contains arbitrary, user-defined information that  is stored with external calibration. \n This attribute is obsolete and should not be used. \n  '
        },
        'name': 'EXTERNAL_CALIBRATION_USER_DEFINED_INFO',
        'type': 'ViString'
    },
    1150079: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the maximum string length for the  NIRFSG_ATTR_EXTERNAL_CALIBRATION_USER_DEFINED_INFO attribute. \n This attribute is obsolete and should not be used. \n  '
        },
        'name': 'EXTERNAL_CALIBRATION_USER_DEFINED_INFO_MAX_SIZE',
        'type': 'ViInt32'
    },
    1150081: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the units of the NIRFSG_ATTR_IQ_I_OFFSET attribute and the  NIRFSG_ATTR_IQ_Q_OFFSET attribute.  Offset units are either percent or  volts.\n \n'
        },
        'enum': 'IqOffsetUnits',
        'name': 'IQ_OFFSET_UNITS',
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the interpretation of the value passed to the  NIRFSG_ATTR_FREQUENCY_SETTLING attribute. \n \n'
        },
        'enum': 'FrequencySettlingUnits',
        'name': 'FREQUENCY_SETTLING_UNITS',
        'type': 'ViInt32'
    },
    1150083: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the frequency settling time.  Interpretation of this value  depends on the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute. \n \n'
        },
        'name': 'FREQUENCY_SETTLING',
        'type': 'ViReal64'
    },
    1150084: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the module revision letter.  If the NI-RFSG session is controlling multiple devices, this returns the module revision letter of the primary RF device.  The NI-RFSG session is  opened using the primary RF device name.\n'
        },
        'name': 'MODULE_REVISION',
        'type': 'ViString'
    },
    1150085: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the external amplification or attenuation, if any, between  the RF signal generator and the device under test.  \n Positive values for this attribute represent amplification, and  negative values for this attribute represent attenuation. \n power to compensate for any amplification or attenuation between  the RF signal generator and the device under test. \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n'
        },
        'name': 'EXTERNAL_GAIN',
        'type': 'ViReal64'
    },
    1150086: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum amount of bus bandwidth to use for data transfers. \n'
        },
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the preferred size of the data field in a PCI Express read request packet. \n'
        },
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'type': 'ViInt32'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the maximum number of concurrent PCI Express read requests the RF signal generator can issue. \n'
        },
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'type': 'ViInt32'
    },
    1150089: {
        'access': 'read-write',
        'documentation': {
            'description': " Specifies the oscillator phase digital-to-analog converter (DAC) value  on the arbitrary waveform generator (AWG).  Use this attribute to reduce  the trigger jitter when synchronizing multiple devices with NI-TClk.  This attribute can also help maintain synchronization repeatability  by writing a previous measurement's phase DAC value to the current session.  This attribute is applicable only when using the  NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE attribute set to NIRFSG_VAL_CLK_IN_STR. /n"
        },
        'name': 'ARB_OSCILLATOR_PHASE_DAC_VALUE',
        'type': 'ViInt32'
    },
    1150096: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the name of the configuration list to make active.  When you get or set  an attribute and it is in the configuration list configuration,  the attribute is set to or read from the active list step of the  active configuration list. \n \n If the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set  to &quot;&quot; (empty string), no list is active. \n \n the NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS attribute supports only NIRFSG_VAL_TIME_AFTER_IO as a valid value. \n',
            'note': ' For the PXI/PXIe-5650/5651/5652, PXIe-5673E, when this attribute is set to a valid list name, '
        },
        'name': 'ACTIVE_CONFIGURATION_LIST',
        'type': 'ViString'
    },
    1150097: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step in the configuration list for RF list mode  that you want to make active for configuration or initiation. \n'
        },
        'name': 'ACTIVE_CONFIGURATION_LIST_STEP',
        'type': 'ViInt32'
    },
    1150098: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the type of trigger to use as the Configuration List Step Trigger.  To set this attribute, the NI-RFSG device must be in the  Configuration state. \n'
        },
        'enum': 'ListStepTriggerType',
        'name': 'CONFIGURATION_LIST_STEP_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1150099: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source terminal for the Configuration List Step trigger.  This attribute is valid only when the  NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_EDGE. \n'
        },
        'enum': 'ConfigListTrigSource',
        'name': 'DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE',
        'type': 'ViString'
    },
    1150100: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the time, in seconds, before the timer emits an event  after the task is started and specifies the time interval  between Timer events after the first event.  If you do not set this attribute, the timer is disabled. \n',
            'note': ' For the PXIe-5820/5840/5841, this attribute must be set for the timer to start. '
        },
        'name': 'TIMER_EVENT_INTERVAL',
        'type': 'ViReal64'
    },
    1150102: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the configuration list runs only once or continuously.\n'
        },
        'enum': 'ConfigurationListRepeat',
        'name': 'CONFIGURATION_LIST_REPEAT',
        'type': 'ViInt32'
    },
    1150103: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active edge for the Configuration List Step  trigger.  This attribute is valid only when the  NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE attribute  is set to NIRFSG_VAL_DIGITAL_EDGE. To set this attribute, the NI-RFSG  device must be in the Configuration state. \n'
        },
        'enum': 'ConfigListTriggerDigEdgeEdge',
        'name': 'DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE',
        'type': 'ViInt32'
    },
    1150104: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the temperature, in degrees Celsius, to use for adjusting the device settings  to correct for temperature changes. If you set this attribute, NI-RFSG uses the value  you specify and therefore no longer uses the actual device temperature as the correction  temperature. If you do not set this attribute, NI-RFSG checks the current device temperature  in the Committed state and automatically sets the value of this attribute.\n \n to be used every time, regardless of the temperature variation. In these cases,  it is good to ensure that the temperature does not vary too much. \n \n PXIe-5820/5830/5831/5840/5841: This attribute is read only. \n \n Units: degrees Celsius (°C) \n \n',
            'note': ' Use this attribute only when your application requires the same settings '
        },
        'name': 'CORRECTION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Configuration List Step trigger.  To set this attribute, the NI-RFSG device must be in the Configuration state. \n'
        },
        'enum': 'ConfigListTrigOutputTerm',
        'name': 'EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150112: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string. \n \n'
        },
        'name': 'STARTED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150113: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string. \n'
        },
        'name': 'DONE_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150114: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string.\n \n'
        },
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150115: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string. \n \n'
        },
        'name': 'MARKER_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150116: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string.\n \n'
        },
        'name': 'SCRIPT_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150117: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the fully qualified signal name as a string. \n'
        },
        'name': 'CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150118: {
        'access': 'read-write',
        'documentation': {
            'description': ' Adjusts the dynamics of the current driving the YIG main coil.\n \n allows the frequency to settle significantly faster for some frequency  transitions at the expense of increased phase noise. \n \n',
            'note': ' Setting this attribute to NIRFSG_VAL_FAST on the PXIe-5653 '
        },
        'enum': 'YigMainCoil',
        'name': 'YIG_MAIN_COIL_DRIVE',
        'type': 'ViInt32'
    },
    1150122: {
        'access': 'read only',
        'documentation': {
            'description': ' Specifies the configuration list step that is currently programmed to the hardware.  The list is zero-indexed. You can query this attribute only when a list is executed. \n'
        },
        'name': 'CONFIGURATION_LIST_STEP_IN_PROGRESS',
        'type': 'ViInt64'
    },
    1150123: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device reads data from the peer-to-peer  endpoint.  This attribute is endpoint-based. \n  \n'
        },
        'name': 'P2P_ENABLED',
        'type': 'ViBoolean'
    },
    1150124: {
        'access': 'read only',
        'documentation': {
            'description': " Returns the size, in samples, of the device's endpoint.  This attribute is endpoint-based. \n \n"
        },
        'name': 'P2P_ENDPOINT_SIZE',
        'type': 'ViInt64'
    },
    1150125: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the current space available in the endpoint. You can use this  attribute when priming the endpoint with initial data using the  niRFSG_WriteP2PEndpointI16 function to determine how many samples  you can write. You also can use this attribute to characterize the  performance and measure the latency of the peer-to-peer stream as data  moves across the bus. This attribute is endpoint-based. \n \n Units: samples per channel \n \n'
        },
        'name': 'P2P_SPACE_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150126: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the largest number of samples per channel available in the endpoint since  this attribute was last read. You can use this attribute to determine how much  endpoint space to use as a buffer against bus traffic latencies by reading  the attribute and keeping track of the largest value returned.  This attribute is endpoint-based. \n \n If you want to minimize the latency for data to move through the endpoint  and be generated by the RF signal generator, use the  NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS attribute to grant  fewer initial credits than the default of the entire endpoint size. \n \n Units: samples per channel \n'
        },
        'name': 'P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT',
        'type': 'ViInt64'
    },
    1150127: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the number of peer-to-peer FIFO endpoints supported by the device. \n  \n'
        },
        'name': 'P2P_ENDPOINT_COUNT',
        'type': 'ViInt32'
    },
    1150128: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the number of samples needed to be received by the endpoint before  the device starts generation. This attribute applies only when the  NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_P2P_ENDPOINT_FULLNESS.\n \n Default Value: -1, which allows NI-RFSG to select the appropriate fullness level. \n'
        },
        'name': 'P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL',
        'type': 'ViInt64'
    },
    1150129: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Configuration Settled event. To set  this attribute, the NI-RFSG device must be in the Configuration state.\n'
        },
        'enum': 'ConfigSettledEventOutputTerm',
        'name': 'EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150132: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the adjustment for the NIRFSG_ATTR_POWER_LEVEL attribute.  The value of the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute adds  to the NIRFSG_ATTR_POWER_LEVEL attribute. The NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT  attribute typically specifies the peak-to-average power ratio (PAPR) of  a waveform. If the PAPR is specified, the specified power level becomes  the average power level of the waveform, even if the  NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER. \n \n Refer to the Assigning Properties or Attributes to a Waveform topic of the  NI RF Signal Generators Help for more information. \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n'
        },
        'name': 'PEAK_POWER_ADJUSTMENT',
        'type': 'ViReal64'
    },
    1150133: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the loop bandwidth of the reference PLL.\n \n'
        },
        'enum': 'LoopBandwidth',
        'name': 'REF_PLL_BANDWIDTH',
        'type': 'ViInt32'
    },
    1150134: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the interval at which the RF signal generator issues  credits to allow the writer peer to transfer data over the bus into  the configured endpoint. Refer to the Flow Control topic in the  NI RF Signal Generators Help for more information. This attribute is  coerced up by NI-RFSG to the nearest 128-byte boundary.  This attribute is endpoint-based. \n Units: samples per channel \n \n'
        },
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INTERVAL',
        'type': 'ViInt64'
    },
    1150135: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the initial amount of data that the writer peer  can transfer over the bus into the configured endpoint when the  peer-to-peer data stream is enabled. If this attribute is not  set and the endpoint is empty, credits equal to the full endpoint  size are issued to the writer peer. If data is written to the  endpoint using the niRFSG_WriteP2PEndpointI16 function prior to  enabling the stream, credits equal to the remaining space available  in the endpoint are issued to the writer peer. This attribute is  coerced up by NI-RFSG to 8-byte boundaries.   This attribute is endpoint based \n \n Units: samples per channel \n \n'
        },
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS',
        'type': 'ViInt64'
    },
    1150136: {
        'access': 'read only',
        'documentation': {
            'description': ' Indicates in degrees Celsius the temperature of the device at the time of  the last self calibration. \n'
        },
        'name': 'SELF_CALIBRATION_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150137: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the  RF power settles within the specified accuracy level after calling the niRFSG_Initiate function  or niRFSG_WaitUntilSettled function or prior to advancing to next step if using RF list mode. \n \n Any specified amplitude settling value that is above the acceptable minimum value is  coerced down to the closest valid value. \n \n PXI/PXIe-5650/5651/5652: This attribute is for NI internal use only. \n \n Units: dB \n \n'
        },
        'name': 'AMPLITUDE_SETTLING',
        'type': 'ViReal64'
    },
    1150140: {
        'access': 'read-write',
        'documentation': {
            'description': ' Indicates the maximum amount of time allowed to complete a streaming write operation.\n \n'
        },
        'name': 'STREAMING_WRITE_TIMEOUT',
        'type': 'ViReal64'
    },
    1150141: {
        'access': 'read-write',
        'documentation': {
            'description': ' Determines the inheritance behavior of the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT  attribute when a script inherits values from specified waveforms. \n \n'
        },
        'enum': 'PPAScriptInheritance',
        'name': 'PEAK_POWER_ADJUSTMENT_INHERITANCE',
        'type': 'ViInt32'
    },
    1150142: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master device when synchronizing the Script Trigger between multiple devices. \n \n The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line. \n \n When synchronizing the Script Trigger, one device must always be designated as the master.  The master device actively drives the Script Trigger distribution line. For slave devices, set the  NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE attribute to NIRFSG_VAL_DIGITAL_EDGE, and set the  NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute to sync_script. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the  NI RF Signal Generators Help for more information about device synchronization for vector signal transceivers. \n \n'
        },
        'name': 'SYNC_SCRIPT_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150143: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the synchronized Script Trigger signal.  When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the  NI RF Signal Generators Help for more information about device synchronization for vector signal transceivers. \n \n'
        },
        'name': 'SYNC_SCRIPT_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150144: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the connector(s) to use to generate the signal. To set this attribute,  the NI-RFSG device must be in the Configuration state. \n \n You must write complex I and Q data for all options. The Q data has no effect if  you set this attribute to I Only and set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY  attribute to 0. If you set the NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY attribute to a  value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex  value and outputs the real portion of the result on the I connector(s) of the device. \n \n If you set the NIRFSG_ATTR_OUTPUT_PORT attribute to NIRFSG_VAL_I_ONLY or NIRFSG_VAL_IQ_OUT,  the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute applies. \n \n'
        },
        'enum': 'OutputPort',
        'name': 'OUTPUT_PORT',
        'type': 'ViInt32'
    },
    1150145: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP)  applies the specified frequency shift to the I/Q data before the data is sent to the  digital-to-analog converter (DAC). To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Units: hertz (Hz) \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_OUT_PORT_CARRIER_FREQUENCY',
        'type': 'ViReal64'
    },
    1150146: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to use the I/Q OUT port for Differential configuration or Single-Ended configuration.  If you set this attribute to NIRFSG_VAL_SINGLE_ENDED, you must terminate the negative I and Q output  connectors with a 50 Ohm termination. \n \n If you set this attribute to NIRFSG_VAL_SINGLE_ENDED, the positive I and Q connectors generate the resulting waveform.  If you set this attribute to NIRFSG_VAL_DIFFERENTIAL, both the positive and negative I and Q connectors generate the resulting waveform. \n\n To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViInt32 function to  specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels  by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the Differential and Single-Ended Operation (I/Q Interface) topic of the NI RF Signal Generators Help  for more information about differential and single-ended operation.\n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'enum': 'IqOutPortTermConfig',
        'name': 'IQ_OUT_PORT_TERMINAL_CONFIGURATION',
        'type': 'ViInt32'
    },
    1150147: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the amplitude of the generated signal in volts, peak-to-peak (Vpk-pk). For example,  if you set this attribute to 1.0, the output signal ranges from -0.5 volts to 0.5 volts. \n To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViReal64 function to  specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels  by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the specifications document for your device for allowable output levels. \n \n Units: Volts, peak-to-peak \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_OUT_PORT_LEVEL',
        'type': 'ViReal64'
    },
    1150148: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the common-mode offset applied to the signals generated at each differential output terminal.  This attribute applies only when you set the NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION attribute to NIRFSG_VAL_DIFFERENTIAL.  Common-mode offset shifts both positive and negative terminals in the same direction. \n To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViReal64 function to  specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels  by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Units: Volts \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_OUT_PORT_COMMON_MODE_OFFSET',
        'type': 'ViReal64'
    },
    1150149: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the value, in volts, that the signal generator adds to the I and Q signals.  To set this attribute, the NI-RFSG device must be in the Configuration state. \n To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViReal64 function to  specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels  by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n Units: Volts \n \n Supported Devices: PXIe-5645, PXIe-5820 \n PXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.\n PXIe-5820: The waveform is not automatically scaled in DSP prior to adding offset. To prevent DSP overflows, use the NIRFSG_ATTR_ARB_PRE_FILTER_GAIN attribute  to scale the waveform to provide additional headroom for offsets. \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_OUT_PORT_OFFSET',
        'type': 'ViReal64'
    },
    1150150: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to use the internal or external local oscillator (LO) source.  If this attribute is set to  (empty string), NI-RFSG uses the internal LO source.  To set this attribute, the NI-RFSG device must be in the Configuration state. \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViString function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n \n',
            'note': ' For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this attribute is set to NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR. \n'
        },
        'enum': 'LoSource',
        'name': 'LO_SOURCE',
        'type': 'ViString'
    },
    1150151: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step size, in hertz, for tuning the local oscillator (LO) phase-locked loop (PLL). \n \n When the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute is enabled, the specified step size  affects the fractional spur performance of the device. When the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED  attribute is disabled, the specified step size affects the phase noise performance of the device. \n \n The valid values for this attribute depend on the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute.  PXIe-5644/5645/5646—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is  coerced to the nearest valid value. \n \n PXIe-5840/5841—If you disable the NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED attribute, the specified value is  coerced to the nearest valid value that is less than or equal to the desired step size. \n \n'
        },
        'name': 'LO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150152: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL).  This attribute enables or disables fractional frequency tuning in the LO. Fractional mode  provides a finer frequency step resolution and allows smaller values for the  NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE attribute. However, fractional mode may introduce non-harmonic spurs. \n \n This attribute applies only if you set the NIRFSG_ATTR_LO_SOURCE attribute to NIRFSG_VAL_LO_SOURCE_ONBOARD_STR. \n \n Refer to the local oscillators topic appropriate to your device in the  NI RF Signal Generators Help for more information about using fractional mode. \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViInt32 function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n \n',
            'note': ' For the PXIe-5841 with PXIe-5655, this attribute is ignored if the PXIe-5655 is used as the LO source. \n'
        },
        'enum': 'EnableValues',
        'name': 'LO_PLL_FRACTIONAL_MODE_ENABLED',
        'type': 'ViInt32'
    },
    1150153: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the delay, in seconds, to apply to the I/Q waveform. To set this attribute,  the NI-RFSG device must be in the Configuration state. \n \n Units: Seconds \n \n'
        },
        'name': 'INTERPOLATION_DELAY',
        'type': 'ViReal64'
    },
    1150154: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the delay, in seconds, applied to the Started event, Done event, and all Marker events with respect to the analog  output of the RF signal generator. To set this attribute, the NI-RFSG device must be in the Configuration or Generation state. \n By default, markers and events are delayed to align with the waveform data generated from the device.  This attribute adds an additional delay to markers and events. Use this attribute to adjust the time delay between  events and the corresponding data. \n \n Units: Seconds \n \n',
            'note': ' If you decrease the event delay during generation, some markers may be dropped. \n\n'
        },
        'name': 'EVENTS_DELAY',
        'type': 'ViReal64'
    },
    1150155: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master device when synchronizing the Start Trigger between multiple devices. \n \n The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line. \n \n When synchronizing the Start Trigger, one device must always be designated as the master.  The master device actively drives the Start Trigger distribution line. For slave devices, set the NIRFSG_ATTR_START_TRIGGER_TYPE  attribute to NIRFSG_VAL_DIGITAL_EDGE, and set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute to sync_script. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the  NI RF Signal Generators Help for more information about device synchronization for vector signal transceivers. \n \n'
        },
        'name': 'SYNC_START_TRIGGER_MASTER',
        'type': 'ViBoolean'
    },
    1150156: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger,  configure all devices to use the same Start Trigger distribution line. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device in the  NI RF Signal Generators Help for more information about device synchronization for vector signal transceivers. \n \n'
        },
        'name': 'SYNC_START_TRIGGER_DIST_LINE',
        'type': 'ViString'
    },
    1150157: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the repetition mode of a waveform when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM.  If you set this attribute to VI_TRUE, the number of repetitions is determined by the NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT attribute.\n To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'name': 'ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE',
        'type': 'ViBoolean'
    },
    1150158: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the repeat count of a waveform when you set the  NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE attribute to VI_TRUE.  This attribute is valid only when you set the NIRFSG_ATTR_GENERATION_MODE attribute to NIRFSG_VAL_ARB_WAVEFORM. \n To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'name': 'ARB_WAVEFORM_REPEAT_COUNT',
        'type': 'ViInt32'
    },
    1150160: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute offsets the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY from the RF frequency.  Use this attribute to keep the local oscillator (LO) leakage at a determined offset from the RF signal. \n \n the NIRFSG_ATTR_ARB_CARRIER_FREQUENCY attribute at the same time as the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute. \n \n \n',
            'note': ' Resetting this attribute disables the upcoverter frequency offset. \n'
        },
        'name': 'UPCONVERTER_FREQUENCY_OFFSET',
        'type': 'ViReal64'
    },
    1150161: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.  \n \n Units: Degrees Celsius \n \n',
            'note': ' If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n'
        },
        'name': 'IQ_OUT_PORT_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150162: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the marker event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal.  Use marker events to toggle the state of RF blanking. The RF Output always starts in the unblanked state. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n You can specify marker events by using scripts to trigger blanking at a certain point in a waveform.  For example, if you set this attribute to NIRFSG_VAL_MARKER0, and marker0 occurs on samples 1,000  and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000. \n \n \n',
            'note': ' For the PXIe-5840/5841, RF blanking does not occur for frequencies below 120 MHz. \n'
        },
        'name': 'RF_BLANKING_SOURCE',
        'type': 'ViString'
    },
    1150163: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the load impedance connected to the I/Q OUT port. To set this attribute, the NI-RFSG device must be in the Configuration state. \n To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViReal64 function to  specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels  by using I or Q as the channel string, or set the channel string to  (empty string) to configure both channels.  For the PXIe-5820, the only valid value for the channel string is  (empty string). \n\n Units: Ohms \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the RF ports. \n'
        },
        'name': 'IQ_OUT_PORT_LOAD_IMPEDANCE',
        'type': 'ViReal64'
    },
    1150165: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the narrowband frequency modulation (FM) range to apply  by sending the signal through an integrator. \n This attribute is valid only when you set the NIRFSG_ATTR_ANALOG_MODULATION_TYPE  attribute to NIRFSG_VAL_FM and the NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND attribute to NIRFSG_VAL_NARROWBAND. \n'
        },
        'enum': 'AnalogModulationFMNarrowbandIntegrator',
        'name': 'ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR',
        'type': 'ViInt32'
    },
    1150166: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the  input signal before the signal modulates the carrier. A value of 0 completely  attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n'
        },
        'name': 'ANALOG_MODULATION_FM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150167: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies an uncalibrated digital-to-analog converter (DAC) value that scales  the input signal before the signal modulates the carrier. A value of 0 completely  attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n \n When using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity.  Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input.  Read this attribute to determine the coerced value. \n'
        },
        'name': 'ANALOG_MODULATION_AM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150168: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies an uncalibrated digital-to-analog converter (DAC) value that  scales the input signal before the signal modulates the carrier. A value of 0  completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.\n'
        },
        'name': 'ANALOG_MODULATION_PM_SENSITIVITY',
        'type': 'ViReal64'
    },
    1150173: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the level of attenuation in the attenuator path.  Setting this attribute overrides the value chosen by NI-RFSG.  Not all power levels are achievable if you set this attribute. \n \n Units: dB \n \n Valid Values: 0 dB to 110 dB in steps of 10 \n',
            'note': ' Resetting this attribute reverts back to the default unset behavior.\n'
        },
        'name': 'ATTENUATOR_SETTING',
        'type': 'ViReal64'
    },
    1150175: {
        'access': 'read-write',
        'name': 'CONFIGURATION_LIST_IS_DONE',
        'type': 'ViBoolean'
    },
    1150180: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. \n \n The master device distributes the Sample Clock sync signal to all devices in the system through the Sample   Clock sync distribution line. \n \n When synchronizing the Sample Clock, one device must always be designated as the master.  The master device actively drives the Sample Clock sync distribution line. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic in the NI RF Signal Generators Help  for more information about PXIe-5646 device synchronization.\n \n'
        },
        'name': 'SYNC_SAMPLE_CLOCK_MASTER',
        'type': 'ViBoolean'
    },
    1150181: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies which external trigger line distributes the Sample Clock sync signal.  When synchronizing the Sample Clock, configure all devices to use the same Sample Clock sync distribution line.\n \n To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n Refer to the Synchronization Using NI-RFSA and NI-RFSG topic in the NI RF Signal Generators Help  for more information about PXIe-5646 device synchronization.\n \n'
        },
        'name': 'SYNC_SAMPLE_CLOCK_DIST_LINE',
        'type': 'ViString'
    },
    1150182: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the amplitude extender module temperature in degrees Celsius. \n \n Units: degrees Celsius (°C) \n \n'
        },
        'name': 'AE_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150185: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the amplification path to use. The low harmonic path provides greater  second and third harmonic spurious response, and the high power path provides higher output power. \n \n NI-RFSG automatically sets the value of this attribute based on power and frequency settings.  Setting this attribute overrides the value chosen by NI-RFSG.\n \n  \n',
            'note': ' Resetting this attribute reverts back to the default unset behavior. \n'
        },
        'enum': 'AmpPath',
        'name': 'AMP_PATH',
        'type': 'ViInt32'
    },
    1150186: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string containing the path to the location of the current NI-RFSG instrument  driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device.  You can specify the bitfile location using the Driver Setup string in the optionString parameter  of the niRFSG_InitWithOptions function. \n \n NI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to  customize the behavior of the vector signal transceiver FPGA while maintaining the functionality  of the NI-RFSG instrument driver. \n  \n Refer to the NI-RFSA and NI-RFSG Instrument Driver FPGA Extensions topic in the NI RF Signal  Generators Help for more information about using NI-RFSG instrument driver FPGA extensions for  NI vector signal analyzers. \n \n'
        },
        'name': 'FPGA_BITFILE_PATH',
        'type': 'ViString'
    },
    1150188: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns whether the NI RF signal generator has the fast tuning option available.\n'
        },
        'name': 'FAST_TUNING_OPTION',
        'type': 'ViBoolean'
    },
    1150190: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse modulation mode to use.\n \n'
        },
        'enum': 'PulseModulationMode',
        'name': 'PULSE_MODULATION_MODE',
        'type': 'ViInt32'
    },
    1150191: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the analog modulation frequency modulation (FM) band to use.  Wideband FM allows for modulating signals higher than 100 kHz.  Narrowband FM allows for modulating lower frequency signals. \n'
        },
        'enum': 'AnalogModulationFMBand',
        'name': 'ANALOG_MODULATION_FM_BAND',
        'type': 'ViInt32'
    },
    1150192: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the phase modulation (PM) mode to use. \n'
        },
        'enum': 'AnalogModulationPMMode',
        'name': 'ANALOG_MODULATION_PM_MODE',
        'type': 'ViInt32'
    },
    1150194: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the name of the fully qualified signal name as a string. \n \n'
        },
        'name': 'CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME',
        'type': 'ViString'
    },
    1150195: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables the automatic leveling control (ALC). \n \n PXIe-5654 with PXIe-5696: If this attribute is enabled, the ALC is closed (closed-loop mode)  and allows for better amplitude accuracy and wider amplitude dynamic range.  If this attribute is disabled, the ALC is open (open-loop mode), which is ideal when using modulation.  Disabling the NIRFSG_ATTR_ALC_CONTROL attribute also allows for NI-RFSG to perform an automatic power search. \n \n PXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device.  The PXIe-5654 does not support the ALC when used as a stand-alone device. \n \n'
        },
        'enum': 'EnableValues',
        'name': 'ALC_CONTROL',
        'type': 'ViInt32'
    },
    1150196: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables automatic power search. When this attribute is enabled,  a power search performs after the device is initiated, after output power is enabled,  or when the frequency or power level changes while the device is generating.  When this attribute is disabled, NI-RFSG does not perform a power search unless you call the niRFSG_PerformPowerSearch function. \n \n This attribute is ignored when the NIRFSG_ATTR_ALC_CONTROL attribute is enabled. \n \n PXIe-5654: NIRFSG_VAL_DISABLE is the only supported value for this device.\n'
        },
        'enum': 'EnableValues',
        'name': 'AUTO_POWER_SEARCH',
        'type': 'ViInt32'
    },
    1150199: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the local oscillator (LO). \n \n Otherwise, this attribute is read-only. \n To use this attribute for the PXIe-5830/5831, you must use the channelName parameter  of the niRFSG_SetAttributeViReal64 function to specify the name of the channel you are configuring. You can  configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2  to configure both channels. For all other devices, the the only valid value for the channel string is  (empty string). \n \n Units: Hz \n \n',
            'note': ' This attribute is read/write if you are using an external LO. '
        },
        'name': 'LO_FREQUENCY',
        'type': 'ViReal64'
    },
    1150204: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the digital gain, in decibels. The digital gain is applied to the  waveform data after filtering. Use this attribute to adjust the output power  of the device while keeping the analog path fixed. This may cause clipping,  overflows, or quantization noise if used improperly. \n To set this attribute, the NI-RFSG device must be in the Configuration or  Generation state. \n \n Default Value: 0 dB \n \n'
        },
        'name': 'ARB_DIGITAL_GAIN',
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the output behavior for the Marker Event.  To set this attribute,  the NI-RFSG device must be in the Configuration state. \n'
        },
        'enum': 'MarkerEventOutputBehavior',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'type': 'ViInt32'
    },
    1150207: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse width value for the Marker Event. Use the  NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS attribute to set the units for the  pulse width value. This attribute is valid only when the  NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n'
        },
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'type': 'ViReal64'
    },
    1150208: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the pulse width units for the Marker Event. This attribute is  valid only when the NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_PULSE. \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n'
        },
        'enum': 'MarkerEventPulseWidthUnits',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the initial state for the Marker Event when the  NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR attribute is set to NIRFSG_VAL_TOGGLE.  \n \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n'
        },
        'enum': 'MarkerEventToggleInitialState',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the total power consumption of the device. \n Units: Watts \n Supported Devices: PXIe-5820/5830/5831/5840/5841 \n \n',
            'note': ' If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n'
        },
        'name': 'MODULE_POWER_CONSUMPTION',
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the FPGA temperature in degrees Celsius. \n \n Serial signals between the sensor and the system control unit can  potentially modulate the signal being generated, thus causing phase spurs.  After the device thoroughly warms up, its temperature varies only slightly  (less than 1 degree Celsius) and slowly, and it is not necessary to  constantly poll this temperature sensor. \n Units: desgrees Celsius (°C) \n \n',
            'note': ' If you query this attribute during RF list mode, list steps may take longer to complete during list execution. \n'
        },
        'name': 'FPGA_TEMPERATURE',
        'type': 'ViReal64'
    },
    1150212: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the minimum time between temperature sensor readings. \n'
        },
        'name': 'TEMPERATURE_READ_INTERVAL',
        'type': 'ViReal64'
    },
    1150217: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether peer-to-peer should continuously generate data from  the peer-to-peer stream or from only a finite number of samples,  according to the NIRFSG_ATTR_P2P_NUMBER_OF_SAMPLES_TO_GENERATE attribute.  To use this attribute, peer-to-peer must be enabled. This attribute is endpoint-based.  \n \n'
        },
        'name': 'P2P_IS_FINITE_GENERATION',
        'type': 'ViBoolean'
    },
    1150218: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies how many samples are generated from the peer-to-peer subsystem  when it is enabled. To use this attribute, peer-to-peer must be enabled and  set to finite generation. This attribute is endpoint-based. \n \n'
        },
        'name': 'P2P_NUMBER_OF_SAMPLES_TO_GENERATE',
        'type': 'ViInt64'
    },
    1150219: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns how many samples NI-RFSG pulls from the peer-to-peer FIFO per read.  You can use this attribute to determine how many samples to send across the  peer-to-peer bus to ensure that no samples are ignored. If you send a number  of samples that is not a multiple of this value, the remaining samples are not  read from the FIFO during generation. This attribute is endpoint-based. \n \n'
        },
        'name': 'P2P_GENERATION_FIFO_SAMPLE_QUANTUM',
        'type': 'ViInt64'
    },
    1150220: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the delay, in seconds, to apply to the I/Q waveform. \n Relative delay allows for delaying the generated signal from one device relative  to the generated signal of another device after those devices have been synchronized.  You can achieve a negative relative delay by delaying both synchronized devices by the  same value (1 us) before generation begins and then changing the relative delay to a  smaller amount than the initial value on only one of the devices. \n \n that does not support this attribute, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY attribute. \n \n To set this attribute, the NI-RFSG device must be in the Configuration or Generation state. \n \n of the sample period but not worse than one Sample Clock period. \n \n Units: Seconds \n \n Valid Values: 0 us to 3.2 us \n \n Supported Devices: PXIe-5820/5830/5831/5840/5841 \n',
            'note': ' The resolution of this attribute is a function of the I/Q sample period at 15E(-6) '
        },
        'name': 'RELATIVE_DELAY',
        'type': 'ViReal64'
    },
    1150225: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform.  Use this attribute to reduce the trigger jitter when synchronizing multiple devices with NI-TClk.  This attribute can also help maintain synchronization repeatability by writing the absolute delay  value of a previous measurement to the current session. \n To set this attribute, the NI-RFSG device must be in the Configuration state. \n \n \n \n Units: Seconds \n \n Valid Values: Plus or minus half of one Sample Clock period. \n \n Supported Devices: PXIe-5820/5840/5841 \n',
            'note': ' The resolution of this attribute is a function of the I/Q sample period at 15E(-6) times that sample period.  \n'
        },
        'name': 'ABSOLUTE_DELAY',
        'type': 'ViReal64'
    },
    1150226: {
        'access': 'read-write',
        'name': 'DEVICE_INSTANTANEOUS_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150228: {
        'access': 'read-write',
        'documentation': {
            'description': ' Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform. \n\n Default Value: NIRFSG_VAL_ERROR_REPORTING_WARNING \n\n Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5840/5841 \n \n'
        },
        'enum': 'OverflowErrorReporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'type': 'ViInt32'
    },
    1150239: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the size of the DMA buffer in computer memory, in bytes. To  set this attribute, the NI-RFSG device must be in the Configuration state.\n\n large fetches to be transferred more efficiently.\n\n Units: bytes\n Default Value: 8 MB\n Supported Devices: PXIe-5820/5830/5831/5840/5841 \n',
            'note': ' A sufficiently large host DMA buffer improves performance by allowing '
        },
        'name': 'HOST_DMA_BUFFER_SIZE',
        'type': 'ViInt64'
    },
    1150241: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the port to configure. \n\n Valid Values: \n PXIe-5644/5645/5646, PXIe-5820/5840/5841:  (empty string) \n PXIe-5830: if0, if1 \n PXIe-5831: if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections  and x is the port number on the mmRH-5582 front panel. \n\n Default Value: \n PXIe-5644/5645/5646, PXIe-5820/5840/5841:  (empty string) \n PXIe-5830/5831: if0 \n Supported Devices: PXIe-5820/5830/5831/5840/5841 \n \n'
        },
        'name': 'SELECTED_PORTS',
        'type': 'ViReal64'
    },
    1150242: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export. Set this attribute to NIRFSG_VAL_ENABLE to allow NI-RFSA to control the LO out export.  Use the NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED attribute to control the LO out export from NI-RFSA.\n\n Default Value: NIRFSG_VAL_DISABLE \n\n Supported Devices: PXIe-5840/5841 \n'
        },
        'enum': 'EnableValues',
        'name': 'LO_OUT_EXPORT_CONFIGURE_FROM_RFSA',
        'type': 'ViInt32'
    },
    1150243: {
        'access': 'read-write',
        'enum': 'RfInLoExportEnabled',
        'name': 'RF_IN_LO_EXPORT_ENABLED',
        'type': 'ViInt32'
    },
    1150244: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the temperature change, in degrees Celsius, required before NI-RFSG recalculates the thermal correction settings when entering the Generation state. \n\n Units: degrees C \n\n Supported Devices: PXIe-5830/5831/5840/5841 Default Values: PXIe-5830/5831: 0.2 PXIe-5840/5841: 1.0    '
        },
        'name': 'THERMAL_CORRECTION_TEMPERATURE_RESOLUTION',
        'type': 'ViReal64'
    },
    1150248: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to allow NI-RFSG to select the upconverter frequency offset.  You can either set an offset yourself or let NI-RFSG select one for you. \n\n Placing the upconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage. \n\n To set an offset yourself, set this attribute to NIRFSG_VAL_AUTOMATIC or NIRFSG_VAL_USER_DEFINED,  and set either the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET attribute. \n To allow NI-RFSG to automatically select the upconverter frequency offset, set this attribute  to NIRFSG_VAL_AUTOMATIC or NIRFSG_VAL_ENABLED and set the NIRFSG_ATTR_SIGNAL_BANDWIDTH to describe your  expected input signal. Do not set the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY or NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET  attributes. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal  bandwidth if there is sufficient room in the device instantaneous bandwidth to do so. \n Set this attribute to NIRFSG_VAL_ENABLED if you want to receive an error any time NIRFSG  is unable to apply automatic offset. \n When you set an offset yourself or do not use an offset, the reference frequency for gain is  near the upconverter center frequency, and offset mode reads back as NIRFSG_VAL_USER_DEFINED. When NI-RFSG  automatically sets an offset, the reference frequency for gain is the carrier frequency, and offset mode reads back as NIRFSG_VAL_ENABLED. \n \n'
        },
        'enum': 'UpconverterFrequencyOffsetMode',
        'name': 'UPCONVERTER_FREQUENCY_OFFSET_MODE',
        'type': 'ViInt32'
    },
    1150249: {
        'access': 'read-write',
        'documentation': {
            'description': ' Returns a comma-separated list of the ports available for use based on your instrument configuration. Supported Devices: PXIe-5644/5645/5646, PXIe-5820/5840/5841, PXIe-5830/5831 \n \n'
        },
        'name': 'AVAILABLE_PORTS',
        'type': 'ViReal64'
    },
    1150251: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a string containing the name of the FPGA target being used. \n This name can be used with the RIO open session to open a reference to the FPGA. \n This attribute is channel dependent if multiple FPGA targets are supported. \n \n Supported Devices: PXIe-5820/5830/5831/5840/5841 \n \n'
        },
        'name': 'FPGA_TARGET_NAME',
        'type': 'ViString'
    },
    1150252: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the type of de-embedding to apply to measurements on the specified port. To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViInt32 function to specify the name of the port to configure for de-embedding. \n\n If you set this attribute to NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR or NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT. \n\n Default Value: NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR \n\n Valid Values for PXIe-5830/5832/5840/5841: NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR, NIRFSG_VAL_DEEMBEDDING_TYPE_NONE \n\n Valid Values for PXIe-5831: NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR, NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR, or NIRFSG_VAL_DEEMBEDDING_TYPE_NONE. NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).\n\n Supported Devices: PXIe-5830/5831/5832/5840/5841     '
        },
        'enum': 'DeembeddingType',
        'name': 'DEEMBEDDING_TYPE',
        'type': 'ViInt32'
    },
    1150253: {
        'access': 'read-write',
        'documentation': {
            'description': ' Selects the de-embedding table to apply to the measurements on the specified port. To use this attribute, you must use the channelName parameter of the niRFSG_SetAttributeViString function to specify the name of the port to configure for de-embedding. \n\n If de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT. \n\n Use the niRFSG_CreateDeembeddingSparameterTableArray function to create tables. \n\n Supported Devices: PXIe-5830/5831/5840/5841     '
        },
        'name': 'DEEMBEDDING_SELECTED_TABLE',
        'type': 'ViString'
    },
    1150257: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. \n\n Default Value: 1 MHz \n Valid Values: 1 Hz to 50 MHz for LO1 and 1 Hz to 100 MHz for LO2 \n\n \n'
        },
        'name': 'LO_VCO_FREQUENCY_STEP_SIZE',
        'type': 'ViReal64'
    },
    1150258: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the expected thermal operating range of the instrument from the self cal temperature in degrees C, as reported by the Device Temperature property. \n\n For example, if the Thermal Correction Headroom Range property is set to 5.0, and the device is self calibrated at 35 degrees C, \n then you can expect to run the device from 30 degC to 40 degC with corrected accuracy and no overflows. \n Setting this value to a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. \n Operating the instrument outside of the specified range may cause degraded performance, or DSP overflows. \n\n Units: degrees C \n\n Supported Devices: PXIe-5830/5831/5840/5841 Default Value (PXIe-5830/5831): 5 \n\n Default Value (PXIe-5840/5841): 10 \n\n    '
        },
        'name': 'THERMAL_CORRECTION_HEADROOM_RANGE',
        'type': 'ViReal64'
    },
    1150263: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the I/Q rate of the waveform. To set this attribute, the NI-RFSG device must be in the Configuration state. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'name': 'WAVEFORM_IQ_RATE',
        'type': 'ViReal64'
    },
    1150264: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8 × I/Q rate). \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'name': 'WAVEFORM_SIGNAL_BANDWIDTH',
        'type': 'ViReal64'
    },
    1150265: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing. \n\n Units: dB\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'name': 'WAVEFORM_RUNTIME_SCALING',
        'type': 'ViReal64'
    },
    1150266: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the peak-to-average power ratio (PAPR). \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'name': 'WAVEFORM_PAPR',
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies a comma-separated list of ports for which to fix the group delay. \n\n Valid Values: \n\n PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel. \n\n Default Value:  (empty string) \n\n Supported Devices: PXIe-5831/5832 \n'
        },
        'name': 'FIXED_GROUP_DELAY_ACROSS_PORTS',
        'type': 'ViString'
    },
    1150272: {
        'access': 'read-write',
        'name': 'WAVEFORM_FILEPATH',
        'type': 'ViString'
    },
    1150273: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables the detection of burst start and burst stop locations in the waveform. Set this attribute to NIRFSG_VAL_ENABLED before writing a waveform to NI-RFSG memory for detecting bursts You can read the detected burst start and burst stop locations using niRFSG_Get_Waveform_Burst_Start_Locations and niRFSG_Get_Waveform_Burst_Stop_Locations functions respectively.\n \n NIRFSG_ATTR_WAVEFORM_RF_BLANKING_ENABLED attribute is enabled, you must set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_ENABLED attribute to NIRFSG_VAL_DISABLE. \n\n Default Value: NIRFSG_VAL_DISABLED\n\n Supported Devices:PXIe-5820/5830/5831/5832/5840/5841\n\n',
            'note': ' When you download a waveform using niRFSG_Read_and_Download_Waveform_From_file_(TDMS) function and if'
        },
        'enum': 'EnableValues',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION',
        'type': 'ViInt32'
    },
    1150274: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_ENABLED attribute. When you set NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE to NIRFSG_VAL_AUTO, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this attribute to NIRFSG_VAL_MANUAL and specify the burst detection parameters using the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME, NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD, NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME attributes. \n\n Default Value: NIRFSG_VAL_AUTO\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n'
        },
        'enum': 'WriteWaveformBurstDetectionMode',
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_MODE',
        'type': 'ViInt32'
    },
    1150275: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies a time duration for which the signal must be quiet before a valid burst start location or after a valid burst stop location. This attribute is ignored when you disable the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_ENABLED attribute or when you set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE attribute to NIRFSG_VAL_AUTO. \n\n The default value of this attribute is 0, which means NI-RFSG does not look for a quiet time before or after detected burst start and stop locations. This attribute is useful for detecting burst locations in signals containing multiple bursts. However, each burst must have large changes in signal power within itself. By configuring the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME attribute to a value that is less than or equal to the minimum time between two adjacent bursts in the waveform, you can ensure that the burst start and stop locations are detected at the beginning and end of a burst respectively, rather than at the signal power change within a burst. \n\n Units: seconds(s)\n\n Default Value: 0\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n'
        },
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME',
        'type': 'ViReal64'
    },
    1150276: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this attribute. This attribute is ignored when you disable the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_ENABLED attribute or when you set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE attribute to NIRFSG_VAL_AUTO. \n\n Units: dB\n\n Default Value: 0\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD',
        'type': 'ViReal64'
    },
    1150277: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the minimum duration of the detected bursts. Any detected burst with a duration smaller than the value of this attribute is ignored by NI-RFSG. This attribute is ignored when you disable the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_ENABLED attribute or when you set the NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE attribute to NIRFSG_VAL_AUTO. \n\n Units: seconds(s)\n\n Default Value: 0\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n'
        },
        'name': 'WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME',
        'type': 'ViReal64'
    },
    1150278: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables RF blanking. \n\n Default Value: NIRFSG_VAL_DISABLED\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n'
        },
        'enum': 'EnableValues',
        'name': 'WAVEFORM_RF_BLANKING',
        'type': 'ViInt32'
    },
    1150289: {
        'access': 'read-write',
        'name': 'DEEMBEDDING_COMPENSATION_GAIN',
        'type': 'ViReal64'
    },
    1150290: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the configurations to skip while loading from a file. \n\n Default Value: NIRFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n'
        },
        'enum': 'LoadOptions',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS',
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the configurations to skip to reset while loading from a file. \n\n Default Value: NIRFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n'
        },
        'enum': 'ResetOptions',
        'name': 'LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS',
        'type': 'ViInt32'
    },
    1150292: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal.  To set this attribute, the NI-RFSG device must be in the Configuration state.  Units: hertz (Hz) \n Default Value: 10 MHz  Valid Values:   PXIe-5820/5830/5831/5832/5840/5841: 10 MHz  PXIe-5842: 10 MHz, 100 MHz, 1 GHz  PXIe-5860: 10 MHz, 100 MHz  Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860  \n  '
        },
        'name': 'EXPORTED_REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1150293: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether to perform the normalization on a waveform. \n\n \n\n Default Value: NIRFSG_VAL_DISABLE\n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841\n\n',
            'note': ' You can not set NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION and NIRFSG_ATTR_POWER_LEVEL_TYPE attributes at the same time.'
        },
        'enum': 'EnableValues',
        'name': 'WRITE_WAVEFORM_NORMALIZATION',
        'type': 'ViInt32'
    },
    1150297: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the size of the waveform specified by active channel. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'WAVEFORM_WAVEFORM_SIZE',
        'type': 'ViInt32'
    },
    1150307: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active level of the pulse modulation signal when pulse modulation is enabled. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'PULSE_MODULATION_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150308: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the source of the pulse modulation signal. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'PULSE_MODULATION_SOURCE',
        'type': 'ViString'
    },
    1150309: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the destination terminal for exporting the Pulse Modulation Event. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    1150310: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active level of the exported Pulse Modulation Event. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL',
        'type': 'ViInt32'
    },
    1150311: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Selected Path. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'SELECTED_PATH',
        'type': 'ViString'
    },
    1150312: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns a comma separated list of the configurable paths available for use based on your instrument configuration. \n\n Supported Devices: PXIe-5820/5830/5831/5832/5840/5841/5842/5860\n'
        },
        'name': 'AVAILABLE_PATHS',
        'type': 'ViString'
    },
    1152832: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables compensation for filter group delay on the AWG module.  This attribute also accounts for the upconverter group delay and aligns  the RF output with the Started Event, Done Event, and Marker Events.\n \n At a low I/Q rate, the group delay can become so large that some devices  may not be able to align the events with the RF output, in which case  you must increase the I/Q rate or disable this attribute. \n'
        },
        'name': 'COMPENSATE_FOR_FILTER_GROUP_DELAY',
        'type': 'ViBoolean'
    },
    1154097: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the gain the upconverter applies to the signal. \n \n read-only on the PXIe-5644/5645/5646, PXI-5670/5671 PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5840/5841. \n \n Units: dB \n \n',
            'note': ' This attribute is read/write on the PXI-5610 and PXIe-5611 and '
        },
        'name': 'UPCONVERTER_GAIN',
        'type': 'ViReal64'
    },
    1154098: {
        'access': 'read-write',
        'documentation': {
            'description': ' Indicates the center frequency of the passband containing the upconverted  RF signal. Writing a value to this attribute while using the   PXIe-5644/5645/5646/5672/5673/5673E/5820/5840/5841 device enables in-band retuning.   In-band retuning increases the speed of  frequency sweeps by reducing the amount of upconverter retunes. \n \n PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5840/5841 and read-only on the PXI-5670/5671.  \n \n \n \n  and PXIe-5820/5830/5831/5840/5841 device is generating has no effect until a dynamic attribute is set. \n \n Units: hertz (Hz) \n \n',
            'note': ' Setting this attribute while the PXIe-5644/5645/5646, PXIe-5673/5673E, '
        },
        'name': 'UPCONVERTER_CENTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the frequency of the generated RF signal. For arbitrary waveform  generation, this attribute specifies the center frequency of the signal. \n \n The PXI-5670/5671, PXIe-5672, and PXIe-5820 must be in the Configuration state to use this attribute.  However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5673/5673E, PXIe-5830/5831/5840/5841 can be in  the Configuration or the Generation state to use this attribute. \n \n Units: hertz (Hz) \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n'
        },
        'name': 'FREQUENCY',
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies either the average power level or peak power level of the  generated RF signal, depending on the NIRFSG_ATTR_POWER_LEVEL_TYPE  attribute setting. average power of the signal or the peak power of the  signal. \n \n The PXI-5670/5671 and PXIe-5672 must be in the Configuration state to use this attribute.  However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5840/5841  can be in the Configuration or the Generation state to use this attribute. \n \n Refer to the specifications document for your device for allowable  power level settings. \n \n Units: dBm \n \n',
            'note': ' For the PXIe-5645, this attribute is ignored if you are using the I/Q ports. \n'
        },
        'name': 'POWER_LEVEL',
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies whether signal output is enabled. Setting the  NIRFSG_ATTR_OUTPUT_ENABLED attribute to VI_FALSE while in  the Generation state stops signal output, although generation  continues internally. Setting the NIRFSG_ATTR_OUTPUT_ENABLED  attribute while in the Committed state does not transition the  device to the Configuration state, but output changes immediately. \n \n to a valid list name, setting the NIRFSG_ATTR_OUTPUT_ENABLED  attribute transitions the device to the Configuration state. \n \n',
            'note': ' When the NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST attribute is set '
        },
        'name': 'OUTPUT_ENABLED',
        'type': 'ViBoolean'
    },
    1250051: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables pulse modulation. \n \n PXIe-5654/5654 with PXIe-5696: If this attribute is enabled and the signal  at the PULSE IN front panel connector is high, the device generates a signal.  If the signal is low, output generation is disabled. \n \n PXIe-5673/5673E: If this attribute is enabled and the signal at the PLS MOD  front panel connector is high, the device generates a signal.  If the signal is low, output generation is disabled. \n \n'
        },
        'name': 'PULSE_MODULATION_ENABLED',
        'type': 'ViBoolean'
    },
    1250322: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector.  This property is only valid when the NIRFSG_ATTR_REF_CLOCK_SOURCE attribute is set to NIRFSG_VAL_CLK_IN_STR,  NIRFSG_VAL_REF_IN_STR, or NIRFSG_VAL_REF_IN_2_STR.. To set this attribute, the NI-RFSG device  must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696,  the NI-RFSG device must be in the Committed state to read this attribute.  When you read this attribute, it returns the frequency the device is  locked to during the Committed state.\n \n If you set this attribute to NIRFSG_VAL_AUTO, NI-RFSG uses the default Reference Clock  rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.\n \n For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10 MHz.\n \n PXIe-5654/5654 with PXIe-5696: Values between 1 MHz to 20 MHz in 1 MHz steps are supported in  addition to the NIRFSG_VAL_AUTO and NIRFSG_VAL_10MHZ values.\n PXIe-5841 with PXIe-5655: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz * y, where y is 4, 8, 16, 24, 25, or 32.\n \n  Units: hertz (Hz) \n \n  ',
            'note': ' Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. '
        },
        'enum': 'RefClockRate',
        'name': 'REF_CLOCK_RATE',
        'type': 'ViReal64'
    },
    1250401: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables I/Q (vector) modulation of the output signal. Enabling this  attribute is required for generating arbitrary signals. To set this attribute, the NI-RFSG device  must be in the Configuration state. \n This attribute is obsolete and should not be used. \n \n  '
        },
        'name': 'IQ_ENABLED',
        'type': 'ViBoolean'
    },
    1250402: {
        'access': 'read-write',
        'name': 'IQ_NOMINAL_VOLTAGE',
        'type': 'ViReal64'
    },
    1250404: {
        'access': 'read-write',
        'documentation': {
            'description': ' Enables or disables the inverse phase rotation of the I/Q signal by  swapping the I and Q inputs. \n To set this attribute, the NI-RFSG device must  be in the Configuration state.\n \n'
        },
        'name': 'IQ_SWAP_ENABLED',
        'type': 'ViBoolean'
    },
    1250451: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the waveform in onboard memory to generate upon calling  the niRFSG_init function when the NIRFSG_ATTR_GENERATION_MODE  attribute is set to NIRFSG_VAL_ARB_WAVEFORM. The  NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute is ignored when  the NIRFSG_ATTR_GENERATION_MODE attribute is set to  NIRFSG_VAL_SCRIPT or NIRFSG_VAL_CW. To set the  NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute, the NI-RFSG  device must be in the Configuration state. \n \n'
        },
        'name': 'ARB_SELECTED_WAVEFORM',
        'type': 'ViString'
    },
    1250452: {
        'access': 'read-write',
        'documentation': {
            'description': ' This attribute specifies the I/Q rate of the arbitrary waveform.  The I/Q rate is coerced to a value the hardware can achieve.  Read this value back after setting it to see what the actual  I/Q rate is. NI-RFSG internally uses an FIR filter with flat  response up to (0.4 × IQ rate). Given a desired signal with  the maximum frequency content f, sample the signal at  an I/Q rate greater than or equal to (f/0.4). \n \n This attribute applies only when the NIRFSG_ATTR_GENERATION_MODE  attribute is set to NIRFSG_VAL_ARB_WAVEFORM or NIRFSG_VAL_SCRIPT. \n \n Use this attribute to associate an I/Q rate with a waveform.  Refer to the Assigning Properties or Attributes to a Waveform topic of  the NI RF Signal Generators Help for more information about assigning an I/Q rate to a waveform. \n'
        },
        'name': 'IQ_RATE',
        'type': 'ViReal64'
    },
    1250453: {
        'access': 'read-write',
        'name': 'ARB_FILTER_FREQUENCY',
        'type': 'ViReal64'
    },
    1250454: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the maximum number of waveforms the device can hold in memory. \n \n'
        },
        'name': 'ARB_MAX_NUMBER_WAVEFORMS',
        'type': 'ViInt32'
    },
    1250455: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the waveform quantum for the device. The number of samples  in a waveform must be an integer multiple of the waveform quantum.  The other restrictions on the length of the waveform are the minimum and  maximum arbitrary waveform sizes. On the PXI-5671 and PXIe-5672, the value of this  attribute depends on the I/Q rate. Set the NIRFSG_ATTR_IQ_RATE attribute  before reading this attribute. \n'
        },
        'name': 'ARB_WAVEFORM_QUANTUM',
        'type': 'ViInt32'
    },
    1250456: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the smallest allowable waveform size. For the  PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate.  Set the NIRFSG_ATTR_IQ_RATE attribute before reading this attribute.\n \n Units: Samples \n \n'
        },
        'name': 'ARB_WAVEFORM_SIZE_MIN',
        'type': 'ViInt32'
    },
    1250457: {
        'access': 'read only',
        'documentation': {
            'description': ' Returns the size of the largest waveform that is allowed. To read  this attribute, the NI-RFSG device must be in the Configuration state.\n \n For the PXI-5671 and PXIe-5672, the value of this attribute depends on the I/Q rate.  Set the I/Q rate before reading this attribute.  For the PXIe-5673/5673E,  the maximum waveform size is reduced to account for the amount of device  memory currently used. \n \n of onboard memory stores scripts that specify how the waveforms are  generated.  These scripts typically require less than 1 KB of onboard  memory. \n \n',
            'note': ' Not all onboard memory is available for waveform storage. A portion '
        },
        'name': 'ARB_WAVEFORM_SIZE_MAX',
        'type': 'ViInt32'
    },
    1250458: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the Start Trigger type. Depending upon the value of this  attribute, more attributes may be needed to fully configure the trigger.  To set this attribute, the NI-RFSG device must be in the Configuration state.\n \n'
        },
        'enum': 'StartTriggerType',
        'name': 'START_TRIGGER_TYPE',
        'type': 'ViInt32'
    },
    1250459: {
        'access': 'read-write',
        'documentation': {
            'description': ' Specifies the active edge for the Start Trigger. This attribute is used  when the NIRFSG_ATTR_START_TRIGGER_TYPE attribute is set to  NIRFSG_VAL_DIGITAL_EDGE. To set the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE  attribute, the NI-RFSG device must be in the Configuration state. \n \n'
        },
        'enum': 'DigitalEdgeEdge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nirfsg/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/config.py sha256=41e4d7fb92128b0c829cc1b6d2f0bb304ad526f001f0f6906940a0b481edf599 bytes=1442 -->
## FILE: source/codegen/metadata/nirfsg/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/config.py`
- sha256: `41e4d7fb92128b0c829cc1b6d2f0bb304ad526f001f0f6906940a0b481edf599`
- bytes: 1442

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.5.0',
    'c_header': 'niRFSG.h',
    'c_function_prefix': 'niRFSG_',
    'service_class_prefix': 'NiRFSG',
    'java_package': 'com.ni.grpc.nirfsg',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFSG',
    'namespace_component': 'nirfsg',
    'close_function': 'Close',
    'context_manager_name': {
        'abort_function': 'Abort',
        'initiate_function': 'Initiate',
        'task': 'generation'
    },
    'custom_types': [],
    'additional_headers': {'custom/ivi_errors.h': ['service.cpp']},
    'code_readiness': 'Release',
    'driver_name': 'NI-RFSG',
    'extra_errors_used': [
    ],
    'init_function': 'InitWithOptions',
    'status_ok': 'status >= 0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsg',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSG_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSG_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfsg',
    'session_class_description': 'An NI-RFSG session to a National Instruments RF Vector Signal Generator.',
    'session_handle_parameter_name': 'vi'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/config_addon.py sha256=d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58 bytes=226 -->
## FILE: source/codegen/metadata/nirfsg/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/config_addon.py`
- sha256: `d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/enums.py sha256=1ad50bf0d916cc9335098bf77706544d4263e985d39ff00eed0ca15e5c31f8ec bytes=75237 -->
## FILE: source/codegen/metadata/nirfsg/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/enums.py`
- sha256: `1ad50bf0d916cc9335098bf77706544d4263e985d39ff00eed0ca15e5c31f8ec`
- bytes: 75237

````python
enums = {
    'AmpPath': {
        'values': [
            {
                'documentation': {
                    'description': ' Sets the amplification path to use the high power path. \n'
                },
                'name': 'HIGH_POWER',
                'value': 16000
            },
            {
                'documentation': {
                    'description': ' Sets the amplification path to use the low harmonic path. \n'
                },
                'name': 'LOW_HARMONIC',
                'value': 16001
            }
        ]
    },
    'AnalogModulationFMBand': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies narrowband frequency modulation.\n'
                },
                'name': 'NARROWBAND',
                'value': 17000
            },
            {
                'documentation': {
                    'description': ' Specifies wideband frequency modulation.\n'
                },
                'name': 'WIDEBAND',
                'value': 17001
            }
        ]
    },
    'AnalogModulationFMNarrowbandIntegrator': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies a range from 100 Hz to 1 kHz.\n'
                },
                'name': '100_HZ_TO_1_KHZ',
                'value': 18000
            },
            {
                'documentation': {
                    'description': ' Specifies a range from 1 kHz to 10 kHz.\n'
                },
                'name': '1_KHZ_TO_10_KHZ',
                'value': 18001
            },
            {
                'documentation': {
                    'description': ' Specifies a range from 10 kHz to 100 kHz.\n'
                },
                'name': '10_KHZ_TO_100_KHZ',
                'value': 18002
            }
        ]
    },
    'AnalogModulationPMMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies high deviation. High deviation comes at the expense of a higher phase noise.\n'
                },
                'name': 'HIGH_DEVIATION',
                'value': 19000
            },
            {
                'documentation': {
                    'description': ' Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.\n'
                },
                'name': 'LOW_PHASE_NOISE',
                'value': 19001
            }
        ]
    },
    'AnalogModulationType': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables analog modulation.\n'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation type is FM.\n'
                },
                'name': 'FM',
                'value': 2000
            },
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation type is PM.\n'
                },
                'name': 'PM',
                'value': 2001
            },
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation type is AM.\n'
                },
                'name': 'AM',
                'value': 2002
            }
        ]
    },
    'AnalogModulationWaveformType': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation waveform type is sine.\n'
                },
                'name': 'SINE',
                'value': 3000
            },
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation waveform type is square.\n'
                },
                'name': 'SQUARE',
                'value': 3001
            },
            {
                'documentation': {
                    'description': ' Specifies that the analog modulation waveform type is triangle.\n'
                },
                'name': 'TRIANGLE',
                'value': 3002
            }
        ]
    },
    'AnySignalOutputTerm': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The signal is not exported.\n'
                },
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel SMB connector.  For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.\n'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel SMB connector.\n'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' PFI 4 on the front panel DDC connector.\n'
                },
                'name': 'PFI4',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': ' PFI 5 on the front panel DDC connector.\n'
                },
                'name': 'PFI5',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 0.\n'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 1.\n'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 2.\n'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 3.\n'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 4.\n'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 5.\n'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 6.\n'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.\n'
                },
                'name': 'PXIE_DSTARC',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': ' TRIG IN/OUT terminal.\n'
                },
                'name': 'TRIG_OUT',
                'value': 'TrigOut'
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel DIO connector.\n'
                },
                'name': 'DIO0',
                'value': 'DIO/PFI0',
                'order': 1
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel DIO connector.\n'
                },
                'name': 'DIO1',
                'value': 'DIO/PFI1',
                'order': 2
            },
            {
                'documentation': {
                    'description': ' PFI 2 on the front panel DIO connector.\n'
                },
                'name': 'DIO2',
                'value': 'DIO/PFI2',
                'order': 3
            },
            {
                'documentation': {
                    'description': ' PFI 3 on the front panel DIO connector.\n'
                },
                'name': 'DIO3',
                'value': 'DIO/PFI3',
                'order': 4
            },
            {
                'documentation': {
                    'description': ' PFI 4 on the front panel DIO connector.\n'
                },
                'name': 'DIO4',
                'value': 'DIO/PFI4',
                'order': 5
            },
            {
                'documentation': {
                    'description': ' PFI 5 on the front panel DIO connector.\n'
                },
                'name': 'DIO5',
                'value': 'DIO/PFI5',
                'order': 6
            },
            {
                'documentation': {
                    'description': ' PFI 6 on the front panel DIO connector.\n'
                },
                'name': 'DIO6',
                'value': 'DIO/PFI6',
                'order': 7
            },
            {
                'documentation': {
                    'description': ' PFI 7 on the front panel DIO connector.\n'
                },
                'name': 'DIO7',
                'value': 'DIO/PFI7',
                'order': 8
            }
        ]
    },
    'ArbFilterType': {
        'values': [
            {
                'documentation': {
                    'description': ' None'
                },
                'name': 'NONE',
                'value': 10000
            },
            {
                'documentation': {
                    'description': ' Applies a root-raised cosine filter to the data with the alpha value  specified with the NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA  attribute. '
                },
                'name': 'ROOT_RAISED_COSINE',
                'value': 10001
            },
            {
                'documentation': {
                    'description': ' Applies a raised cosine filter to the data with the alpha value specified  with the NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA attribute. '
                },
                'name': 'RAISED_COSINE',
                'value': 10002
            }
        ]
    },
    'ArbOnboardSampleClockMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the clock mode is high resoultion. High resolution  sampling is when a sample rate is generated by a high resolution clock  source.\n'
                },
                'name': 'HIGH_RESOLUTION',
                'value': 6000
            },
            {
                'documentation': {
                    'description': ' Specifies that the clock mode is divide down. Divide down sampling is  when sample rates are generated by dividing the source frequency.\n'
                },
                'name': 'DIVIDE_DOWN',
                'value': 6001
            }
        ]
    },
    'ArbSampleClockSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Use the AWG module onboard clock as the clock source.\n'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' Use the external clock as the clock source.\n'
                },
                'name': 'CLK_IN',
                'value': 'ClkIn'
            }
        ]
    },
    'ConfigListTrigOutputTerm': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The signal is not exported.\n'
                },
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel SMB connector.  For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.\n'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel SMB connector.\n'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 0.\n'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 1.\n'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 2.\n'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 3.\n'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 4.\n'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 5.\n'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 6.\n'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.\n'
                },
                'name': 'PXIE_DSTARC',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': ' TRIG IN/OUT terminal.\n'
                },
                'name': 'TRIG_OUT',
                'value': 'TrigOut'
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel DIO connector.\n'
                },
                'name': 'DIO0',
                'value': 'DIO/PFI0',
                'order': 9
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel DIO connector.\n'
                },
                'name': 'DIO1',
                'value': 'DIO/PFI1',
                'order': 10
            },
            {
                'documentation': {
                    'description': ' PFI 2 on the front panel DIO connector.\n'
                },
                'name': 'DIO2',
                'value': 'DIO/PFI2',
                'order': 11
            },
            {
                'documentation': {
                    'description': ' PFI 3 on the front panel DIO connector.\n'
                },
                'name': 'DIO3',
                'value': 'DIO/PFI3',
                'order': 12
            },
            {
                'documentation': {
                    'description': ' PFI 4 on the front panel DIO connector.\n'
                },
                'name': 'DIO4',
                'value': 'DIO/PFI4',
                'order': 13
            },
            {
                'documentation': {
                    'description': ' PFI 5 on the front panel DIO connector.\n'
                },
                'name': 'DIO5',
                'value': 'DIO/PFI5',
                'order': 14
            },
            {
                'documentation': {
                    'description': ' PFI 6 on the front panel DIO connector.\n'
                },
                'name': 'DIO6',
                'value': 'DIO/PFI6',
                'order': 15
            },
            {
                'documentation': {
                    'description': ' PFI 7 on the front panel DIO connector.\n'
                },
                'name': 'DIO7',
                'value': 'DIO/PFI7',
                'order': 16
            }
        ]
    },
    'ConfigListTrigSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel SMB connector.\n'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel SMB connector.\n'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 0.\n'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 1.\n'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 2.\n'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 3.\n'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 4.\n'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 5.\n'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 6.\n'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 7.\n'
                },
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': ' PXI Star trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.\n'
                },
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': ' Marker Event 0.\n'
                },
                'name': 'MARKER0_EVENT',
                'value': 'Marker0Event'
            },
            {
                'documentation': {
                    'description': ' Marker Event 1.\n'
                },
                'name': 'MARKER1_EVENT',
                'value': 'Marker1Event'
            },
            {
                'documentation': {
                    'description': ' Marker Event 2.\n'
                },
                'name': 'MARKER2_EVENT',
                'value': 'Marker2Event'
            },
            {
                'documentation': {
                    'description': ' Marker Event 3.\n'
                },
                'name': 'MARKER3_EVENT',
                'value': 'Marker3Event'
            },
            {
                'documentation': {
                    'description': ' Timer Event.\n'
                },
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'documentation': {
                    'description': ' TRIG IN/OUT terminal.\n'
                },
                'name': 'TRIG_IN',
                'value': 'TrigIn'
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel DIO connector.\n'
                },
                'name': 'DIO0',
                'value': 'DIO/PFI0',
                'order': 17
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel DIO connector.\n'
                },
                'name': 'DIO1',
                'value': 'DIO/PFI1',
                'order': 18
            },
            {
                'documentation': {
                    'description': ' PFI 2 on the front panel DIO connector.\n'
                },
                'name': 'DIO2',
                'value': 'DIO/PFI2',
                'order': 19
            },
            {
                'documentation': {
                    'description': ' PFI 3 on the front panel DIO connector.\n'
                },
                'name': 'DIO3',
                'value': 'DIO/PFI3',
                'order': 20
            },
            {
                'documentation': {
                    'description': ' PFI 4 on the front panel DIO connector.\n'
                },
                'name': 'DIO4',
                'value': 'DIO/PFI4',
                'order': 21
            },
            {
                'documentation': {
                    'description': ' PFI 5 on the front panel DIO connector.\n'
                },
                'name': 'DIO5',
                'value': 'DIO/PFI5',
                'order': 22
            },
            {
                'documentation': {
                    'description': ' PFI 6 on the front panel DIO connector.\n'
                },
                'name': 'DIO6',
                'value': 'DIO/PFI6',
                'order': 23
            },
            {
                'documentation': {
                    'description': ' PFI 7 on the front panel DIO connector.\n'
                },
                'name': 'DIO7',
                'value': 'DIO/PFI7',
                'order': 24
            }
        ]
    },
    'ConfigListTriggerDigEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the rising edge as the active edge.  The rising edge  occurs when the signal transitions from low level to high level.\n'
                },
                'name': 'RISING_EDGE',
                'value': 0
            }
        ]
    },
    'ConfigSettledEventOutputTerm': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' The signal is not exported.\n'
                },
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 0.\n'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 1.\n'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 2.\n'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 3.\n'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 4.\n'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 5.\n'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 6.\n'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841.\n'
                },
                'name': 'PXIE_DSTARC',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': ' TRIG IN/OUT terminal.\n'
                },
                'name': 'TRIG_OUT',
                'value': 'TrigOut'
            }
        ]
    },
    'ConfigurationListRepeat': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSG runs the configuration list continuously.\n'
                },
                'name': 'CONFIGURATION_LIST_REPEAT_CONTINUOUS',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' NI-RFSG runs the configuration list only once.'
                },
                'name': 'CONFIGURATION_LIST_REPEAT_SINGLE',
                'value': 1
            }
        ]
    },
    'DeembeddingType': {
        'values': [
            {
                'documentation': {
                    'description': ' De-embedding is not applied to the measurement. '
                },
                'name': 'NONE',
                'value': 25000
            },
            {
                'documentation': {
                    'description': ' De-embeds the measurement using only the gain term.'
                },
                'name': 'SCALAR',
                'value': 25001
            },
            {
                'documentation': {
                    'description': ' De-embeds the measurement using the gain term and the reflection term.'
                },
                'name': 'VECTOR',
                'value': 25002
            }
        ]
    },
    'DigitalEdgeConfigurationListStepTriggerSource': {
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
                'name': 'PFI2',
                'value': 'PFI2'
            },
            {
                'name': 'PFI3',
                'value': 'PFI3'
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
                'name': 'MARKER0_EVENT',
                'value': 'Marker0Event'
            },
            {
                'name': 'MARKER1_EVENT',
                'value': 'Marker1Event'
            },
            {
                'name': 'MARKER2_EVENT',
                'value': 'Marker2Event'
            },
            {
                'name': 'MARKER3_EVENT',
                'value': 'Marker3Event'
            },
            {
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'name': 'TRIG_IN',
                'value': 'TrigIn'
            }
        ]
    },
    'DigitalEdgeEdge': {
        'values': [
            {
                'documentation': {
                    'description': ' Occurs when the signal transitions from low level to high level. \n'
                },
                'name': 'RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Occurs when the signal transitions from high level to low level. \n'
                },
                'name': 'FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'DigitalEdgeScriptTriggerIdentifier': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'SCRIPT_TRIGGER0',
                'value': 'scriptTrigger0'
            },
            {
                'name': 'SCRIPT_TRIGGER1',
                'value': 'scriptTrigger1'
            },
            {
                'name': 'SCRIPT_TRIGGER2',
                'value': 'scriptTrigger2'
            },
            {
                'name': 'SCRIPT_TRIGGER3',
                'value': 'scriptTrigger3'
            }
        ]
    },
    'DigitalLevelActiveLevel': {
        'values': [
            {
                'documentation': {
                    'description': ' Trigger when the digital trigger signal is high. \n'
                },
                'name': 'ACTIVE_HIGH',
                'value': 9000
            },
            {
                'documentation': {
                    'description': ' Trigger when the digital trigger signal is low. \n'
                },
                'name': 'ACTIVE_LOW',
                'value': 9001
            }
        ]
    },
    'DigitalModulationType': {
        'values': [
            {
                'documentation': {
                    'description': ' Disables digital modulation.\n'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Specifies that the digital modulation type is frequency-shift keying  (FSK).\n'
                },
                'name': 'FSK',
                'value': 4000
            },
            {
                'documentation': {
                    'description': ' Specifies that the digital modulation type is on-off keying (OOK).\n'
                },
                'name': 'OOK',
                'value': 4001
            },
            {
                'documentation': {
                    'description': ' Specifies that the digital modulation type is PSK.\n'
                },
                'name': 'PSK',
                'value': 4002
            }
        ]
    },
    'DigitalModulationWaveformType': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the digital modulation waveform type is pseudorandom bit  sequence (PRBS).\n'
                },
                'name': 'PRBS',
                'value': 5000
            },
            {
                'documentation': {
                    'description': ' Specifies that the digital modulation waveform type is user defined. To  specify the user-defined waveform, call the  niRFSG_ConfigureDigitalModulationUserDefinedWaveform function.\n'
                },
                'name': 'USER_DEFINED',
                'value': 5001
            }
        ]
    },
    'EnableValues': {
        'values': [
            {
                'documentation': {
                    'description': ' Enabled'
                },
                'name': 'ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' Disabled'
                },
                'name': 'DISABLE',
                'value': 0
            }
        ]
    },
    'FrequencySettlingUnits': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the value in Frequency Settling is the time to wait after the  frequency PLL locks.\n'
                },
                'name': 'TIME_AFTER_LOCK',
                'value': 12000
            },
            {
                'documentation': {
                    'description': ' Specifies the value in Frequency Settling is the time to wait after all  writes to change the frequency occur.\n'
                },
                'name': 'TIME_AFTER_IO',
                'value': 12001
            },
            {
                'documentation': {
                    'description': ' Specifies the value in Frequency Settling is the minimum frequency  accuracy when settling completes. Units are in parts per million (PPM or  1E-6).\n'
                },
                'name': 'PPM',
                'value': 12002
            }
        ]
    },
    'GenerationMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures the RF signal generator to generate a CW signal. \n'
                },
                'name': 'CW',
                'value': 1000
            },
            {
                'documentation': {
                    'description': ' Configures the RF signal generator to generate the arbitrary waveform  specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute. \n'
                },
                'name': 'ARB_WAVEFORM',
                'value': 1001
            },
            {
                'documentation': {
                    'description': ' Configures the RF signal generator to generate arbitrary waveforms as  directed by the NIRFSG_ATTR_SELECTED_SCRIPT attribute. \n'
                },
                'name': 'SCRIPT',
                'value': 1002
            }
        ]
    },
    'IqOffsetUnits': {
        'values': [
            {
                'name': 'PERCENT',
                'value': 11000
            },
            {
                'name': 'VOLTS',
                'value': 11001
            }
        ]
    },
    'IqOutPortTermConfig': {
        'values': [
            {
                'documentation': {
                    'description': ' Sets the terminal configuration to differential. \n'
                },
                'name': 'DIFFERENTIAL',
                'value': 15000
            },
            {
                'documentation': {
                    'description': ' Sets the terminal configuration to single-ended. \n'
                },
                'name': 'SINGLE_ENDED',
                'value': 15001
            }
        ]
    },
    'LinearInterpolationFormat': {
        'values': [
            {
                'name': 'REAL_AND_IMAGINARY',
                'value': 26000
            },
            {
                'name': 'MAGNITUDE_AND_PHASE',
                'value': 26001
            },
            {
                'name': 'MAGNITUDE_DB_AND_PHASE',
                'value': 26002
            }
        ]
    },
    'ListStepTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': ' Generation starts immediately.  No trigger is configured. \n'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a digital edge is detected.  The  source  of the digital edge is specified in the   NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active  edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE  attribute. \n'
                },
                'name': 'DIGITAL_EDGE',
                'value': 1
            }
        ]
    },
    'LoSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated  within the device itself. \n\n PXIe-5840 with PXIe-5653: If the center frequency is greater than or equal to 3.2 GHz,  this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz,  this configuration uses the PXIe-5840 internal LO. \n PXIe-5841 with PXIe-5655: This configuration uses the onboard LO of the PXIe-5655. \n'
                },
                'name': 'ONBOARD',
                'value': 'Onboard'
            },
            {
                'documentation': {
                    'description': ' Uses an external LO as the LO source. Connect a signal to the LO IN connector on  the device and use the NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attribute to specify the LO frequency. \n'
                },
                'name': 'LO_IN',
                'value': 'LO_In'
            },
            {
                'documentation': {
                    'description': ' Uses the PXIe-5840 internal LO as the LO source. This value is valid on only the PXIe-5840 with PXIe-5653.'
                },
                'name': 'SECONDARY',
                'value': 'Secondary'
            },
            {
                'documentation': {
                    'description': ' Uses the same internal LO during some RX and TX operations. In this mode, an internal synthesizer  is chosen by the driver and the synthesizer signal is switched to both the RF In and RF Out mixers.  This value is valid on only the PXIe-5830/5831/5841 with PXIe-5655. \n'
                },
                'name': 'SG_SA_SHARED',
                'value': 'SG_SA_Shared'
            },
            {
                'documentation': {
                    'description': ' NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841. \n'
                },
                'name': 'AUTOMATIC_SG_SA_SHARED',
                'value': 'Automatic_SG_SA_Shared'
            }
        ]
    },
    'LoadOptions': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSG loads all the configurations to the session.'
                },
                'name': 'SKIP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' NI-RFSG skips loading the waveform configurations to the session.'
                },
                'name': 'SKIP_WAVEFORMS',
                'value': 1
            }
        ]
    },
    'LoopBandwidth': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the device uses a narrow loop bandwidth.\n'
                },
                'name': 'NARROW',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Specifies that the device uses a medium loop bandwidth.\n'
                },
                'name': 'MEDIUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' Specifies that the device uses a wide loop bandwidth.\n'
                },
                'name': 'WIDE',
                'value': 2
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the Marker Event output behavior as pulse.  \n'
                },
                'name': 'PULSE',
                'value': 23000
            },
            {
                'documentation': {
                    'description': ' Specifies the Marker Event output behavior as toggle. \n'
                },
                'name': 'TOGGLE',
                'value': 23001
            }
        ]
    },
    'MarkerEventPulseWidthUnits': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the Marker Event pulse width units as seconds.  \n'
                },
                'name': 'SECONDS',
                'value': 22000
            },
            {
                'documentation': {
                    'description': ' Specifies the Marker Event pulse width units as Sample Clock periods. \n'
                },
                'name': 'SAMPLE_CLOCK_PERIODS',
                'value': 22001
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies the initial state of the Marker Event toggle behavior as digital low. \n'
                },
                'name': 'DIGITAL_LOW',
                'value': 21000
            },
            {
                'documentation': {
                    'description': ' Specifies the initial state of the Marker Event toggle behavior as digital high. \n'
                },
                'name': 'DIGITAL_HIGH',
                'value': 21001
            }
        ]
    },
    'Module': {
        'values': [
            {
                'name': 'PRIMARY_MODULE',
                'value': 13000
            },
            {
                'name': 'AWG',
                'value': 13001
            },
            {
                'name': 'LO',
                'value': 13002
            }
        ]
    },
    'OutputPort': {
        'values': [
            {
                'documentation': {
                    'description': ' Enables the RF OUT port. \n'
                },
                'name': 'RF_OUT',
                'value': 14000
            },
            {
                'documentation': {
                    'description': ' Enables the I/Q OUT port. \n'
                },
                'name': 'IQ_OUT',
                'value': 14001
            },
            {
                'documentation': {
                    'description': ' Enables the CAL OUT port. \n'
                },
                'name': 'CAL_OUT',
                'value': 14002
            },
            {
                'documentation': {
                    'description': ' Enables the I connectors of the I/Q OUT port. \n'
                },
                'name': 'I_ONLY',
                'value': 14003
            }
        ]
    },
    'OutputSignal': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'name': 'PFI4',
                'value': 'PFI4'
            },
            {
                'name': 'PFI5',
                'value': 'PFI5'
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
                'name': 'REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'name': 'REF_OUT',
                'value': 'RefOut'
            },
            {
                'name': 'TRIG_OUT',
                'value': 'TrigOut'
            }
        ]
    },
    'OverflowErrorReporting': {
        'values': [
            {
                'documentation': {
                    'description': ' Configures NI-RFSG to return a warning when an OSP overflow occurs.'
                },
                'name': 'WARNING',
                'value': 1301
            },
            {
                'documentation': {
                    'description': ' Configures NI-RFSG to not return an error or a warning when an OSP overflow occurs.'
                },
                'name': 'DISABLED',
                'value': 1302
            }
        ]
    },
    'PPAScriptInheritance': {
        'values': [
            {
                'documentation': {
                    'description': ' Errors out if different values are detected in the script.\n'
                },
                'name': 'EXACT_MATCH',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Uses the minimum value found in the script.\n'
                },
                'name': 'MINIMUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' Uses the maximum value found in the script.\n'
                },
                'name': 'MAXIMUM',
                'value': 2
            }
        ]
    },
    'PXIChassisClk10': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Do not drive the PXI_CLK10 signal.\n'
                },
                'name': 'NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': ' Use the highly stable oven-controlled onboard Reference Clock to drive  the PXI_CLK10 signal. This value is not valid on the PXIe-5672.\n'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' Use the clock present at the front panel REF IN connector to drive the  PXI_CLK10 signal.\n'
                },
                'name': 'REF_IN',
                'value': 'RefIn'
            }
        ]
    },
    'PhaseContinuity': {
        'values': [
            {
                'documentation': {
                    'description': ' Auto'
                },
                'name': 'AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': ' Enabled'
                },
                'name': 'ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' Disabled'
                },
                'name': 'DISABLE',
                'value': 0
            }
        ]
    },
    'PowerLevelType': {
        'values': [
            {
                'documentation': {
                    'description': ' Specifies that the power level type is average power. Average power  indicates the desired power averaged in time. The driver maximizes the  dynamic range by scaling the IQ waveform. If you write more than one  waveform, NI-RFSG scales each waveform without preserving the power level  ratio between the waveforms. This value is not valid for the PXIe-5820. \n'
                },
                'name': 'AVERAGE_POWER',
                'value': 7000
            },
            {
                'documentation': {
                    'description': ' Specifies that the power level type is peak power. Peak power indicates  the maximum power level of the RF signal averaged over one period of the  RF carrier signal frequency (the peak envelope power). This setting  requires that the magnitude of the IQ waveform must always be less than  or equal to one. When using the peak power level type, the power level of  the RF signal matches the specified power level at moments when the  magnitude of the IQ waveform equals one. If you write more than one  waveform, the relative scaling between waveforms is preserved.\n'
                },
                'name': 'PEAK_POWER',
                'value': 7001
            }
        ]
    },
    'PulseModulationMode': {
        'values': [
            {
                'documentation': {
                    'description': ' Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation.  \n'
                },
                'name': 'OPTIMAL_MATCH',
                'value': 20000
            },
            {
                'documentation': {
                    'description': ' Allows for the best on/off power ratio of the pulsed signal. \n'
                },
                'name': 'HIGH_ISOLATION',
                'value': 20001
            }
        ]
    },
    'RefClockOutputTerm': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Do not export the Reference Clock.\n'
                },
                'name': 'DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': ' Export the Reference Clock signal to the REF OUT connector of the device.\n'
                },
                'name': 'REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': ' Export the Reference Clock signal to the REF OUT2 connector of the device, if applicable.\n'
                },
                'name': 'REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': ' Export the Reference Clock signal to the CLK OUT connector of the device.\n'
                },
                'name': 'CLK_OUT',
                'value': 'ClkOut'
            }
        ]
    },
    'RefClockRate': {
        'values': [
            {
                'name': '10_MHZ',
                'value': 10000000
            },
            {
                'name': 'AUTO',
                'value': -1
            }
        ]
    },
    'RefClockSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' Uses the onboard Reference Clock as the clock source.\n PXIe-5830/5831—For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector.  For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. \n PXIe-5831 with PXIe-5653—Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.  Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. \n PXIe-5840 with PXIe-5653—Lock to the PXIe-5653 onboard clock. Connect the REF OUT (10 MHz)  connector on the PXIe-5653 to the PXIe-5840 REF IN connector. Configure open NI-RFSA  sessions to the device to use NIRFSA_VAL_REF_IN_STR for the PXIe-5840 or  NIRFSA_VAL_REF_IN_2_STR for the PXIe-5840 with PXIe-5653. \n PXIe-5841 with PXIe-5655—Lock to the PXIe-5655 onboard clock. Connect the REF OUT  connector on the PXIe-5655 to the PXIe-5841 REF IN connector. \n'
                },
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': ' Use the clock signal present at the front panel RefIn connector as the  clock source.\n PXIe-5830/5831—For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector.  For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830,  lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external  signal to the PXIe-3622 REF IN connector. \n PXIe-5831 with PXIe-5653—Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.  Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  PXIe-5840 with PXIe-5653—Lock to the PXIe-5653 onboard clock.  Connect the REF OUT (10 MHz) connector on the PXIe-5653 to the PXIe-5840 REF IN connector. \n PXIe-5841 with PXIe-5655—Lock to the signal at the REF IN connector on the associated PXIe-5655.  Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. \n'
                },
                'name': 'REF_IN',
                'value': 'RefIn'
            },
            {
                'documentation': {
                    'description': ' Use the PXI_CLK signal, which is present on the PXI backplane, as the  clock source.\n'
                },
                'name': 'PXI_CLK',
                'value': 'PXI_CLK'
            },
            {
                'documentation': {
                    'description': ' Use the clock signal present at the front panel ClkIn connector as the  clock source. This value is not valid for the PXIe-5644/5645/5646 or  PXIe-5820/5830/5831/5831 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655. \n'
                },
                'name': 'CLK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': ' This value is valid on only the PXIe-5840 with PXIe-5653. NI-RFSG locks the  Reference Clock to the clock sourced at the PXIe-5840 REF IN terminal that is already  configured by an NI-RFSA session. Connect the PXIe-5840 REF OUT connector to the PXIe-5653  REF IN connector. Configure open NI-RFSA sessions to the device to use NIRFSA_VAL_REF_IN_STR  for the PXIe-5840 or NIRFSA_VAL_ONBOARD_CLOCK_STR for the PXIe-5840 with PXIe-5653. \n'
                },
                'name': 'REF_IN_2',
                'value': 'RefIn2'
            },
            {
                'documentation': {
                    'description': ' This value is valid on only the PXIe-5831 with PXIe-5653 and the PXIe-5840 with PXIe-5653.  PXIe-5831 with PXIe-5653—NI-RFSG configures the PXIe-5653 to export the Reference clock and  configures the PXIe-5820 and PXIe-3622 to use NIRFSG_VAL_PXI_CLK_STR as the Reference Clock source.  Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. \n PXIe-5840 with PXIe-5653—NI-RFSG configures the  PXIe-5653 to export the Reference Clock, and configures the PXIe-5840 to use  NIRFSG_VAL_PXI_CLK_STR. Connect the PXIe-5653 REF OUT (10 MHz) connector to the  PXI chassis REF IN connector. For best performance, configure all other devices  in the system to use NIRFSG_VAL_PXI_CLK_STR as the Reference Clock source. \n'
                },
                'name': 'PXI_CLK_MASTER',
                'value': 'PXI_ClkMaster'
            }
        ]
    },
    'RelativeTo': {
        'values': [
            {
                'name': 'START_OF_WAVEFORM',
                'value': 8000
            },
            {
                'name': 'CURRENT_POSITION',
                'value': 8001
            }
        ]
    },
    'ResetOptions': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSG resets all the configurations.'
                },
                'name': 'SKIP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' NI-RFSG skips resetting the waveform configurations.'
                },
                'name': 'SKIP_WAVEFORMS',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' NI-RFSG skips resetting the scripts.'
                },
                'name': 'SKIP_SCRIPTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': ' NI-RFSG skips resetting the de-embeding tables.'
                },
                'name': 'SKIP_DEEMBEDING_TABLES',
                'value': 8
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
                'name': 'WAVEFORMS',
                'value': 1
            },
            {
                'name': 'SCRIPTS',
                'value': 2
            },
            {
                'name': 'ROUTES',
                'value': 4
            },
            {
                'name': 'DEEMBEDDING_TABLES',
                'value': 8
            }
        ]
    },
    'RfInLoExportEnabled': {
        'values': [
            {
                'name': 'UNSPECIFIED',
                'value': -2
            },
            {
                'name': 'DISABLE',
                'value': 0
            },
            {
                'name': 'ENABLE',
                'value': 1
            }
        ]
    },
    'RoutedSignal': {
        'values': [
            {
                'name': 'CONFIGURATION_LIST_STEP_TRIGGER',
                'value': 6
            },
            {
                'name': 'CONFIGURATION_SETTLED_EVENT',
                'value': 7
            },
            {
                'name': 'DONE_EVENT',
                'value': 5
            },
            {
                'name': 'MARKER_EVENT',
                'value': 2
            },
            {
                'name': 'REF_CLOCK',
                'value': 3
            },
            {
                'name': 'SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'name': 'STARTED_EVENT',
                'value': 4
            },
            {
                'name': 'START_TRIGGER',
                'value': 0
            }
        ]
    },
    'SParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 24000
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 24001
            }
        ]
    },
    'ScriptTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': ' Setting trigger attributes to this value specifies that no trigger is   configured. Signal generation starts immediately. \n'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a digital edge is detected. The  source of the digital edge is specified in the  NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE attribute, and the active edge is  specified in the NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE attribute. \n'
                },
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a digital level is detected. The  source of the digital level is specified in the  NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, and the active level is  specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute. \n'
                },
                'name': 'DIGITAL_LEVEL',
                'value': 8000
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a software event occurs. You may  create a software event by calling the niRFSG_SendSoftwareEdgeTrigger function. \n'
                },
                'name': 'SOFTWARE',
                'value': 2
            }
        ]
    },
    'SelfCalibrateRangeStepsToOmit': {
        'values': [
            {
                'name': 'OMIT_NONE',
                'value': 0
            },
            {
                'name': 'LO_SELF_CAL',
                'value': 1
            },
            {
                'name': 'POWER_LEVEL_ACCURACY',
                'value': 2
            },
            {
                'name': 'RESIDUAL_LO_POWER',
                'value': 4
            },
            {
                'name': 'IMAGE_SUPPRESSION',
                'value': 8
            },
            {
                'name': 'SYNTHESIZER_ALIGNMENT',
                'value': 16
            }
        ]
    },
    'SignalIdentifier': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'NONE',
                'value': ''
            },
            {
                'name': 'SCRIPT_TRIGGER0',
                'value': 'scriptTrigger0'
            },
            {
                'name': 'SCRIPT_TRIGGER1',
                'value': 'scriptTrigger1'
            },
            {
                'name': 'SCRIPT_TRIGGER2',
                'value': 'scriptTrigger2'
            },
            {
                'name': 'SCRIPT_TRIGGER3',
                'value': 'scriptTrigger3'
            },
            {
                'name': 'MARKER0',
                'value': 'marker0'
            },
            {
                'name': 'MARKER1',
                'value': 'marker1'
            },
            {
                'name': 'MARKER2',
                'value': 'marker2'
            },
            {
                'name': 'MARKER3',
                'value': 'marker3'
            }
        ]
    },
    'StartTriggerType': {
        'values': [
            {
                'documentation': {
                    'description': ' Setting trigger attributes to this value specifies that no trigger is  configured. \n'
                },
                'name': 'NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a digital edge is detected. The  source of the digital edge is specified in the  NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active  edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE  attribute. \n'
                },
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' The data operation does not start until a software event occurs. You may  create a software event by calling the niRFSG_SendSoftwareEdgeTrigger function. \n'
                },
                'name': 'SOFTWARE',
                'value': 2
            },
            {
                'documentation': {
                    'description': ' Data operation does not start until the endpoint reaches a threshold  specified in the NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL  attribute. \n'
                },
                'name': 'P2_P_ENDPOINT_FULLNESS',
                'value': 3
            }
        ]
    },
    'TriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel SMB connector.\n'
                },
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel SMB connector.\n'
                },
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': ' PFI 2 on the front panel DDC connector.\n'
                },
                'name': 'PFI2',
                'value': 'PFI2'
            },
            {
                'documentation': {
                    'description': ' PFI 3 on the front panel DDC connector.\n'
                },
                'name': 'PFI3',
                'value': 'PFI3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 0.\n'
                },
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 1.\n'
                },
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 2.\n'
                },
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 3.\n'
                },
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 4.\n'
                },
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 5.\n'
                },
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 6.\n'
                },
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': ' PXI trigger line 7.\n'
                },
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': ' PXI Star trigger line. This value is not valid on the PXIe-5644/5645/5646.\n'
                },
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': ' PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5840/5841/5842/5860. \n'
                },
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': ' Sync Start trigger line.'
                },
                'name': 'SYNC_START_TRIGGER',
                'value': 'Sync_Start'
            },
            {
                'documentation': {
                    'description': ' Sync script trigger line.'
                },
                'name': 'SYNC_SCRIPT_TRIGGER',
                'value': 'Sync_Script'
            },
            {
                'documentation': {
                    'description': ' TRIG IN/OUT terminal.\n'
                },
                'name': 'TRIG_IN',
                'value': 'TrigIn'
            },
            {
                'documentation': {
                    'description': ' PULSE IN terminal.\n'
                },
                'name': 'PULSE_IN',
                'value': 'PulseIn',
                'order': 25
            },
            {
                'documentation': {
                    'description': ' PFI 0 on the front panel DIO connector.\n'
                },
                'name': 'DIO0',
                'value': 'DIO/PFI0',
                'order': 26
            },
            {
                'documentation': {
                    'description': ' PFI 1 on the front panel DIO connector.\n'
                },
                'name': 'DIO1',
                'value': 'DIO/PFI1',
                'order': 27
            },
            {
                'documentation': {
                    'description': ' PFI 2 on the front panel DIO connector.\n'
                },
                'name': 'DIO2',
                'value': 'DIO/PFI2',
                'order': 28
            },
            {
                'documentation': {
                    'description': ' PFI 3 on the front panel DIO connector.\n'
                },
                'name': 'DIO3',
                'value': 'DIO/PFI3',
                'order': 29
            },
            {
                'documentation': {
                    'description': ' PFI 4 on the front panel DIO connector.\n'
                },
                'name': 'DIO4',
                'value': 'DIO/PFI4',
                'order': 30
            },
            {
                'documentation': {
                    'description': ' PFI 5 on the front panel DIO connector.\n'
                },
                'name': 'DIO5',
                'value': 'DIO/PFI5',
                'order': 31
            },
            {
                'documentation': {
                    'description': ' PFI 6 on the front panel DIO connector.\n'
                },
                'name': 'DIO6',
                'value': 'DIO/PFI6',
                'order': 32
            },
            {
                'documentation': {
                    'description': ' PFI 7 on the front panel DIO connector.\n'
                },
                'name': 'DIO7',
                'value': 'DIO/PFI7',
                'order': 33
            }
        ]
    },
    'UpconverterFrequencyOffsetMode': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the  NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. '
                },
                'name': 'AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': ' NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute  has been set and can be avoided. NI-RFSG returns an error if unable to avoid the specified signal bandwidth,  or if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has not been set. '
                },
                'name': 'ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': ' NI-RFSG uses the offset that you specified with the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET  or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes. '
                },
                'name': 'USER_DEFINED',
                'value': 5001
            }
        ]
    },
    'WriteWaveformBurstDetectionMode': {
        'values': [
            {
                'documentation': {
                    'description': ' NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.'
                },
                'name': 'AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': ' User sets the burst detection parameters.'
                },
                'name': 'MANUAL',
                'value': 0
            }
        ]
    },
    'YigMainCoil': {
        'values': [
            {
                'documentation': {
                    'description': ' Adjusts the YIG main coil for an underdampened response. \n'
                },
                'name': 'SLOW',
                'value': 0
            },
            {
                'documentation': {
                    'description': ' Adjusts the YIG main coil for an overdampened response. \n'
                },
                'name': 'FAST',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nirfsg/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/functions.py sha256=c6ee2b05252b551e0e0238be8cd9f52b4bd13f7c43779069d0d4cf90b621f289 bytes=73687 -->
## FILE: source/codegen/metadata/nirfsg/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/functions.py`
- sha256: `c6ee2b05252b551e0e0238be8cd9f52b4bd13f7c43779069d0d4cf90b621f289`
- bytes: 73687

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
    'AllocateArbWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'sizeInSamples',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
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
    'CheckAttributeViInt32': {
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
    'CheckAttributeViInt64': {
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
    'CheckAttributeViReal64': {
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
    'CheckAttributeViSession': {
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
    'CheckAttributeViString': {
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
    'CheckGenerationStatus': {
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
    'CheckIfConfigurationListExists': {
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
                'direction': 'out',
                'name': 'listExists',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfScriptExists': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'scriptName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'scriptExists',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckIfWaveformExists': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'waveformExists',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearAllArbWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'name',
                'type': 'ViConstString'
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
        'cname': 'niRFSG_close',
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
    'ConfigureDigitalEdgeConfigurationListStepTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeConfigurationListStepTriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeScriptTriggerIdentifier',
                'name': 'triggerID',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'TriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32'
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
                'enum': 'TriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeEdge',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeScriptTriggerIdentifier',
                'name': 'triggerID',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'TriggerSource',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'DigitalLevelActiveLevel',
                'name': 'level',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalModulationUserDefinedWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'userDefinedWaveform',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureGenerationMode': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'GenerationMode',
                'name': 'generationMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputEnabled': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'outputEnabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureP2PEndpointFullnessStartTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'p2pEndpointFullnessLevel',
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
                'enum': 'PXIChassisClk10',
                'name': 'pxiClk10Source',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePowerLevelType': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'PowerLevelType',
                'name': 'powerLevelType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRF': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'powerLevel',
                'type': 'ViReal64'
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
                'name': 'refClockSource',
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
    'ConfigureSignalBandwidth': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'signalBandwidth',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareScriptTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeScriptTriggerIdentifier',
                'name': 'triggerID',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareStartTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureUpconverterPLLSettlingTime': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'pllSettlingTime',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'ensurePLLLocked',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reservedForFutureUse',
                'type': 'ViInt32'
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
                'name': 'numberOfAttributes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'configurationListAttributes',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfAttributes'
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
                'enum': 'SParameterOrientation',
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
                'enum': 'SParameterOrientation',
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
    'DeleteScript': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'scriptName',
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
    'DisableAllModulation': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableConfigurationListStepTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableScriptTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeScriptTriggerIdentifier',
                'name': 'triggerID',
                'type': 'ViConstString'
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
    'ErrorMessage': {
        'cname': 'niRFSG_error_message',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
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
        'cname': 'niRFSG_error_query',
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
                'enum': 'RoutedSignal',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'enum': 'SignalIdentifier',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'OutputSignal',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllNamedWaveformNames': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'waveformNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualBufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllScriptNames': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'scriptNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualBufferSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetScript': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'scriptName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'Script',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualBufferSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'actualBufferSize',
                'type': 'ViInt32'
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
    'GetChannelName': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
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
    'GetExternalCalibrationLastDateAndTime': {
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
            },
            {
                'direction': 'out',
                'name': 'second',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetMaxSettablePower': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationDateAndTime': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Module',
                'name': 'module',
                'type': 'ViInt32'
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
            },
            {
                'direction': 'out',
                'name': 'second',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalibrationTemperature': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'Module',
                'name': 'module',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'temperature',
                'type': 'ViReal64'
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
                'enum': 'RoutedSignal',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'enum': 'SignalIdentifier',
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
                    'mechanism': 'ivi-dance',
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
    'GetWaveformBurstStartLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'requiredSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetWaveformBurstStopLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'requiredSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetWaveformMarkerEventLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'locations',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'numberOfLocations',
                    'value_twist': 'requiredSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'name': 'requiredSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niRFSG_init',
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
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'newVi',
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
                'name': 'resetDevice',
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
    'PerformPowerSearch': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
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
    'QueryArbWaveformCapabilities': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'maxNumberWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'waveformQuantum',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'minWaveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'maxWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadAndDownloadWaveformFromFileTDMS': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'waveformIndex',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niRFSG_reset',
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
        'cname': 'niRFSG_revision_query',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'name': 'firmwareRevision',
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
    'SelectArbWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'name',
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
    'SelfCalibrateRange': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'enum': 'SelfCalibrateRangeStepsToOmit',
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
                'name': 'minPowerLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'maxPowerLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niRFSG_self_test',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'selfTestMessage',
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
                'enum': 'RoutedSignal',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'enum': 'SignalIdentifier',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetArbWaveformNextWritePosition': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViInt32'
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
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'bufferSize'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStartLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformBurstStopLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformMarkerEventLocations': {
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
                'name': 'numberOfLocations',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'locations',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfLocations'
                },
                'type': 'ViReal64[]'
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
    },
    'WaitUntilSettled': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'maxTimeMilliseconds',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'iData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'qData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'moreDataPending',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumberF32',
                'name': 'wfmData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumberF32_struct[]'
            },
            {
                'direction': 'in',
                'name': 'moreDataPending',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'wfmData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'moreDataPending',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformComplexI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'wfmData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'NIComplexI16_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteArbWaveformF32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'iData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal32[]'
            },
            {
                'direction': 'in',
                'name': 'qData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViReal32[]'
            },
            {
                'direction': 'in',
                'name': 'moreDataPending',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteScript': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nirfsg/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfsg_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nirfsg_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/attributes_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfsg_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/attributes_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/config.py sha256=6008b51f980a2ab1275a9389a67a6784aebeae88c2dc16b8d5177eee48755410 bytes=1219 -->
## FILE: source/codegen/metadata/nirfsg_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/config.py`
- sha256: `6008b51f980a2ab1275a9389a67a6784aebeae88c2dc16b8d5177eee48755410`
- bytes: 1219

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '23.0.0',
    'c_header': 'niRFSGPrivate.h',
    'c_function_prefix': 'niRFSG_',
    'service_class_prefix': 'NiRFSGRestricted',
    'java_package': 'com.ni.grpc.rfsgrestricted',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFSGRestricted',
    'namespace_component': 'nirfsg_restricted',
    'close_function': None,
    'custom_types': [],
    'additional_headers': {'custom/ivi_errors.h': ['service.cpp']},
    'code_readiness': 'Release',
    'driver_name': 'NI-RFSG-RESTRICTED',
    'is_restricted': True,
    'status_ok': 'status >= 0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfsg',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFSG_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFSG_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'module_name': 'nirfsg_restricted',
    'session_handle_parameter_name': 'vi',
    'duplicate_resource_handles_allowed': True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/config_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfsg_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/config_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/enums.py sha256=a65c5e04ce4623f173a729fdfcbfe50380975cc7285e6708b3e5a717f925983f bytes=302 -->
## FILE: source/codegen/metadata/nirfsg_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/enums.py`
- sha256: `a65c5e04ce4623f173a729fdfcbfe50380975cc7285e6708b3e5a717f925983f`
- bytes: 302

````python
enums = {
    'SParameterOrientation': {
        'values': [
            {
                'name': 'PORT1_TOWARDS_DUT',
                'value': 24000
            },
            {
                'name': 'PORT2_TOWARDS_DUT',
                'value': 24001
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/enums_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfsg_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/enums_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/functions.py sha256=c847c95aebb2a072fdcf39191edaf2c77bea29d53b52c4b9573405767cbd6bf4 bytes=5005 -->
## FILE: source/codegen/metadata/nirfsg_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/functions.py`
- sha256: `c847c95aebb2a072fdcf39191edaf2c77bea29d53b52c4b9573405767cbd6bf4`
- bytes: 5005

````python
functions = {
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
    'ErrorMessage': {
        'cname': 'niRFSG_error_message',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
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
    'CreateDeembeddingSparameterTable': {
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
                'name': 'numberOfFrequencies',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSparameterTableFrequencies': {
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
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSparameterTableSparameters': {
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
                'enum': 'SParameterOrientation',
                'name': 'sparameterOrientation',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeembeddingTableNumberOfPorts': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'numberOfPorts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfsg_restricted/functions_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfsg_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfsg_restricted/functions_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/__init__.py sha256=4f7091ddacba9e112e08cde0cd52181f876a59f36f39519bc0c6d3ce904da0a4 bytes=714 -->
## FILE: source/codegen/metadata/niscope/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/__init__.py`
- sha256: `4f7091ddacba9e112e08cde0cd52181f876a59f36f39519bc0c6d3ce904da0a4`
- bytes: 714

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/attributes.py sha256=63fee5d16466d2eaae840ea56935c94871e21fb5fb6e96e54278a930d47fce48 bytes=43319 -->
## FILE: source/codegen/metadata/niscope/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/attributes.py`
- sha256: `63fee5d16466d2eaae840ea56935c94871e21fb5fb6e96e54278a930d47fce48`
- bytes: 43319

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 23.3.0d127
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'HORZ_NUM_RECORDS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150002: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INPUT_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150003: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'OUTPUT_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'HORZ_ENFORCE_REALTIME',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150005: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'BINARY_SAMPLE_WIDTH',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150006: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_HYSTERESIS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'CLOCK_SYNC_PULSE_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150008: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'MASTER_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150009: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MIN_SAMPLE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150012: {
        'codegen_method': 'public',
        'enum': 'TriggerWindowMode',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_WINDOW_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150013: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_WINDOW_LOW_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150014: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_WINDOW_HIGH_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150016: {
        'codegen_method': 'public',
        'enum': 'MeasRefLevelUnits',
        'grpc_type': 'sint32',
        'name': 'MEAS_REF_LEVEL_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150018: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'MEAS_OTHER_CHANNEL',
        'resettable': True,
        'type': 'ViString'
    },
    1150019: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_HYSTERESIS_PERCENT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150020: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_LAST_ACQ_HISTOGRAM_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150021: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150022: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150023: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150024: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_TIME_HISTOGRAM_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150025: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_VOLTS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150026: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_VOLTS',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150027: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150028: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150029: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_POLYNOMIAL_INTERPOLATION_ORDER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150030: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_INTERPOLATION_SAMPLING_FACTOR',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150031: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_FILTER_CUTOFF_FREQ',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150032: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_FILTER_CENTER_FREQ',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150033: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_FILTER_RIPPLE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150034: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150035: {
        'codegen_method': 'public',
        'enum': 'MeasFilterType',
        'grpc_type': 'sint32',
        'name': 'MEAS_FILTER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150036: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_FILTER_ORDER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150037: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEAS_FILTER_TAPS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150038: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_CHAN_LOW_REF_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150039: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_CHAN_MID_REF_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150040: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_CHAN_HIGH_REF_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150041: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_FILTER_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150042: {
        'codegen_method': 'public',
        'enum': 'FIRFilterWindow',
        'grpc_type': 'sint32',
        'name': 'MEAS_FIR_FILTER_WINDOW',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150043: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_ARRAY_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150044: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_ARRAY_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150045: {
        'codegen_method': 'public',
        'enum': 'MeasPercentageMethod',
        'grpc_type': 'sint32',
        'name': 'MEAS_PERCENTAGE_METHOD',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150053: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ACQ_ARM_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150066: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_PROBE_COMP_ON',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150067: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'USE_SPEC_INITIAL_X',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150068: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150069: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ONBOARD_MEMORY_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150070: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'RIS_NUM_AVERAGES',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150071: {
        'codegen_method': 'public',
        'enum': 'RISMethod',
        'grpc_type': 'sint32',
        'name': 'RIS_METHOD',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150072: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'FETCH_INTERLEAVED_DATA',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150073: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_REAL_TIME_SAMPLING_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150074: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_RIS_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150075: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150076: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DEVICE_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150077: {
        'codegen_method': 'public',
        'enum': 'FetchRelativeTo',
        'grpc_type': 'sint32',
        'name': 'FETCH_RELATIVE_TO',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150078: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FETCH_OFFSET',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150079: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FETCH_RECORD_NUMBER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150080: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FETCH_NUM_RECORDS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150081: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FETCH_MEAS_NUM_SAMPLES',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150082: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'POINTS_DONE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150083: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'RECORDS_DONE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150084: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'BACKLOG',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150086: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DEVICE_TEMPERATURE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150087: {
        'codegen_method': 'public',
        'enum': 'SampClkTimepaceSrc',
        'grpc_type': 'string',
        'name': 'SAMP_CLK_TIMEBASE_SRC',
        'resettable': True,
        'type': 'ViString'
    },
    1150088: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SAMP_CLK_TIMEBASE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150089: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SAMP_CLK_TIMEBASE_DIV',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150090: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'REF_CLK_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150091: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150093: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'ENABLE_DC_RESTORE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150094: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ADV_TRIG_SRC',
        'resettable': True,
        'type': 'ViString'
    },
    1150095: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ARM_REF_TRIG_SRC',
        'resettable': True,
        'type': 'ViString'
    },
    1150096: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'REF_TRIG_TDC_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150097: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150098: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150099: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150100: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'POLL_INTERVAL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150101: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150102: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'RESOLUTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150103: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150104: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150105: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150106: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RIS_IN_AUTO_SETUP_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150107: {
        'codegen_method': 'public',
        'enum': 'TerminalConfiguration',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_TERMINAL_CONFIGURATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150109: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150110: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150111: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150112: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150128: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'ENABLE_TIME_INTERLEAVED_SAMPLING',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150129: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': '5V_OUT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150132: {
        'codegen_method': 'public',
        'enum': 'RuntTimeCondition',
        'grpc_type': 'sint32',
        'name': 'RUNT_TIME_CONDITION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150133: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RUNT_TIME_LOW_LIMIT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150134: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RUNT_TIME_HIGH_LIMIT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150137: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CABLE_SENSE_VOLTAGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150138: {
        'codegen_method': 'public',
        'enum': 'CableSenseMode',
        'grpc_type': 'double',
        'name': 'CABLE_SENSE_MODE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150139: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CABLE_SENSE_SIGNAL_ENABLE',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150140: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ENABLED_CHANNELS',
        'resettable': False,
        'type': 'ViString'
    },
    1150141: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'END_OF_ACQUISITION_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150142: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'END_OF_RECORD_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150143: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ADVANCE_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150144: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'REF_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150145: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'START_TRIGGER_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150146: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_ADVANCE_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150147: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_REF_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150148: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_START_EVENT_TERMINAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1150271: {
        'codegen_method': 'public',
        'enum': 'FlexFIRAntialiasFilterType',
        'grpc_type': 'sint32',
        'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150278: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'TRIGGER_AUTO_TRIGGERED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150279: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SIGNAL_COND_GAIN',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150280: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SIGNAL_COND_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150300: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DDC_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150302: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DDC_FREQUENCY_TRANSLATION_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150303: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DDC_CENTER_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150304: {
        'codegen_method': 'public',
        'enum': 'DataProcessingMode',
        'grpc_type': 'sint32',
        'name': 'DDC_DATA_PROCESSING_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150305: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150306: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150307: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DIGITAL_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150308: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DIGITAL_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150309: {
        'codegen_method': 'public',
        'enum': 'OverflowErrorReporting',
        'grpc_type': 'sint32',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150310: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DDC_Q_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150311: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'FETCH_INTERLEAVED_IQ_DATA',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150312: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'EQUALIZATION_NUM_COEFFICIENTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150313: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'EQUALIZATION_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150314: {
        'codegen_method': 'public',
        'enum': 'RefTriggerDetectorLocation',
        'grpc_type': 'sint32',
        'name': 'REF_TRIGGER_DETECTOR_LOCATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150315: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150316: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150318: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'BANDPASS_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150319: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DITHER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150320: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'FRACTIONAL_RESAMPLE_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150321: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150322: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150328: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150329: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150330: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150331: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_DESTINATION_WINDOW_ADDR',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150332: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_DESTINATION_WINDOW_ADDR_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150333: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_DESTINATION_WINDOW_SIZE',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150334: {
        'codegen_method': 'public',
        'enum': 'NotificationType',
        'grpc_type': 'sint32',
        'name': 'P2P_NOTIFY_PUSH_MESSAGE_ON',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150335: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150336: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150337: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_VALUE',
        'resettable': True,
        'type': 'ViInt64'
    },
    1150338: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150339: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'P2P_CHANNELS_TO_STREAM',
        'resettable': True,
        'type': 'ViString'
    },
    1150340: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_SAMPLES_TRANSFERRED',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150341: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150342: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150343: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_MANUAL_CONFIGURATION_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150344: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_ENDPOINT_OVERFLOW',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150345: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_FIFO_ENDPOINT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150354: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_ONBOARD_MEMORY_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150366: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150367: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SAMP_CLK_TIMEBASE_MULT',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150373: {
        'codegen_method': 'public',
        'enum': 'P2PStreamRelativeTo',
        'grpc_type': 'sint32',
        'name': 'P2P_STREAM_RELATIVE_TO',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150374: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ABSOLUTE_SAMPLE_CLOCK_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150375: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': False,
        'type': 'ViString'
    },
    1150376: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERLEAVING_OFFSET_CORRECTION_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150377: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'HIGH_PASS_FILTER_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150380: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_SAMPLES_TRANSFERRED_PER_RECORD',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151303: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'PLL_LOCK_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250001: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VERTICAL_RANGE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250002: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'VERTICAL_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250003: {
        'codegen_method': 'public',
        'enum': 'VerticalCoupling',
        'grpc_type': 'sint32',
        'name': 'VERTICAL_COUPLING',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250004: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PROBE_ATTENUATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CHANNEL_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1250006: {
        'codegen_method': 'public',
        'enum': 'MaxInputFrequency',
        'grpc_type': 'double',
        'name': 'MAX_INPUT_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'HORZ_TIME_PER_RECORD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250008: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'HORZ_RECORD_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250009: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'HORZ_MIN_NUM_PTS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250010: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'HORZ_SAMPLE_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250011: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'HORZ_RECORD_REF_POSITION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250012: {
        'codegen_method': 'public',
        'enum': 'TriggerType',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250013: {
        'codegen_method': 'public',
        'enum': 'TriggerSource',
        'grpc_type': 'string',
        'name': 'TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1250014: {
        'codegen_method': 'public',
        'enum': 'TriggerCoupling',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_COUPLING',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250015: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_DELAY_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250016: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_HOLDOFF',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250017: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TRIGGER_LEVEL',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250018: {
        'codegen_method': 'public',
        'enum': 'TriggerSlope',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SLOPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250101: {
        'codegen_method': 'public',
        'enum': 'AcquisitionType',
        'grpc_type': 'sint32',
        'name': 'ACQUISITION_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250102: {
        'codegen_method': 'public',
        'enum': 'TriggerModifier',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_MODIFIER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250103: {
        'codegen_method': 'public',
        'enum': 'InputImpedance',
        'grpc_type': 'double',
        'name': 'INPUT_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250106: {
        'codegen_method': 'public',
        'enum': 'SampleMode',
        'grpc_type': 'sint32',
        'name': 'SAMPLE_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250109: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ACQUISITION_START_TIME',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250201: {
        'codegen_method': 'public',
        'enum': 'VideoSignalFormat',
        'grpc_type': 'sint32',
        'name': 'TV_TRIGGER_SIGNAL_FORMAT',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250204: {
        'codegen_method': 'public',
        'enum': 'VideoPolarity',
        'grpc_type': 'sint32',
        'name': 'TV_TRIGGER_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250205: {
        'codegen_method': 'public',
        'enum': 'VideoTriggerEvent',
        'grpc_type': 'sint32',
        'name': 'TV_TRIGGER_EVENT',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250206: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'TV_TRIGGER_LINE_NUMBER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250301: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RUNT_HIGH_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250302: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'RUNT_LOW_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250303: {
        'codegen_method': 'public',
        'enum': 'RuntPolarity',
        'grpc_type': 'sint32',
        'name': 'RUNT_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250401: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'GLITCH_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250402: {
        'codegen_method': 'public',
        'enum': 'GlitchPolarity',
        'grpc_type': 'sint32',
        'name': 'GLITCH_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250403: {
        'codegen_method': 'public',
        'enum': 'GlitchCondition',
        'grpc_type': 'sint32',
        'name': 'GLITCH_CONDITION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250501: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'WIDTH_LOW_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250502: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'WIDTH_HIGH_THRESHOLD',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250503: {
        'codegen_method': 'public',
        'enum': 'WidthPolarity',
        'grpc_type': 'sint32',
        'name': 'WIDTH_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250504: {
        'codegen_method': 'public',
        'enum': 'WidthCondition',
        'grpc_type': 'sint32',
        'name': 'WIDTH_CONDITION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250607: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_HIGH_REF',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250608: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_LOW_REF',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250609: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MEAS_MID_REF',
        'resettable': True,
        'type': 'ViReal64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/niscope/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/config.py sha256=bc47c8b8b46d51af3efdb9033de91f73bbfb0c78a38f8401740e96641ebca8e6 bytes=3453 -->
## FILE: source/codegen/metadata/niscope/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/config.py`
- sha256: `bc47c8b8b46d51af3efdb9033de91f73bbfb0c78a38f8401740e96641ebca8e6`
- bytes: 3453

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 23.3.0d127
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '23.3.0d127',
    'c_function_prefix': 'niScope_',
    'c_header': 'niScopeCal.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Scope',
    'custom_types': [
        {
            'fields': [
                {
                    'grpc_type': 'double',
                    'name': 'offset',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'gain',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'reserved1',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'reserved2',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'CoefficientInfo',
            'name': 'niScope_coefficientInfo'
        },
        {
            'fields': [
                {
                    'grpc_type': 'double',
                    'name': 'absoluteInitialX',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'relativeInitialX',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'xIncrement',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'sint32',
                    'name': 'actualSamples',
                    'type': 'ViInt32'
                },
                {
                    'grpc_type': 'double',
                    'name': 'offset',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'gain',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'reserved1',
                    'type': 'ViReal64'
                },
                {
                    'grpc_type': 'double',
                    'name': 'reserved2',
                    'type': 'ViReal64'
                }
            ],
            'grpc_name': 'WaveformInfo',
            'name': 'niScope_wfmInfo'
        }
    ],
    'driver_name': 'NI-SCOPE',
    'java_package': 'com.ni.grpc.scope',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niscope',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niScope_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niScope_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'niscope',
    'namespace_component': 'niscope',
    'service_class_prefix': 'NiScope',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/config_addon.py sha256=b73d5b5afd16cddb72b9b40e615c2085da572c13d69bf8c9abd59ddef9872985 bytes=886 -->
## FILE: source/codegen/metadata/niscope/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/config_addon.py`
- sha256: `b73d5b5afd16cddb72b9b40e615c2085da572c13d69bf8c9abd59ddef9872985`
- bytes: 886

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.0.0',
    'custom_types': [
        # Redundant, since waveform_info is also in the base config.py file. See issue 1495 (https://github.com/ni/nimi-python/issues/1495) 
        {
            'ctypes_type': 'struct_niScope_wfmInfo',
            'file_name': 'waveform_info',
            'python_name': 'WaveformInfo'
        },
        {
            'ctypes_type': 'struct_niScope_coefficientInfo',
            'file_name': 'coefficient_info',
            'python_name': 'CoefficientInfo'
        },
        {
            'ctypes_type': '',
            'file_name': 'measurement_stats',
            'python_name': 'MeasurementStats'
        }
    ]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/enums.py sha256=3c4c37f8b9d50b3c4a3e9cc1bce815810e344d0c88089383b3b03f993d6ea9b8 bytes=68116 -->
## FILE: source/codegen/metadata/niscope/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/enums.py`
- sha256: `3c4c37f8b9d50b3c4a3e9cc1bce815810e344d0c88089383b3b03f993d6ea9b8`
- bytes: 68116

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 23.3.0d127
enums = {
    'AcquisitionStatus': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_ACQ_IN_PROGRESS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ACQ_COMPLETE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ACQ_STATUS_UNKNOWN',
                'value': -1
            }
        ]
    },
    'AcquisitionType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NORMAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_FLEXRES',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_DDC',
                'value': 1002
            }
        ]
    },
    'AddressType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'ArrayMeasurement': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'name': 'NISCOPE_VAL_LAST_ACQ_HISTOGRAM',
                'value': 4001
            },
            {
                'name': 'NISCOPE_VAL_FFT_PHASE_SPECTRUM',
                'value': 4002
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS',
                'value': 4003
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_INTEGRAL',
                'value': 4006
            },
            {
                'name': 'NISCOPE_VAL_DERIVATIVE',
                'value': 4007
            },
            {
                'name': 'NISCOPE_VAL_INVERSE',
                'value': 4008
            },
            {
                'name': 'NISCOPE_VAL_HANNING_WINDOW',
                'value': 4009
            },
            {
                'name': 'NISCOPE_VAL_FLAT_TOP_WINDOW',
                'value': 4010
            },
            {
                'name': 'NISCOPE_VAL_POLYNOMIAL_INTERPOLATION',
                'value': 4011
            },
            {
                'name': 'NISCOPE_VAL_MULTIPLY_CHANNELS',
                'value': 4012
            },
            {
                'name': 'NISCOPE_VAL_ADD_CHANNELS',
                'value': 4013
            },
            {
                'name': 'NISCOPE_VAL_SUBTRACT_CHANNELS',
                'value': 4014
            },
            {
                'name': 'NISCOPE_VAL_DIVIDE_CHANNELS',
                'value': 4015
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'name': 'NISCOPE_VAL_BUTTERWORTH_FILTER',
                'value': 4017
            },
            {
                'name': 'NISCOPE_VAL_CHEBYSHEV_FILTER',
                'value': 4018
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMP_SPECTRUM_DB',
                'value': 4019
            },
            {
                'name': 'NISCOPE_VAL_HAMMING_WINDOW',
                'value': 4020
            },
            {
                'name': 'NISCOPE_VAL_WINDOWED_FIR_FILTER',
                'value': 4021
            },
            {
                'name': 'NISCOPE_VAL_BESSEL_FILTER',
                'value': 4022
            },
            {
                'name': 'NISCOPE_VAL_TRIANGLE_WINDOW',
                'value': 4023
            },
            {
                'name': 'NISCOPE_VAL_BLACKMAN_WINDOW',
                'value': 4024
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_OFFSET',
                'value': 4025
            },
            {
                'name': 'NISCOPE_VAL_ARRAY_GAIN',
                'value': 4026
            }
        ]
    },
    'CableSenseMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_CABLE_SENSE_MODE_DISABLED',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CABLE_SENSE_MODE_ON_DEMAND',
                'value': 1
            }
        ]
    },
    'CalibrationTypes': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_CAL_EXTERNAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_CAL_SELF',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_CAL_MANUFACTURE',
                'value': 2
            }
        ]
    },
    'ClearableMeasurement': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ALL_MEASUREMENTS',
                'value': 10000
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM',
                'value': 4004
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM',
                'value': 4005
            },
            {
                'name': 'NISCOPE_VAL_MULTI_ACQ_AVERAGE',
                'value': 4016
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN',
                'value': 2000
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV',
                'value': 2001
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN',
                'value': 2003
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE',
                'value': 2010
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX',
                'value': 2005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN',
                'value': 2006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK',
                'value': 2002
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 2007
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 2008
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 2009
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS',
                'value': 2004
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS',
                'value': 2011
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN',
                'value': 3000
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_STDEV',
                'value': 3001
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN',
                'value': 3003
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MODE',
                'value': 3010
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MAX',
                'value': 3005
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MIN',
                'value': 3006
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK',
                'value': 3002
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV',
                'value': 3007
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV',
                'value': 3008
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV',
                'value': 3009
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_HITS',
                'value': 3004
            },
            {
                'name': 'NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS',
                'value': 3011
            }
        ]
    },
    'ClockingTerminalValues': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_SOURCE',
                'value': 'VAL_NO_SOURCE'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_CLOCK',
                'value': 'VAL_RTSI_CLOCK'
            },
            {
                'name': 'NISCOPE_VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL'
            },
            {
                'name': 'NISCOPE_VAL_PFI_0',
                'value': 'VAL_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_PFI_1',
                'value': 'VAL_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_PFI_2',
                'value': 'VAL_PFI_2'
            },
            {
                'name': 'NISCOPE_VAL_CLK_IN',
                'value': 'VAL_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_CLK_OUT',
                'value': 'VAL_CLK_OUT'
            },
            {
                'name': 'NISCOPE_VAL_INTERNAL10MHZ_OSC',
                'value': 'VAL_INTERNAL10MHZ_OSC'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK',
                'value': 'VAL_PXI_CLK'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK10',
                'value': 'VAL_PXI_CLK10'
            },
            {
                'name': 'NISCOPE_VAL_PXI_CLK100',
                'value': 'VAL_PXI_CLK100'
            },
            {
                'name': 'NISCOPE_VAL_PXIE_DSTAR_A',
                'value': 'VAL_PXIE_DSTAR_A'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_IN',
                'value': 'VAL_AUX_0_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_OUT',
                'value': 'VAL_AUX_0_CLK_OUT'
            },
            {
                'name': 'NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK',
                'value': 'VAL_ONBOARD_CONFIGURABLE_RATE_CLK'
            }
        ]
    },
    'DataProcessingMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_REAL',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_COMPLEX',
                'value': 1
            }
        ]
    },
    'ExportableSignals': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_REF_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_START_TRIGGER',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_END_OF_ACQUISITION_EVENT',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_END_OF_RECORD_EVENT',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_ADVANCE_TRIGGER',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_ADVANCE_EVENT',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_START_EVENT',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_READY_FOR_REF_EVENT',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_5V_OUT',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_REF_CLOCK',
                'value': 100
            },
            {
                'name': 'NISCOPE_VAL_SAMPLE_CLOCK',
                'value': 101
            }
        ]
    },
    'FIRFilterWindow': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_HANNING',
                'value': 409
            },
            {
                'name': 'NISCOPE_VAL_FLAT_TOP',
                'value': 410
            },
            {
                'name': 'NISCOPE_VAL_HAMMING',
                'value': 420
            },
            {
                'name': 'NISCOPE_VAL_TRIANGLE',
                'value': 423
            },
            {
                'name': 'NISCOPE_VAL_BLACKMAN',
                'value': 424
            }
        ]
    },
    'FetchRelativeTo': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_READ_POINTER',
                'value': 388
            },
            {
                'name': 'NISCOPE_VAL_PRETRIGGER',
                'value': 477
            },
            {
                'name': 'NISCOPE_VAL_NOW',
                'value': 481
            },
            {
                'name': 'NISCOPE_VAL_START',
                'value': 482
            },
            {
                'name': 'NISCOPE_VAL_TRIGGER',
                'value': 483
            }
        ]
    },
    'FlexFIRAntialiasFilterType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_48_TAP_STANDARD',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_48_TAP_HANNING',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_16_TAP_HANNING',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_8_TAP_HANNING',
                'value': 3
            }
        ]
    },
    'GlitchCondition': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_GLITCH_GREATER_THAN',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_GLITCH_LESS_THAN',
                'value': 1
            }
        ]
    },
    'GlitchPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_GLITCH_POSITIVE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_GLITCH_NEGATIVE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_GLITCH_EITHER',
                'value': 3
            }
        ]
    },
    'InputImpedance': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NISCOPE_VAL_50_OHMS',
                'value': 50.0
            },
            {
                'name': 'NISCOPE_VAL_75_OHMS',
                'value': 75.0
            },
            {
                'name': 'NISCOPE_VAL_1_MEG_OHM',
                'value': 1000000.0
            }
        ]
    },
    'MaxInputFrequency': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT',
                'value': 0.0
            },
            {
                'name': 'NISCOPE_VAL_BANDWIDTH_FULL',
                'value': -1.0
            },
            {
                'name': 'NISCOPE_VAL_20MHZ_BANDWIDTH',
                'value': 20000000.0
            },
            {
                'name': 'NISCOPE_VAL_100MHZ_BANDWIDTH',
                'value': 100000000.0
            },
            {
                'name': 'NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY',
                'value': 20000000.0
            },
            {
                'name': 'NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY',
                'value': 100000000.0
            }
        ]
    },
    'MeasFilterType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_LOWPASS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_HIGHPASS',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BANDPASS',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BANDSTOP',
                'value': 3
            }
        ]
    },
    'MeasPercentageMethod': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_LOW_HIGH',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_MIN_MAX',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_MEAS_BASE_TOP',
                'value': 2
            }
        ]
    },
    'MeasRefLevelUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_MEAS_VOLTAGE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_MEAS_PERCENTAGE',
                'value': 1
            }
        ]
    },
    'NiScopeInt32AttributeValues': {
        'enum-value-prefix': 'NISCOPE_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'ACQUISITION_TYPE_VAL_NORMAL',
                'value': 0
            },
            {
                'name': 'ACQUISITION_TYPE_VAL_FLEXRES',
                'value': 1001
            },
            {
                'name': 'ACQUISITION_TYPE_VAL_DDC',
                'value': 1002
            },
            {
                'name': 'ADDRESS_TYPE_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'name': 'ADDRESS_TYPE_VAL_ADDR_VIRTUAL',
                'value': 1
            },
            {
                'name': 'DATA_PROCESSING_MODE_VAL_REAL',
                'value': 0
            },
            {
                'name': 'DATA_PROCESSING_MODE_VAL_COMPLEX',
                'value': 1
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_NONE',
                'value': 0
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_HANNING',
                'value': 409
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_FLAT_TOP',
                'value': 410
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_HAMMING',
                'value': 420
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_TRIANGLE',
                'value': 423
            },
            {
                'name': 'FIR_FILTER_WINDOW_VAL_BLACKMAN',
                'value': 424
            },
            {
                'name': 'FETCH_RELATIVE_TO_VAL_READ_POINTER',
                'value': 388
            },
            {
                'name': 'FETCH_RELATIVE_TO_VAL_PRETRIGGER',
                'value': 477
            },
            {
                'name': 'FETCH_RELATIVE_TO_VAL_NOW',
                'value': 481
            },
            {
                'name': 'FETCH_RELATIVE_TO_VAL_START',
                'value': 482
            },
            {
                'name': 'FETCH_RELATIVE_TO_VAL_TRIGGER',
                'value': 483
            },
            {
                'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_STANDARD',
                'value': 0
            },
            {
                'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_HANNING',
                'value': 1
            },
            {
                'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_16_TAP_HANNING',
                'value': 2
            },
            {
                'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_8_TAP_HANNING',
                'value': 3
            },
            {
                'name': 'GLITCH_CONDITION_VAL_GLITCH_GREATER_THAN',
                'value': 2
            },
            {
                'name': 'GLITCH_CONDITION_VAL_GLITCH_LESS_THAN',
                'value': 1
            },
            {
                'name': 'GLITCH_POLARITY_VAL_GLITCH_POSITIVE',
                'value': 1
            },
            {
                'name': 'GLITCH_POLARITY_VAL_GLITCH_NEGATIVE',
                'value': 2
            },
            {
                'name': 'GLITCH_POLARITY_VAL_GLITCH_EITHER',
                'value': 3
            },
            {
                'name': 'MEAS_FILTER_TYPE_VAL_MEAS_LOWPASS',
                'value': 0
            },
            {
                'name': 'MEAS_FILTER_TYPE_VAL_MEAS_HIGHPASS',
                'value': 1
            },
            {
                'name': 'MEAS_FILTER_TYPE_VAL_MEAS_BANDPASS',
                'value': 2
            },
            {
                'name': 'MEAS_FILTER_TYPE_VAL_MEAS_BANDSTOP',
                'value': 3
            },
            {
                'name': 'MEAS_PERCENTAGE_METHOD_VAL_MEAS_LOW_HIGH',
                'value': 0
            },
            {
                'name': 'MEAS_PERCENTAGE_METHOD_VAL_MEAS_MIN_MAX',
                'value': 1
            },
            {
                'name': 'MEAS_PERCENTAGE_METHOD_VAL_MEAS_BASE_TOP',
                'value': 2
            },
            {
                'name': 'MEAS_REF_LEVEL_UNITS_VAL_MEAS_VOLTAGE',
                'value': 0
            },
            {
                'name': 'MEAS_REF_LEVEL_UNITS_VAL_MEAS_PERCENTAGE',
                'value': 1
            },
            {
                'name': 'NOTIFICATION_TYPE_VAL_NOTIFY_NEVER',
                'value': 0
            },
            {
                'name': 'NOTIFICATION_TYPE_VAL_NOTIFY_DONE',
                'value': 1
            },
            {
                'name': 'OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'name': 'OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_WARNING',
                'value': 1
            },
            {
                'name': 'OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            },
            {
                'name': 'P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_START_TRIGGER',
                'value': 0
            },
            {
                'name': 'P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'name': 'P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER',
                'value': 2
            },
            {
                'name': 'RIS_METHOD_VAL_RIS_EXACT_NUM_AVERAGES',
                'value': 1
            },
            {
                'name': 'RIS_METHOD_VAL_RIS_MIN_NUM_AVERAGES',
                'value': 2
            },
            {
                'name': 'RIS_METHOD_VAL_RIS_INCOMPLETE',
                'value': 3
            },
            {
                'name': 'RIS_METHOD_VAL_RIS_LIMITED_BIN_WIDTH',
                'value': 5
            },
            {
                'name': 'REF_TRIGGER_DETECTOR_LOCATION_VAL_ANALOG_DETECTION_CIRCUIT',
                'value': 0
            },
            {
                'name': 'REF_TRIGGER_DETECTOR_LOCATION_VAL_DDC_OUTPUT',
                'value': 1
            },
            {
                'name': 'RUNT_POLARITY_VAL_RUNT_POSITIVE',
                'value': 1
            },
            {
                'name': 'RUNT_POLARITY_VAL_RUNT_NEGATIVE',
                'value': 2
            },
            {
                'name': 'RUNT_POLARITY_VAL_RUNT_EITHER',
                'value': 3
            },
            {
                'name': 'RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_NONE',
                'value': 0
            },
            {
                'name': 'RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_WITHIN',
                'value': 1
            },
            {
                'name': 'RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_OUTSIDE',
                'value': 2
            },
            {
                'name': 'SAMPLE_MODE_VAL_REAL_TIME',
                'value': 0
            },
            {
                'name': 'SAMPLE_MODE_VAL_EQUIVALENT_TIME',
                'value': 1
            },
            {
                'name': 'TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED',
                'value': 0
            },
            {
                'name': 'TERMINAL_CONFIGURATION_VAL_UNBALANCED_DIFFERENTIAL',
                'value': 1
            },
            {
                'name': 'TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL',
                'value': 2
            },
            {
                'name': 'TRIGGER_COUPLING_VAL_AC',
                'value': 0
            },
            {
                'name': 'TRIGGER_COUPLING_VAL_DC',
                'value': 1
            },
            {
                'name': 'TRIGGER_COUPLING_VAL_HF_REJECT',
                'value': 3
            },
            {
                'name': 'TRIGGER_COUPLING_VAL_LF_REJECT',
                'value': 4
            },
            {
                'name': 'TRIGGER_COUPLING_VAL_AC_PLUS_HF_REJECT',
                'value': 1001
            },
            {
                'name': 'TRIGGER_MODIFIER_VAL_NO_TRIGGER_MOD',
                'value': 1
            },
            {
                'name': 'TRIGGER_MODIFIER_VAL_AUTO',
                'value': 2
            },
            {
                'name': 'TRIGGER_MODIFIER_VAL_AUTO_LEVEL',
                'value': 3
            },
            {
                'name': 'TRIGGER_SLOPE_VAL_NEGATIVE',
                'value': 0
            },
            {
                'name': 'TRIGGER_SLOPE_VAL_POSITIVE',
                'value': 1
            },
            {
                'name': 'TRIGGER_SLOPE_VAL_SLOPE_EITHER',
                'value': 3
            },
            {
                'name': 'TRIGGER_TYPE_VAL_EDGE_TRIGGER',
                'value': 1
            },
            {
                'name': 'TRIGGER_TYPE_VAL_HYSTERESIS_TRIGGER',
                'value': 1001
            },
            {
                'name': 'TRIGGER_TYPE_VAL_DIGITAL_TRIGGER',
                'value': 1002
            },
            {
                'name': 'TRIGGER_TYPE_VAL_WINDOW_TRIGGER',
                'value': 1003
            },
            {
                'name': 'TRIGGER_TYPE_VAL_SOFTWARE_TRIGGER',
                'value': 1004
            },
            {
                'name': 'TRIGGER_TYPE_VAL_TV_TRIGGER',
                'value': 5
            },
            {
                'name': 'TRIGGER_TYPE_VAL_GLITCH_TRIGGER',
                'value': 4
            },
            {
                'name': 'TRIGGER_TYPE_VAL_WIDTH_TRIGGER',
                'value': 2
            },
            {
                'name': 'TRIGGER_TYPE_VAL_RUNT_TRIGGER',
                'value': 3
            },
            {
                'name': 'TRIGGER_TYPE_VAL_IMMEDIATE_TRIGGER',
                'value': 6
            },
            {
                'name': 'TRIGGER_WINDOW_MODE_VAL_ENTERING_WINDOW',
                'value': 0
            },
            {
                'name': 'TRIGGER_WINDOW_MODE_VAL_LEAVING_WINDOW',
                'value': 1
            },
            {
                'name': 'TRIGGER_WINDOW_MODE_VAL_ENTERING_OR_LEAVING_WINDOW',
                'value': 2
            },
            {
                'name': 'VERTICAL_COUPLING_VAL_AC',
                'value': 0
            },
            {
                'name': 'VERTICAL_COUPLING_VAL_DC',
                'value': 1
            },
            {
                'name': 'VERTICAL_COUPLING_VAL_GND',
                'value': 2
            },
            {
                'name': 'VIDEO_POLARITY_VAL_TV_POSITIVE',
                'value': 1
            },
            {
                'name': 'VIDEO_POLARITY_VAL_TV_NEGATIVE',
                'value': 2
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_NTSC',
                'value': 1
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_PAL',
                'value': 2
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_SECAM',
                'value': 3
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_M_PAL',
                'value': 1001
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_60_FIELDS_PER_SECOND',
                'value': 1011
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_60_FRAMES_PER_SECOND',
                'value': 1016
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576I_50_FIELDS_PER_SECOND',
                'value': 1020
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576P_50_FRAMES_PER_SECOND',
                'value': 1025
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_50_FRAMES_PER_SECOND',
                'value': 1031
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_60_FRAMES_PER_SECOND',
                'value': 1033
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND',
                'value': 1040
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND',
                'value': 1042
            },
            {
                'name': 'VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND',
                'value': 1045
            },
            {
                'name': 'VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD1',
                'value': 1
            },
            {
                'name': 'VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD2',
                'value': 2
            },
            {
                'name': 'VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_FIELD',
                'value': 3
            },
            {
                'name': 'VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_LINE',
                'value': 4
            },
            {
                'name': 'VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_LINE_NUMBER',
                'value': 5
            },
            {
                'name': 'WIDTH_CONDITION_VAL_WIDTH_WITHIN',
                'value': 1
            },
            {
                'name': 'WIDTH_CONDITION_VAL_WIDTH_OUTSIDE',
                'value': 2
            },
            {
                'name': 'WIDTH_POLARITY_VAL_WIDTH_POSITIVE',
                'value': 1
            },
            {
                'name': 'WIDTH_POLARITY_VAL_WIDTH_NEGATIVE',
                'value': 2
            },
            {
                'name': 'WIDTH_POLARITY_VAL_WIDTH_EITHER',
                'value': 3
            }
        ]
    },
    'NiScopeReal64AttributeValues': {
        'enum-value-prefix': 'NISCOPE_REAL64',
        'generate-mappings': False,
        'values': [
            {
                'name': 'CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_DISABLED',
                'value': 0
            },
            {
                'name': 'CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_ON_DEMAND',
                'value': 1
            }
        ]
    },
    'NiScopeReal64AttributeValuesMapped': {
        'enum-value-prefix': 'NISCOPE_REAL64',
        'generate-mappings': True,
        'values': [
            {
                'name': 'INPUT_IMPEDANCE_VAL_50_OHMS',
                'value': 50.0
            },
            {
                'name': 'INPUT_IMPEDANCE_VAL_75_OHMS',
                'value': 75.0
            },
            {
                'name': 'INPUT_IMPEDANCE_VAL_1_MEG_OHM',
                'value': 1000000.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_DEVICE_DEFAULT',
                'value': 0.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_FULL',
                'value': -1.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_20MHZ_BANDWIDTH',
                'value': 20000000.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_100MHZ_BANDWIDTH',
                'value': 100000000.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_20MHZ_MAX_INPUT_FREQUENCY',
                'value': 20000000.0
            },
            {
                'name': 'MAX_INPUT_FREQUENCY_VAL_100MHZ_MAX_INPUT_FREQUENCY',
                'value': 100000000.0
            }
        ]
    },
    'NiScopeStringAttributeValuesMapped': {
        'enum-value-prefix': 'NISCOPE_STRING',
        'generate-mappings': True,
        'values': [
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_CLK_IN',
                'value': 'VAL_CLK_IN'
            },
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_NO_SOURCE',
                'value': 'VAL_NO_SOURCE'
            },
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_PXIE_DSTAR_A',
                'value': 'VAL_PXIE_DSTAR_A'
            },
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_AUX_0_CLK_IN',
                'value': 'VAL_AUX_0_CLK_IN'
            },
            {
                'name': 'SAMP_CLK_TIMEPACE_SRC_VAL_ONBOARD_CONFIGURABLE_RATE_CLK',
                'value': 'VAL_ONBOARD_CONFIGURABLE_RATE_CLK'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_IMMEDIATE',
                'value': 'VAL_IMMEDIATE'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_SW_TRIG_FUNC',
                'value': 'VAL_SW_TRIG_FUNC'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL0',
                'value': 'VAL_TTL0'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL1',
                'value': 'VAL_TTL1'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL2',
                'value': 'VAL_TTL2'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL3',
                'value': 'VAL_TTL3'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL4',
                'value': 'VAL_TTL4'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL5',
                'value': 'VAL_TTL5'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL6',
                'value': 'VAL_TTL6'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL7',
                'value': 'VAL_TTL7'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_ECL0',
                'value': 'VAL_ECL0'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_ECL1',
                'value': 'VAL_ECL1'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_0',
                'value': 'VAL_RTSI_0'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_1',
                'value': 'VAL_RTSI_1'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_2',
                'value': 'VAL_RTSI_2'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_3',
                'value': 'VAL_RTSI_3'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_4',
                'value': 'VAL_RTSI_4'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_5',
                'value': 'VAL_RTSI_5'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_6',
                'value': 'VAL_RTSI_6'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_7',
                'value': 'VAL_RTSI_7'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_0',
                'value': 'VAL_PFI_0'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_1',
                'value': 'VAL_PFI_1'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_2',
                'value': 'VAL_PFI_2'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_3',
                'value': 'VAL_PFI_3'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_4',
                'value': 'VAL_PFI_4'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_5',
                'value': 'VAL_PFI_5'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_6',
                'value': 'VAL_PFI_6'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_7',
                'value': 'VAL_PFI_7'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_0',
                'value': 'VAL_AUX_0_PFI_0'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_1',
                'value': 'VAL_AUX_0_PFI_1'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_3',
                'value': 'VAL_AUX_0_PFI_3'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_4',
                'value': 'VAL_AUX_0_PFI_4'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_5',
                'value': 'VAL_AUX_0_PFI_5'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_6',
                'value': 'VAL_AUX_0_PFI_6'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_7',
                'value': 'VAL_AUX_0_PFI_7'
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_AUX_0_PFI_2',
                'value': 'VAL_AUX_0_PFI_2'
            }
        ]
    },
    'NotificationType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NOTIFY_NEVER',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_NOTIFY_DONE',
                'value': 1
            }
        ]
    },
    'Option': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION',
                'value': 1
            }
        ]
    },
    'OverflowErrorReporting': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_WARNING',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'P2PStreamRelativeTo': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_START_TRIGGER',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER',
                'value': 2
            }
        ]
    },
    'RISMethod': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_RIS_EXACT_NUM_AVERAGES',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RIS_MIN_NUM_AVERAGES',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_RIS_INCOMPLETE',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_RIS_LIMITED_BIN_WIDTH',
                'value': 5
            }
        ]
    },
    'RefTriggerDetectorLocation': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_ANALOG_DETECTION_CIRCUIT',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_DDC_OUTPUT',
                'value': 1
            }
        ]
    },
    'RuntPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_RUNT_POSITIVE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RUNT_NEGATIVE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_RUNT_EITHER',
                'value': 3
            }
        ]
    },
    'RuntTimeCondition': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_NONE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_WITHIN',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_RUNT_TIME_CONDITION_OUTSIDE',
                'value': 2
            }
        ]
    },
    'SampClkTimepaceSrc': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NISCOPE_VAL_CLK_IN',
                'value': 'VAL_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_NO_SOURCE',
                'value': 'VAL_NO_SOURCE'
            },
            {
                'name': 'NISCOPE_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'NISCOPE_VAL_PXIE_DSTAR_A',
                'value': 'VAL_PXIE_DSTAR_A'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_CLK_IN',
                'value': 'VAL_AUX_0_CLK_IN'
            },
            {
                'name': 'NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK',
                'value': 'VAL_ONBOARD_CONFIGURABLE_RATE_CLK'
            }
        ]
    },
    'SampleMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_REAL_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_EQUIVALENT_TIME',
                'value': 1
            }
        ]
    },
    'ScalarMeasurement': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_RISE_TIME',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_NO_MEASUREMENT',
                'value': 4000
            },
            {
                'name': 'NISCOPE_VAL_FALL_TIME',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_FREQUENCY',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_PERIOD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_RMS',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MAX',
                'value': 6
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_MIN',
                'value': 7
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_HIGH',
                'value': 8
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_LOW',
                'value': 9
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_AVERAGE',
                'value': 10
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEG',
                'value': 11
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_POS',
                'value': 12
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_NEG',
                'value': 13
            },
            {
                'name': 'NISCOPE_VAL_DUTY_CYCLE_POS',
                'value': 14
            },
            {
                'name': 'NISCOPE_VAL_AMPLITUDE',
                'value': 15
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_RMS',
                'value': 16
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE',
                'value': 17
            },
            {
                'name': 'NISCOPE_VAL_OVERSHOOT',
                'value': 18
            },
            {
                'name': 'NISCOPE_VAL_PRESHOOT',
                'value': 19
            },
            {
                'name': 'NISCOPE_VAL_LOW_REF_VOLTS',
                'value': 1000
            },
            {
                'name': 'NISCOPE_VAL_MID_REF_VOLTS',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_HIGH_REF_VOLTS',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_AREA',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_CYCLE_AREA',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_INTEGRAL',
                'value': 1005
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE',
                'value': 1006
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_TOP',
                'value': 1007
            },
            {
                'name': 'NISCOPE_VAL_FFT_FREQUENCY',
                'value': 1008
            },
            {
                'name': 'NISCOPE_VAL_FFT_AMPLITUDE',
                'value': 1009
            },
            {
                'name': 'NISCOPE_VAL_RISE_SLEW_RATE',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_FALL_SLEW_RATE',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_AC_ESTIMATE',
                'value': 1012
            },
            {
                'name': 'NISCOPE_VAL_DC_ESTIMATE',
                'value': 1013
            },
            {
                'name': 'NISCOPE_VAL_TIME_DELAY',
                'value': 1014
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_PERIOD',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_AVERAGE_FREQUENCY',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_VOLTAGE_BASE_TO_TOP',
                'value': 1017
            },
            {
                'name': 'NISCOPE_VAL_PHASE_DELAY',
                'value': 1018
            }
        ]
    },
    'TerminalConfiguration': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_SINGLE_ENDED',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_UNBALANCED_DIFFERENTIAL',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_DIFFERENTIAL',
                'value': 2
            }
        ]
    },
    'TriggerCoupling': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_HF_REJECT',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_LF_REJECT',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_AC_PLUS_HF_REJECT',
                'value': 1001
            }
        ]
    },
    'TriggerModifier': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NO_TRIGGER_MOD',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_AUTO',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_AUTO_LEVEL',
                'value': 3
            }
        ]
    },
    'TriggerSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NEGATIVE',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_POSITIVE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_SLOPE_EITHER',
                'value': 3
            }
        ]
    },
    'TriggerSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NISCOPE_VAL_IMMEDIATE',
                'value': 'VAL_IMMEDIATE'
            },
            {
                'name': 'NISCOPE_VAL_EXTERNAL',
                'value': 'VAL_EXTERNAL'
            },
            {
                'name': 'NISCOPE_VAL_SW_TRIG_FUNC',
                'value': 'VAL_SW_TRIG_FUNC'
            },
            {
                'name': 'NISCOPE_VAL_TTL0',
                'value': 'VAL_TTL0'
            },
            {
                'name': 'NISCOPE_VAL_TTL1',
                'value': 'VAL_TTL1'
            },
            {
                'name': 'NISCOPE_VAL_TTL2',
                'value': 'VAL_TTL2'
            },
            {
                'name': 'NISCOPE_VAL_TTL3',
                'value': 'VAL_TTL3'
            },
            {
                'name': 'NISCOPE_VAL_TTL4',
                'value': 'VAL_TTL4'
            },
            {
                'name': 'NISCOPE_VAL_TTL5',
                'value': 'VAL_TTL5'
            },
            {
                'name': 'NISCOPE_VAL_TTL6',
                'value': 'VAL_TTL6'
            },
            {
                'name': 'NISCOPE_VAL_TTL7',
                'value': 'VAL_TTL7'
            },
            {
                'name': 'NISCOPE_VAL_ECL0',
                'value': 'VAL_ECL0'
            },
            {
                'name': 'NISCOPE_VAL_ECL1',
                'value': 'VAL_ECL1'
            },
            {
                'name': 'NISCOPE_VAL_PXI_STAR',
                'value': 'VAL_PXI_STAR'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_0',
                'value': 'VAL_RTSI_0'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_1',
                'value': 'VAL_RTSI_1'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_2',
                'value': 'VAL_RTSI_2'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_3',
                'value': 'VAL_RTSI_3'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_4',
                'value': 'VAL_RTSI_4'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_5',
                'value': 'VAL_RTSI_5'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_6',
                'value': 'VAL_RTSI_6'
            },
            {
                'name': 'NISCOPE_VAL_RTSI_7',
                'value': 'VAL_RTSI_7'
            },
            {
                'name': 'NISCOPE_VAL_PFI_0',
                'value': 'VAL_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_PFI_1',
                'value': 'VAL_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_PFI_2',
                'value': 'VAL_PFI_2'
            },
            {
                'name': 'NISCOPE_VAL_PFI_3',
                'value': 'VAL_PFI_3'
            },
            {
                'name': 'NISCOPE_VAL_PFI_4',
                'value': 'VAL_PFI_4'
            },
            {
                'name': 'NISCOPE_VAL_PFI_5',
                'value': 'VAL_PFI_5'
            },
            {
                'name': 'NISCOPE_VAL_PFI_6',
                'value': 'VAL_PFI_6'
            },
            {
                'name': 'NISCOPE_VAL_PFI_7',
                'value': 'VAL_PFI_7'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_0',
                'value': 'VAL_AUX_0_PFI_0'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_1',
                'value': 'VAL_AUX_0_PFI_1'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_3',
                'value': 'VAL_AUX_0_PFI_3'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_4',
                'value': 'VAL_AUX_0_PFI_4'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_5',
                'value': 'VAL_AUX_0_PFI_5'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_6',
                'value': 'VAL_AUX_0_PFI_6'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_7',
                'value': 'VAL_AUX_0_PFI_7'
            },
            {
                'name': 'NISCOPE_VAL_AUX_0_PFI_2',
                'value': 'VAL_AUX_0_PFI_2'
            }
        ]
    },
    'TriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_EDGE_TRIGGER',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_HYSTERESIS_TRIGGER',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_DIGITAL_TRIGGER',
                'value': 1002
            },
            {
                'name': 'NISCOPE_VAL_WINDOW_TRIGGER',
                'value': 1003
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NISCOPE_VAL_TV_TRIGGER',
                'value': 5
            },
            {
                'name': 'NISCOPE_VAL_GLITCH_TRIGGER',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_TRIGGER',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_RUNT_TRIGGER',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_IMMEDIATE_TRIGGER',
                'value': 6
            }
        ]
    },
    'TriggerWindowMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_ENTERING_WINDOW',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_LEAVING_WINDOW',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW',
                'value': 2
            }
        ]
    },
    'VerticalCoupling': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_AC',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_DC',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_GND',
                'value': 2
            }
        ]
    },
    'VideoPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_TV_POSITIVE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_TV_NEGATIVE',
                'value': 2
            }
        ]
    },
    'VideoSignalFormat': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_NTSC',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_PAL',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_SECAM',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_M_PAL',
                'value': 1001
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND',
                'value': 1010
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND',
                'value': 1011
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND',
                'value': 1015
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND',
                'value': 1016
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND',
                'value': 1020
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND',
                'value': 1025
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND',
                'value': 1031
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND',
                'value': 1032
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND',
                'value': 1033
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND',
                'value': 1040
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND',
                'value': 1041
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND',
                'value': 1042
            },
            {
                'name': 'NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND',
                'value': 1045
            }
        ]
    },
    'VideoTriggerEvent': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD1',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_FIELD2',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_FIELD',
                'value': 3
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_ANY_LINE',
                'value': 4
            },
            {
                'name': 'NISCOPE_VAL_TV_EVENT_LINE_NUMBER',
                'value': 5
            }
        ]
    },
    'WhichTrigger': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_START',
                'value': 0
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE',
                'value': 3
            }
        ]
    },
    'WidthCondition': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_WIDTH_WITHIN',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_OUTSIDE',
                'value': 2
            }
        ]
    },
    'WidthPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISCOPE_VAL_WIDTH_POSITIVE',
                'value': 1
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_NEGATIVE',
                'value': 2
            },
            {
                'name': 'NISCOPE_VAL_WIDTH_EITHER',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/enums_addon.py sha256=45cc684d8b0313c590716cf22de2fc0c026f8d4c6d0d1c6dacdec1e722d2910a bytes=297 -->
## FILE: source/codegen/metadata/niscope/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/enums_addon.py`
- sha256: `45cc684d8b0313c590716cf22de2fc0c026f8d4c6d0d1c6dacdec1e722d2910a`
- bytes: 297

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "MaxInputFrequency": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/functions.py sha256=132e61192338d9a049b8fe155bda5abf2f8aaa424c444be0149c88a4a4c2c163 bytes=108623 -->
## FILE: source/codegen/metadata/niscope/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/functions.py`
- sha256: `132e61192338d9a049b8fe155bda5abf2f8aaa424c444be0149c88a4a4c2c163`
- bytes: 108623

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SCOPE API metadata version 23.3.0d127
functions = {
    'Abort': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AcquisitionStatus': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'acquisitionStatus',
                'direction': 'out',
                'enum': 'AcquisitionStatus',
                'grpc_type': 'sint32',
                'name': 'acquisitionStatus',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualMeasWfmSize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'arrayMeasFunction',
                'direction': 'in',
                'enum': 'ArrayMeasurement',
                'grpc_type': 'sint32',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measWaveformSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'measWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualNumWfms': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numWfms',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numWfms',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ActualRecordLength': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'recordLength',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'recordLength',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AddWaveformProcessing': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'measFunction',
                'direction': 'in',
                'enum': 'ArrayMeasurement',
                'grpc_type': 'sint32',
                'name': 'measFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AdjustSampleClockRelativeDelay': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'AutoSetup': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CableSenseSignalStart': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CableSenseSignalStop': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchDate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'whichOne',
                'direction': 'in',
                'enum': 'CalibrationTypes',
                'grpc_type': 'sint32',
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalFetchTemperature': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'whichOne',
                'direction': 'in',
                'enum': 'CalibrationTypes',
                'grpc_type': 'sint32',
                'name': 'whichOne',
                'type': 'ViInt32'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'option',
                'direction': 'in',
                'enum': 'Option',
                'grpc_type': 'sint32',
                'name': 'option',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'enum': 'NiScopeInt32AttributeValues',
                'grpc_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'enum': 'NiScopeReal64AttributeValues',
                'grpc_field_number': '5',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '4',
                'grpc_type': 'double',
                'mapped-enum': 'NiScopeReal64AttributeValuesMapped',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'string',
                'mapped-enum': 'NiScopeStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearWaveformMeasurementStats': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'clearableMeasurementFunction',
                'direction': 'in',
                'enum': 'ClearableMeasurement',
                'grpc_type': 'sint32',
                'name': 'clearableMeasurementFunction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearWaveformProcessing': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niScope_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcquisition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'acquisitionType',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'acquisitionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChanCharacteristics': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'inputImpedance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'inputImpedance',
                'type': 'ViReal64'
            },
            {
                'cppName': 'maxInputFrequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'maxInputFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureClock': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'inputClockSource',
                'direction': 'in',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '2',
                'grpc_type': 'string',
                'mapped-enum': 'ClockingTerminalValues',
                'name': 'inputClockSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputClockSource',
                'direction': 'in',
                'grpc_mapped_field_number': '7',
                'grpc_raw_field_number': '3',
                'grpc_type': 'string',
                'mapped-enum': 'ClockingTerminalValues',
                'name': 'outputClockSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'clockSyncPulseSource',
                'direction': 'in',
                'grpc_mapped_field_number': '8',
                'grpc_raw_field_number': '4',
                'grpc_type': 'string',
                'mapped-enum': 'ClockingTerminalValues',
                'name': 'clockSyncPulseSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'masterEnabled',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'masterEnabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureEqualizationFilterCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfCoefficients',
                'determine_size_from': [
                    'coefficients'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficients',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'coefficients',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureHorizontalTiming': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'minSampleRate',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'minSampleRate',
                'type': 'ViReal64'
            },
            {
                'cppName': 'minNumPts',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'minNumPts',
                'type': 'ViInt32'
            },
            {
                'cppName': 'refPosition',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'refPosition',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numRecords',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'cppName': 'enforceRealtime',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enforceRealtime',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerDigital': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'slope',
                'direction': 'in',
                'enum': 'TriggerSlope',
                'grpc_type': 'sint32',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerEdge': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'cppName': 'slope',
                'direction': 'in',
                'enum': 'TriggerSlope',
                'grpc_type': 'sint32',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerGlitch': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'cppName': 'width',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'width',
                'type': 'ViReal64'
            },
            {
                'cppName': 'polarity',
                'direction': 'in',
                'enum': 'GlitchPolarity',
                'grpc_type': 'sint32',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'cppName': 'glitchCondition',
                'direction': 'in',
                'enum': 'GlitchCondition',
                'grpc_type': 'sint32',
                'name': 'glitchCondition',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerHysteresis': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'cppName': 'hysteresis',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'hysteresis',
                'type': 'ViReal64'
            },
            {
                'cppName': 'slope',
                'direction': 'in',
                'enum': 'TriggerSlope',
                'grpc_type': 'sint32',
                'name': 'slope',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerImmediate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerRunt': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'lowThreshold',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'lowThreshold',
                'type': 'ViReal64'
            },
            {
                'cppName': 'highThreshold',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'highThreshold',
                'type': 'ViReal64'
            },
            {
                'cppName': 'polarity',
                'direction': 'in',
                'enum': 'RuntPolarity',
                'grpc_type': 'sint32',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSoftware': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerVideo': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'enableDcRestore',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enableDcRestore',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'signalFormat',
                'direction': 'in',
                'enum': 'VideoSignalFormat',
                'grpc_type': 'sint32',
                'name': 'signalFormat',
                'type': 'ViInt32'
            },
            {
                'cppName': 'eventParameter',
                'direction': 'in',
                'enum': 'VideoTriggerEvent',
                'grpc_type': 'sint32',
                'name': 'event',
                'type': 'ViInt32'
            },
            {
                'cppName': 'lineNumber',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'lineNumber',
                'type': 'ViInt32'
            },
            {
                'cppName': 'polarity',
                'direction': 'in',
                'enum': 'VideoPolarity',
                'grpc_type': 'sint32',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWidth': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'level',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'level',
                'type': 'ViReal64'
            },
            {
                'cppName': 'lowThreshold',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'lowThreshold',
                'type': 'ViReal64'
            },
            {
                'cppName': 'highThreshold',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'highThreshold',
                'type': 'ViReal64'
            },
            {
                'cppName': 'polarity',
                'direction': 'in',
                'enum': 'WidthPolarity',
                'grpc_type': 'sint32',
                'name': 'polarity',
                'type': 'ViInt32'
            },
            {
                'cppName': 'condition',
                'direction': 'in',
                'enum': 'WidthCondition',
                'grpc_type': 'sint32',
                'name': 'condition',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerWindow': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'lowLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'lowLevel',
                'type': 'ViReal64'
            },
            {
                'cppName': 'highLevel',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'highLevel',
                'type': 'ViReal64'
            },
            {
                'cppName': 'windowMode',
                'direction': 'in',
                'enum': 'TriggerWindowMode',
                'grpc_type': 'sint32',
                'name': 'windowMode',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerCoupling',
                'direction': 'in',
                'enum': 'TriggerCoupling',
                'grpc_type': 'sint32',
                'name': 'triggerCoupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'holdoff',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'holdoff',
                'type': 'ViReal64'
            },
            {
                'cppName': 'delay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'delay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVertical': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'range',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'cppName': 'offset',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'offset',
                'type': 'ViReal64'
            },
            {
                'cppName': 'coupling',
                'direction': 'in',
                'enum': 'VerticalCoupling',
                'grpc_type': 'sint32',
                'name': 'coupling',
                'type': 'ViInt32'
            },
            {
                'cppName': 'probeAttenuation',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'probeAttenuation',
                'type': 'ViReal64'
            },
            {
                'cppName': 'enabled',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorHandler': {
        'cname': 'niScope_errorHandler',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'errorSource',
                'size': {
                    'mechanism': 'fixed',
                    'value': 55
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'errorDescription',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'fixed',
                    'value': 642
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'signal',
                'direction': 'in',
                'enum': 'ExportableSignals',
                'grpc_type': 'sint32',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'cppName': 'signalIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'mapped-enum': 'ClockingTerminalValues',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Fetch': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveform',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchArrayMeasurement': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'arrayMeasFunction',
                'direction': 'in',
                'enum': 'ArrayMeasurement',
                'grpc_type': 'sint32',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measWfmSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_optional': True,
                'name': 'measWfmSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'measWfm',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'measWfm',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(measurement_waveform_size * actual_num_wfms)'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary16': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'waveform',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'ViInt16[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary32': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'waveform',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchBinary8': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'waveform',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'ViInt8[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchComplex': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'wfm',
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'wfm',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'struct NIComplexNumber_struct[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchComplexBinary16': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'wfm',
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'wfm',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'struct NIComplexI16_struct[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMeasurement': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'scalarMeasFunction',
                'direction': 'in',
                'enum': 'ScalarMeasurement',
                'grpc_type': 'sint32',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'result',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'result',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMeasurementStats': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'scalarMeasFunction',
                'direction': 'in',
                'enum': 'ScalarMeasurement',
                'grpc_type': 'sint32',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'result',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'result',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'mean',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'mean',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'stdev',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'stdev',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'min',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'min',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'max',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'max',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'numInStats',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'numInStats',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'string',
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
    'GetChannelName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelString',
                'direction': 'out',
                'grpc_type': 'string',
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
    'GetChannelNameFromString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'index',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'name',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetEqualizationFilterCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfCoefficients',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficients',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'coefficients',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessage': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFrequencyResponse': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'frequencies',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'amplitudes',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'amplitudes',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'phases',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'phases',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'bufferSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'numberOfFrequencies',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numberOfFrequencies',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNormalizationCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficientInfo',
                'direction': 'out',
                'grpc_type': 'repeated CoefficientInfo',
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfCoefficientSets'
                },
                'type': 'struct niScope_coefficientInfo[]'
            },
            {
                'cppName': 'numberOfCoefficientSets',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetScalingCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficientInfo',
                'direction': 'out',
                'grpc_type': 'repeated CoefficientInfo',
                'name': 'coefficientInfo',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'numberOfCoefficientSets'
                },
                'type': 'struct niScope_coefficientInfo[]'
            },
            {
                'cppName': 'numberOfCoefficientSets',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numberOfCoefficientSets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'streamName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'streamName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'writerHandle',
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'writerHandle',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niScope_init',
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
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
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
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
    'InitiateAcquisition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ProbeCompensationSignalStart': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ProbeCompensationSignalStop': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'numSamples',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'numSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveform',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'waveform',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(num_samples * actual_num_wfms)'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'wfmInfo',
                'direction': 'out',
                'grpc_type': 'repeated WaveformInfo',
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMeasurement': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'cppName': 'scalarMeasFunction',
                'direction': 'in',
                'enum': 'ScalarMeasurement',
                'grpc_type': 'sint32',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'cppName': 'result',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'result',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'actual_num_wfms'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niScope_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niScope_revision_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'driverRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'driverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'firmwareRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SampleMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleMode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'sampleMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SampleRate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleRate',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'sampleRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niScope_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTriggerEdge': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'whichTrigger',
                'direction': 'in',
                'enum': 'WhichTrigger',
                'grpc_type': 'sint32',
                'name': 'whichTrigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'enum': 'NiScopeInt32AttributeValues',
                'grpc_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'sint32',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'enum': 'NiScopeReal64AttributeValues',
                'grpc_field_number': '5',
                'grpc_mapped_field_number': '6',
                'grpc_raw_field_number': '4',
                'grpc_type': 'double',
                'mapped-enum': 'NiScopeReal64AttributeValuesMapped',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiScopeAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'string',
                'mapped-enum': 'NiScopeStringAttributeValuesMapped',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/functions_addon.py sha256=7e613980f1584101946c6f10b68bd89148e095622a66086c93b108b6de6a9328 bytes=1314 -->
## FILE: source/codegen/metadata/niscope/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/functions_addon.py`
- sha256: `7e613980f1584101946c6f10b68bd89148e095622a66086c93b108b6de6a9328`
- bytes: 1314

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/niscope.proto sha256=2af243969b0b3f109e2a4c34db64dc6f35f35aa45074d5b4aec82c58e2cec529 bytes=70217 -->
## FILE: source/codegen/metadata/niscope/niscope.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/niscope.proto`
- sha256: `2af243969b0b3f109e2a4c34db64dc6f35f35aa45074d5b4aec82c58e2cec529`
- bytes: 70217

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-SCOPE API metadata version 23.3.0d127
//---------------------------------------------------------------------
// Proto file for the NI-SCOPE Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.scope";
option java_outer_classname = "NiScope";
option csharp_namespace = "NationalInstruments.Grpc.Scope";

package niscope_grpc;

import "nidevice.proto";
import "session.proto";

service NiScope {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AcquisitionStatus(AcquisitionStatusRequest) returns (AcquisitionStatusResponse);
  rpc ActualMeasWfmSize(ActualMeasWfmSizeRequest) returns (ActualMeasWfmSizeResponse);
  rpc ActualNumWfms(ActualNumWfmsRequest) returns (ActualNumWfmsResponse);
  rpc ActualRecordLength(ActualRecordLengthRequest) returns (ActualRecordLengthResponse);
  rpc AddWaveformProcessing(AddWaveformProcessingRequest) returns (AddWaveformProcessingResponse);
  rpc AdjustSampleClockRelativeDelay(AdjustSampleClockRelativeDelayRequest) returns (AdjustSampleClockRelativeDelayResponse);
  rpc AutoSetup(AutoSetupRequest) returns (AutoSetupResponse);
  rpc CableSenseSignalStart(CableSenseSignalStartRequest) returns (CableSenseSignalStartResponse);
  rpc CableSenseSignalStop(CableSenseSignalStopRequest) returns (CableSenseSignalStopResponse);
  rpc CalFetchDate(CalFetchDateRequest) returns (CalFetchDateResponse);
  rpc CalFetchTemperature(CalFetchTemperatureRequest) returns (CalFetchTemperatureResponse);
  rpc CalSelfCalibrate(CalSelfCalibrateRequest) returns (CalSelfCalibrateResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViInt64(CheckAttributeViInt64Request) returns (CheckAttributeViInt64Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc ClearWaveformMeasurementStats(ClearWaveformMeasurementStatsRequest) returns (ClearWaveformMeasurementStatsResponse);
  rpc ClearWaveformProcessing(ClearWaveformProcessingRequest) returns (ClearWaveformProcessingResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ConfigureAcquisition(ConfigureAcquisitionRequest) returns (ConfigureAcquisitionResponse);
  rpc ConfigureChanCharacteristics(ConfigureChanCharacteristicsRequest) returns (ConfigureChanCharacteristicsResponse);
  rpc ConfigureClock(ConfigureClockRequest) returns (ConfigureClockResponse);
  rpc ConfigureEqualizationFilterCoefficients(ConfigureEqualizationFilterCoefficientsRequest) returns (ConfigureEqualizationFilterCoefficientsResponse);
  rpc ConfigureHorizontalTiming(ConfigureHorizontalTimingRequest) returns (ConfigureHorizontalTimingResponse);
  rpc ConfigureTriggerDigital(ConfigureTriggerDigitalRequest) returns (ConfigureTriggerDigitalResponse);
  rpc ConfigureTriggerEdge(ConfigureTriggerEdgeRequest) returns (ConfigureTriggerEdgeResponse);
  rpc ConfigureTriggerGlitch(ConfigureTriggerGlitchRequest) returns (ConfigureTriggerGlitchResponse);
  rpc ConfigureTriggerHysteresis(ConfigureTriggerHysteresisRequest) returns (ConfigureTriggerHysteresisResponse);
  rpc ConfigureTriggerImmediate(ConfigureTriggerImmediateRequest) returns (ConfigureTriggerImmediateResponse);
  rpc ConfigureTriggerRunt(ConfigureTriggerRuntRequest) returns (ConfigureTriggerRuntResponse);
  rpc ConfigureTriggerSoftware(ConfigureTriggerSoftwareRequest) returns (ConfigureTriggerSoftwareResponse);
  rpc ConfigureTriggerVideo(ConfigureTriggerVideoRequest) returns (ConfigureTriggerVideoResponse);
  rpc ConfigureTriggerWidth(ConfigureTriggerWidthRequest) returns (ConfigureTriggerWidthResponse);
  rpc ConfigureTriggerWindow(ConfigureTriggerWindowRequest) returns (ConfigureTriggerWindowResponse);
  rpc ConfigureVertical(ConfigureVerticalRequest) returns (ConfigureVerticalResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc ErrorHandler(ErrorHandlerRequest) returns (ErrorHandlerResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc Fetch(FetchRequest) returns (FetchResponse);
  rpc FetchArrayMeasurement(FetchArrayMeasurementRequest) returns (FetchArrayMeasurementResponse);
  rpc FetchBinary16(FetchBinary16Request) returns (FetchBinary16Response);
  rpc FetchBinary32(FetchBinary32Request) returns (FetchBinary32Response);
  rpc FetchBinary8(FetchBinary8Request) returns (FetchBinary8Response);
  rpc FetchComplex(FetchComplexRequest) returns (FetchComplexResponse);
  rpc FetchComplexBinary16(FetchComplexBinary16Request) returns (FetchComplexBinary16Response);
  rpc FetchMeasurement(FetchMeasurementRequest) returns (FetchMeasurementResponse);
  rpc FetchMeasurementStats(FetchMeasurementStatsRequest) returns (FetchMeasurementStatsResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetChannelNameFromString(GetChannelNameFromStringRequest) returns (GetChannelNameFromStringResponse);
  rpc GetEqualizationFilterCoefficients(GetEqualizationFilterCoefficientsRequest) returns (GetEqualizationFilterCoefficientsResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetErrorMessage(GetErrorMessageRequest) returns (GetErrorMessageResponse);
  rpc GetFrequencyResponse(GetFrequencyResponseRequest) returns (GetFrequencyResponseResponse);
  rpc GetNormalizationCoefficients(GetNormalizationCoefficientsRequest) returns (GetNormalizationCoefficientsResponse);
  rpc GetScalingCoefficients(GetScalingCoefficientsRequest) returns (GetScalingCoefficientsResponse);
  rpc GetStreamEndpointHandle(GetStreamEndpointHandleRequest) returns (GetStreamEndpointHandleResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitiateAcquisition(InitiateAcquisitionRequest) returns (InitiateAcquisitionResponse);
  rpc ProbeCompensationSignalStart(ProbeCompensationSignalStartRequest) returns (ProbeCompensationSignalStartResponse);
  rpc ProbeCompensationSignalStop(ProbeCompensationSignalStopRequest) returns (ProbeCompensationSignalStopResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc ReadMeasurement(ReadMeasurementRequest) returns (ReadMeasurementResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc SampleMode(SampleModeRequest) returns (SampleModeResponse);
  rpc SampleRate(SampleRateRequest) returns (SampleRateResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareTriggerEdge(SendSoftwareTriggerEdgeRequest) returns (SendSoftwareTriggerEdgeResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
}

enum NiScopeAttribute {
  NISCOPE_ATTRIBUTE_UNSPECIFIED = 0;
  NISCOPE_ATTRIBUTE_RANGE_CHECK = 1050002;
  NISCOPE_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NISCOPE_ATTRIBUTE_CACHE = 1050004;
  NISCOPE_ATTRIBUTE_SIMULATE = 1050005;
  NISCOPE_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NISCOPE_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NISCOPE_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NISCOPE_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NISCOPE_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NISCOPE_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NISCOPE_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NISCOPE_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NISCOPE_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NISCOPE_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NISCOPE_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NISCOPE_ATTRIBUTE_HORZ_NUM_RECORDS = 1150001;
  NISCOPE_ATTRIBUTE_INPUT_CLOCK_SOURCE = 1150002;
  NISCOPE_ATTRIBUTE_OUTPUT_CLOCK_SOURCE = 1150003;
  NISCOPE_ATTRIBUTE_HORZ_ENFORCE_REALTIME = 1150004;
  NISCOPE_ATTRIBUTE_BINARY_SAMPLE_WIDTH = 1150005;
  NISCOPE_ATTRIBUTE_TRIGGER_HYSTERESIS = 1150006;
  NISCOPE_ATTRIBUTE_CLOCK_SYNC_PULSE_SOURCE = 1150007;
  NISCOPE_ATTRIBUTE_MASTER_ENABLE = 1150008;
  NISCOPE_ATTRIBUTE_MIN_SAMPLE_RATE = 1150009;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_MODE = 1150012;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_LOW_LEVEL = 1150013;
  NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_HIGH_LEVEL = 1150014;
  NISCOPE_ATTRIBUTE_MEAS_REF_LEVEL_UNITS = 1150016;
  NISCOPE_ATTRIBUTE_MEAS_OTHER_CHANNEL = 1150018;
  NISCOPE_ATTRIBUTE_MEAS_HYSTERESIS_PERCENT = 1150019;
  NISCOPE_ATTRIBUTE_MEAS_LAST_ACQ_HISTOGRAM_SIZE = 1150020;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_SIZE = 1150021;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS = 1150022;
  NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS = 1150023;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_SIZE = 1150024;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_VOLTS = 1150025;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_VOLTS = 1150026;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_TIME = 1150027;
  NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_TIME = 1150028;
  NISCOPE_ATTRIBUTE_MEAS_POLYNOMIAL_INTERPOLATION_ORDER = 1150029;
  NISCOPE_ATTRIBUTE_MEAS_INTERPOLATION_SAMPLING_FACTOR = 1150030;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_CUTOFF_FREQ = 1150031;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_CENTER_FREQ = 1150032;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_RIPPLE = 1150033;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT = 1150034;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TYPE = 1150035;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_ORDER = 1150036;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_TAPS = 1150037;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_LOW_REF_LEVEL = 1150038;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_MID_REF_LEVEL = 1150039;
  NISCOPE_ATTRIBUTE_MEAS_CHAN_HIGH_REF_LEVEL = 1150040;
  NISCOPE_ATTRIBUTE_MEAS_FILTER_WIDTH = 1150041;
  NISCOPE_ATTRIBUTE_MEAS_FIR_FILTER_WINDOW = 1150042;
  NISCOPE_ATTRIBUTE_MEAS_ARRAY_GAIN = 1150043;
  NISCOPE_ATTRIBUTE_MEAS_ARRAY_OFFSET = 1150044;
  NISCOPE_ATTRIBUTE_MEAS_PERCENTAGE_METHOD = 1150045;
  NISCOPE_ATTRIBUTE_ACQ_ARM_SOURCE = 1150053;
  NISCOPE_ATTRIBUTE_IS_PROBE_COMP_ON = 1150066;
  NISCOPE_ATTRIBUTE_USE_SPEC_INITIAL_X = 1150067;
  NISCOPE_ATTRIBUTE_ALLOW_MORE_RECORDS_THAN_MEMORY = 1150068;
  NISCOPE_ATTRIBUTE_ONBOARD_MEMORY_SIZE = 1150069;
  NISCOPE_ATTRIBUTE_RIS_NUM_AVERAGES = 1150070;
  NISCOPE_ATTRIBUTE_RIS_METHOD = 1150071;
  NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_DATA = 1150072;
  NISCOPE_ATTRIBUTE_MAX_REAL_TIME_SAMPLING_RATE = 1150073;
  NISCOPE_ATTRIBUTE_MAX_RIS_RATE = 1150074;
  NISCOPE_ATTRIBUTE_TRIGGER_IMPEDANCE = 1150075;
  NISCOPE_ATTRIBUTE_DEVICE_NUMBER = 1150076;
  NISCOPE_ATTRIBUTE_FETCH_RELATIVE_TO = 1150077;
  NISCOPE_ATTRIBUTE_FETCH_OFFSET = 1150078;
  NISCOPE_ATTRIBUTE_FETCH_RECORD_NUMBER = 1150079;
  NISCOPE_ATTRIBUTE_FETCH_NUM_RECORDS = 1150080;
  NISCOPE_ATTRIBUTE_FETCH_MEAS_NUM_SAMPLES = 1150081;
  NISCOPE_ATTRIBUTE_POINTS_DONE = 1150082;
  NISCOPE_ATTRIBUTE_RECORDS_DONE = 1150083;
  NISCOPE_ATTRIBUTE_BACKLOG = 1150084;
  NISCOPE_ATTRIBUTE_DEVICE_TEMPERATURE = 1150086;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC = 1150087;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE = 1150088;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV = 1150089;
  NISCOPE_ATTRIBUTE_REF_CLK_RATE = 1150090;
  NISCOPE_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL = 1150091;
  NISCOPE_ATTRIBUTE_ENABLE_DC_RESTORE = 1150093;
  NISCOPE_ATTRIBUTE_ADV_TRIG_SRC = 1150094;
  NISCOPE_ATTRIBUTE_ARM_REF_TRIG_SRC = 1150095;
  NISCOPE_ATTRIBUTE_REF_TRIG_TDC_ENABLE = 1150096;
  NISCOPE_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150097;
  NISCOPE_ATTRIBUTE_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL = 1150098;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_OUTPUT_TERMINAL = 1150099;
  NISCOPE_ATTRIBUTE_POLL_INTERVAL = 1150100;
  NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL = 1150101;
  NISCOPE_ATTRIBUTE_RESOLUTION = 1150102;
  NISCOPE_ATTRIBUTE_START_TO_REF_TRIGGER_HOLDOFF = 1150103;
  NISCOPE_ATTRIBUTE_SERIAL_NUMBER = 1150104;
  NISCOPE_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE = 1150105;
  NISCOPE_ATTRIBUTE_RIS_IN_AUTO_SETUP_ENABLE = 1150106;
  NISCOPE_ATTRIBUTE_CHANNEL_TERMINAL_CONFIGURATION = 1150107;
  NISCOPE_ATTRIBUTE_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL = 1150109;
  NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL = 1150110;
  NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_OUTPUT_TERMINAL = 1150111;
  NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL = 1150112;
  NISCOPE_ATTRIBUTE_ENABLE_TIME_INTERLEAVED_SAMPLING = 1150128;
  NISCOPE_ATTRIBUTE_5V_OUT_OUTPUT_TERMINAL = 1150129;
  NISCOPE_ATTRIBUTE_RUNT_TIME_CONDITION = 1150132;
  NISCOPE_ATTRIBUTE_RUNT_TIME_LOW_LIMIT = 1150133;
  NISCOPE_ATTRIBUTE_RUNT_TIME_HIGH_LIMIT = 1150134;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_VOLTAGE = 1150137;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_MODE = 1150138;
  NISCOPE_ATTRIBUTE_CABLE_SENSE_SIGNAL_ENABLE = 1150139;
  NISCOPE_ATTRIBUTE_ENABLED_CHANNELS = 1150140;
  NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_TERMINAL_NAME = 1150141;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_TERMINAL_NAME = 1150142;
  NISCOPE_ATTRIBUTE_ADVANCE_TRIGGER_TERMINAL_NAME = 1150143;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_TERMINAL_NAME = 1150144;
  NISCOPE_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME = 1150145;
  NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME = 1150146;
  NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_TERMINAL_NAME = 1150147;
  NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_TERMINAL_NAME = 1150148;
  NISCOPE_ATTRIBUTE_FLEX_FIR_ANTIALIAS_FILTER_TYPE = 1150271;
  NISCOPE_ATTRIBUTE_TRIGGER_AUTO_TRIGGERED = 1150278;
  NISCOPE_ATTRIBUTE_SIGNAL_COND_GAIN = 1150279;
  NISCOPE_ATTRIBUTE_SIGNAL_COND_OFFSET = 1150280;
  NISCOPE_ATTRIBUTE_DDC_ENABLED = 1150300;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_ENABLED = 1150302;
  NISCOPE_ATTRIBUTE_DDC_CENTER_FREQUENCY = 1150303;
  NISCOPE_ATTRIBUTE_DDC_DATA_PROCESSING_MODE = 1150304;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_I = 1150305;
  NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_Q = 1150306;
  NISCOPE_ATTRIBUTE_DIGITAL_GAIN = 1150307;
  NISCOPE_ATTRIBUTE_DIGITAL_OFFSET = 1150308;
  NISCOPE_ATTRIBUTE_OVERFLOW_ERROR_REPORTING = 1150309;
  NISCOPE_ATTRIBUTE_DDC_Q_SOURCE = 1150310;
  NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_IQ_DATA = 1150311;
  NISCOPE_ATTRIBUTE_EQUALIZATION_NUM_COEFFICIENTS = 1150312;
  NISCOPE_ATTRIBUTE_EQUALIZATION_FILTER_ENABLED = 1150313;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_DETECTOR_LOCATION = 1150314;
  NISCOPE_ATTRIBUTE_REF_TRIGGER_MINIMUM_QUIET_TIME = 1150315;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE = 1150316;
  NISCOPE_ATTRIBUTE_BANDPASS_FILTER_ENABLED = 1150318;
  NISCOPE_ATTRIBUTE_DITHER_ENABLED = 1150319;
  NISCOPE_ATTRIBUTE_FRACTIONAL_RESAMPLE_ENABLED = 1150320;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH = 1150321;
  NISCOPE_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE = 1150322;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_AVAIL_IN_ENDPOINT = 1150328;
  NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR = 1150329;
  NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE = 1150330;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR = 1150331;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR_TYPE = 1150332;
  NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_SIZE = 1150333;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_PUSH_MESSAGE_ON = 1150334;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR = 1150335;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE = 1150336;
  NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_VALUE = 1150337;
  NISCOPE_ATTRIBUTE_P2P_ENABLED = 1150338;
  NISCOPE_ATTRIBUTE_P2P_CHANNELS_TO_STREAM = 1150339;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED = 1150340;
  NISCOPE_ATTRIBUTE_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT = 1150341;
  NISCOPE_ATTRIBUTE_P2P_ENDPOINT_SIZE = 1150342;
  NISCOPE_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED = 1150343;
  NISCOPE_ATTRIBUTE_P2P_ENDPOINT_OVERFLOW = 1150344;
  NISCOPE_ATTRIBUTE_P2P_FIFO_ENDPOINT_COUNT = 1150345;
  NISCOPE_ATTRIBUTE_P2P_ONBOARD_MEMORY_ENABLED = 1150354;
  NISCOPE_ATTRIBUTE_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF = 1150366;
  NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_MULT = 1150367;
  NISCOPE_ATTRIBUTE_P2P_STREAM_RELATIVE_TO = 1150373;
  NISCOPE_ATTRIBUTE_ABSOLUTE_SAMPLE_CLOCK_OFFSET = 1150374;
  NISCOPE_ATTRIBUTE_FPGA_BITFILE_PATH = 1150375;
  NISCOPE_ATTRIBUTE_INTERLEAVING_OFFSET_CORRECTION_ENABLED = 1150376;
  NISCOPE_ATTRIBUTE_HIGH_PASS_FILTER_FREQUENCY = 1150377;
  NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED_PER_RECORD = 1150380;
  NISCOPE_ATTRIBUTE_PLL_LOCK_STATUS = 1151303;
  NISCOPE_ATTRIBUTE_VERTICAL_RANGE = 1250001;
  NISCOPE_ATTRIBUTE_VERTICAL_OFFSET = 1250002;
  NISCOPE_ATTRIBUTE_VERTICAL_COUPLING = 1250003;
  NISCOPE_ATTRIBUTE_PROBE_ATTENUATION = 1250004;
  NISCOPE_ATTRIBUTE_CHANNEL_ENABLED = 1250005;
  NISCOPE_ATTRIBUTE_MAX_INPUT_FREQUENCY = 1250006;
  NISCOPE_ATTRIBUTE_HORZ_TIME_PER_RECORD = 1250007;
  NISCOPE_ATTRIBUTE_HORZ_RECORD_LENGTH = 1250008;
  NISCOPE_ATTRIBUTE_HORZ_MIN_NUM_PTS = 1250009;
  NISCOPE_ATTRIBUTE_HORZ_SAMPLE_RATE = 1250010;
  NISCOPE_ATTRIBUTE_HORZ_RECORD_REF_POSITION = 1250011;
  NISCOPE_ATTRIBUTE_TRIGGER_TYPE = 1250012;
  NISCOPE_ATTRIBUTE_TRIGGER_SOURCE = 1250013;
  NISCOPE_ATTRIBUTE_TRIGGER_COUPLING = 1250014;
  NISCOPE_ATTRIBUTE_TRIGGER_DELAY_TIME = 1250015;
  NISCOPE_ATTRIBUTE_TRIGGER_HOLDOFF = 1250016;
  NISCOPE_ATTRIBUTE_TRIGGER_LEVEL = 1250017;
  NISCOPE_ATTRIBUTE_TRIGGER_SLOPE = 1250018;
  NISCOPE_ATTRIBUTE_ACQUISITION_TYPE = 1250101;
  NISCOPE_ATTRIBUTE_TRIGGER_MODIFIER = 1250102;
  NISCOPE_ATTRIBUTE_INPUT_IMPEDANCE = 1250103;
  NISCOPE_ATTRIBUTE_SAMPLE_MODE = 1250106;
  NISCOPE_ATTRIBUTE_ACQUISITION_START_TIME = 1250109;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_SIGNAL_FORMAT = 1250201;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_POLARITY = 1250204;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_EVENT = 1250205;
  NISCOPE_ATTRIBUTE_TV_TRIGGER_LINE_NUMBER = 1250206;
  NISCOPE_ATTRIBUTE_RUNT_HIGH_THRESHOLD = 1250301;
  NISCOPE_ATTRIBUTE_RUNT_LOW_THRESHOLD = 1250302;
  NISCOPE_ATTRIBUTE_RUNT_POLARITY = 1250303;
  NISCOPE_ATTRIBUTE_GLITCH_WIDTH = 1250401;
  NISCOPE_ATTRIBUTE_GLITCH_POLARITY = 1250402;
  NISCOPE_ATTRIBUTE_GLITCH_CONDITION = 1250403;
  NISCOPE_ATTRIBUTE_WIDTH_LOW_THRESHOLD = 1250501;
  NISCOPE_ATTRIBUTE_WIDTH_HIGH_THRESHOLD = 1250502;
  NISCOPE_ATTRIBUTE_WIDTH_POLARITY = 1250503;
  NISCOPE_ATTRIBUTE_WIDTH_CONDITION = 1250504;
  NISCOPE_ATTRIBUTE_MEAS_HIGH_REF = 1250607;
  NISCOPE_ATTRIBUTE_MEAS_LOW_REF = 1250608;
  NISCOPE_ATTRIBUTE_MEAS_MID_REF = 1250609;
}

enum AcquisitionStatus {
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_IN_PROGRESS = 0;
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_COMPLETE = 1;
  ACQUISITION_STATUS_NISCOPE_VAL_ACQ_STATUS_UNKNOWN = -1;
}

enum ArrayMeasurement {
  ARRAY_MEASUREMENT_UNSPECIFIED = 0;
  ARRAY_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT = 4000;
  ARRAY_MEASUREMENT_NISCOPE_VAL_LAST_ACQ_HISTOGRAM = 4001;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_PHASE_SPECTRUM = 4002;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS = 4003;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM = 4005;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_INTEGRAL = 4006;
  ARRAY_MEASUREMENT_NISCOPE_VAL_DERIVATIVE = 4007;
  ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE = 4008;
  ARRAY_MEASUREMENT_NISCOPE_VAL_HANNING_WINDOW = 4009;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FLAT_TOP_WINDOW = 4010;
  ARRAY_MEASUREMENT_NISCOPE_VAL_POLYNOMIAL_INTERPOLATION = 4011;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTIPLY_CHANNELS = 4012;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ADD_CHANNELS = 4013;
  ARRAY_MEASUREMENT_NISCOPE_VAL_SUBTRACT_CHANNELS = 4014;
  ARRAY_MEASUREMENT_NISCOPE_VAL_DIVIDE_CHANNELS = 4015;
  ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE = 4016;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BUTTERWORTH_FILTER = 4017;
  ARRAY_MEASUREMENT_NISCOPE_VAL_CHEBYSHEV_FILTER = 4018;
  ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_DB = 4019;
  ARRAY_MEASUREMENT_NISCOPE_VAL_HAMMING_WINDOW = 4020;
  ARRAY_MEASUREMENT_NISCOPE_VAL_WINDOWED_FIR_FILTER = 4021;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BESSEL_FILTER = 4022;
  ARRAY_MEASUREMENT_NISCOPE_VAL_TRIANGLE_WINDOW = 4023;
  ARRAY_MEASUREMENT_NISCOPE_VAL_BLACKMAN_WINDOW = 4024;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_OFFSET = 4025;
  ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_GAIN = 4026;
}

enum CalibrationTypes {
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_EXTERNAL = 0;
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_SELF = 1;
  CALIBRATION_TYPES_NISCOPE_VAL_CAL_MANUFACTURE = 2;
}

enum ClearableMeasurement {
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_TIME = 0;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_ALL_MEASUREMENTS = 10000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM = 4005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE = 4016;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FREQUENCY = 2;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY = 1016;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY = 1008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PERIOD = 3;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD = 1015;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_TIME = 1;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE = 1010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE = 1011;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_OVERSHOOT = 18;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PRESHOOT = 19;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS = 4;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS = 16;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE = 1012;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE = 1009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE = 10;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE = 17;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE = 1013;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX = 6;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN = 7;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK = 5;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH = 8;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW = 9;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AMPLITUDE = 15;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP = 1007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE = 1006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP = 1017;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG = 11;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_POS = 12;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG = 13;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS = 14;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_INTEGRAL = 1005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_AREA = 1003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA = 1004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_DELAY = 1014;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY = 1018;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS = 1000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS = 1001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS = 1002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN = 2000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV = 2001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN = 2003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE = 2010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX = 2005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN = 2006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK = 2002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV = 2007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV = 2008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV = 2009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS = 2004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS = 2011;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN = 3000;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_STDEV = 3001;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN = 3003;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MODE = 3010;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MAX = 3005;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MIN = 3006;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK = 3002;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV = 3007;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV = 3008;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV = 3009;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_HITS = 3004;
  CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS = 3011;
}

enum ClockingTerminalValues {
  CLOCKING_TERMINAL_VALUES_UNSPECIFIED = 0;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_NO_SOURCE = 1;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_RTSI_CLOCK = 2;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_EXTERNAL = 3;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_0 = 4;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_1 = 5;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_2 = 6;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_IN = 7;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_OUT = 8;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_INTERNAL10MHZ_OSC = 9;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK = 10;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK10 = 11;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK100 = 12;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXIE_DSTAR_A = 13;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_IN = 14;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_OUT = 15;
  CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK = 16;
}

enum ExportableSignals {
  EXPORTABLE_SIGNALS_UNSPECIFIED = 0;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_TRIGGER = 1;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_START_TRIGGER = 2;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_ACQUISITION_EVENT = 3;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_RECORD_EVENT = 4;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_ADVANCE_TRIGGER = 5;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_ADVANCE_EVENT = 6;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_START_EVENT = 7;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_REF_EVENT = 10;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_5V_OUT = 13;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_CLOCK = 100;
  EXPORTABLE_SIGNALS_NISCOPE_VAL_SAMPLE_CLOCK = 101;
}

enum GlitchCondition {
  GLITCH_CONDITION_UNSPECIFIED = 0;
  GLITCH_CONDITION_NISCOPE_VAL_GLITCH_GREATER_THAN = 2;
  GLITCH_CONDITION_NISCOPE_VAL_GLITCH_LESS_THAN = 1;
}

enum GlitchPolarity {
  GLITCH_POLARITY_UNSPECIFIED = 0;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_POSITIVE = 1;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_NEGATIVE = 2;
  GLITCH_POLARITY_NISCOPE_VAL_GLITCH_EITHER = 3;
}

enum NiScopeInt32AttributeValues {
  option allow_alias = true;
  NISCOPE_INT32_UNSPECIFIED = 0;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_NORMAL = 0;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_FLEXRES = 1001;
  NISCOPE_INT32_ACQUISITION_TYPE_VAL_DDC = 1002;
  NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL = 0;
  NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL = 1;
  NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_REAL = 0;
  NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_COMPLEX = 1;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_NONE = 0;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HANNING = 409;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_FLAT_TOP = 410;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HAMMING = 420;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_TRIANGLE = 423;
  NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_BLACKMAN = 424;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_READ_POINTER = 388;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_PRETRIGGER = 477;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_NOW = 481;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_START = 482;
  NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_TRIGGER = 483;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_STANDARD = 0;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_HANNING = 1;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_16_TAP_HANNING = 2;
  NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_8_TAP_HANNING = 3;
  NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_GREATER_THAN = 2;
  NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_LESS_THAN = 1;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_POSITIVE = 1;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_NEGATIVE = 2;
  NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_EITHER = 3;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_LOWPASS = 0;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_HIGHPASS = 1;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDPASS = 2;
  NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDSTOP = 3;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_LOW_HIGH = 0;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_MIN_MAX = 1;
  NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_BASE_TOP = 2;
  NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_VOLTAGE = 0;
  NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_PERCENTAGE = 1;
  NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_NEVER = 0;
  NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_DONE = 1;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR = 0;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_WARNING = 1;
  NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED = 2;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_START_TRIGGER = 0;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER = 1;
  NISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER = 2;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_EXACT_NUM_AVERAGES = 1;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_MIN_NUM_AVERAGES = 2;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_INCOMPLETE = 3;
  NISCOPE_INT32_RIS_METHOD_VAL_RIS_LIMITED_BIN_WIDTH = 5;
  NISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_ANALOG_DETECTION_CIRCUIT = 0;
  NISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_DDC_OUTPUT = 1;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_POSITIVE = 1;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_NEGATIVE = 2;
  NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_EITHER = 3;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_NONE = 0;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_WITHIN = 1;
  NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_OUTSIDE = 2;
  NISCOPE_INT32_SAMPLE_MODE_VAL_REAL_TIME = 0;
  NISCOPE_INT32_SAMPLE_MODE_VAL_EQUIVALENT_TIME = 1;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED = 0;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_UNBALANCED_DIFFERENTIAL = 1;
  NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL = 2;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC = 0;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_DC = 1;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_HF_REJECT = 3;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_LF_REJECT = 4;
  NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC_PLUS_HF_REJECT = 1001;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_NO_TRIGGER_MOD = 1;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO = 2;
  NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO_LEVEL = 3;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_NEGATIVE = 0;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_POSITIVE = 1;
  NISCOPE_INT32_TRIGGER_SLOPE_VAL_SLOPE_EITHER = 3;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_EDGE_TRIGGER = 1;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_HYSTERESIS_TRIGGER = 1001;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_DIGITAL_TRIGGER = 1002;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_WINDOW_TRIGGER = 1003;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_SOFTWARE_TRIGGER = 1004;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_TV_TRIGGER = 5;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_GLITCH_TRIGGER = 4;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_WIDTH_TRIGGER = 2;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_RUNT_TRIGGER = 3;
  NISCOPE_INT32_TRIGGER_TYPE_VAL_IMMEDIATE_TRIGGER = 6;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_WINDOW = 0;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_LEAVING_WINDOW = 1;
  NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_OR_LEAVING_WINDOW = 2;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_AC = 0;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_DC = 1;
  NISCOPE_INT32_VERTICAL_COUPLING_VAL_GND = 2;
  NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_POSITIVE = 1;
  NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_NEGATIVE = 2;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_NTSC = 1;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_PAL = 2;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_SECAM = 3;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_M_PAL = 1001;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_60_FIELDS_PER_SECOND = 1011;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_60_FRAMES_PER_SECOND = 1016;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576I_50_FIELDS_PER_SECOND = 1020;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576P_50_FRAMES_PER_SECOND = 1025;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_50_FRAMES_PER_SECOND = 1031;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_60_FRAMES_PER_SECOND = 1033;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND = 1040;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND = 1042;
  NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND = 1045;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD1 = 1;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD2 = 2;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_FIELD = 3;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_LINE = 4;
  NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_LINE_NUMBER = 5;
  NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_WITHIN = 1;
  NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_OUTSIDE = 2;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_POSITIVE = 1;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_NEGATIVE = 2;
  NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_EITHER = 3;
}

enum NiScopeReal64AttributeValues {
  option allow_alias = true;
  NISCOPE_REAL64_UNSPECIFIED = 0;
  NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_DISABLED = 0;
  NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_ON_DEMAND = 1;
}

enum NiScopeReal64AttributeValuesMapped {
  NISCOPE_REAL64_MAPPED_UNSPECIFIED = 0;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_50_OHMS = 1;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_75_OHMS = 2;
  NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_1_MEG_OHM = 3;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_DEVICE_DEFAULT = 4;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_FULL = 5;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_BANDWIDTH = 6;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_BANDWIDTH = 7;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_MAX_INPUT_FREQUENCY = 8;
  NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_MAX_INPUT_FREQUENCY = 9;
}

enum NiScopeStringAttributeValuesMapped {
  NISCOPE_STRING_MAPPED_UNSPECIFIED = 0;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_CLK_IN = 1;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_NO_SOURCE = 2;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXI_STAR = 3;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXIE_DSTAR_A = 4;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_AUX_0_CLK_IN = 5;
  NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_ONBOARD_CONFIGURABLE_RATE_CLK = 6;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_IMMEDIATE = 7;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_EXTERNAL = 8;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_SW_TRIG_FUNC = 9;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL0 = 10;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL1 = 11;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL2 = 12;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL3 = 13;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL4 = 14;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL5 = 15;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL6 = 16;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL7 = 17;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL0 = 18;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL1 = 19;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PXI_STAR = 20;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_0 = 21;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_1 = 22;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_2 = 23;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_3 = 24;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_4 = 25;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_5 = 26;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_6 = 27;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_7 = 28;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_0 = 29;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_1 = 30;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_2 = 31;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_3 = 32;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_4 = 33;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_5 = 34;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_6 = 35;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_7 = 36;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_0 = 37;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_1 = 38;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_3 = 39;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_4 = 40;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_5 = 41;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_6 = 42;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_7 = 43;
  NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_2 = 44;
}

enum Option {
  OPTION_NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS = 0;
  OPTION_NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION = 1;
}

enum RuntPolarity {
  RUNT_POLARITY_UNSPECIFIED = 0;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_POSITIVE = 1;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_NEGATIVE = 2;
  RUNT_POLARITY_NISCOPE_VAL_RUNT_EITHER = 3;
}

enum ScalarMeasurement {
  SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_TIME = 0;
  SCALAR_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT = 4000;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_TIME = 1;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FREQUENCY = 2;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PERIOD = 3;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS = 4;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK = 5;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX = 6;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN = 7;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH = 8;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW = 9;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE = 10;
  SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG = 11;
  SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_POS = 12;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG = 13;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS = 14;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AMPLITUDE = 15;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS = 16;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE = 17;
  SCALAR_MEASUREMENT_NISCOPE_VAL_OVERSHOOT = 18;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PRESHOOT = 19;
  SCALAR_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS = 1000;
  SCALAR_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS = 1001;
  SCALAR_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS = 1002;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AREA = 1003;
  SCALAR_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA = 1004;
  SCALAR_MEASUREMENT_NISCOPE_VAL_INTEGRAL = 1005;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE = 1006;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP = 1007;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY = 1008;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE = 1009;
  SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE = 1010;
  SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE = 1011;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE = 1012;
  SCALAR_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE = 1013;
  SCALAR_MEASUREMENT_NISCOPE_VAL_TIME_DELAY = 1014;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD = 1015;
  SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY = 1016;
  SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP = 1017;
  SCALAR_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY = 1018;
}

enum TriggerCoupling {
  TRIGGER_COUPLING_NISCOPE_VAL_AC = 0;
  TRIGGER_COUPLING_NISCOPE_VAL_DC = 1;
  TRIGGER_COUPLING_NISCOPE_VAL_HF_REJECT = 3;
  TRIGGER_COUPLING_NISCOPE_VAL_LF_REJECT = 4;
  TRIGGER_COUPLING_NISCOPE_VAL_AC_PLUS_HF_REJECT = 1001;
}

enum TriggerSlope {
  TRIGGER_SLOPE_NISCOPE_VAL_NEGATIVE = 0;
  TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE = 1;
  TRIGGER_SLOPE_NISCOPE_VAL_SLOPE_EITHER = 3;
}

enum TriggerWindowMode {
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_WINDOW = 0;
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_LEAVING_WINDOW = 1;
  TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW = 2;
}

enum VerticalCoupling {
  VERTICAL_COUPLING_NISCOPE_VAL_AC = 0;
  VERTICAL_COUPLING_NISCOPE_VAL_DC = 1;
  VERTICAL_COUPLING_NISCOPE_VAL_GND = 2;
}

enum VideoPolarity {
  VIDEO_POLARITY_UNSPECIFIED = 0;
  VIDEO_POLARITY_NISCOPE_VAL_TV_POSITIVE = 1;
  VIDEO_POLARITY_NISCOPE_VAL_TV_NEGATIVE = 2;
}

enum VideoSignalFormat {
  VIDEO_SIGNAL_FORMAT_UNSPECIFIED = 0;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_NTSC = 1;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_PAL = 2;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_SECAM = 3;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_M_PAL = 1001;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND = 1011;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND = 1016;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND = 1020;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND = 1025;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND = 1031;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND = 1033;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND = 1040;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND = 1042;
  VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND = 1045;
}

enum VideoTriggerEvent {
  VIDEO_TRIGGER_EVENT_UNSPECIFIED = 0;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD1 = 1;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD2 = 2;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_FIELD = 3;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_LINE = 4;
  VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_LINE_NUMBER = 5;
}

enum WhichTrigger {
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_START = 0;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE = 1;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE = 2;
  WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE = 3;
}

enum WidthCondition {
  WIDTH_CONDITION_UNSPECIFIED = 0;
  WIDTH_CONDITION_NISCOPE_VAL_WIDTH_WITHIN = 1;
  WIDTH_CONDITION_NISCOPE_VAL_WIDTH_OUTSIDE = 2;
}

enum WidthPolarity {
  WIDTH_POLARITY_UNSPECIFIED = 0;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_POSITIVE = 1;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_NEGATIVE = 2;
  WIDTH_POLARITY_NISCOPE_VAL_WIDTH_EITHER = 3;
}

message CoefficientInfo {
  double offset = 1;
  double gain = 2;
  double reserved1 = 3;
  double reserved2 = 4;
}

message WaveformInfo {
  double absolute_initial_x = 1;
  double relative_initial_x = 2;
  double x_increment = 3;
  sint32 actual_samples = 4;
  double offset = 5;
  double gain = 6;
  double reserved1 = 7;
  double reserved2 = 8;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message AcquisitionStatusRequest {
  nidevice_grpc.Session vi = 1;
}

message AcquisitionStatusResponse {
  int32 status = 1;
  AcquisitionStatus acquisition_status = 2;
  sint32 acquisition_status_raw = 3;
}

message ActualMeasWfmSizeRequest {
  nidevice_grpc.Session vi = 1;
  oneof array_meas_function_enum {
    ArrayMeasurement array_meas_function = 2;
    sint32 array_meas_function_raw = 3;
  }
}

message ActualMeasWfmSizeResponse {
  int32 status = 1;
  sint32 meas_waveform_size = 2;
}

message ActualNumWfmsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ActualNumWfmsResponse {
  int32 status = 1;
  sint32 num_wfms = 2;
}

message ActualRecordLengthRequest {
  nidevice_grpc.Session vi = 1;
}

message ActualRecordLengthResponse {
  int32 status = 1;
  sint32 record_length = 2;
}

message AddWaveformProcessingRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof meas_function_enum {
    ArrayMeasurement meas_function = 3;
    sint32 meas_function_raw = 4;
  }
}

message AddWaveformProcessingResponse {
  int32 status = 1;
}

message AdjustSampleClockRelativeDelayRequest {
  nidevice_grpc.Session vi = 1;
  double delay = 2;
}

message AdjustSampleClockRelativeDelayResponse {
  int32 status = 1;
}

message AutoSetupRequest {
  nidevice_grpc.Session vi = 1;
}

message AutoSetupResponse {
  int32 status = 1;
}

message CableSenseSignalStartRequest {
  nidevice_grpc.Session vi = 1;
}

message CableSenseSignalStartResponse {
  int32 status = 1;
}

message CableSenseSignalStopRequest {
  nidevice_grpc.Session vi = 1;
}

message CableSenseSignalStopResponse {
  int32 status = 1;
}

message CalFetchDateRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_one_enum {
    CalibrationTypes which_one = 2;
    sint32 which_one_raw = 3;
  }
}

message CalFetchDateResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
}

message CalFetchTemperatureRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_one_enum {
    CalibrationTypes which_one = 2;
    sint32 which_one_raw = 3;
  }
}

message CalFetchTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message CalSelfCalibrateRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof option_enum {
    Option option = 3;
    sint32 option_raw = 4;
  }
}

message CalSelfCalibrateResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  bool value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    sint32 value_raw = 4;
    NiScopeInt32AttributeValues value = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message CheckAttributeViInt64Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    double value_raw = 4;
    NiScopeReal64AttributeValues value = 5;
    NiScopeReal64AttributeValuesMapped value_mapped = 6;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    NiScopeStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message ClearWaveformMeasurementStatsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  oneof clearable_measurement_function_enum {
    ClearableMeasurement clearable_measurement_function = 3;
    sint32 clearable_measurement_function_raw = 4;
  }
}

message ClearWaveformMeasurementStatsResponse {
  int32 status = 1;
}

message ClearWaveformProcessingRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message ClearWaveformProcessingResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ConfigureAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 acquisition_type = 2;
}

message ConfigureAcquisitionResponse {
  int32 status = 1;
}

message ConfigureChanCharacteristicsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double input_impedance = 3;
  double max_input_frequency = 4;
}

message ConfigureChanCharacteristicsResponse {
  int32 status = 1;
}

message ConfigureClockRequest {
  nidevice_grpc.Session vi = 1;
  oneof input_clock_source_enum {
    string input_clock_source_raw = 2;
    ClockingTerminalValues input_clock_source_mapped = 6;
  }
  oneof output_clock_source_enum {
    string output_clock_source_raw = 3;
    ClockingTerminalValues output_clock_source_mapped = 7;
  }
  oneof clock_sync_pulse_source_enum {
    string clock_sync_pulse_source_raw = 4;
    ClockingTerminalValues clock_sync_pulse_source_mapped = 8;
  }
  bool master_enabled = 5;
}

message ConfigureClockResponse {
  int32 status = 1;
}

message ConfigureEqualizationFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  repeated double coefficients = 3;
}

message ConfigureEqualizationFilterCoefficientsResponse {
  int32 status = 1;
}

message ConfigureHorizontalTimingRequest {
  nidevice_grpc.Session vi = 1;
  double min_sample_rate = 2;
  sint32 min_num_pts = 3;
  double ref_position = 4;
  sint32 num_records = 5;
  bool enforce_realtime = 6;
}

message ConfigureHorizontalTimingResponse {
  int32 status = 1;
}

message ConfigureTriggerDigitalRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  oneof slope_enum {
    TriggerSlope slope = 3;
    sint32 slope_raw = 4;
  }
  double holdoff = 5;
  double delay = 6;
}

message ConfigureTriggerDigitalResponse {
  int32 status = 1;
}

message ConfigureTriggerEdgeRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  oneof slope_enum {
    TriggerSlope slope = 4;
    sint32 slope_raw = 5;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 6;
    sint32 trigger_coupling_raw = 7;
  }
  double holdoff = 8;
  double delay = 9;
}

message ConfigureTriggerEdgeResponse {
  int32 status = 1;
}

message ConfigureTriggerGlitchRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double width = 4;
  oneof polarity_enum {
    GlitchPolarity polarity = 5;
    sint32 polarity_raw = 6;
  }
  oneof glitch_condition_enum {
    GlitchCondition glitch_condition = 7;
    sint32 glitch_condition_raw = 8;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 9;
    sint32 trigger_coupling_raw = 10;
  }
  double holdoff = 11;
  double delay = 12;
}

message ConfigureTriggerGlitchResponse {
  int32 status = 1;
}

message ConfigureTriggerHysteresisRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double hysteresis = 4;
  oneof slope_enum {
    TriggerSlope slope = 5;
    sint32 slope_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerHysteresisResponse {
  int32 status = 1;
}

message ConfigureTriggerImmediateRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureTriggerImmediateResponse {
  int32 status = 1;
}

message ConfigureTriggerRuntRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double low_threshold = 3;
  double high_threshold = 4;
  oneof polarity_enum {
    RuntPolarity polarity = 5;
    sint32 polarity_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerRuntResponse {
  int32 status = 1;
}

message ConfigureTriggerSoftwareRequest {
  nidevice_grpc.Session vi = 1;
  double holdoff = 2;
  double delay = 3;
}

message ConfigureTriggerSoftwareResponse {
  int32 status = 1;
}

message ConfigureTriggerVideoRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  bool enable_dc_restore = 3;
  oneof signal_format_enum {
    VideoSignalFormat signal_format = 4;
    sint32 signal_format_raw = 5;
  }
  oneof event_enum {
    VideoTriggerEvent event = 6;
    sint32 event_raw = 7;
  }
  sint32 line_number = 8;
  oneof polarity_enum {
    VideoPolarity polarity = 9;
    sint32 polarity_raw = 10;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 11;
    sint32 trigger_coupling_raw = 12;
  }
  double holdoff = 13;
  double delay = 14;
}

message ConfigureTriggerVideoResponse {
  int32 status = 1;
}

message ConfigureTriggerWidthRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double level = 3;
  double low_threshold = 4;
  double high_threshold = 5;
  oneof polarity_enum {
    WidthPolarity polarity = 6;
    sint32 polarity_raw = 7;
  }
  oneof condition_enum {
    WidthCondition condition = 8;
    sint32 condition_raw = 9;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 10;
    sint32 trigger_coupling_raw = 11;
  }
  double holdoff = 12;
  double delay = 13;
}

message ConfigureTriggerWidthResponse {
  int32 status = 1;
}

message ConfigureTriggerWindowRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_source = 2;
  double low_level = 3;
  double high_level = 4;
  oneof window_mode_enum {
    TriggerWindowMode window_mode = 5;
    sint32 window_mode_raw = 6;
  }
  oneof trigger_coupling_enum {
    TriggerCoupling trigger_coupling = 7;
    sint32 trigger_coupling_raw = 8;
  }
  double holdoff = 9;
  double delay = 10;
}

message ConfigureTriggerWindowResponse {
  int32 status = 1;
}

message ConfigureVerticalRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double range = 3;
  double offset = 4;
  oneof coupling_enum {
    VerticalCoupling coupling = 5;
    sint32 coupling_raw = 6;
  }
  double probe_attenuation = 7;
  bool enabled = 8;
}

message ConfigureVerticalResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message ErrorHandlerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
  string error_source = 3;
}

message ErrorHandlerResponse {
  int32 status = 1;
  string error_description = 2;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    ExportableSignals signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  oneof output_terminal_enum {
    ClockingTerminalValues output_terminal_mapped = 5;
    string output_terminal_raw = 6;
  }
}

message ExportSignalResponse {
  int32 status = 1;
}

message FetchRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchResponse {
  int32 status = 1;
  repeated double waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchArrayMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof array_meas_function_enum {
    ArrayMeasurement array_meas_function = 4;
    sint32 array_meas_function_raw = 5;
  }
  optional sint32 meas_wfm_size = 6;
}

message FetchArrayMeasurementResponse {
  int32 status = 1;
  repeated double meas_wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary16Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary16Response {
  int32 status = 1;
  repeated sint32 waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary32Response {
  int32 status = 1;
  repeated sint32 waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchBinary8Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchBinary8Response {
  int32 status = 1;
  bytes waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchComplexRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchComplexResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumber wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchComplexBinary16Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message FetchComplexBinary16Response {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexI16 wfm = 2;
  repeated WaveformInfo wfm_info = 3;
}

message FetchMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message FetchMeasurementResponse {
  int32 status = 1;
  repeated double result = 2;
}

message FetchMeasurementStatsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message FetchMeasurementStatsResponse {
  int32 status = 1;
  repeated double result = 2;
  repeated double mean = 3;
  repeated double stdev = 4;
  repeated double min = 5;
  repeated double max = 6;
  repeated sint32 num_in_stats = 7;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message GetChannelNameFromStringRequest {
  nidevice_grpc.Session vi = 1;
  string index = 2;
}

message GetChannelNameFromStringResponse {
  int32 status = 1;
  string name = 2;
}

message GetEqualizationFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel = 2;
  sint32 number_of_coefficients = 3;
}

message GetEqualizationFilterCoefficientsResponse {
  int32 status = 1;
  repeated double coefficients = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string description = 3;
}

message GetErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message GetErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message GetFrequencyResponseRequest {
  nidevice_grpc.Session vi = 1;
  string channel = 2;
  sint32 buffer_size = 3;
}

message GetFrequencyResponseResponse {
  int32 status = 1;
  repeated double frequencies = 2;
  repeated double amplitudes = 3;
  repeated double phases = 4;
  sint32 number_of_frequencies = 5;
}

message GetNormalizationCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetNormalizationCoefficientsResponse {
  int32 status = 1;
  repeated CoefficientInfo coefficient_info = 2;
  sint32 number_of_coefficient_sets = 3;
}

message GetScalingCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
}

message GetScalingCoefficientsResponse {
  int32 status = 1;
  repeated CoefficientInfo coefficient_info = 2;
  sint32 number_of_coefficient_sets = 3;
}

message GetStreamEndpointHandleRequest {
  nidevice_grpc.Session vi = 1;
  string stream_name = 2;
}

message GetStreamEndpointHandleResponse {
  int32 status = 1;
  uint32 writer_handle = 2;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
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

message InitiateAcquisitionRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateAcquisitionResponse {
  int32 status = 1;
}

message ProbeCompensationSignalStartRequest {
  nidevice_grpc.Session vi = 1;
}

message ProbeCompensationSignalStartResponse {
  int32 status = 1;
}

message ProbeCompensationSignalStopRequest {
  nidevice_grpc.Session vi = 1;
}

message ProbeCompensationSignalStopResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  sint32 num_samples = 4;
}

message ReadResponse {
  int32 status = 1;
  repeated double waveform = 2;
  repeated WaveformInfo wfm_info = 3;
}

message ReadMeasurementRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  double timeout = 3;
  oneof scalar_meas_function_enum {
    ScalarMeasurement scalar_meas_function = 4;
    sint32 scalar_meas_function_raw = 5;
  }
}

message ReadMeasurementResponse {
  int32 status = 1;
  repeated double result = 2;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string driver_revision = 2;
  string firmware_revision = 3;
}

message SampleModeRequest {
  nidevice_grpc.Session vi = 1;
}

message SampleModeResponse {
  int32 status = 1;
  sint32 sample_mode = 2;
}

message SampleRateRequest {
  nidevice_grpc.Session vi = 1;
}

message SampleRateResponse {
  int32 status = 1;
  double sample_rate = 2;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message SendSoftwareTriggerEdgeRequest {
  nidevice_grpc.Session vi = 1;
  oneof which_trigger_enum {
    WhichTrigger which_trigger = 2;
    sint32 which_trigger_raw = 3;
  }
}

message SendSoftwareTriggerEdgeResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  bool value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    sint32 value_raw = 4;
    NiScopeInt32AttributeValues value = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  int64 value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    double value_raw = 4;
    NiScopeReal64AttributeValues value = 5;
    NiScopeReal64AttributeValuesMapped value_mapped = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_list = 2;
  NiScopeAttribute attribute_id = 3;
  oneof value_enum {
    NiScopeStringAttributeValuesMapped value_mapped = 4;
    string value_raw = 5;
  }
}

message SetAttributeViStringResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope/README.md sha256=eacf5d96d736b3e455d5747f8cd7dcf82da89b108461f86256bd4c63d12ed2ef bytes=210 -->
## FILE: source/codegen/metadata/niscope/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope/README.md`
- sha256: `eacf5d96d736b3e455d5747f8cd7dcf82da89b108461f86256bd4c63d12ed2ef`
- bytes: 210

````markdown
# Updating

To update this metadata folder. Find the niscope_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/niscope_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/__init__.py`
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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/niscope_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/attributes_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/niscope_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/attributes_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/config.py sha256=a2b775317065336cf3b5fc000fefae7e448880cdb7d0925390896fc59fabb28f bytes=1765 -->
## FILE: source/codegen/metadata/niscope_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/config.py`
- sha256: `a2b775317065336cf3b5fc000fefae7e448880cdb7d0925390896fc59fabb28f`
- bytes: 1765

````python
# -*- coding: utf-8 -*-
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    "code_readiness": "Release",
    "is_restricted": True,
    "api_version": "25.8.0",
    "c_header": "niScopeCal.h",
    "c_function_prefix": "niScope_",
    "service_class_prefix": "NiScopeRestricted",
    "java_package": "com.ni.grpc.scoperestricted",
    "csharp_namespace": "NationalInstruments.Grpc.NiScopeRestricted",
    "namespace_component": "niscope_restricted",
    'close_function': None,
    "custom_types": [],
    "type_to_grpc_type": {
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
    },
    "driver_name": "NI-SCOPE-RESTRICTED",
    "status_ok": "status >= 0",
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niscope',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niScope_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niScope_64.dll',
                'type': 'cdll'
            }
        }
    },
    "linux_rt_support": True,
    "module_name": "niscope_restricted",
    'session_handle_parameter_name': 'vi',
    "duplicate_resource_handles_allowed": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/config_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/niscope_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/config_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/enums.py sha256=b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc bytes=14 -->
## FILE: source/codegen/metadata/niscope_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/enums.py`
- sha256: `b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc`
- bytes: 14

````python
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/enums_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/niscope_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/enums_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/functions.py sha256=cb53cdadd59fd05ac6c8d77a2913c5bf13e7a41c8c00a0f86750fdc2c52a1328 bytes=8367 -->
## FILE: source/codegen/metadata/niscope_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/functions.py`
- sha256: `cb53cdadd59fd05ac6c8d77a2913c5bf13e7a41c8c00a0f86750fdc2c52a1328`
- bytes: 8367

````python
functions = {
    'GetError': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetErrorMessage': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStartTimestampInformation': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sysTimeIn128BitsT1',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t1',
                'grpc_type': 'uint32',
                'name': 'sysTimeIn128BitsT1',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sysTimeIn128BitsT2',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t2',
                'grpc_type': 'uint32',
                'name': 'sysTimeIn128BitsT2',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sysTimeIn128BitsT3',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t3',
                'grpc_type': 'uint32',
                'name': 'sysTimeIn128BitsT3',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sysTimeIn128BitsT4',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t4',
                'grpc_type': 'uint32',
                'name': 'sysTimeIn128BitsT4',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'deviceTimeInAbsoluteTimeUnits',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'deviceTimeInAbsoluteTimeUnits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStartTimestampInformationWithChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfChannels',
                'direction': 'in',
                'grpc_type': 'uint32',
                'is_size_param': True,
                'name': 'numberOfChannels',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sysTimeIn128BitsT1Array',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t1_array',
                'grpc_type': 'repeated uint32',
                'name': 'sysTimeIn128BitsT1Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfChannels'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'sysTimeIn128BitsT2Array',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t2_array',
                'grpc_type': 'repeated uint32',
                'name': 'sysTimeIn128BitsT2Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfChannels'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'sysTimeIn128BitsT3Array',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t3_array',
                'grpc_type': 'repeated uint32',
                'name': 'sysTimeIn128BitsT3Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfChannels'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'sysTimeIn128BitsT4Array',
                'direction': 'out',
                'grpc_name': 'sys_time_in_128_bits_t4_array',
                'grpc_type': 'repeated uint32',
                'name': 'sysTimeIn128BitsT4Array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfChannels'
                },
                'type': 'ViUInt32[]'
            },
            {
                'cppName': 'deviceTimeInAbsoluteTimeUnitsArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'deviceTimeInAbsoluteTimeUnitsArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfChannels'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseNumberOfChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numChannels',
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'numChannels',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niscope_restricted/functions_addon.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/niscope_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niscope_restricted/functions_addon.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/__init__.py sha256=3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a bytes=589 -->
## FILE: source/codegen/metadata/niswitch/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/__init__.py`
- sha256: `3f3177b9bfb8b1928720894e2452fe8decbd6707df63967cc881e20a7f8fb45a`
- bytes: 589

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/attributes.py sha256=44587399bb9439735c84a5757b169dc5053f452b9a5215f2fbba8f10cbfb636e bytes=12553 -->
## FILE: source/codegen/metadata/niswitch/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/attributes.py`
- sha256: `44587399bb9439735c84a5757b169dc5053f452b9a5215f2fbba8f10cbfb636e`
- bytes: 12553

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0f167
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': False,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SERIAL_NUMBER_I32',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_WAITING_FOR_TRIG',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150005: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150006: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MASTER_SLAVE_TRIGGER_BUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150007: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MASTER_SLAVE_SCAN_ADVANCED_BUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150008: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CABLED_MODULE_TRIGGER_BUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150009: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CABLED_MODULE_SCAN_ADVANCED_BUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150010: {
        'codegen_method': 'public',
        'enum': 'TriggerInputPolarity',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_INPUT_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150011: {
        'codegen_method': 'public',
        'enum': 'ScanAdvancedPolarity',
        'grpc_type': 'sint32',
        'name': 'SCAN_ADVANCED_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150012: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'PARSED_SCAN_LIST',
        'resettable': False,
        'type': 'ViString'
    },
    1150013: {
        'codegen_method': 'public',
        'enum': 'HandshakingInitiation',
        'grpc_type': 'sint32',
        'name': 'HANDSHAKING_INITIATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150014: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'NUMBER_OF_RELAYS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150015: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150016: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DIGITAL_FILTER_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150017: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150018: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'ANALOG_BUS_SHARING_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150019: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TEMPERATURE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_SOURCE_CHANNEL',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_DEBOUNCED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_CONFIGURATION_CHANNEL',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250004: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SETTLING_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250005: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'BANDWIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250006: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_DC_VOLTAGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250007: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_AC_VOLTAGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250008: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_SWITCHING_DC_CURRENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250009: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_SWITCHING_AC_CURRENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250010: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_CARRY_DC_CURRENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250011: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_CARRY_AC_CURRENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250012: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_SWITCHING_DC_POWER',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250013: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_SWITCHING_AC_POWER',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250014: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_CARRY_DC_POWER',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250015: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_CARRY_AC_POWER',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250016: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CHARACTERISTIC_IMPEDANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250017: {
        'codegen_method': 'public',
        'enum': 'WireMode',
        'grpc_type': 'sint32',
        'name': 'WIRE_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250018: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'NUM_OF_ROWS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250019: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'NUM_OF_COLUMNS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250020: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SCAN_LIST',
        'resettable': False,
        'type': 'ViString'
    },
    1250021: {
        'codegen_method': 'public',
        'enum': 'ScanMode',
        'grpc_type': 'sint32',
        'name': 'SCAN_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250022: {
        'codegen_method': 'public',
        'enum': 'TriggerInput',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_INPUT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250023: {
        'codegen_method': 'public',
        'enum': 'ScanAdvancedOutput',
        'grpc_type': 'sint32',
        'name': 'SCAN_ADVANCED_OUTPUT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250024: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'IS_SCANNING',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250025: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SCAN_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250026: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CONTINUOUS_SCAN',
        'resettable': False,
        'type': 'ViBoolean'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/niswitch/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/config.py sha256=f4eb9538f71b06b0c2d45572f42edfc91d1a72e0c04520efe9d41f910311e4c6 bytes=1184 -->
## FILE: source/codegen/metadata/niswitch/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/config.py`
- sha256: `f4eb9538f71b06b0c2d45572f42edfc91d1a72e0c04520efe9d41f910311e4c6`
- bytes: 1184

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0f167
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '23.0.0f167',
    'c_function_prefix': 'niSwitch_',
    'c_header': 'niswitch.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Switch',
    'custom_types': [
    ],
    'driver_name': 'NI-SWITCH',
    'java_package': 'com.ni.grpc.niswitch',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niswitch',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niswitch_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niswitch_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'niswitch',
    'namespace_component': 'niswitch',
    'service_class_prefix': 'NiSwitch',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/config_addon.py sha256=d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58 bytes=226 -->
## FILE: source/codegen/metadata/niswitch/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/config_addon.py`
- sha256: `d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/custom_proto.mako sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/niswitch/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/custom_proto.mako`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````mako

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/enums.py sha256=854927f5449391badd647800860633175bba0ece964386adb0bffe09e0fa7e0d bytes=23838 -->
## FILE: source/codegen/metadata/niswitch/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/enums.py`
- sha256: `854927f5449391badd647800860633175bba0ece964386adb0bffe09e0fa7e0d`
- bytes: 23838

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0f167
enums = {
    'HandshakingInitiation': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_SWITCH_INITIATED',
                'value': 1
            }
        ]
    },
    'NiSwitchInt32AttributeValues': {
        'enum-value-prefix': 'NISWITCH_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'HANDSHAKING_INITIATION_VAL_MEASUREMENT_DEVICE_INITIATED',
                'value': 0
            },
            {
                'name': 'HANDSHAKING_INITIATION_VAL_SWITCH_INITIATED',
                'value': 1
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_NONE',
                'value': 0
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_TTL7',
                'value': 118
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_PXI_STAR',
                'value': 125
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'name': 'SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            },
            {
                'name': 'SCAN_ADVANCED_POLARITY_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'name': 'SCAN_ADVANCED_POLARITY_VAL_FALLING_EDGE',
                'value': 1
            },
            {
                'name': 'SCAN_MODE_VAL_NONE',
                'value': 0
            },
            {
                'name': 'SCAN_MODE_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'name': 'SCAN_MODE_VAL_BREAK_AFTER_MAKE',
                'value': 2
            },
            {
                'name': 'TRIGGER_INPUT_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'TRIGGER_INPUT_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'TRIGGER_INPUT_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'TRIGGER_INPUT_VAL_TTL7',
                'value': 118
            },
            {
                'name': 'TRIGGER_INPUT_VAL_PXI_STAR',
                'value': 125
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'name': 'TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'name': 'TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            },
            {
                'name': 'TRIGGER_INPUT_POLARITY_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'name': 'TRIGGER_INPUT_POLARITY_VAL_FALLING_EDGE',
                'value': 1
            },
            {
                'name': 'WIRE_MODE_VAL_1_WIRE',
                'value': 1
            },
            {
                'name': 'WIRE_MODE_VAL_2_WIRE',
                'value': 2
            },
            {
                'name': 'WIRE_MODE_VAL_4_WIRE',
                'value': 4
            }
        ]
    },
    'PathCapability': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_PATH_AVAILABLE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_PATH_EXISTS',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_PATH_UNSUPPORTED',
                'value': 3
            },
            {
                'name': 'NISWITCH_VAL_RESOURCE_IN_USE',
                'value': 4
            },
            {
                'name': 'NISWITCH_VAL_SOURCE_CONFLICT',
                'value': 5
            },
            {
                'name': 'NISWITCH_VAL_CHANNEL_NOT_AVAILABLE',
                'value': 6
            }
        ]
    },
    'RelayAction': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_OPEN_RELAY',
                'value': 20
            },
            {
                'name': 'NISWITCH_VAL_CLOSE_RELAY',
                'value': 21
            }
        ]
    },
    'RelayPosition': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_OPEN',
                'value': 10
            },
            {
                'name': 'NISWITCH_VAL_CLOSED',
                'value': 11
            }
        ]
    },
    'ScanAdvancedOutput': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'ScanAdvancedPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'ScanMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_BREAK_AFTER_MAKE',
                'value': 2
            }
        ]
    },
    'TriggerInput': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'TriggerInputPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'WireMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NISWITCH_VAL_1_WIRE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_2_WIRE',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_4_WIRE',
                'value': 4
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/niswitch/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/functions.py sha256=852d1825bc20125ad0815f9f921edf8797643d287f9613fbbf33151aba67ccce bytes=55799 -->
## FILE: source/codegen/metadata/niswitch/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/functions.py`
- sha256: `852d1825bc20125ad0815f9f921edf8797643d287f9613fbbf33151aba67ccce`
- bytes: 55799

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0f167
functions = {
    'AbortScan': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CanConnect': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'channel2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'cppName': 'pathCapability',
                'direction': 'out',
                'enum': 'PathCapability',
                'grpc_type': 'sint32',
                'name': 'pathCapability',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiSwitchInt32AttributeValues',
                'grpc_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'attribute_value_raw',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niSwitch_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureScanList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'scanlist',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'scanlist',
                'type': 'ViConstString'
            },
            {
                'cppName': 'scanMode',
                'direction': 'in',
                'enum': 'ScanMode',
                'grpc_type': 'sint32',
                'name': 'scanMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureScanTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'scanDelay',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'scanDelay',
                'type': 'ViReal64'
            },
            {
                'cppName': 'triggerInput',
                'direction': 'in',
                'enum': 'TriggerInput',
                'grpc_type': 'sint32',
                'name': 'triggerInput',
                'type': 'ViInt32'
            },
            {
                'cppName': 'scanAdvancedOutput',
                'direction': 'in',
                'enum': 'ScanAdvancedOutput',
                'grpc_type': 'sint32',
                'name': 'scanAdvancedOutput',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Connect': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'channel2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectMultiple': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'connectionList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'connectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disconnect': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'channel2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectAll': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectMultiple': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'disconnectionList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'disconnectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niSwitch_error_message',
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorQuery': {
        'cname': 'niSwitch_error_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'string',
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
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelNameBuffer',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'channelNameBuffer',
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
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'code',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'code',
                'type': 'ViStatus'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'description',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coercionRecord',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'coercionRecord',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'interchangeWarning',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'interchangeWarning',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPath': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channel1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'channel2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'path',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'path',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayCount': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'relayName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'relayCount',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'relayCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'relayNameBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'relayNameBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'relayNameBuffer',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'relayNameBuffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'relayNameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayPosition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'relayName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'relayPosition',
                'direction': 'out',
                'enum': 'RelayPosition',
                'grpc_type': 'sint32',
                'name': 'relayPosition',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niSwitch_init',
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
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
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionsString',
                'direction': 'in',
                'grpc_name': 'option_string',
                'grpc_type': 'string',
                'name': 'optionsString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
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
    'InitWithTopology': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'topology',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'topology',
                'type': 'ViConstString'
            },
            {
                'cppName': 'simulate',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'simulate',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
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
    'InitiateScan': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDebounced': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'isDebounced',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isDebounced',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsScanning': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'isScanning',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isScanning',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'RelayControl': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'relayName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'relayAction',
                'direction': 'in',
                'enum': 'RelayAction',
                'grpc_type': 'sint32',
                'name': 'relayAction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niSwitch_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niSwitch_revision_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'instrumentDriverRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'firmwareRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteScanAdvancedOutput': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'scanAdvancedOutputConnector',
                'direction': 'in',
                'enum': 'ScanAdvancedOutput',
                'grpc_type': 'sint32',
                'name': 'scanAdvancedOutputConnector',
                'type': 'ViInt32'
            },
            {
                'cppName': 'scanAdvancedOutputBusLine',
                'direction': 'in',
                'enum': 'ScanAdvancedOutput',
                'grpc_type': 'sint32',
                'name': 'scanAdvancedOutputBusLine',
                'type': 'ViInt32'
            },
            {
                'cppName': 'invert',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteTriggerInput': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerInputConnector',
                'direction': 'in',
                'enum': 'TriggerInput',
                'grpc_type': 'sint32',
                'name': 'triggerInputConnector',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerInputBusLine',
                'direction': 'in',
                'enum': 'TriggerInput',
                'grpc_type': 'sint32',
                'name': 'triggerInputBusLine',
                'type': 'ViInt32'
            },
            {
                'cppName': 'invert',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Scan': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'scanlist',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'scanlist',
                'type': 'ViConstString'
            },
            {
                'cppName': 'initiation',
                'direction': 'in',
                'enum': 'HandshakingInitiation',
                'grpc_type': 'sint32',
                'name': 'initiation',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niSwitch_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiSwitchInt32AttributeValues',
                'grpc_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'attribute_value_raw',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiSwitchAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'attribute_value_raw',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetContinuousScan': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'continuousScan',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'continuousScan',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetPath': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'pathList',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'pathList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForDebounce': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTimeMs',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'maximumTimeMs',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForScanComplete': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumTimeMs',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'maximumTimeMs',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/functions_addon.py sha256=509cdb9ccc9aa05529c706d6ca32bf420ee698835bf29cf7fb30bb80c58a3144 bytes=1318 -->
## FILE: source/codegen/metadata/niswitch/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/functions_addon.py`
- sha256: `509cdb9ccc9aa05529c706d6ca32bf420ee698835bf29cf7fb30bb80c58a3144`
- bytes: 1318

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/niswitch.proto sha256=dcc380d8acddb13e8080c6d2c7d97c62f0259d3d4b22590737289329c8367944 bytes=33103 -->
## FILE: source/codegen/metadata/niswitch/niswitch.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/niswitch.proto`
- sha256: `dcc380d8acddb13e8080c6d2c7d97c62f0259d3d4b22590737289329c8367944`
- bytes: 33103

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-SWITCH API metadata version 23.0.0f167
//---------------------------------------------------------------------
// Proto file for the NI-SWITCH Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.niswitch";
option java_outer_classname = "NiSwitch";
option csharp_namespace = "NationalInstruments.Grpc.Switch";

package niswitch_grpc;

import "session.proto";

service NiSwitch {
  rpc AbortScan(AbortScanRequest) returns (AbortScanResponse);
  rpc CanConnect(CanConnectRequest) returns (CanConnectResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ConfigureScanList(ConfigureScanListRequest) returns (ConfigureScanListResponse);
  rpc ConfigureScanTrigger(ConfigureScanTriggerRequest) returns (ConfigureScanTriggerResponse);
  rpc Connect(ConnectRequest) returns (ConnectResponse);
  rpc ConnectMultiple(ConnectMultipleRequest) returns (ConnectMultipleResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc Disconnect(DisconnectRequest) returns (DisconnectResponse);
  rpc DisconnectAll(DisconnectAllRequest) returns (DisconnectAllResponse);
  rpc DisconnectMultiple(DisconnectMultipleRequest) returns (DisconnectMultipleResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetNextCoercionRecord(GetNextCoercionRecordRequest) returns (GetNextCoercionRecordResponse);
  rpc GetNextInterchangeWarning(GetNextInterchangeWarningRequest) returns (GetNextInterchangeWarningResponse);
  rpc GetPath(GetPathRequest) returns (GetPathResponse);
  rpc GetRelayCount(GetRelayCountRequest) returns (GetRelayCountResponse);
  rpc GetRelayName(GetRelayNameRequest) returns (GetRelayNameResponse);
  rpc GetRelayPosition(GetRelayPositionRequest) returns (GetRelayPositionResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitWithTopology(InitWithTopologyRequest) returns (InitWithTopologyResponse);
  rpc InitiateScan(InitiateScanRequest) returns (InitiateScanResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc IsDebounced(IsDebouncedRequest) returns (IsDebouncedResponse);
  rpc IsScanning(IsScanningRequest) returns (IsScanningResponse);
  rpc RelayControl(RelayControlRequest) returns (RelayControlResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc RouteScanAdvancedOutput(RouteScanAdvancedOutputRequest) returns (RouteScanAdvancedOutputResponse);
  rpc RouteTriggerInput(RouteTriggerInputRequest) returns (RouteTriggerInputResponse);
  rpc Scan(ScanRequest) returns (ScanResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareTrigger(SendSoftwareTriggerRequest) returns (SendSoftwareTriggerResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetContinuousScan(SetContinuousScanRequest) returns (SetContinuousScanResponse);
  rpc SetPath(SetPathRequest) returns (SetPathResponse);
  rpc WaitForDebounce(WaitForDebounceRequest) returns (WaitForDebounceResponse);
  rpc WaitForScanComplete(WaitForScanCompleteRequest) returns (WaitForScanCompleteResponse);
}

enum NiSwitchAttribute {
  NISWITCH_ATTRIBUTE_UNSPECIFIED = 0;
  NISWITCH_ATTRIBUTE_RANGE_CHECK = 1050002;
  NISWITCH_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NISWITCH_ATTRIBUTE_CACHE = 1050004;
  NISWITCH_ATTRIBUTE_SIMULATE = 1050005;
  NISWITCH_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NISWITCH_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NISWITCH_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NISWITCH_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NISWITCH_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NISWITCH_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NISWITCH_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NISWITCH_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NISWITCH_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NISWITCH_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NISWITCH_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NISWITCH_ATTRIBUTE_SERIAL_NUMBER_I32 = 1150001;
  NISWITCH_ATTRIBUTE_IS_WAITING_FOR_TRIG = 1150004;
  NISWITCH_ATTRIBUTE_TRIGGER_MODE = 1150005;
  NISWITCH_ATTRIBUTE_MASTER_SLAVE_TRIGGER_BUS = 1150006;
  NISWITCH_ATTRIBUTE_MASTER_SLAVE_SCAN_ADVANCED_BUS = 1150007;
  NISWITCH_ATTRIBUTE_CABLED_MODULE_TRIGGER_BUS = 1150008;
  NISWITCH_ATTRIBUTE_CABLED_MODULE_SCAN_ADVANCED_BUS = 1150009;
  NISWITCH_ATTRIBUTE_TRIGGER_INPUT_POLARITY = 1150010;
  NISWITCH_ATTRIBUTE_SCAN_ADVANCED_POLARITY = 1150011;
  NISWITCH_ATTRIBUTE_PARSED_SCAN_LIST = 1150012;
  NISWITCH_ATTRIBUTE_HANDSHAKING_INITIATION = 1150013;
  NISWITCH_ATTRIBUTE_NUMBER_OF_RELAYS = 1150014;
  NISWITCH_ATTRIBUTE_SERIAL_NUMBER = 1150015;
  NISWITCH_ATTRIBUTE_DIGITAL_FILTER_ENABLE = 1150016;
  NISWITCH_ATTRIBUTE_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE = 1150017;
  NISWITCH_ATTRIBUTE_ANALOG_BUS_SHARING_ENABLE = 1150018;
  NISWITCH_ATTRIBUTE_TEMPERATURE = 1150019;
  NISWITCH_ATTRIBUTE_IS_SOURCE_CHANNEL = 1250001;
  NISWITCH_ATTRIBUTE_IS_DEBOUNCED = 1250002;
  NISWITCH_ATTRIBUTE_IS_CONFIGURATION_CHANNEL = 1250003;
  NISWITCH_ATTRIBUTE_SETTLING_TIME = 1250004;
  NISWITCH_ATTRIBUTE_BANDWIDTH = 1250005;
  NISWITCH_ATTRIBUTE_MAX_DC_VOLTAGE = 1250006;
  NISWITCH_ATTRIBUTE_MAX_AC_VOLTAGE = 1250007;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_CURRENT = 1250008;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_CURRENT = 1250009;
  NISWITCH_ATTRIBUTE_MAX_CARRY_DC_CURRENT = 1250010;
  NISWITCH_ATTRIBUTE_MAX_CARRY_AC_CURRENT = 1250011;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_POWER = 1250012;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_POWER = 1250013;
  NISWITCH_ATTRIBUTE_MAX_CARRY_DC_POWER = 1250014;
  NISWITCH_ATTRIBUTE_MAX_CARRY_AC_POWER = 1250015;
  NISWITCH_ATTRIBUTE_CHARACTERISTIC_IMPEDANCE = 1250016;
  NISWITCH_ATTRIBUTE_WIRE_MODE = 1250017;
  NISWITCH_ATTRIBUTE_NUM_OF_ROWS = 1250018;
  NISWITCH_ATTRIBUTE_NUM_OF_COLUMNS = 1250019;
  NISWITCH_ATTRIBUTE_SCAN_LIST = 1250020;
  NISWITCH_ATTRIBUTE_SCAN_MODE = 1250021;
  NISWITCH_ATTRIBUTE_TRIGGER_INPUT = 1250022;
  NISWITCH_ATTRIBUTE_SCAN_ADVANCED_OUTPUT = 1250023;
  NISWITCH_ATTRIBUTE_IS_SCANNING = 1250024;
  NISWITCH_ATTRIBUTE_SCAN_DELAY = 1250025;
  NISWITCH_ATTRIBUTE_CONTINUOUS_SCAN = 1250026;
}

enum HandshakingInitiation {
  HANDSHAKING_INITIATION_NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED = 0;
  HANDSHAKING_INITIATION_NISWITCH_VAL_SWITCH_INITIATED = 1;
}

enum NiSwitchInt32AttributeValues {
  option allow_alias = true;
  NISWITCH_INT32_UNSPECIFIED = 0;
  NISWITCH_INT32_HANDSHAKING_INITIATION_VAL_MEASUREMENT_DEVICE_INITIATED = 0;
  NISWITCH_INT32_HANDSHAKING_INITIATION_VAL_SWITCH_INITIATED = 1;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_NONE = 0;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_EXTERNAL = 2;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL0 = 111;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL1 = 112;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL2 = 113;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL3 = 114;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL4 = 115;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL5 = 116;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL6 = 117;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL7 = 118;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_PXI_STAR = 125;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR = 1000;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR = 1001;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE1 = 1021;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE2 = 1022;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE3 = 1023;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE4 = 1024;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE5 = 1025;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE6 = 1026;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE7 = 1027;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE8 = 1028;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE9 = 1029;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE10 = 1030;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE11 = 1031;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE12 = 1032;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE12 = 1052;
  NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_RISING_EDGE = 0;
  NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_FALLING_EDGE = 1;
  NISWITCH_INT32_SCAN_MODE_VAL_NONE = 0;
  NISWITCH_INT32_SCAN_MODE_VAL_BREAK_BEFORE_MAKE = 1;
  NISWITCH_INT32_SCAN_MODE_VAL_BREAK_AFTER_MAKE = 2;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_IMMEDIATE = 1;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_EXTERNAL = 2;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_SOFTWARE_TRIG = 3;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL0 = 111;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL1 = 112;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL2 = 113;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL3 = 114;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL4 = 115;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL5 = 116;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL6 = 117;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL7 = 118;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_PXI_STAR = 125;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR = 1000;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR = 1001;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE1 = 1021;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE2 = 1022;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE3 = 1023;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE4 = 1024;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE5 = 1025;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE6 = 1026;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE7 = 1027;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE8 = 1028;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE9 = 1029;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE10 = 1030;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE11 = 1031;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE12 = 1032;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE12 = 1052;
  NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_RISING_EDGE = 0;
  NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_FALLING_EDGE = 1;
  NISWITCH_INT32_WIRE_MODE_VAL_1_WIRE = 1;
  NISWITCH_INT32_WIRE_MODE_VAL_2_WIRE = 2;
  NISWITCH_INT32_WIRE_MODE_VAL_4_WIRE = 4;
}

enum PathCapability {
  PATH_CAPABILITY_UNSPECIFIED = 0;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_AVAILABLE = 1;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_EXISTS = 2;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_UNSUPPORTED = 3;
  PATH_CAPABILITY_NISWITCH_VAL_RESOURCE_IN_USE = 4;
  PATH_CAPABILITY_NISWITCH_VAL_SOURCE_CONFLICT = 5;
  PATH_CAPABILITY_NISWITCH_VAL_CHANNEL_NOT_AVAILABLE = 6;
}

enum RelayAction {
  RELAY_ACTION_UNSPECIFIED = 0;
  RELAY_ACTION_NISWITCH_VAL_OPEN_RELAY = 20;
  RELAY_ACTION_NISWITCH_VAL_CLOSE_RELAY = 21;
}

enum RelayPosition {
  RELAY_POSITION_UNSPECIFIED = 0;
  RELAY_POSITION_NISWITCH_VAL_OPEN = 10;
  RELAY_POSITION_NISWITCH_VAL_CLOSED = 11;
}

enum ScanAdvancedOutput {
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_NONE = 0;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_EXTERNAL = 2;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL0 = 111;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL1 = 112;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL2 = 113;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL3 = 114;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL4 = 115;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL5 = 116;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL6 = 117;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL7 = 118;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_PXI_STAR = 125;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR = 1000;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR = 1001;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1 = 1021;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2 = 1022;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3 = 1023;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4 = 1024;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5 = 1025;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6 = 1026;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7 = 1027;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8 = 1028;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9 = 1029;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10 = 1030;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11 = 1031;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12 = 1032;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12 = 1052;
}

enum ScanMode {
  SCAN_MODE_NISWITCH_VAL_NONE = 0;
  SCAN_MODE_NISWITCH_VAL_BREAK_BEFORE_MAKE = 1;
  SCAN_MODE_NISWITCH_VAL_BREAK_AFTER_MAKE = 2;
}

enum TriggerInput {
  TRIGGER_INPUT_UNSPECIFIED = 0;
  TRIGGER_INPUT_NISWITCH_VAL_IMMEDIATE = 1;
  TRIGGER_INPUT_NISWITCH_VAL_EXTERNAL = 2;
  TRIGGER_INPUT_NISWITCH_VAL_SOFTWARE_TRIG = 3;
  TRIGGER_INPUT_NISWITCH_VAL_TTL0 = 111;
  TRIGGER_INPUT_NISWITCH_VAL_TTL1 = 112;
  TRIGGER_INPUT_NISWITCH_VAL_TTL2 = 113;
  TRIGGER_INPUT_NISWITCH_VAL_TTL3 = 114;
  TRIGGER_INPUT_NISWITCH_VAL_TTL4 = 115;
  TRIGGER_INPUT_NISWITCH_VAL_TTL5 = 116;
  TRIGGER_INPUT_NISWITCH_VAL_TTL6 = 117;
  TRIGGER_INPUT_NISWITCH_VAL_TTL7 = 118;
  TRIGGER_INPUT_NISWITCH_VAL_PXI_STAR = 125;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR = 1000;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR = 1001;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1 = 1021;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2 = 1022;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3 = 1023;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4 = 1024;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5 = 1025;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6 = 1026;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7 = 1027;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8 = 1028;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9 = 1029;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10 = 1030;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11 = 1031;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12 = 1032;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12 = 1052;
}

message AbortScanRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortScanResponse {
  int32 status = 1;
}

message CanConnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message CanConnectResponse {
  int32 status = 1;
  PathCapability path_capability = 2;
  sint32 path_capability_raw = 3;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  oneof attribute_value_enum {
    sint32 attribute_value_raw = 4;
    NiSwitchInt32AttributeValues attribute_value = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  double attribute_value_raw = 4;
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ConfigureScanListRequest {
  nidevice_grpc.Session vi = 1;
  string scanlist = 2;
  oneof scan_mode_enum {
    ScanMode scan_mode = 3;
    sint32 scan_mode_raw = 4;
  }
}

message ConfigureScanListResponse {
  int32 status = 1;
}

message ConfigureScanTriggerRequest {
  nidevice_grpc.Session vi = 1;
  double scan_delay = 2;
  oneof trigger_input_enum {
    TriggerInput trigger_input = 3;
    sint32 trigger_input_raw = 4;
  }
  oneof scan_advanced_output_enum {
    ScanAdvancedOutput scan_advanced_output = 5;
    sint32 scan_advanced_output_raw = 6;
  }
}

message ConfigureScanTriggerResponse {
  int32 status = 1;
}

message ConnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message ConnectResponse {
  int32 status = 1;
}

message ConnectMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string connection_list = 2;
}

message ConnectMultipleResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message DisconnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message DisconnectResponse {
  int32 status = 1;
}

message DisconnectAllRequest {
  nidevice_grpc.Session vi = 1;
}

message DisconnectAllResponse {
  int32 status = 1;
}

message DisconnectMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string disconnection_list = 2;
}

message DisconnectMultipleResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_name_buffer = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 code = 2;
  string description = 3;
}

message GetNextCoercionRecordRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextCoercionRecordResponse {
  int32 status = 1;
  string coercion_record = 2;
}

message GetNextInterchangeWarningRequest {
  nidevice_grpc.Session vi = 1;
}

message GetNextInterchangeWarningResponse {
  int32 status = 1;
  string interchange_warning = 2;
}

message GetPathRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message GetPathResponse {
  int32 status = 1;
  string path = 2;
}

message GetRelayCountRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
}

message GetRelayCountResponse {
  int32 status = 1;
  sint32 relay_count = 2;
}

message GetRelayNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetRelayNameResponse {
  int32 status = 1;
  string relay_name_buffer = 2;
}

message GetRelayPositionRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
}

message GetRelayPositionResponse {
  int32 status = 1;
  RelayPosition relay_position = 2;
  sint32 relay_position_raw = 3;
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

message InitWithTopologyRequest {
  string session_name = 1;
  string resource_name = 2;
  string topology = 3;
  bool simulate = 4;
  bool reset_device = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithTopologyResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateScanRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateScanResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}

message IsDebouncedRequest {
  nidevice_grpc.Session vi = 1;
}

message IsDebouncedResponse {
  int32 status = 1;
  bool is_debounced = 2;
}

message IsScanningRequest {
  nidevice_grpc.Session vi = 1;
}

message IsScanningResponse {
  int32 status = 1;
  bool is_scanning = 2;
}

message RelayControlRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
  oneof relay_action_enum {
    RelayAction relay_action = 3;
    sint32 relay_action_raw = 4;
  }
}

message RelayControlResponse {
  int32 status = 1;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message RouteScanAdvancedOutputRequest {
  nidevice_grpc.Session vi = 1;
  oneof scan_advanced_output_connector_enum {
    ScanAdvancedOutput scan_advanced_output_connector = 2;
    sint32 scan_advanced_output_connector_raw = 3;
  }
  oneof scan_advanced_output_bus_line_enum {
    ScanAdvancedOutput scan_advanced_output_bus_line = 4;
    sint32 scan_advanced_output_bus_line_raw = 5;
  }
  bool invert = 6;
}

message RouteScanAdvancedOutputResponse {
  int32 status = 1;
}

message RouteTriggerInputRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_input_connector_enum {
    TriggerInput trigger_input_connector = 2;
    sint32 trigger_input_connector_raw = 3;
  }
  oneof trigger_input_bus_line_enum {
    TriggerInput trigger_input_bus_line = 4;
    sint32 trigger_input_bus_line_raw = 5;
  }
  bool invert = 6;
}

message RouteTriggerInputResponse {
  int32 status = 1;
}

message ScanRequest {
  nidevice_grpc.Session vi = 1;
  string scanlist = 2;
  oneof initiation_enum {
    HandshakingInitiation initiation = 3;
    sint32 initiation_raw = 4;
  }
}

message ScanResponse {
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

message SendSoftwareTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message SendSoftwareTriggerResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  oneof attribute_value_enum {
    sint32 attribute_value_raw = 4;
    NiSwitchInt32AttributeValues attribute_value = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  double attribute_value_raw = 4;
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetContinuousScanRequest {
  nidevice_grpc.Session vi = 1;
  bool continuous_scan = 2;
}

message SetContinuousScanResponse {
  int32 status = 1;
}

message SetPathRequest {
  nidevice_grpc.Session vi = 1;
  string path_list = 2;
}

message SetPathResponse {
  int32 status = 1;
}

message WaitForDebounceRequest {
  nidevice_grpc.Session vi = 1;
  sint32 maximum_time_ms = 2;
}

message WaitForDebounceResponse {
  int32 status = 1;
}

message WaitForScanCompleteRequest {
  nidevice_grpc.Session vi = 1;
  sint32 maximum_time_ms = 2;
}

message WaitForScanCompleteResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/niswitch/README.md sha256=b3cb9ec5fbb974c6af7f6218bec8a2670d3da7394ebb6eaaf5503364b918d7df bytes=211 -->
## FILE: source/codegen/metadata/niswitch/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/niswitch/README.md`
- sha256: `b3cb9ec5fbb974c6af7f6218bec8a2670d3da7394ebb6eaaf5503364b918d7df`
- bytes: 211

````markdown
# Updating

To update this metadata folder. Find the niswitch_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/__init__.py sha256=bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5 bytes=248 -->
## FILE: source/codegen/metadata/nisync/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/__init__.py`
- sha256: `bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5`
- bytes: 248

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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/attributes.py sha256=4de9c9edaa7bf35514b146cc4449bfd90c3e4f5b104c56ac80d71c2f40981646 bytes=6900 -->
## FILE: source/codegen/metadata/nisync/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/attributes.py`
- sha256: `4de9c9edaa7bf35514b146cc4449bfd90c3e4f5b104c56ac80d71c2f40981646`
- bytes: 6900

````python
# -*- coding: utf-8 -*-
attributes = {
    1150000: {
        'name': 'INTF_NUM'
    },
    1150001: {
        'name': 'SERIAL_NUM'
    },
    1150002: {
        'name': 'MODEL_CODE'
    },
    1150100: {
        'name': 'PFI0_THRESHOLD'
    },
    1150101: {
        'name': 'PFI1_THRESHOLD'
    },
    1150102: {
        'name': 'PFI2_THRESHOLD'
    },
    1150103: {
        'name': 'PFI3_THRESHOLD'
    },
    1150104: {
        'name': 'PFI4_THRESHOLD'
    },
    1150105: {
        'name': 'PFI5_THRESHOLD'
    },
    1150106: {
        'name': 'OSCILLATOR_VOLTAGE'
    },
    1150107: {
        'name': 'CLK10_PHASE_ADJUST'
    },
    1150108: {
        'name': 'DDS_VCXO_VOLTAGE'
    },
    1150109: {
        'name': 'DDS_PHASE_ADJUST'
    },
    1150110: {
        'name': 'PFI0_1KOHM_ENABLE'
    },
    1150111: {
        'name': 'PFI1_1KOHM_ENABLE'
    },
    1150112: {
        'name': 'PFI2_1KOHM_ENABLE'
    },
    1150113: {
        'name': 'PFI3_1KOHM_ENABLE'
    },
    1150114: {
        'name': 'PFI4_1KOHM_ENABLE'
    },
    1150115: {
        'name': 'PFI5_1KOHM_ENABLE'
    },
    1150116: {
        'name': 'PFI0_10KOHM_ENABLE'
    },
    1150117: {
        'name': 'PFI1_10KOHM_ENABLE'
    },
    1150118: {
        'name': 'PFI2_10KOHM_ENABLE'
    },
    1150119: {
        'name': 'PFI3_10KOHM_ENABLE'
    },
    1150120: {
        'name': 'PFI4_10KOHM_ENABLE'
    },
    1150121: {
        'name': 'PFI5_10KOHM_ENABLE'
    },
    1150200: {
        'name': 'FRONT_SYNC_CLK_SRC'
    },
    1150201: {
        'name': 'REAR_SYNC_CLK_SRC'
    },
    1150202: {
        'name': 'SYNC_CLK_DIV1'
    },
    1150203: {
        'name': 'SYNC_CLK_DIV2'
    },
    1150204: {
        'name': 'SYNC_CLK_RST_PXITRIG_NUM'
    },
    1150205: {
        'name': 'SYNC_CLK_PFI0_FREQ'
    },
    1150206: {
        'name': 'SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG'
    },
    1150207: {
        'name': 'SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG'
    },
    1150208: {
        'name': 'SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG'
    },
    1150300: {
        'name': 'TERMINAL_STATE_PXISTAR'
    },
    1150301: {
        'name': 'TERMINAL_STATE_PXITRIG'
    },
    1150302: {
        'name': 'TERMINAL_STATE_PFI'
    },
    1150303: {
        'name': 'TERMINAL_STATE_PXIEDSTARC'
    },
    1150304: {
        'name': 'TERMINAL_STATE_PFILVDS'
    },
    1150305: {
        'name': 'TERMINAL_STATE_PXIEDSTARCPERIPHERAL'
    },
    1150306: {
        'name': 'TERMINAL_STATE_PXIEDSTARBPERIPHERAL'
    },
    1150307: {
        'name': 'TERMINAL_STATE_PXISTARPERIPHERAL'
    },
    1150400: {
        'name': 'DDS_FREQ'
    },
    1150401: {
        'name': 'DDS_UPDATE_SOURCE'
    },
    1150402: {
        'name': 'DDS_INITIAL_DELAY'
    },
    1150500: {
        'name': 'CLKIN_PLL_FREQ'
    },
    1150501: {
        'name': 'CLKIN_USE_PLL'
    },
    1150502: {
        'name': 'CLKIN_PLL_LOCKED'
    },
    1150503: {
        'name': 'CLKOUT_GAIN_ENABLE'
    },
    1150504: {
        'name': 'PXICLK10_PRESENT'
    },
    1150505: {
        'name': 'CLKIN_ATTENUATION_DISABLE'
    },
    1150600: {
        'name': 'USER_LED_STATE'
    },
    1150700: {
        'name': '1588_IP_ADDRESS'
    },
    1150712: {
        'name': '1588_CLOCK_STATE'
    },
    1150729: {
        'name': '1588_CLOCK_ID'
    },
    1150730: {
        'name': '1588_CLOCK_CLASS'
    },
    1150731: {
        'name': '1588_CLOCK_ACCURACY'
    },
    1150732: {
        'name': '1588_PRIORITY1'
    },
    1150733: {
        'name': '1588_PRIORITY2'
    },
    1150734: {
        'name': '1588_GRANDMASTER_CLOCK_ID'
    },
    1150735: {
        'name': '1588_GRANDMASTER_CLOCK_CLASS'
    },
    1150736: {
        'name': '1588_GRANDMASTER_CLOCK_ACCURACY'
    },
    1150737: {
        'name': '1588_GRANDMASTER_PRIORITY1'
    },
    1150738: {
        'name': '1588_GRANDMASTER_PRIORITY2'
    },
    1150716: {
        'name': '1588_STEPS_TO_GRANDMASTER'
    },
    1150739: {
        'name': '1588_LOG_SYNC_INTERVAL'
    },
    1150740: {
        'name': '1588_MEAN_PATH_DELAY'
    },
    1150741: {
        'name': '1588_GRANDMASTER_IP_ADDRESS'
    },
    1150742: {
        'name': '1588_BMCA_MODE'
    },
    1150743: {
        'name': '1588_INTERFACE_NAME'
    },
    1150718: {
        'name': '1588_TIMESTAMP_BUF_SIZE'
    },
    1150719: {
        'name': '1588_AVAIL_TIMESTAMPS'
    },
    1150720: {
        'name': '1588_CLK_RESOLUTION'
    },
    1150800: {
        'name': 'TIMEREF_PRESENT'
    },
    1150801: {
        'name': 'TIMEREF_CURRENT'
    },
    1150802: {
        'name': 'TIMEREF_OFFSET'
    },
    1150808: {
        'name': 'TIMEREF_OFFSET_NS'
    },
    1150804: {
        'name': 'TIMEREF_CORRECTION'
    },
    1150805: {
        'name': 'TIMEREF_UTC_OFFSET'
    },
    1150806: {
        'name': 'TIMEREF_UTC_OFFSET_VALID'
    },
    1150807: {
        'name': 'TIMEREF_LAST_SYNC_ID'
    },
    1150809: {
        'name': 'TIMEREF_SELECTED_TYPE'
    },
    1150810: {
        'name': 'TIMEREF_TYPE'
    },
    1150811: {
        'name': 'TIMEREF_SELECTED_NAME'
    },
    1150812: {
        'name': 'TIMEREF_ENABLED'
    },
    1150813: {
        'name': 'TIMEREF_IS_SELECTED'
    },
    1150900: {
        'name': 'GPS_ANTENNA_CONNECTED'
    },
    1150901: {
        'name': 'GPS_RECALCULATE_POSITION'
    },
    1150902: {
        'name': 'GPS_SATELLITES_AVAILABLE'
    },
    1150903: {
        'name': 'GPS_SELF_SURVEY'
    },
    1150904: {
        'name': 'GPS_MOBILE_MODE'
    },
    1150905: {
        'name': 'GPS_STATUS'
    },
    1151100: {
        'name': '8021AS_PORT_STATE'
    },
    1151101: {
        'name': '8021AS_CLOCK_ID'
    },
    1151102: {
        'name': '8021AS_CLOCK_CLASS'
    },
    1151103: {
        'name': '8021AS_CLOCK_ACCURACY'
    },
    1151104: {
        'name': '8021AS_PRIORITY1'
    },
    1151105: {
        'name': '8021AS_PRIORITY2'
    },
    1151106: {
        'name': '8021AS_GRANDMASTER_CLOCK_ID'
    },
    1151107: {
        'name': '8021AS_GRANDMASTER_CLOCK_CLASS'
    },
    1151108: {
        'name': '8021AS_GRANDMASTER_CLOCK_ACCURACY'
    },
    1151109: {
        'name': '8021AS_GRANDMASTER_PRIORITY1'
    },
    1151110: {
        'name': '8021AS_GRANDMASTER_PRIORITY2'
    },
    1151111: {
        'name': '8021AS_LOG_SYNC_INTERVAL'
    },
    1151112: {
        'name': '8021AS_LOG_ANNOUNCE_INTERVAL'
    },
    1151113: {
        'name': '8021AS_INTERFACE_NAME'
    },
    1151114: {
        'name': '8021AS_NEIGHBOR_PROP_DELAY_THRESH'
    },
    1151115: {
        'name': '8021AS_AS_CAPABLE'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nisync/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/config.py sha256=93e0123ba8f78d5652091f3b44590a82861add92ac6920d49827cd837c4da688 bytes=1234 -->
## FILE: source/codegen/metadata/nisync/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/config.py`
- sha256: `93e0123ba8f78d5652091f3b44590a82861add92ac6920d49827cd837c4da688`
- bytes: 1234

````python
# -*- coding: utf-8 -*-
config = {
    "api_version": "20.1.0",
    "c_header": "nisync.h",
    "c_function_prefix": "niSync_",
    "service_class_prefix": "NiSync",
    "java_package": "com.ni.grpc.sync",
    "csharp_namespace": "NationalInstruments.Grpc.Sync",
    "namespace_component": "nisync",
    "close_function": "Close",
    "context_manager_name": {
        "abort_function": "Abort",
        "initiate_function": "InitiateAcquisition",
        "task": "acquisition",
    },
    "custom_types": [],
    "driver_name": "NI-SYNC",
    "init_function": "init",
    "status_ok": "status >= 0",
    "library_info": {
        "Linux": {"64bit": {"name": "nisync", "type": "cdll"}},
        "Windows": {
            "32bit": {"name": "nisync.dll", "type": "windll"},
            "64bit": {"name": "nisync.dll", "type": "cdll"},
        },
    },
    'linux_rt_support': True,
    "metadata_version": "2.0",
    "module_name": "nisync",
    "repeated_capabilities": [{"prefix": "", "python_name": "channels"}],
    "session_class_description": "An NI-SYNC session to a National Instruments timing and synchronization device.",
    "session_handle_parameter_name": "vi",
    "uses_nitclk": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/config_addon.py sha256=b7926e5e93e1fe91f1c439d0bd8730cb336d31f8601a1da7a7a0f79ba29dc4b6 bytes=133 -->
## FILE: source/codegen/metadata/nisync/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/config_addon.py`
- sha256: `b7926e5e93e1fe91f1c439d0bd8730cb336d31f8601a1da7a7a0f79ba29dc4b6`
- bytes: 133

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/custom_proto.mako sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nisync/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/custom_proto.mako`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````mako

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/enums.py sha256=0513ba33bc50a2a1764b05bcbf0532a83389b0e76dbdf8df7328584ceda1ee33 bytes=39 -->
## FILE: source/codegen/metadata/nisync/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/enums.py`
- sha256: `0513ba33bc50a2a1764b05bcbf0532a83389b0e76dbdf8df7328584ceda1ee33`
- bytes: 39

````python
# -*- coding: utf-8 -*-
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nisync/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/functions.py sha256=f749021707c9e951ab6dde9effdcfe1e23da356154f019a31b130d743dd04b1e bytes=43918 -->
## FILE: source/codegen/metadata/nisync/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/functions.py`
- sha256: `f749021707c9e951ab6dde9effdcfe1e23da356154f019a31b130d743dd04b1e`
- bytes: 43918

````python
# -*- coding: utf-8 -*-
functions = {
    "Init": {
        "cname": "niSync_init",
        "init_method": True,
        "parameters": [
            {
                "direction": "in",
                "name": "resourceName",
                "type": "ViRsrc",
            },
            {
                "direction": "in",
                "name": "idQuery",
                "type": "ViBoolean",
            },
            {
                "direction": "in",
                "name": "resetDevice",
                "type": "ViBoolean",
            },
            {
                "direction": "out",
                "name": "vi",
                "type": "ViSession",
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
        "returns": "ViStatus",
    },
    "Close": {
        "cname": "niSync_close",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "ErrorMessage": {
        "cname": "niSync_error_message",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "errorCode",
                "type": "ViStatus",
            },
            {
                "direction": "out",
                "name": "errorMessage",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "fixed",
                    "value": 256,
                },
            },
        ],
        "returns": "ViStatus",
    },
    "Reset": {
        "cname": "niSync_reset",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "PersistConfig": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "SelfTest": {
        "cname": "niSync_self_test",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "selfTestResult",
                "type": "ViInt16",
            },
            {
                "direction": "out",
                "name": "selfTestMessage",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "fixed",
                    "value": 256,
                },
            },
        ],
        "returns": "ViStatus",
    },
    "RevisionQuery": {
        "cname": "niSync_revision_query",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "driverRevision",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "fixed",
                    "value": 256,
                },
            },
            {
                "direction": "out",
                "name": "firmwareRevision",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "fixed",
                    "value": 256,
                },
            },
        ],
        "returns": "ViStatus",
    },
    "ConnectTrigTerminals": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "syncClock",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "updateEdge",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "DisconnectTrigTerminals": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "ConnectSWTrigToTerminal": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "syncClock",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "updateEdge",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "delay",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "DisconnectSWTrigFromTerminal": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "SendSoftwareTrigger": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "ConnectClkTerminals": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "DisconnectClkTerminals": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "MeasureFrequency": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "duration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "actualDuration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequency",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "error",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "MeasureFrequencyEx": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "duration",
                "type": "ViReal64",
            },
            {
                "direction": "in",
                "name": "decimationCount",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "actualDuration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequency",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequencyError",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "Start1588": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "Stop1588": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "Start8021AS": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "Stop8021AS": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTime": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "timeSource",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "GetTime": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "ResetFrequency": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "CreateFutureTimeEvent": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "outputLevel",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "ClearFutureTimeEvents": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "EnableTimeStampTrigger": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "activeEdge",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "EnableTimeStampTriggerWithDecimation": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "activeEdge",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "decimationCount",
                "type": "ViUInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "ReadTriggerTimeStamp": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "timeout",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "detectedEdge",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "ReadMultipleTriggerTimeStamp": {
        "codegen_method": "CustomCode",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "timestampsToRead",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeout",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "timeSecondsBuffer",
                "type": "ViUInt32[]",
                "size": {
                    "mechanism": "passed-in",
                    "value": "timestampsToRead",
                },
            },
            {
                "direction": "out",
                "name": "timeNanosecondsBuffer",
                "type": "ViUInt32[]",
                "size": {
                    "mechanism": "passed-in",
                    "value": "timestampsToRead",
                },
            },
            {
                "direction": "out",
                "name": "timeFractionalNanosecondsBuffer",
                "type": "ViUInt16[]",
                "size": {
                    "mechanism": "passed-in",
                    "value": "timestampsToRead",
                },
            },
            {
                "direction": "out",
                "name": "detectedEdgeBuffer",
                "type": "ViInt32[]",
                "size": {
                    "mechanism": "passed-in",
                    "value": "timestampsToRead",
                },
            },
            {
                "direction": "out",
                "name": "timestampsRead",
                "type": "ViUInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "DisableTimeStampTrigger": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "CreateClock": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "highTicks",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "lowTicks",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "in",
                "name": "stopTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "stopTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "stopTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "ClearClock": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReferenceFreeRunning": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReferenceGPS": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReferenceIRIG": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "irigType",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReferencePPS": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "useManualTime",
                "type": "ViBoolean",
            },
            {
                "direction": "in",
                "name": "initialTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReference1588OrdinaryClock": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "SetTimeReference8021AS": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "EnableGPSTimestamping": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "EnableIRIGTimestamping": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "irigType",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "ReadLastGPSTimestamp": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "timestampSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "gpsSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "gpsNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "gpsFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "ReadLastIRIGTimestamp": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "timestampSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "irigbSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "irigbNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "irigbFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "returns": "ViStatus",
    },
    "DisableGPSTimestamping": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "returns": "ViStatus",
    },
    "DisableIRIGTimestamping": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "GetVelocity": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "eastVelocity",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "northVelocity",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "upVelocity",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "GetLocation": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "latitude",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "longitude",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "altitude",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "GetTimeReferenceNames": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "bufferSize",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeReferenceNames",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "ivi-dance",
                    "value": "bufferSize",
                },
            },
        ],
        "returns": "ViStatus",
    },
    "GetAttributeViInt32": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "GetAttributeViReal64": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "GetAttributeViBoolean": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViBoolean",
            },
        ],
        "returns": "ViStatus",
    },
    "GetAttributeViString": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "bufferSize",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViChar[]",
                "size": {
                    "mechanism": "ivi-dance",
                    "value": "bufferSize",
                },
            },
        ],
        "returns": "ViStatus",
    },
    "SetAttributeViInt32": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "SetAttributeViReal64": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "SetAttributeViBoolean": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViBoolean",
            },
        ],
        "returns": "ViStatus",
    },
    "SetAttributeViString": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "GetExtCalLastDateAndTime": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "year",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "month",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "day",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "hour",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "minute",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "GetExtCalLastTemp": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "temp",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "GetExtCalRecommendedInterval": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "months",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "ChangeExtCalPassword": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "oldPassword",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "newPassword",
                "type": "ViConstString",
            },
        ],
        "returns": "ViStatus",
    },
    "ReadCurrentTemperature": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "temperature",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalGetOscillatorVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalGetClk10PhaseVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalGetDDSStartPulsePhaseVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalGetDDSInitialPhase": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "phase",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "InitExtCal": {
        "init_method": True,
        "parameters": [
            {
                "direction": "in",
                "name": "resourceName",
                "type": "ViRsrc",
            },
            {
                "direction": "in",
                "name": "password",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "vi",
                "type": "ViSession",
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
        "returns": "ViStatus",
    },
    "CloseExtCal": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "action",
                "type": "ViInt32",
            },
        ],
        "returns": "ViStatus",
    },
    "CalAdjustOscillatorVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalAdjustClk10PhaseVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalAdjustDDSStartPulsePhaseVoltage": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
    "CalAdjustDDSInitialPhase": {
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredPhase",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldPhase",
                "type": "ViReal64",
            },
        ],
        "returns": "ViStatus",
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nisync/functions_addon.py sha256=ceef314306e111183d1709307b9c107416f8968ce2cddcb9a8f63ad136887314 bytes=239 -->
## FILE: source/codegen/metadata/nisync/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nisync/functions_addon.py`
- sha256: `ceef314306e111183d1709307b9c107416f8968ce2cddcb9a8f63ad136887314`
- bytes: 239

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/__init__.py sha256=bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5 bytes=248 -->
## FILE: source/codegen/metadata/nitclk/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/__init__.py`
- sha256: `bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5`
- bytes: 248

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

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/attributes.py sha256=97c7ce1d9139b5315f6a6943b8b5935a9aadf33522a1aaf9b085e31d9707eec4 bytes=2504 -->
## FILE: source/codegen/metadata/nitclk/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/attributes.py`
- sha256: `97c7ce1d9139b5315f6a6943b8b5935a9aadf33522a1aaf9b085e31d9707eec4`
- bytes: 2504

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 23.0.0f77
attributes = {
    1: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SYNC_PULSE_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    2: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    3: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'START_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession'
    },
    4: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'REF_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession'
    },
    5: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'SCRIPT_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession'
    },
    6: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'PAUSE_TRIGGER_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession'
    },
    8: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'TCLK_ACTUAL_PERIOD',
        'resettable': False,
        'type': 'ViReal64'
    },
    9: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_TCLK_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    10: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SYNC_PULSE_CLOCK_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    11: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SAMPLE_CLOCK_DELAY',
        'resettable': False,
        'type': 'ViReal64'
    },
    13: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    16: {
        'codegen_method': 'public',
        'grpc_type': 'nidevice_grpc.Session',
        'name': 'SEQUENCER_FLAG_MASTER_SESSION',
        'resettable': False,
        'type': 'ViSession'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/attributes_addon.py sha256=9146afb2a7b5ff733089fdb1e8196ac0ffa358def5853f0aa9ceaf75e5b2e8a3 bytes=489 -->
## FILE: source/codegen/metadata/nitclk/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/attributes_addon.py`
- sha256: `9146afb2a7b5ff733089fdb1e8196ac0ffa358def5853f0aa9ceaf75e5b2e8a3`
- bytes: 489

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release

attributes_codegen_method = {
}

attributes_converters = {
}

attributes_enums = {
}

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/config.py sha256=80429015f3ca50064d3b3fa77efa7ba502c84935c67c3b932201cf3aa60ac44a bytes=1090 -->
## FILE: source/codegen/metadata/nitclk/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/config.py`
- sha256: `80429015f3ca50064d3b3fa77efa7ba502c84935c67c3b932201cf3aa60ac44a`
- bytes: 1090

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 23.0.0f77
config = {
    'additional_headers': {
    },
    'api_version': '23.0.0f77',
    'c_function_prefix': 'niTClk_',
    'c_header': 'niTClk.h',
    'close_function': None,
    'csharp_namespace': 'NationalInstruments.Grpc.TClk',
    'custom_types': [
    ],
    'driver_name': 'NI-TClk',
    'java_package': 'com.ni.grpc.tclk',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nitclk',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niTClk.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niTClk_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'nitclk',
    'namespace_component': 'nitclk',
    'service_class_prefix': 'NiTClk',
    'session_handle_parameter_name': 'session_number',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/config_addon.py sha256=ab226f65092356895748859400d84500ff52b274f9db5cfe4c818b32037079e1 bytes=226 -->
## FILE: source/codegen/metadata/nitclk/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/config_addon.py`
- sha256: `ab226f65092356895748859400d84500ff52b274f9db5cfe4c818b32037079e1`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.4.dev0',
    'latest_runtime_version_tested_against': '20.0.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/enums.py sha256=659942c5ea6ee689bb1e9e598d9f6bccc76f99d9cfea2779f7950cdbba62b035 bytes=109 -->
## FILE: source/codegen/metadata/nitclk/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/enums.py`
- sha256: `659942c5ea6ee689bb1e9e598d9f6bccc76f99d9cfea2779f7950cdbba62b035`
- bytes: 109

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 23.0.0f77
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/enums_addon.py sha256=dbf418b8284947b47f924645405d73afcec7e32244537e068fdb604dc3a1f12b bytes=466 -->
## FILE: source/codegen/metadata/nitclk/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/enums_addon.py`
- sha256: `dbf418b8284947b47f924645405d73afcec7e32244537e068fdb604dc3a1f12b`
- bytes: 466

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/functions.py sha256=5ee6d73b53ffb0ff3b1b1f15fc317658416215eda3cedad56aa714cd5c952744 bytes=17067 -->
## FILE: source/codegen/metadata/nitclk/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/functions.py`
- sha256: `5ee6d73b53ffb0ff3b1b1f15fc317658416215eda3cedad56aa714cd5c952744`
- bytes: 17067

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 23.0.0f77
functions = {
    'ConfigureForHomogeneousTriggers': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FinishSyncPulseSenderSynchronize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'minTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'minTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'bufSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'value',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'tags': [
                        'strlen-bug'
                    ],
                    'value': 'bufSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtendedErrorInfo': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'errorString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorStringSize'
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'errorStringSize',
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'errorStringSize',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'done',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'value_raw',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'session',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiTClkAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'value',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'value_raw',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetupForSyncPulseSenderSynchronize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'minTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'minTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Synchronize': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'minTclkPeriod',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'minTclkPeriod',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SynchronizeToSyncPulseSender': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'minTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'minTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitUntilDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'sessionCount',
                'determine_size_from': [
                    'sessions'
                ],
                'direction': 'in',
                'grpc_type': 'uint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'cppName': 'sessions',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'sessions',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]'
            },
            {
                'cppName': 'timeout',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/functions_addon.py sha256=25d30eedbc868691fd20b6567188e8765f8298a7e4ba3ff179985cdb447ff636 bytes=1636 -->
## FILE: source/codegen/metadata/nitclk/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/functions_addon.py`
- sha256: `25d30eedbc868691fd20b6567188e8765f8298a7e4ba3ff179985cdb447ff636`
- bytes: 1636

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
}

functions_locking = {
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
}

# Default values for method parameters
functions_default_value = {
}

# Parameter that need to be array.array
functions_array = {
}

# We want to use a common name for self_cal across all drivers
functions_name = {
}

# Functions not in original metadata.
functions_additional_functions = {
}

# Converted parameters
functions_converters = {
}

# The extracted metadata is incorrect. Patch it here.
functions_bad_source_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/nitclk.proto sha256=da0ec15d68e02da200ec37b83637e893152c445e462f4e58c9cf4a5ba8d77b55 bytes=5775 -->
## FILE: source/codegen/metadata/nitclk/nitclk.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/nitclk.proto`
- sha256: `da0ec15d68e02da200ec37b83637e893152c445e462f4e58c9cf4a5ba8d77b55`
- bytes: 5775

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-TClk API metadata version 23.0.0f77
//---------------------------------------------------------------------
// Proto file for the NI-TClk Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.tclk";
option java_outer_classname = "NiTClk";
option csharp_namespace = "NationalInstruments.Grpc.TClk";

package nitclk_grpc;

import "session.proto";

service NiTClk {
  rpc ConfigureForHomogeneousTriggers(ConfigureForHomogeneousTriggersRequest) returns (ConfigureForHomogeneousTriggersResponse);
  rpc FinishSyncPulseSenderSynchronize(FinishSyncPulseSenderSynchronizeRequest) returns (FinishSyncPulseSenderSynchronizeResponse);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetExtendedErrorInfo(GetExtendedErrorInfoRequest) returns (GetExtendedErrorInfoResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc IsDone(IsDoneRequest) returns (IsDoneResponse);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetupForSyncPulseSenderSynchronize(SetupForSyncPulseSenderSynchronizeRequest) returns (SetupForSyncPulseSenderSynchronizeResponse);
  rpc Synchronize(SynchronizeRequest) returns (SynchronizeResponse);
  rpc SynchronizeToSyncPulseSender(SynchronizeToSyncPulseSenderRequest) returns (SynchronizeToSyncPulseSenderResponse);
  rpc WaitUntilDone(WaitUntilDoneRequest) returns (WaitUntilDoneResponse);
}

enum NiTClkAttribute {
  NITCLK_ATTRIBUTE_UNSPECIFIED = 0;
  NITCLK_ATTRIBUTE_SYNC_PULSE_SOURCE = 1;
  NITCLK_ATTRIBUTE_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL = 2;
  NITCLK_ATTRIBUTE_START_TRIGGER_MASTER_SESSION = 3;
  NITCLK_ATTRIBUTE_REF_TRIGGER_MASTER_SESSION = 4;
  NITCLK_ATTRIBUTE_SCRIPT_TRIGGER_MASTER_SESSION = 5;
  NITCLK_ATTRIBUTE_PAUSE_TRIGGER_MASTER_SESSION = 6;
  NITCLK_ATTRIBUTE_TCLK_ACTUAL_PERIOD = 8;
  NITCLK_ATTRIBUTE_EXPORTED_TCLK_OUTPUT_TERMINAL = 9;
  NITCLK_ATTRIBUTE_SYNC_PULSE_CLOCK_SOURCE = 10;
  NITCLK_ATTRIBUTE_SAMPLE_CLOCK_DELAY = 11;
  NITCLK_ATTRIBUTE_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE = 13;
  NITCLK_ATTRIBUTE_SEQUENCER_FLAG_MASTER_SESSION = 16;
}

message ConfigureForHomogeneousTriggersRequest {
  repeated nidevice_grpc.Session sessions = 1;
}

message ConfigureForHomogeneousTriggersResponse {
  int32 status = 1;
}

message FinishSyncPulseSenderSynchronizeRequest {
  repeated nidevice_grpc.Session sessions = 1;
  double min_time = 2;
}

message FinishSyncPulseSenderSynchronizeResponse {
  int32 status = 1;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetExtendedErrorInfoRequest {
}

message GetExtendedErrorInfoResponse {
  int32 status = 1;
  string error_string = 2;
}

message InitiateRequest {
  repeated nidevice_grpc.Session sessions = 1;
}

message InitiateResponse {
  int32 status = 1;
}

message IsDoneRequest {
  repeated nidevice_grpc.Session sessions = 1;
}

message IsDoneResponse {
  int32 status = 1;
  bool done = 2;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
  double value_raw = 4;
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
  nidevice_grpc.Session value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session session = 1;
  string channel_name = 2;
  NiTClkAttribute attribute_id = 3;
  string value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetupForSyncPulseSenderSynchronizeRequest {
  repeated nidevice_grpc.Session sessions = 1;
  double min_time = 2;
}

message SetupForSyncPulseSenderSynchronizeResponse {
  int32 status = 1;
}

message SynchronizeRequest {
  repeated nidevice_grpc.Session sessions = 1;
  double min_tclk_period = 2;
}

message SynchronizeResponse {
  int32 status = 1;
}

message SynchronizeToSyncPulseSenderRequest {
  repeated nidevice_grpc.Session sessions = 1;
  double min_time = 2;
}

message SynchronizeToSyncPulseSenderResponse {
  int32 status = 1;
}

message WaitUntilDoneRequest {
  repeated nidevice_grpc.Session sessions = 1;
  double timeout = 2;
}

message WaitUntilDoneResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nitclk/README.md sha256=14abbce94e68ab0e3500afe1208798ff0d64a1caeeec55df486a2482fb948261 bytes=209 -->
## FILE: source/codegen/metadata/nitclk/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nitclk/README.md`
- sha256: `14abbce94e68ab0e3500afe1208798ff0d64a1caeeec55df486a2482fb948261`
- bytes: 209

````markdown
# Updating

To update this metadata folder. Find the nitclk_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/__init__.py sha256=9c48927788cdb651f7d16925d0f7aec7581ffd84fc90c81588a106207b5c6712 bytes=375 -->
## FILE: source/codegen/metadata/nixnet/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/__init__.py`
- sha256: `9c48927788cdb651f7d16925d0f7aec7581ffd84fc90c81588a106207b5c6712`
- bytes: 375

````python
from .functions import functions
from .attributes import attributes
from .enums_addon import enums_validation_suppressions
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nixnet/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nixnet/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/config.py sha256=3c5aa95ed1931c32712ca71ceb614bd378fef1b72e0652fa365ee0e94d9bca94 bytes=2444 -->
## FILE: source/codegen/metadata/nixnet/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/config.py`
- sha256: `3c5aa95ed1931c32712ca71ceb614bd378fef1b72e0652fa365ee0e94d9bca94`
- bytes: 2444

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '21.0.0',
    'c_header': 'nixnet.h',
    'c_function_prefix': 'nx',
    'service_class_prefix': 'NiXnet',
    'java_package': 'com.ni.grpc.nixnet',
    'csharp_namespace': 'NationalInstruments.Grpc.NiXnet',
    'namespace_component': 'nixnet',
    'close_function': 'Clear',
    'code_readiness': 'Release',
    'driver_name': 'NI-XNET',
    'status_ok': 'status >= 0',
    'additional_headers': { 'custom/nixnet_converters.h': ['service.cpp'] },
    'resource_handle_type': ['nxSessionRef_t', 'nxDatabaseRef_t'],
    'type_to_grpc_type': {
        'nxSessionRef_t': 'nidevice_grpc.Session',
        'nxDatabaseRef_t': 'nidevice_grpc.Session',
        'nxDatabaseRef_t[]': 'repeated nidevice_grpc.Session',
        'u32': 'uint32',
        'u64': 'uint64',
        'u8': 'uint32',
        'u8[]': 'bytes',
        'f64': 'double',
        'char[]': 'string',
        'const char[]': 'string',
        'nxStatus_t': 'int32',
        'void[]': 'bytes',
        'nxTimestamp1ns_t': 'uint64',
        'nxTimestamp100ns_t': 'uint64'
    },
    'custom_types': [
        {
            'name': '_nxTimeLocalNetwork_t',
            'grpc_name': 'TimeLocalNetwork',
            'fields': [
                {
                    'type': 'nxTimestamp1ns_t',
                    'name': 'LocalTime',
                    'grpc_name': 'local_time'
                },
                {
                    'type': 'nxTimestamp1ns_t',
                    'name': 'NetworkTime',
                    'grpc_name': 'network_time'
                },
                {
                    'type': 'u32',
                    'name': 'Flags',
                    'grpc_name': 'flags'
                }
            ]
        }
    ],
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nixnet',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nixnet.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nixnet.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'metadata_version': '0.1',
    'module_name': 'nixnet',
    'session_class_description': 'An NI-XNET session.',
    'session_handle_parameter_name': 'session'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/config_addon.py sha256=d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58 bytes=226 -->
## FILE: source/codegen/metadata/nixnet/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/config_addon.py`
- sha256: `d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nixnet/custom_proto.mako sha256=ede736c05051d535f71872bc1b3f36adcbaf427353e0d2dcf47438525517d4f9 bytes=7432 -->
## FILE: source/codegen/metadata/nixnet/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nixnet/custom_proto.mako`
- sha256: `ede736c05051d535f71872bc1b3f36adcbaf427353e0d2dcf47438525517d4f9`
- bytes: 7432

````mako
message FlexRayStats {
  uint32 num_syntax_error_ch_a = 1;
  uint32 num_syntax_error_ch_b = 2;
  uint32 num_content_error_ch_a = 3;
  uint32 num_content_error_ch_b = 4;
  uint32 num_slot_boundary_violation_ch_a = 5;
  uint32 num_slot_boundary_violation_ch_b = 6;
}

message J1939CommState {
  uint32 pgn = 1;
  uint32 source_address = 2;
  uint32 destination_address = 3;
  uint32 transmit_error = 4;
  uint32 receive_error = 5;
}

message CanCommResponse {
  CanCommState comm_state = 1;
  uint32 comm_state_raw = 2;
  uint32 transceiver_error = 3;
  uint32 sleep = 4;
  CanLastErr last_error = 5;
  uint32 last_error_raw = 6;
  uint32 transmit_error_counter = 7;
  uint32 receive_error_counter = 8;
}

message FlexRayCommResponse {
  FlexRayPocState poc_state = 1;
  uint32 poc_state_raw = 2;
  uint32 clock_correction_failed = 3;
  uint32 passive_to_active_count = 4;
  uint32 channel_a_sleep = 5;
  uint32 channel_b_sleep = 6;
}

message LinCommResponse {
  uint32 sleep = 1;
  LinCommState comm_state = 2;
  uint32 comm_state_raw = 3;
  uint32 last_error = 4;
  uint32 last_error_received = 5;
  uint32 last_error_expected = 6;
  uint32 last_error_id = 7;
  uint32 transceiver_ready = 8;
  uint32 schedule_index = 9;
}

message SessionInfoResponse {
  SessionInfoState info = 1;
  uint32 info_raw = 2;
}

message ReadStateValue {
  oneof value {
    uint64 time_current = 1;
    uint64 time_communicating = 2;
    uint64 time_start = 3;
    CanCommResponse can_comm = 4;
    FlexRayCommResponse flex_ray_comm = 5;
    FlexRayStats flex_ray_stats = 6;
    LinCommResponse lin_comm = 7;
    SessionInfoResponse session_info = 8;
    J1939CommState j1939_comm_state = 9;
    TimeLocalNetwork time_current2 = 10;
    TimeLocalNetwork time_communicating2 = 11;
    TimeLocalNetwork time_start2 = 12;
  }
  bytes state_value_raw = 13;
}

message LinDiagnosticScheduleChangeRequest {
  oneof schedule_enum {
    LinDiagnosticSchedule schedule = 1;
    uint32 schedule_raw = 2;
  }
}

message WriteStateValue {
  oneof value {
    uint32 lin_schedule_change = 1;
    uint32 flex_ray_symbol = 2;
    LinDiagnosticScheduleChangeRequest lin_diagnostic_schedule_change = 3;
    uint32 ethernet_sleep = 4;
    uint32 ethernet_wake = 5;
  }
}

message U32Array {
  repeated uint32 u32_array = 1;
}

message DbRefArray {
  repeated nidevice_grpc.Session db_ref = 1;
}

message DeviceRefArray {
  repeated nidevice_grpc.Session dev_ref = 1;
}

message InterfaceRefArray {
  repeated nidevice_grpc.Session intf_ref = 1;
}

message EptRxFilter {
  uint32 use_flags = 1;
  uint32 vid = 2;
  uint32 priority = 3;
  string destination_mac = 4;    
}

message EptRxFilterArray {
  repeated EptRxFilter ept_rx_filter = 1;
}

message GetPropertyRequest {
  oneof session_repository {
    nidevice_grpc.Session device = 1;
    nidevice_grpc.Session interface_ref = 2;
    nidevice_grpc.Session session = 3;
  }
  oneof property_id_enum {
    Property property_id = 4;
    uint32 property_id_raw = 5;
  }
} 

message GetPropertyResponse {
  int32 status = 1;
  oneof property_value {
    uint32 u32_scalar = 2;
    bool bool_scalar = 3;
    string str = 4;
    uint64 u64_scalar = 5;
    int32 i32_scalar = 6;
    double f64_scalar = 7;
    string string_array = 8;
    U32Array u32_array = 9;
    nidevice_grpc.Session db_ref = 10;
    DbRefArray db_ref_array = 11;
    nidevice_grpc.Session dev_ref = 12;
    DeviceRefArray dev_ref_array = 13;
    InterfaceRefArray intf_ref_array = 14;
    EptRxFilterArray ept_rx_filter_array = 15;
  }
}

message SetPropertyRequest {
  nidevice_grpc.Session session = 1;
  oneof property_id_enum {
    Property property_id = 2;
    uint32 property_id_raw = 3;
  }
  oneof property_value {
    uint32 u32_scalar = 4;
    bool bool_scalar = 5;
    string str = 6;
    uint64 u64_scalar = 7;
    int32 i32_scalar = 8;
    double f64_scalar = 9;
    string string_array = 10;
    U32Array u32_array = 11;
    nidevice_grpc.Session db_ref = 12;
    DbRefArray db_ref_array = 13;
    EptRxFilterArray ept_rx_filter_array = 14;
  }
}

message SetPropertyResponse {
  int32 status = 1;
}

message GetSubPropertyRequest {
  nidevice_grpc.Session session = 1;
  uint32 active_index = 2;
  oneof subproperty_id_enum {
    SubProperty property_id = 3;
    uint32 property_id_raw = 4;
  }
}

message GetSubPropertyResponse {
  int32 status = 1;
  oneof property_value {
    uint32 u32_scalar = 2;
    string str = 3;
    double f64_scalar = 9;
  }
}

message DbGetPropertyRequest {
  nidevice_grpc.Session dbobject = 1;
  oneof dbproperty_id_enum {
    DBProperty property_id = 2;
    uint32 property_id_raw = 3;
  }
}

message DbGetPropertyResponse {
  int32 status = 1;
  oneof property_value {
    uint32 u32_scalar = 2;
    bool bool_scalar = 3;
    string str = 4;
    uint64 u64_scalar = 5;
    double f64_scalar = 6;
    U32Array u32_array = 7;
    bytes u8_array = 8;
    nidevice_grpc.Session db_ref = 9;
    DbRefArray db_ref_array = 10;
  }
}

message SetSubPropertyRequest {
  nidevice_grpc.Session session = 1;
  uint32 active_index = 2;
  oneof subproperty_id_enum {
    SubProperty property_id = 3;
    uint32 property_id_raw = 4;
  }
  oneof property_value {
    uint32 u32_scalar = 5;
    string str = 6;
    double f64_scalar = 7;
  }
}

message SetSubPropertyResponse {
  int32 status = 1;
}

message DbSetPropertyRequest {
  nidevice_grpc.Session dbobject = 1;
  oneof dbproperty_id_enum {
    DBProperty property_id = 2;
    uint32 property_id_raw = 3;
  }
  oneof property_value {
    uint32 u32_scalar = 4;
    bool bool_scalar = 5;
    string str = 6;
    uint64 u64_scalar = 7;
    double f64_scalar = 8;
    U32Array u32_array = 9;
    bytes u8_array = 10;
    nidevice_grpc.Session db_ref = 11;
    DbRefArray db_ref_array = 12;
  }
}

message DbSetPropertyResponse {
  int32 status = 1;
}

message FrameRequest {
  uint64 timestamp = 1;
  uint32 identifier = 2;
  oneof type_enum{
     FrameType type = 3;
     uint32 type_raw = 4;
  }
  repeated FrameFlags flags = 5;
  uint32 info = 6;
  bytes payload = 7;
}

message FrameResponse {
  uint64 timestamp = 1;
  uint32 identifier = 2;
  FrameType type = 3;
  uint32 type_raw = 4;
  repeated FrameFlags flags = 5;
  uint32 flags_raw = 6;
  uint32 info = 7;
  bytes payload = 8;
}

message EnetFrameRequest {
  oneof type_enum{
    EnetFrameType type = 1;
    uint32 type_raw = 2;
  }
  uint64 device_timestamp = 3;
  uint64 network_timestamp = 4;
  repeated EnetFlags flags_mapped = 5;
  bytes frame_data = 6;
}

message EnetFrameResponse {
  EnetFrameType type = 1;
  uint32 type_raw = 2;
  uint64 device_timestamp = 3;
  uint64 network_timestamp = 4;
  repeated EnetFlags flags_mapped= 5;
  uint32 flags_raw = 6;
  bytes frame_data = 7;
}

message FrameBufferRequest {
  oneof frame {
    FrameRequest can = 1;
    FrameRequest lin = 2;
    FrameRequest flex_ray = 3;
    FrameRequest j1939 = 4;
    EnetFrameRequest enet = 5;
  }
}

message FrameBufferResponse {
  oneof frame {
    FrameResponse can = 1;
    FrameResponse lin = 2;
    FrameResponse flex_ray = 3;
    FrameResponse j1939 = 4;
    EnetFrameResponse enet = 5;
  }
}
````
