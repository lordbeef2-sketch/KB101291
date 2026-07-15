# NI DOCUMENT BUNDLE: ni-switch-properties

<!--NI_BUNDLE_CHUNK bundle=ni-switch-properties start=1 end=66 -->
<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/cniswitch.html language=enus -->
## TOPIC 00001: niSwitch Properties

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/cniswitch.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/cniswitch.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### niSwitch Properties

August 2013

Use the NI-SWITCH properties to access advanced configuration options for switch applications.

© 2007–2013 National Instruments. All rights reserved.

| Property | Description |
| --- | --- |
| Active Channel | Specifies the channel name the instrument driver uses to access all subsequent channel-based properties in this property node. Set the active channel before setting channel-based properties. Details |
| Channel Configuration:Is Configuration Channel | Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. The instrument driver uses configuration channels to create paths between the channels you specify in the niSwitch Connect Channels VI. Details |
| Channel Configuration:Is Source Channel | Specifies whether to designate the channel as a source channel. Details |
| Channel Configuration:Analog Bus Sharing Enable | Enables or disables sharing of an analog bus line so that multiple NI SwitchBlock devices may connect to it simultaneously. To enable multiple NI SwitchBlock devices to share an analog bus line, set this property to TRUE for each device on the channel that corresponds with the shared analog bus line. The default value for all devices is FALSE, which disables sharing of the analog bus. Details |
| Inherent IVI Attributes:Advanced Session Information:Driver Setup | Contains the Driver Setup string that you specified when initializing the instrument driver. Details |
| Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor | Contains the resource descriptor the instrument driver uses to identify the physical device. Details |
| Inherent IVI Attributes:Advanced Session Information:Logical Name | Contains the logical name you specified when opening the current IVI session. Details |
| Inherent IVI Attributes:Driver Capabilities:Channel Count | Contains the number of channels that the instrument driver supports. Details |
| Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities | Contains a comma-separated (,) list of class-extension groups that the instrument driver implements. Details |
| Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models | Contains a comma-separated (,) list of supported instrument models. Details |
| Inherent IVI Attributes:Driver Identification:Class Specification Major Version | Contains the major version number of the IviSwtch class specification. Details |
| Inherent IVI Attributes:Driver Identification:Class Specification Minor Version | Contains the minor version number of the class specification with which the instrument driver is compliant. Details |
| Inherent IVI Attributes:Driver Identification:Description | Contains a brief description of the instrument driver. Details |
| Inherent IVI Attributes:Driver Identification:Driver Prefix | Contains the prefix for all of the instrument driver VIs. Details |
| Inherent IVI Attributes:Driver Identification:Driver Vendor | Contains the name of the vendor that supplies the instrument driver. Details |
| Inherent IVI Attributes:Driver Identification:Revision | Contains additional version information about the instrument driver. Details |
| Inherent IVI Attributes:Instrument Identification:Firmware Revision | Contains the firmware revision information for the instrument currently in use. Details |
| Inherent IVI Attributes:Instrument Identification:Manufacturer | Contains the name of the manufacturer of the instrument currently in use. Details |
| Inherent IVI Attributes:Instrument Identification:Model | Contains the model number or name of the instrument currently in use. Details |
| Inherent IVI Attributes:User Options:Cache | Specifies whether to cache the value of properties. The default value is TRUE. Use the niSwitch Initialize With Options VI to override the default value. Details |
| Inherent IVI Attributes:User Options:Interchange Check | Specifies whether to perform interchangeability checking and retrieve interchangeability warnings when you call the niSwitch Connect Channels, niSwitch Set Path and niSwitch Initiate Scan VIs. The default value is FALSE. Details |
| Inherent IVI Attributes:User Options:Query Instrument Status | Specifies whether the instrument driver queries the instrument status after each operation. The default value is TRUE. Use the niSwitch Initialize With Options VI to override the default value. Details |
| Inherent IVI Attributes:User Options:Range Check | Specifies whether to validate property values and VI parameters. The default value is TRUE. Use the niSwitch Initialize With Options VI to override the default value. Details |
| Inherent IVI Attributes:User Options:Record Value Coercions | Specifies whether the IVI engine keeps a list of the value coercions it makes for properties with ViInt32 and ViReal64 datatypes. The default value is FALSE. Use the niSwitch Initialize With Options VI to override the default value. Details |
| Inherent IVI Attributes:User Options:Simulate | Specifies whether to simulate instrument driver I/O operations. The default value is FALSE. Use the niSwitch Initialize With Options VI to override the default value. Details |
| Matrix Configuration:Number of Columns | Returns the number of channels on the column of a matrix or scanner. If the switch module is a scanner, this property returns the number of input channels. Details |
| Matrix Configuration:Number of Rows | Returns the number of channels on the row of a matrix or scanner. If the switch module is a scanner, this property returns the number of output channels. Details |
| Module Characteristics:Bandwidth | Returns the bandwidth for the channel in hertz. Details |
| Module Characteristics:Characteristic Impedance | Returns the characteristic impedance for the channel in ohms. Details |
| Module Characteristics:Is Debounced | Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid. Details |
| Module Characteristics:Maximum AC Voltage | Returns the maximum AC voltage the channel can switch in volts RMS. Details |
| Module Characteristics:Maximum Carry AC Current | Returns the maximum AC current the channel can carry in amperes RMS. Details |
| Module Characteristics:Maximum Carry AC Power | Returns the maximum AC power the channel can carry in volt-amperes. Details |
| Module Characteristics:Maximum Carry DC Current | Returns the maximum DC current the channel can carry in amperes. Details |
| Module Characteristics:Maximum Carry DC Power | Returns the maximum DC power the channel can carry in watts. Details |
| Module Characteristics:Maximum DC Voltage | Returns the maximum DC voltage the channel can switch in volts. Details |
| Module Characteristics:Maximum Switching AC Current | Returns the maximum AC current the channel can switch in amperes RMS. Details |
| Module Characteristics:Maximum Switching AC Power | Returns the maximum AC power the channel can switch in volt-amperes. Details |
| Module Characteristics:Maximum Switching DC Current | Returns the maximum DC current the channel can switch in amperes. Details |
| Module Characteristics:Maximum Switching DC Power | Returns the maximum DC power the channel can switch in watts. Details |
| Module Characteristics:Number of Relays | Returns the number of relays that the instrument driver supports. Details |
| Module Characteristics:Power Down Latching Relays After Debounce | Specifies whether to power down latching relays after calling the niSwitch Wait For Debounce VI. Set this property to TRUE to ensure that the relays settle and the latching relays power down after you call the niSwitch Wait for Debounce VI. Details |
| Module Characteristics:Serial Number | Returns the serial number for the switch module controlled by the instrument driver. If the switch module does not return a serial number, the instrument driver returns the Invalid Attribute error. Details |
| Module Characteristics:Settling Time | Returns the maximum length of time in seconds from after you make a connection until the signal flowing through the channel settles. Settling time can vary depending on the switch module. Details |
| Module Characteristics:Temperature | Returns the temperature as read by the Switch module in degrees Celsius. Refer to the device documentation for more information. Details |
| Module Characteristics:Wire mode | Returns the wire mode of the switch module. This property affects the values of the Number of Rows and Number of Columns properties. The actual number of input and output lines on the switch module does not change, but the number of channels depends on how many lines constitute each channel. Details |
| Scanning Configuration:Continuous Scan | Specifies whether to continuously scan through a scan list. Set the property to FALSE to stop scanning after one pass through the scan list. Set this property to TRUE to loop continuously through the scan list. Details |
| Scanning Configuration:Digital Filter Enable | Specifies whether to apply the pulse width filter to the Trigger Input. Set the property to TRUE to prevent the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0-7. Details |
| Scanning Configuration:Handshaking Initiation | Specifies how to start handshaking with a measurement device. Details |
| Scanning Configuration:Is Scanning | Indicates whether the switch module has completed the scan operation. TRUE indicates that the scan has completed. Details |
| Scanning Configuration:Is Waiting for Trigger? | Indicates with a semi-colon (;) that at that point in the scan list, the scan engine should pause until a trigger is received from the trigger input. If you generate that trigger through either a hardware pulse or the niSwitch Send Software Trigger VI, you must know when the scan engine has reached such a state. Details |
| Scanning Configuration:Scan Advanced Output | Specifies the method to use to notify another instrument that all signals through the switch module have settled following the processing of one entry in the scan list. Details |
| Scanning Configuration:Scan Advanced Polarity | Specifies the driving level for the Scan Advanced Output signal sent from the switch module through either the external (PXI/PXIe) or front connector (SCXI) lines. When the Scan Advanced Output signal is sent to one of the PXI_Trig lines, the driven level is always low and this property is ignored. Between each Scan Advanced Output signal, the line is not driven and is in a high-impedance state. Details |
| Scanning Configuration:Scan Delay | Specifies the minimum amount of time the switch module waits before it asserts the scan advanced output trigger after opening or closing the switch. The switch module always waits for debounce before asserting the trigger. Thus, the actual delay will always be the greater value of the settling time and the value you specify as the switch delay, measured in seconds. Settling time can vary depending on the switch module. Details |
| Scanning Configuration:Scan List | Contains a scan list (a string that specifies channel connections and trigger conditions). The niSwitch Initiate Scan VI makes or breaks connections and waits for triggers according to the instructions in the scan list. The scan list is comprised of channel names separated by special characters that determine the operations the scanner performs on the channels when it executes the scan list. Details |
| Scanning Configuration:Scan Mode | Specifies how to handle existing connections that conflict with the connections you make in a scan list. For example, if CH1 is already connected to CH2 and the scan list instructs the switch module to connect CH1 to CH3, this property specifies what happens to the connection between CH1 and CH2. Details |
| Scanning Configuration:Trigger Input | Specifies the source of the trigger for which the switch module can wait upon encountering a semi-colon (;) when processing a scan list. When the trigger occurs, the switch module advances to the next entry in the scan list. Details |
| Scanning Configuration:Trigger Input Polarity | Determines the behavior of the trigger input. Details |
| Obsolete Attributes:Cabled Module Scan Advanced Bus | This property has been deprecated and might be removed from a future release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI instead. Details |
| Obsolete Attributes:Cabled Module Trigger Bus | This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead. Details |
| Obsolete Attributes:Master Slave Scan Advanced Bus | This property has been deprecated and might be removed from a future release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI instead. Details |
| Obsolete Attributes:Master Slave Trigger Bus | This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead. Details |
| Obsolete Attributes:Parsed Scan List | This property has been deprecated and might be removed from a future release of NI-SWITCH. Details |
| Obsolete Attributes:Serial Number | This property has been deprecated and might be removed from a future release of NI-SWITCH. Details |
| Obsolete Attributes:Trigger Mode | This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the niSwitch Route Trigger Input and/or niSwitch Route Scan Advanced Output VIs instead. Details |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_activechannel.html language=enus -->
## TOPIC 00002: Active Channel Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_activechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_activechannel.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Active Channel Property

**Short Name:**Active Channel

Property of [niSwitch](cniswitch.html)

Specifies the channel name the instrument driver uses to access all subsequent channel-based properties in this property node. Set the active channel before setting channel-based properties.

Wire a name that the instrument driver defines or a virtual channel name configured in Measurement and Automation Explorer (MAX).

**Related topics**

- niSwitch Properties
- Setting and Checking Properties and Attributes

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_analogbussharingenable.html language=enus -->
## TOPIC 00003: Channel Configuration:Analog Bus Sharing Enable Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_analogbussharingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_analogbussharingenable.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Channel Configuration:Analog Bus Sharing Enable Property

**Short Name:**Analog Bus Sharing Enable

Property of [niSwitch](cniswitch.html)

Enables or disables sharing of an analog bus line so that multiple NI SwitchBlock devices may connect to it simultaneously. To enable multiple NI SwitchBlock devices to share an analog bus line, set this property to TRUE for each device on the channel that corresponds with the shared analog bus line. The default value for all devices is FALSE, which disables sharing of the analog bus.

**Related topics**

- niSwitch Properties
- Using the Analog Bus on an NI SwitchBlock Carrier

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_bandwidth.html language=enus -->
## TOPIC 00004: Module Characteristics:Bandwidth Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_bandwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_bandwidth.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Bandwidth Property

**Short Name:**Bandwidth

Property of [niSwitch](cniswitch.html)

Returns the bandwidth for the channel in hertz.

**Related topics**

- Bandwidth and Insertion Loss
- niSwitch Properties
- RF Switching Considerations

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_cabledmodulescanadvancedbus.html language=enus -->
## TOPIC 00005: Obsolete Attributes:Cabled Module Scan Advanced Bus Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_cabledmodulescanadvancedbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_cabledmodulescanadvancedbus.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Cabled Module Scan Advanced Bus Property

**Short Name:**Cabled Module Scan Advanced Bus

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use [niSwitch Route Scan Advanced Output](/csh?topicname=switchviref/niswitch_route_scan_advanced_output.html) VI instead.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_cabledmoduletriggerbus.html language=enus -->
## TOPIC 00006: Obsolete Attributes:Cabled Module Trigger Bus Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_cabledmoduletriggerbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_cabledmoduletriggerbus.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Cabled Module Trigger Bus Property

**Short Name:**Cabled Module Trigger Bus

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the [niSwitch Route Trigger Input](/csh?topicname=switchviref/niswitch_route_trigger_input.html) VI instead.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_cache.html language=enus -->
## TOPIC 00007: Inherent IVI Attributes:User Options:Cache Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_cache.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_cache.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Cache Property

**Short Name:**Cache

Property of [niSwitch](cniswitch.html)

Specifies whether to cache the value of properties. The default value is TRUE. Use the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI to override the default value.

Set this property to TRUE to ensure the instrument driver tracks the current instrument settings and avoid sending redundant commands to the instrument.
 The instrument driver can always cache or never cache regardless of the setting of this property.

**Related topics**

- niSwitch Initialize With Options
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_channelcount.html language=enus -->
## TOPIC 00008: Inherent IVI Attributes:Driver Capabilities:Channel Count Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_channelcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_channelcount.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Capabilities:Channel Count Property

**Short Name:**Channel Count

Property of [niSwitch](cniswitch.html)

Contains the number of channels that the instrument driver supports.

**Related topics**

- niSwitch Get Channel Name
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_characteristicimpedance.html language=enus -->
## TOPIC 00009: Module Characteristics:Characteristic Impedance Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_characteristicimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_characteristicimpedance.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Characteristic Impedance Property

**Short Name:**Characteristic Impedance

Property of [niSwitch](cniswitch.html)

Returns the characteristic impedance for the channel in ohms.

**Related topics**

- Characteristic Impedance
- niSwitch Properties
- RF Switching Considerations

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_classgroupcapabilities.html language=enus -->
## TOPIC 00010: Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_classgroupcapabilities.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_classgroupcapabilities.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities Property

**Short Name:**Class Group Capabilities

Property of [niSwitch](cniswitch.html)

Contains a comma-separated (,) list of class-extension groups that the instrument driver implements.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_classspecificationmajorversion.html language=enus -->
## TOPIC 00011: Inherent IVI Attributes:Driver Identification:Class Specification Major Version Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_classspecificationmajorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_classspecificationmajorversion.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Class Specification Major Version Property

**Short Name:**Class Specification Major Version

Property of [niSwitch](cniswitch.html)

Contains the major version number of the IviSwtch class specification.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_classspecificationminorversion.html language=enus -->
## TOPIC 00012: Inherent IVI Attributes:Driver Identification:Class Specification Minor Version Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_classspecificationminorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_classspecificationminorversion.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Class Specification Minor Version Property

**Short Name:**Class Specification Minor Version

Property of [niSwitch](cniswitch.html)

Contains the minor version number of the class specification with which the instrument driver is compliant.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_continuousscan.html language=enus -->
## TOPIC 00013: Scanning Configuration:Continuous Scan Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_continuousscan.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_continuousscan.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Continuous Scan Property

**Short Name:**Continuous Scan

Property of [niSwitch](cniswitch.html)

Specifies whether to continuously scan through a scan list. Set the property to FALSE to stop scanning after one pass through the scan list. Set this property to TRUE to loop continuously through the scan list.

If you set the property to TRUE, the [niSwitch Wait For Scan To Complete](/csh?topicname=switchviref/niswitch_wait_for_scan_to_complete.html) VI times out, and you must call the [niSwitch Abort Scan](/csh?topicname=switchviref/niswitch_abort_scan.html) VI to stop the scan.

**Related topics**

- niSwitch Properties
- Scanning

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_description.html language=enus -->
## TOPIC 00014: Inherent IVI Attributes:Driver Identification:Description Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_description.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_description.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Description Property

**Short Name:**Description

Property of [niSwitch](cniswitch.html)

Contains a brief description of the instrument driver.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_digitalfilterenable.html language=enus -->
## TOPIC 00015: Scanning Configuration:Digital Filter Enable Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_digitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_digitalfilterenable.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Digital Filter Enable Property

**Short Name:**Digital Filter Enable

Property of [niSwitch](cniswitch.html)

Specifies whether to apply the pulse width filter to the Trigger Input. Set the property to TRUE to prevent the switch module from being triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.

When this property is set to FALSE, noise on the PXI trigger lines might trigger the switch module. If the device triggering the switch module can send pulses greater than 150 ns, do not disable this property.

**Related topics**

- Disabling Digital Filtering
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_driverprefix.html language=enus -->
## TOPIC 00016: Inherent IVI Attributes:Driver Identification:Driver Prefix Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_driverprefix.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_driverprefix.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Driver Prefix Property

**Short Name:**Driver Prefix

Property of [niSwitch](cniswitch.html)

Contains the prefix for all of the instrument driver VIs.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_driversetup.html language=enus -->
## TOPIC 00017: Inherent IVI Attributes:Advanced Session Information:Driver Setup Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_driversetup.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_driversetup.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Advanced Session Information:Driver Setup Property

**Short Name:**Driver Setup

Property of [niSwitch](cniswitch.html)

Contains the Driver Setup string that you specified when initializing the instrument driver.

In some cases, you must specify instrument driver options at initialization time—for example, when specifying a particular instrument model from among a family of instruments that the instrument driver supports. This is useful when using simulation.

You can specify instrument driver-specific options through the DriverSetup keyword in the **option string** parameter of the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI, or through the IVI Configuration Utility. If you did not specify a Driver Setup string, this property returns an empty string.

**Related topics**

- niSwitch Initialize With Options
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_drivervendor.html language=enus -->
## TOPIC 00018: Inherent IVI Attributes:Driver Identification:Driver Vendor Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_drivervendor.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Driver Vendor Property

**Short Name:**Driver Vendor

Property of [niSwitch](cniswitch.html)

Contains the name of the vendor that supplies the instrument driver.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_firmwarerevision.html language=enus -->
## TOPIC 00019: Inherent IVI Attributes:Instrument Identification:Firmware Revision Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_firmwarerevision.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_firmwarerevision.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Firmware Revision Property

**Short Name:**Firmware Revision

Property of [niSwitch](cniswitch.html)

Contains the firmware revision information for the instrument currently in use.

**Related topics**

- niSwitch Properties
- niSwitch Revision Query

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_handshakinginitiation.html language=enus -->
## TOPIC 00020: Scanning Configuration:Handshaking Initiation Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_handshakinginitiation.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_handshakinginitiation.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Handshaking Initiation Property

**Short Name:**Handshaking Initiation

Property of [niSwitch](cniswitch.html)

Specifies how to start handshaking with a measurement device.

**Related topics**

- Handshaking
- niSwitch Properties
- Scanning

| Switch_Initiated (1) | The niSwitch Initiate Scan VI returns immediately after beginning scan list execution. It is assumed that the measurement device has already been configured and is waiting for the scanner advanced signal. The measurement should be configured to first wait for a trigger, then take a measurement. Thus, the first scanner advanced output signal of the switch module initiates handshaking. |
| --- | --- |
| Measurement_Device_Initiated (0) | The niSwitch Initiate Scan VI does not return until the switch hardware is waiting for a trigger input. This ensures that if you initiate the measurement device after calling the niSwitch Initiate Scan VI , the switch is sure to receive the first measurement complete (MC) signal sent by the measurement device. The measurement device should be configured to first take a measurement, send MC, then wait for scanner advanced output signal. Thus, the first MC of the measurement device initiates handshaking. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_interchangecheck.html language=enus -->
## TOPIC 00021: Inherent IVI Attributes:User Options:Interchange Check Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_interchangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_interchangecheck.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Interchange Check Property

**Short Name:**Interchange Check

Property of [niSwitch](cniswitch.html)

Specifies whether to perform interchangeability checking and retrieve interchangeability warnings when you call the [niSwitch Connect Channels](/csh?topicname=switchviref/niswitch_connect_channels.html), [niSwitch Set Path](/csh?topicname=switchviref/niswitch_set_path.html) and [niSwitch Initiate Scan](/csh?topicname=switchviref/niswitch_initiate_scan.html) VIs. The default value is FALSE.

Interchangeability checking examines the properties in a capability group only if you specify a value for at least one property within that group. Interchangeability warnings can occur when a property that you have not set or that has been invalidated affects the behavior of the instrument.

Interchangeability warnings indicate that using your application with a different instrument might cause different behavior. Call [niSwitch Get Next Interchange Warning](/csh?topicname=switchviref/niswitch_get_next_interchange_warning.html) VI to extract interchange warnings. Call the [niSwitch Clear Interchange Warnings](/csh?topicname=switchviref/niswitch_clear_interchange_warnings.html) VI to clear the list of interchangeability warnings without reading them.

**Related topics**

- niSwitch Get Next Interchange Warning
- niSwitch Properties
- niSwitch Reset Interchange Check

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_ioresourcedescriptor.html language=enus -->
## TOPIC 00022: Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_ioresourcedescriptor.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_ioresourcedescriptor.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor Property

**Short Name:**IO Resource Descriptor

Property of [niSwitch](cniswitch.html)

Contains the resource descriptor the instrument driver uses to identify the physical device.

If you initialize the instrument driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration Utility. If you initialize the instrument driver with the resource descriptor, this property contains that value.

**Related topics**

- Initialization
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_isconfigurationchannel.html language=enus -->
## TOPIC 00023: Channel Configuration:Is Configuration Channel Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_isconfigurationchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_isconfigurationchannel.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Channel Configuration:Is Configuration Channel Property

**Short Name:**Is Configuration Channel

Property of [niSwitch](cniswitch.html)

Specifies whether to designate the channel as a configuration channel—a channel reserved for internal path creation. The instrument driver uses configuration channels to create paths between the channels you specify in the [niSwitch Connect Channels](/csh?topicname=switchviref/niswitch_connect_channels.html) VI.

Set this property to TRUE to designate the channel as a configuration channel. Set this property to FALSE to designate the channel as available for external connections.
 Because you cannot use a configuration channel for external connections, the [niSwitch Connect Channels](/csh?topicname=switchviref/niswitch_connect_channels.html) VI returns the Is Configuration Channel error when you attempt to establish a connection between a configuration channel and any other channel.

**Related topics**

- niSwitch Properties
- Setting Source and Configuration Channels

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_isdebounced.html language=enus -->
## TOPIC 00024: Module Characteristics:Is Debounced Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_isdebounced.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_isdebounced.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Is Debounced Property

**Short Name:**Is Debounced

Property of [niSwitch](cniswitch.html)

Indicates whether the entire switch module has settled since the last switching command. A value of TRUE indicates that all signals going through the switch module are valid.

**Related topics**

- Electromechanical Relays
- niSwitch Properties
- Settling Time

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_isscanning.html language=enus -->
## TOPIC 00025: Scanning Configuration:Is Scanning Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_isscanning.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_isscanning.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Is Scanning Property

**Short Name:**Is Scanning

Property of [niSwitch](cniswitch.html)

Indicates whether the switch module has completed the scan operation. TRUE indicates that the scan has completed.

**Related topics**

- niSwitch Properties
- Scanning

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_issourcechannel.html language=enus -->
## TOPIC 00026: Channel Configuration:Is Source Channel Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_issourcechannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_issourcechannel.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Channel Configuration:Is Source Channel Property

**Short Name:**Is Source Channel

Property of [niSwitch](cniswitch.html)

Specifies whether to designate the channel as a source channel.

Set this property to TRUE when you connect the channel to a power supply, a function generator, or an active measurement point on the unit under test, and you do not want to connect the channel to another source. The instrument driver prevents source channels from connecting to each other: when you attempt to connect two source channels, the [niSwitch Connect Channels](/csh?topicname=switchviref/niswitch_connect_channels.html) VI returns the Attempt To Connect Sources error.

**Related topics**

- niSwitch Properties
- Setting Source and Configuration Channels

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_iswaitingfortrigger.html language=enus -->
## TOPIC 00027: Scanning Configuration:Is Waiting for Trigger? Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_iswaitingfortrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_iswaitingfortrigger.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Is Waiting for Trigger? Property

**Short Name:**Is Waiting for Trigger?

Property of [niSwitch](cniswitch.html)

Indicates with a semi-colon (;) that at that point in the scan list, the scan engine should pause until a trigger is received from the trigger input. If you generate that trigger through either a hardware pulse or the [niSwitch Send Software Trigger](/csh?topicname=switchviref/niswitch_send_software_trigger.html) VI, you must know when the scan engine has reached such a state.

**Related topics**

- niSwitch Configure Scan Trigger
- niSwitch Properties
- Scanning

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_logicalname.html language=enus -->
## TOPIC 00028: Inherent IVI Attributes:Advanced Session Information:Logical Name Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_logicalname.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Advanced Session Information:Logical Name Property

**Short Name:**Logical Name

Property of [niSwitch](cniswitch.html)

Contains the logical name you specified when opening the current IVI session.

You can wire a logical name to the [niSwitch Initialize](/csh?topicname=switchviref/niswitch_initialize.html) or the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VIs. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section, which specifies a physical device and initial user options, in the IVI Configuration file.

**Related topics**

- Initialization
- niSwitch Properties
- Using NI Switches in IVI

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_manufacturer.html language=enus -->
## TOPIC 00029: Inherent IVI Attributes:Instrument Identification:Manufacturer Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_manufacturer.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_manufacturer.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Manufacturer Property

**Short Name:**Manufacturer

Property of [niSwitch](cniswitch.html)

Contains the name of the manufacturer of the instrument currently in use.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_masterslavescanadvancedbus.html language=enus -->
## TOPIC 00030: Obsolete Attributes:Master Slave Scan Advanced Bus Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_masterslavescanadvancedbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_masterslavescanadvancedbus.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Master Slave Scan Advanced Bus Property

**Short Name:**Master Slave Scan Advanced Bus

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use [niSwitch Route Scan Advanced Output](/csh?topicname=switchviref/niswitch_route_scan_advanced_output.html) VI instead.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_masterslavetriggerbus.html language=enus -->
## TOPIC 00031: Obsolete Attributes:Master Slave Trigger Bus Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_masterslavetriggerbus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_masterslavetriggerbus.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Master Slave Trigger Bus Property

**Short Name:**Master Slave Trigger Bus

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the [niSwitch Route Trigger Input](/csh?topicname=switchviref/niswitch_route_trigger_input.html) VI instead.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumacvoltage.html language=enus -->
## TOPIC 00032: Module Characteristics:Maximum AC Voltage Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumacvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumacvoltage.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum AC Voltage Property

**Short Name:**Maximum AC Voltage

Property of [niSwitch](cniswitch.html)

Returns the maximum AC voltage the channel can switch in volts RMS.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumcarryaccurrent.html language=enus -->
## TOPIC 00033: Module Characteristics:Maximum Carry AC Current Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumcarryaccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumcarryaccurrent.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Carry AC Current Property

**Short Name:**Maximum Carry AC Current

Property of [niSwitch](cniswitch.html)

Returns the maximum AC current the channel can carry in amperes RMS.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumcarryacpower.html language=enus -->
## TOPIC 00034: Module Characteristics:Maximum Carry AC Power Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumcarryacpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumcarryacpower.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Carry AC Power Property

**Short Name:**Maximum Carry AC Power

Property of [niSwitch](cniswitch.html)

Returns the maximum AC power the channel can carry in volt-amperes.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumcarrydccurrent.html language=enus -->
## TOPIC 00035: Module Characteristics:Maximum Carry DC Current Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumcarrydccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumcarrydccurrent.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Carry DC Current Property

**Short Name:**Maximum Carry DC Current

Property of [niSwitch](cniswitch.html)

Returns the maximum DC current the channel can carry in amperes.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumcarrydcpower.html language=enus -->
## TOPIC 00036: Module Characteristics:Maximum Carry DC Power Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumcarrydcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumcarrydcpower.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Carry DC Power Property

**Short Name:**Maximum Carry DC Power

Property of [niSwitch](cniswitch.html)

Returns the maximum DC power the channel can carry in watts.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumdcvoltage.html language=enus -->
## TOPIC 00037: Module Characteristics:Maximum DC Voltage Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumdcvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumdcvoltage.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum DC Voltage Property

**Short Name:**Maximum DC Voltage

Property of [niSwitch](cniswitch.html)

Returns the maximum DC voltage the channel can switch in volts.

**Related topics**

- General Switching Considerations
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumswitchingaccurrent.html language=enus -->
## TOPIC 00038: Module Characteristics:Maximum Switching AC Current Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumswitchingaccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumswitchingaccurrent.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Switching AC Current Property

**Short Name:**Maximum Switching AC Current

Property of [niSwitch](cniswitch.html)

Returns the maximum AC current the channel can switch in amperes RMS.

**Related topics**

- niSwitch Properties
- Switching Current

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumswitchingacpower.html language=enus -->
## TOPIC 00039: Module Characteristics:Maximum Switching AC Power Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumswitchingacpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumswitchingacpower.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Switching AC Power Property

**Short Name:**Maximum Switching AC Power

Property of [niSwitch](cniswitch.html)

Returns the maximum AC power the channel can switch in volt-amperes.

**Related topics**

- niSwitch Properties
- Switching Power

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumswitchingdccurrent.html language=enus -->
## TOPIC 00040: Module Characteristics:Maximum Switching DC Current Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumswitchingdccurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumswitchingdccurrent.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Switching DC Current Property

**Short Name:**Maximum Switching DC Current

Property of [niSwitch](cniswitch.html)

Returns the maximum DC current the channel can switch in amperes.

**Related topics**

- niSwitch Properties
- Switching Current

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_maximumswitchingdcpower.html language=enus -->
## TOPIC 00041: Module Characteristics:Maximum Switching DC Power Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_maximumswitchingdcpower.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_maximumswitchingdcpower.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Maximum Switching DC Power Property

**Short Name:**Maximum Switching DC Power

Property of [niSwitch](cniswitch.html)

Returns the maximum DC power the channel can switch in watts.

**Related topics**

- niSwitch Properties
- Switching Power

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_model.html language=enus -->
## TOPIC 00042: Inherent IVI Attributes:Instrument Identification:Model Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_model.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_model.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Instrument Identification:Model Property

**Short Name:**Model

Property of [niSwitch](cniswitch.html)

Contains the model number or name of the instrument currently in use.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_numberofcolumns.html language=enus -->
## TOPIC 00043: Matrix Configuration:Number of Columns Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_numberofcolumns.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_numberofcolumns.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Matrix Configuration:Number of Columns Property

**Short Name:**Number of Columns

Property of [niSwitch](cniswitch.html)

Returns the number of channels on the column of a matrix or scanner. If the switch module is a scanner, this property returns the number of input channels.

The [Wire mode](pniswitch_wiremode.html) property affects the number of available columns. For example, if your switch module has eight input lines and you use the 4-wire mode, then the number of columns available is two.

**Related topics**

- Matrix
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_numberofrelays.html language=enus -->
## TOPIC 00044: Module Characteristics:Number of Relays Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_numberofrelays.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_numberofrelays.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Number of Relays Property

**Short Name:**Number of Relays

Property of [niSwitch](cniswitch.html)

Returns the number of relays that the instrument driver supports.

**Related topics**

- niSwitch Get Relay Name
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_numberofrows.html language=enus -->
## TOPIC 00045: Matrix Configuration:Number of Rows Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_numberofrows.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_numberofrows.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Matrix Configuration:Number of Rows Property

**Short Name:**Number of Rows

Property of [niSwitch](cniswitch.html)

Returns the number of channels on the row of a matrix or scanner. If the switch module is a scanner, this property returns the number of output channels.

The [Wire mode](pniswitch_wiremode.html) property affects the number of available rows. For example, if your switch module has eight input lines and you use the 2-wire mode, then the number of columns you have available is four.

**Related topics**

- Matrix
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_parsedscanlist.html language=enus -->
## TOPIC 00046: Obsolete Attributes:Parsed Scan List Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_parsedscanlist.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_parsedscanlist.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Parsed Scan List Property

**Short Name:**Parsed Scan List

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_powerdownlatchingrelaysafterdebounce.html language=enus -->
## TOPIC 00047: Module Characteristics:Power Down Latching Relays After Debounce Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_powerdownlatchingrelaysafterdebounce.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_powerdownlatchingrelaysafterdebounce.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Power Down Latching Relays After Debounce Property

**Short Name:**Power Down Latching Relays After Debounce

Property of [niSwitch](cniswitch.html)

Specifies whether to power down latching relays after calling the [niSwitch Wait For Debounce](/csh?topicname=switchviref/niswitch_wait_for_debounce.html) VI. Set this property to TRUE to ensure that the relays settle and the latching relays power down after you call the [niSwitch Wait for Debounce](/csh?topicname=switchviref/niswitch_wait_for_debounce.html) VI.

**Related topics**

- Armature Relays
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_queryinstrumentstatus.html language=enus -->
## TOPIC 00048: Inherent IVI Attributes:User Options:Query Instrument Status Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_queryinstrumentstatus.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_queryinstrumentstatus.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Query Instrument Status Property

**Short Name:**Query Instrument Status

Property of [niSwitch](cniswitch.html)

Specifies whether the instrument driver queries the instrument status after each operation. The default value is TRUE. Use the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI to override the default value.

Querying the instrument status is useful for debugging. After you validate your program, set this property to FALSE to disable status checking and maximize performance.
 The instrument driver can choose to ignore status checking for particular properties regardless of the setting of this property.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_rangecheck.html language=enus -->
## TOPIC 00049: Inherent IVI Attributes:User Options:Range Check Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_rangecheck.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_rangecheck.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Range Check Property

**Short Name:**Range Check

Property of [niSwitch](cniswitch.html)

Specifies whether to validate property values and VI parameters. The default value is TRUE. Use the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI to override the default value.

Set this property to TRUE to validate the parameter values that you pass to instrument driver VIs. Range checking parameters is useful for debugging. After validating your program, set this property to FALSE to disable range checking and maximize performance.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_recordvaluecoercions.html language=enus -->
## TOPIC 00050: Inherent IVI Attributes:User Options:Record Value Coercions Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_recordvaluecoercions.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_recordvaluecoercions.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Record Value Coercions Property

**Short Name:**Record Value Coercions

Property of [niSwitch](cniswitch.html)

Specifies whether the IVI engine keeps a list of the value coercions it makes for properties with ViInt32 and ViReal64 datatypes. The default value is FALSE. Use the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI to override the default value.

Call [niSwitch Get Next Coercion Record](/csh?topicname=switchviref/niswitch_get_next_coercion_record.html) VI to extract and delete the oldest coercion record from the list.

**Related topics**

- niSwitch Get Next Coercion Record
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_revision.html language=enus -->
## TOPIC 00051: Inherent IVI Attributes:Driver Identification:Revision Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_revision.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_revision.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Identification:Revision Property

**Short Name:**Revision

Property of [niSwitch](cniswitch.html)

Contains additional version information about the instrument driver.

**Related topics**

- niSwitch Properties
- niSwitch Revision Query VI

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_scanadvancedoutput.html language=enus -->
## TOPIC 00052: Scanning Configuration:Scan Advanced Output Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_scanadvancedoutput.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_scanadvancedoutput.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Scan Advanced Output Property

**Short Name:**Scan Advanced Output

Property of [niSwitch](cniswitch.html)

Specifies the method to use to notify another instrument that all signals through the switch module have settled following the processing of one entry in the scan list.

**Related topics**

- niSwitch Properties
- Scanning

| NONE (0) | The switch module does not produce a Scan Advanced Output trigger. |
| --- | --- |
| EXTERNAL (2) | The switch module produces the Scan Advanced Output trigger on the external trigger output. |
| PXI_Trig0 (111) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig0 line before processing the next entry in the scan list. |
| PXI_Trig1 (112) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig1 line before processing the next entry in the scan list. |
| PXI_Trig2 (113) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig2 line before processing the next entry in the scan list. |
| PXI_Trig3 (114) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig3 line before processing the next entry in the scan list. |
| PXI_Trig4 (115) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig4 line before processing the next entry in the scan list. |
| PXI_Trig5 (116) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig5 line before processing the next entry in the scan list. |
| PXI_Trig6 (117) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig6 line before processing the next entry in the scan list. |
| PXI_Trig7 (118) | The switch module produces the Scan Advanced Output Trigger on the PXI_Trig7 line before processing the next entry in the scan list. |
| PXI_STAR (125) | The switch module produces the Scan Advanced Output Trigger on the PXI Star trigger bus before processing the next entry in the scan list. |
| REARCONNECTOR (1000) | The switch module produces the Scan Advanced Output Trigger on the rear connector. |
| REARCONNECTOR_MODULE1 (1021) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 1. |
| REARCONNECTOR_MODULE2 (1022) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 2. |
| REARCONNECTOR_MODULE3 (1023) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 3. |
| REARCONNECTOR_MODULE4 (1024) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 4. |
| REARCONNECTOR_MODULE5 (1025) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 5. |
| REARCONNECTOR_MODULE6 (1026) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 6. |
| REARCONNECTOR_MODULE7 (1027) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 7. |
| REARCONNECTOR_MODULE8 (1028) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 8. |
| REARCONNECTOR_MODULE9 (1029) | The switch module produces the Scan Advanced Ouptut Trigger on the rear connector module 9. |
| REARCONNECTOR_MODULE10 (1030) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 10. |
| REARCONNECTOR_MODULE11 (1031) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 11. |
| REARCONNECTOR_MODULE12 (1032) | The switch module produces the Scan Advanced Output Trigger on the rear connector module 12. |
| FRONTCONNECTOR (1001) | The switch module produces the Scan Advanced Output Trigger on the front connector. |
| FRONTCONNECTOR_MODULE1 (1041) | The switch module produces the Scan Advanced Output Trigger on the front connector module 1. |
| FRONTCONNECTOR_MODULE2 (1042) | The switch module produces the Scan Advanced Output Trigger on the front connector module 2. |
| FRONTCONNECTOR_MODULE3 (1043) | The switch module produces the Scan Advanced Output Trigger on the front connector module 3. |
| FRONTCONNECTOR_MODULE4 (1044) | The switch module produces the Scan Advanced Output Trigger on the front connector module 4. |
| FRONTCONNECTOR_MODULE5 (1045) | The switch module produces the Scan Advanced Output Trigger on the front connector module 5. |
| FRONTCONNECTOR_MODULE6 (1046) | The switch module produces the Scan Advanced Output Trigger on the front connector module 6. |
| FRONTCONNECTOR_MODULE7 (1047) | The switch module produces the Scan Advanced Output Trigger on the front connector module 7. |
| FRONTCONNECTOR_MODULE8 (1048) | The switch module produces the Scan Advanced Output Trigger on the front connector module 8. |
| FRONTCONNECTOR_MODULE9 (1049) | The switch module produces the Scan Advanced Output Trigger on the front connector module 9. |
| FRONTCONNECTOR_MODULE10 (1050) | The switch module produces the Scan Advanced Output Trigger on the front connector module 10. |
| FRONTCONNECTOR_MODULE11 (1051) | The switch module produces the Scan Advanced Output Trigger on the front connector module 11. |
| FRONTCONNECTOR_MODULE12 (1052) | The switch module produces the Scan Advanced Output Trigger on the front connector module 12. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_scanadvancedpolarity.html language=enus -->
## TOPIC 00053: Scanning Configuration:Scan Advanced Polarity Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_scanadvancedpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_scanadvancedpolarity.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Scan Advanced Polarity Property

**Short Name:**Scan Advanced Polarity

Property of [niSwitch](cniswitch.html)

Specifies the driving level for the Scan Advanced Output signal sent from the switch module through either the external (PXI/PXIe) or front connector (SCXI) lines. 

When the Scan Advanced Output signal is sent to one of the PXI_Trig lines, the driven level is always low and this property is ignored. Between each Scan Advanced Output signal, the line is not driven and is in a high-impedance state.

**Related topics**

- niSwitch Properties
- Scanning

| RISING_EDGE (0) | The trigger occurs on the rising edge of the signal. |
| --- | --- |
| FALLING_EDGE (1) | The trigger occurs on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_scandelay.html language=enus -->
## TOPIC 00054: Scanning Configuration:Scan Delay Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_scandelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_scandelay.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Scan Delay Property

**Short Name:**Scan Delay

Property of [niSwitch](cniswitch.html)

Specifies the minimum amount of time the switch module waits before it asserts the scan advanced output trigger after opening or closing the switch. The switch module always waits for debounce before asserting the trigger. Thus, the actual delay will always be the greater value of the settling time and the value you specify as the switch delay, measured in seconds.
Settling time can vary depending on the switch module.

**Related topics**

- niSwitch Properties
- Scanning

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_scanlist.html language=enus -->
## TOPIC 00055: Scanning Configuration:Scan List Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_scanlist.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_scanlist.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Scan List Property

**Short Name:**Scan List

Property of [niSwitch](cniswitch.html)

Contains a scan list (a string that specifies channel connections and trigger conditions). The [niSwitch Initiate Scan](/csh?topicname=switchviref/niswitch_initiate_scan.html) VI makes or breaks connections and waits for triggers according to the instructions in the scan list.
 The scan list is comprised of channel names separated by special characters that determine the operations the scanner performs on the channels when it executes the scan list.

To create a path between two channels, use the following character between the two channel names:
 -> (a dash followed by a '>' sign)
Example: 'CH1->CH2' tells the switch to make a path from channel CH1 to channel CH2.

To break or clear a path, use the following character as a prefix before the path:
 ~ (tilde)
Example: '~CH1->CH2' tells the switch to break the path from channel CH1 to channel CH2.

To tell the switch module to wait for a trigger event, use the following character as a separator between paths:
 ; (semi-colon)
Example: 'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1 to channel CH2, wait for a trigger, and then make the path from CH3 to CH4.

To tell the switch module to create multiple paths as quickly as possible, use the & (ampersand) or && (double ampersand) as a separator between the paths. The & in 'CH0->CH1;CH2->CH3&CH4->CH5' instructs the scanner to make the path between channels CH0 and CH1, wait for a trigger, and then make the paths between channels CH2 and CH3 and between channels CH4 and CH5 in no particular order without waiting for settling or waiting for a trigger. If wait for settling is desired, replace & with &&. The && in 'CH0->CH1;CH2->CH3&&CH4->CH5' instructs the scanner to make the path between channels CH0 and CH1, wait for a trigger, and then make the path between channels CH2 and CH3, wait for settling, then make the path between channels CH4 and CH5.

**Related topics**

- niSwitch Properties
- Scan Lists
- Scanning

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_scanmode.html language=enus -->
## TOPIC 00056: Scanning Configuration:Scan Mode Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_scanmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_scanmode.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Scan Mode Property

**Short Name:**Scan Mode

Property of [niSwitch](cniswitch.html)

Specifies how to handle existing connections that conflict with the connections you make in a scan list. For example, if CH1 is already connected to CH2 and the scan list instructs the switch module to connect CH1 to CH3, this property specifies what happens to the connection between CH1 and CH2.

Set the property value to **None** to make the switch module take no action on existing paths. Set the value to **Break Before Make** to make the switch module break conflicting paths before making new ones. Set the value to **Break After Make** to make the switch module break conflicting paths after making new ones.
 Most switch modules support only one of the possible values: in such cases, this property serves as an indicator of the module's behavior.

**Related topics**

- niSwitch Properties
- Scanning

| NONE (0) | No implicit action on connections when scanning. |
| --- | --- |
| BREAK_BEFORE_MAKE (1) | When scanning, the switch module breaks existing connections before making new connections. |
| BREAK_AFTER_MAKE (2) | When scanning, the switch module breaks existing connections after making new connections. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_serialnumber.html language=enus -->
## TOPIC 00057: Module Characteristics:Serial Number Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_serialnumber.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_serialnumber.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Serial Number Property

**Short Name:**Serial Number

Property of [niSwitch](cniswitch.html)

Returns the serial number for the switch module controlled by the instrument driver. If the switch module does not return a serial number, the instrument driver returns the Invalid Attribute error.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_serialnumber_i32.html language=enus -->
## TOPIC 00058: Obsolete Attributes:Serial Number Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_serialnumber_i32.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_serialnumber_i32.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Serial Number Property

**Short Name:**Serial Number (I32)

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_settlingtime.html language=enus -->
## TOPIC 00059: Module Characteristics:Settling Time Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_settlingtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_settlingtime.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Settling Time Property

**Short Name:**Settling Time

Property of [niSwitch](cniswitch.html)

Returns the maximum length of time in seconds from after you make a connection until the signal flowing through the channel settles. 
Settling time can vary depending on the switch module.

**Related topics**

- niSwitch Properties
- Settling Time

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_simulate.html language=enus -->
## TOPIC 00060: Inherent IVI Attributes:User Options:Simulate Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_simulate.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_simulate.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:User Options:Simulate Property

**Short Name:**Simulate

Property of [niSwitch](cniswitch.html)

Specifies whether to simulate instrument driver I/O operations. The default value is FALSE. Use the [niSwitch Initialize With Options](/csh?topicname=switchviref/niswitch_initialize_with_options.html) VI to override the default value.

Set this property to TRUE to perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute functions without performing instrument I/O. For output parameters that represent instrument data, the instrument driver VIs return calculated values.

**Related topics**

- niSwitch Properties
- Simulating a Switch

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_supportedinstrumentmodels.html language=enus -->
## TOPIC 00061: Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_supportedinstrumentmodels.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_supportedinstrumentmodels.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models Property

**Short Name:**Supported Instrument Models

Property of [niSwitch](cniswitch.html)

Contains a comma-separated (,) list of supported instrument models.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_temperature.html language=enus -->
## TOPIC 00062: Module Characteristics:Temperature Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_temperature.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_temperature.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Temperature Property

**Short Name:**Temperature

Property of [niSwitch](cniswitch.html)

Returns the temperature as read by the Switch module in degrees Celsius. Refer to the device documentation for more information.

**Related topics**

- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_triggerinput.html language=enus -->
## TOPIC 00063: Scanning Configuration:Trigger Input Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_triggerinput.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_triggerinput.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Trigger Input Property

**Short Name:**Trigger Input

Property of [niSwitch](cniswitch.html)

Specifies the source of the trigger for which the switch module can wait upon encountering a semi-colon (;) when processing a scan list. When the trigger occurs, the switch module advances to the next entry in the scan list.

**Related topics**

- niSwitch Configure Scan List
- niSwitch Properties
- Scanning

| IMMEDIATE (1) | The switch module does not wait for a trigger before processing the next entry in the scan list. |
| --- | --- |
| SW_TRIG_FUNC (3) | The switch module waits until you call the niSwitch Send Software Trigger VI before processing the next entry in the scan list. |
| EXTERNAL (2) | The switch module waits until it receives a trigger from an external source through the external trigger input before processing the next entry in the scan list. |
| PXI_Trig0 (111) | The switch module waits until it receives a trigger on the PXI_Trig0 line before processing the next entry in the scan list. |
| PXI_Trig1 (112) | The switch module waits until it receives a trigger on the PXI_Trig1 line before processing the next entry in the scan list. |
| PXI_Trig2 (113) | The switch module waits until it receives a trigger on the PXI_Trig2 line before processing the next entry in the scan list. |
| PXI_Trig3 (114) | The switch module waits until it receives a trigger on the PXI_Trig3 line before processing the next entry in the scan list. |
| PXI_Trig4 (115) | The switch module waits until it receives a trigger on the PXI_Trig4 line before processing the next entry in the scan list. |
| PXI_Trig5 (116) | The switch module waits until it receives a trigger on the PXI_Trig5 line before processing the next entry in the scan list. |
| PXI_Trig6 (117) | The switch module waits until it receives a trigger on the PXI_Trig6 line before processing the next entry in the scan list. |
| PXI_Trig7 (118) | The switch module waits until it receives a trigger on the PXI_Trig7 line before processing the next entry in the scan list. |
| PXI_STAR (125) | The switch module waits until it receives a trigger on the PXI star trigger bus before processing the next entry in the scan list. |
| REARCONNECTOR (1000) | The switch module waits until it receives a trigger on the rear connector. |
| FRONTCONNECTOR (1001) | The switch module waits until it receives a trigger on the front connector. |
| REARCONNECTOR_MODULE1 (1021) | The switch module waits until it receives a trigger on the rear connector module 1. |
| REARCONNECTOR_MODULE2 (1022) | The switch module waits until it receives a trigger on the rear connector module 2. |
| REARCONNECTOR_MODULE3 (1023) | The switch module waits until it receives a trigger on the rear connector module 3. |
| REARCONNECTOR_MODULE4 (1024) | The switch module waits until it receives a trigger on the rear connector module 4. |
| REARCONNECTOR_MODULE5 (1025) | The switch module waits until it receives a trigger on the rear connector module 5. |
| REARCONNECTOR_MODULE6 (1026) | The switch module waits until it receives a trigger on the rear connector module 6. |
| REARCONNECTOR_MODULE7 (1027) | The switch module waits until it receives a trigger on the rear connector module 7. |
| REARCONNECTOR_MODULE8 (1028) | The switch module waits until it receives a trigger on the rear connector module 8. |
| REARCONNECTOR_MODULE9 (1029) | The switch module waits until it receives a trigger on the rear connector module 9. |
| REARCONNECTOR_MODULE10 (1030) | The switch module waits until it receives a trigger on the rear connector module 10. |
| REARCONNECTOR_MODULE11 (1031) | The switch module waits until it receives a trigger on the rear connector module 11. |
| REARCONNECTOR_MODULE12 (1032) | The switch module waits until it receives a trigger on the rear connector module 12. |
| FRONTCONNECTOR_MODULE1 (1041) | The switch module waits until it receives a trigger on the front connector module 1. |
| FRONTCONNECTOR_MODULE2 (1042) | The switch module waits until it receives a trigger on the front connector module 2. |
| FRONTCONNECTOR_MODULE3 (1043) | The switch module waits until it receives a trigger on the front connector module 3. |
| FRONTCONNECTOR_MODULE4 (1044) | The switch module waits until it receives a trigger on the front connector module 4. |
| FRONTCONNECTOR_MODULE5 (1045) | The switch module waits until it receives a trigger on the front connector module 5. |
| FRONTCONNECTOR_MODULE6 (1046) | The switch module waits until it receives a trigger on the front connector module 6. |
| FRONTCONNECTOR_MODULE7 (1047) | The switch module waits until it receives a trigger on the front connector module 7. |
| FRONTCONNECTOR_MODULE8 (1048) | The switch module waits until it receives a trigger on the front connector module 8. |
| FRONTCONNECTOR_MODULE9 (1049) | The switch module waits until it receives a trigger on the front connector module 9. |
| FRONTCONNECTOR_MODULE10 (1050) | The switch module waits until it receives a trigger on the front connector module 10. |
| FRONTCONNECTOR_MODULE11 (1051) | The switch module waits until it receives a trigger on the front connector module 11. |
| FRONTCONNECTOR_MODULE12 (1052) | The switch module waits until it receives a trigger on the front connector module 12. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_triggerinputpolarity.html language=enus -->
## TOPIC 00064: Scanning Configuration:Trigger Input Polarity Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_triggerinputpolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_triggerinputpolarity.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Scanning Configuration:Trigger Input Polarity Property

**Short Name:**Trigger Input Polarity

Property of [niSwitch](cniswitch.html)

Determines the behavior of the trigger input.

**Related topics**

- niSwitch Properties
- Scanning

| RISING_EDGE (0) | The trigger occurs on the rising edge of the signal. |
| --- | --- |
| FALLING_EDGE (1) | The trigger occurs on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_triggermode.html language=enus -->
## TOPIC 00065: Obsolete Attributes:Trigger Mode Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_triggermode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_triggermode.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Obsolete Attributes:Trigger Mode Property

**Short Name:**Trigger Mode

Property of [niSwitch](cniswitch.html)

This property has been deprecated and might be removed from a future release of NI-SWITCH. Use the [niSwitch Route Trigger Input](/csh?topicname=switchviref/niswitch_route_trigger_input.html) and/or [niSwitch Route Scan Advanced Output](/csh?topicname=switchviref/niswitch_route_scan_advanced_output.html) VIs instead.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-switch-properties path=switchpropref/pniswitch_wiremode.html language=enus -->
## TOPIC 00066: Module Characteristics:Wire mode Property

- bundle_id: `ni-switch-properties`
- source_path: `switchpropref/pniswitch_wiremode.html`
- source_url: https://docs-be.ni.com/bundle/ni-switch-properties/raw/resource/enus/switchpropref/pniswitch_wiremode.html
- document_id: `ni-switch-properties`
- page_type: `leaf`
- content_type: ``

### Module Characteristics:Wire mode Property

**Short Name:**Wire mode

Property of [niSwitch](cniswitch.html)

Returns the wire mode of the switch module.
 This property affects the values of the [Number of Rows](pniswitch_numberofrows.html) and [Number of Columns](pniswitch_numberofcolumns.html) properties. The actual number of input and output lines on the switch module does not change, but the number of channels depends on how many lines constitute each channel.

**Related topics**

- N-Wire Switching Modes
- niSwitch Properties

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| Channel-based | Yes |
| Resettable | No |
