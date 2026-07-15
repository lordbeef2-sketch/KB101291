# NI DOCUMENT BUNDLE: ni-dmm-properties

<!--NI_BUNDLE_CHUNK bundle=ni-dmm-properties start=1 end=93 -->
<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/cnidmm.html language=enus -->
## TOPIC 00001: niDMM Properties

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/cnidmm.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/cnidmm.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### niDMM Properties

February 2019

Use the NI-DMM properties to access advanced configuration options for digital multimeter applications.

© 2004–2019 National Instruments Corporation. All Rights Reserved.

| Property | Description |
| --- | --- |
| Active Channel | Specifies the channel name used to access all subsequent channel-based properties in this property node. Set the channel before setting channel-based properties. Pass a name that the instrument driver defines or a virtual channel name configured in MAX. Details |
| Configuration:Function | Specifies the measurement function. If you are setting this property directly, you must also set the Operation Mode property, which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform. If you are programming properties directly, you must set the Operation Mode property before setting other configuration properties. If the Operation Mode property is set to Waveform Mode, the only valid function types are Waveform Voltage and Waveform Current. Set the Operation Mode property to IVIDMM Mode to set all other function values. Details |
| Configuration:Range | Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the Function property. For example, if the Function property is set to DC Volts, the units are volts. Details |
| Configuration:Auto Range Value | Specifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this property is set during a read operation. Details |
| Configuration:Digits Resolution | Specifies the measurement resolution in digits. Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed. Details |
| Configuration:Absolute Resolution | Specifies the measurement resolution in absolute units. Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed. Details |
| Configuration:Measurement Options:Input Resistance | Specifies the input resistance of the instrument. Details |
| Configuration:Measurement Options:Auto Zero | Specifies the AutoZero mode. Details |
| Configuration:Measurement Options:ADC Calibration | For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC calibration mode. Details |
| Configuration:Measurement Options:Powerline Frequency | Specifies the powerline frequency. The NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases for setting the Aperture Time property in powerline cycles. Details |
| Configuration:Measurement Options:Offset Compensated Ohms | For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables offset compensated ohms. Details |
| Configuration:Measurement Options:Current Source | Specifies the current source provided during diode measurements. Details |
| Configuration:Measurement Options:Shunt Value | For the NI 4050 only, specifies the shunt resistance value. Details |
| Configuration:Measurement Options:DC Noise Rejection | Specifies the DC noise rejection mode. Details |
| Configuration:Measurement Options:Min Frequency | Specifies the minimum frequency component of the input signal for AC measurements. This property affects the DMM only when you set the Function property to AC measurements. The valid range is 1 Hz-300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz-100 Hz for the NI 4065. Details |
| Configuration:Measurement Options:Max Frequency | Specifies the maximum frequency component of the input signal for AC measurements. This property is used only for error checking and verifies that the value of this parameter is less than the maximum frequency of the device. This property affects the DMM only when you set the Function property to AC measurements. Details |
| Configuration:Measurement Options:Frequency Voltage Range | For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum amplitude of the input signal for frequency measurements. Details |
| Configuration:Measurement Options:Frequency Voltage Auto Range Value | For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of the frequency voltage range. If auto ranging is enabled, shows the actual value of the active frequency voltage range. If not Auto Ranging, the value is the same as that of the Frequency Voltage Range property. Details |
| Configuration:Measurement Options:Temperature:Transducer Type | Specifies the transducer type. Details |
| Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type | Specifies the thermocouple type. Details |
| Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type | Specifies the thermocouple reference junction type. Details |
| Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction | Specifies the value of the fixed reference junction temperature for a thermocouple in degrees Celsius. Details |
| Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type | Specifies the RTD type. Details |
| Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance | Specifies the RTD resistance at 0 degrees Celsius. Details |
| Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A | Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property is set to Custom. Details |
| Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B | Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property is set to Custom. Details |
| Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C | Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property is set to Custom. Details |
| Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type | Specifies the thermistor type. Details |
| Configuration:Measurement Options:Temperature:Thermistor:Thermistor A | Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type property is set to Custom. Details |
| Configuration:Measurement Options:Temperature:Thermistor:Thermistor B | Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type property is set to Custom. Details |
| Configuration:Measurement Options:Temperature:Thermistor:Thermistor C | Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type property is set to Custom. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average | For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type | For the NI 4081 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance | For the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance | For the NI 4082 and NI 4072 only, represents the active part (resistance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance | For the NI 4082 and NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance | For the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model | For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements. Details |
| Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias | For the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements. Details |
| Configuration:Advanced:Aperture Time | Specifies the measurement aperture time for the current configuration. Aperture time is specified in units set by the Aperture Time Units property. To override the default aperture, set this property to the desired aperture time after calling niDMM Config Measurement. To return to the default, set this property to Aperture Time Auto (-1). Details |
| Configuration:Advanced:Aperture Time Units | Specifies the units of aperture time for the current configuration. Details |
| Configuration:Advanced:Settle Time | Specifies the settling time in seconds. Use this property to override the default settling time. To return to the default, set this property to Auto (-1). Details |
| Configuration:Advanced:Number Of Averages | Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, this property applies only when the aperture time is not set to Auto and Auto Zero is ON. The Number of Averages Property will be ignored otherwise. The default is 4 for 7 1/2 digits; otherwise, the default is 1. Details |
| Configuration:Advanced:Operation Mode | Specifies how the DMM acquires data. When you call niDMM Config Measurement, NI-DMM sets this property to IVIDMM Mode. When you call niDMM Configure Waveform Acquisition, NI-DMM sets this property to Waveform Mode. If you are programming properties directly, you must set this property before setting other configuration properties. Details |
| Multi Point Acquisition:Sample Count | Specifies the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. Setting Sample Count to 0 causes the conditional statement "Measurements equal to Sample Count" to always evaluate to False, and causes the DMM to continue taking measurements in the inner loop. Details |
| Multi Point Acquisition:Trigger Count | Specifies the number of triggers the DMM receives before returning to the Idle state. This property can be set to any positive ViInt32 value for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082. Refer to Multiple Point Acquisitions in the NI Digital Multimeters Help for more information. Details |
| Multi Point Acquisition:Sample Trigger | Specifies the sample trigger source. To determine which values are supported by each device, refer to the LabVIEW Trigger Routing section in the NI Digital Multimeters Help. Details |
| Multi Point Acquisition:Sample Trig Slope | Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered. Details |
| Multi Point Acquisition:Sample Interval | Specifies the amount of time in seconds the DMM waits between measurement cycles. This property only applies when the Sample Trigger property is set to INTERVAL. The default value (-1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger. Details |
| Multi Point Acquisition:Sample Delay Mode | Specifies when the Sample Interval property is used. Set this property before calling niDMM Configure Multi Point if you configure the properties for multipoint measurements using the niDMM Configure Multi Point VI. Note The NI 4080/4081/4082 are not supported. |
|  | Note The NI 4080/4081/4082 are not supported. |
| Multi Point Acquisition:Advanced:Buffer Size | Specifies the size in samples of the internal data buffer. Maximum size is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM chooses the buffer size. Details |
| Multi Point Acquisition:Advanced:Latency | Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses the transfer size. Details |
| Waveform Acquisition:Waveform Points | For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of points to acquire in a waveform acquisition. Details |
| Waveform Acquisition:Waveform Rate | Specifies the rate of the waveform acquisition in samples per second (S/s). The valid rate is calculated by dividing 1,800,000 by an integer divisor, and the rate falls between 10 and 1,800,000 samples per second. The waveform rate is coerced upwards to the next valid rate. The default value is 1,800,000 samples per second. Not supported by NI 4065. Details |
| Waveform Acquisition:Waveform Coupling | For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition. Details |
| Trigger:Trigger Source | Specifies the trigger source. When niDMM Initiate is called, the DMM waits for the trigger specified with this property. After it receives the trigger, the DMM waits the length of time specified with the Trigger Delay property. The DMM then takes a measurement. To determine which values are supported by each device, refer to the LabVIEW Trigger Routing section in the NI Digital Multimeters Help. Details |
| Trigger:Trigger Slope | Specifies the edge of the signal from the specified trigger source on which the DMM is triggered. Details |
| Trigger:Trigger Delay | Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. The default value is Auto Delay (-1), which means that the DMM waits an appropriate settling time before taking the measurement. The NI 4080/4081/4082 uses the value specified in this property as additional settling time. The valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is 10.0 ns. The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time. For these devices, the valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the onboard timing resolution is 34.72 ns. Use positive values to set the trigger delay in seconds. Valid Range: Auto Delay (-1.0), 0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072) Default Value: Auto Delay Details |
| Trigger:Measurement Complete Dest | Specifies the destination of the measurement complete (MC) signal. To determine which values are supported by each device, refer to the LabVIEW Trigger Routing section in the NI Digital Multimeters Help. Details |
| Trigger:Measurement Destination Slope | Specifies the polarity of the generated measurement complete signal. Details |
| Inherent IVI Attributes:User Options:Simulate | Specifies whether to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call IVI Get and Set VIs, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver VIs return calculated values. The default value is FALSE (0). Use niDMM Initialize With Options to override the default setting. Details |
| Inherent IVI Attributes:User Options:Driver Setup | This property indicates the Driver Setup string that the user specified when initializing the driver. Some cases exist where the end-user must specify instrument driver options at initialization time. An example of this is specifying a particular instrument model from among a family of instruments that the driver supports. This is useful when using simulation. The end-user can specify driver-specific options through the Driver Setup keyword in the Option String parameter in niDMM Initialize With Options. If the user does not specify a Driver Setup string, this property returns an empty string. Details |
| Inherent IVI Attributes:User Options:Range Check | Specifies whether to validate property values and VI parameters. If enabled, the instrument driver validates the parameter values passed to driver VIs. Range checking parameters is very useful for debugging. After the user program is validated, you can set this property to FALSE (0) to disable range checking and maximize performance. The default value is TRUE (1). Use niDMM Initialize With Options to override the default setting. Details |
| Inherent IVI Attributes:User Options:Query Instrument Status | Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After the user program is validated, this property can be set to FALSE (0) to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property. The default value is TRUE (1). Use niDMM Initialize With Options to override the default setting. Details |
| Inherent IVI Attributes:User Options:Cache | Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, it significantly increases execution speed. The instrument driver can choose to always cache or to never cache particular properties regardless of the setting of this property. The default value is TRUE (1). Use niDMM Initialize With Options to override the default setting. Details |
| Inherent IVI Attributes:User Options:Record Value Coercions | Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 properties. The default value is FALSE (0). Use niDMM Initialize With Options to override the default setting. Use niDMM Get Next Coercion Record to extract and delete the oldest coercion record from the list. Details |
| Inherent IVI Attributes:User Options:Interchange Check | Specifies whether to perform interchangeability checking and log interchangeability warnings when you call niDMM VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Use niDMM Get Next Interchange Warning to extract interchange warnings. Use niDMM Clear Interchange Warnings to clear the list of interchangeability warnings without reading them. Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property affects the behavior of the instrument and you have not set that property, or the property has been invalidated since you set it. Details |
| Inherent IVI Attributes:Instrument Capabilities:Channel Count | Indicates the number of channels that the specific instrument driver supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag property is set, the IVI engine maintains a separate cache value for each channel. Details |
| Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix | The prefix for the specific instrument driver. The name of each user-callable VI in this driver starts with this prefix. The prefix can be up to a maximum of eight characters. Details |
| Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer | A string containing the manufacturer of the instrument. Details |
| Inherent IVI Attributes:Instrument Identification:Instrument Model | A string containing the instrument model. Details |
| Inherent IVI Attributes:Instrument Identification:Instrument Product ID | The PCI product ID. Details |
| Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision | A string containing the instrument firmware revision number. Details |
| Inherent IVI Attributes:Instrument Identification:Instrument Serial Number | A string containing the serial number of the instrument. This property corresponds to the serial number label that is attached to most products. Details |
| Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models | A string containing the instrument models supported by the specific driver. Details |
| Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities | A string containing the capabilities and extension groups supported by the specific driver. Details |
| Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor | A string containing the vendor of the specific driver. Details |
| Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version | The major version number of the class specification for the specific driver. Details |
| Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version | The minor version number of the class specification for the specific driver. Details |
| Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description | A string containing a description of the specific driver. Details |
| Inherent IVI Attributes:Version Info:Specific Driver Major Version | Returns the major version number of this instrument driver. Details |
| Inherent IVI Attributes:Version Info:Specific Driver Minor Version | Returns the minor version number of this instrument driver. Details |
| Inherent IVI Attributes:Version Info:Specific Driver Revision | A string that contains additional version information about this instrument driver. Details |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | A string containing the logical name of the instrument. Details |
| Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor | A string containing the resource descriptor of the instrument. Details |
| Obsolete:Inherent IVI Attributes:Error Info:Primary Error | A code that describes the first error that occurred since the last call to niDMM Get Error for the session. The value follows the VXIplug&play conventions. A negative value describes an error condition. A positive value describes a warning condition. A zero indicates that no error or warning occurred. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Details |
| Obsolete:Inherent IVI Attributes:Error Info:Secondary Error | An optional code that provides additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information. Details |
| Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration | An optional string that contains additional information concerning the primary error condition. Details |
| Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version | The major version number of the IVI engine. Details |
| Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version | The minor version number of the IVI engine. Details |
| Obsolete:Inherent IVI Attributes:Version Info:Engine Revision | A string that contains additional version information about the IVI engine. Details |
| Obsolete:Misc:IDQuery response | A string containing the type of instrument used in the current session. Details |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_absoluteresolution.html language=enus -->
## TOPIC 00002: Configuration:Absolute Resolution Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_absoluteresolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_absoluteresolution.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Absolute Resolution Property

**Short Name:**Absolute Resolution

Property of [niDMM](cnidmm.html)

Specifies the measurement resolution in absolute units. Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed.

|  | Note NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Measurement Absolute, niDMM Configure Measurement Digits |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_activechannel.html language=enus -->
## TOPIC 00003: Active Channel Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_activechannel.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Active Channel Property

**Short Name:**Active Channel

Property of [niDMM](cnidmm.html)

Specifies the channel name used to access all subsequent channel-based properties in this property node. Set the channel before setting channel-based properties. Pass a name that the instrument driver defines or a virtual channel name configured in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_adccalibration.html language=enus -->
## TOPIC 00004: Configuration:Measurement Options:ADC Calibration Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_adccalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_adccalibration.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:ADC Calibration Property

**Short Name:**ADC Calibration

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC calibration mode.

| Auto (-1) | The DMM enables or disables ADC calibration based on the configured function and resolution. |
| --- | --- |
| Off (0) | The DMM does not compensate for changes to the gain. |
| On (1) | The DMM measures an internal reference to calculate the correct gain for the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure ADC Calibration |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_aperturetime.html language=enus -->
## TOPIC 00005: Configuration:Advanced:Aperture Time Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_aperturetime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_aperturetime.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Advanced:Aperture Time Property

**Short Name:**Aperture Time

Property of [niDMM](cnidmm.html)

Specifies the measurement aperture time for the current configuration. Aperture time is specified in units set by the Aperture Time Units property. To override the default aperture, set this property to the desired aperture time after calling [niDMM Config Measurement](/csh?topicname=dmmviref/nidmm_config_measurement.html). To return to the default, set this property to Aperture Time Auto (-1).

Any number of powerline cycles (PLCs) within the minimum and maximum ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

On the NI 4065 the minimum aperture time is 333 micro s and the maximum aperture time is 78.2 s. If setting the number of averages directly, the total measurement time is aperture time X the number of averages, which must be less than 72.8 s. The aperture times allowed are 333 micro s, 667 micro s, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so on. If you set an aperture time other than 333 micro s, 667 micro s, or multiples of 1.11 ms, the value will be coerced up to the next supported aperture time.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Get Aperture Time Info |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_aperturetimeunits.html language=enus -->
## TOPIC 00006: Configuration:Advanced:Aperture Time Units Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_aperturetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_aperturetimeunits.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Advanced:Aperture Time Units Property

**Short Name:**Aperture Time Units

Property of [niDMM](cnidmm.html)

Specifies the units of aperture time for the current configuration.

| Seconds (0) | Units are seconds. |
| --- | --- |
| Power Line Cycles (1) | Units are powerline cycles (PLCs). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Get Aperture Time Info |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_autorangevalue.html language=enus -->
## TOPIC 00007: Configuration:Auto Range Value Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_autorangevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_autorangevalue.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Auto Range Value Property

**Short Name:**Auto Range Value

Property of [niDMM](cnidmm.html)

Specifies the value of the range. If auto ranging is enabled, shows the actual value of the active range. The value of this property is set during a read operation.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | niDMM Get Auto Range Value |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_autozero.html language=enus -->
## TOPIC 00008: Configuration:Measurement Options:Auto Zero Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_autozero.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_autozero.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Auto Zero Property

**Short Name:**Auto Zero

Property of [niDMM](cnidmm.html)

Specifies the AutoZero mode.

| Auto (-1) | NI-DMM chooses the Auto Zero setting based on the configured function and resolution. |
| --- | --- |
| Off (0) | Disables AutoZero. Note The NI 4065 does not support this setting |
|  | Note The NI 4065 does not support this setting |
| On (1) | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading. For NI 4065 devices, Auto Zero is always ON. Auto Zero is an integral part of the signal measurement phase and adds no extra time to the overall measurement. |
| Once (2) | The DMM internally disconnects the input signal for the first measurement and takes a zero reading. It then subtracts the zero reading from the first reading and the following readings. The NI 4065 does not support this setting. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Auto Zero |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_buffersize.html language=enus -->
## TOPIC 00009: Multi Point Acquisition:Advanced:Buffer Size Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_buffersize.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_buffersize.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Advanced:Buffer Size Property

**Short Name:**Buffer Size

Property of [niDMM](cnidmm.html)

Specifies the size in samples of the internal data buffer. Maximum size is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM chooses the buffer size.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_cablecompensationtype.html language=enus -->
## TOPIC 00010: Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_cablecompensationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_cablecompensationtype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type Property

**Short Name:**Cable Compensation Type

Property of [niDMM](cnidmm.html)

For the NI 4081 and NI 4072 only, specifies the type of cable compensation that is applied to the current capacitance or inductance measurement for the current range.

|  | Note Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value. |
| --- | --- |

| None (0) | No cable compensation. |
| --- | --- |
| Open (1) | Open cable compensation. |
| Short (2) | Short cable compensation. |
| Open_and_Short (3) | Open and short cable compensation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Cable Comp Type |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_cache.html language=enus -->
## TOPIC 00011: Inherent IVI Attributes:User Options:Cache Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_cache.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Cache Property

**Short Name:**Cache

Property of [niDMM](cnidmm.html)

Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. Thus, it significantly increases execution speed. The instrument driver can choose to always cache or to never cache particular properties regardless of the setting of this property. The default value is TRUE (1). 
 
 
 Use [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html) to override the default setting.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Initialize With Options |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_channelcount.html language=enus -->
## TOPIC 00012: Inherent IVI Attributes:Instrument Capabilities:Channel Count Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_channelcount.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Capabilities:Channel Count Property

**Short Name:**Channel Count

Property of [niDMM](cnidmm.html)

Indicates the number of channels that the specific instrument driver supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag property is set, the IVI engine maintains a separate cache value for each channel.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_conductance.html language=enus -->
## TOPIC 00013: Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_conductance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_conductance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance Property

**Short Name:**Conductance

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, specifies the active part (conductance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place.

|  | Note Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Open Cable Comp Values |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_currentsource.html language=enus -->
## TOPIC 00014: Configuration:Measurement Options:Current Source Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_currentsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_currentsource.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Current Source Property

**Short Name:**Current Source

Property of [niDMM](cnidmm.html)

Specifies the current source provided during diode measurements.

| 1 Microamp (1.000000E-6) | NI 4070/4071/4072 are supported. |
| --- | --- |
| 10 Microamp (1.000000E-5) | NI 4080/4081/4082 and NI 4070/4071/4072 are supported. |
| 100 Microamp (1.000000E-4) | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported. |
| 1 Milliamp (1.000000E-3) | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Current Source |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_dcbias.html language=enus -->
## TOPIC 00015: Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_dcbias.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_dcbias.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias Property

**Short Name:**DC Bias

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, controls the available DC bias for capacitance measurements.

| DC Bias Off (0) | NI-DMM programs the device not to use the DC bias. |
| --- | --- |
| DC Bias On (1) | NI-DMM programs the device to use the DC bias. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_dcnoiserejection.html language=enus -->
## TOPIC 00016: Configuration:Measurement Options:DC Noise Rejection Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_dcnoiserejection.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_dcnoiserejection.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:DC Noise Rejection Property

**Short Name:**DC Noise Rejection

Property of [niDMM](cnidmm.html)

Specifies the DC noise rejection mode.

| Auto (-1) | The driver chooses the DC noise rejection setting based on the configured function and resolution. |
| --- | --- |
| Normal (0) | NI-DMM weighs all samples equally. |
| Second Order (1) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a triangular weighing function. |
| High Order (2) | NI-DMM weighs the samples taken in the middle of the aperture time more than samples taken at the beginning and the end of the measurement using a bell-curve weighing function. Note NI 4065 does not support this setting. |
|  | Note NI 4065 does not support this setting. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_digitsresolution.html language=enus -->
## TOPIC 00017: Configuration:Digits Resolution Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_digitsresolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_digitsresolution.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Digits Resolution Property

**Short Name:**Digits Resolution

Property of [niDMM](cnidmm.html)

Specifies the measurement resolution in digits. Setting this property to higher values increases the measurement accuracy. Setting this property to lower values increases the measurement speed.

|  | Note NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property. |
| --- | --- |

| 3.5 (3.5000000E+0) | Specifies 3.5 digits resolution. |
| --- | --- |
| 4.5 (4.500000E+0) | Specifies 4.5 digits resolution. |
| 5.5 (5.500000E+0) | Specifies 5.5 digits resolution. |
| 6.5 (6.500000E+0) | Specifies 6.5 digits resolution. |
| 7.5 (7.500000E+0) | Specifies 7.5 digits resolution. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Measurement Absolute, niDMM Configure Measurement Digits |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_driversetup.html language=enus -->
## TOPIC 00018: Inherent IVI Attributes:User Options:Driver Setup Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_driversetup.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Driver Setup Property

**Short Name:**Driver Setup

Property of [niDMM](cnidmm.html)

This property indicates the Driver Setup string that the user specified when initializing the driver. Some cases exist where the end-user must specify instrument driver options at initialization time. An example of this is specifying a particular instrument model from among a family of instruments that the driver supports. This is useful when using simulation. The end-user can specify driver-specific options through the Driver Setup keyword in the Option String parameter in [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html). If the user does not specify a Driver Setup string, this property returns an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | niDMM Initialize With Options |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_enginemajorversion.html language=enus -->
## TOPIC 00019: Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_enginemajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_enginemajorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version Property

**Short Name:**Engine Major Version

Property of [niDMM](cnidmm.html)

The major version number of the IVI engine.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_engineminorversion.html language=enus -->
## TOPIC 00020: Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_engineminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_engineminorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version Property

**Short Name:**Engine Minor Version

Property of [niDMM](cnidmm.html)

The minor version number of the IVI engine.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_enginerevision.html language=enus -->
## TOPIC 00021: Obsolete:Inherent IVI Attributes:Version Info:Engine Revision Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_enginerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_enginerevision.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Version Info:Engine Revision Property

**Short Name:**Engine Revision

Property of [niDMM](cnidmm.html)

A string that contains additional version information about the IVI engine.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_errorelaboration.html language=enus -->
## TOPIC 00022: Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_errorelaboration.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_errorelaboration.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration Property

**Short Name:**Error Elaboration

Property of [niDMM](cnidmm.html)

An optional string that contains additional information concerning the primary error condition.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_frequencyvoltageautorangevalue.html language=enus -->
## TOPIC 00023: Configuration:Measurement Options:Frequency Voltage Auto Range Value Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_frequencyvoltageautorangevalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_frequencyvoltageautorangevalue.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Frequency Voltage Auto Range Value Property

**Short Name:**Frequency Voltage Auto Range Value

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of the frequency voltage range. If auto ranging is enabled, shows the actual value of the active frequency voltage range. If not Auto Ranging, the value is the same as that of the Frequency Voltage Range property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_frequencyvoltagerange.html language=enus -->
## TOPIC 00024: Configuration:Measurement Options:Frequency Voltage Range Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_frequencyvoltagerange.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_frequencyvoltagerange.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Frequency Voltage Range Property

**Short Name:**Frequency Voltage Range

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum amplitude of the input signal for frequency measurements.

| Auto Range On | -1.0 | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
| --- | --- | --- |
| Auto Range Off | -2.0 | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Frequency Voltage Range |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_function.html language=enus -->
## TOPIC 00025: Configuration:Function Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_function.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_function.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Function Property

**Short Name:**Function

Property of [niDMM](cnidmm.html)

Specifies the measurement function. 
 
 
 If you are setting this property directly, you must also set the [Operation Mode](pnidmm_operationmode.html) property, which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform. If you are programming properties directly, you must set the Operation Mode property before setting other configuration properties. If the Operation Mode property is set to Waveform Mode, the only valid function types are Waveform Voltage and Waveform Current. Set the Operation Mode property to IVIDMM Mode to set all other function values.

| DC Volts (1) | All devices supported. |
| --- | --- |
| AC Volts (2) | All devices supported. |
| DC Current (3) | All devices supported. |
| AC Current (4) | All devices supported. |
| 2-Wire Resistance (5) | All devices supported. |
| 4-Wire Resistance (101) | NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported. |
| Frequency (104) | NI 4070/4071/4072 and NI 4080/4081/4182 supported. |
| Period (105) | NI 4070/4071/4072 and NI 4080/4081/4182 supported. |
| AC Volts DC Coupled (1001) | NI 4070/4071/4072 and NI 4080/4081/4182 supported. |
| Diode (1002) | All devices supported. |
| Waveform Voltage (1003) | NI 4070/4071/4072 and NI 4080/4081/4182 supported. |
| Waveform Current (1004) | NI 4070/4071/4072 and NI 4080/4081/4182 supported. |
| Capacitance (1005) | NI 4072 and NI 4082 supported. |
| Inductance (1006) | NI 4072 and NI 4082 supported. |
| Temperature (108) | NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Measurement Absolute, niDMM Configure Measurement Digits, niDMM Configure Waveform Acquisition |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_groupcapabilities.html language=enus -->
## TOPIC 00026: Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_groupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_groupcapabilities.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities Property

**Short Name:**Group Capabilities

Property of [niDMM](cnidmm.html)

A string containing the capabilities and extension groups supported by the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_idqueryresponse.html language=enus -->
## TOPIC 00027: Obsolete:Misc:IDQuery response Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_idqueryresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_idqueryresponse.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Misc:IDQuery response Property

**Short Name:**IDQuery response

Property of [niDMM](cnidmm.html)

A string containing the type of instrument used in the current session.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_inputresistance.html language=enus -->
## TOPIC 00028: Configuration:Measurement Options:Input Resistance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_inputresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_inputresistance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Input Resistance Property

**Short Name:**Input Resistance

Property of [niDMM](cnidmm.html)

Specifies the input resistance of the instrument.

| 1 M Ohm (1.000000E+6) | Input resistance of 1 M Ohm |
| --- | --- |
| 10 M Ohm (1.000000E+7) | Input resistance of 10 M Ohm |
| Greater Than 10 G Ohm (1.000000E+10) | Input resistance greater than 10 G Ohm |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_instrumentfirmwarerevision.html language=enus -->
## TOPIC 00029: Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_instrumentfirmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_instrumentfirmwarerevision.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision Property

**Short Name:**Instrument Firmware Revision

Property of [niDMM](cnidmm.html)

A string containing the instrument firmware revision number.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | niDMM Revision Query |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_instrumentmanufacturer.html language=enus -->
## TOPIC 00030: Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_instrumentmanufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_instrumentmanufacturer.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer Property

**Short Name:**Instrument Manufacturer

Property of [niDMM](cnidmm.html)

A string containing the manufacturer of the instrument.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_instrumentmodel.html language=enus -->
## TOPIC 00031: Inherent IVI Attributes:Instrument Identification:Instrument Model Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_instrumentmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_instrumentmodel.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Instrument Model Property

**Short Name:**Instrument Model

Property of [niDMM](cnidmm.html)

A string containing the instrument model.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_instrumentproductid.html language=enus -->
## TOPIC 00032: Inherent IVI Attributes:Instrument Identification:Instrument Product ID Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_instrumentproductid.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_instrumentproductid.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Instrument Product ID Property

**Short Name:**Instrument Product ID

Property of [niDMM](cnidmm.html)

The PCI product ID.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_instrumentserialnumber.html language=enus -->
## TOPIC 00033: Inherent IVI Attributes:Instrument Identification:Instrument Serial Number Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_instrumentserialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_instrumentserialnumber.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Instrument Serial Number Property

**Short Name:**Instrument Serial Number

Property of [niDMM](cnidmm.html)

A string containing the serial number of the instrument. This property corresponds to the serial number label that is attached to most products.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_interchangecheck.html language=enus -->
## TOPIC 00034: Inherent IVI Attributes:User Options:Interchange Check Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_interchangecheck.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Interchange Check Property

**Short Name:**Interchange Check

Property of [niDMM](cnidmm.html)

Specifies whether to perform interchangeability checking and log interchangeability warnings when you call niDMM VIs. Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Use [niDMM Get Next Interchange Warning](/csh?topicname=dmmviref/nidmm_get_next_interchange_warning.html) to extract interchange warnings. Use [niDMM Clear Interchange Warnings](/csh?topicname=dmmviref/nidmm_clear_interchange_warnings.html) to clear the list of interchangeability warnings without reading them. Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property affects the behavior of the instrument and you have not set that property, or the property has been invalidated since you set it.

| TRUE | 1 |
| --- | --- |
| FALSE | 0 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Clear Interchange Warnings, niDMM Get Next Interchange Warning |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_ioresourcedescriptor.html language=enus -->
## TOPIC 00035: Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_ioresourcedescriptor.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor Property

**Short Name:**I/O Resource Descriptor

Property of [niDMM](cnidmm.html)

A string containing the resource descriptor of the instrument.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_latency.html language=enus -->
## TOPIC 00036: Multi Point Acquisition:Advanced:Latency Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_latency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_latency.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Advanced:Latency Property

**Short Name:**Latency

Property of [niDMM](cnidmm.html)

Specifies the number of measurements transferred at a time from the instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses the transfer size.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_lccalculationmodel.html language=enus -->
## TOPIC 00037: Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_lccalculationmodel.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_lccalculationmodel.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model Property

**Short Name:**LC Calculation Model

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, specifies the type of algorithm that the measurement processing uses for capacitance and inductance measurements.

| Auto (-1) | NI-DMM chooses the algorithm based on function and range. |
| --- | --- |
| Series (0) | NI-DMM uses the series impedance model to calculate capacitance and inductance. |
| Parallel (1) | NI-DMM uses the parallel admittance model to calculate capacitance and inductance. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_logicalname.html language=enus -->
## TOPIC 00038: Inherent IVI Attributes:Advanced Session Information:Logical Name Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_logicalname.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Advanced Session Information:Logical Name Property

**Short Name:**Logical Name

Property of [niDMM](cnidmm.html)

A string containing the logical name of the instrument.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_maxfrequency.html language=enus -->
## TOPIC 00039: Configuration:Measurement Options:Max Frequency Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_maxfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_maxfrequency.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Max Frequency Property

**Short Name:**Max Frequency

Property of [niDMM](cnidmm.html)

Specifies the maximum frequency component of the input signal for AC measurements. This property is used only for error checking and verifies that the value of this parameter is less than the maximum frequency of the device. This property affects the DMM only when you set the Function property to AC measurements.

The valid ranges are shown in the following table.

| NI 4080/4081/4082, NI 4070/4071/4072 | 1 Hz-300 kHz |
| --- | --- |
| NI 4065 | 10 Hz-100 Hz |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure AC Bandwidth |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_measurementcompletdest.html language=enus -->
## TOPIC 00040: Trigger:Measurement Complete Dest Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_measurementcompletdest.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_measurementcompletdest.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Trigger:Measurement Complete Dest Property

**Short Name:**Measurement CompletDest

Property of [niDMM](cnidmm.html)

Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?topicname=dmm/lvtrigger_routing.html) section in the *NI Digital Multimeters Help*.

| None (-1) | No destination specified. |
| --- | --- |
| External (2) | Pin 6 on the AUX Connector |
| TTL 0 (111) | PXI Trigger Line 0 |
| TTL 1 (112) | PXI Trigger Line 1 |
| TTL 2 (113) | PXI Trigger Line 2 |
| TTL 3 (114) | PXI Trigger Line 3 |
| TTL 4 (115) | PXI Trigger Line 4 |
| TTL 5 (116) | PXI Trigger Line 5 |
| TTL 6 (117) | PXI Trigger Line 6 |
| TTL 7 (118) | PXI Trigger Line 7 |
| LBR Trig 0 (1003) | Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Meas Complete Dest |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_measurementdestinationslope.html language=enus -->
## TOPIC 00041: Trigger:Measurement Destination Slope Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_measurementdestinationslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_measurementdestinationslope.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Trigger:Measurement Destination Slope Property

**Short Name:**Measurement Destination Slope

Property of [niDMM](cnidmm.html)

Specifies the polarity of the generated measurement complete signal.

| Positive (0) | The driver triggers on the rising edge of the trigger signal. |
| --- | --- |
| Negative (1) | The driver triggers on the falling edge of the trigger signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_minfrequency.html language=enus -->
## TOPIC 00042: Configuration:Measurement Options:Min Frequency Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_minfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_minfrequency.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Min Frequency Property

**Short Name:**Min Frequency

Property of [niDMM](cnidmm.html)

Specifies the minimum frequency component of the input signal for AC measurements. This property affects the DMM only when you set the Function property to AC measurements. The valid range is 1 Hz-300 kHz for the NI 4080/4081/4082 and NI 4070/4071/4072 and 10 Hz-100 Hz for the NI 4065.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure AC Bandwidth |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_numberofaverages.html language=enus -->
## TOPIC 00043: Configuration:Advanced:Number Of Averages Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_numberofaverages.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_numberofaverages.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Advanced:Number Of Averages Property

**Short Name:**Number Of Averages

Property of [niDMM](cnidmm.html)

Specifies the number of averages to perform in a measurement. For the NI 4080/4081/4082 and NI 4070/4071/4072, this property applies only when the aperture time is not set to Auto and Auto Zero is ON. The Number of Averages Property will be ignored otherwise. The default is 4 for 7 1/2 digits; otherwise, the default is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_numberoflcmeasurementstoaverage.html language=enus -->
## TOPIC 00044: Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_numberoflcmeasurementstoaverage.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_numberoflcmeasurementstoaverage.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average Property

**Short Name:**Number of LC Measurements To Average

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_offsetcompensatedohms.html language=enus -->
## TOPIC 00045: Configuration:Measurement Options:Offset Compensated Ohms Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_offsetcompensatedohms.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_offsetcompensatedohms.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Offset Compensated Ohms Property

**Short Name:**Offset Compensated Ohms

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables offset compensated ohms.

| Off (0) | Disables Offset Compensated Ohms. |
| --- | --- |
| On (1) | Enables Offset Compensated Ohms. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Offset Comp Ohms |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_operationmode.html language=enus -->
## TOPIC 00046: Configuration:Advanced:Operation Mode Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_operationmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_operationmode.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Advanced:Operation Mode Property

**Short Name:**Operation Mode

Property of [niDMM](cnidmm.html)

Specifies how the DMM acquires data.

When you call [niDMM Config Measurement](/csh?topicname=dmmviref/nidmm_config_measurement.html), NI-DMM sets this property to IVIDMM Mode. When you call [niDMM Configure Waveform Acquisition](/csh?topicname=dmmviref/nidmm_configure_waveform_acquisition.html), NI-DMM sets this property to Waveform Mode. If you are programming properties directly, you must set this property before setting other configuration properties.

| IVIDMM Mode (0) | Single or multipoint measurements: When the Trigger Count and Sample Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM takes multipoint measurements. |
| --- | --- |
| Waveform Mode (1) | Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform measurements. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_powerlinefrequency.html language=enus -->
## TOPIC 00047: Configuration:Measurement Options:Powerline Frequency Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_powerlinefrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_powerlinefrequency.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Powerline Frequency Property

**Short Name:**Powerline Frequency

Property of [niDMM](cnidmm.html)

Specifies the powerline frequency. The NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases for setting the Aperture Time property in powerline cycles.

After configuring powerline frequency, set the Aperture Time Units property to PLCs. When setting the Aperture Time property, select the number of PLCs for the powerline frequency. For example, if powerline frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then aperture time in seconds = 20 ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs = 6, then aperture time in seconds = 16.667 ms * 6 PLCs = 100 ms.

|  | Note For 400 Hz powerline frequency, use the 50 Hz setting. |
| --- | --- |

| 50 Hz (5.000000E+1) | Specifies the powerline frequency as 50 Hz. |
| --- | --- |
| 60 Hz (6.000000E+1) | Specifies the powerline frequency as 60 Hz. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Powerline Frequency |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_primaryerror.html language=enus -->
## TOPIC 00048: Obsolete:Inherent IVI Attributes:Error Info:Primary Error Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_primaryerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_primaryerror.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Error Info:Primary Error Property

**Short Name:**Primary Error

Property of [niDMM](cnidmm.html)

A code that describes the first error that occurred since the last call to niDMM Get Error for the session. The value follows the VXIplug&play conventions. A negative value describes an error condition. A positive value describes a warning condition. A zero indicates that no error or warning occurred. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_queryinstrumentstatus.html language=enus -->
## TOPIC 00049: Inherent IVI Attributes:User Options:Query Instrument Status Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_queryinstrumentstatus.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Query Instrument Status Property

**Short Name:**Query Instrument Status

Property of [niDMM](cnidmm.html)

Specifies whether the instrument driver queries the instrument status after each operation. Querying the instrument status is very useful for debugging. After the user program is validated, this property can be set to FALSE (0) to disable status checking and maximize performance. The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property. The default value is TRUE (1). 
 
 
 Use [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html) to override the default setting.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Initialize With Options |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_range.html language=enus -->
## TOPIC 00050: Configuration:Range Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_range.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_range.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Range Property

**Short Name:**Range

Property of [niDMM](cnidmm.html)

Specifies the measurement range. Use positive values to represent the absolute value of the maximum expected measurement. The value is in units appropriate for the current value of the Function property. For example, if the Function property is set to DC Volts, the units are volts.

|  | Note The NI NI 4065 only supports Auto Range when the trigger and sample trigger are set to Immediate. |
| --- | --- |

| (-1.0) | Auto Range On | NI-DMM performs an Auto Range before acquiring the measurement. |
| --- | --- | --- |
| (-2.0) | Auto Range Off | NI-DMM sets the Range to the current Auto Range Value and uses this range for all subsequent measurements until the measurement configuration is changed. |
| (-3.0) | Auto Range Once | NI-DMM performs an Auto Range before acquiring the next measurement. The Auto Range Value is stored and used for all subsequent measurements until the measurement configuration is changed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Measurement Absolute, niDMM Configure Measurement Digits |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rangecheck.html language=enus -->
## TOPIC 00051: Inherent IVI Attributes:User Options:Range Check Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rangecheck.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Range Check Property

**Short Name:**Range Check

Property of [niDMM](cnidmm.html)

Specifies whether to validate property values and VI parameters. If enabled, the instrument driver validates the parameter values passed to driver VIs. Range checking parameters is very useful for debugging. After the user program is validated, you can set this property to FALSE (0) to disable range checking and maximize performance. The default value is TRUE (1). 
 Use [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html) to override the default setting.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Initialize With Options |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_reactance.html language=enus -->
## TOPIC 00052: Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_reactance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_reactance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance Property

**Short Name:**Reactance

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, represents the reactive part (reactance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place.

|  | Note Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Short Cable Comp Values |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_recordvaluecoercions.html language=enus -->
## TOPIC 00053: Inherent IVI Attributes:User Options:Record Value Coercions Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_recordvaluecoercions.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Record Value Coercions Property

**Short Name:**Record Value Coercions

Property of [niDMM](cnidmm.html)

Specifies whether the IVI engine keeps a list of the value coercions it makes for ViInt32 and ViReal64 properties. The default value is FALSE (0). 
 
 
 Use [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html) to override the default setting. Use [niDMM Get Next Coercion Record](/csh?topicname=dmmviref/nidmm_get_next_coercion_record.html) to extract and delete the oldest coercion record from the list.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_resistance.html language=enus -->
## TOPIC 00054: Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_resistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_resistance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance Property

**Short Name:**Resistance

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, represents the active part (resistance) of the short cable compensation. The valid range is any real number >0. The default value (-1) indicates that compensation has not taken place.

|  | Note Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Short Cable Comp Values |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rtda.html language=enus -->
## TOPIC 00055: Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rtda.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rtda.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A Property

**Short Name:**RTD A

Property of [niDMM](cnidmm.html)

Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the **RTD Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rtdb.html language=enus -->
## TOPIC 00056: Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rtdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rtdb.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B Property

**Short Name:**RTD B

Property of [niDMM](cnidmm.html)

Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the **RTD Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rtdc.html language=enus -->
## TOPIC 00057: Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rtdc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rtdc.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C Property

**Short Name:**RTD C

Property of [niDMM](cnidmm.html)

Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the **RTD Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rtdresistance.html language=enus -->
## TOPIC 00058: Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rtdresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rtdresistance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance Property

**Short Name:**RTD Resistance

Property of [niDMM](cnidmm.html)

Specifies the RTD resistance at 0 degrees Celsius.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_rtdtype.html language=enus -->
## TOPIC 00059: Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_rtdtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_rtdtype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type Property

**Short Name:**RTD Type

Property of [niDMM](cnidmm.html)

Specifies the RTD type.

| Custom (0) | Performs Callendar-Van Dusen RTD scaling with the user-specified A, B, and C coefficients. |
| --- | --- |
| Pt 3750 (1) | Performs scaling for a Pt 3750 RTD. |
| Pt 3851 (2) | Performs scaling for a Pt 3851 RTD. |
| Pt 3911 (3) | Performs scaling for a Pt 3911 RTD. |
| Pt 3916 (4) | Performs scaling for a Pt 3916 RTD. |
| Pt 3920 (5) | Performs scaling for a Pt 3920 RTD. |
| Pt 3928 (6) | Performs scaling for a Pt 3928 RTD. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_samplecount.html language=enus -->
## TOPIC 00060: Multi Point Acquisition:Sample Count Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_samplecount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_samplecount.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Sample Count Property

**Short Name:**Sample Count

Property of [niDMM](cnidmm.html)

Specifies the number of measurements the DMM takes each time it receives a trigger in a multiple point acquisition. Setting Sample Count to 0 causes the conditional statement "Measurements equal to Sample Count" to always evaluate to False, and causes the DMM to continue taking measurements in the inner loop.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_sampledelaymode.html language=enus -->
## TOPIC 00061: Multi Point Acquisition:Sample Delay Mode Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_sampledelaymode.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_sampledelaymode.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Sample Delay Mode Property

**Short Name:**Sample Delay Mode

Property of [niDMM](cnidmm.html)

Specifies when the [Sample Interval](pnidmm_sampleinterval.html) property is used. Set this property before calling [niDMM Configure Multi Point](/csh?topicname=dmmviref/nidmm_configure_multi_point.html) if you configure the properties for multipoint measurements using the [niDMM Configure Multi Point](/csh?topicname=dmmviref/nidmm_configure_multi_point.html) VI.

|  | Note The NI 4080/4081/4082 are not supported. |
| --- | --- |

| 0 | IVI compliant | The Sample Interval property is only used when the Sample Trigger is set to Interval. |
| --- | --- | --- |
| 1 | Not IVI compliant | The Sample Interval property is used as a delay after any type of Sample Trigger. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_sampleinterval.html language=enus -->
## TOPIC 00062: Multi Point Acquisition:Sample Interval Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_sampleinterval.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_sampleinterval.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Sample Interval Property

**Short Name:**Sample Interval

Property of [niDMM](cnidmm.html)

Specifies the amount of time in seconds the DMM waits between measurement cycles. This property only applies when the Sample Trigger property is set to INTERVAL. The default value (-1) ensures that the DMM settles for a recommended time, which is the same as using an immediate trigger.

The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional delay. On these devices, the onboard timing resolution is 34.72 ns and the valid range is 0-149 s.

Only positive values are valid when setting the sample interval.

|  | Note The NI 4080/4081/4082 are not supported. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_sampletrigger.html language=enus -->
## TOPIC 00063: Multi Point Acquisition:Sample Trigger Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_sampletrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_sampletrigger.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Sample Trigger Property

**Short Name:**Sample Trigger

Property of [niDMM](cnidmm.html)

Specifies the sample trigger source.

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?topicname=dmm/lvtrigger_routing.html) section in the *NI Digital Multimeters Help*.

| Immediate (1) | No trigger specified |
| --- | --- |
| Interval (10) | Interval trigger |
| External (2) | Pin 9 on the AUX Connector |
| Software Trig (3) | Configures the DMM to wait until niDMM Send Software Trigger is called. |
| TTL 0 (111) | PXI Trigger Line 0 |
| TTL 1 (112) | PXI Trigger Line 1 |
| TTL 2 (113) | PXI Trigger Line 2 |
| TTL 3 (114) | PXI Trigger Line 3 |
| TTL 4 (115) | PXI Trigger Line 4 |
| TTL 5 (116) | PXI Trigger Line 5 |
| TTL 6 (117) | PXI Trigger Line 6 |
| TTL 7 (118) | PXI Trigger Line 7 |
| PXI Star (131) | PXI Star trigger line |
| LBR Trig 1 (1004) | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis |
| AUX Trig 1 (1001) | Pin 3 on the AUX connector |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_sampletrigslope.html language=enus -->
## TOPIC 00064: Multi Point Acquisition:Sample Trig Slope Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_sampletrigslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_sampletrigslope.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Sample Trig Slope Property

**Short Name:**Sample Trig Slope

Property of [niDMM](cnidmm.html)

Specifies the edge of the signal from the specified sample trigger source on which the DMM is triggered.

| Positive (0) | The driver triggers on the rising edge of the trigger signal. |
| --- | --- |
| Negative (1) | The driver triggers on the falling edge of the trigger signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_secondaryerror.html language=enus -->
## TOPIC 00065: Obsolete:Inherent IVI Attributes:Error Info:Secondary Error Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_secondaryerror.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_secondaryerror.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete:Inherent IVI Attributes:Error Info:Secondary Error Property

**Short Name:**Secondary Error

Property of [niDMM](cnidmm.html)

An optional code that provides additional information concerning the primary error condition. The error and warning values can be status codes defined by IVI, VISA, class drivers, or specific drivers. Zero indicates no additional information.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_settletime.html language=enus -->
## TOPIC 00066: Configuration:Advanced:Settle Time Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_settletime.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_settletime.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Advanced:Settle Time Property

**Short Name:**Settle Time

Property of [niDMM](cnidmm.html)

Specifies the settling time in seconds. Use this property to override the default settling time. To return to the default, set this property to Auto (-1).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_shuntvalue.html language=enus -->
## TOPIC 00067: Configuration:Measurement Options:Shunt Value Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_shuntvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_shuntvalue.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Shunt Value Property

**Short Name:**Shunt Value

Property of [niDMM](cnidmm.html)

For the NI 4050 only, specifies the shunt resistance value.

|  | Note The NI 4050 requires an external shunt resistor for current measurements. This property should be set to the value of the shunt resistor. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_simulate.html language=enus -->
## TOPIC 00068: Inherent IVI Attributes:User Options:Simulate Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_simulate.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Simulate Property

**Short Name:**Simulate

Property of [niDMM](cnidmm.html)

Specifies whether to simulate instrument driver I/O operations. If simulation is enabled, instrument driver functions perform range checking and call IVI Get and Set VIs, but they do not perform instrument I/O. For output parameters that represent instrument data, the instrument driver VIs return calculated values. The default value is FALSE (0). Use [niDMM Initialize With Options](/csh?topicname=dmmviref/nidmm_initialize_with_options.html) to override the default setting.

|  | Note Simulate can only be set within the niDMM Initialize With Options VI. The property value cannot be changed outside of the VI. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Initialize With Options |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverclassspecmajorversion.html language=enus -->
## TOPIC 00069: Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverclassspecmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverclassspecmajorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version Property

**Short Name:**Specific Driver Class Spec Major Version

Property of [niDMM](cnidmm.html)

The major version number of the class specification for the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverclassspecminorversion.html language=enus -->
## TOPIC 00070: Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverclassspecminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverclassspecminorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version Property

**Short Name:**Specific Driver Class Spec Minor Version

Property of [niDMM](cnidmm.html)

The minor version number of the class specification for the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverdescription.html language=enus -->
## TOPIC 00071: Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverdescription.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverdescription.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description Property

**Short Name:**Specific Driver Description

Property of [niDMM](cnidmm.html)

A string containing a description of the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdrivermajorversion.html language=enus -->
## TOPIC 00072: Inherent IVI Attributes:Version Info:Specific Driver Major Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdrivermajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdrivermajorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Version Info:Specific Driver Major Version Property

**Short Name:**Specific Driver Major Version

Property of [niDMM](cnidmm.html)

Returns the major version number of this instrument driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverminorversion.html language=enus -->
## TOPIC 00073: Inherent IVI Attributes:Version Info:Specific Driver Minor Version Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverminorversion.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Version Info:Specific Driver Minor Version Property

**Short Name:**Specific Driver Minor Version

Property of [niDMM](cnidmm.html)

Returns the minor version number of this instrument driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverprefix.html language=enus -->
## TOPIC 00074: Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverprefix.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix Property

**Short Name:**Specific Driver Prefix

Property of [niDMM](cnidmm.html)

The prefix for the specific instrument driver. The name of each user-callable VI in this driver starts with this prefix. The prefix can be up to a maximum of eight characters.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdriverrevision.html language=enus -->
## TOPIC 00075: Inherent IVI Attributes:Version Info:Specific Driver Revision Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdriverrevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdriverrevision.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Version Info:Specific Driver Revision Property

**Short Name:**Specific Driver Revision

Property of [niDMM](cnidmm.html)

A string that contains additional version information about this instrument driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_specificdrivervendor.html language=enus -->
## TOPIC 00076: Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_specificdrivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_specificdrivervendor.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor Property

**Short Name:**Specific Driver Vendor

Property of [niDMM](cnidmm.html)

A string containing the vendor of the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_supportedinstrumentmodels.html language=enus -->
## TOPIC 00077: Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_supportedinstrumentmodels.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models Property

**Short Name:**Supported Instrument Models

Property of [niDMM](cnidmm.html)

A string containing the instrument models supported by the specific driver.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_susceptance.html language=enus -->
## TOPIC 00078: Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_susceptance.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_susceptance.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance Property

**Short Name:**Susceptance

Property of [niDMM](cnidmm.html)

For the NI 4082 and NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation. The valid range is any real number >0. The default value (-1.0) indicates that compensation has not taken place.

|  | Note Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Open Cable Comp Values |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_tcfixedrefjunction.html language=enus -->
## TOPIC 00079: Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_tcfixedrefjunction.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_tcfixedrefjunction.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction Property

**Short Name:**TC Fixed Ref Junction

Property of [niDMM](cnidmm.html)

Specifies the value of the fixed reference junction temperature for a thermocouple in degrees Celsius.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_tcrefjunctiontype.html language=enus -->
## TOPIC 00080: Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_tcrefjunctiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_tcrefjunctiontype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type Property

**Short Name:**TC Ref Junction Type

Property of [niDMM](cnidmm.html)

Specifies the thermocouple reference junction type.

| Fixed (2) | Thermocouple reference juction is fixed at the user-specified temperature. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_thermistora.html language=enus -->
## TOPIC 00081: Configuration:Measurement Options:Temperature:Thermistor:Thermistor A Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_thermistora.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_thermistora.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor A Property

**Short Name:**Thermistor A

Property of [niDMM](cnidmm.html)

Specifies the Steinhart-Hart A coefficient for thermistor scaling when the **Thermistor Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_thermistorb.html language=enus -->
## TOPIC 00082: Configuration:Measurement Options:Temperature:Thermistor:Thermistor B Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_thermistorb.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_thermistorb.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor B Property

**Short Name:**Thermistor B

Property of [niDMM](cnidmm.html)

Specifies the Steinhart-Hart B coefficient for thermistor scaling when the **Thermistor Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_thermistorc.html language=enus -->
## TOPIC 00083: Configuration:Measurement Options:Temperature:Thermistor:Thermistor C Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_thermistorc.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_thermistorc.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor C Property

**Short Name:**Thermistor C

Property of [niDMM](cnidmm.html)

Specifies the Steinhart-Hart C coefficient for thermistor scaling when the **Thermistor Type property** is set to Custom.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_thermistortype.html language=enus -->
## TOPIC 00084: Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_thermistortype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_thermistortype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type Property

**Short Name:**Thermistor Type

Property of [niDMM](cnidmm.html)

Specifies the thermistor type.

| Custom (0) | Performs Steinhart-Hart thermistor scaling with the user-specified A, B, and C coefficients. |
| --- | --- |
| 44004 (1) | Performs scaling for an Omega Series 44004 thermistor. |
| 44006 (2) | Performs scaling for an Omega Series 44006 thermistor. |
| 44007 (3) | Performs scaling for an Omega Series 44007 thermistor. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_thermocoupletype.html language=enus -->
## TOPIC 00085: Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_thermocoupletype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type Property

**Short Name:**Thermocouple Type

Property of [niDMM](cnidmm.html)

Specifies the thermocouple type.

| B (1) | Thermocouple type B |
| --- | --- |
| E (4) | Thermocouple type E |
| J (6) | Thermocouple type J |
| K (7) | Thermocouple type K |
| N (8) | Thermocouple type N |
| R (9) | Thermocouple type R |
| S (10) | Thermocouple type S |
| T (11) | Thermocouple type T |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_transducertype.html language=enus -->
## TOPIC 00086: Configuration:Measurement Options:Temperature:Transducer Type Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_transducertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_transducertype.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Configuration:Measurement Options:Temperature:Transducer Type Property

**Short Name:**Transducer Type

Property of [niDMM](cnidmm.html)

Specifies the transducer type.

| Thermocouple (1) | Use for thermocouple measurements. |
| --- | --- |
| Thermistor (2) | Use for thermistor measurements. |
| 2-Wire RTD (3) | Use for 2-wire RTD measurements. |
| 4-Wire RTD (4) | Use for 4-wire RTD measurements. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_triggercount.html language=enus -->
## TOPIC 00087: Multi Point Acquisition:Trigger Count Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_triggercount.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_triggercount.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Multi Point Acquisition:Trigger Count Property

**Short Name:**Trigger Count

Property of [niDMM](cnidmm.html)

Specifies the number of triggers the DMM receives before returning to the Idle state. This property can be set to any positive ViInt32 value for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

Refer to [Multiple Point Acquisitions](/csh?topicname=dmm/multi_point.html) in the *NI Digital Multimeters Help*for more information.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Multi Point |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_triggerdelay.html language=enus -->
## TOPIC 00088: Trigger:Trigger Delay Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_triggerdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_triggerdelay.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Trigger:Trigger Delay Property

**Short Name:**Trigger Delay

Property of [niDMM](cnidmm.html)

Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement. The default value is Auto Delay (-1), which means that the DMM waits an appropriate settling time before taking the measurement.

The NI 4080/4081/4082 uses the value specified in this property as additional settling time. The valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is 10.0 ns.

The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time. For these devices, the valid range for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the onboard timing resolution is 34.72 ns.

Use positive values to set the trigger delay in seconds.

Valid Range: Auto Delay (-1.0), 0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

Default Value: Auto Delay

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Trigger |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_triggerslope.html language=enus -->
## TOPIC 00089: Trigger:Trigger Slope Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_triggerslope.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_triggerslope.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Trigger:Trigger Slope Property

**Short Name:**Trigger Slope

Property of [niDMM](cnidmm.html)

Specifies the edge of the signal from the specified trigger source on which the DMM is triggered.

| Positive (0) | The driver triggers on the rising edge of the trigger signal. |
| --- | --- |
| Negative (1) | The driver triggers on the falling edge of the trigger signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Sample Trigger Slope, niDMM Configure Trigger Slope |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_triggersource.html language=enus -->
## TOPIC 00090: Trigger:Trigger Source Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_triggersource.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_triggersource.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Trigger:Trigger Source Property

**Short Name:**Trigger Source

Property of [niDMM](cnidmm.html)

Specifies the trigger source. When [niDMM Initiate](/csh?topicname=dmmviref/nidmm_initiate.html) is called, the DMM waits for the trigger specified with this property. After it receives the trigger, the DMM waits the length of time specified with the [Trigger Delay](pnidmm_triggerdelay.html) property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the [LabVIEW Trigger Routing](/csh?topicname=dmm/lvtrigger_routing.html) section in the *NI Digital Multimeters Help*.

| Immediate (1) | No trigger specified. |
| --- | --- |
| External (2) | Pin 9 on the AUX Connector |
| Software Trig (3) | Waits until niDMM Send Software Trigger is called. |
| TTL 0 (111) | PXI Trigger Line 0 |
| TTL 1 (112) | PXI Trigger Line 1 |
| TTL 2 (113) | PXI Trigger Line 2 |
| TTL 3 (114) | PXI Trigger Line 3 |
| TTL 4 (115) | PXI Trigger Line 4 |
| TTL 5 (116) | PXI Trigger Line 5 |
| TTL 6 (117) | PXI Trigger Line 6 |
| TTL 7 (118) | PXI Trigger Line 7 |
| PXI Star (131) | PXI Star Trigger Line |
| LBR Trig 1 (1004) | Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis |
| AUX_Trig 1 (1001) | Pin 3 on the AUX connector |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Trigger |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_waveformcoupling.html language=enus -->
## TOPIC 00091: Waveform Acquisition:Waveform Coupling Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_waveformcoupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_waveformcoupling.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Waveform Acquisition:Waveform Coupling Property

**Short Name:**Waveform Coupling

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.

| AC (0) | Specifies AC coupling. |
| --- | --- |
| DC (1) | Specifies DC coupling. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Waveform Coupling |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_waveformpoints.html language=enus -->
## TOPIC 00092: Waveform Acquisition:Waveform Points Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_waveformpoints.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_waveformpoints.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Waveform Acquisition:Waveform Points Property

**Short Name:**Waveform Points

Property of [niDMM](cnidmm.html)

For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of points to acquire in a waveform acquisition.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Waveform Acquisition |
| Resettable | No |

<!--NI_TOPIC bundle=ni-dmm-properties path=dmmpropref/pnidmm_waveformrate.html language=enus -->
## TOPIC 00093: Waveform Acquisition:Waveform Rate Property

- bundle_id: `ni-dmm-properties`
- source_path: `dmmpropref/pnidmm_waveformrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-dmm-properties/raw/resource/enus/dmmpropref/pnidmm_waveformrate.html
- document_id: `ni-dmm-properties`
- page_type: `leaf`
- content_type: ``

### Waveform Acquisition:Waveform Rate Property

**Short Name:**Waveform Rate

Property of [niDMM](cnidmm.html)

Specifies the rate of the waveform acquisition in samples per second (S/s). The valid rate is calculated by dividing 1,800,000 by an integer divisor, and the rate falls between 10 and 1,800,000 samples per second. The waveform rate is coerced upwards to the next valid rate. The default value is 1,800,000 samples per second. Not supported by NI 4065.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niDMM Configure Waveform Acquisition |
| Resettable | No |
